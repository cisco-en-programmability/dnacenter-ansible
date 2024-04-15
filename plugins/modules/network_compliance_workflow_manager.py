
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
import time

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Rugvedi Kapse")


DOCUMENTATION = r"""
---
module: network_compliance_workflow_manager
short_description: 
description:
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Rugvedi Kapse (@rukapse)
options:
  config:



"""

EXAMPLES = r"""
- name: 
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: "{{dnac_log}}"
    config:


"""

RETURN = r"""
#Case_1:

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
)

class NetworkCompliance(DnacBase):
    """Class containing member attributes for network_compliance_workflow_manager module"""

    def __init__(self, module):
        """
        Initialize an instance of the class. 

        Parameters:
          - module: The module associated with the class instance.

        Returns:
          The method does not return a value.
        """

        super().__init__(module)


    def validate_input(self, state=None):
        """
        Validate the fields provided in the playbook.  Checks the
        configuration provided in the playbook against a predefined
        specification to ensure it adheres to the expected structure
        and data types.

        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either 'success' or 'failed').
          - self.validated_config: If successful, a validated version of the
                                   'config' parameter.
        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            self.log(self.msg, "ERROR")
            return self

        temp_spec = {
            'ip_address_list': {'type': 'list', 'elements': 'str', 'required': False},
            'site_name': {'type': 'str', 'required': False},
            'run_compliance': {'type': 'dict','required': False},
            'sync_device_config': {'type': 'bool', 'required': False, 'default': False},
        }

        # Validate device params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_temp

        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def validate_ip4_address_list(self, ip_address_list):
        """
        Validates the IP address list provided in the playbook. 
        """
        for ip in ip_address_list:
            if not self.is_valid_ipv4(ip):
                msg = "IP address {0} is not valid".format(ip)
                self.log(msg, "ERROR")
                self.module.fail_json(msg)
                
        self.log("Successfully validated the IP address/es: {0}", "DEBUG")

    def validate_run_compliance(self, run_compliance):
        trigger_full = run_compliance.get('trigger_full')
        categories = run_compliance.get('categories')

        if not trigger_full or not categories:
            self.log("Both trigger_full and categories are required parameters for running compliance.", "ERROR")
            self.status = "failed"
            return self

        for category in categories:
            if category.upper() not in ['RUNNING_CONFIG', 'INTENT']:
                self.log(f"Invalid category provided: {category}. Valid categories are 'RUNNING_CONFIG' or 'INTENT'.", "ERROR")
                self.status = "failed"
                return self
        
        self.log("Successfully validated run_compliance parameters.", "DEBUG")


    def site_exists(self, site_name):
        """
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            tuple: A tuple containing two values:
            - site_exists (bool): A boolean indicating whether the site exists (True) or not (False).
            - site_id (str or None): The ID of the site if it exists, or None if the site is not found.
        Description:
            This method checks the existence of a site in the Catalyst Center. If the site is found,it sets 'site_exists' to True,
            retrieves the site's ID, and returns both values in a tuple. If the site does not exist, 'site_exists' is set
            to False, and 'site_id' is None. If an exception occurs during the site lookup, an exception is raised.
        """

        site_exists = False
        site_id = None
        response = None
        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                op_modifies=True,
                params={"name": site_name},
            )
        except Exception as e:
            self.msg = "An exception occurred: Site '{0}' does not exist in the Cisco Catalyst Center".format(site_name)
            self.log(self.msg, "ERROR")
            self.module.fail_json(msg=self.msg)

        if response:
            self.log("Received API response from 'get_site': {0}".format(str(response)), "DEBUG")
            site = response.get("response")
            site_id = site[0].get("id")
            site_exists = True

        return (site_exists, site_id)

    def get_device_ids_from_ip(self, ip_address_list):
        mgmt_ip_instance_id_map = {}
        for device_ip in ip_address_list:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    op_modifies=True,
                    params={"managementIpAddress": device_ip}
                )

                if response:
                    self.log("Received API response from 'get_device_list' for device: {0}".format(str(response)), "DEBUG")
                    response = response.get("response")
                    if not response:
                        continue
                    for device_info in response:
                        if device_info["reachabilityStatus"] == "Reachable":
                            device_id = response[0]["id"]
                            mgmt_ip_instance_id_map[device_ip] = device_id

            except Exception as e:
                error_message = "Error while fetching device ID for device: '{0}' from Cisco Catalyst Center: {1}".format(device_ip, str(e))
                self.log(error_message, "ERROR")

        return mgmt_ip_instance_id_map

    def get_device_ids_from_site(self, site_name, site_id):
        #device_id_list = []
        mgmt_ip_instance_id_map = {}

        site_params = {
            "site_id": site_id,
        }

        #Get 
        try:
            response = self.dnac._exec(
                family="sites",
                function='get_membership',
                op_modifies=True,
                params=site_params,
            )
            if response:
                self.log("Received API response from 'get_membership': {0}".format(str(response)), "DEBUG")
                site_response_list = []
                for item in response['device']:
                    if item['response']:
                        for item_dict in item['response']:
                            site_response_list.append(item_dict)

        except Exception as e:
            self.log("Unable to fetch the device(s) associated to the site '{0}' due to '{1}'".format(site_name, str(e)), "WARNING")
            return device_id_list

        self.log("Received API response from 'get_membership': {0}".format(str(response)), "DEBUG")
        response = response['device']
        
        # Iterate over the devices in the site membership
        for item in response:
            if item['response']:
                for item_dict in item['response']:
                    # Check if the device is reachable
                    if item_dict["reachabilityStatus"] == "Reachable":
                        #device_id_list.append(item_dict["instanceUuid"])
                        mgmt_ip_instance_id_map[item_dict["managementIpAddress"]] = item_dict["instanceUuid"]
                    else:
                        msg = 'Unable to get deviceId  for device {0} in site {1} as its status is {2}'.format(
                        item["managementIpAddress"], site_name, item["reachabilityStatus"])
                        self.log(msg, "CRITICAL")
                        self.module.fail_json(msg=msg)

        if not mgmt_ip_instance_id_map:
            msg = 'Site: {0} provided in the playbook does not have any reachable devices'.format(site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        return mgmt_ip_instance_id_map

    def get_device_id_list(self, ip_address_list, site_name):
        """
        Get the list of unique device IDs for list of specified management IP addresses of devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ips (list): The management IP addresses of devices for which you want to retrieve the device IDs.
        Returns:
            list: The list of unique device IDs for the specified devices.
        Description:
            Queries Cisco Catalyst Center to retrieve the unique device ID associated with a device having the specified
            IP address. If the device is not found in Cisco Catalyst Center, then print the log message with error severity.
        """
        if site_name and ip_address_list:
            (site_exists, site_id) = self.site_exists(site_name)
            if site_exists:
                site_mgmt_ip_instance_id_map  = self.get_device_ids_from_site(site_name, site_id)
            iplist_mgmt_ip_instance_id_map = self.get_device_ids_from_ip(ip_address_list)
            mgmt_ip_instance_id_map = {
                ip: instance_id 
                for ip, instance_id in iplist_mgmt_ip_instance_id_map.items() 
                if ip in site_mgmt_ip_instance_id_map
            }
        elif site_name and not ip_address_list:
            (site_exists, site_id) = self.site_exists(site_name)
            if site_exists:
                mgmt_ip_instance_id_map  = self.get_device_ids_from_site(site_id)
        elif ip_address_list and not site_name:
            mgmt_ip_instance_id_map = self.get_device_ids_from_ip(ip_address_list)
            

        return mgmt_ip_instance_id_map

    def get_want(self, config):
        """
        """

        #Validate either ip_address_list OR site_name is present
        ip_address_list = config.get('ip_address_list')
        site_name = config.get('site_name')

        if not ip_address_list and not site_name:
            msg = 'ip_address_list is {} and site_name is {}. Either the ip_address_list or the site_name must be provided.'.format(ip_address_list, site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        #Validate valid ip_addresses
        if ip_address_list:
            self.validate_ip4_address_list(ip_address_list)
        
        mgmt_ip_instance_id_map = self.get_device_id_list(ip_address_list, site_name)
        self.log('Retrieved device_id_list : {0}'.format(mgmt_ip_instance_id_map), 'DEBUG')

        #Validate run_compliance parameters
        run_compliance = config.get('run_compliance')
        sync_device_config = config.get('sync_device_config')
        if run_compliance:
            self.validate_run_compliance(run_compliance)

            run_compliance_params = {
                'triggerFull': config.get('run_compliance').get('trigger_full'),
                'categories': config.get('run_compliance').get('categories'), 
                'deviceUuids': list(mgmt_ip_instance_id_map.values()),    
            }
        else:
            run_compliance_params = {}

        if sync_device_config:
            sync_device_config_params = {
                'deviceId': list(mgmt_ip_instance_id_map.values())

            }
        else:
            sync_device_config_params = {}

        want = {}
        want = dict(
            ip_address_list = ip_address_list,
            site_name = site_name,
            mgmt_ip_instance_id_map = mgmt_ip_instance_id_map,
            run_compliance_params=run_compliance_params,
            sync_device_config_params=sync_device_config_params
        )
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self


    def run_compliance(self, run_compliance_params):

        result = self.dnac_apply['exec'](
            family="compliance",
            function="run_compliance",
            params=run_compliance_params,
            op_modifies=True,
        )

        self.log("The response received post Run Compliance API call is {0}".format(str(result)), "DEBUG")

        self.result.update(dict(run_compliance_result=result))
        self.log("Task Id of the API task created is {0}".format(result.response.get('taskId')), "INFO")
        return result.response.get('taskId')

    def sync_device_config(self, sync_device_config_params):
        result = self.dnac_apply['exec'](
            family="compliance",
            function="commit_device_configuration",
            params=sync_device_config_params,
            op_modifies=True,
        )

        self.log("The response received post Commit Configuration API call is {0}".format(str(result)), "DEBUG")

        self.result.update(dict(sync_device_configuration_result=result))
        self.log("Task Id of the API task created is {0}".format(result.response.get('taskId')), "INFO")
        return result.response.get('taskId')

    def get_merged_task_status(self, task_id, task_name, ip_address_list):
        result = False
        params = dict(task_id=task_id)
        start_time = time.time()
        while True:

            # Check if the elapsed time exceeds the timeout
            if time.time() - start_time > 300:
                self.log("Task {0} with task id {1} has not completed within the timeout period.".format(task_name, task_id), "CRITICAL")
                self.module.fail_json(msg="Task execution timed out.")
                break

            response = self.dnac_apply['exec'](
                family="task",
                function='get_task_by_id',
                params=params,
                op_modifies=True,
            )
            response = response.response
            self.log("Task status for the task id {0} is {1}, is_error: {2}".format(str(task_id), str(response), str(response.get('isError'))), "INFO")

            # Check for success status
            if not response.get('isError') and 'success' in response.get('progress').lower():
                self.log("Task {0} with task id {1} has completed successfully on device/s: {2} .".format(task_name, str(task_id), ip_address_list), "INFO")
                result = True

                self.status = "success"
                self.msg = "{0} has completed successfully on device/s: {1}".format(task_name, ip_address_list)
                self.result['response'] = self.msg
                self.result['changed'] = True
                self.result['status'] = "success"
                self.log(self.msg, "INFO")
                break  

            # Check for failed status
            if response.get('isError') or 'failed' in response.get('progress').lower():
                msg = 'Task {0} with task id {1} has not completed on device/s {2}- Reason: {3}'.format(
                    task_name, task_id, ip_address_list, response.get("failureReason"))
                self.log(msg, "CRITICAL")
                self.module.fail_json(msg=msg)
                break 

    def get_diff_merged(self):
        if self.want.get('run_compliance_params'):
            result_task_id = self.run_compliance(self.want.get('run_compliance_params'))
            self.get_merged_task_status(result_task_id, 'Run Compliance', list(self.want.get('mgmt_ip_instance_id_map').keys()))

        if self.want.get('sync_device_config_params'):
            result_task_id = self.sync_device_config(self.want.get('sync_device_config_params'))
            self.get_merged_task_status(result_task_id, 'Commit Device Configuration', list(self.want.get('mgmt_ip_instance_id_map').keys()))
        

def main():
    """ main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    ccc_network_compliance = NetworkCompliance(module)
    state = ccc_network_compliance.params.get("state")

    if state not in ccc_network_compliance.supported_states:
        ccc_network_compliance.status = "invalid"
        ccc_network_compliance.msg = "State {0} is invalid".format(state)
        ccc_network_compliance.check_return_status()

    ccc_network_compliance.validate_input().check_return_status()
    config_verify = ccc_network_compliance.params.get("config_verify")

    for config in ccc_network_compliance.validated_config:
        ccc_network_compliance.get_want(config)
        ccc_network_compliance.get_diff_merged()

    module.exit_json(**ccc_network_compliance.result)



if __name__ == "__main__":
    main()


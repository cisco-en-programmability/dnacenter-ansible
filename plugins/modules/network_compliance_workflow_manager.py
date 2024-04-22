#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform Network Compliance Operations on devices in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function
import time

__metaclass__ = type
__author__ = ("Rugvedi Kapse, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: network_compliance_workflow_manager
short_description: Network Compliance module for managing network compliance tasks on reachable device(s) in Cisco Catalyst Center. 
description:
- Perform compliance checks or sync configurations on reachable devices using IP Address(s) or Site.
- API to perform full compliance checks or specific category checks on reachable device(s).
- API to sync device configuration on device(s).
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Rugvedi Kapse (@rukapse)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [merged]
    default: merged
  config:
    description: List of device details for running a compliance check or synchronizing device configuration.
    type: list
    elements: dict
    required: True
    suboptions:
      ip_address_list: 
        description: List of IP addresses of devices to Run Compliance check on or Sync Device Configuration.
                     Either ip_address_list or site_name is required for module to execute.
                     If both ip_address_list and site_name are provided, ip_address_list takes precedence, and the operations are executed 
                     on devices that are in the ip_address_list, but only those from the specified site
        elements: str
        type: list
      site_name:
        description: When site_name is specified, the module executes the operation on all the devices located within the specified site.
                     This is a string value that should represent the complete hierarchical path of the site.
                     For example: "Global/USA/San Francisco/Building_2/floor_1"
                     Either site_name or ip_address_list is required for module to execute.
                     If both site_name and ip_address_list are provided, ip_address_list takes precedence, and the operations are executed 
                     on devices that are in the ip_address_list, but only those from the specified site
        type: str
      run_compliance:
        description: Configuration for running a compliance check on the devices specified in the ip_address_list.
        type: dict
        suboptions:
          trigger_full: 
            description: Determines if a full compliance check should be triggered.
                         This parameter is required when running a compliance check.
                         if it is True then compliance will be triggered for all categories. 
                         If it is False then compliance will be triggered for categories mentioned in categories section.
            required: This paramter is required in order to run compliance check on device(s).
            type: bool
            default: False
          categories: 
            description: Specifying compliance categories allows you to trigger compliance checks only for the mentioned categories.
                         Compliance's categories are required when trigger_full is set to False.
                         Category can have any value among ['INTENT', 'RUNNING_CONFIG' , 'IMAGE' , 'PSIRT' , 'EOX' , 'NETWORK_SETTINGS'].
                         Category 'INTENT' is mapped to compliance types: NETWORK_SETTINGS, NETWORK_PROFILE, WORKFLOW, FABRIC,APPLICATION_VISIBILITY.

            required: This parameter is required when trigger_full is set to False.
            type: bool
            default: False
      sync_device_config: 
        description: Determines whether to synchronize the device configuration on the devices specified in the ip_address_list.
                     This operation, known as "Sync device configuration," primarily addresses the status of the `RUNNING_CONFIG`.
                     If set to True, and if `RUNNING_CONFIG` status is non-compliant this operation would commit device running configuration 
                     to startup by issuing "write memory" to device.
        type: bool
        default: False

requirements:
- dnacentersdk == 2.6.10
- python >= 3.5
notes:
  - SDK Method used are
    compliance.Compliance.run_compliance
    compliance.Compliance.commit_device_configuration
    task.Task.get_task_by_id
    compliance.Compliance.get_compliance_detail
    
  - Paths used are
    post /dna/intent/api/v1/compliance/
    post /dna/intent/api/v1/network-device-config/write-memory
    get /dna/intent/api/v1/task/{taskId}
    get /dna/intent/api/v1/compliance/detail
"""

EXAMPLES = r"""
- name: Run full compliance check on device(s) in the ip_address_list
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - ip_address_list: ['204.1.2.2', '204.1.2.5', '204.1.2.4']
          run_compliance:
             trigger_full: True

- name: Run full compliance check on device(s) in the site 
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - site_name: "Global/USA/San Francisco/Building_1/floor_1"
          run_compliance:
             trigger_full: True

- name: Run full compliance check on device(s) with both ip_address_list and site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - ip_address_list: ['204.1.2.2', '204.1.2.5', '204.1.2.4']
          site_name: "Global/USA/San Francisco/Building_1/floor_1"
          run_compliance:
             trigger_full: True

- name: Run compliance check with specific categories on device(s) in the ip_address_list 
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - ip_address_list: ['204.1.2.2', '204.1.2.5', '204.1.2.4']
          run_compliance:
             trigger_full: False
             categories: ['INTENT', 'RUNNING_CONFIG' , 'IMAGE' , 'PSIRT']

- name: Run compliance check with specific categories on device(s) in the site 
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - site_name: "Global/USA/San Francisco/Building_1/floor_1"
          run_compliance:
             trigger_full: False
             categories: ['INTENT', 'RUNNING_CONFIG' , 'IMAGE' , 'PSIRT']

- name: Run compliance check with specific categories on device(s) with both ip_address_list and site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - ip_address_list: ['204.1.2.2', '204.1.2.5', '204.1.2.4']
          site_name: "Global/USA/San Francisco/Building_1/floor_1"
          run_compliance:
             trigger_full: False
             categories: ['INTENT', 'RUNNING_CONFIG' , 'IMAGE' , 'PSIRT']

- name: Sync device configuration on device(s) in the ip_address_list 
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - site: "Global"
          sync_device_config: True

- name: Sync device configuration on device(s) in the site 
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - site_name: "Global/USA/San Francisco/Building_1/floor_1"
          sync_device_config: True

- name: Sync device configuration on device(s) with both ip_address_list and site 
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - ip_address_list: ['204.1.2.2', '204.1.2.5', '204.1.2.4']
          site_name: "Global/USA/San Francisco/Building_1/floor_1"
          sync_device_config: True

- name: Run Compliance and sync configuration with both ip_address_list and site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
      config:
        - ip_address_list: ['204.1.2.2', '204.1.2.5', '204.1.2.4']
          site_name: "Global/USA/San Francisco/Building_1/floor_1"
          run_compliance:
             trigger_full: False
             categories: ['INTENT', 'RUNNING_CONFIG' , 'IMAGE' , 'PSIRT']
          sync_device_config: True
"""

RETURN = r"""
#Case_1: 
dnac_response: 
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "changed": bool,
      "msg": "string"
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }

#Case_2: When compliance check is run, the response of the compliance status
dnac_response:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "changed": bool,
      "msg": "string"
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "data": [list of dictionaries],
      "version": "string"
    }

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
                
        self.log("Successfully validated the IP address/es: {0}".format(ip_address_list), "DEBUG")

    def validate_run_compliance(self, run_compliance):
        trigger_full = run_compliance.get('trigger_full')
        categories = run_compliance.get('categories')
        msg = ""
        if trigger_full not in [True, False]:
            msg = "trigger_full is a required parameter in order to run compliance check on device(s)"
        if trigger_full == False and not categories:
            msg = "Categories is a required paramtere when trigger_full is set to False."

        if categories and not all(category.upper() in ['INTENT','RUNNING_CONFIG' , 'IMAGE' , 'PSIRT' , 'EOX' , 'NETWORK_SETTINGS'] for category in categories):
            msg = "Invalid category provided. Valid categories are ['INTENT', 'RUNNING_CONFIG', 'IMAGE', 'PSIRT', 'EOX', 'NETWORK_SETTINGS']."

        if msg:
            self.log(msg, 'ERROR')
            self.module.fail_json(msg)
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

                if response.get("response"):
                    self.log("Received API response from 'get_device_list' for device:{0} response: {1}".format(device_ip, str(response)), "DEBUG")
                    response = response.get("response")
                    if not response:
                        continue
                    for device_info in response:
                        if device_info["reachabilityStatus"] == "Reachable":
                            device_id = response[0]["id"]
                            mgmt_ip_instance_id_map[device_ip] = device_id
                else:
                    self.msg = "Unable to retrieve device information for {0}. Please ensure that the device exists and is reachable.".format(device_ip)
                    self.log(self.msg, "ERROR")
                    self.module.fail_json(msg=self.msg)

            except Exception as e:
                error_message = "Error while fetching device ID for device: '{0}' from Cisco Catalyst Center: {1}".format(device_ip, str(e))
                self.log(error_message, "ERROR")

        return mgmt_ip_instance_id_map

    def get_device_ids_from_site(self, site_name, site_id):
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
                mgmt_ip_instance_id_map  = self.get_device_ids_from_site(site_name, site_id)
        elif ip_address_list and not site_name:
            mgmt_ip_instance_id_map = self.get_device_ids_from_ip(ip_address_list)
            

        return mgmt_ip_instance_id_map

    def get_want(self, config):
        """
        """
        run_compliance_params = {}
        sync_device_config_params = {}
        compliance_detail_params = {}


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
            run_compliance_params = {
                'triggerFull': config.get('run_compliance').get('trigger_full'),
                'deviceUuids': list(mgmt_ip_instance_id_map.values()),    
            }

            compliance_detail_params = {
                'deviceUuid': ','.join(list(mgmt_ip_instance_id_map.values())),
            }

            if config.get('run_compliance').get('categories'):
                categories_copy = config.get('run_compliance').get('categories').copy()
                run_compliance_params['categories'] = categories_copy

                compliance_types = config.get('run_compliance').get('categories')       
                if 'INTENT' in compliance_types:
                    compliance_types.remove('INTENT')
                    compliance_types.extend(['NETWORK_PROFILE', 'APPLICATION_VISIBILITY', 'WORKFLOW', 'FABRIC', 'NETWORK_SETTINGS'])
                compliance_types = list(set(compliance_types))
                compliance_detail_params['complianceType'] = "', '".join(compliance_types)
                compliance_detail_params['complianceType'] = "'" + compliance_detail_params['complianceType'] + "'"

        if sync_device_config:
            sync_device_config_params = {
                'deviceId': list(mgmt_ip_instance_id_map.values())
            }

            compliance_detail_params_sync = {
                'deviceUuid': ','.join(list(mgmt_ip_instance_id_map.values())),
                'complianceType': 'RUNNING_CONFIG'
            }


        want = {}
        want = dict(
            ip_address_list = ip_address_list,
            site_name = site_name,
            mgmt_ip_instance_id_map = mgmt_ip_instance_id_map,
            run_compliance_params=run_compliance_params,
            sync_device_config_params=sync_device_config_params,
            compliance_detail_params=compliance_detail_params,
            compliance_detail_params_sync=compliance_detail_params_sync
        )
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_compliance_detail(self, compliance_detail_params):
        response = self.dnac_apply['exec'](
                family="compliance",
                function='get_compliance_detail',
                params=compliance_detail_params,
                op_modifies=True,
            )
        response = response.response

        self.log("The response received post get_compliance_detail API call is {0}".format(str(response)), "DEBUG")
        return response

    def modify_compliance_response(self, response, mgmt_ip_instance_id_map):
        modified_response = {}

        for item in response:
            device_uuid = item.get('deviceUuid')
            ip_address = next((ip for ip, uuid in mgmt_ip_instance_id_map.items() if uuid == device_uuid), None)
            #if ip_address and item.get('status')!= 'NOT_APPLICABLE':
            if ip_address:
                if ip_address not in modified_response:
                    modified_response[ip_address] = []
                modified_response[ip_address].append(item)

        return modified_response


    def run_compliance(self, run_compliance_params):

        result = self.dnac_apply['exec'](
            family="compliance",
            function="run_compliance",
            params=run_compliance_params,
            op_modifies=True,
        )

        self.log("The response received post run_compliancee API call is {0}".format(str(result)), "DEBUG")

        self.result.update(dict(response=result['response']))
        self.log("Task Id of the API task created is {0}".format(result.response.get('taskId')), "INFO")
        return result.response.get('taskId')

    def sync_device_config(self, sync_device_config_params):
        result = self.dnac_apply['exec'](
            family="compliance",
            function="commit_device_configuration",
            params=sync_device_config_params,
            op_modifies=True,
        )

        self.log("The response received post commit_device_configuration API call is {0}".format(str(result)), "DEBUG")

        self.result.update(dict(response=result['response']))
        self.log("Task Id of the API task created is {0}".format(result.response.get('taskId')), "INFO")
        return result.response.get('taskId')

    def get_task_status(self, task_id, task_name):
        response = self.dnac_apply['exec'](
                family="task",
                function='get_task_by_id',
                params=dict(task_id=task_id),
                op_modifies=True,
            )
        response = response.response
        self.log("Task status for the task id {0} is {1}, is_error: {2}".format(str(task_id), str(response), str(response.get('isError'))), "INFO")
        return response

    def update_result(self, status, changed, msg, log_level, data=None):
        self.status = status
        self.result['status'] = status
        self.result['msg'] = msg
        self.result['changed'] = changed 
        self.log(msg, log_level)
        if status == 'failed':
            self.result['failed'] = True  
        if data:
            self.result['data'] = data
        return self

    def exit_while_loop(self, start_time, task_id, task_name, response):
        if time.time() - start_time > 10:
            if response.get('data'):
                self.msg = "Task {0} with task id {1} has not completed within the timeout period. Task Status: {2} ".format(
                task_name, task_id, response.get('data'))
            else:
                self.msg = "Task {0} with task id {1} has not completed within the timeout period.".format(
                    task_name, task_id)
            self.update_result('failed', False, self.msg, 'ERROR')
            return True
        return False 

    def handle_error(self, task_name, mgmt_ip_instance_id_map, failure_reason=None):
        if failure_reason:
            self.msg = "An error occurred while performing {0} on device(s): {1}. The operation failed due to the following reason: {2}".format(
                task_name, list(mgmt_ip_instance_id_map.keys()), failure_reason)
        else:
            self.msg = "An error occurred while performing {0} on device(s): {1}".format(
                task_name, list(mgmt_ip_instance_id_map.keys()))
        self.update_result('failed', False, self.msg, 'ERROR')
        return self


    def get_compliance_task_status(self, task_id, mgmt_ip_instance_id_map):
        task_name = 'Run Compliance Check'
        start_time = time.time()
        while True:
            response = self.get_task_status(task_id, task_name)

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break
            
            if response.get('isError'):
                failure_reason = response.get("failureReason")
                self.handle_error(task_name, mgmt_ip_instance_id_map, failure_reason)
                break

            elif not response.get('isError') and 'success' in response.get('progress').lower():
                self.msg = "{0} has completed successfully on device(s): {1}".format(task_name, list(mgmt_ip_instance_id_map.keys()))
                response = self.get_compliance_detail(self.want.get('compliance_detail_params'))
                modified_response = self.modify_compliance_response(response, mgmt_ip_instance_id_map)
                self.log('Modified {0} Response for device(s) {1} : {2}'.format(task_name, list(mgmt_ip_instance_id_map.keys()), modified_response), 'INFO')
                self.update_result('success', True, self.msg, 'INFO', modified_response)
                break

            elif 'failed' in response.get('progress').lower():
                self.msg = "Failed to {0} on the following device(s): {1}".format(task_name, list(mgmt_ip_instance_id_map.keys()))
                self.update_result('failed', False, self.msg, 'CRITICAL')
                break
        return self

    def sync_config_task_status(self, task_id, mgmt_ip_instance_id_map):
        task_name = 'Sync Device Configuration'

        #Validate if sync is required
        response = self.get_compliance_detail(self.want.get('compliance_detail_params_sync'))
        modified_response = self.modify_compliance_response(response, mgmt_ip_instance_id_map)
        self.log('Modified {0} Response for device(s) {1} : {2}'.format(task_name, list(mgmt_ip_instance_id_map.keys()), modified_response), 'INFO')
        
        categorized_devices = {'COMPLIANT': {}, 'NON_COMPLIANT': {}, 'OTHER': {}}
        for ip_address, compliance_type in modified_response.items():
          if compliance_type[0]['status'] == 'NON_COMPLIANT':
            categorized_devices['NON_COMPLIANT'][ip_address] = compliance_type
          elif compliance_type[0]['status'] == 'COMPLIANT':
            categorized_devices['COMPLIANT'][ip_address] = compliance_type
          else:
            categorized_devices['OTHER'][ip_address] = compliance_type

        if len(categorized_devices['COMPLIANT']) == len(mgmt_ip_instance_id_map):
          self.msg = "Device(s) {0} are already compliant with the RUNNING_CONFIG compliance type. Therefore, {1} is not required.".format( 
                list(mgmt_ip_instance_id_map.keys()), task_name)
          self.update_result('success', False, self.msg, 'INFO',categorized_devices['COMPLIANT'])
          return self

        if categorized_devices['OTHER']:
          self.msg = "The operation {0} cannot be performed on device(s) {1} because the status of the RUNNING_CONFIG compliance type is not as expected; it should be NON_COMPLIANT.".format(
            task_name, list(mgmt_ip_instance_id_map.keys()))
          self.update_result('success', False, self.msg, 'INFO',categorized_devices )
          return self


        start_time = time.time()
        while True:

            response = self.get_task_status(task_id, task_name)

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break

            if response.get('isError'):
                failure_reason = response.get("failureReason")
                self.handle_error(task_name, mgmt_ip_instance_id_map, failure_reason)
                break

            elif len(mgmt_ip_instance_id_map) == 1:
                ip_address = next(iter(mgmt_ip_instance_id_map))
                progress = response.get('progress', '').lower()
                if not response.get('isError') and 'success' in progress:
                    self.log("Task {0} with task id {1} has completed successfully on device {2}.".format(
                        task_name, task_id, ip_address), "INFO")
                    self.msg = "{0} has completed successfully on device: {1}".format(task_name, ip_address)
                    self.update_result('success', True, self.msg, 'INFO')
                    break

                elif 'failed' in progress:
                    self.log('Task {0} with task id {1} has failed on device {2}.'.format(
                        task_name, task_id, ip_address), "CRITICAL")

                    self.msg = "Failed to {0} on the following device(s):".format(task_name, ip_address)
                    self.update_result('failed', False, self.msg, 'CRITICAL')
                    break

            elif len(mgmt_ip_instance_id_map) > 1:
                data = response.get('data')
                if data:
                    count_values = [count.strip() for count in data.split(',')]
                    success_count = int(count_values[0].split('=')[1])
                    running_count = int(count_values[2].split('=')[1])
                    pending_count = int(count_values[3].split('=')[1])
                    total_count = int(count_values[-1].split('=')[1])

                    if success_count == len(mgmt_ip_instance_id_map):
                        self.log("Task {0} with task id {1} has completed successfully on devices: {2}.".format(
                            task_name, task_id, list(mgmt_ip_instance_id_map.keys())), "INFO")

                        self.msg = "{0} has completed successfully on devices: {1}".format(task_name, list(mgmt_ip_instance_id_map.keys()))
                        self.update_result('success', True, self.msg, 'INFO')
                        break

                    elif running_count == 0 and pending_count == 0  and success_count < len(mgmt_ip_instance_id_map):
                        status_info = {'Success': {'count': success_count, 'devices': []}, 'Failed': {'count': failure_count, 'devices': []}}
                        device_actions = response['progress'].split(',')
                        for action in device_actions:
                            device_id = action.split('=')[1].strip()
                            ip_address = next((ip for ip, device_id_map in mgmt_ip_instance_id_map.items() if device_id_map == device_id), None)
                            if ip_address:
                                if 'Success' in action:
                                    status_info['Success']['devices'].append({'ip_address': ip_address, 'device_id': device_id})
                                elif 'Failed' in action:
                                    status_info['Failure']['devices'].append({'ip_address': ip_address, 'device_id': device_id})
                        self.msg = 'Task {0} status: {1}'.format(task_name, status_info)
                        self.update_result('failed', True, self.msg, 'CRITICAL')
                        break
        return self

    def get_diff_merged(self):
        if self.want.get('run_compliance_params'):
            result_task_id = self.run_compliance(self.want.get('run_compliance_params'))
            self.get_compliance_task_status(result_task_id, self.want.get('mgmt_ip_instance_id_map')).check_return_status()

        if self.want.get('sync_device_config_params'):
            result_task_id = self.sync_device_config(self.want.get('sync_device_config_params'))
            self.sync_config_task_status(result_task_id, self.want.get('mgmt_ip_instance_id_map')).check_return_status()

        return self

    # def get_diff_merged(self):
    #     action_map = {
    #         'run_compliance_params': (self.run_compliance, self.get_compliance_task_status),
    #         'sync_device_config_params': (self.sync_device_config, self.sync_config_task_status)
    #     }

    #     if not any(self.want.get(action_param) for action_param in action_map):
    #       msg = "Network compliance operations are missing from the playbook. You can perform compliance checks or sync device configuration tasks using this module."
    #       self.log(msg, "ERROR")
    #       self.module.fail_json(msg)

    #     for action_param, (action_func, status_func) in action_map.items():
    #         if self.want.get(action_param):
    #             result_task_id = action_func(self.want.get(action_param))
    #             status_func(result_task_id, self.want.get('mgmt_ip_instance_id_map')).check_return_status()

    #     return self
        
    def verify_diff_merged(self, config):
      pass

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
        ccc_network_compliance.get_diff_state_apply[state]().check_return_status()
        # if config_verify:
        #   ccc_network_compliance.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_network_compliance.result)


if __name__ == "__main__":
    main()

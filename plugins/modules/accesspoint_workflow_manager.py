#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, A Mohamed Rafeek, Natarajan")

DOCUMENTATION = r"""
---
module: accesspoint_workflow_manager
short_description: accesspoint_workflow_manager used to automate bulk AP configuration changes.
description:
- We can change the AP display name, AP name or Other Param based on the input.yml file
- Using by this package we can filter specific device details like hostname = Switches and Hubs
- We can compare input details with current AP configuration.
- Desired configuration will be updated to the needed APs Only
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.accesspoint_workflow_manager
author: Madhan Sankaranarayanan (@madhansansel)
        A Mohamed Rafeek (@mohamedrafeek)
        Natarajan (@natarajan)

options:
    config_verify:
        description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: False
    state:
        description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged ]
    default: merged

  config:
    description: List of details of AP being managed
    type: list
    elements: dict
    required: True
    device_fields:
        description: This is a optional field, if you want to see only few param
            from the device details you can mention those field in this list.
            each field need to mention with , seperation not space before or after ,
            if this fields not defined then default will show all field param
            eg : device_fields: "id,hostname,family,type,mac_address,management_ip_address,ap_ethernet_mac_address,last_updated,up_time"
        type: str
        required: False
    ap_selected_field:
        description: This is a optional field, if you want to see only few param
            from the Accesspoint config details, then you can mention those field
            in this list. each field need to mention with , seperation not space before or after ,
            if this fields not defined then default will show all field param
            eg : ap_selected_field: "mac_address,eth_mac,ap_name,led_brightness_level,led_status,location"
        type: str
        required: False

      Unchangable Params are below any one of the below 4 is required.
    mac_address:
        description: This is MAC Address Field use to identify the devices
            from the device detail we have used to get the AP Details
            (also it is Required or Hostname Required), This field cannot be mofidied.
            MAC Address format should be eg: mac_address: "90:e9:5e:03:f3:40"
        type: str
        required: True
    hostname:
        description: This is name of device if MAC address not known
            Then hostname can be used to indentify the device
            eg : hostname: "NFW-AP1-9130AXE"
        type: str
        required: True
    management_ip_address:
        description: This param used to indetify the devices based on IP address
            from the device detail we have used to get the AP Details
            eg: management_ip_address: "204.192.6.200"
        type: str
        required: True

      below list of AP Config param can be changes based on the requirement
    ap_name:
        description: AP Name changes, we need to provide the current name
            of AP and ap_name_new.
            unless the AP name never change.
            eg : ap_name: "Test2"
                 ap_name_new: "NFW-AP1-9130AXE"
        type: str
        required: False
    ap_name_new:
        description: AP Name name changes new name need to be added in this field.
            we need to provide along with AP Name. so that able to change the AP Name
            eg : ap_name: "Test2"
                 ap_name_new: "NFW-AP1-9130AXE"
        type: str
        required: False
    led_brightness_level:
        description: AP LED brightness level field also able to modify by update
            this field. Brightness level from 1 to 10.
            eg : led_brightness_level: 3
        type: int
        required: False
    led_status:
        description: AP LED light need to enable or disable based on this param update.
            this will accept only 2 state "Enabled" or "Disabled"
            eg : led_status: "Enabled"
        type: str
        required: False
    location:
        description: Changing the location name of the AP, need to provide the data
            in case changes required.
            eg: location: "Bangalore"
        type: str
        required: False

requirements:
- dnacentersdk >= 2.4.5
- python >= 3.8
notes:
  - SDK Method used are 
    devices.get_device_list
    wireless.get_access_point_configuration
    wireless.configure_access_points

  - Paths used are
    get /dna/intent/api/v1/network-device
    get /dna/intent/api/v1/wireless/accesspoint-configuration/summary?key={ap_ethernet_mac_address}
    post /dna/intent/api/v2/wireless/accesspoint-configuration
"""

EXAMPLES = r"""
- name: Create/Update/Delete Wireless Accesspoint Configuration
  hosts: dnac_servers
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Updating Accesspoint Configureation
      cisco.dnac.accesspoint_workflow_manager:
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{dnac_debug}}"
        dnac_log: True
        dnac_log_level: DEBUG
        config_verify: True
        state: merged
        config:
          - device_fields: "id,hostname,family,type,mac_address,management_ip_address,ap_ethernet_mac_address,last_updated,up_time"
            ap_selected_field: "mac_address,eth_mac,ap_name,led_brightness_level,led_status,location"
            mac_address: "90:e9:5e:03:f3:40"
            led_brightness_level: 2
            led_status: "Enabled"
            location: "LTTS-Bangalore"
            ap_name: "LTTS-Test1"
            ap_name_new: "NFW-AP1-9130AXE"
      register: output_list
"""

RETURN = r"""
#Case: Modification of the AP details updated and Rebooted Accesspoint
response:
  description: A dictionary with activation details as returned by the Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    "response": [
        {
            "accesspoints_updates": {
                "response": {
                    "macAdress": "34:5d:a8:0e:20:b4",
                    "response": {
                        "taskId": "2ce139fa-1d58-4739-a6ad-b735b97e4dfe",
                        "url": "/api/v1/task/2ce139fa-1d58-4739-a6ad-b735b97e4dfe"
                    }
                }
            }
        },
        {
            "accesspoints_verify": {
                "have": [
                    {
                        "ap_name": "NFW-AP1-9130AXE",
                        "eth_mac": "34:5d:a8:0e:20:b4",
                        "led_brightness_level": 2,
                        "led_status": "Enabled",
                        "location": "LTTS-Bangalore",
                        "mac_address": "90:e9:5e:03:f3:40"
                    }
                ],
                "message": "The update for AP Config 'NFW-AP1-9130AXE' has been successfully verified.",
                "want": {
                    "ap_name": "LTTS-Test1",
                    "ap_name_new": "NFW-AP1-9130AXE",
                    "hostname": null,
                    "led_brightness_level": 2,
                    "led_status": "Enabled",
                    "location": "LTTS-Bangalore",
                    "mac_address": "90:e9:5e:03:f3:40",
                    "management_ip_address": null
                }
            }
        }
    ]
"""

import re, time
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    validate_str
)
from ansible.module_utils.basic import AnsibleModule


class Accesspoint(DnacBase):
    """Class containing member attributes for DNAC Access Point Automation module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = []
        self.supported_states = ["merged", "deleted"]
        self.payload = module.params
        self.keymap = {}


    # Below function used to validate input over the ansible validation
    def validate_input_yml(self):
        """
        Validate the fields provided in the yml files.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types based on input.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
          The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        Description:
            Example:
                To use this method, create an instance of the class and call 'validate_input_yml' on it.
                If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
                will contain the validated configuration. If it fails, 'self.status' will be 'failed', and
                'self.msg' will describe the validation issues.To use this method, create an instance of the class and call 'validate_input_yml' on it.
                If the validation succeeds, this will allow to go next step, unless this will stop execution.
                based on the fields.
        """
        self.log('Validating the Playbook Yaml File..', "INFO")
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        aplist = self.payload.get("config")
        aplist = self.camel_to_snake_case(aplist)
        aplist = self.update_site_type_key(aplist)
        accesspoint_spec = dict(mac_address=dict(required=False, type='str'),
                    led_brightness_level=dict(required=False, type='int'),
                    led_status = dict(required=False, type='str'),
                    location = dict(required=False, type='str'),
                    ap_name = dict(required=False, type='str'),
                    ap_name_new = dict(required=False, type='str'),
                    management_ip_address = dict(required=False, type='str'),
                    hostname = dict(required=False, type='str'),
                    device_fields = dict(required=False, type='str'),
                    ap_selected_field = dict(required=False, type='str'),
                    )
        valid_param, invalid_params = validate_list_of_dicts(aplist, accesspoint_spec)
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params)
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_param
        self.msg = "Successfully validated playbook config params:{0}".format(str(valid_param[0]))
        self.log(self.msg, "INFO")
        self.status = "success"
        return self

    def get_want(self, ap_config):
        """
        Get all site-related information from the playbook needed for creation/updation/deletion of site in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            Retrieves all site-related information from playbook that is
            required for creating a site in Cisco Catalyst Center. It includes
            parameters such as 'site_params' and 'site_name.' The gathered
            information is stored in the 'want' attribute for later reference.
        """
        self.log("CHECKIN" + str(ap_config), "INFO")
        want = {}
        for key,value in ap_config.items():
            if key not in ("device_fields", "ap_selected_field"):
                want[key] = value
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        return self


    def get_have(self, input_config):
        """
        Get the site details from Cisco Catalyst Center
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - input_config (dict): A dictionary containing the configuration details.
        Returns:
          - self (object): An instance of a class used for interacting with  Cisco Catalyst Center.
        Description:
            This method queries Cisco Catalyst Center to check if a specified site
            exists. If the site exists, it retrieves details about the current
            site, including the site ID and other relevant information. The
            results are stored in the 'have' attribute for later reference.
        """
        device_exists = False
        current_ap_config = None
        # check if given AP config exists, if exists store current AP config info
        (device_exists, current_ap_config) = self.get_current_config(input_config)
        self.log("Current AP config details (have): {0}".format(str(current_ap_config)), "DEBUG")
        have = {}
        if device_exists:
            have["mac_address"] = current_ap_config.get("mac_address")
            have["device_exists"] = device_exists
            have["current_ap_config"] = current_ap_config
        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        return self


    def get_diff_merged(self, config):
        """
        Update/Create wireless accesspoint configuration in Cisco Catalyst Center with fields
        provided in the playbook.
        Parameters:
          self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method determines whether to update or create AP configuration in Cisco
            Catalyst Center based on the provided configuration information. 
            If the specified site exists, the method checks if it requires an update
            by calling the 'update_ap_configuration' method. If an update is required, 
            it calls the 'configure_access_points' function from the 'wireless' family of 
            the Cisco Catalyst Center API. If Current configuration same as input configuration 
            does not require an update, the method exits, indicating that Accesspoint 
            configuration is up to date.
        """

        config_updated = False
        config_created = False
        task_response = None
        errormsg = []
        eachap = config
        if eachap.get("mac_address"):
            mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
            if not mac_regex.match(eachap["mac_address"]):
                errormsg.append("mac_address : Invalid MAC Address '{0}' in playbook."\
                                .format(eachap["mac_address"]))

        if eachap.get("management_ip_address"):
            if not self.is_valid_ipv4(eachap["management_ip_address"]):
                errormsg.append("management_ip_address: Invalid Management IP Address '{0}' in playbook"\
                                .format(eachap["management_ip_address"]))

        if eachap.get("ap_name"):
            param_spec = dict(type = "str", length_max = 32)
            validate_str(eachap["ap_name"], param_spec, "ap_name", errormsg)

        if eachap.get("ap_name_new"):
            param_spec = dict(type = "str", length_max = 32)
            validate_str(eachap["ap_name_new"], param_spec, "ap_name_new", errormsg)

        if eachap.get("led_brightness_level"):
            if eachap["led_brightness_level"] not in range(1,9):
                errormsg.append("led_brightness_level: Invalid LED Brightness level '{0}' in playbook"\
                                .format(eachap["led_brightness_level"]))

        if eachap.get("led_status") and eachap.get("led_status") not in ("Disabled", "Enabled"):
            errormsg.append("led_status: Invalid LED Status '{0}' in playbook"\
                            .format(eachap["led_status"]))

        if eachap.get("location"):
            param_spec = dict(type = "str", length_max = 255)
            validate_str(eachap["location"], param_spec, "location",
                            errormsg)

        if len(errormsg) > 0:
            self.log("Invalid parameters in playbook config: '{0}' "\
                     .format(str("\n".join(errormsg))), "ERROR")
            self.module.fail_json(msg=str("\n".join(errormsg)))

        # check if the given AP config exists and/or needs to be updated/created.
        if self.have.get("device_exists"):
            consolidated_data = self.compare_ap_cofig_with_inputdata(self.have["current_ap_config"])
            if consolidated_data:
                self.log('Final AP Configuration data to update {0}'.format(str(consolidated_data)),
                      "INFO")
                task_response = self.update_ap_configuration(consolidated_data)
                self.log('Task respoonse {0}'.format(str(task_response)),"INFO")
                config_updated = True
            else:
                # Accesspoint does not need update
                self.msg = "AP - {0} does not need any update"\
                    .format(self.have.get("current_ap_config").get("ap_name"))
                self.log(self.msg, "INFO")
                responses = {}
                del self.payload["device_list"]
                responses["accesspoints_updates"] = {"response": self.payload["device_config"]}
                self.result['msg'] = self.msg
                self.result["response"].append(responses)
                self.result["changed"] = False
                return self

        responses = {}
        if config_updated or config_created:
            if task_response and isinstance(task_response, dict):
                self.check_task_response_status(task_response, "task_intent", True)\
                    .check_return_status()
                if self.status == "success":
                    self.result['changed'] = True
                    responses["accesspoints_updates"] = {"response": task_response}
                    state = "Updated" if config_updated else "Created"
                    self.msg = "AP Configuration - {0} {1} Successfully"\
                        .format(self.have["current_ap_config"].get("ap_name"), state)
                    self.log(self.msg, "INFO")
                    self.result['msg'] = self.msg
                    self.result['response'].append(responses)
                else:
                    self.status = "failed"
                    self.msg = "Unable to get task response"
            return self


    def verify_diff_merged(self, config):
        """
        Verify the merged status(Creation/Updation) of AP configuration in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by retrieving the current state
            (have) and desired state (want) of the configuration, logs the states, and validates whether the specified
            AP exists in the Catalyst Center configuration.
        """
        time.sleep(5)
        self.get_have(config)
        self.log("Current AP Config (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired AP Config (want): {0}".format(str(self.want)), "INFO")

        # Code to validate dnac config for merged state
        ap_config_exist = self.have.get("device_exists")
        ap_name = self.have.get("current_ap_config").get("ap_name")

        if ap_config_exist:
            self.status = "success"
            self.msg = "The requested AP Config '{0}' is present in the Cisco Catalyst Center and its creation has been verified."\
                .format(ap_name)
            self.log(self.msg, "INFO")

        require_update = self.compare_ap_cofig_with_inputdata(self.have["current_ap_config"])
        self.log(str(require_update), "INFO")
        if not require_update:
            msg = "The update for AP Config '{0}' has been successfully verified.".format(ap_name)
            self.log(msg, "INFO")
            self.status = "success"
            responses = {}
            responses["accesspoints_verify"] = {"want": self.want,
                                                "have": self.payload["device_config"],
                                                "message": msg}
            self.result['response'].append(responses)
            return self

        self.log("""The playbook input for AP '{0}' does not align with the Cisco Catalyst Center, indicating that the merge task
                 may not have executed successfully.""".format(ap_name), "INFO")

        return self


    def get_current_config(self, input_config):
        """
        Check if the input wireless accesspoint configuration exists in Cisco Catalyst Center.

        Parameters:
          - self (object): An instance of the class containing the method.
        Returns:
            A Dictionary list contains Accesspoint configuration based on the input given from
            playbook either mac_address or management_ip_address or hostname
            [
                {
                    "ap_name": "NFW-AP1-9130AXE",
                    "eth_mac": "34:5d:a8:0e:20:b4",
                    "led_brightnessLevel": 3,
                    "led_status": "Enabled",
                    "location": "LTTS",
                    "mac_address": "90:e9:5e:03:f3:40"
                }
            ]
        Description:
            Checks the existence of a Device details in Cisco Catalyst Center by querying the
            'get_device_list' function in the 'devices' family. Based on the response need to 
            pass the ap_ethernet_mac_address to the another 'get_access_point_configuration' function
            in the 'wireless' family to get AP configuration to check the input data with current
            config data and return above resoponse.
        """
        accesspoint_exists = False
        current_configuration = {}
        response = None
        input_param = {}
        if input_config.get("mac_address") is not None and input_config.get("mac_address") != "":
            input_param["macAddress"] = input_config["mac_address"]
        elif input_config.get("management_ip_address") is not None and \
            input_config.get("management_ip_address") != "":
            input_param["managementIpAddress"] = input_config["management_ip_address"]
        elif input_config.get("hostname") is not None and input_config.get("hostname") != "":
            input_param["hostname"] = input_config["hostname"]

        if not input_param:
            self.log("Required param mac_address, management_ip_address or hostname is not in playbook config",
                      "ERROR")
            return (accesspoint_exists, current_configuration)

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                op_modifies=True,
                params=input_param,
            )
            if response:
                response = response.get("response")
                response = self.camel_to_snake_case(response)
                device_fields = self.payload.get("config")[0].get("device_fields")
                if device_fields is None or device_fields == "" or device_fields == "all":
                    self.payload["device_list"] = response[0]
                else:
                    self.payload["device_list"]=self.data_frame(device_fields,response)
                self.log("Received API response from 'get_device_list': {0}"\
                        .format(str(self.payload["device_list"][0])), "DEBUG")

                ap_ethernet_mac_address = response[0]["ap_ethernet_mac_address"]
                accesspoint_exists, current_configuration = self.get_accesspoint_config(
                ap_ethernet_mac_address)
        except Exception as e:
            self.log("The provided device '{0}' is either invalid or not present in the Cisco Catalyst Center."\
                     .format(str(input_param) + str(e)), "WARNING")

        return (accesspoint_exists, current_configuration)


    def get_accesspoint_config(self, ap_ethernet_mac_address):
        """
        Gives output as accesspoint configuration data from Cisco Catalyst Center.

        Parameters:
          - self (object): An instance of the class containing the method.
          - ap_ethernet_mac_address (str): Contains AP eth mac address from device data
        Returns:
            A Dictionary list contains Accesspoint configuration based on the input given from
            Device list 
            [
                {
                    "ap_name": "NFW-AP1-9130AXE",
                    "eth_mac": "34:5d:a8:0e:20:b4",
                    "led_brightnessLevel": 3,
                    "led_status": "Enabled",
                    "location": "LTTS",
                    "mac_address": "90:e9:5e:03:f3:40"
                }
            ]
        Description:
            get the Accesspoint configuration data from Cisco Catalyst Center by querying the
             to this function 'get_access_point_configuration' function
            in the 'wireless' family to get AP configuration data.
        """
        ap_response = None
        input_param = {}
        input_param["key"] = ap_ethernet_mac_address
        try:
            ap_response = self.dnac._exec(
                family="wireless",
                function='get_access_point_configuration',
                params=input_param,
            )
        except Exception as e:
            self.log("Unable to get the Accesspoint configuratoin for '{0}' ."\
                        .format(str(input_param) + str(e)), "WARNING")

        if ap_response:
            self.keymap = self.keymaping(self.keymap, ap_response)
            ap_response = self.camel_to_snake_case(ap_response)
            current_configuration = ap_response
            self.log("Received API response from 'get_access_point_configuration': {0}"\
                        .format(str(current_configuration)), "DEBUG")
            ap_selected_field = self.payload.get("config")[0].get("ap_selected_field")
            if ap_selected_field is None or ap_selected_field == "" or ap_selected_field == "all":
                self.payload["device_config"] = ap_response
            else:
                self.payload["device_config"]=self.data_frame(ap_selected_field,[ap_response])

            self.log("AP configuration {0} exists in Cisco Catalyst Center"\
                        .format(str(self.payload["device_config"][0])), "INFO")
            accesspoint_exists = True
        return (accesspoint_exists, current_configuration)


    def compare_ap_cofig_with_inputdata(self, apconfig):
        """
        This function used to compare with the input ap detail with the current ap configuration
        information are not same, those data will be updated in the AP input information.
        Parameters:
          - apconfig: This is response of the get_have
        Returns:
            This will be the return the final data for update AP detail.
            "final_input": [
                {
                    "adminStatus": true,
                    "apList": [
                        {
                            "macAddress": "34:5d:a8:0e:20:b4"
                        }
                    ],
                    "configureLedBrightnessLevel": true,
                    "ledBrightnessLevel": 4,
                    "macAddress": "34:5d:a8:0e:20:b4"
                } ]
        Example:
            functions = Accesspoint(module)
            final_input_data = functions.compare_ap_cofig_with_inputdata(all_apconfig)
        """

        newdict = {}
        if self.want and apconfig:
            if self.want.get("mac_address") == apconfig["mac_address"] or \
                    self.want.get("hostname") == apconfig["ap_name"]:
                allkey = list(self.want.keys())
                for value in ("mac_address","hostname","management_ip_address", "family"):
                    if value in allkey: allkey.remove(value)
                for each_key in allkey:
                    if each_key == "ap_name_new":
                        if self.want["ap_name_new"] != apconfig.get("ap_name"):
                            newdict["apNameNew"] = self.want["ap_name_new"]
                    elif each_key == "ap_name":
                        newdict[self.keymap[each_key]] = self.want[each_key]
                    else:
                        if self.want[each_key] != apconfig[each_key]:
                            newdict[self.keymap[each_key]] = self.want[each_key]
                if newdict.get("apName") is not None and newdict.get("apNameNew") is None:
                    del newdict["apName"]
                if newdict:
                    newdict["macAddress"] = apconfig["eth_mac"]
            if newdict:
                return newdict
            else:
                self.log('Playbook AP Configuration remain same in Current AP configration',
                      "INFO")
                return None


    def update_ap_configuration(self, device_data):
        """
        This function used to update the ap detail with the current ap configuration
        Final data received from compare_ap_cofig_with_inputdata response will be the 
        input of this function.
        Parameters:
          - device_data: DNAC final device data response from compare_ap_cofig_with_inputdata
        Returns:
            {
                "response": {
                    "taskId": "string",
                    "url": "string"
                },
                "version": "string"
            }
        Example:
            functions = Accesspoint(module)
            final_input_data = functions.update_ap_configuration(device_data)
        """

        device = device_data
        try:
            self.log("Updating Access Point Configuration Information "+ device["macAddress"],
                        "INFO")
            # Below code might changed once we receive the dev dnac credentials
            device["adminStatus"] = True
            if device.get("apName") is not None:
                device["apList"] = [dict(apName = device["apName"],
                                    apNameNew = device["apNameNew"],
                                    macAddress = device["macAddress"])]
                del device["apName"]
                del device["apNameNew"]
            elif device.get("apName") is None and device.get("macAddress") is not None:
                device["apList"] = [dict(macAddress = device["macAddress"])]

            if device.get("location") is not None:
                device["configureLocation"] = True
            if device.get("ledBrightnessLevel") is not None:
                device["configureLedBrightnessLevel"] = True
            if device.get("ledStatus") is not None:
                device["configureLedStatus"] = True
                device["ledStatus"] = True if device["ledStatus"] == "Enabled" else False

            for rmkey in ("mac_address", "hostname", "management_ip_address"):
                if device.get(rmkey): del device[rmkey]
            
            #response = self.dnacsdk.wireless.configure_access_points(**device)
            response = self.dnac._exec(
                    family="wireless",
                    function='configure_access_points',
                    op_modifies=True,
                    params=device,
                )

            self.log("Response of Access Point Configuration: {0}"\
                     .format(str(response["response"])), "INFO")
            return dict(macAdress=device["macAddress"], response=response["response"])

        except Exception as e:
            self.log("AP config update Error {0}".format(str(device["macAddress"])+str(e)), "ERROR")


    def data_frame(self, fieldlist = None, data = list):
        """
        This function used to give output as limited field to show for given in the fieldlist
        need to pass the list of field need to show with , separated string value also need
        to pass the data as device list or device config list as input
        Parameters:
          - fieldlist: (str) key need to display the value.
            eg : device_fields: "id,hostname,family,type,mac_address,up_time"
          - data: (list of dict) Device list or Config list
        Returns:
            {
                "family": "Unified AP",
                "hostname": "LTTS-Test2",
                "id": "34f5a410-413d-4a6c-b195-8267fd599491",
                "last_updated": "2024-06-05 13:06:24",
                "mac_address": "34:5d:a8:3b:d8:e0",
                "up_time": "7 days, 13:07:00.020"
            }
        Example:
            functions = Accesspoint(module)
            final_input_data = functions.data_frame(device_fields, device_data)
        """
        try:
            data = self.camel_to_snake_case(data)
            if len(data) != 0 and fieldlist is not None:
                fields = [x for x in fieldlist.split(",")]
                dataframe = []
                for eachdata in data:
                    limitedfields = {}
                    for each_key in fields:
                        limitedfields[each_key] = eachdata[each_key]
                    dataframe.append(limitedfields)
                return dataframe
            else:
                return data
        except Exception as e:
            self.log("Unable to process Dataframe "+ str(e) , "ERROR")
            return None


    def keymaping(self, keymap = any, data = any):
        """
        This function used to create the key value by snake case and Camal Case
        we need to pass the input as the device list or AP cofig list this function collects
        all key which is in Camal case and convert the key to Snake Case 
        Snake case will be key and value will be as Camal Case return as Dict
        Parameters:
          - keymap: type Dict : Already any Key map dict was available add here or empty dict.{}
          - data: Type :Dict : Which key need do the key map use the data {}
            eg: Device list response or AP config response as a input
        Returns:
            {
                {
                    "mac_address": "macAddress",
                    "ap_name": "apName"
                }
            }
        Example:
            functions = Accesspoint(module)
            keymap = functions.keymaping(keymap,device_data)
        """
        if isinstance(data, dict):
            keymap.update(keymap)
            for key, value in data.items():
                new_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key).lower()
                keymap[new_key] = key
                if isinstance(value, dict):
                    self.keymaping(keymap, value)
                elif isinstance(value, list):
                    self.keymaping(keymap, (item for item in value if isinstance(item, dict)))
            return keymap
        elif isinstance(data, list):
            self.keymaping(keymap, (item for item in data if isinstance(item, dict)))
        else:
            return keymap



def main():
    """ main entry point for module execution
    """
    # Basic Ansible type check or assign default.
    accepoint_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin'},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    'config_verify': {'type': 'bool', "default": False},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                }
    module = AnsibleModule(
        argument_spec=accepoint_spec,
        supports_check_mode=True
    )

    ccc_network = Accesspoint(module)
    state = ccc_network.params.get("state")

    if state not in ccc_network.supported_states:
        ccc_network.status = "invalid"
        ccc_network.msg = "State {0} is invalid".format(state)
        ccc_network.check_return_status()

    ccc_network.validate_input_yml().check_return_status()
    config_verify = ccc_network.params.get("config_verify")

    for config in ccc_network.validated_config:
        ccc_network.reset_values()
        ccc_network.get_want(config).check_return_status()
        ccc_network.get_have(config).check_return_status()
        ccc_network.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_network.verify_diff_state_apply[state](config).check_return_status()
    module.exit_json(**ccc_network.result)


if __name__ == '__main__':
    main()

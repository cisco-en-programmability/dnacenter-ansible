#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Natarajan, Madhan Sankaranarayanan, Abhishek Maheshwari")

DOCUMENTATION = r"""
---
module: accesspoint_workflow_manager
short_description: accesspoint_workflow_manager used to automate bulk AP configuration changes.
description:
  - Automates bulk configuration changes for Access Point (APs).
  - Modify AP display names, AP names, or other parameters.
  - Filter specific device details, such as selecting devices with hostnames matching "NFW-AP1-9130AXE"
  - Compares input details with current AP configurations and applies desired changes only to relevant APs.

version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.accesspoint_workflow_manager
author: 
    - A Mohamed Rafeek (@mohamedrafeek)
    - Natarajan (@natarajan)
    - Madhan Sankaranarayanan (@madhansansel)
    - Abhishek Maheshwari (@abmahesh)
       
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
        description:
            - Optional field to specify specific fields to display from the device details.
            - Fields should be separated by commas without spaces before or after the commas.
            - If not defined, all device fields are shown by default.
            - Example: "id,hostname,family,type,mac_address,management_ip_address,ap_ethernet_mac_address,last_updated,up_time"
        type: str
        required: False
    ap_selected_field:
        description: Optional field to specify specific parameters from the Access Point configuration details.
            Each field should be separated by commas without spaces.
            If not defined, all fields will be shown by default.
            Example: "mac_address,eth_mac,ap_name,led_brightness_level,led_status,location"
        type: str
        required: False

      Unchangable Params are below any one of the below 3 is required.
    mac_address:
        description: |
            MAC Address field used to identify the device. If MAC address is known,
            it must be provided. This field cannot be modified.
            Example: mac_address: "90:e9:5e:03:f3:40"
        type: str
        required: True
    hostname:
        description: |
            Device hostname used to identify the device.
            Example: hostname: "NFW-AP1-9130AXE"
        type: str
        required: True
    management_ip_address:
        description: |
            Management IP address used to identify the device based on IP.
            This is an alternative if MAC address or hostname is not available.
            Example: management_ip_address: "204.192.6.200"
        type: str
        required: True

      below list of AP Config param can be changes based on the requirement
    ap_name:
        description: |
            Current AP name that needs to be changed along with the new AP name.
            Example: ap_name: "Test2", ap_name_new: "NFW-AP1-9130AXE"
        type: str
        required: False
    ap_name_new:
        description: |
            New AP name to be assigned. Must be provided along with the current AP name.
            Example: ap_name: "Test2", ap_name_new: "NFW-AP1-9130AXE"
        type: str
        required: False
    led_brightness_level:
        description: |
            Brightness level of the AP's LED. Accepts values from 1 to 8.
            Example: led_brightness_level: 3
        type: int
        required: False
    led_status:
        description: |
            State of the AP's LED. Accepts "Enabled" or "Disabled".
            Example: led_status: "Enabled"
        type: str
        required: False
    location:
        description: |
            Location name of the AP. Provide this data if a change is required.
            Example: location: "Bangalore"
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
- name: Create/Update Wireless Access Point Configuration
  hosts: dnac_servers
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Updating Access Point Configuration
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


- name: Create/Update Wireless Access Point Configuration
  hosts: dnac_servers
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Updating Access Point name change in configuration
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
          - device_fields: "id,hostname,mac_address,management_ip_address,ap_ethernet_mac_address"
            ap_selected_field: "mac_address,eth_mac,ap_name"
            mac_address: "90:e9:5e:03:f3:40"
            ap_name: "LTTS-Test1"
            ap_name_new: "NFW-AP1-9130AXE"
      register: output_list
"""

RETURN = r"""
#Case: Modification of the AP details updated and Rebooted Access Point
response:
  description: A list of dictionaries containing details about the AP updates and verification
                results, as returned by the Catalyst Center Python SDK
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
                'self.msg' will describe the validation issues.To use this method, create an
                instance of the class and call 'validate_input_yml' on it.
                If the validation succeeds, this will allow to go next step, 
                unless this will stop execution based on the fields.
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
        Get all Access Point related information from the playbook needed for creation/updation
         in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
             Retrieves all Access Point configuration details from the playbook config,
        excluding any fields not directly related to the Access Point configuration such as
        'device_fields' and 'ap_selected_field'. The extracted information is stored in the 
        'want' attribute of the instance for later use in the workflow.
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
        Retrieves the current Access Point configuration details from Cisco Catalyst Center.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - input_config (dict): A dictionary containing the configuration details.
        Returns:
          - self (object): An instance of a class used for interacting with  Cisco Catalyst Center.
        Description:
            This method checks the system to determine if the specified Access Point configuration exists.
        If it does, it retrieves the current configuration details, such as the MAC address, ... and other
        relevant information. These details are stored in the 'self.have' attribute of the instance.
        """
        ap_exists = False
        current_ap_config = None
        # check if given AP config exists, if exists store current AP config info
        (ap_exists, current_ap_config) = self.get_current_config(input_config)
        self.log("Current AP config details (have): {0}".format(str(current_ap_config)), "DEBUG")
        have = {}

        if ap_exists:
            have["mac_address"] = current_ap_config.get("mac_address")
            have["ap_exists"] = ap_exists
            have["current_ap_config"] = current_ap_config

        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        return self


    def get_diff_merged(self, ap_config):
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

        if ap_config.get("mac_address"):
            mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
            if not mac_regex.match(ap_config["mac_address"]):
                errormsg.append("mac_address : Invalid MAC Address '{0}' in playbook."\
                                .format(ap_config["mac_address"]))

        if ap_config.get("management_ip_address"):
            if not self.is_valid_ipv4(ap_config["management_ip_address"]):
                errormsg.append("management_ip_address: Invalid Management IP Address '{0}' in playbook"\
                                .format(ap_config["management_ip_address"]))

        if ap_config.get("ap_name"):
            param_spec = dict(type = "str", length_max = 32)
            validate_str(ap_config["ap_name"], param_spec, "ap_name", errormsg)

        if ap_config.get("ap_name_new"):
            param_spec = dict(type = "str", length_max = 32)
            validate_str(ap_config["ap_name_new"], param_spec, "ap_name_new", errormsg)

        if ap_config.get("led_brightness_level"):
            if ap_config["led_brightness_level"] not in range(1,9):
                errormsg.append("led_brightness_level: Invalid LED Brightness level '{0}' in playbook"\
                                .format(ap_config["led_brightness_level"]))

        if ap_config.get("led_status") and ap_config.get("led_status") not in ("Disabled", "Enabled"):
            errormsg.append("led_status: Invalid LED Status '{0}' in playbook"\
                            .format(ap_config["led_status"]))

        if ap_config.get("location"):
            param_spec = dict(type = "str", length_max = 255)
            validate_str(ap_config["location"], param_spec, "location",
                            errormsg)

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: '{0}' "\
                     .format(str("\n".join(errormsg)))
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        # check if the given AP config exists and/or needs to be updated/created.
        if self.have.get("ap_exists"):
            consolidated_data = self.compare_ap_config_with_inputdata(self.have["current_ap_config"])

            if not consolidated_data:
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

            self.log('Final AP Configuration data to update {0}'.format(str(consolidated_data)),
                      "INFO")
            task_response = self.update_ap_configuration(consolidated_data)
            self.log('Task respoonse {0}'.format(str(task_response)),"INFO")
            config_updated = True

        responses = {}
        if config_updated or config_created:
            if task_response and isinstance(task_response, dict):
                self.check_task_response_status(task_response, "task_intent", True)\
                    .check_return_status()
                self.log("Status of the task is {}.".format(self.status), "INFO")
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
        Verifies whether the configuration changes for an AP have been successfully applied
            in the Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method logs the current and desired configuration states and checks if 
            the AP exists and whether any updates are required. If the configuration is
            as expected, it logs a success message. Otherwise, it indicates a potential 
            issue with the merge operation.
        """
        self.get_have(config)
        self.log("Current AP Config (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired AP Config (want): {0}".format(str(self.want)), "INFO")

        # Code to validate dnac config for merged state
        ap_exists  = self.have.get("ap_exists")
        ap_name = self.have.get("current_ap_config").get("ap_name")

        if not ap_exists:
            self.status = "failure"
            self.msg = "AP Config '{0}' does not exist in the system.".format(ap_name)
            self.log(self.msg, "ERROR")
            return self
        else:
            self.status = "success"
            self.msg = """The requested AP Config '{0}' is present in the Cisco Catalyst Center 
                        and its creation has been verified.""".format(ap_name)
            self.log(self.msg, "INFO")

        require_update = self.compare_ap_config_with_inputdata(self.have["current_ap_config"])
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
        else:
            self.msg = "Configuration for AP '{0}' does not match the desired state."\
                .format(ap_name)
            self.log(self.msg, "INFO")
            self.status = "failure"

        return self


    def get_current_config(self, input_config):
        """
        Retrieves the current configuration of an access point in Cisco Catalyst Center.

        Parameters:
          - self (object): An instance of the class containing the method.
          - input_config (dict): A dictionary containing the input configuration details.
        Returns:
            A tuple containing a boolean indicating if the access point exists and a
            dictionary of the current configuration based on the input given from
            playbook either mac_address or management_ip_address or hostname
            (
                True
                {
                    "ap_name": "NFW-AP1-9130AXE",
                    "eth_mac": "34:5d:a8:0e:20:b4",
                    "led_brightnessLevel": 3,
                    "led_status": "Enabled",
                    "location": "LTTS",
                    "mac_address": "90:e9:5e:03:f3:40"
                }
            )
        Description:
            Queries the Cisco Catalyst Center for the existence of an Access Point
            using the provided input configuration details such as MAC address,
            management IP address, or hostname. If found, it retrieves the current
            Access Point configuration and returns it.
        """
        accesspoint_exists = False
        current_configuration = {}
        ap_response = None
        input_param = {}
        self.keymap = self.map_config_key_to_api_param(self.keymap, input_config)

        for key in ['mac_address', 'management_ip_address', 'hostname']:
            if input_config.get(key):
                input_param[self.keymap[key]]= input_config[key]
                break

        if not input_param:
            self.log("""Required param of mac_address, management_ip_address or hostname
                      is not in playbook config""","ERROR")
            return (accesspoint_exists, current_configuration)

        try:
            ap_response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                op_modifies=True,
                params=input_param,
            )

            if ap_response and ap_response.get("response"):
                ap_response = self.camel_to_snake_case(ap_response["response"])
                device_fields = self.payload.get("config")[0].get("device_fields")

                if device_fields is None or device_fields == "" or device_fields == "all":
                    self.payload["device_list"] = ap_response[0]
                else:
                    self.payload["device_list"]=self.data_frame(device_fields,ap_response)

                self.log("Received API response from 'get_device_list': {0}"\
                        .format(str(self.payload["device_list"][0])), "DEBUG")

                ap_ethernet_mac_address = ap_response[0]["ap_ethernet_mac_address"]
                accesspoint_exists, current_configuration = self.get_accesspoint_config(
                ap_ethernet_mac_address)

        except Exception as e:
            self.log("The provided device '{0}' is either invalid or not present in the Cisco Catalyst Center."\
                     .format(str(input_param) + str(e)), "WARNING")

        return (accesspoint_exists, current_configuration)


    def get_accesspoint_config(self, ap_ethernet_mac_address):
        """
        Retrieves the access point configuration data from Cisco Catalyst Center.

        Parameters:
          - self (object): An instance of the class containing the method.
          - ap_ethernet_mac_address (str): The Ethernet MAC address of the access point.
          - tuple: A tuple containing a boolean indicating if the access point exists and
            a dictionary of the current configuration.
        Returns:
            (
                True
                {
                    "ap_name": "NFW-AP1-9130AXE",
                    "eth_mac": "34:5d:a8:0e:20:b4",
                    "led_brightnessLevel": 3,
                    "led_status": "Enabled",
                    "location": "LTTS",
                    "mac_address": "90:e9:5e:03:f3:40"
                }
            )
        Description:
            Requests the current configuration of an access point from the Cisco Catalyst Center
            using the Ethernet MAC address. The response is then processed and returned
            as a dictionary.
        """
        input_param = {}
        input_param["key"] = ap_ethernet_mac_address
        current_configuration = {}

        try:
            ap_config_response = self.dnac._exec(
                family="wireless",
                function='get_access_point_configuration',
                params=input_param,
            )

            if ap_config_response:
                self.keymap = self.map_config_key_to_api_param(self.keymap, ap_config_response)
                current_configuration = self.camel_to_snake_case(ap_config_response)
                self.log("Received API response from 'get_access_point_configuration': {0}"\
                            .format(str(current_configuration)), "DEBUG")
                ap_selected_field = self.payload.get("config")[0].get("ap_selected_field")

                if ap_selected_field is None or ap_selected_field == "" \
                    or ap_selected_field == "all":
                    self.payload["device_config"] = current_configuration
                else:
                    self.payload["device_config"]=self.data_frame(ap_selected_field,
                                                                  [current_configuration])

                self.log("AP configuration {0} exists in Cisco Catalyst Center"\
                            .format(str(self.payload["device_config"][0])), "INFO")
                accesspoint_config_exists = True
            return (accesspoint_config_exists, current_configuration)

        except Exception as e:
            self.log("Unable to get the Accesspoint configuratoin for '{0}' ."\
                        .format(str(input_param) + str(e)), "WARNING")
            return None


    def compare_ap_config_with_inputdata(self, current_ap_config):
        """
        Compares the desired AP configuration with the current configuration and identifies
        changes.
        Parameters:
            - ap_config: Response of the get_have containing the current AP configuration.
        Returns:
            This will be the return the final data for update AP detail.
            dict: Configuration updates needed to match the desired AP configuration.
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
            final_input_data = functions.compare_ap_config_with_inputdata(current_ap_config)
        """
        update_config = {}

        if self.want and current_ap_config:

            if self.want.get("mac_address") == current_ap_config["mac_address"] or \
                    self.want.get("hostname") == current_ap_config["ap_name"]:
                allkey = list(self.want.keys())

                excluded_keys = ("mac_address", "hostname", "management_ip_address")
                for value in excluded_keys:
                    if value in allkey: allkey.remove(value)

                for each_key in allkey:

                    if each_key == "ap_name_new":
                        if self.want["ap_name_new"] != current_ap_config.get("ap_name"):
                            update_config["apNameNew"] = self.want["ap_name_new"]
                    elif each_key == "ap_name":
                        update_config[self.keymap[each_key]] = self.want[each_key]
                    else:

                        if self.want[each_key] != current_ap_config[each_key]:
                            update_config[self.keymap[each_key]] = self.want[each_key]

                if update_config.get("apName") is not None and update_config.get("apNameNew") is None:
                    del update_config["apName"]

                if update_config:
                    update_config["macAddress"] = current_ap_config["eth_mac"]

            if update_config:
                return update_config
            else:
                self.log('Playbook AP Configuration remain same in Current AP configration',
                      "INFO")
                return None


    def update_ap_configuration(self, ap_config):
        """
        Updates the Access Point (AP) configuration based on the provided device data.
        Parameters:
              - ap_config: Final input config data response from compare_ap_config_with_inputdata
              - dict: A dictionary containing the task ID and URL from the update response.
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
            final_input_data = functions.update_ap_configuration(ap_config)
        """

        try:
            self.log("Updating access point configuration information: "+ ap_config["macAddress"],
                        "INFO")
            ap_config["adminStatus"] = True

            if ap_config.get("apName") is not None:
                ap_config["apList"] = [dict(apName = ap_config["apName"],
                                    apNameNew = ap_config["apNameNew"],
                                    macAddress = ap_config["macAddress"])]
                del ap_config["apName"]
                del ap_config["apNameNew"]
            elif ap_config.get("macAddress") is not None:
                ap_config["apList"] = [dict(macAddress = ap_config["macAddress"])]

            if ap_config.get("location") is not None:
                ap_config["configureLocation"] = True

            if ap_config.get("ledBrightnessLevel") is not None:
                ap_config["configureLedBrightnessLevel"] = True

            if ap_config.get("ledStatus") is not None:
                ap_config["configureLedStatus"] = True
                ap_config["ledStatus"] = True if ap_config["ledStatus"] == "Enabled" else False

            for key_to_remove in ("mac_address", "hostname", "management_ip_address"):
                if ap_config.get(key_to_remove): del ap_config[key_to_remove]

            response = self.dnac._exec(
                    family="wireless",
                    function='configure_access_points',
                    op_modifies=True,
                    params=ap_config,
                )

            self.log("Response of Access Point Configuration: {0}"\
                     .format(str(response["response"])), "INFO")
            return dict(macAdress=ap_config["macAddress"], response=response["response"])

        except Exception as e:
            self.log("AP config update Error {0}".format(str(ap_config["macAddress"])+str(e)), "ERROR")
            return None

    def data_frame(self, fields_to_include=None, records=list):
        """
        Filters the input data to include only the specified fields.
        Parameters:
           - fieldlist (str): Comma-separated string of keys to display.
           - records (list of dict): A list of dictionaries with only the specified fields.
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
            final_input_data = functions.data_frame(device_fields, device_records)
        """
        try:
            if records is None:
                return []

            records = self.camel_to_snake_case(records)

            if not fields_to_include or fields_to_include.strip() == '':
                return records

            field_names = [field.strip() for field in fields_to_include.split(",")]
            filtered_data = []

            for record in records:
                filtered_record = {}

                for field in field_names:
                    filtered_record[field] = record.get(field)

                filtered_data.append(filtered_record)

            return filtered_data

        except Exception as e:
            self.log("Unable to filter fields: {0}".format(str(e)) , "ERROR")
            return None


    def map_config_key_to_api_param(self, keymap=any, data=any):
        """
        Converts keys in a dictionary from CamelCase to snake_case and creates a keymap.
        Parameters:
          - keymap: type Dict : Already any Key map dict was available add here or empty dict.{}
          - data: Type :Dict : Which key need do the key map use the data {}
            eg: Device list response or AP config response as a input
          - dict: A dictionary with the original keys as values and the converted snake_case keys as keys.
        Returns:
            {
                {
                    "mac_address": "macAddress",
                    "ap_name": "apName"
                }
            }
        Example:
            functions = Accesspoint(module)
            keymap = functions.map_config_key_to_api_param(keymap,device_data)
        """
        if keymap is None:
           keymap = {}

        if isinstance(data, dict):
            keymap.update(keymap)

            for key, value in data.items():
                new_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key).lower()
                keymap[new_key] = key

                if isinstance(value, dict):
                    self.map_config_key_to_api_param(keymap, value)
                elif isinstance(value, list):

                    for item in value:
                        if isinstance(item, dict):
                            self.map_config_key_to_api_param(keymap, item)

        elif isinstance(data, list):

            for item in data:
                if isinstance(item, dict):
                    self.map_config_key_to_api_param(keymap, item)

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
            time.sleep(5)
            ccc_network.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_network.result)


if __name__ == '__main__':
    main()

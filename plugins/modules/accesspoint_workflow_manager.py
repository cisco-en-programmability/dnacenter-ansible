#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Megha Kandari, Sonali Deepthi Kesali, Natarajan, Madhan Sankaranarayanan, Abhishek Maheshwari")

DOCUMENTATION = r"""
---
module: accesspoint_workflow_manager
short_description: accesspoint_workflow_manager used to automate bulk AP configuration changes.
description:
  - Automates bulk configuration changes for Access Point (APs).
  - Modify AP display names, AP names, or other parameters.
  - Filter specific device details, such as selecting devices with hostnames matching "NFW-AP1-9130AXE"
  - Compares input details with current AP configurations and applies desired changes only to relevant APs.

version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.accesspoint_workflow_manager
author: 
    - A Mohamed Rafeek (@mohamedrafeek)
    - Sonali Deepthi Kesali (@sonalideepthi)
    - Megha Kandari (@meghakandari)
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
        description: It represents a list of details for Updating site of an access point.
    type: list
    elements: dict
    required: True
    suboptions:
        ap_type:
            description: Specifies the access point type used to facilitate seamless mobility between different sites within a network infrastructure.
            type :str
            example: "Unified AP"
        mac_address:
            description: "MAC address of the Access Point (e.g., '90:e9:5e:03:f3:40')."
            type: str
            example: "90:e9:5e:03:f3:40"  # Replace with actual MAC address
        rf_profile:
            description: "Radio Frequency (RF) profile of the Access Point (e.g., 'HIGH')."
            type: str
            example: "HIGH"
        site:
            description: "Current site details where the Access Point is located."
            type: object
            suboptions:
                floor:
                    description: "Floor details of the current site."
                    type: object
                    suboptions:
                        name:
                            description: "Name of the floor (e.g., 'FLOOR1')."
                            type: str
                        parent_name:
                    description: "Parent name of the floor in the site hierarchy (e.g., 'Global/USA/New York/BLDNYC')."
                    type: str
        dest_site:
            description: "Destination site details where the Access Point will be moved."
            type: object
            suboptions:
                floor:
                description: "Floor details of the destination site."
                type: object
                suboptions:
                    name:
                        description: "Name of the floor (e.g., 'FLOOR2')."
                        type: str
                    parent_name:
                        description: "Parent name of the floor in the site hierarchy (e.g., 'Global/USA/New York/BLDNYC')."
                        type: str
        type:
            description: "Type of site detail provided (e.g., 'floor')."
            type: str
            example: "floor"


    config:
        description: List of details of AP being managed
    type: list
    elements: dict
    required: True

    mac_address:
        description: |
            MAC Address field used to identify the device. If MAC address is known,
            it must be provided. This field cannot be modified.
            To identify the specific access point any one of the (mac_address, hostname,
            management_ip_address) 3 param is required.
            Example: mac_address: "90:e9:5e:03:f3:40"
        type: str
        required: True
    hostname:
        description: |
            Device hostname used to identify the device.
            To identify the specific access point any one of the (mac_address, hostname,
            management_ip_address) 3 param is required.
            Example: hostname: "NFW-AP1-9130AXE"
        type: str
        required: True
    management_ip_address:
        description: |
            Management IP address used to identify the device based on IP.
            This is an alternative if MAC address or hostname is not available.
            To identify the specific access point any one of the (mac_address, hostname,
            management_ip_address) 3 param is required.
            Example: management_ip_address: "204.192.6.200"
        type: str
        required: True

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

    ap_selected_fields:
        description:
            - Optional field to specify specific fields to display from the AP device details.
            - Below list of available fields to display the output in the "access_point_list"
                "type,memory_size,last_update_time,device_support_level,software_type,software_version,
                serial_number,mac_address,inventory_status_detail,collection_interval,
                dns_resolved_management_address,management_state,pending_sync_requests_count,
                reasons_for_device_resync,reasons_for_pending_sync_requests,up_time,role_source,
                last_updated,boot_date_time,ap_manager_interface_ip,collection_status,family,
                hostname,location_name,management_ip_address,platform_id,reachability_failure_reason,
                reachability_status,series,snmp_contact,snmp_location,tag_count,tunnel_udp_port,
                uptime_seconds,vendor,waas_device_mode,associated_wlc_ip,ap_ethernet_mac_address,
                error_code,error_description,interface_count,last_device_resync_start_time,line_card_count,
                line_card_id,managed_atleast_once,description,location,role,instance_tenant_id,
                instance_uuid,id"
            - Fields should be separated by commas without spaces before or after the commas.
            - If not defined, all device fields are shown by default.
            - Example: "id,hostname,family,type,mac_address,management_ip_address,ap_ethernet_mac_address,last_updated,up_time"
        type: str
        required: False
    ap_config_selected_fields:
        description:
            - Optional field to specify specific parameters from the Access Point configuration details.
            - Below list of available fields to display the output in the "have" or "access_point_config"
                "instance_uuid,instance_id,auth_entity_id,auth_entity_class,instance_tenant_id,
                _ordered_list_oeindex,_ordered_list_oeassoc_name,_creation_order_index,_is_being_changed,
                deploy_pending,instance_created_on,instance_updated_on,change_log_list,instance_origin,
                instance_version,admin_status,ap_height,ap_mode,ap_name,eth_mac,failover_priority,
                led_brightness_level,led_status,location,mac_address,primary_controller_name,primary_ip_address,
                secondary_controller_name,secondary_ip_address,tertiary_controller_name,tertiary_ip_address,
                mesh_dtos,radio_dtos,internal_key,display_name,lazy_loaded_entities"
            - Each field should be separated by commas without spaces.
            - If not defined, all fields will be shown by default.
            - Example: "mac_address,eth_mac,ap_name,led_brightness_level,led_status,location"
        type: str
        required: False

requirements:
- dnacentersdk >= 2.4.5
- python >= 3.8
notes:
  - SDK Method used are 

    devices.get_device_list
    wireless.get_access_point_configuration
    sites.get_site
    sites.get_membership
    wireless.ap_provision
    wireless.configure_access_points

  - Paths used are
    get /dna/intent/api/v1/network-device
    get /dna/intent/api/v1/wireless/accesspoint-configuration/summary?key={ap_ethernet_mac_address}
    get /dna/intent/api/v1/site
    post /dna/intent/api/v1/wireless/ap-provision
    post /dna/intent/api/v2/wireless/accesspoint-configuration
"""

EXAMPLES = r"""
- name: Provision/Move/Update Wireless Access Point Configuration
  hosts: dnac_servers
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"
  tasks:
  - name: Create/Update Wireless Access Point Configuration
  hosts: dnac_servers
  connection: local
  gather_facts: no
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Provision AP to Site with RF properties
      cisco.dnac.accesspoint_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: True
        dnac_log_level: DEBUG
        config_verify: True
        state: merged
        config:
          - site:
              devices:
                host_name: "NFW-AP1-9130AXE"
                family: "Unified AP"
                mac_address: "90:e9:5e:03:x3:400"
                management_ip_address: "204.1.216.2"
                # serial_number: "FJC27101PRX"
                # image_version: "17.14.0.79"
                rf_profile: "HIGH"
              floor:
                name: "FLOOR2"
                parent_name: "Global/USA/New York/BLDNYC"
                rf_model: "Cubes And Walled Offices"
            site_type: "floor"
      register: result
    - name: Display provisioning result
      debug:
        var: result

    - name: Updating Access Point Site details
      cisco.dnac.accesspoint_movement:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: True
        dnac_log_level: DEBUG
        config_verify: True
        state: merged
        config:
              - ap_type: "Unified AP"
                mac_address:  90:e9:5e:03:f3:40
                rf_profile: "HIGH"
                site:
                  floor:
                    name: "FLOOR1"
                    parent_name: "Global/USA/New York/BLDNYC"
                dest_site:
                  floor:
                    name: "FLOOR2"
                    parent_name: "Global/USA/New York/BLDNYC"
                type: floor
      register: output_list
    - name: Display Accesspoint movement results
      debug:
        var: output_list

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
          - mac_address: "90:e9:5e:03:f3:40"
            ap_name: "LTTS-Test1"
            ap_name_new: "NFW-AP1-9130AXE"
            ap_selected_fields: "id,hostname,mac_address,management_ip_address,ap_ethernet_mac_address"
            ap_config_selected_fields: "mac_address,eth_mac,ap_name"
      register: output_list

    - name: Updating Access Point few field changes in configuration
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
          - mac_address: "68:7d:b4:06:b0:a0"
            led_brightness_level: 2
            led_status: "Enabled"
            location: "LTTS/Cisco/Bangalore"
            ap_name: "AP687D.B402.1E98"
            ap_name_new: "LTTS-Test01"
            ap_mode: "Monitor"
            admin_status: "Enabled"
            failover_priority: "Medium"
            ap_selected_fields: "id,hostname,family,type,mac_address,management_ip_address,ap_ethernet_mac_address,last_updated,up_time"
            ap_config_selected_fields: "mac_address,eth_mac,ap_name,led_brightness_level,led_status,location"
      register: output_list

    - name: Updating Access Point all field changes in configuration
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
          - ap_selected_fields: "id,hostname,family,type,mac_address,management_ip_address,ap_ethernet_mac_address,last_updated,up_time"
            ap_config_selected_fields: "mac_address,eth_mac,ap_name,led_brightness_level,led_status,location,radioDTOs"
            mac_address: "68:7d:b4:06:b0:a0"
            led_brightness_level: 2
            led_status: "Enabled"
            location: "LTTS/Cisco/Bangalore"
            ap_name: "AP687D.B402.1E98"
            ap_name_new: "LTTS-Test01"
            ap_mode: "Monitor"
            admin_status: "Enabled"
            failover_priority: "Medium"
            radio_dtos:
              - admin_status: "Enabled"
                antenna_gain: 4
                radio_role_assignment: "Auto"
                clean_air_si: "Enabled"
                antenna_cable_name: "other"
                antenna_pattern_name: "AntennaPatternName"
                radio_band: "2.4 GHz"
                cable_loss: 75
                channel_assignment_mode: "Custom"
                channel_number: 36
                channel_width: "20 MHz"
                power_assignment_mode: "Global"
                powerlevel: 1
                radio_type: "2.4 GHz"
                slot_id: 0
                antenna_angle: 0
                antenna_elev_angle: 0
              - admin_status: "Enabled"
                antenna_gain: 4
                radio_role_assignment: "Auto"
                clean_air_si: "Enabled"
                antenna_cable_name: "other"
                antenna_pattern_name: "AntennaPatternName"
                radio_band: "5 GHz"
                cable_loss: 75
                channel_assignment_mode: "Global"
                channel_number: 40
                channel_width: "40 MHz"
                power_assignment_mode: "Global"
                powerlevel: 2
                radio_type: "5 GHz"
                slot_id: 1
                antenna_angle: 0
                antenna_elev_angle: 0

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

import re, time, json
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    validate_str,
    get_dict_result,
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
        accesspoint_spec = {
            "mac_address": {"required": False, "type": "str"},
            "management_ip_address": {"required": False, "type": "str"},
            "hostname": {"required": False, "type": "str"},
            "admin_status": {"required": False, "type": "str"},
            "led_brightness_level": {"required": False, "type": "int"},
            "led_status": {"required": False, "type": "str"},
            "location": {"required": False, "type": "str"},
            "ap_name": {"required": False, "type": "str"},
            "ap_name_new": {"required": False, "type": "str"},
            "ap_mode": {"required": False, "type": "str"},
            "failover_priority": {"required": False, "type": "str"},
            "primary_controller_name": {"required": False, "type": "str"},
            "primary_ip_address": {"required": False, "type": "dict"},
            "secondary_controller_name": {"required": False, "type": "str"},
            "secondary_ip_address": {"required": False, "type": "dict"},
            "tertiary_controller_name": {"required": False, "type": "str"},
            "tertiary_ip_address": {"required": False, "type": "dict"},
            "radio_dtos": {"required": False, "type": "list", "elements": "dict"},
            "ap_selected_fields": {"required": False, "type": "str"},
            "ap_config_selected_fields": {"required": False, "type": "str"}
        }

        radio_config_list = aplist[0].get("radio_dtos")
        valid_param_radio, invalid_params_radio = (None, None)
        if aplist[0].get("radio_dtos"):
            radio_config_sepc = {
                "admin_status": {"required": False, "type": "str"},
                "antenna_gain": {"required": False, "type": "int"},
                "radio_role_assignment": {"required": False, "type": "str"},
                "antenna_cable_name": {"required": False, "type": "str"},
                "antenna_pattern_name": {"required": False, "type": "str"},
                "radio_band": {"required": True, "type": "str"},
                "cable_loss": {"required": False, "type": "int"},
                "channel_assignment_mode": {"required": False, "type": "str"},
                "channel_number": {"required": False, "type": "int"},
                "channel_width": {"required": False, "type": "str"},
                "power_assignment_mode": {"required": False, "type": "str"},
                "powerlevel": {"required": False, "type": "int"},
                "radio_type": {"required": True, "type": "str"},
                "clean_air_si": {"required": False, "type": "str"},
                "slot_id": {"required": False, "type": "int"},
                "antenna_angle": {"required": False, "type": "int"},
                "antenna_elev_angle": {"required": False, "type": "int"},
            }
            valid_param_radio, invalid_params_radio = \
                validate_list_of_dicts(radio_config_list, radio_config_sepc)

        valid_param, invalid_params = validate_list_of_dicts(aplist, accesspoint_spec)

        if invalid_params or invalid_params_radio:
            self.msg = "Invalid parameters in playbook: {0} ".format(
                "\n".join(invalid_params) + "\n".join(invalid_params_radio)
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_param
        self.msg = "Successfully validated playbook config params:{0}".format(
            self.pprint(valid_param[0]))
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
        'ap_selected_fields' and 'ap_config_selected_fields'. The extracted information is stored in the 
        'want' attribute of the instance for later use in the workflow.
        """
        want = {}

        for key,value in ap_config.items():
            if key not in ("ap_selected_fields", "ap_config_selected_fields"):
                if ap_config.get(key) is not None:
                    want[key] = value

        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")
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
          ap_config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method determines whether to update or create AP configuration in Cisco
            Catalyst Center based on the provided configuration information.
            If the specified access point exists, the method checks if it requires an update
            by calling the 'update_ap_configuration' method. If an update is required,
            it calls the 'configure_access_points' function from the 'wireless' family of
            the Cisco Catalyst Center API. If Current configuration same as input configuration
            does not require an update, the method exits, indicating that Accesspoint
            configuration is up to date.
        """
        task_response = None
        self.valid_ap_config_parameters(ap_config).check_return_status()

        # check if the given AP config exists and/or needs to be updated/created.
        if self.have.get("ap_exists"):
            consolidated_data = self.compare_ap_config_with_inputdata(
                self.have["current_ap_config"])

            if not consolidated_data:
                # Accesspoint does not need update
                self.msg = "AP - {0} does not need any update"\
                    .format(self.have.get("current_ap_config").get("ap_name"))
                self.log(self.msg, "INFO")
                responses = {}
                del self.payload["access_point_list"]
                responses["accesspoints_updates"] = {
                    "response": self.payload["access_point_config"]}
                self.result['msg'] = self.msg
                self.result["response"].append(responses)
                self.result["changed"] = False
                return self

            self.log('Final AP Configuration data to update {0}'.format(self.pprint(
                consolidated_data)), "INFO")
            task_response = self.update_ap_configuration(consolidated_data)
            self.log('Task respoonse {0}'.format(str(task_response)),"INFO")

            if task_response and isinstance(task_response, dict):
                self.check_task_response_status(task_response, "task_intent", True)\
                    .check_return_status()
                self.log("Status of the task is {0}.".format(self.status), "INFO")
                if self.status == "success":
                    self.result['changed'] = True
                    responses = {}
                    responses["accesspoints_updates"] = {"response": task_response}
                    self.msg = "AP Configuration - {0} updated Successfully"\
                        .format(self.have["current_ap_config"].get("ap_name"))
                    self.log(self.msg, "INFO")
                    self.result['msg'] = self.msg
                    self.result['response'].append(responses)
                else:
                    self.status = "failed"
                    self.msg = "Unable to get task response, hence AP config not updated"
                    self.log(self.msg, "ERROR")
                return self
            self.status = "failed"
            self.msg = "Unable to call update AP config API "
            self.log(self.msg, "ERROR")
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
            self.status = "failed"
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
                                                "have": self.payload["access_point_config"],
                                                "message": msg}
            self.result['response'].append(responses)
        else:
            self.msg = "Configuration for AP '{0}' does not match the desired state."\
                .format(ap_name)
            self.log(self.msg, "INFO")
            self.status = "failed"

        return self

    def valid_ap_config_parameters(self, ap_config):
        """
        Addtional validation for the update API AP configuration payload.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - ap_config (dict): A dictionary containing the input configuration details.
        Returns:
          The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
        Description:
            Example:
                To use this method, create an instance of the class and call 
                'valid_ap_config_parameters' on it. If the validation succeeds it return 'success'.
                If it fails, 'self.status' will be 'failed', and
                'self.msg' will describe the validation issues.To use this method, create an
                instance of the class and call 'valid_ap_config_parameters' on it.
                If the validation succeeds, this will allow to go next step, 
                unless this will stop execution based on the fields.
        """
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

        if ap_config.get("ap_mode") not in ("Local", "Monitor", "Sniffer",
                                             "Bridge"):
            errormsg.append("ap_mode: Invalid value '{0}' for ap_mode in playbook. Must be one of:\
                              Local, Monitor, Sniffer or Bridge."\
                            .format(ap_config.get("ap_mode")))

        if ap_config.get("admin_status") not in ("Enabled", "Disabled"):
            errormsg.append("admin_status: Invalid value '{0}' for admin_status in playbook.\
                             Must be either 'Enabled' or 'Disabled'."\
                            .format(ap_config.get("admin_status")))

        if ap_config.get("failover_priority") not in ("Low", "Medium", "High", "Critical"):
            errormsg.append("failover_priority: Invalid value '{0}' for failover_priority in playbook.\
                             Must be one of:  Low, Medium, High or Critical."\
                            .format(ap_config.get("failover_priority")))

        if ap_config.get("primary_controller_name"):
            if ap_config["primary_controller_name"] == "":
                errormsg.append("primary_controller_name: Invalid primary controller name '{0}' \
                                in playbook. Please select one of: Inherit from site/Clear or \
                                Controller name."\
                                .format(ap_config["primary_controller_name"]))

        if ap_config.get("secondary_controller_name"):
            if ap_config["secondary_controller_name"] == "":
                errormsg.append("secondary_controller_name: Invalid Secondary Controller Name '{0}' \
                                in playbook. Please select one of: Inherit from site/Clear or \
                                controller name."\
                                .format(ap_config["secondary_controller_name"]))

        if ap_config.get("tertiary_controller_name"):
            if ap_config["tertiary_controller_name"] == "":
                errormsg.append("tertiary_controller_name: Invalid Tertiary Controller Name '{0}' \
                                in playbook. Please select: Clear or Controller name."\
                                .format(ap_config["tertiary_controller_name"]))

        if ap_config.get("primary_ip_address"):
            if not self.is_valid_ipv4(ap_config["primary_ip_address"]["address"]):
                errormsg.append("primary_ip_address: Invalid Primary IP Address '{0}' in playbook"\
                                .format(ap_config["primary_ip_address"]))

        if ap_config.get("secondary_ip_address"):
            if not self.is_valid_ipv4(ap_config["secondary_ip_address"]["address"]):
                errormsg.append("secondary_ip_address: Invalid Secondary IP Address '{0}' in playbook"\
                                .format(ap_config["secondary_ip_address"]))

        if ap_config.get("tertiary_ip_address"):
            if not self.is_valid_ipv4(ap_config["tertiary_ip_address"]["address"]):
                errormsg.append("tertiary_ip_address: Invalid Tertiary IP Address '{0}' in playbook"\
                                .format(ap_config["tertiary_ip_address"]))

        if ap_config.get("dual_radio_mode") and \
            ap_config.get("dual_radio_mode") not in ["Auto", "Enable", "Disable"]:
            errormsg.append("dual_radio_mode: Invalid value '{0}' for Dual Radio Mode in playbook.\
                             Must be one of: Auto, Enable, Disable."\
                            .format(ap_config.get("dual_radio_mode")))

        if ap_config.get("radio_dtos"):
            for each_radio in ap_config["radio_dtos"]:
                if each_radio.get("admin_status") not in ("Enabled", "Disabled"):
                    errormsg.append("admin_status: Invalid value '{0}' for admin_status in playbook.\
                             Must be either 'Enabled' or 'Disabled'."\
                            .format(each_radio.get("admin_status")))

                if each_radio.get("clean_air_si") not in ("Enabled", "Disabled"):
                    errormsg.append("clean_air_si: Invalid value '{0}' for clean air si in playbook.\
                             Must be either 'Enabled' or 'Disabled'."\
                            .format(each_radio.get("clean_air_si")))

                if each_radio.get("antenna_gain"):
                    if each_radio["antenna_gain"] not in range(1,10):
                        errormsg.append("antenna_gain: Invalid Antenna Gain '{0}' in playbook"\
                                .format(each_radio["antenna_gain"]))

                if each_radio.get("channel_assignment_mode") not in ("Global", "Custom"):
                    errormsg.append("channel_assignment_mode: Invalid value '{0}' \
                        for Channel Assignment Mode in playbook. \
                        Must be either 'Global' or 'Custom'."\
                        .format(each_radio.get("channel_assignment_mode")))

                allowed_channel_no = (36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,
                                      132,136,140,144,149,153,157,161,165,169,173)
                if each_radio.get("channel_number"):
                    if each_radio.get("channel_number") not in allowed_channel_no:
                        errormsg.append("channel_number: Invalid value '{0}' \
                            for Channel Number in playbook. Must be one of: {1}."\
                            .format(each_radio.get("channel_assignment_mode"),
                                 ",".join(allowed_channel_no)))

                if each_radio.get("channel_width"):
                    if each_radio.get("channel_width") not in ("20 MHz", "40 MHz", "80 MHz", "160 MHz"):
                        errormsg.append("channel_width: Invalid value '{0}' \
                        for Channel width in playbook. \
                        Must be one of: '20 MHz', '40 MHz', '80 MHz', or '160 MHz'."\
                        .format(each_radio.get("channel_width")))

                if each_radio.get("power_assignment_mode") not in ("Global", "Custom"):
                    errormsg.append("power_assignment_mode: Invalid value '{0}' \
                        for Power assignment mode in playbook. \
                        Must be either 'Global' or 'Custom'."\
                        .format(each_radio.get("power_assignment_mode")))

                if each_radio.get("powerlevel"):
                    if each_radio["powerlevel"] not in range(1,9):
                        errormsg.append("powerlevel: Invalid Power level '{0}' in playbook"\
                                .format(each_radio["powerlevel"]))

                if each_radio.get("radio_type"):
                    if each_radio.get("radio_type") not in ("2.4 GHz", "5 GHz", "XOR", "6 GHz"):
                        errormsg.append("radio_type: Invalid value '{0}' \
                        for Radio type in playbook. \
                        Must be one of: '2.4 GHz', '5 GHz', 'XOR', or '6 GHz'."\
                        .format(each_radio.get("radio_type")))

                if each_radio.get("radio_type") == "6 GHz":
                    set_flag = False
                    allowed_series = ["9136I", "9162I", "9163E", "9164I", "IW9167IH", "9178I", "9176I", "9176D1"]
                    for series in allowed_series:
                        pattern = rf'\b{series}\b'
                        match = re.search(pattern, self.payload["access_point_list"][0]["series"],\
                                          re.IGNORECASE)
                        if match:
                            set_flag = True
                            break
                    if set_flag == False:
                        errormsg.append("Access Point series '{0}' not supported for the radio type {1} \
                                        allowed series {2} "\
                                .format(self.payload["access_point_list"][0]["series"],
                                        each_radio["radio_type"], ", ".join(allowed_series)))

                if each_radio.get("antenna_pattern_name"):
                    param_spec = dict(type = "str", length_max = 255)
                    validate_str(each_radio["antenna_pattern_name"], param_spec,
                                 "antenna_pattern_name", errormsg)

                if each_radio.get("radio_band") not in ("2.4 GHz", "5 GHz"):
                    errormsg.append("radio_band: Invalid value '{0}' for Radio band in playbook.\
                        Must be either '2.4 GHz' or '5 GHz'."\
                        .format(each_radio.get("radio_band")))

                if each_radio.get("radio_role_assignment") not in ("Auto", "Client-Serving", "Monitor"):
                    errormsg.append("radio_role_assignment: Invalid value '{0}' \
                                    for radio role assignment in playbook.\
                        Must be one of: 'Auto', 'Monitor' or 'Client-Serving'."\
                        .format(each_radio.get("radio_role_assignment")))

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: '{0}' "\
                     .format(str("\n".join(errormsg)))
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.msg = "Successfully validated config params:{0}".format(str(ap_config))
        self.log(self.msg, "INFO")
        self.status = "success"
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
        self.keymap["mac_address"] = "macAddress"
        self.keymap["management_ip_address"] = "managementIpAddress"
        self.keymap["mac_address"] = "macAddress"
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
                ap_selected_fields = self.payload.get("config")[0].get("ap_selected_fields")

                if ap_selected_fields is None or ap_selected_fields == "" or \
                    ap_selected_fields == "all":
                    self.payload["access_point_list"] = ap_response
                else:
                    self.payload["access_point_list"]=self.data_frame(ap_selected_fields,
                                                                      ap_response)

                self.log("Received API response from 'get_device_list': {0}"\
                        .format(self.pprint(self.payload["access_point_list"][0])), "DEBUG")

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
                            .format(self.pprint(current_configuration)), "DEBUG")
                ap_config_selected_fields = self.payload.get("config")[0].get("ap_config_selected_fields")

                if ap_config_selected_fields is None or ap_config_selected_fields == "" \
                    or ap_config_selected_fields == "all":
                    self.payload["access_point_config"] = [current_configuration]
                else:
                    self.payload["access_point_config"]=self.data_frame(ap_config_selected_fields,
                                                                  [current_configuration])

                self.log("AP configuration {0} exists in Cisco Catalyst Center"\
                            .format(str(self.payload["access_point_config"][0])), "INFO")
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
                configurable_keys = list(self.want.keys())

                excluded_keys = ("mac_address", "hostname", "management_ip_address")
                for value in excluded_keys:
                    if value in configurable_keys: configurable_keys.remove(value)

                for each_key in configurable_keys :
                    if each_key == "ap_name_new":
                        if self.want["ap_name_new"] != current_ap_config.get("ap_name"):
                            update_config["apNameNew"] = self.want["ap_name_new"]
                    elif each_key == "ap_name":
                        update_config[self.keymap[each_key]] = self.want[each_key]
                    elif each_key in ("primary_ip_address", "secondary_ip_address", "tertiary_ip_address"):
                        if current_ap_config.get(each_key) != self.want.get(each_key):
                            update_config[self.keymap[each_key]] = {}
                            update_config[self.keymap[each_key]]["address"] = self.want[each_key]["address"]
                    elif each_key == "radio_dtos" and self.want.get(each_key):
                        want_dtos = self.want[each_key]
                        temp_dtos_list = []
                        for each_dtos in want_dtos:
                            dtos_keys = list(each_dtos.keys())
                            temp_dtos = {}
                            for dto_key in dtos_keys:
                                temp_dtos[self.keymap[dto_key]] = each_dtos[dto_key]
                            temp_dtos_list.append(temp_dtos)
                        update_config["radioConfigurations"] = temp_dtos_list
                    else:
                        if self.want[each_key] != current_ap_config.get(each_key):
                            update_config[self.keymap[each_key]] = self.want[each_key]

                if update_config.get("apName") is not None and update_config.get("apNameNew") is None:
                    del update_config["apName"]

                if self.want.get("primary_controller_name") == "Inherit from site/Clear":
                    update_config[self.keymap["primary_ip_address"]] = {}
                    update_config[self.keymap["primary_ip_address"]]["address"] = \
                        self.payload["access_point_list"][0]["associated_wlc_ip"]
                    update_config[self.keymap["primary_controller_name"]] = \
                        self.want["primary_controller_name"]
                    self.want["primary_ip_address"] = {}
                    self.want["primary_ip_address"]["address"] = \
                        self.payload["access_point_list"][0]["associated_wlc_ip"]

                if update_config:
                    update_config["macAddress"] = current_ap_config["eth_mac"]

            if update_config:
                self.log("Consolidated config to update AP configuration: {0}"\
                         .format(self.pprint(update_config)), "INFO")
                return update_config

            self.log('Playbook AP configuration remain same in current AP configration', "INFO")
            return None

    def update_ap_configuration(self, ap_config):
        """
        Updates the Access Point (AP) configuration based on the provided device data.
        Parameters:
              - ap_config: Final input config data response from compare_ap_config_with_inputdata
              - dict: A dictionary containing the task ID and URL from the update response.
        Returns:
            {
                "mac_address": "string",
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
            self.log("Updating access point configuration information: {0}"\
                     .format(ap_config[self.keymap["mac_address"]]), "INFO")
            ap_config["adminStatus"] = True
            ap_config["configureAdminStatus"] = True

            ap_config["apList"] = []
            temp_dict = {}

            if ap_config.get(self.keymap["ap_name"]) is not None:
                temp_dict[self.keymap["ap_name"]] = ap_config.get(self.keymap["ap_name"])
                temp_dict["apNameNew"] = ap_config["apNameNew"]
                temp_dict[self.keymap["mac_address"]] = ap_config[self.keymap["mac_address"]]
                del ap_config[self.keymap["ap_name"]]
                del ap_config["apNameNew"]
            elif ap_config.get(self.keymap["mac_address"]) is not None:
                temp_dict[self.keymap["mac_address"]] = ap_config.get(self.keymap["mac_address"])

            ap_config["apList"].append(temp_dict)

            if ap_config.get(self.keymap["location"]) is not None:
                ap_config["configureLocation"] = True
            else:
                ap_config["isAssignedSiteAsLocation"] = True

            if ap_config.get(self.keymap["led_brightness_level"]) is not None:
                ap_config["configureLedBrightnessLevel"] = True

            if ap_config.get(self.keymap["led_status"]) is not None:
                ap_config["configureLedStatus"] = True
                ap_config[self.keymap["led_status"]] = True \
                    if ap_config[self.keymap["led_status"]] == "Enabled" else False

            if ap_config.get(self.keymap["ap_mode"]) is not None:
                if ap_config.get(self.keymap["ap_mode"]) == "Local":
                    ap_config[self.keymap["ap_mode"]] = 0
                elif ap_config.get(self.keymap["ap_mode"]) == "Monitor":
                    ap_config[self.keymap["ap_mode"]] = 1
                elif ap_config.get(self.keymap["ap_mode"]) == "Sniffer":
                    ap_config[self.keymap["ap_mode"]] = 4
                else:
                    ap_config[self.keymap["ap_mode"]] = 5
                ap_config["configureApMode"] = True

            if ap_config.get(self.keymap["primary_controller_name"]) is not None or \
                ap_config.get(self.keymap["secondary_controller_name"]) is not None or \
                ap_config.get(self.keymap["tertiary_controller_name"]) is not None or \
                ap_config.get(self.keymap["primary_ip_address"]) is not None or \
                ap_config.get(self.keymap["secondary_ip_address"]) is not None or \
                ap_config.get(self.keymap["tertiary_ip_address"]) is not None :
                ap_config["configureHAController"] = True

            if ap_config.get(self.keymap["failover_priority"]) is not None:
                if ap_config.get(self.keymap["failover_priority"]) == "Low":
                    ap_config[self.keymap["failover_priority"]] = 1
                elif ap_config.get(self.keymap["failover_priority"]) == "Medium":
                    ap_config[self.keymap["failover_priority"]] = 2
                elif ap_config.get(self.keymap["failover_priority"]) == "High":
                    ap_config[self.keymap["failover_priority"]] = 3
                else:
                    ap_config[self.keymap["failover_priority"]] = 4
                ap_config["configureFailoverPriority"] = True

            if ap_config.get("radioConfigurations") is not None:
                radio_config_list = ap_config.get("radioConfigurations")
                temp_radio_dtos_list = []
                for each_radio in radio_config_list:
                    radio_dtos = {}

                    radio_dtos["configureAdminStatus"] = True
                    radio_dtos["adminStatus"] = True if each_radio["adminStatus"] == "Enabled" \
                        else False

                    if each_radio.get(self.keymap["antenna_gain"]) is not None and \
                        each_radio.get(self.keymap["antenna_gain"]) > 0:
                        radio_dtos[self.keymap["antenna_gain"]] = \
                            each_radio.get(self.keymap["antenna_gain"])
                        radio_dtos["antennaPatternName"] = "other"
                        radio_dtos["configureAntennaPatternName"] = True

                    radio_dtos[self.keymap["channel_assignment_mode"]] = 1 \
                        if each_radio[self.keymap["channel_assignment_mode"]] == "Global" else 2

                    if each_radio.get(self.keymap["channel_number"]) is not None:
                        radio_dtos[self.keymap["channel_number"]] = \
                            each_radio.get(self.keymap["channel_number"])
                        radio_dtos["configureChannel"] = True
                        radio_dtos[self.keymap["channel_assignment_mode"]] = 2

                    if each_radio.get(self.keymap["channel_width"]) is not None:
                        if each_radio.get(self.keymap["channel_width"]) == "20 MHz":
                            radio_dtos[self.keymap["channel_width"]] = 3
                        elif each_radio.get(self.keymap["channel_width"]) == "40 MHz":
                            radio_dtos[self.keymap["channel_width"]] = 4
                        elif each_radio.get(self.keymap["channel_width"]) == "80 MHz":
                            radio_dtos[self.keymap["channel_width"]] = 5
                        else:
                            radio_dtos[self.keymap["channel_width"]] = 6
                        radio_dtos["configureChannelWidth"] = True

                    if each_radio.get(self.keymap["power_assignment_mode"]) is not None:
                        if each_radio[self.keymap["power_assignment_mode"]] == "Global":
                            radio_dtos[self.keymap["power_assignment_mode"]] = 1
                        else:
                            radio_dtos[self.keymap["power_assignment_mode"]] = 2
                        radio_dtos["configurePower"] = True

                    if each_radio.get(self.keymap["powerlevel"]) is not None:
                        radio_dtos[self.keymap["powerlevel"]] = \
                            each_radio.get(self.keymap["powerlevel"])

                    if each_radio.get(self.keymap["radio_type"]) is not None:
                        if each_radio.get(self.keymap["radio_type"]) == "2.4 GHz":
                            radio_dtos["radioType"] = 1
                            if each_radio[self.keymap["clean_air_si"]] == "Enabled":
                                ap_config["cleanAirSI24"] = True
                                ap_config["configureCleanAirSI24Ghz"] = True
                            else:
                                radio_dtos["cleanAirSI24"] = False
                                ap_config["configureCleanAirSI24Ghz"] = False
                        elif each_radio.get(self.keymap["radio_type"]) == "5 GHz":
                            radio_dtos["radioType"] = 2
                            if each_radio[self.keymap["clean_air_si"]] == "Enabled":
                                ap_config["cleanAirSI5"] = True
                                ap_config["configureCleanAirSI5Ghz"] = True
                            else:
                                radio_dtos["cleanAirSI5"] = False
                                ap_config["configureCleanAirSI5Ghz"] = False
                        elif each_radio.get(self.keymap["radio_type"]) == "XOR":
                            radio_dtos["radioType"] = 3
                        else:
                            radio_dtos["radioType"] = 6
                            if each_radio[self.keymap["clean_air_si"]] == "Enabled":
                                ap_config["cleanAirSI6"] = True
                                ap_config["configureCleanAirSI6Ghz"] = True
                            else:
                                radio_dtos["cleanAirSI6"] = False
                                ap_config["configureCleanAirSI6Ghz"] = False

                    if each_radio.get(self.keymap["cable_loss"]) is not None:
                        radio_dtos["cableLoss"] = each_radio.get(self.keymap["cable_loss"])
                        radio_dtos["antennaCableName"] = "other"

                    if each_radio.get(self.keymap["antenna_cable_name"]) is not None:
                        radio_dtos["antennaCableName"] = \
                            each_radio.get(self.keymap["antenna_cable_name"])
                        radio_dtos["configureAntennaCable"] = True

                    if each_radio.get(self.keymap["antenna_pattern_name"]) is not None:
                        radio_dtos[self.keymap["antenna_pattern_name"]] = \
                            each_radio.get(self.keymap["antenna_pattern_name"])

                    radio_dtos[self.keymap["radio_band"]] = "RADIO24" \
                        if each_radio[self.keymap["radio_band"]] == "2.4 GHz" else "RADIO5"

                    if each_radio.get(self.keymap["radio_role_assignment"]) is not None:
                        if each_radio.get(self.keymap["radio_role_assignment"]) == "Auto":
                            radio_dtos[self.keymap["radio_role_assignment"]] = "AUTO"
                        elif each_radio.get(self.keymap["radio_role_assignment"]) == "Client-Serving":
                            radio_dtos[self.keymap["radio_role_assignment"]] = "SERVING"
                        else:
                            radio_dtos[self.keymap["radio_role_assignment"]] = "MONITOR"
                        radio_dtos["configureRadioRoleAssignment"] = True

                    temp_radio_dtos_list.append(radio_dtos)
                ap_config["radioConfigurations"] = temp_radio_dtos_list

            for key_to_remove in ("mac_address", "hostname", "management_ip_address"):
                if ap_config.get(key_to_remove): del ap_config[key_to_remove]
            self.log("CHECKIN update: {0}".format(self.pprint(ap_config)),
                         "INFO")
            response = self.dnac._exec(
                    family="wireless",
                    function='configure_access_points',
                    op_modifies=True,
                    params={"payload": ap_config}
                )

            if response:
                response = response.get("response")
                self.log("Response of Access Point Configuration: {0}".format(str(response)),
                         "INFO")
                return dict(mac_address=ap_config["macAddress"], response=response)

        except Exception as e:
            self.log("AP config update Error {0}".format(str(ap_config["macAddress"])+str(e)),
                     "ERROR")
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
            final_input_data = functions.data_frame(ap_selected_fields, device_records)
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

    def pprint(self, jsondata):
        return json.dumps(jsondata, indent=4, separators=(',',': '))

    def camel_to_snake_case(self, config):
        """
        Convert camel case keys to snake case keys in the config.

        Parameters:
            config (list) - Playbook details provided by the user.

        Returns:
            new_config (list) - Updated config after eliminating the camel cases.
        """

        if isinstance(config, dict):
            new_config = {}
            for key, value in config.items():
                new_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key).lower()
                #if new_key != key:
                #    self.log("{0} will be deprecated soon. Please use {1}.".format(key, new_key), "DEBUG")
                new_value = self.camel_to_snake_case(value)
                new_config[new_key] = new_value
        elif isinstance(config, list):
            return [self.camel_to_snake_case(item) for item in config]
        else:
            return config
        return new_config


class ProvisionAccesspoint(DnacBase):

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged"]

    def pprint(self, jsondata):
        return json.dumps(jsondata, indent=4, separators=(',', ': '))

    def validate_input(self):
        """
        Validates the input configuration from the playbook.
        Returns:
        The method returns an instance of the class with updated attributes:
            - self.msg: A message describing the validation result.
            - self.status: The status of the validation (either 'success' or 'failed').
            - self.validated_config: If successful, a validated version of the 'config' parameter.
        Description:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed',
            and 'self.msg' will describe the validation issues.
        """
        self.logger.debug('Validating input...')
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        temp_spec = dict(
            type=dict(required=False, type='str'),
            site=dict(required=True, type='dict'),
        )

        self.config = self.update_site_type_key(self.config)

        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params)
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook config params: {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def get_want(self, config):
        """
        Retrieves the desired state from the configuration.
        Args:
            config (dict): Configuration dictionary.
        Returns:
            self: Returns the instance itself.
        Description:
            Retrieves desired AP and site configuration parameters from the provided playbook.
        """
        want = dict(
            ap_params= self.get_ap_params(config),
            ap_name = self.get_ap_name(config),
            site_params= self.get_site_params(config),
            site_name= self.get_site_name(config),
        )
        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")

        return self

    def ap_exists(self):
        """
        Checks if the Access Point (AP) exists in Cisco Catalyst Center.
        Returns:
            bool: True if AP exists, False otherwise.
            dict: Current AP details if AP exists, including hostname, MAC address,
            and RF profile.
        Description:
            This method queries the Cisco DNA Center (DNAC) API to check if the AP
            identified by its MAC address exists. If found, it retrieves and logs
            details such as hostname, MAC address, and RF profile of the AP.
        """
        ap_exists = False
        current_ap = {}
        response = None

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                op_modifies=True,
                params={"macAddress": self.want.get("ap_params").get("device").get("macAddress")}
            )
        except Exception as e:
            self.log("Error fetching AP details: {0}".format(str(e)), "WARNING")
            self.log("The provided AP name '{0}' is either invalid or not present in the \
                     Cisco Catalyst Center.".format(self.want.get("ap_name")), "WARNING")
            return ap_exists, current_ap

        if response:
            response_data = response.get("response")
            self.log("Task response: {0}".format(self.pprint(response_data)), "INFO")

            if response_data:
                site = response_data[0]
                ap_info = {
                    "devices": {
                        "host_name": site.get("hostname"),
                        "mac_address": site.get("macAddress"),
                        "rf_profile": site.get("rfProfile")
                    }
                }

                current_ap = {
                    "type": "devices",
                    "ap": ap_info,
                    "device": site.get("id")
                }

                ap_exists = True
                self.log("AP '{0}' exists in Cisco Catalyst Center".format(
                    self.want.get("ap_name")), "INFO")
                self.log("Current AP details: {0}".format(self.pprint(current_ap)), "INFO")

        return ap_exists, current_ap

    def get_ap_params(self, config):
        """
        Retrieves AP parameters from the configuration.
        Args:
            config (dict): Configuration dictionary.
        Returns:
            dict: AP parameters.
        """
        if config is None or config.get("site") is None or config.get("site", {}).get("devices") is None:
            self.log("Config, site, or devices is None. Cannot proceed with get_ap_params.", "ERROR")
            return {}

        ap_details = config.get("site", {}).get("devices", {})
        ap_info = {
            'device': {
                'host_name': ap_details.get('host_name'),
                'macAddress': ap_details.get('mac_address'),
                'family': ap_details.get('family'),
                'managementIPAddress': ap_details.get('management_ip_address'),
                'serialNumber': ap_details.get('serial_number'),
                'imageVersion': ap_details.get('image_version'),
                'rf_profile': ap_details.get('rf_profile')
            }
        }

        self.log("AP parameters: {0}".format(self.pprint(ap_info)), "DEBUG")
        return ap_info

    def get_ap_name(self, config):
        """
        Retrieves the AP name from the configuration.
        Args:
            config (dict): Configuration dictionary.
        Returns:
            str: AP name.
        """
        if config is None or config.get("site") is None or \
            config.get("site", {}).get("devices") is None:
            self.log("Config, site, or devices is None. Cannot proceed with get_ap_name.", "ERROR")
            return None

        self.log("Getting AP name with config: {0}".format(self.pprint(config)), "DEBUG")

        host_name = config.get("site", {}).get("devices", {}).get("host_name")
        mac_address = config.get("site", {}).get("devices", {}).get("mac_address")

        self.log("Host name: {0}, MAC address: {1}".format(host_name, mac_address), "DEBUG")

        if not host_name or not mac_address:
            self.log("Host name or MAC address is missing or None. Host name: {0},\
                      MAC address: {1}".format(host_name, mac_address), "WARNING")
            return None

        ap_name = host_name
        self.log("AP name: {0}".format(ap_name), "INFO")
        return ap_name

    def get_site_params(self, params):
        """
        Retrieves site parameters from the configuration.
        Args:
            params (dict): Configuration parameters.
        Returns:
            dict: Site parameters.
        """
        typeinfo = params.get("type")
        site_info = {}

        if typeinfo == 'area':
            floor_details = params.get('site').get('area')
            site_info['area'] = {
                'name': floor_details.get('name'),
                'parentName': floor_details.get('parent_name')
            }

            try:
                site_info["area"]["rfModel"] = floor_details.get("rf_model")
            except Exception as e:
                self.log("The attribute 'rf_model' is missing in floor '{0}'.".format(
                    floor_details.get('name') + str(e)), "WARNING")

        site_params = dict(
            type=typeinfo,
            site=site_info,
        )
        self.log("Site parameters: {0}".format(str(site_params)), "DEBUG")

        return site_params

    def get_site_name(self, site):
        """
        Retrieves and extracts current site details from the site information.
        Args:
            site (dict): Site details.
        Returns:
            dict: Current site details.
        """
        site_type = site.get("type")
        parent_name = site.get("site").get(site_type).get("parent_name")
        name = site.get("site").get(site_type).get("name")
        site_name = '/'.join([parent_name, name])
        self.log("Site name: {0}".format(site_name), "INFO")
        return site_name

    def site_exists(self):
        """
        Checks if the site exists in Cisco Catalyst Center and retrieves current site details
         if it exists.
        Returns:
            bool: True if site exists, False otherwise.
            dict: Current site details if site exists, None otherwise.
        """
        site_exists = False
        current_site = {}
        response = None

        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                op_modifies=True,
                params={"name": self.want.get("site_name")},
            )
        except Exception as e:
            self.log("The provided site name '{0}' is either invalid or not present in the \
                     Cisco Catalyst Center.".format(self.want.get("site_name")), "WARNING")
            return site_exists, None

        if response:
            response_data = response.get("response")
            self.log("Task response: {0}".format(self.pprint(response_data)), "INFO")
            
            try:
                location = get_dict_result(response_data[0].get("additionalInfo"), 'nameSpace', "Location")
                type_info = location.get("attributes", {}).get("type")

                if type_info == "floor":
                    site_info = {
                        "floor": {
                            "name": response_data[0].get("name"),
                            "parentName": response_data[0].get("siteNameHierarchy").split(
                                "/" + response_data[0].get("name"))[0]
                        }
                    }

                current_site = {
                    "type": type_info,
                    "site": site_info,
                    "siteId": response_data[0].get("id")
                }

                self.log('Current site details: {0}'.format(str(current_site)), "INFO")
                site_exists = True
                self.log("Site '{0}' exists in Cisco Catalyst Center".format(self.want.get("site_name")), "INFO")

            except Exception as e:
                self.log('Error retrieving current site details: {0}. Details: {1}'.format(str(e), self.pprint(response_data)), "ERROR")
                return site_exists, None

        return site_exists, current_site

    def get_have(self, config):
        """
        Retrieves and checks existing state information (have) for site and AP.
        Args:
            config (dict): Configuration dictionary.
        Returns:
            self: Returns the instance itself.
        """
        have = {}

        (site_exists, current_site) = self.site_exists()
        self.log("Site exists: {}, Current site: {}".format(site_exists,
                                                            self.pprint(current_site)), "DEBUG")

        if site_exists and current_site:
            have["site_name_hierarchy"] = current_site.get("site")
            have["site_exists"] = site_exists
            have["current_site"] = current_site

        (ap_exists, current_ap) = self.ap_exists()
        self.log("AP exists: {}, Current AP: {}".format(ap_exists,
                                                        self.pprint(current_ap)), "DEBUG")

        if ap_exists and current_ap:
            have["device_id"] = current_ap.get("device")
            have["ap_exists"] = ap_exists
            have["current_ap"] = current_ap

        self.have = have
        self.log("Current State (have): {}".format(self.pprint(self.have)), "INFO")

        return self

    def valid_ap_config_parameters(self, config):
        """
        Validate AP configuration parameters.
        Args:
        - config (dict): Dictionary containing AP configuration parameters.
        Returns:
        - ClassName instance: Returns self instance with updated status and logs.
        """
        errormsg = []

        if config.get("host_name"):
            if not isinstance(config["host_name"], str) or len(config["host_name"]) > 32:
                errormsg.append("host_name: Invalid type or length > 32 characters in playbook.")

        if config.get("family"):
            if not isinstance(config["family"], str) or len(config["family"]) > 64:
                errormsg.append("family: Invalid type or length > 64 characters in playbook.")

        if config.get("mac_address"):
            mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
            if not mac_regex.match(config["mac_address"]):
                errormsg.append("mac_address: Invalid MAC Address '{0}' in playbook.".format(config["mac_address"]))

        if config.get("management_ip_address"):
            if not self.is_valid_ipv4(config["management_ip_address"]):
                errormsg.append("management_ip_address: Invalid Management IP Address '{0}' in playbook"\
                                .format(config["management_ip_address"]))

        if config.get("serial_number"):
            if not isinstance(config["serial_number"], str) or len(config["serial_number"]) > 32:
                errormsg.append("serial_number: Invalid type or length > 32 characters in playbook.")

        if config.get("image_version"):
            if not isinstance(config["image_version"], str) or len(config["image_version"]) > 32:
                errormsg.append("image_version: Invalid type or length > 32 characters in playbook.")

        if config.get("name"):
            if not isinstance(config["name"], str) or len(config["name"]) > 32:
                errormsg.append("name: Invalid type or length > 32 characters in playbook.")

        if config.get("parent_name"):
            if not isinstance(config["parent_name"], str) or len(config["parent_name"]) > 64:
                errormsg.append("parent_name: Invalid type or length > 64 characters in playbook.")

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: '{0}'".format("\n".join(errormsg))
            self.log('Task response {0}'.format(str(self.msg)), "ERROR")
            self.status = "failed"
            return self

        self.msg = "Successfully validated config params: {0}".format(str(config))
        self.log('Task response {0}'.format(str(self.msg)), "INFO")
        self.status = "success"
        return self

    def get_diff_merged(self, config):
        """
        Get differences between current state (have) and desired state (want).
        Returns:
        - ClassName instance: Returns self instance with updated diff and logs.
        """
        diff = {}

        if self.have.get("site_exists") and self.want.get("site_params"):
            diff["site_id"] = self.have["site_id"]

        if self.have.get("ap_exists") and self.want.get("ap_params"):
            diff["mac_address"] = self.have["mac_address"]

        self.diff = diff
        self.log('Difference (get_diff_merged):\n{0}'.format(self.pprint(self.diff)), "INFO")

        return self

    def verify_diff_merged(self):
        """
        Verify differences between current state (have) and desired state (want).
        Returns:
        - ClassName instance: Returns self instance with updated diff and logs.
        """
        diff = {}

        if self.have.get("site_exists"):
            diff["site_id"] = self.have["site_id"]

        if self.have.get("ap_exists"):
            diff["mac_address"] = self.have["mac_address"]

        self.diff = diff
        self.log('Difference (verify_diff_merged):\n{0}'.format(self.pprint(self.diff)), "INFO")

        return self

    def assign_device_to_site(self):
        """
        Assigns a device (AP) to a specific site.
        Returns:
            self: Returns the instance itself.
        """
        site_name = self.want.get("site_name")
        device_ip = self.want.get("ap_params").get("device").get("managementIPAddress")
        site_id= self.have.get("current_site").get("id")

        if not site_name or not device_ip:
            error_msg="Cannot assign device to site: site_name ({0}), device_ip ({1}) is missing."\
                .format(site_name, device_ip)
            self.log(error_msg, "ERROR")
            self.status = "failed"
            return self

        try:
            self.log("Fetching site details for site_name: '{0}'".format(site_name), "DEBUG")
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                params={"name": site_name}
            )

            self.log("Response from get_site: {0}".format(str(response)), "DEBUG")
            site_id = response.get("response")[0].get("id") if response.get("response") else None

            if not site_id:
                self.log("Site with name '{0}' not found.".format(site_name), "ERROR")
                self.status = "failed"
                return self

            payload_param = {"site_id": site_id, "device": [{"ip": device_ip}]}
            response = self.dnac._exec(
                family="sites",
                function='assign_devices_to_site',
                op_modifies=True,
                params=payload_param
            )

            self.status = "success"
            self.log("Assigned device with IP '{0}' to site '{1}' successfully.".format(
                device_ip, site_name), "INFO")

            self.result['site_id'] = site_id
            self.result['execution_id'] = response.get("executionId")

        except Exception as e:
            self.log("Error assigning device to site: {0}".format(str(e)), "ERROR")
            self.status = "failed"

        return self

    def provision_device(self):
        """
        Provisions a device (AP) to a specific site.
        Returns:
            dict: Returns a dictionary with status and result message.
        """
        try:
            site_name_hierarchy = self.want.get("site_name")
            rf_profile = self.want.get("ap_params").get("device").get("rf_profile")
            host_name = self.want.get("ap_name")
            type_name = self.want.get("ap_params").get("device").get("family")

            if not site_name_hierarchy or not rf_profile or not host_name or not type_name:
                error_msg = ("Cannot provision device: Missing parameters - \
                            site_name_hierarchy: {0}, rf_profile: {1}, host_name: {2},\
                            type_name: {3}").format(site_name_hierarchy, rf_profile, host_name,
                                                   type_name)
                self.log(error_msg, "ERROR")
                self.status = "failed"
                self.result['msg'] = error_msg
                return self

            self.log("Fetching site details for site_name: '{0}'".format(
                site_name_hierarchy), "DEBUG")

            provision_params = [{
                "rfProfile": rf_profile,
                "deviceName": host_name,
                "type": type_name,
                "siteNameHierarchy": site_name_hierarchy
            }]
            self.log('Current site details: {0}'.format(self.pprint(provision_params)), "INFO")

            response = self.dnac._exec(
                family="wireless",
                function='ap_provision',
                op_modifies=True,
                params={"payload": provision_params},
            )

            self.log('Response from ap_provision: {0}'.format(str(response)), "INFO")
            if response and isinstance(response, dict):
                executionid = response.get("executionId")
                while True:
                    execution_details = self.get_execution_details(executionid)
                    if execution_details.get("status") == "SUCCESS":
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        break

                    elif execution_details.get("bapiError"):
                        self.module.fail_json(msg=execution_details.get("bapiError"),
                                              response=execution_details)
                        break

            self.msg = "Site - {0} Updated Successfully".format(site_name_hierarchy)
            self.log(self.msg, "INFO")
            self.log("Provisioned device with host '{0}' to site '{1}' successfully.".format(
                host_name, site_name_hierarchy), "INFO")
            self.status = "success"
            self.result['msg'] = self.msg
            self.result['response'].append({"siteId": self.have.get("site_id")})

        except Exception as e:
            error_msg = 'An error occurred during device provisioning: {0}'.format(str(e))
            self.log(error_msg, "ERROR")
            self.status = "failed"
            self.result['msg'] = error_msg

        return self


floor_plan = {
    '101101': 'Cubes And Walled Offices',
    '101102': 'Drywall Office Only',
    '101105': 'Free Space',
    '101104': 'Indoor High Ceiling',
    '101103': 'Outdoor Open Space'
}

class Accesspointmovement(Accesspoint):
    """Class containing member attributes for DNAC Access Point Automation module"""
    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = []
        self.supported_states = ["merged"]
        self.payload = module.params

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
                - self.validated_config: If successful, a validated version of the 'config' 
                  parameter.
        Description:
            Example:
                To use this method, create an instance of the class and call 'validate_input_yml' 
                on it. If the validation succeeds, 'self.status' will be 'success' and  
                'self.validated_config' will contain the validated configuration. If it fails, 
                'self.status' will be 'failed' and 'self.msg' will describe the validation issues.
                To use this method, create an instance of the class and call 'validate_input_yml' 
                on it. If the validation succeeds, this will allow to go next step, 
                unless this will stop execution based on the fields.
        """
        self.log('Validating the Playbook Yaml File..', "INFO")

        if not self.config:
            self.status = "failure"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self
        else:
            aplist = self.payload.get("config")
            aplist = self.camel_to_snake_case(aplist)
            aplist = self.update_site_type_key(aplist)
            accesspoint_spec = dict(mac_address=dict(required=False, type='str'),
                                    ap_type = dict(required= True, type= 'str'),
                                    rf_profile = dict(required= True, type= 'str'),
                                    type = dict(required=False, type='str'),
                                    site = dict(required=True, type='dict'),
                                    dest_site = dict(required=True, type='dict'),
                                    ap_name = dict(required=False, type='str'),
                                    management_ip_address = dict(required=False, type='str'),
                                    hostname = dict(required=False, type='str'),
                                )
            valid_param , invalid_params = validate_list_of_dicts(aplist, accesspoint_spec)

            if invalid_params:
                self.msg = "Invalid parameters in playbook: {0}".format(
                    "\n".join(invalid_params)
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self
            else:
                self.validated_config = valid_param
                self.msg = "Successfully validated playbook config params: {0}".format(
                    str(valid_param))
                self.log(self.msg, "INFO")
                self.status = "success"
                return self

    def get_site_name(self, config):
        """
        Get and Return the site name.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - site (dict): A dictionary containing information about the site.
        Returns:
          - str: The constructed site name.
        Description:
            This method takes a dictionary 'site' containing information about
          the site and constructs the site name by combining the parent name
          and site name.
        """
        site_type = config["type"]
        parent_name = config["site"][site_type]["parent_name"]
        name = config["site"][site_type]["name"]
        site_name = '/'.join([parent_name, name])
        self.log("Site name: {0}".format(site_name), "INFO")
        return site_name

    def get_dest_site_name(self, config):
        """
        Get and Return the destination destination site name.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - site (dict): A dictionary containing information about the destination site.
        Returns:
          - str: The constructed destination site name.
        Description:
            This method takes a dictionary 'site' containing information about
          the site and constructs the destination site name by combining the parent name
          and site name.
        """
        site_type = config["type"]
        dest_parent_name = config["dest_site"][site_type]["parent_name"]
        name = config["dest_site"][site_type]["name"]
        dest_site_name = '/'.join([dest_parent_name, name])
        self.log("Destination Site name: {0}".format(dest_site_name), "INFO")
        return dest_site_name

    def get_want(self, config):
        """
        Retrieves all necessary information from the playbook configuration for configuring 
        Access Points in Cisco Catalyst Center.
        
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing configuration details from the playbook.
            
        Returns:
            - dict: A dictionary containing the extracted access point and site information.
        Description:
            This method retrieves essential access point details such as 'site_name',
            'dest_site_name', 'mac_address', 'ap_type', and 'rf_profile' from the playbook config.
            The extracted information is stored in the 'want' attribute  of the instance for 
            subsequent use in the access point movement workflow.
        """
        want = {}
        want["site_name"] = self.get_site_name(config)
        want["dest_site_name"] = self.get_dest_site_name(config) 

        for key,value in config.items():
            if key not in ("site", "dest_site"):
                want[key] = value

        self.want = want  
        self.log("Current State (want): {0}".format(str(self.want)), "INFO")
        return self

    def get_have(self, input_config):
        """
        Get the site details from Cisco Catalyst Center
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - config (dict): A dictionary containing the configuration details.
        Returns:
          - self (object): An instance of a class used for interacting with  Cisco Catalyst Center.
        Description:
            This method queries Cisco Catalyst Center to check if a specified access point and site
            exists. If the access point and site exists, it retrieves details about the current
            site, including the ap_name, mac_address, site ID and other relevant information. The
            results are stored in the 'have' attribute for later reference.
        """
        self.log(input_config)
        ap_exists = False
        current_ap_config = None
        site_exists = False
        current_site = None
        dest_site_exists = False
        current_dest_site = None

        (ap_exists, current_ap_config) = Accesspoint.get_current_config(self, input_config)
        self.log("Current AP config details (have): {0}".format(str(current_ap_config)), "DEBUG")
        (site_exists, current_site) = self.site_exists("site_name")
        self.log("Current Site details (have): {0}".format(str(current_site)), "DEBUG")
        (dest_site_exists, current_dest_site) = self.site_exists("dest_site_name")
        self.log("Current Destination Site details (have): {0}".format(str(current_dest_site)),
                  "DEBUG")

        have = {}

        if ap_exists:
            have["mac_address"] = current_ap_config.get("mac_address")
            have["ap_name"] = current_ap_config.get("ap_name")
            have["ap_exists"] = ap_exists
        if site_exists:
            have["current_site_id"] = current_site.get("siteId")
            have["site_exists"] = site_exists
            have["current_site"] = current_site 
        if dest_site_exists:
            have["dest_site_id"] = current_dest_site.get("siteId")
            have["dest_site_exists"] = dest_site_exists
            have["current_dest_site"] = current_dest_site
        if site_exists:
            site_id = current_site.get("siteId")
            ap_mac_address = have.get("mac_address")
            if self.get_site_device(site_id, ap_mac_address):
                have["device_belongs_to_site"] = True
            else:
                have["device_belongs_to_site"] = False
        if dest_site_exists:
            site_id = current_dest_site.get("siteId")
            ap_mac_address = have.get("mac_address")
            if self.get_site_device(site_id, ap_mac_address):
                have["device_belongs_to_dest_site"] = True
            else:
                have["device_belongs_to_dest_site"] = False

        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        return self

    def site_exists(self,site_type):
        """
        Check if the site exists in Cisco Catalyst Center.

        Parameters:
          - self (object): An instance of the class containing the method.
        Returns:
          - tuple: A tuple containing a boolean indicating whether the site exists and
                   a dictionary containing information about the existing site.
                   The returned tuple includes two elements:
                   - site_exists (bool): Indicates whether the site exists.
                   - dict: Contains information about the existing site. If the
                           site doesn't exist, this dictionary is empty.
        Description:
            Checks the existence of a site in Cisco Catalyst Center by querying the
          'get_site' function in the 'sites' family. It utilizes the
          'site_name' parameter from the 'want' attribute to identify the site.
        """
        site_exists = False
        current_site = {}
        response = None
        self.log(site_type)
        self.log(self.want.get(site_type))

        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                op_modifies=True,
                params={"name": self.want.get(site_type)},
            )
            self.log(response)

        except Exception as e:
            self.log("The provided site name '{0}' is either invalid or not present \
                     in the Cisco Catalyst Center."
                     .format(self.want.get(site_type)), "WARNING")

        if response:
            response = response.get("response")
            self.log("Received API response from 'get_site': {0}".format(str(response)),\
                      "DEBUG")
            current_site = self.get_current_site(response)
            site_exists = True
            self.log("Site '{0}' exists in Cisco Catalyst Center".format(self.want.get(
                site_type)), "INFO")

        return (site_exists, current_site)

    def get_current_site(self, site):
        """
        Get the current site information.
        Parameters:
          self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          - site (list): A list containing information about the site.
        Returns:
          - dict: A dictionary containing the extracted site information.
        Description:
            This method extracts information about the current site based on
          the provided 'site' list. It determines the type of the site
          (area, building, or floor) and retrieves specific details
          accordingly. The resulting dictionary includes the type, site
          details, and the site ID.
        """
        site_info = {}
        location = get_dict_result(site[0].get("additionalInfo"), 'nameSpace', "Location")
        typeinfo = location.get("attributes").get("type")

        if typeinfo == "area":
            site_info = dict(
                area=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split("/" + site[0].get("name"))[0]
                )
            )
        elif typeinfo == "building":
            site_info = dict(
                building=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split("/" + site[0].get("name"))[0],
                    address=location.get("attributes").get("address"),
                    latitude=location.get("attributes").get("latitude"),
                    longitude=location.get("attributes").get("longitude"),
                    country=location.get("attributes").get("country"),
                )
            )
        elif typeinfo == "floor":
            map_geometry = get_dict_result(site[0].get("additionalInfo"), 'nameSpace', "mapGeometry")
            map_summary = get_dict_result(site[0].get("additionalInfo"), 'nameSpace', "mapsSummary")
            rf_model = map_summary.get("attributes").get("rfModel")
            site_info = dict(
                floor=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split("/" + site[0].get("name"))[0],
                    rf_model=floor_plan.get(rf_model),
                    width=map_geometry.get("attributes").get("width"),
                    length=map_geometry.get("attributes").get("length"),
                    height=map_geometry.get("attributes").get("height"),
                    floorNumber=map_geometry.get("attributes").get("floor_number", "")
                )
            )

        current_site = dict(
            type=typeinfo,
            site=site_info,
            siteId=site[0].get("id")
        )

        self.log("Current site details: {0}".format(str(current_site)), "INFO")
        return current_site

    def get_site_device(self, site_id, ap_mac_address):
        """
        Fetches device information associated with a specific site and checks if a given AP 
        MAC address is present.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_id (str): The identifier for the site whose devices are to be fetched.
            ap_mac_address (str): The MAC address of the Access Point (AP) device to check.

        Returns:
            tuple: A tuple containing a boolean indicating success or failure of the operation,
                and an optional dictionary or list of retrieved device information.

        Description:
            This method utilizes the 'get_membership' API to retrieve details about devices
            associated with the specified 'site_id'. It verifies if the AP device identified by
            'ap_mac_address' is among the devices retrieved for the site. If found, it logs a
            success message indicating presence; otherwise, it logs a failure message.

            If successful, the method returns a tuple (True, ...), indicating the device was found
            in the site. If unsuccessful or if the device is not found, it returns (False, ...).

            Example log messages:
            - "Device with MAC address: <ap_mac_address> found in site: <site_id>, Proceeding with 
               ap_site updation."
            - "Device with MAC address: <ap_mac_address> not found in site: <site_id>"

            Logging levels used:
            - DEBUG for logging API response details.
            - INFO for logging device presence or absence.
            - ERROR for logging any exceptions encountered during API interaction.

        """
        try:
            response = self.dnac._exec(family="sites",
                                       function="get_membership",
                                       op_modifies=True,
                                       params={"site_id": site_id}
                                      )
            self.log(response)

        except Exception as e:
            self.log("Failed to fetch child sites for site_id '{}'.\
                      Error: {}".format(site_id, str(e)), "ERROR")
            return False

        site_response = response.get("site", {}).get("response", [])
        self.log("Site '{}' response along with its child sites: \
                 {}".format(site_id, str(site_response)), "DEBUG")

        device_mac_info = []
        for device_info in response.get('device', []): 
            response_list = device_info.get('response', [])
            for response_item in response_list:
                mac_address = response_item.get('macAddress')
                if mac_address:
                    device_mac_info.append(mac_address)

        if ap_mac_address in device_mac_info:
            self.log("Device with MAC address: {macAddress} found in site: {sId},\
                      Proceeding with ap_site updation.".format(macAddress= ap_mac_address,
                                                                sId = site_id) ,  "INFO")
        else:
            self.log("Device with MAC address: {macAddress} not found in site: \
                     {sId}".format(macAddress= ap_mac_address,sId = site_id) ,  "INFO")
            return False

        return True

    def get_diff_merged(self, config):
        """
        Update site information for access point in Cisco Catalyst Center with fields
        provided in the playbook.
        Parameters:
          self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method determines whether to update or not the access point site information in
            Cisco Catalyst Center based on the provided configuration information. If the specified
            site exists and access point, the method checks if it requires an update by comparing
            the current site id and destination site id. If an update is required, it calls the 
            'ap_provision' function from the 'wireless' family of the Cisco Catalyst Center API.
            If the access point movement is not required(UPDATE), the method exits, indicating that
            access point movemented is not required and it is up to date.
     
        Check if access point movement is required and perform the movement if needed.
        """
        if self.have.get("dest_site_exists") and self.have.get("ap_exists"):
            current_site_id = self.have.get("site_id")
            self.log(current_site_id)
            dest_site_id = self.have.get("dest_site_id")
            self.log(dest_site_id)
            if dest_site_id == current_site_id :
                self.msg = "Access point is already at destination site or there is no\
                    site allocated. No movement required."
                self.log(self.msg, "INFO")
                self.result['msg'] = self.msg
                return self
            else:
                rf_profile = self.want.get("rf_profile")
                ap_name = self.have.get("ap_name")
                ap_type = self.want.get("ap_type")
                dest_site_name = self.want.get("dest_site_name")

                try:
                    ap_params = [{
                            "rfProfile": rf_profile,
                            "deviceName": ap_name,
                            "type": ap_type, 
                            "siteNameHierarchy": dest_site_name,
                        }]

                    response = self.dnac._exec(
                        family="wireless",
                        function="ap_provision",
                        op_modifies=True,
                        params= {"payload":ap_params},
                    )
                    self.log("Received API response from 'update_SIte_Id': {0}".format(
                        str(response)), "DEBUG")
                    executionid = response.get("executionId")

                    while True:
                        execution_details = self.get_execution_details(executionid)
                        if execution_details.get("status") == "IN_PROGRESS":
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            self.msg = "Access point moved successfully  to site {}".format( dest_site_id)
                            self.log(self.msg, "INFO")
                            self.result['msg'] = self.msg
                            self.result['response'].append({"siteId": dest_site_id})
                            break
                        else:
                            self.module.fail_json(msg=execution_details.get("bapiError"),
                                                  response=execution_details)
                            break

                except Exception as e:
                    self.log("Failed to move access point. Error: {0}".format((e)), "ERROR")
        else:
            self.log("Site or access point does not exist. Cannot perform access point\
                      movement check.", "ERROR")

        return self

    def validate_input(self, config):
        """
        Validate the fields provided in the configuration dictionary against predefined 
        specifications.

        Checks various parameters within the provided configuration (`config`) to ensure they
        adhere to expected structures and data types based on input requirements.

        Parameters:
        - self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
        The method returns an instance of the class with updated attributes:
            - self.msg: A message describing the validation result.
            - self.status: The status of the validation (either 'success' or 'failed').
            - self.validated_config: If successful, a validated version of the 'config' parameter.

        Description:
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success', indicating that the 
            configuration adheres to the specified requirements. The validated configuration
            will be accessible  through 'self.validated_config'. If validation fails,
            'self.status' will be 'failed', and 'self.msg' will describe the encountered
            validation issues.

        This method validates the following fields in the 'config' dictionary:
            - 'mac_address': Validates format and length constraints of MAC addresses.
            - 'site.name': Ensures it is a string and does not exceed 32 characters.
            - 'site.parent_name': Ensures it is a string and does not exceed 64 characters.
            - 'rf_Profile': Validates it as a string with a maximum length of 128 characters.
            - 'ap_type': Ensures it equals "Unified AP".
            - 'site.type': Ensures it equals "floor".

        Debug messages are logged to aid in understanding the validation process.
        """     
        errormsg = []
        self.log(f"Debug: Initial config: {config}", "DEBUG")

        if config.get("mac_address"):
            mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
            if not mac_regex.match(config["mac_address"]) or len(config["mac_address"]) != 17:
                errormsg.append("mac_address: Invalid MAC Address format \
                                '{0}' in playbook.".format(config["mac_address"]))

        if config.get("site") and config["site"].get("name"):
            if not isinstance(config["site"]["name"], str) or len(config["site"]["name"]) > 32:
                errormsg.append("name: Invalid type or length > 32 characters in playbook.")

        if config.get("site") and config["site"].get("parent_name"):
            if not isinstance(config["site"]["parent_name"], str) \
                or len(config["site"]["parent_name"]) > 64:
                errormsg.append("parent_name: Invalid type or length > 64 characters in playbook.")

        if config.get("dest_site") and config["dest_site"].get("name"):
            if not isinstance(config["dest_site"]["name"], str) or \
                len(config["dest_site"]["name"]) > 32:
                errormsg.append("name: Invalid type or length > 32 characters in playbook.")

        if config.get("dest_site") and config["dest_site"].get("dest_parent_name"):
            if not isinstance(config["site"]["parent_name"], str) \
                or len(config["site"]["parent_name"]) > 64:
                errormsg.append("parent_name: Invalid type or length > 64 characters in playbook.")

        if config.get("rf_Profile"):
            if not isinstance(config["rf_Profile"], str) or len(config["rf_Profile"]) > 10:
                errormsg.append("rf_Profile: Invalid type or length > 128 characters in playbook.")

        if config.get("ap_type"):
            if config["ap_type"] != "Unified AP":
                errormsg.append("ap_type: Invalid value '{0}' in playbook. \
                                Expected 'Unified AP'.".format(config["ap_type"]))

        if config.get("site") and config["site"].get("type"):
            if config["site"]["type"] != "floor":
                errormsg.append("type: Invalid value '{0}' in playbook. \
                                Expected 'floor'.".format(config["site"]["type"]))

        self.log(f"Debug: Error messages: {errormsg}", "DEBUG")

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config:"
            for error in errormsg:
                self.msg += f"\n- {error}"
            self.log(self.msg, "ERROR")
            self.status = "failed"
        else:
            self.msg = "Successfully validated config params: {0}".format(str(config))
            self.log(self.msg, "INFO")
            self.status = "success"

        return self

    def verify_diff_merged(self, config):
        """
        Verify the merged status(Updation) of site name for access point in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center
            by retrieving the current state (have) and desired state (want) of the configuration,
            logs the states, and validates whether the specified destination site exists in the
            Catalyst Center configuration.
        """
        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        # Code to validate ccc config for merged state
        dest_site_exist = self.have.get("dest_site_exists")
        dest_site_id = self.have.get("dest_site_id")
        dest_site_name = self.want.get("dest_site_name")
        device_exist = self.have.get("get_site_device")

        if dest_site_exist:  
            self.status = "success"
            self.msg = "The requested site '{}' is present in the Cisco Catalyst Center and Access\
                 point can be moved to this destination site.".format(dest_site_name)
            self.log(self.msg, "INFO")

        changed_status = False
        current_site_id = self.have.get("current_site_id")

        if (current_site_id == dest_site_id):
            changed_status = True

        if  not changed_status:
            self.log("The Movement to site '{}' has been successfully verified."\
                     .format(dest_site_name), "INFO")
            self. status = "success"
            return self
        else:
            self.log("""The playbook input for site of access point '{}' does not align with \
                     the Cisco Catalyst Center, indicating that the merge task
                 may not have executed successfully.""".format(dest_site_name), "INFO")
            return self

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

    main_config = module.params.get("config")
    if main_config and (main_config[0].get("site").get("devices")):
        ccc_site = ProvisionAccesspoint(module)
        state = ccc_site.params.get("state")

        if state not in ccc_site.supported_states:
            ccc_site.status = "invalid"
            ccc_site.msg = "State {0} is invalid".format(state)
            ccc_site.check_return_status()

        ccc_site.validate_input().check_return_status()
        config_verify = ccc_site.params.get("config_verify")

        for config in ccc_site.validated_config:
            ccc_site.reset_values()
            ccc_site.get_want(config).check_return_status()
            ccc_site.get_have(config).check_return_status()
            ccc_site.get_diff_state_apply[state](config).check_return_status()

            #if config_verify:
            #    time.sleep(20)
            #    ccc_site.verify_diff_state_apply[state](config).check_return_status()

            #ccc_site.verify_diff_merged().check_return_status()
            #ccc_site.get_diff_merged().check_return_status()

            #if config_verify:
            #    ccc_site.assign_device_to_site().check_return_status()
            #    ccc_site.provision_device().check_return_status()

    elif main_config and (main_config[0].get("dest_site").get("floor")):
        ccc_network = Accesspointmovement(module)
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
            ccc_network.validate_input(config).check_return_status()

        if config_verify:
            time.sleep(5)
            ccc_network.verify_diff_state_apply[state](config).check_return_status()
    else:
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
                time.sleep(20)
                ccc_network.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_network.result)

if __name__ == '__main__':
    main()

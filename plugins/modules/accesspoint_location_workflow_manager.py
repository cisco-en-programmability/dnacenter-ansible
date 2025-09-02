#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to manage Access Point to the planned locations
in Cisco Catalyst Center, and assign the access point to floor plans."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["A Mohamed Rafeek, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: accesspoint_location_workflow_manager
short_description: Resource module for managing Access Point planned location in Cisco Catalyst Center
description: >
  This module facilitates the creation, update, assignment and deletion of Access Point planned locations
  in Cisco Catalyst Center.
  - Supports creating, assigning and deleting Access Point planned locations.
  - Enables assignment of the access point to floor plans.
version_added: "6.38.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: >
      Set to `True` to enable configuration verification on Cisco Catalyst Center after applying the playbook configuration.
      This ensures that the system validates the configuration state after the changes are applied.
    type: bool
    default: false
  state:
    description: >
      Specifies the desired state for the configuration.
      If set to `merged`, the module will create or update the configuration by adding new settings or modifying existing ones.
      If set to `deleted`, the module will remove the specified settings.
    type: str
    choices:
      - merged
      - deleted
    default: merged
  config:
    description: >
      A list containing the details required for creating or updating the Access Point planned location.
    type: list
    elements: dict
    required: true
    suboptions:
      floor_site_hierarchy:
        description: >
          Complete floor site hierarchy for the access point location.
        type: str
        required: true
      access_points:
        description: >
          List of access points to be configured at the specified location.
        type: list
        elements: dict
        required: true
      suboptions:
        accesspoint_name:
          description: >
            Complete floor site hierarchy for the access point location.
          type: str
          required: true
        mac_address:
          description: |
            The MAC address used to identify the access point.
          type: str
          required: false
        serial_number:
          description: Alternative device identification using serial numbers.
          type: str
          required: false
        accesspoint_model:
          description: Model of the access point.
          type: str
          required: true
        position:
          description: |
            The X,Y and Z coordinates representing the access point's position on the floor plan.
          type: dict
          suboptions:
            x_position:
              description: >
                The X coordinate of the access point's position. allows from 0 to 100
              type: int
              required: true
            y_position:
              description: >
                The Y coordinate of the access point's position. allows from 0 to 88
              type: int
              required: true
            z_position:
              description: >
                The Z coordinate of the access point's position. allows from 3.0 to 10.0
              type: float
              required: true
        radios:
          description: |
            List of radios details for the access point.
          type: list
          elements: dict
          required: true
          suboptions:
            - bands:
                description: >
                  Any one of radio bands supported by the access point.
                type: str
                required: true
                choices:
                  - 2.4GHz
                  - 5GHz
                  - 6GHz
              channel:
                description: |
                  The channel number for the radio interface.
                  - Radio band of "2.4GHz", valid values are from 1 to 14.
                  - Radio band of "5GHz", valid values are
                    36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108,
                    112, 116, 120, 124, 128, 132, 136, 140, 144,
                    149, 153, 157, 161, 165, 169, 173.
                  - Radio band of "6GHz", valid values are
                    1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49,
                    53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97,
                    101, 105, 109, 113, 117, 121, 125, 129, 133, 137,
                    141, 145, 149, 153, 157, 161, 165, 169, 173, 177,
                    181, 185, 189, 193, 197, 201, 205, 209, 213, 217,
                    221, 225, 229, 233.
                type: int
                required: true
              tx_power:
                description: >
                  The transmit power level of the access point.
                type: int
                required: true
              antenna:
                description: |
                  Antenna type of the access point.
                type: dict
                elements: str
                required: true
                suboptions:
                  antenna_name:
                    description: >
                      Model name of the antenna.
                    type: str
                    required: true
                  azimuth:
                    description: >
                      The azimuth angle of the antenna. starts from 1 to 360
                    type: int
                    required: true
                  elevation:
                    description: >
                      The elevation angle of the antenna. starts from -90 to 90
                    type: int
                    required: true
requirements:
  - dnacentersdk >= 2.8.6
  - python >= 3.9
seealso:
  - name: Cisco Catalyst Center API Documentation
    description: Complete API reference for device management.
    link: https://developer.cisco.com/docs/dna-center/
notes:
    # Version Compatibility
    - Minimum Catalyst Center version 3.1.3.0 required for accesspoint location workflow features.

    

  - This module utilizes the following SDK methods
    site_design.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1
    site_design.assign_sites
    site_design.retrieves_the_list_of_network_profiles_for_sites_v1
    site_design.assign_a_network_profile_for_sites_to_the_given_site_v1
    site_design.unassigns_a_network_profile_for_sites_from_multiple_sites_v1
    site_design.deletes_a_network_profile_for_sites_v1
    configuration_templates.gets_the_templates_available_v1
    network_settings.retrieve_cli_templates_attached_to_a_network_profile_v1
  - The following API paths are used
    GET /dna/intent/api/v1/networkProfilesForSites
    GET /dna/intent/api/v1/template-programmer/template
    GET /dna/intent/api/v1/networkProfilesForSites/{profileId}/templates
    POST /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments
    POST /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/bulk
    POST /api/v1/siteprofile
"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Create network profile for switch
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:
          - profile_name: "Campus_Switching_Profile"
            day_n_templates:
              - "Campus_Switch_Config_Update"
            site_names:
              - "Global/Chennai"
              - "Global/Abc"
    - name: Update network profile for switch
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:
          - profile_name: "Enterprise_Switching_Profile"
            day_n_templates:
              - "Periodic_Config_Audit"
            site_names:
              - "Global/India/Chennai/Main_Office"
              - "Global/India/Madurai/Branch_Office"
              - "Global/USA/San Francisco/Regional_HQ"
    - name: Idempotent redelete multiple switching profile
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: deleted
        config:
          - profile_name: Enterprise_Switching_Profile
          - profile_name: Local_Switching_Profile

    # Delete a switching profile by providing its profile name
    - name: Delete Specified Switching Profile
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: deleted
        config:
          - profile_name: Enterprise_Switching_Profile

    # Unassign sites from a switching profile but do not delete the profile
    - name: Unassign Sites from Switching Profile
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: deleted
        config:
          - profile_name: Enterprise_Switching_Profile
            site_names:
              - Global/India/Chennai/Main_Office

    # Unassign a template from a switching profile but do not delete the profile
    - name: Unassign Template from Switching Profile
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: deleted
        config:
          - profile_name: Enterprise_Switching_Profile
            day_n_templates:
              - Periodic_Config_Audit
"""

RETURN = r"""
# Case 1: Successful Creation of Switch Profile
response_create:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a switch profile is successfully created. The response confirms the successful
    creation of the profile and provides details about the profile, including its name
    and status.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Profile created/updated are verified successfully for '['Enterprise_Access_Switch']'.",
        "response": [
            {
                "profile_name": "Enterprise_Access_Switch",
                "status": "Network Profile [487bf1e8-b014-4cc7-9e33-1ea7c2805b4c] Successfully Created"
            }
        ],
        "status": "success"
    }

# Case 2: Successful Update of Switch Profile
response_update:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a switch profile is successfully updated. The response confirms the successful update of
    the profile and provides details about the profile, including its name and status.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Profile created/updated are verified successfully for '['Campus_Core_Switch_Profile']'.",
        "response": [
                {
                    "profile_name": "Campus_Core_Switch_Profile",
                    "status": "Network profile 'Campus_Core_Switch_Profile' updated successfully"
                }
            ],
        "status": "success"
    }

# Case 3: Idempotent Delete of Multiple Switching Profiles
response_delete_idempotent:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK.
    This response is provided when attempting to delete switching profiles in an idempotent manner.
    If the profiles are already deleted, the response indicates that no changes were required.
  returned: always
  type: dict
  sample: >
    {
        "msg": "No changes required, profile(s) are already deleted.",
        "response": "No changes required, profile(s) are already deleted.",
        "status": "success"
    }

# Case 4: Successful Deletion of Switch Profile
response_delete_profile:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a switch profile is successfully deleted or unassigned. The response confirms the
    deletion/unassignment and provides details of the profile and its associated operations.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Switch profile(s) deleted/unassigned and verified successfully for '['Enterprise_Switching_Profile']'.",
        "response": [
            {
                "profile_name": "Enterprise_Switching_Profile",
                "site_unassign_status": "Site(s) are unassigned successfully.",
                "status": "Network profile [740ebd91-4f82-42ac-bbca-94393f0cc799] successfully deleted"
            }
        ],
        "status": "success"
    }

# Case 5: Successfully Unassign Sites from the Profile
response_unassign_site:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a site is successfully unassigned from a switch profile. The response confirms the
    unassignment and provides details about the profile and site(s) affected.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Switch profile(s) deleted/unassigned and verified successfully for '['Enterprise_Switching_Profile']'.",
        "response": [
            {
                "profile_name": "Enterprise_Switching_Profile",
                "site_unassign_status": "Site(s) '['Global/India/Chennai/Main_Office']' unassigned successfully."
            }
        ],
        "status": "success"
    }

# Case 6: Successfully Unassign Templates from the Profile
response_unassign_template:
  description: >
    A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK
    when a template is successfully unassigned from a switch profile. The response confirms the
    unassignment and provides details about the profile and the template(s) affected.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Switch profile(s) deleted/unassigned and verified successfully for '['Enterprise_Switching_Profile']'.",
        "response": [
            {
                "profile_name": "Enterprise_Switching_Profile",
                "template_unassign_status": "Template(s) '['Periodic_Config_Audit']' unassigned successfully."
            }
        ],
        "status": "success"
    }
"""


try:
    import requests

    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    requests = None
import time
import re
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    validate_str,
    get_dict_result,
)
from ansible.module_utils.basic import AnsibleModule


class AccessPointLocation(DnacBase):
    """Class containing member attributes for network profile workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.location_created, self.location_deleted = [], []
        self.location_not_created, self.location_not_deleted = [], []
        self.location_exist, self.location_already_deleted = [], []

        self.result_response = {
            "success_responses": self.location_created,
            "unprocessed": self.location_not_created,
            "already_processed": self.location_exist
        }

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.

        Returns:
            The method updates these attributes of the instance:
                - msg: A message describing the validation result.
                - self.status: The status of the validation ('success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        """
        temp_spec = {
            "floor_site_hierarchy": {"type": "str", "required": True},
            "access_points": {
                "type": "list",
                "elements": "dict",
                "accesspoint_name": {"type": "str", "required": True},
                "mac_address": {"type": "str"},
                "serial_number": {"type": "str"},
                "accesspoint_model": {"type": "str", "required": True},
                "position": {
                    "type": "dict",
                    "x_position": {"type": "int", "required": True},
                    "y_position": {"type": "int", "required": True},
                    "z_position": {"type": "int", "required": True},
                },
                "radios": {
                    "type": "list",
                    "elements": "dict",
                    "bands": {"type": "str", "required": True},
                    "channel": {"type": "int", "required": True},
                    "tx_power": {"type": "int", "required": True},
                    "antenna": {
                        "type": "dict",
                        "antenna_name": {"type": "str", "required": True},
                        "azimuth": {"type": "int", "required": True},
                        "elevation": {"type": "int", "required": True},
                    },
                },
            },
        }

        if not self.config:
            msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, msg, "ERROR")
            return self

        # Validate configuration against the specification
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            msg = "The playbook contains invalid parameters: {0}".format(invalid_params)
            self.result["response"] = msg
            self.set_operation_result("failed", False, msg, "ERROR")
            return self

        self.validated_config = valid_temp
        msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(
            str(valid_temp)
        )
        self.log(msg, "INFO")

        return self

    def input_data_validation(self, config):
        """
        Additional validation to check if the provided input switch profile is correct
        and as per the UI Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            config (dict): Dictionary containing the Access point planned location details.

        Returns:
            list: List of invalid access point location data with details.

        Description:
            Iterates through available access point location details and Returns the list of invalid
            data for further action or validation.
        """
        self.log(
            "Validating input data from Playbook config: {0}".format(config), "INFO"
        )
        errormsg = []

        floor_site_hierarchy = config.get("floor_site_hierarchy", "")
        if floor_site_hierarchy:
            param_spec = dict(type="str", length_max=200)
            validate_str(floor_site_hierarchy, param_spec, "floor_site_hierarchy", errormsg)
        else:
            errormsg.append("floor_site_hierarchy: Floor Site Hierarchy is missing in playbook.")

        access_points = config.get("access_points", [])
        duplicate_name = self.find_duplicate_value(access_points, "accesspoint_name")
        if duplicate_name:
            errormsg.append(
                "accesspoint_name: Duplicate Access Point Name(s) '{0}' found in playbook.".format(
                    duplicate_name
                )
            )

        for each_access_point in access_points:
            accesspoint_name = each_access_point.get("accesspoint_name")
            if accesspoint_name:
                param_spec = dict(type="str", length_max=255)
                validate_str(accesspoint_name, param_spec, "accesspoint_name", errormsg)
            else:
                errormsg.append("accesspoint_name: Access Point Name is missing in playbook.")

            mac_address = each_access_point.get("mac_address")
            if mac_address:
                param_spec = dict(type="str", length_max=17)
                validate_str(mac_address, param_spec, "mac_address", errormsg)

            serial_number = each_access_point.get("serial_number")
            if serial_number:
                param_spec = dict(type="str", length_max=200)
                validate_str(serial_number, param_spec, "serial_number", errormsg)

            accesspoint_model = each_access_point.get("accesspoint_model")
            if accesspoint_model:
                param_spec = dict(type="str", length_max=50)
                validate_str(accesspoint_model, param_spec, "accesspoint_model", errormsg)

            position = each_access_point.get("position")
            if position:

                x_position = each_access_point.get("x_position")
                if x_position is None:
                    errormsg.append("x_position: X Position is missing in playbook.")
                elif x_position and isinstance(x_position, int) and not (0 < x_position < 100):
                    errormsg.append("x_position: X Position must be between 0 and 100.")

                y_position = each_access_point.get("y_position")
                if y_position is None:
                    errormsg.append("y_position: Y Position is missing in playbook.")
                elif y_position and isinstance(y_position, int) and not(0 < y_position < 88):
                    errormsg.append("y_position: Y Position must be between 0 and 88.")

                z_position = each_access_point.get("z_position")
                if z_position is None:
                    errormsg.append("z_position: Z Position is missing in playbook.")
                elif z_position and isinstance(z_position, (int, float)) and not (3 < z_position < 10):
                    errormsg.append("z_position: Z Position must be between 3 and 10.")

            radios = each_access_point.get("radios")
            if not radios:
                errormsg.append("radios: Radios is missing in playbook.")
            elif radios and isinstance(radios, list):
                self.validate_radios(radios, errormsg)

                # for radio in radios:
                #     bands = radio.get("bands")
                #     if bands:
                #         param_spec = dict(type="str", length_max=6)
                #         validate_str(bands, param_spec, "bands", errormsg)
                #         if bands not in ["2.4GHz", "5GHz", "6GHz"]:
                #             errormsg.append(
                #                 "bands: Bands must be one of '2.4GHz', '5GHz' or '6GHz'."
                #             )
                #     else:
                #         errormsg.append("bands: Bands is missing in playbook.")

                #     channel = radio.get("channel")
                #     channel_5GHz = [
                #         36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108,
                #         112, 116, 120, 124, 128, 132, 136, 140, 144,
                #         149, 153, 157, 161, 165, 169, 173
                #     ]
                #     channel_6GHz = [
                #         1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45,
                #         49, 53, 57, 61, 65, 69, 73, 77, 81, 85,
                #         89, 93, 97, 101, 105, 109, 113, 117,
                #         121, 125, 129, 133, 137, 141, 145, 149, 153,
                #         157, 161, 165, 169, 173, 177, 181, 185, 189,
                #         193, 197, 201, 205, 209, 213, 217,
                #         221, 225, 229, 233]
                #     if channel is None:
                #         errormsg.append("channel: Channel is missing in playbook.")
                #     elif channel and isinstance(channel, int):
                #         if bands == "2.4GHz" and not (0 < channel < 15):
                #             errormsg.append("channel: Channel must be between 1 and 14 for 2.4GHz band.")
                #         elif bands == "5GHz" and channel not in channel_5GHz:
                #             errormsg.append(
                #                 "channel: Channel must be one of '{0}' for 5GHz band.".format(
                #                     str(channel_5GHz)
                #                 )
                #             )
                #         elif bands == "6GHz" and channel not in channel_6GHz:
                #             errormsg.append(
                #                 "channel: Channel must be one of '{0}' for 6GHz band.".format(
                #                     str(channel_6GHz)
                #                 )
                #             )

                #     tx_power = radio.get("tx_power")
                #     if tx_power is None:
                #         errormsg.append("tx_power: Tx Power is missing in playbook.")
                #     elif tx_power and isinstance(tx_power, int) and not (0 < tx_power < 101):
                #         errormsg.append("tx_power: Tx Power must be between 0 and 100.")

                #     antenna = radio.get("antenna")
                #     if antenna is None:
                #         errormsg.append("antenna: Antenna is missing in playbook.")
                #     elif antenna and isinstance(antenna, dict):
                #         antenna_name = antenna.get("antenna_name")
                #         if antenna_name:
                #             param_spec = dict(type="str", length_max=50)
                #             validate_str(antenna_name, param_spec, "antenna_name", errormsg)
                #         else:
                #             errormsg.append("antenna_name: Antenna Name is missing in playbook.")

                #         azimuth = antenna.get("azimuth")
                #         if azimuth is None:
                #             errormsg.append("azimuth: Azimuth is missing in playbook.")
                #         elif azimuth and isinstance(azimuth, int) and not (0 < azimuth < 361):
                #             errormsg.append("azimuth: Azimuth must be between 1 and 360.")

                #         elevation = antenna.get("elevation")
                #         if elevation is None:
                #             errormsg.append("elevation: Elevation is missing in playbook.")
                #         elif elevation and isinstance(elevation, int) and not (-91 < elevation < 91):
                #             errormsg.append("elevation: Elevation must be between -90 and 90.")

        if errormsg:
            self.msg = "Invalid parameters in playbook config: '{0}' ".format(errormsg)
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        msg = "Successfully validated config params: {0}".format(str(config))
        self.log(msg, "INFO")
        return self

    def validate_radios(self, radios_param, errormsg):
        """
        Validate the radio configuration parameters.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            radios_param (list): A list of radio configuration dictionaries.
            errormsg (list): A list to collect error messages.
        
        Returns:
            list: List of invalid access point location radios data with details.

        Description:
            Iterates through available access point location radios details and Returns the list of invalid
            data for further action or validation.

        """
        for radio in radios_param:
            bands = radio.get("bands")
            if bands:
                param_spec = dict(type="str", length_max=6)
                validate_str(bands, param_spec, "bands", errormsg)
                if bands not in ["2.4GHz", "5GHz", "6GHz"]:
                    errormsg.append(
                        "bands: Bands must be one of '2.4GHz', '5GHz' or '6GHz'."
                    )
            else:
                errormsg.append("bands: Bands is missing in playbook.")

            channel = radio.get("channel")
            channel_5GHz = [
                36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108,
                112, 116, 120, 124, 128, 132, 136, 140, 144,
                149, 153, 157, 161, 165, 169, 173
            ]
            channel_6GHz = [
                1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45,
                49, 53, 57, 61, 65, 69, 73, 77, 81, 85,
                89, 93, 97, 101, 105, 109, 113, 117,
                121, 125, 129, 133, 137, 141, 145, 149, 153,
                157, 161, 165, 169, 173, 177, 181, 185, 189,
                193, 197, 201, 205, 209, 213, 217,
                221, 225, 229, 233]
            if channel is None:
                errormsg.append("channel: Channel is missing in playbook.")
            elif channel and isinstance(channel, int):
                if bands == "2.4GHz" and not (0 < channel < 15):
                    errormsg.append("channel: Channel must be between 1 and 14 for 2.4GHz band.")
                elif bands == "5GHz" and channel not in channel_5GHz:
                    errormsg.append(
                        "channel: Channel must be one of '{0}' for 5GHz band.".format(
                            str(channel_5GHz)
                        )
                    )
                elif bands == "6GHz" and channel not in channel_6GHz:
                    errormsg.append(
                        "channel: Channel must be one of '{0}' for 6GHz band.".format(
                            str(channel_6GHz)
                        )
                    )

            tx_power = radio.get("tx_power")
            if tx_power is None:
                errormsg.append("tx_power: Tx Power is missing in playbook.")
            elif tx_power and isinstance(tx_power, int) and not (0 < tx_power < 101):
                errormsg.append("tx_power: Tx Power must be between 0 and 100.")

            antenna = radio.get("antenna")
            if antenna is None:
                errormsg.append("antenna: Antenna is missing in playbook.")
            elif antenna and isinstance(antenna, dict):
                antenna_name = antenna.get("antenna_name")
                if antenna_name:
                    param_spec = dict(type="str", length_max=50)
                    validate_str(antenna_name, param_spec, "antenna_name", errormsg)
                else:
                    errormsg.append("antenna_name: Antenna Name is missing in playbook.")

                azimuth = antenna.get("azimuth")
                if azimuth is None:
                    errormsg.append("azimuth: Azimuth is missing in playbook.")
                elif azimuth and isinstance(azimuth, int) and not (0 < azimuth < 361):
                    errormsg.append("azimuth: Azimuth must be between 1 and 360.")

                elevation = antenna.get("elevation")
                if elevation is None:
                    errormsg.append("elevation: Elevation is missing in playbook.")
                elif elevation and isinstance(elevation, int) and not (-91 < elevation < 91):
                    errormsg.append("elevation: Elevation must be between -90 and 90.")

        self.log("Radio configuration validation completed.", "DEBUG")
        return errormsg

    def get_want(self, config):
        """
        Retrieve access point planned location playbook config

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing access point location details.

        Returns:
            self: The current instance of the class with updated 'want' attributes.

        Description:
            This function parses the playbook configuration to extract information related
            to access point location profile. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """
        self.log(
            "Validating input data and update to want for: {0}".format(config), "INFO"
        )

        self.input_data_validation(config).check_return_status()
        want = {}
        if config:
            want["ap_location"] = config

        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")

        return self

    def get_have(self, config):
        """
        Get required details for the given access point location config from Cisco Catalyst Center

        Parameters:
            config (dict) - Playbook details containing access point location

        Returns:
            self - The current object with site details and access point location
            information collection for create and update.
        """

        self.log(
            "Collecting access point location related information for: {0}".format(
                config
            ),
            "INFO",
        )

        response = self.get_site(config.get("floor_site_hierarchy"))
        if not response:
            msg = "No response received from API for the site: {0}".format(
                config.get("floor_site_hierarchy")
            )
            self.log(msg, "WARNING")
            self.fail_and_exit(msg)

        site = response["response"][0]
        if not site.get("id"):
            msg = "No site information found for: {0}".format(config)
            self.log(msg, "WARNING")
            self.fail_and_exit(msg)

        have = {}
        have["site_id"] = site["id"]
        have["site_name"] = config.get("floor_site_hierarchy")

        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")

        return self

    def get_diff_merged(self, config):
        """
        Update or create network switch profile in Cisco Catalyst Center based on the
        playbook details

        Parameters:
            config (list of dict) - Playbook details containing switch profile information.

        Returns:
            self - The current object with message and created/updated response information.
        """
        self.log(
            "Starting to create/update switch profile for: {0}".format(config), "INFO"
        )



        if self.location_created:
            self.msg = "Access Point Location created/updated successfully for '{0}'.".format(
                str(self.location_created)
            )
            self.log(self.msg, "INFO")
            self.changed = True

        if self.location_not_created:
            self.msg += " Unable to process the following Access Point Location(s): '{0}'. They may not have been created or already exist.".format(
                ", ".join(map(str, self.location_not_created))
            )
            self.log(self.msg, "DEBUG")

        self.log(self.msg, "INFO")
        self.set_operation_result(
            self.status, self.changed, self.msg, "INFO", self.result_response
        ).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing network switch profile
                            releated information.

        Returns:
            self - The current object with message and response information.
        """
        self.log(
            "Starting to verify created/updated Access Point Location(s) for: {0}".format(config),
            "INFO",
        )

        msg = "Access Point Location(s) created/updated are verified successfully for '{0}'.".format(
            str(self.location_created)
        )
        self.log(msg, "INFO")
        self.set_operation_result(
            "success", True, msg, "INFO", self.location_created
        ).check_return_status()
        return self

    def get_diff_deleted(self, config):
        """
        Delete Network switch profile in Cisco Catalyst Center based on playbook details.

        Parameters:
            config (list of dict) - Playbook details

        Returns:
            self - The current object with profile deletion message and response information.
        """
        self.log("Starting to delete switch profile(s) for: {0}".format(config), "INFO")


        return self

    def verify_diff_deleted(self, config):
        """
        Validates that the switch profile(s) in Cisco Catalyst Center have been deleted
        based on the playbook details.

        Parameters:
            config (dict) - Playbook details containing Network profile switch information.

        Returns:
            self - The current object with message and response.
        """
        self.log(
            "Starting to verify the deleted Access Point Location(s) for: {0}".format(config),
            "INFO",
        )

        if len(self.location_not_deleted) > 0:
            self.msg += " Unable to delete below Access Point Location(s) '{0}'.".format(config)
            self.changed = False
            self.status = "failed"

        if len(self.location_exist) == len(config):
            self.msg = "No Changes required, Access Point Location(s) already deleted/unassigned " +\
                "and verified successfully for '{0}'.".format(self.location_exist)
            self.changed = False
            self.status = "success"

        self.log(self.msg, "INFO")
        self.set_operation_result(
            self.status, self.changed, self.msg, "INFO", self.location_deleted
        ).check_return_status()
        return self


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": "str", "required": True},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"type": "list", "required": True, "elements": "dict"},
        "state": {"default": "merged", "choices": ["merged", "deleted"]},
        "validate_response_schema": {"type": "bool", "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_ap_location = AccessPointLocation(module)
    state = ccc_ap_location.params.get("state")

    if (
        ccc_ap_location.compare_dnac_versions(
            ccc_ap_location.get_ccc_version(), "3.1.3.0"
        )
        < 0
    ):
        ccc_ap_location.status = "failed"
        ccc_ap_location.msg = (
            "The specified version '{0}' does not support the network profile workflow feature."
            "Supported version(s) start from '3.1.3.0' onwards.".format(
                ccc_ap_location.get_ccc_version()
            )
        )
        ccc_ap_location.log(ccc_ap_location.msg, "ERROR")
        ccc_ap_location.check_return_status()

    if state not in ccc_ap_location.supported_states:
        ccc_ap_location.status = "invalid"
        ccc_ap_location.msg = "State {0} is invalid".format(state)
        ccc_ap_location.check_return_status()

    ccc_ap_location.validate_input().check_return_status()
    config_verify = ccc_ap_location.params.get("config_verify")

    for config in ccc_ap_location.validated_config:
        if not config:
            ccc_ap_location.msg = "Playbook configuration is missing."
            ccc_ap_location.log(ccc_ap_location.msg, "ERROR")
            ccc_ap_location.fail_and_exit(ccc_ap_location.msg)

        ccc_ap_location.reset_values()
        ccc_ap_location.get_want(config).check_return_status()
        ccc_ap_location.get_have(config).check_return_status()
        ccc_ap_location.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_ap_location.verify_diff_state_apply[state](
                config
            ).check_return_status()

    ccc_ap_location.final_response_message(state).check_return_status()
    module.exit_json(**ccc_ap_location.result)


if __name__ == "__main__":
    main()

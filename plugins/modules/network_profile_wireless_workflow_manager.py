#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on create and delete wireless network profile details
in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["A Mohamed Rafeek, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: network_profile_wireless_workflow_manager
short_description: Resource module for managing network wireless profile in Cisco Catalyst Center
description:
    - This module allows the creation and deletion of wireless profiles in Cisco Catalyst Center.
    - It enables configuring SSID details, assigning profile names, and managing
      additional interface settings, destination ports, and protocols.
    - This module interacts with Cisco Catalyst Center's to create profile name, SSID details,
      additinal interface details destination port and protcol.
version_added: "6.31.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description: |
      Set to `True` to enable configuration verification on Cisco Catalyst Center
      after applying the playbook config. This will ensure that the system validates
      the configuration state after the change is applied.
    type: bool
    default: false
  offset_limit:
    description: |
      Set the offset limit based on the API data limit for each pagination.
    type: int
    default: 500
  state:
    description: |
      Specifies the desired state for the configuration. If "merged", the module
      will create or update the configuration, adding new settings or modifying existing
      ones. If "deleted", it will remove the specified settings.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description: A list containing the details for network wireless profile creation.
    type: list
    elements: dict
    required: true
    suboptions:
      profile_name:
        description: Name the wireless profile needs to be created.
        type: str
        required: true
      site_names:
        description: |
          List of site names assigned to the profile. For example, ["Global/USA/New York/BLDNYC"].
        type: list
        elements: str
        required: false
      ssid_details:
        description: |
            Contains ssid details to update for the wireless network profile.
        type: list
        elements: dict
        required: false
        suboptions:
          ssid:
            description: The name of the SSID (Service Set Identifier) to be configured.
            type: str
            required: true
          dot11be_profile_name:
            description: |
              The 802.11be profile name to be assigned to this SSID.
              This profile defines advanced Wi-Fi 7 (802.11be) parameters to optimize
              network performance and efficiency.
            type: str
            required: true
          enable_fabric:
            description: |
              Set to `True` to enable fabric mode for this SSID.
              When enabled, the SSID operates within a Cisco SD-Access fabric network,
              leveraging policy-based segmentation and automation.
            type: bool
            required: false
          vlan_group_name:
            description: |
              The VLAN group name to which this SSID belongs, if applicable.
              VLAN groups allow multiple VLANs to be logically grouped for efficient
              traffic segmentation and policy enforcement.
            type: str
            required: false
          interface_name:
            description: |
              The name of the network interface where this SSID is configured.
              If specified, the SSID will be mapped to this interface instead of
              being part of a VLAN group.
            type: str
            required: false
          anchor_group_name:
            description: |
              The name of the anchor group if SSID anchoring is required.
              SSID anchoring is used in mobility architectures where traffic
              for a particular SSID is tunneled to a designated anchor controller.
            type: str
            required: false
          local_to_vlan:
            description: |
              The VLAN ID to which the SSID is mapped. This must be a numeric value
              between 1 and 4094, ensuring proper network segmentation.
            type: int
            required: false
      ap_zones:
        description: |
          Defines AP (Access Point) zones that need to be associated with
          the wireless network profile.
        type: list
        elements: dict
        required: false
        suboptions:
          ap_zone_name:
            description: Name of the AP zone to be created and associated with the wireless profile.
            type: str
            required: true
          ssids:
            description: |
              A list of SSIDs to be linked to this AP zone.
              For example, ["SSID1", "SSID2"].
            type: list
            elements: str
            required: false
          rf_profile_name:
            description: |
              Specifies the Radio Frequency (RF) profile to be assigned to the AP zone.
              This can be a predefined profile such as "HIGH", "LOW", "TYPICAL",
              or a custom RF profile created by the user.
              For example, "HIGH".
            type: str
            required: false
      onboarding_templates:
        description: |
          List of onboarding template names assigned to the profile.
        type: list
        elements: str
        required: false
      day_n_templates:
        description: |
          List of Day-N template names assigned to the profile.
        type: list
        elements: str
        required: false
      additional_interfaces:
        description: |
          Specifies additional interfaces to be added to this wireless profile.
          If the specified interface name and VLAN ID do not exist, they will be created.
        type: list
        elements: dict
        required: false
        suboptions:
          interface_name:
            description: Name of the additional interface.
            type: str
            required: true
          vlan_id:
            description: |
              VLAN ID for the interface. It must be a numeric value between 1 and 4094.
              This field is required if the VLAN interface and ID do not already exist.
            type: int
            required: true

requirements:
- dnacentersdk >= 2.8.6
- python >= 3.9
notes:
 - SDK Method used are
    wireless.create_wireless_profile ,
    wireless.update_application_policy,
    wireless.get_wireless_profile,
    site_design.assign_sites,
    wireless.get_interfaces_v1
    wireless.create_interface_v1

 - Paths used are
    GET dna/intent/api/v1/wirelessProfiles
    POST dna/intent/api/v1/wirelessProfiles/{
    GET /dna/intent/api/v1/app-policy-intent
    DELETE /dna/intent/api/v1/app-policy-intent
    GET /dna/intent/api/v1/wirelessSettings/interfaces
    POST /dna/intent/api/v1/wirelessSettings/interfaces
"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  connection: local
  tasks:
    - name: Create network wireless profile
      cisco.dnac.network_profile_wireless_workflow_manager:
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
        offset_limit: 500
        state: merged
        config:
          - profile_name: "Corporate_Wireless_Profile"
            site_names:
              - "Global/Headquarters"
              - "Global/BranchOffice"
            ssid_details:
              - ssid_name: "Corporate_WiFi"
                enable_fabric: false
                profile_name: "Corporate_WiFi_Profile"
                policy_profile_name: "Corporate_Access_Policy"
                vlan_group_name: "Corporate_VLAN_Group"
              - ssid_name: "Guest_WiFi"
                enable_fabric: false
                profile_name: "Guest_WiFi_Profile"
                policy_profile_name: "Guest_Access_Policy"
                interface_name: "guest_network"
                local_to_vlan: 3002
            ap_zones:
              - ap_zone_name: "HQ_AP_Zone"
                rf_profile_name: "HIGH"
                ssids:
                  - "Corporate_WiFi"
              - ap_zone_name: "Branch_AP_Zone"
                rf_profile_name: "TYPICAL"
                ssids:
                  - "Guest_WiFi"
            additional_interfaces:
              - interface_name: "Corp_Interface_1"
                vlan_id: 100
              - interface_name: "Guest_Interface_1"
                vlan_id: 3002
            onboarding_templates:
              - "Corporate_Onboarding_Template"
            day_n_templates:
              - "Wireless_Controller_Config"

"""

RETURN = r"""

# Case 1: Successful creation/updatation of wireless profile
response_create:
  description: A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK.
    This response indicates that the wireless profile was either created or updated successfully.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Wireless Profile created/updated successfully for '[{'profile_name': 'Corporate_Wireless_Profile',
            'status': 'Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] Successfully created'}]'.",
        "response": [
            {
                "profile_name": "Corporate_Wireless_Profile",
                "status": "Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] created Successfully"
            }
        ],
        "status": "success"
    }

# Case 2: Successfully deleted wireless profile
response_delete:
  description: A dictionary or list containing the response returned by the Cisco Catalyst Center Python SDK.
    This response indicates that the wireless profile was successfully deleted from the system.
  returned: always
  type: dict
  sample: >
    {
        "msg": "Wireless Profile deleted successfully for '[{'profile_name': 'Corporate_Wireless_Profile',
        'status': 'Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] Successfully Deleted'}]'.",
        "response": [
            {
                "profile_name": "Corporate_Wireless_Profile",
                "status": "Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] Successfully Deleted"
            }
        ],
        "status": "success"
    }

"""

import re
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    validate_list_of_dicts,
    validate_str
)
from ansible_collections.cisco.dnac.plugins.module_utils.network_profiles import (
    NetworkProfileFunctions
)


class NetworkWirelessProfile(NetworkProfileFunctions):
    """Class containing member attributes for network profile workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.created, self.deleted, self.not_processed = [], [], []

        self.keymap = dict(
            profile_name="wirelessProfileName",
            rf_profile_name="rfProfileName",
            sites="sites",
            ssid="ssidName",
            wlan_profile_name="wlanProfileName",
            dot11be_profile_name="dot11beProfileId",
            vlan_group_name="vlanGroupName",
            enable_fabric="enableFabric",
            interface_name="interfaceName",
            local_to_vlan="localToVlan",
            anchor_group_name="anchorGroupName",
            policy_profile_name="policyProfileName",
            ap_zone_name="apZoneName"
        )

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.

        Returns:
            The method updates these attributes of the instance:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation ('success' or 'failed').
                - self.validated_config: If successful, validated version of 'config' parameter.
        """
        temp_spec = {
            'profile_name': {'type': 'str', 'required': True},
            'site_names': {'type': 'list', 'elements': 'str', 'required': False},
            'ssid_details': {
                'type': 'list',
                'elements': 'dict',
                'ssid': {'type': 'str', 'required': False},
                'dot11be_profile_name': {'type': 'str', 'required': False},
                'enable_fabric': {'type': 'bool', 'default': False},
                'vlan_group_name': {'type': 'str', 'required': False},
                'interface_name': {'type': 'str', 'required': False},
                'anchor_group_name': {'type': 'str', 'required': False},
                'local_to_vlan': {'type': 'int', 'range_min': 1, 'range_max': 4094, 'required': False}
            },
            'ap_zones': {
                'type': 'list',
                'elements': 'dict',
                'ap_zone_name': {'type': 'str', 'required': False},
                'rf_profile_name': {'type': 'str', 'required': False},
                'ssids': {'type': 'list', 'elements': 'str', 'required': False},
            },
            'onboarding_templates': {'type': 'list', 'elements': 'str', 'required': False},
            'day_n_templates': {'type': 'list', 'elements': 'str', 'required': False},
            'additional_interfaces': {
                'type': 'list',
                'elements': 'dict',
                'interface_name': {'type': 'str', 'required': True},
                'vlan_id': {'type': 'int', 'range_min': 1, 'range_max': 4094, 'required': True}
            }
        }

        if not self.config:
            msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, msg, "ERROR")
            return self

        # Validate configuration against the specification
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        duplicate_profile = self.find_duplicate_value(self.config, "profile_name")
        if duplicate_profile:
            msg = "profile_name: Duplicate Profile Name(s) '{0}' found in playbook.".format(
                duplicate_profile)
            self.result['response'] = msg
            self.set_operation_result("failed", False, msg, "ERROR").check_return_status()

        if invalid_params:
            msg = "The playbook contains invalid parameters: {0}".format(
                invalid_params)
            self.result['response'] = msg
            self.set_operation_result("failed", False, msg, "ERROR").check_return_status()

        self.validated_config = valid_temp
        msg = "Successfully validated playbook configuration parameters using " +\
            "'validate_input': {0}".format(str(valid_temp))
        self.log(msg, "INFO")

        return self

    def input_data_validation(self, config):
        """
        Additional validation to check if the provided input wireless profile is correct
        and as per the UI Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            config (dict): Dictionary containing the wirelss profile details.

        Returns:
            self - The current object with input config details

        """
        errormsg = []
        param_spec_str = dict(type="str")

        profile_name = config.get("profile_name")
        if profile_name:
            validate_str(profile_name, param_spec_str, "profile_name", errormsg)
        else:
            errormsg.append("profile_name: Profile Name is missing in playbook.")

        if self.payload.get("state") == "deleted":
            return self

        site_names = config.get("site_names")
        if site_names:
            for sites in site_names:
                validate_str(sites, param_spec_str, "sites", errormsg)
                duplicate_sites = list(set([site for site in site_names
                                            if site_names.count(site) > 1]))
                if duplicate_sites:
                    errormsg.append("Duplicate site(s) '{0}' found in site_names".format(
                        duplicate_sites))
                    break

        ssid_list = config.get("ssid_details")
        if ssid_list:
            self.validate_ssid_info(ssid_list, config, errormsg)

        onboarding_templates = config.get("onboarding_templates")
        day_n_templates = config.get("day_n_templates")
        if onboarding_templates:
            for template_name in onboarding_templates:
                validate_str(template_name, param_spec_str, "onboarding_templates", errormsg)
                duplicate_template = list(set([template for template in onboarding_templates
                                               if onboarding_templates.count(template) > 1]))
                if duplicate_template:
                    errormsg.append("Duplicate template(s) '{0}' found in onboarding_templates".format(
                        duplicate_template))
                    break

                if template_name in day_n_templates:
                    errormsg.append("Onboarding_templates: Duplicate template " +
                                    "'{0}' found in day_n_templates".format(template_name))
                    break

        if day_n_templates:
            for template_name in day_n_templates:
                validate_str(template_name, param_spec_str, "day_n_templates", errormsg)
                duplicate_template = list(set([template for template in day_n_templates
                                               if day_n_templates.count(template) > 1]))
                if duplicate_template:
                    errormsg.append("Duplicate template(s) '{0}' found in day_n_templates".format(
                        duplicate_template))
                    break

        additional_interfaces = config.get("additional_interfaces")
        if additional_interfaces:
            duplicate_interfaces = self.find_duplicate_value(additional_interfaces, "interface_name")
            if duplicate_interfaces:
                msg = "interface_name: Duplicate interface name(s) '{0}' found in playbook.".format(
                    duplicate_interfaces)
                errormsg.append(msg)

            for interface in additional_interfaces:
                interface_name = interface.get("interface_name")
                if interface_name:
                    validate_str(interface_name, dict(type="str", length_max=31),
                                 "interface_name", errormsg)
                else:
                    errormsg.append("interface_name: additional_interfaces of Interface Name is missing in playbook.")

                vlan_id = interface.get("vlan_id")
                if vlan_id is not None:
                    try:
                        vlan_id = int(vlan_id)
                        if vlan_id not in range(1, 4094):
                            errormsg.append(
                                "vlan_id: Invalid Additional Interface VLAN ID '{0}' in playbook.".
                                format(vlan_id))
                    except ValueError:
                        errormsg.append("vlan_id: VLAN ID '{0}' must be an integer.".format(vlan_id))
                else:
                    errormsg.append("vlan_id: VLAN ID of Interface is missing in playbook.")

        if errormsg:
            msg = "Invalid parameters in playbook config: '{0}' ".format(errormsg)
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

        msg = "Successfully validated config params: {0}".format(str(config))
        self.log(msg, "INFO")
        return self

    def validate_ssid_info(self, ssid_list, config, errormsg):
        """
        Extends validation for SSID Details.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            ssid_list (list): List of dictionaries containing SSID details.
            errormsg(list) - List contains error message any validation failure.

        Returns:
            errormsg(list) - List contains error message any validation failure.
        """
        self.log("Starting SSID validation...", "DEBUG")
        for ssid_details in ssid_list:
            ssid = ssid_details.get("ssid")
            if ssid:
                self.log("Validating SSID: {0}".format(ssid), "DEBUG")
                param_spec = dict(type="str", length_max=32)
                validate_str(ssid, param_spec, "ssid", errormsg)
            else:
                errormsg.append("ssid: SSID is missing in playbook.")

            enable_fabric = ssid_details.get("enable_fabric")
            if enable_fabric and enable_fabric not in (True, False):
                errormsg.append("enable_fabric: Invalid enable fabric '{0}' in playbook. either true or false."
                                .format(enable_fabric))

            dot11be_profile_name = ssid_details.get("dot11be_profile_name")
            if dot11be_profile_name:
                param_spec = dict(type="str", length_max=32)
                validate_str(dot11be_profile_name, param_spec, "dot11be_profile_name", errormsg)

            if not enable_fabric:
                vlan_group_name = ssid_details.get("vlan_group_name")
                if vlan_group_name:
                    param_spec = dict(type="str", length_max=32)
                    validate_str(vlan_group_name, param_spec, "vlan_group_name", errormsg)

                interface_name = ssid_details.get("interface_name")
                if interface_name:
                    param_spec = dict(type="str", length_max=31)
                    validate_str(interface_name, param_spec, "interface_name", errormsg)

                anchor_group_name = ssid_details.get("anchor_group_name")
                if anchor_group_name:
                    param_spec = dict(type="str", length_max=32)
                    validate_str(anchor_group_name, param_spec, "anchor_group_name", errormsg)

                local_to_vlan = ssid_details.get("local_to_vlan")
                if local_to_vlan and local_to_vlan not in range(1, 4094) and interface_name:
                    errormsg.append("local_to_vlan: Invalid local vlan number '{0}' in playbook."
                                    .format(local_to_vlan))

                if not (vlan_group_name or interface_name):
                    errormsg.append("Either VLAN Group Name or Interface Name required in playbook.")

                if anchor_group_name:
                    if vlan_group_name and interface_name:
                        errormsg.append("If the SSID includes an anchor group name, " +
                                        "either vlan group name or interface name must " +
                                        "be specified, but not necessarily both")

                if vlan_group_name and interface_name:
                    errormsg.append("Either vlan group name or interface name must " +
                                    "be specified, but not necessarily both")

                if vlan_group_name and local_to_vlan:
                    errormsg.append("Either vlan group name or Local to vlan must " +
                                    "be specified, but not necessarily both")

                ap_zone_list = config.get("ap_zones")
                if ap_zone_list:
                    duplicate_zone_name = self.find_duplicate_value(ap_zone_list, "ap_zone_name")
                    if duplicate_zone_name:
                        msg = "ap_zone_name: Duplicate AP zone name(s) '{0}' found in playbook.".format(
                            duplicate_zone_name)
                        errormsg.append(msg)

                    if len(ap_zone_list) > 100:
                        errormsg.append("ap_zones: AP zones list is more than 100 in playbook.")
                    else:
                        for ap_zones in ap_zone_list:
                            if ap_zones:
                                self.validate_ap_zone(ap_zones, ssid_list, errormsg)

    def validate_ap_zone(self, ap_zones, ssid_list, errormsg):
        """
        Extends validation for AP zone values.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            ap_zones (dict) - Contains AP zone data given from playbook
            ssid_list (list) - Contains list of dict contains SSID details to validate AP
                               zone SSID

        Returns:
            No return, collect the error message in case of any validation failure.
        """
        self.log("Starting AP Zone validation...", "DEBUG")

        ap_zone_name = ap_zones.get("ap_zone_name")
        if ap_zone_name:
            param_spec = dict(type="str", length_max=32)
            validate_str(ap_zone_name, param_spec, "ap_zone_name", errormsg)
        else:
            errormsg.append("ap_zone_name: AP Zone Name is missing in playbook.")

        rf_profile_name = ap_zones.get("rf_profile_name")
        if rf_profile_name:
            param_spec = dict(type="str", length_max=30)
            validate_str(rf_profile_name, param_spec, "rf_profile_name", errormsg)
        else:
            errormsg.append("rf_profile_name: RF Profile name is missing in playbook.")

        device_tags = ap_zones.get("device_tags")
        if device_tags:
            for device_tag in device_tags:
                param_spec = dict(type="str", length_max=30)
                validate_str(device_tag, param_spec, "device_tag", errormsg)

        ssids = ap_zones.get("ssids")
        if ssids:
            if len(ssids) > 16:
                errormsg.append("ssids: AP Zone SSIDs list is more than 16 in playbook.")
                return

            for ap_ssid in ssids:
                param_spec = dict(type="str", length_max=32)
                validate_str(ap_ssid, param_spec, "ap_ssid", errormsg)
                ssid_exists = any(ap_ssid in zone.values() for zone in ssid_list)
                if not ssid_exists:
                    zone_msg = "ssids: AP Zone SSID: {0} : {1} not exist in ssid_details.".format(
                        ap_ssid, ssid_exists)
                    errormsg.append(zone_msg)

    def get_want(self, config):
        """
        Retrieve wireless network profile or delete profile from playbook configuration.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing network profile details.

        Returns:
            self: The current instance of the class with updated 'want' attributes.

        Description:
            This function parses the playbook configuration to extract information
            related to network profile. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """
        want = {}

        self.log("Validating input data before proceeding...", "DEBUG")
        self.input_data_validation(config).check_return_status()
        self.log("Input data validation successful. Extracting wireless profile details.", "DEBUG")

        want["wireless_profile"] = config
        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")

        return self

    def get_have(self, config):
        """
        Get required details for the given profile config from Cisco Catalyst Center

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict) - Playbook details containing network profile

        Returns:
            self - The current object with ssid info, template validate site id
            information collection for profile update.
        """

        self.have["wireless_profile"], self.have["wireless_profile_list"] = {}, []
        offset = 1
        limit = int(self.payload.get("offset_limit"))

        while True:
            profiles = self.get_network_profile("Wireless", offset, limit)
            if not profiles:
                self.log("No data received from API (Offset={0}). Exiting pagination.".
                         format(offset), "DEBUG")
                break

            self.log("Received {0} profile(s) from API (Offset={1}).".format(
                len(profiles), offset), "DEBUG")
            self.have["wireless_profile_list"].extend(profiles)

            if len(profiles) < limit:
                self.log("Received less than limit ({0}) results, assuming last page. Exiting pagination.".
                         format(limit), "DEBUG")
                break

            offset += limit  # Increment offset for pagination
            self.log("Incrementing offset to {0} for next API request.".format(offset),
                     "DEBUG")

        if self.have["wireless_profile_list"]:
            self.log("Total {0} profile(s) retrieved for 'Wireless': {1}.".format(
                len(self.have["wireless_profile_list"]),
                self.pprint(self.have["wireless_profile_list"])), "DEBUG")
        else:
            self.log("No existing wireless profile(s) found.", "WARNING")

        profile_info = {}
        profile_name = config.get("profile_name")
        if profile_name:
            self.log("Checking if profile '{0}' exists in retrieved profiles.".
                     format(profile_name), "DEBUG")

            if self.value_exists(self.have["wireless_profile_list"], "name", profile_name):
                profile_info["profile_info"] = self.get_wireless_profile(profile_name)
                self.log("Fetched wireless profile details for '{0}': {1}".format(
                    profile_name, profile_info["profile_info"]), "DEBUG")

        if self.payload.get("state") == "deleted":
            self.have["wireless_profile"] = profile_info

        self.log("Validating site template existence for config: {0}".format(config), "DEBUG")
        self.check_site_template(config, profile_info)

        ssid_details = config.get("ssid_details")
        ssid_for_apzone = []
        if ssid_details:
            ssid_response = []

            for each_ssid in ssid_details:
                if each_ssid:
                    each_ssid_response = {}
                    self.log("Check Site ID exist in for global for SSID", "INFO")
                    site_exist, site_id = self.get_site_id("global")

                    if site_exist:
                        self.log("Collect SSID details for global: {0}".format(site_id), "INFO")
                        global_ssid_list = self.get_ssid_details(site_id, "global")

                        self.log("Check given ssid exist for: {0}".format(
                            each_ssid.get("ssid")), "INFO")
                        ssid_exist, ssid_info = \
                            self.check_ssid_details(each_ssid.get("ssid"), global_ssid_list)

                        each_ssid_response["ssid_exist"] = ssid_exist
                        each_ssid_response["ssid_response"] = ssid_info
                        each_ssid["wlan_profile_name"] = ssid_info["wlan_profile_name"]
                        each_ssid["policy_profile_name"] = ssid_info["policy_profile_name"]

                    ssid_response.append(each_ssid_response)
                    ssid_for_apzone.append(each_ssid["ssid"])

            if ssid_response:
                profile_info["ssid_response"] = ssid_response

        ap_zones = config.get("ap_zones")
        if ap_zones:
            self.log("Fetching AP zone information.", "DEBUG")
            self.get_ap_zone_info(ap_zones, ssid_for_apzone, profile_info)

        additional_interfaces = config.get("additional_interfaces")
        if additional_interfaces:
            self.log("Fetching additional interface information.", "DEBUG")
            self.get_additional_interface_info(additional_interfaces, profile_info)

        onboarding_templates = config.get("onboarding_templates")
        day_n_templates = config.get("day_n_templates")
        profile_id = profile_info.get("profile_info", {}).get("instanceUuid")
        if (onboarding_templates or day_n_templates) and profile_id:
            self.log("Getting templates for the profile: {0}: {1}".format(
                profile_name, self.pprint(profile_info.get("profile_info"))),
                "INFO")
            profile_info["profile_id"] = profile_id
            template_detail = self.get_templates_for_profile(profile_id)
            if template_detail:
                profile_info["previous_templates"] = template_detail

        self.log("Collected Required data, now compare Configuration Data", "INFO")
        if profile_info.get("profile_info"):
            profile_stat, unmatched = self.compare_config_data(config, profile_info)
            profile_info["profile_compare_stat"] = profile_stat
            profile_info["profile_compare_unmatched"] = unmatched

        have_profile_name = profile_info.get("profile_info", {}).get("name")
        # Check if there are no additional configurations and profile names match
        if have_profile_name == profile_name and not any(
            config.get(key) for key in [
                "ssid_details", "ap_zones", "site_names",
                "additional_interfaces", "onboarding_templates", "day_n_templates"]):
            self.log("No additional configurations found. Profile names match.", "DEBUG")
            profile_info["profile_compare_stat"] = True
            profile_info["profile_compare_unmatched"] = None

        self.have["wireless_profile"] = profile_info

        if not self.have["wireless_profile"]:
            self.msg = "No wireless profile data found for given configuration: {0}".format(
                config)
            self.log(self.msg, "DEBUG")

        self.log("Current State (have): {0}".format(self.pprint(self.have)), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        return self

    def get_ap_zone_info(self, ap_zones, ssid_for_apzone, profile_info):
        """
        This function extending the get have function to get details for AP Zone details

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            ap_zones (list): A List of dict containing AP Zone name, rf profile and SSIDs.
            ssid_for_apzone (list): A List contains SSID list given on SSID section in playbook
            profile_info (dict): A dict contain AP zone informations

        Returns:
            No return, Contains the information of AP zone and to parse ot the profile_info
        """
        try:
            if not ap_zones:
                self.log("No AP Zones provided in the configuration.", "DEBUG")
                return

            self.log("Starting AP Zone comparison.", "INFO")
            apzone_response = []
            for each_ap_zone in ap_zones:
                if each_ap_zone.get("ssids"):
                    each_apzone_response = []
                    for sub_ap_zone in each_ap_zone.get("ssids"):
                        if sub_ap_zone in ssid_for_apzone:
                            each_apzone_response.append(sub_ap_zone)
                    if len(each_apzone_response) == len(each_ap_zone.get("ssids")):
                        apzone_response.append(each_ap_zone.get("ssids"))
            if len(apzone_response) == len(ap_zones):
                profile_info["apzone_change_required"] = False
            else:
                profile_info["apzone_change_required"] = True
        except Exception as e:
            msg = 'An error occurred during compare AP Zone: {0}'.format(str(e))
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def get_additional_interface_info(self, additional_interfaces, profile_info):
        """
        This function extending the get have function to get details for
        additional interface information

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            additional_interfaces (list): A List of dict containing interface names and Vlan ids.
            profile_info (dict): A dict contain additional interface information with status

        Returns:
            No return, Contains the information about the Additional interface details to add to
            profile_info
        """
        self.log("Get the Additional interface details for: {0}".
                 format(additional_interfaces), "DEBUG")
        try:
            if not additional_interfaces:
                self.log("No additional interfaces provided in the configuration.", "DEBUG")
                return

            self.log("Fetching additional interface details: {0}".format(
                additional_interfaces), "INFO")
            all_interfaces = []

            for each_interface in additional_interfaces:
                interface = each_interface.get("interface_name")
                vlan_id = each_interface.get("vlan_id")

                if not interface or not vlan_id:
                    self.log("Skipping invalid interface entry: {0}".format(
                        each_interface), "WARNING")
                    continue

                self.log("Checking additional interface: {0} (VLAN {1})".format(
                    interface, vlan_id), "DEBUG")
                check_response = self.additional_interface_check_or_create(interface, vlan_id)
                all_interfaces.append({
                    "interface_name": interface,
                    "vlan_id": vlan_id,
                    "exist": bool(check_response)
                })

            profile_info["additional_interfaces"] = all_interfaces
            self.log("Collected additional interface details: {0}".format(all_interfaces), "INFO")

        except Exception as e:
            msg = "An error occurred during get Additional interface: {0}".format(str(e))
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def additional_interface_check_or_create(self, interface, vlan_id):
        """
        This function used to check the interface and vlan exist if not exist
        then need to be created.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            interface (str): A string containing interface name.
            vlan_id (int): A integer contains Vlan ID from 1 to 4094

        Returns:
            matched (bool): Update True or False if additional interface match with input.
        """
        self.log("Check the interface name: {0} vlan: {1}".
                 format(interface, vlan_id), "INFO")
        payload = {
            "limit": 500,
            "offset": 1,
            "interface_name": interface,
            "vlan_id": vlan_id
        }
        try:
            interfaces = self.execute_get_request("wireless", "get_interfaces_v1", payload)
            if interfaces and isinstance(interfaces.get("response"), list):
                self.log("Interface {0} with VLAN {1} already exists.".format(
                    interface, vlan_id), "DEBUG")
                return True

            self.log("Interface {0} with VLAN {1} not found. Creating...".format(
                interface, vlan_id), "INFO")

            self.log("Creating new Interface and Vlan : {0} Vlan: {1}".format(
                interface, vlan_id), "INFO")
            payload = {
                "interfaceName": interface,
                "vlanId": vlan_id
            }
            task_details = self.execute_process_task_data("wireless", "create_interface_v1",
                                                          payload)
            if task_details:
                self.log("Successfully created interface {0} with VLAN {1}.".format(
                    interface, vlan_id), "INFO")
                return True

            self.log("Failed to create interface {0} with VLAN {1}.".format(
                interface, vlan_id), "ERROR")
            self.fail_and_exit("Unable to create interface: {0}".format(payload))

        except Exception as e:
            msg = 'An error occurred during Additional interface Check: {0}'.format(str(e))
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def compare_config_data(self, input_config, have_info):
        """
        This function used to compare the playbook input with the have data and
        return the status and unmatch value

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            input_config (dict): A dict containing playbook config of wireless profile.
            have_prof_info (dict): A string contain the profile response from have function

        Returns:
            matched (bool): Update True or False if input match with the have data
            dict or None: A dict contain unmatched kay value pair
        """
        self.log("Compare the input config: {0} with have: {1}".
                 format(self.pprint(input_config), self.pprint(have_info)), "INFO")
        unmatched_keys = []
        have_prof_info = have_info.get("profile_info")
        ssid_list = input_config.get("ssid_details", [])
        have_ssid_details = have_prof_info.get("ssidDetails", [])
        site_list = input_config.get("site_names", [])
        have_site_list = have_prof_info.get("sites", [])
        onboarding_templates_list = input_config.get("onboarding_templates", [])
        have_ob_templates = have_info.get("onboarding_templates", [])
        day_n_templates_list = input_config.get("day_n_templates", [])
        have_dn_templates = have_info.get("day_n_templates", [])

        if ssid_list:
            if not have_ssid_details:
                self.log("No SSID details found in the existing profile.", "DEBUG")
                unmatched_keys.append(ssid_list)
            else:
                for each_ssid in ssid_list:
                    for have_ssid in have_ssid_details:
                        if each_ssid.get("ssid") == have_ssid.get("name"):
                            ssid_match, unmatched_values = self.compare_each_config_with_have(
                                each_ssid, have_ssid, "ssid_details"
                            )
                            if not ssid_match:
                                unmatched_keys.append(unmatched_values)

        if site_list:
            have_sites = [each_site.lower() for each_site in have_site_list]
            want_sites = [site_name.lower() for site_name in site_list]
            self.log("Have Sites: {0}, Want Sites: {1}".format(have_sites, want_sites), "DEBUG")
            for given_site in want_sites:
                if given_site not in have_sites:
                    self.log("Given site name: {0} does not exist in the retrieved site list: {1}".
                             format(given_site, self.pprint(have_sites)), "INFO")
                    unmatched_keys.append(given_site)

        if onboarding_templates_list:
            for each_template in onboarding_templates_list:
                self.log("Checking onboarding template: {0}".format(each_template), "DEBUG")
                if not self.value_exists(have_ob_templates, "template_name", each_template):
                    self.log("Template '{0}' not found in existing onboarding templates.".
                             format(each_template), "INFO")
                    unmatched_keys.append(each_template)

        if day_n_templates_list:
            self.log("Checking Day-N template: {0}".format(each_template), "DEBUG")
            for each_template in day_n_templates_list:
                if not self.value_exists(have_dn_templates, "template_name", each_template):
                    self.log("Template '{0}' not found in existing Day-N templates.".
                             format(each_template), "INFO")
                    unmatched_keys.append(each_template)

        if unmatched_keys:
            self.log("Unmatched templates: {0}".format(", ".join(unmatched_keys)), "WARN")
            return False, unmatched_keys

        return True, None

    def get_wireless_profile(self, profile_name):
        """
        Get wireless profile from the given playbook data and response with
        wireless profile information with ssid details.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_name (str): A string containing input data to get wireless profile
                                for given profile name.

        Returns:
            dict or None: Dict contains wireless profile information, otherwise None.

        Description:
            This function used to get the wireless profile from the input config.
        """

        self.log("Get wireless profile for : {0}".format(profile_name), "INFO")
        try:
            response = self.dnac._exec(
                family="wireless",
                function="get_wireless_profile",
                params={"profile_name": profile_name}
            )
            self.log("Response from get_wireless_profile API: {0}".
                     format(self.pprint(response)), "DEBUG")
            if not response:
                self.log("No wireless profile found for: {0}".format(profile_name), "INFO")
                return None
            self.log("Received the wireless profile response: {0}".
                     format(self.pprint(response)), "INFO")
            return response[0].get("profileDetails")

        except Exception as e:
            msg = 'An error occurred during get wireless profile: {0}'.format(str(e))
            self.log(msg, "ERROR")
            self.set_operation_result("failed", False, msg, "ERROR")
            return None

    def get_ssid_details(self, site_id, site_name):
        """
        Get SSID details from the given playbook data and response with SSID information.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_id (str) : Site ID contain string of UUID for the global site
            site_name (str): A str containing Site name to collect the SSID information.

        Returns:
            global_ssids (list): Contains list of dict SSID details for the SSID validation

        Description:
            This function used to get the list of SSID informations for the given site.
        """

        self.log("Fetching SSID information for site {0}: {1}".format(site_name, site_id), "INFO")
        offset_limit = int(self.payload.get("offset_limit"))
        payload = {
            "site_id": site_id,
            "limit": offset_limit,
            "offset": 1
        }
        global_ssids = []
        try:
            while True:
                response = self.dnac._exec(
                    family="wireless",
                    function="get_ssid_by_site",
                    params=payload
                )
                self.log("Response from get_enterprise_ssid API: {0}".
                         format(self.pprint(response)), "DEBUG")

                if not response or not isinstance(response, dict):
                    self.log("Unexpected or empty response received from API, " +
                             "expected a non-empty dictionary.", "ERROR")
                    break

                self.log("Received the SSID details response: {0}".format(
                    self.pprint(response.get("response"))), "INFO")
                ssid_list = response.get("response")

                if not ssid_list:
                    self.log("No SSID data found at offset {0}. Exiting pagination.".format(
                        payload["offset"]), "DEBUG")
                    break

                self.log("Retrieved {0} SSID detail(s) from API (Offset={1}).".format(
                    len(ssid_list), payload["offset"]), "DEBUG")
                global_ssids.extend(ssid_list)

                if len(ssid_list) < offset_limit:
                    self.log("Fetched fewer than the limit ({0}), assuming last page. Exiting.".
                             format(offset_limit), "DEBUG")
                    break

                payload["offset"] += offset_limit
                self.log("Incrementing offset to {0} for next API request.".format(
                    payload["offset"]), "DEBUG")

            if not global_ssids:
                msg = "No SSID details avalable for Global to validate input playbook SSIDs"
                self.log(msg, "ERROR")
                self.fail_and_exit(msg)

            self.log("Total {0} SSID detail(s) retrieved for the site: '{1}'.".
                     format(len(global_ssids), site_name), "DEBUG")
            return global_ssids

        except Exception as e:
            msg = 'An error occurred during get wireless profile: {0}'.format(str(e))
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def check_ssid_details(self, ssid_name, ssid_list):
        """
        Check the SSID Name is available in the SSID list collected based on the site id.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            ssid_name (str): A str containing input data of SSID name.
            ssid_list (list): A list of dict contains SSID name and other details.

        Returns:
            bool: Update True or False if SSID exist
            dict: A string contains SSID information.

        Description:
            This function used to get the SSID information from the input config.
        """
        self.log("Checking if SSID '{0}' exists in the provided SSID list.".format(
            ssid_name), "INFO")

        try:
            ssid_details = {}
            global_ssids = []

            for each_ssid in ssid_list:
                global_ssids.append(each_ssid["ssid"])
                if ssid_name == each_ssid.get("ssid"):
                    ssid_details["ssid"] = ssid_name
                    ssid_details["wlan_profile_name"] = each_ssid.get("profileName")
                    ssid_details["policy_profile_name"] = each_ssid.get("policyProfileName")
                    msg = "Verified SSID: {0} exist in Global SSID list.".format(ssid_name)
                    self.log(msg, "INFO")
                    return True, ssid_details

            if not ssid_details:
                msg = "Given SSID: {0} not in the Global SSID list: {1}.".format(
                    ssid_name, global_ssids)
                self.log(msg, "ERROR")
                self.fail_and_exit(msg)

        except Exception as e:
            msg = 'An error occurred during ssid checking: {0}'.format(str(e))
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def parse_input_data_for_payload(self, wireless_data, payload_data):
        """
        Parse input playbook data to payload for the profile creation and updation.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            wireless_data (dict): A dictionary containing input config data from playbook.
            payload_data (dict): A dictionary contain parsed data for the payload.

        Returns:
            No return, parse the input data and load the parsed data to the payload_data
        """
        exclude_keys = ["site_names", "feature_templates", "onboarding_templates",
                        "day_n_templates", "provision_group"]
        try:
            for key, value in wireless_data.items():
                if value is None or key in exclude_keys:
                    continue

                mapped_key = self.keymap.get(key, key)
                if key not in exclude_keys:
                    if key == "ssid_details" and isinstance(value, list):
                        payload_data["ssidDetails"] = []
                        ssid_details = wireless_data[key]
                        if ssid_details:
                            for each_ssid in ssid_details:
                                ssid_data = {}
                                for ssid_key, ssid_value in each_ssid.items():
                                    mapped_ssidkey = self.keymap.get(ssid_key, ssid_key)
                                    if ssid_key not in ("policy_profile_name"):
                                        if ssid_key == "local_to_vlan" and ssid_value:
                                            ssid_data["flexConnect"] = dict(enableFlexConnect=True,
                                                                            localToVlan=ssid_value)
                                        ssid_data[mapped_ssidkey] = ssid_value
                                if ssid_data.get("enableFabric"):
                                    remove_keys = ["aflexConnect", "localToVlan"
                                                   "interfaceName", "anchorGroupName",
                                                   "vlanGroupName"]
                                    for rm_key in remove_keys:
                                        ssid_data.pop(rm_key, None)
                                ssid_data.pop("localToVlan", None)
                                payload_data["ssidDetails"].append(ssid_data)

                    elif key == "ap_zones" and isinstance(value, list):
                        payload_data["apZones"] = []
                        ap_zones = wireless_data[key]
                        if ap_zones:
                            for ap_zone in ap_zones:
                                ap_zone_data = {}
                                for zone_key, zone_value in ap_zone.items():
                                    mapped_zonekey = self.keymap.get(zone_key, zone_key)
                                    if zone_key not in ["device_tags"]:
                                        if ssid_key == "ssids" and zone_value:
                                            ap_zone_data["ssids"] = zone_value
                                        ap_zone_data[mapped_zonekey] = zone_value
                                payload_data["apZones"].append(ap_zone_data)

                    elif key == "additional_interfaces" and isinstance(value, list):
                        payload_data["additionalInterfaces"] = []
                        addi_interfaces = wireless_data[key]
                        if addi_interfaces:
                            for interface in addi_interfaces:
                                if interface.get("interface_name") is not None:
                                    payload_data["additionalInterfaces"].append(
                                        interface.get("interface_name"))
                    else:
                        payload_data[mapped_key] = value

        except Exception as e:
            msg = 'An error occurred during Parsing for payload: {0}'.format(str(e))
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def create_update_wireless_profile(self, wireless_data, profile_id=None):
        """
        Create/Update the wireless profile for the given config with site and SSID details.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            wireless_data (dict): A dictionary containing input config data from playbook.
            profile_id (str, optional): ID of the wireless profile to update.

        Returns:
            dict: A dictionary of execution task details.

        Description:
            This function create/update the wireless profile with the site the and SSID details.
        """
        payload_data = {}
        self.log("Parse the input playbook to payload for: {0}".format(wireless_data), "INFO")
        self.parse_input_data_for_payload(wireless_data, payload_data)

        profile_name = payload_data.get("wirelessProfileName")
        profile = self.have.get("wireless_profile", {})

        profile_exist = self.value_exists(profile, "name", profile_name)
        function_name = "create_wireless_profile_connectivity_v1"
        profile_payload = payload_data  # Default case for creation

        if profile_exist:
            function_name = "update_wireless_profile_connectivity_v1"
            profile = self.have.get("wireless_profile")
            if profile and isinstance(profile, dict):
                if profile.get("profile_info", {}).get("name") == \
                   payload_data.get("wirelessProfileName"):
                    profile_id = profile.get("profile_info", {}).get("instanceUuid")
                    profile_payload = {"id": profile_id, "payload": payload_data}
                    self.log("Updating wireless profile with parameters: {0}".format(
                        self.pprint(payload_data)), "INFO")
        elif profile_id:
            function_name = "update_wireless_profile_connectivity_v1"
            profile_payload = {"id": profile_id, "payload": payload_data}
            self.log("Updating wireless profile for template with parameters: {0}".format(
                self.pprint(payload_data)), "INFO")
        else:
            self.log("Creating wireless profile with parameters: {0}".format(
                self.pprint(payload_data)), "INFO")

        return self.execute_process_task_data("wireless", function_name, profile_payload)

    def compare_each_config_with_have(self, input_data, have_data, type_of):
        """
        Compare input configuration data with existing ("have") data and return
        a boolean indicating whether they match, along with any unmatched data.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            input_data (dict): A dict containing playbook config of ssid info and ap zone data.
            have_data (dict): A dict contain the data exist with specific ssid retrived data
            type_of (str): A string contain the ssid details or ap_zone for check data

        Returns:
            tuple: (matched (bool), unmatched_data (dict or None))

        Description:
            This function used to compare the data same have and input config data.
        """
        if type_of != "ssid_details":
            self.log("Unsupported type for comparison: {0}".format(type_of), "ERROR")
            return False, None

        self.log("Comparing Have SSID: {0}, Want SSID: {1}".format(
            self.pprint(have_data), self.pprint(input_data)), "DEBUG")

        un_match_data = {}
        for ssid_key in input_data.keys():
            if ssid_key == "ssid":
                if input_data[ssid_key] != have_data.get("name"):
                    un_match_data[ssid_key] = input_data[ssid_key]
                    self.log("Found Un matched SSID {0}".format(
                        self.pprint(un_match_data[ssid_key])), "DEBUG")
            elif ssid_key in ["wlan_profile_name", "interface_name", "enable_fabric",
                              "anchor_group_name", "dot11be_profile_name",
                              "policy_profile_name"]:
                if input_data[ssid_key] != have_data.get(self.keymap[ssid_key]):
                    un_match_data[ssid_key] = input_data[ssid_key]
            elif ssid_key == "local_to_vlan":
                if str(input_data[ssid_key]) != have_data.get(
                   "flexConnect", {}).get(self.keymap[ssid_key]):
                    un_match_data[ssid_key] = input_data[ssid_key]

        if not un_match_data:
            return True, None

        self.log("Found the unmatched data {0}".format(self.pprint(
            un_match_data)), "INFO")
        return False, un_match_data

    def process_templates(self, templates, previous_templates, profile_name, profile_id):
        """
        Check and assign the list of template from the input config.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            templates (list): A list containing template name from input config.
            previous_templates (list): A list containing existing template name and id
                                       assigned to the profile.
            profile_name (str): A string containing profile name used to assign template to profile.
            profile_id (str): A string containing profile id used to assign the onboarding or
                              day n template.

        Returns:
            list: A list contains templates assigned to the profile status.
        """
        self.log("Processing {0} templates for profile: {1}".format(len(templates),
                                                                    profile_name), "DEBUG")
        template_response = []

        for each_template in templates:
            template_name = each_template.get("name")
            self.log("Checking template: {0}".format(template_name), "DEBUG")

            if not each_template.get("template_exist"):
                self.log("Template '{0}' does not exist, skipping.".format(template_name), "DEBUG")
                continue  # Skip the rest of the loop if template doesn't exist

            template_id = each_template.get("template_id")
            self.log("Template '{0}' exists, attaching network profile.".format(
                template_name), "DEBUG")

            # If no previous templates, we can directly attach
            if not previous_templates:
                self.log("No previous templates to check, attaching '{0}'.".format(
                    template_name), "DEBUG")
                template_response.append(self.attach_networkprofile_cli_template(
                    profile_name, profile_id, template_name, template_id))
                continue  # Continue to the next template

            # If template already exists in previous templates, skip it
            if self.value_exists(previous_templates, "name", template_name):
                self.log("Template '{0}' already exists in previous templates, skipping.".
                         format(template_name), "DEBUG")
                continue  # Skip the rest of the loop if template already exists in previous_templates

            # Otherwise, attach the template
            self.log("Template '{0}' not found in previous templates, attaching.".format(
                template_name), "DEBUG")
            template_response.append(self.attach_networkprofile_cli_template(
                profile_name, profile_id, template_name, template_id))

        self.log("Finished processing templates. Total attached: {0}".format(
            len(template_response)), "DEBUG")
        return template_response

    def get_diff_merged(self, config):
        """
        Create or update the wireless profile in Cisco Catalyst Center based on the playbook

        Parameters:
            config (dict) - Playbook details containing wireless profile information.

        Returns:
            self - The current object with create or update message with task response.
        """
        self.changed = False
        profile_id = None

        unmatch_stat = self.have["wireless_profile"].get("profile_compare_stat")
        for profile in self.have["wireless_profile_list"]:
            if profile.get("name") == config.get("profile_name") and unmatch_stat:
                profile_id = profile.get("id")
                self.msg = "No changes required, profile(s) are already exist"
                self.log(self.msg, "INFO")
                self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
                return self

        if not unmatch_stat:
            self.log("Creating wireless profile for the config: {0}".format(config), "INFO")
            task_details = self.create_update_wireless_profile(config)

            profile_response = {"profile_name": config["profile_name"], "status": "Failed"}

            if task_details:
                profile_response["status"] = task_details["progress"]
                self.log("Task response for the profile creation: {0}".format(
                    profile_response), "INFO")
                uuid_pattern = \
                    r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
                match = re.search(uuid_pattern, task_details["progress"])
                if match:
                    profile_id = match.group()
                    self.log("Profile created: {0} and found the profile id: {1}".
                             format(config["profile_name"], profile_id), "INFO")

            have_site = self.have["wireless_profile"].get("site_response")
            site_id_list = []
            site_name_list = []
            if have_site and isinstance(have_site, list):
                for each_site in have_site:
                    if each_site["site_exist"]:
                        site_id_list.append(each_site["site_id"])
                        site_name_list.append(each_site["site_names"])

            if site_id_list:
                assign_response = []
                site_index = 0
                for site in site_id_list:
                    assign_response.append(self.assign_site_to_network_profile(
                        profile_id, site, config.get("profile_name"),
                        site_name_list[site_index]))
                    site_index += 1
        else:
            self.not_processed.append(config)
            self.msg = "Unable to create wireless profile: '{0}'.".format(
                str(self.not_processed))
            self.status = "failed"

        ob_template = self.have["wireless_profile"].get("onboarding_templates")
        dn_template = self.have["wireless_profile"].get("day_n_templates")
        previous_templates = self.have["wireless_profile"].get("previous_templates")
        profile_name = config.get("profile_name")

        if ob_template and profile_id:
            template_response = self.process_templates(ob_template, previous_templates,
                                                       profile_name, profile_id)
            self.log("Template Response (ob_template): {0}".format(template_response), "DEBUG")

        if dn_template and profile_id:
            template_response = self.process_templates(dn_template, previous_templates,
                                                       profile_name, profile_id)
            self.log("Template Response (dn_template): {0}".format(template_response), "DEBUG")

        if config.get("ssid_details") and config.get("ap_zones") and\
           config.get("additional_interfaces"):
            self.create_update_wireless_profile(config, profile_id)

        self.created.append(profile_response)
        self.msg = "Wireless Profile created/updated successfully for '{0}'.".format(
            str(self.created))
        self.changed = True
        self.log(self.msg, "INFO")
        self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                                  self.created).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Verify the merged status(Creation/Updation) of wireless profile in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by
            retrieving the current state (have) and desired state (want) of the configuration,
            logs the states, and validates whether the specified profiles exists in the Catalyst
            Center.
        """
        success_profile = []
        self.changed = False
        self.get_have(config)
        self.log("Current profile Config (have): {0}".format(self.pprint(self.have)), "INFO")
        self.log("Desired profile Config (want): {0}".format(self.pprint(self.want)), "INFO")

        unmatch_stat = self.have["wireless_profile"].get("profile_compare_stat")
        if not unmatch_stat:
            msg = "Profile verification failed, Unable to create/update profile: {0}".format(config)
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

        msg = "Profile created/updated are verified successfully for '{0}'.".format(config)
        self.log(msg, "INFO")
        self.set_operation_result(self.status, self.changed, msg, "INFO",
                                  self.created).check_return_status()

        return self

    def get_diff_deleted(self, each_profile):
        """
        Delete Network profile based on the given profile ID
        Network configurations in Cisco Catalyst Center based on the playbook details

        Parameters:
            each_profile (dict): The profile details to be deleted from Cisco Catalyst Center.

        Returns:
            self - The current object with deleted status and return response with task details.
        """
        if not self.value_exists(self.have["wireless_profile_list"], "name",
                                 each_profile["profile_name"]):
            self.msg = "No changes required, profile(s) are already deleted"
            self.log(self.msg, "INFO")
            self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
            return self

        each_have = self.have.get("wireless_profile")
        have_profile_name = each_have.get("profile_info")
        if not have_profile_name:
            self.msg = "No changes required, profile(s) not exist or already deleted"
            self.log(self.msg, "INFO")
            self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
        else:
            have_profile_name = each_have.get("profile_info", {}).get("name")

        if have_profile_name != each_profile.get("profile_name"):
            self.msg = "Profile name not matching : {0}".format(each_profile.get("profile_name"))
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        have_profile_id = each_have.get("profile_info", {}).get("instanceUuid")
        sites = each_have.get("profile_info", {}).get("sites")
        if sites:
            unassign_site = []
            for each_site in sites:
                site_exist, site_id = self.get_site_id(each_site)
                unassign_response = self.unassign_site_to_network_profile(
                    each_profile["profile_name"], have_profile_id, each_site, site_id)
                unassign_site.append(unassign_response)

            if len(unassign_site) == len(sites):
                self.log("Sites unassigned successfully {0}".format(
                    sites), "INFO")

        task_details = None
        if have_profile_id:
            task_details = self.delete_network_profiles(
                each_profile.get("profile_name"), have_profile_id)

        if not task_details:
            self.not_processed.append(each_profile)
            self.msg = "Unable to delete profile: '{0}'.".format(
                str(self.not_processed))
            self.log(self.msg, "INFO")
            self.fail_and_exit(self.msg)

        profile_response = dict(profile_name=each_profile["profile_name"],
                                status=task_details["progress"])
        self.deleted.append(profile_response)
        self.msg = "Wireless Profile deleted successfully for '{0}'.".format(
            str(self.deleted))

        self.log(self.msg, "INFO")
        self.set_operation_result("success", True, self.msg, "INFO",
                                  each_profile).check_return_status()
        return self

    def verify_diff_deleted(self, config):
        """
        Verify the deletion status of wireless network profile in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.

        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.

        Description:
            This method checks the deletion status of a configuration in Cisco Catalyst Center.
            It validates whether the specified profile exists in the Cisco Catalyst Center.
        """
        self.get_have(config)
        self.log("Current profile state (have): {0}".format(
            self.pprint(self.have.get("wireless_profile", {}))), "INFO")

        each_profile = self.have.get("wireless_profile")
        profile_info = each_profile.get("profile_info")
        if profile_info:
            msg = "Unable to delete below wireless profile '{0}'.".format(
                profile_info.get("name"))
            self.log(msg, "INFO")
            self.set_operation_result("failed", False, msg, "INFO",
                                      profile_info.get("name")).check_return_status()

        msg = "Wireless profile deleted and verified successfully"
        self.log(msg, "INFO")
        self.set_operation_result("success", True, msg, "INFO", msg).check_return_status()

        return self

    def final_response_message(self, state):
        """
        To show the final message with Wireless profile response

        Parameters:
            configs (list of dict) - Playbook config contains Wireless profile
            playbook information.

        Returns:
            self - Return response as verified created/updated/deleted
            Wireless profile messages
        """
        if state == "merged":
            if self.created:
                self.msg = "Wireless profile(s) created and verified successfully: {0}".format(
                    self.created)
                if self.not_processed:
                    self.msg += " Unable to create the following profiles: {0}".format(
                        self.not_processed)
                self.log(self.msg, "INFO")
                self.set_operation_result("success", True, self.msg, "INFO",
                                          self.created).check_return_status()
            elif not self.created and not self.not_processed:
                self.msg = "No changes required, profile(s) already exist."
                self.log(self.msg, "INFO")
                self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
            else:
                self.msg = "Unable to create the following profiles: {0}".format(
                    self.not_processed)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR",
                                          self.not_processed).check_return_status()

        elif state == "deleted":
            if self.deleted:
                self.msg = "Wireless profile(s) deleted and verified successfully: {0}".format(
                    self.deleted)
                if self.not_processed:
                    self.msg += " Unable to delete the following profiles: {0}".format(
                        self.not_processed)
                self.log(self.msg, "INFO")
                self.set_operation_result("success", True, self.msg, "INFO",
                                          self.deleted).check_return_status()
            elif self.not_processed:
                self.msg = "Unable to delete the following profiles: {0}".format(
                    self.not_processed)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR",
                                          self.not_processed).check_return_status()
            else:
                self.msg = "Wireless profile(s) already deleted for: {0}".format(self.config)
                self.log(self.msg, "INFO")
                self.set_operation_result("success", False, self.msg, "INFO").check_return_status()

        return self


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": "443"},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": True},
        "dnac_version": {"type": 'str', "default": "2.2.3.3"},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": "WARNING"},
        "dnac_log_file_path": {"type": 'str', "default": "dnac.log"},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": False},
        "dnac_api_task_timeout": {"type": 'int', "default": 1200},
        "dnac_task_poll_interval": {"type": 'int', "default": 2},
        "offset_limit": {"type": 'int', "default": 500},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ["merged", "deleted"]},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_wireless_profile = NetworkWirelessProfile(module)
    state = ccc_wireless_profile.params.get("state")

    if ccc_wireless_profile.compare_dnac_versions(
       ccc_wireless_profile.get_ccc_version(), "2.3.7.9") < 0:
        ccc_wireless_profile.status = "failed"
        ccc_wireless_profile.msg = (
            "The specified version '{0}' does not support the network profile workflow feature."
            "Supported version(s) start from '2.3.7.9' onwards.".
            format(ccc_wireless_profile.get_ccc_version())
        )
        ccc_wireless_profile.log(ccc_wireless_profile.msg, "ERROR")
        ccc_wireless_profile.check_return_status()

    if state not in ccc_wireless_profile.supported_states:
        ccc_wireless_profile.status = "invalid"
        ccc_wireless_profile.msg = "State {0} is invalid".format(state)
        ccc_wireless_profile.check_return_status()

    ccc_wireless_profile.validate_input().check_return_status()
    config_verify = ccc_wireless_profile.params.get("config_verify")

    for config in ccc_wireless_profile.validated_config:
        if not config:
            ccc_wireless_profile.msg = "Playbook configuration is missing."
            ccc_wireless_profile.log(ccc_wireless_profile.msg, "ERROR")
            ccc_wireless_profile.fail_and_exit(ccc_wireless_profile.msg)

        ccc_wireless_profile.reset_values()
        ccc_wireless_profile.get_want(config).check_return_status()
        ccc_wireless_profile.get_have(config).check_return_status()
        ccc_wireless_profile.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_wireless_profile.verify_diff_state_apply[state](config).check_return_status()

    ccc_wireless_profile.final_response_message(state).check_return_status()
    module.exit_json(**ccc_wireless_profile.result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Network Profile Wireless Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: brownfield_network_profile_wireless_playbook_generator
short_description: Generate YAML configurations playbook for 'network_profile_wireless_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the 'network_profile_wireless_workflow_manager'
    module, reducing the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
version_added: 6.45.0
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
      - A list of filters for generating YAML playbook compatible with the
        'brownfield_network_profile_wireless_playbook_generator' module.
      - Filters specify which components to include in the YAML configuration file.
      - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all wireless profile and all supported features.
          - This mode discovers all managed devices in Cisco Catalyst Center and extracts all supported configurations.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete brownfield infrastructure discovery and documentation.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "network_profile_wireless_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
        - For example, "network_profile_wireless_workflow_manager_playbook_2025-11-12_21-43-26.yml".
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML configuration file.
          - These filters apply to all components unless overridden by component-specific filters.
          - At least one filter type must be specified to identify target devices.
        type: dict
        required: false
        suboptions:
          profile_name_list:
            description:
              - List of wireless profile names to extract configurations from.
              - LOWEST PRIORITY - Only used if neither day_n_templates nor site_names are provided.
              - Wireless Profile names must match those registered in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Example ["Campus_Wireless_Profile", "Enterprise_Wireless_Profile"]
            type: list
            elements: str
            required: false
          day_n_template_list:
            description:
              - List of day_n_templates assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor site_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["evpn_l2vn_anycast_template", "Wireless_Controller_Config"]
            type: list
            elements: str
            required: false
          site_list:
            description:
              - List of sites assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor day_n_template_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["Global/India/Chennai/Main_Office", "Global/USA/San_Francisco/Regional_HQ"]
            type: list
            elements: str
            required: false
          ssid_list:
            description:
              - List of SSIDs assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor day_n_template_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["Guest_WiFi", "Corporate_WiFi"]
            type: list
            elements: str
            required: false
          ap_zone_list:
            description:
              - List of AP zones assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor day_n_template_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["Branch_AP_Zone", "HQ_AP_Zone"]
            type: list
            elements: str
            required: false
          feature_template_list:
            description:
              - List of feature templates assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor day_n_template_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["Default AAA_Radius_Attributes_Configuration", "Default CleanAir 6GHz Design"]
            type: list
            elements: str
            required: false
          additional_interface_list:
            description:
              - List of additional interfaces assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor day_n_template_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["VLAN_22", "GigabitEthernet0/2"]
            type: list
            elements: str
            required: false
requirements:
  - dnacentersdk >= 2.10.10
  - python >= 3.9
notes:
  - This module utilizes the following SDK methods
    site_design.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1
    site_design.retrieves_the_list_of_network_profiles_for_sites_v1
    configuration_templates.gets_the_templates_available_v1
    network_settings.retrieve_cli_templates_attached_to_a_network_profile_v1
    wireless.get_wireless_profile
    wireless.get_interfaces
  - The following API paths are used
    GET /dna/intent/api/v1/networkProfilesForSites
    GET /dna/intent/api/v1/template-programmer/template
    GET /dna/intent/api/v1/networkProfilesForSites/{profileId}/templates
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Switch Profiles
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - generate_all_configurations: true

- name: Auto-generate YAML Configuration with custom file path
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - file_path: "/tmp/complete_wireless_profile_config.yml"
        generate_all_configurations: true

- name: Generate YAML Configuration with default file path for given wireless profiles
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - global_filters:
          profile_name_list: ["Campus_Wireless_Profile", "Enterprise_Wireless_Profile"]

- name: Generate YAML Configuration with default file path based on Day-N templates filters
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - global_filters:
          day_n_template_list: ["Periodic_Config_Audit", "Security_Compliance_Check"]

- name: Generate YAML Configuration with default file path based on site list filters
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - global_filters:
          site_list: ["Global/India/Chennai/Main_Office", "Global/USA/San_Francisco/Regional_HQ"]

- name: Generate YAML Configuration with default file path based on ssid list filters
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - global_filters:
          ssid_list: ["SSID1", "SSID2"]

- name: Generate YAML Configuration with default file path based on ap zone list filters
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - global_filters:
          ap_zone_list: ["AP_Zone1", "AP_Zone2"]

- name: Generate YAML Configuration with default file path based on feature template list filters
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - global_filters:
          feature_template_list: ["Default AAA_Radius_Attributes_Configuration", "Default CleanAir 6GHz Design"]

- name: Generate YAML Configuration with default file path based on additional interface list filters
  cisco.dnac.brownfield_network_profile_wireless_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - global_filters:
          additional_interface_list: ["VLAN_22", "GigabitEthernet0/2"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "YAML config generation Task succeeded for module 'network_profile_wireless_workflow_manager'.": {
            "file_path": "tmp/brownfield_network_profile_wireless_workflow_playbook_templatebase.yml"}
        },
      "msg": {
        "YAML config generation Task succeeded for module 'network_profile_wireless_workflow_manager'.": {
            "file_path": "tmp/brownfield_network_profile_wireless_workflow_playbook_templatebase.yml"}
        }
    }

# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": "No configurations or components to process for module 'network_profile_wireless_workflow_manager'.
                  Verify input filters or configuration.",
      "msg": "No configurations or components to process for module 'network_profile_wireless_workflow_manager'.
             Verify input filters or configuration."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    validate_list_of_dicts,
)
from ansible_collections.cisco.dnac.plugins.module_utils.network_profiles import (
    NetworkProfileFunctions,
)
import time
from collections import OrderedDict

try:
    import yaml
    HAS_YAML = True

    # Only define OrderedDumper if yaml is available
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
except ImportError:
    HAS_YAML = False
    yaml = None
    OrderedDumper = None


class NetworkProfileWirelessPlaybookGenerator(NetworkProfileFunctions, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center
    using the GET APIs.
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        """
        Initialize an instance of the class.

        Parameters:
            module: The module associated with the class instance.

        Returns:
            The method does not return a value.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_name = "network_profile_wireless_workflow_manager"
        self.module_schema = self.get_workflow_elements_schema()
        self.log("Initialized NetworkProfileWirelessPlaybookGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False

    def validate_input(self):
        """
        Validates the input configuration parameters for the playbook.

        Returns:
            object: An instance of the class with updated attributes:
                self.msg: A message describing the validation result.
                self.status: The status of the validation (either "success" or "failed").
                self.validated_config: If successful, a validated version of the "config" parameter.
        """
        self.log("Starting validation of input configuration parameters.", "DEBUG")

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "global_filters": {"type": "dict", "elements": "dict", "required": False},
        }

        allowed_keys = set(temp_spec.keys())

        # Validate that only allowed keys are present in the configuration
        for config_item in self.config:
            if not isinstance(config_item, dict):
                self.msg = "Configuration item must be a dictionary, got: {0}".format(
                    type(config_item).__name__)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Check for invalid keys
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            if invalid_keys:
                self.msg = (
                    "Invalid parameters found in playbook configuration: {0}. "
                    "Only the following parameters are allowed: {1}. "
                    "Please remove the invalid parameters and try again.".format(
                        list(invalid_keys), list(allowed_keys)
                    )
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

        self.validate_minimum_requirements(self.config)
        self.log("Validating configuration parameters against the expected schema: {0}".format(
            temp_spec), "DEBUG")

        # # Import validate_list_of_dicts function here to avoid circular imports
        # from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = f"Successfully validated playbook configuration parameters using 'validated_input': {valid_temp}"
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_elements_schema(self):
        """
        Returns the mapping configuration for network wireless profile workflow manager.

        Returns:
            dict: A dictionary containing network elements and global filters configuration with validation rules.
        """
        return {
            "global_filters": {
                "profile_name_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "day_n_template_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "site_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "ssid_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "ap_zone_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "feature_template_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "additional_interface_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            }
        }

    def collect_all_wireless_profile_list(self, profile_names=None):
        """
        Get required details for the given profile config from Cisco Catalyst Center

        Parameters:
            profile_names (list) - List of network wireless profile names

        Returns:
            self - The current object with Filtered or all profile list
        """
        self.log(
            f"Collecting template and wireless profile related information for: {profile_names}",
            "INFO",
        )
        self.have["wireless_profile_names"], self.have["wireless_profile_list"] = [], []
        self.have["wireless_profile_info"] = {}
        offset = 1
        limit = 500

        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
        while resync_retry_count > 0:
            profiles = self.get_network_profile("Wireless", offset, limit)
            if not profiles:
                self.log(
                    "No data received from API (Offset={0}). Exiting pagination.".format(
                        offset
                    ),
                    "DEBUG",
                )
                break

            self.log(
                "Received {0} profile(s) from API (Offset={1}).".format(
                    len(profiles), offset
                ),
                "DEBUG",
            )
            self.have["wireless_profile_list"].extend(profiles)

            if len(profiles) < limit:
                self.log(
                    "Received less than limit ({0}) results, assuming last page. Exiting pagination.".format(
                        limit
                    ),
                    "DEBUG",
                )
                break

            offset += limit  # Increment offset for pagination
            self.log(
                "Incrementing offset to {0} for next API request.".format(offset),
                "DEBUG",
            )

            self.log(
                "Pauses execution for {0} seconds.".format(resync_retry_interval),
                "INFO",
            )
            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval

        if self.have["wireless_profile_list"]:
            self.log(
                "Total {0} profile(s) retrieved for 'wireless': {1}.".format(
                    len(self.have["wireless_profile_list"]),
                    self.pprint(self.have["wireless_profile_list"]),
                ),
                "DEBUG",
            )

            # Filter profiles based on provided profile names
            if profile_names:
                filtered_profiles = []
                non_existing_profiles = []
                for profile in profile_names:
                    if self.value_exists(self.have["wireless_profile_list"], "name", profile):
                        self.log(f"Found existing wireless profile: {profile}", "DEBUG")
                        profile_id = self.get_value_by_key(self.have["wireless_profile_list"],
                                                           "name", profile, "id")
                        filtered_profiles.append(profile)
                        profile_info = self.get_wireless_profile(profile)
                        self.log(
                            "Fetched wireless profile details for '{0}': {1}".format(
                                profile, profile_info
                            ),
                            "DEBUG",
                        )
                        self.have.setdefault("wireless_profile_info", {})[
                            profile_id] = profile_info
                    else:
                        non_existing_profiles.append(profile)
                        self.log(f"Wireless profile not found: {profile}", "WARNING")

                if non_existing_profiles:
                    self.log(
                        f"The following wireless profile(s) do not exist in Cisco Catalyst Center: {non_existing_profiles}.",
                        "ERROR",
                    )
                    not_exist_profile = ", ".join(non_existing_profiles)
                    self.fail_and_exit(f"Wireless profile(s) '{not_exist_profile}' does not exist in Cisco Catalyst Center.")

                if filtered_profiles:
                    self.log(
                        f"Filtered existing wireless profile(s): {filtered_profiles}.",
                        "DEBUG",
                    )
                    self.have["wireless_profile_names"] = filtered_profiles
            else:
                for profile in self.have["wireless_profile_list"]:
                    profile_id = profile.get("id")
                    profile_name = profile.get("name")
                    self.have["wireless_profile_names"].append(profile_name)
                    profile_info = self.get_wireless_profile(profile_name)
                    self.log(
                        "Fetched wireless profile details for '{0}': {1}".format(
                            profile_name, self.pprint(profile_info)
                        ),
                        "DEBUG",
                    )
                    self.have.setdefault("wireless_profile_info", {})[
                        profile_id] = profile_info
                self.log(
                    "No specific profile names provided. Using all retrieved wireless profiles: {0}, {1}".format(
                        self.have["wireless_profile_names"], self.have["wireless_profile_info"]
                    ),
                    "DEBUG",
                )
        else:
            self.log("No existing wireless profile(s) found.", "WARNING")

        return self

    def collect_site_and_template_details(self, profile_names):
        """
        Get template details based on the profile names from Cisco Catalyst Center

        Parameters:
            profile_names (list) - List of network wireless profile names

        Returns:
            self - The current object with templates and site details
            information collection for profile create and update.
        """
        self.log(f"Collecting template name based on the wireless profile: {profile_names}", "INFO")

        for each_profile in profile_names:
            profile_id = self.get_value_by_key(
                self.have["wireless_profile_list"],
                "name",
                each_profile,
                "id",
            )
            if not profile_id:
                self.log(
                    f"Profile ID not found for wireless profile: {each_profile}. Skipping template retrieval.",
                    "WARNING",
                )
                continue

            templates = self.get_templates_for_profile(profile_id)
            if templates:
                template_names = [
                    template.get("name") for template in templates
                ]
                self.have.setdefault("wireless_profile_templates", {})[
                    profile_id
                ] = template_names
                self.log(
                    f"Retrieved templates for wireless profile '{each_profile}': {template_names}",
                    "DEBUG",
                )
            else:
                self.log(
                    f"No templates found for wireless profile: {each_profile}.",
                    "WARNING",
                )

            site_list = self.get_site_lists_for_profile(
                each_profile, profile_id)
            if site_list:
                self.log(
                    "Received Site List: {0} for config: {1}.".format(
                        site_list, each_profile
                    ),
                    "INFO",
                )
                site_id_list = [site.get("id") for site in site_list]
                site_id_name_mapping = self.get_site_id_name_mapping(site_id_list)
                self.log(f"Site ID to Name Mapping: {self.pprint(site_id_name_mapping)} for profile: {each_profile}",
                         "DEBUG")
                self.have.setdefault("wireless_profile_sites", {})[
                    profile_id
                ] = site_id_name_mapping
                log_msg = f"Retrieved site list for wireless profile '{each_profile}': {site_id_name_mapping}"
                self.log(log_msg, "DEBUG")
            else:
                self.log(
                    f"No sites found for wireless profile: {each_profile}.",
                    "WARNING",
                )

        return self

    def process_global_filters(self, global_filters):
        """
        Process global filters for network wireless profile.

        Parameters:
            global_filters (dict): A dictionary containing global filter parameters.

        Returns:
            list: A list containing processed global filter parameters.
        """
        self.log("Processing global filters: {0}".format(global_filters), "DEBUG")
        profile_names = global_filters.get("profile_name_list")
        day_n_templates = global_filters.get("day_n_template_list")
        site_list = global_filters.get("site_list")
        ssid_list = global_filters.get("ssid_list")
        ap_zone_list = global_filters.get("ap_zone_list")
        feature_template_list = global_filters.get("feature_template_list")
        additional_interface_list = global_filters.get("additional_interface_list")
        final_list = []

        if profile_names and isinstance(profile_names, list):
            self.log(f"Filtering wireless profiles based on profile_name_list: {profile_names}",
                     "DEBUG")

            for profile in self.have["wireless_profile_names"]:
                if profile in profile_names:
                    profile_id = self.get_value_by_key(
                        self.have["wireless_profile_list"],
                        "name", profile, "id",
                    )
                    if profile_id:
                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        self.log(f"Processed configuration for profile ID '{profile_id}': {each_profile_config}",
                                 "DEBUG")

            self.log(f"Profile configurations are collected based on profile name list: {final_list}", "DEBUG")

        elif day_n_templates and isinstance(day_n_templates, list):
            self.log(f"Filtering wireless profiles based on day_n_template_list: {day_n_templates}",
                     "DEBUG")

            for profile_id, templates in self.have.get("wireless_profile_templates", {}).items():
                if any(template in templates for template in day_n_templates):
                    each_profile_config = self.process_profile_info(profile_id, final_list)
                    self.log(f"Processed configuration for profile ID '{profile_id}': {each_profile_config}",
                             "DEBUG")

            self.log(f"Profile configurations are collected based on day n template list: {final_list}", "DEBUG")

        elif site_list and isinstance(site_list, list):
            self.log(f"Filtering wireless profiles based on site_list: {site_list}",
                     "DEBUG")

            for profile_id, sites in self.have.get("wireless_profile_sites", {}).items():
                if any(site in sites.values() for site in site_list):
                    each_profile_config = self.process_profile_info(profile_id, final_list)
                    self.log(f"Processed configuration for profile ID '{profile_id}': {each_profile_config}",
                             "DEBUG")

            self.log(f"Profile configurations are collected based on site list: {final_list}", "DEBUG")

        elif ssid_list and isinstance(ssid_list, list):
            self.log(f"Filtering wireless profiles based on ssid_list: {ssid_list}",
                     "DEBUG")

            for profile_id, profile_info in self.have.get("wireless_profile_info", {}).items():
                ssid_details = profile_info.get("ssidDetails", "")
                if any(ssid.get("ssidName") in ssid_list for ssid in ssid_details):
                    each_profile_config = self.process_profile_info(profile_id, final_list)
                    self.log(f"Processed configuration for profile ID '{profile_id}': {each_profile_config}",
                             "DEBUG")

            self.log(f"Profile configurations are collected based on ssid list: {final_list}", "DEBUG")

        elif ap_zone_list and isinstance(ap_zone_list, list):
            self.log(f"Filtering wireless profiles based on ap_zone_list: {ap_zone_list}", "DEBUG")

            for profile_id, profile_info in self.have.get("wireless_profile_info", {}).items():
                ap_zones = profile_info.get("apZones", "")
                if any(ap_zone.get("apZoneName") in ap_zone_list for ap_zone in ap_zones):
                    each_profile_config = self.process_profile_info(profile_id, final_list)
                    self.log(f"Processed configuration for profile ID '{profile_id}': {each_profile_config}",
                             "DEBUG")

            self.log(f"Profile configurations are collected based on ap zone list: {final_list}", "DEBUG")

        elif feature_template_list and isinstance(feature_template_list, list):
            self.log(f"Filtering wireless profiles based on feature_template_list: {feature_template_list}",
                     "DEBUG")

            for profile_id, profile_info in self.have.get("wireless_profile_info", {}).items():
                feature_templates = profile_info.get("featureTemplates", "")
                if any(feature_template.get("designName") in feature_template_list
                       for feature_template in feature_templates):
                    each_profile_config = self.process_profile_info(profile_id, final_list)
                    self.log(f"Processed configuration for profile ID '{profile_id}': {each_profile_config}",
                             "DEBUG")

            self.log(f"Profile configurations are collected based on feature template list: {final_list}", "DEBUG")

        elif additional_interface_list and isinstance(additional_interface_list, list):
            self.log(f"Filtering wireless profiles based on additional_interface_list: {additional_interface_list}",
                     "DEBUG")

            for profile_id, profile_info in self.have.get("wireless_profile_info", {}).items():
                additional_interfaces = profile_info.get("additionalInterfaces", "")
                if any(interface in additional_interface_list
                       for interface in additional_interfaces):
                    each_profile_config = self.process_profile_info(profile_id, final_list)
                    self.log(f"Processed configuration for profile ID '{profile_id}': {each_profile_config}",
                             "DEBUG")

            self.log(f"Profile configurations are collected based on additional interface list: {final_list}", "DEBUG")
        else:
            self.log("No specific global filters provided, processing all profiles", "DEBUG")

        if not final_list:
            self.log("No profiles matched the provided global filters", "WARNING")
            return None

        return final_list

    def process_profile_info(self, profile_id, final_list):
        """
        Process core details of a wireless profile.

        Parameters:
            profile_id (str): The ID of the wireless profile.
            final_list (list): The list to append the processed profile configuration.

        Returns:
            dict: Updated configuration dictionary with core details.
        """
        self.log(f"Processing core details for profile ID: '{profile_id}'", "DEBUG")
        each_profile_config = {}

        profile_info = self.have.get("wireless_profile_info", {}).get(profile_id)
        if not profile_info:
            self.log(f"No profile information found for profile ID: '{profile_id}'. Skipping parsing details.",
                     "WARNING")
            return each_profile_config

        cli_template_details = self.have.get(
            "wireless_profile_templates", {}).get(profile_id)
        if cli_template_details and isinstance(cli_template_details, list):
            if len(cli_template_details) > 0:
                each_profile_config["day_n_templates"] = cli_template_details

        site_details = self.have.get(
            "wireless_profile_sites", {}).get(profile_id)
        if site_details and isinstance(site_details, dict):
            site_list = list(site_details.values())
            if site_list:
                each_profile_config["sites"] = site_list

        each_profile_config["profile_name"] = profile_info.get("wirelessProfileName")
        ssid_details = profile_info.get("ssidDetails", "")
        additional_interfaces = profile_info.get("additionalInterfaces", "")
        ap_zones = profile_info.get("apZones", "")
        feature_template_designs = profile_info.get("featureTemplates", "")

        parsed_ssids = self.parse_profile_info(ssid_details, "ssid_details")
        if parsed_ssids:
            each_profile_config["ssid_details"] = parsed_ssids

        parsed_interfaces = self.parse_profile_info(
            additional_interfaces, "additional_interfaces")
        if parsed_interfaces:
            each_profile_config["additional_interfaces"] = parsed_interfaces

        parsed_ap_zones = self.parse_profile_info(ap_zones, "ap_zones")
        if parsed_ap_zones:
            each_profile_config["ap_zone_list"] = parsed_ap_zones

        parsed_feature_templates = self.parse_profile_info(
            feature_template_designs, "feature_template_designs")
        if parsed_feature_templates:
            each_profile_config["feature_template_designs"] = parsed_feature_templates

        if each_profile_config:
            self.log("Processed configuration for profile '{0}': {1}".format(
                each_profile_config["profile_name"], self.pprint(each_profile_config)), "DEBUG")
            final_list.append(each_profile_config)

        return each_profile_config

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters, processes the data,
        and writes the YAML content to a specified file. It dynamically handles multiple network elements and their respective filters.

        Parameters:
            yaml_config_generator (dict): Contains file_path, global_filters, and component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """

        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log("Generate all wireless profile configurations from Catalyst Center", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("Initializing filter dictionaries", "DEBUG")
        # Set empty filters to retrieve everything
        global_filters = {}
        final_list = []
        if generate_all:
            self.log("Preparing to collect all configurations for wireless profile.",
                     "DEBUG")
            for each_profile_name in self.have.get("wireless_profile_names", []):
                each_profile_config = {}
                each_profile_config["profile_name"] = each_profile_name

                profile_id = self.get_value_by_key(
                    self.have["wireless_profile_list"],
                    "name",
                    each_profile_name,
                    "id",
                )
                if profile_id:
                    cli_template_details = self.have.get(
                        "wireless_profile_templates", {}).get(profile_id)
                    if cli_template_details and isinstance(cli_template_details, list):
                        each_profile_config["day_n_templates"] = cli_template_details
                        self.log("CLI template details added for profile '{0}': {1}".format(
                            each_profile_name, cli_template_details), "DEBUG")

                    site_details = self.have.get(
                        "wireless_profile_sites", {}).get(profile_id)
                    if site_details and isinstance(site_details, dict):
                        each_profile_config["sites"] = list(site_details.values())
                        self.log("Site details added for profile '{0}': {1}".format(
                            each_profile_name, each_profile_config["sites"]), "DEBUG")

                    profile_info = self.have.get("wireless_profile_info", {}).get(profile_id)
                    self.log("Processing profile information for profile '{0}': {1}".format(
                        each_profile_name, profile_info), "DEBUG")
                    if profile_info:
                        ssid_details = profile_info.get("ssidDetails", "")
                        additional_interfaces = profile_info.get("additionalInterfaces", "")
                        ap_zones = profile_info.get("apZones", "")
                        feature_template_designs = profile_info.get("featureTemplates", "")

                        parsed_ssids = self.parse_profile_info(ssid_details, "ssid_details")
                        if parsed_ssids:
                            each_profile_config["ssid_details"] = parsed_ssids

                        parsed_interfaces = self.parse_profile_info(
                            additional_interfaces, "additional_interfaces")
                        if parsed_interfaces:
                            each_profile_config["additional_interfaces"] = parsed_interfaces

                        parsed_ap_zones = self.parse_profile_info(ap_zones, "ap_zones")
                        if parsed_ap_zones:
                            each_profile_config["ap_zone_list"] = parsed_ap_zones

                        parsed_feature_templates = self.parse_profile_info(
                            feature_template_designs, "feature_template_designs")
                        if parsed_feature_templates:
                            each_profile_config["feature_template_designs"] = parsed_feature_templates

                    final_list.append(each_profile_config)
            self.log("All configurations collected for generate_all_configurations mode: {0}".format(
                final_list), "DEBUG")
        else:
            # we get ALL configurations
            self.log("Overriding any provided filters to retrieve based on global filters", "INFO")
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            if global_filters:
                final_list = self.process_global_filters(global_filters)

        if not final_list:
            self.msg = "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name
            )
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        final_dict = {"config": final_list}
        self.log("Final dictionary created: {0}".format(final_dict), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def parse_profile_info(self, profile_info, profile_key):
        """
        Parses the profile information to extract relevant details.

        Parameters:
            profile_info (dict): The profile information retrieved from the system.
            profile_key (str): The key identifying the specific profile.

        Returns:
            dict: A dictionary containing parsed config for the profile.
        """
        self.log("Parsing profile information for profile: {0}".format(profile_key), "DEBUG")

        if not (profile_info or profile_key):
            self.log(f"No profile information available to parse for profile: {profile_key}",
                     "WARNING")
            return None

        if profile_key == "ssid_details" and isinstance(profile_info, list):
            self.log("Parsing SSID details for profile: {0}".format(profile_key), "DEBUG")
            parsed_ssid = []
            for ssid in profile_info:
                each_parsed_ssid = {}
                ssid_name = ssid.get("ssidName")
                if ssid_name:
                    each_parsed_ssid["ssid_name"] = ssid_name
                else:
                    self.log("SSID name not found in SSID details: {0}".format(ssid), "WARNING")
                    continue  # Skip this SSID if name is not found

                dot11be_profile_id = ssid.get("dot11beProfileId")
                if dot11be_profile_id:
                    dot11be_profile_name = self.get_dot11be_profile_by_id(dot11be_profile_id)
                    if dot11be_profile_name:
                        each_parsed_ssid["dot11be_profile_name"] = dot11be_profile_name

                enable_fabric = ssid.get("enableFabric")
                each_parsed_ssid["enable_fabric"] = True if enable_fabric else False

                vlan_group_name = ssid.get("vlanGroupName")
                if vlan_group_name:
                    each_parsed_ssid["vlan_group_name"] = vlan_group_name

                interface_name = ssid.get("interfaceName")
                if interface_name:
                    each_parsed_ssid["interface_name"] = interface_name

                anchor_group_name = ssid.get("anchorGroupName")
                if anchor_group_name:
                    each_parsed_ssid["anchor_group_name"] = anchor_group_name

                flex_connect = ssid.get("flexConnect", {}).get("enableFlexConnect")
                local_to_vlan = ssid.get("flexConnect", {}).get("localToVlan")
                if flex_connect:
                    each_parsed_ssid["local_to_vlan"] = local_to_vlan

                self.log("Parsed SSID details: {0}".format(each_parsed_ssid), "DEBUG")
                parsed_ssid.append(each_parsed_ssid)

            self.log("Completed parsing all SSID details: {0}".format(parsed_ssid), "DEBUG")
            return parsed_ssid

        elif profile_key == "ap_zones" and isinstance(profile_info, list):
            self.log("Parsing AP zone details for profile: {0}".format(profile_key), "DEBUG")
            parsed_ap_zones = []
            for ap_zone in profile_info:
                each_ap_zone = {}
                ap_zone_name = ap_zone.get("apZoneName")
                if ap_zone_name:
                    each_ap_zone["ap_zone_name"] = ap_zone_name
                else:
                    self.log("Zone name not found in AP zone details: {0}".format(ap_zone), "WARNING")
                    continue  # Skip this AP zone if name is not found

                ssids = ap_zone.get("ssids", [])
                if ssids and isinstance(ssids, list):
                    each_ap_zone["ssids"] = ssids

                rf_profile_name = ap_zone.get("rfProfileName")
                if rf_profile_name:
                    each_ap_zone["rf_profile_name"] = rf_profile_name

                self.log("Parsed AP zone details: {0}".format(each_ap_zone), "DEBUG")
                parsed_ap_zones.append(each_ap_zone)

            self.log("Completed parsing all AP zone details: {0}".format(parsed_ap_zones), "DEBUG")
            return parsed_ap_zones

        elif profile_key == "feature_template_designs" and isinstance(profile_info, list):
            self.log("Parsing Feature Template details for profile: {0}".format(profile_key), "DEBUG")
            parsed_feature_template = []
            for feature_template in profile_info:
                each_feature_template = {}
                feature_templates = feature_template.get("designName")
                if feature_templates:
                    each_feature_template["feature_templates"] = [feature_templates]
                else:
                    self.log(f"Template name not found in Feature Template details: {feature_template}",
                             "WARNING")
                    continue  # Skip this Feature Template if name is not found

                ssids = feature_template.get("ssids")
                if ssids and isinstance(ssids, list):
                    each_feature_template["ssids"] = ssids

                parsed_feature_template.append(each_feature_template)
                self.log("Parsed Feature Template details: {0}".format(each_feature_template), "DEBUG")

            self.log("Completed parsing all Feature Template details: {0}".format(parsed_feature_template), "DEBUG")
            return parsed_feature_template

        elif profile_key == "additional_interfaces" and isinstance(profile_info, list):
            self.log("Parsing Additional Interface details for profile: {0}".format(profile_key), "DEBUG")
            parsed_interfaces = []
            for interface in profile_info:
                each_interface = {}
                vlan_id = self.get_additional_interface(interface)
                if vlan_id:
                    each_interface["interface_name"] = interface
                    each_interface["vlan_id"] = vlan_id
                else:
                    self.log("Interface name not found in Additional Interface details: {0}".format(interface), "WARNING")
                    continue  # Skip this interface if name is not found

                parsed_interfaces.append(each_interface)
                self.log("Parsed Additional Interface details: {0}".format(each_interface), "DEBUG")

            self.log(f"Completed parsing all Additional Interface details: {parsed_interfaces}", "DEBUG")
            return parsed_interfaces

        else:
            self.log(f"Unknown profile key '{profile_key}' or invalid profile information format.", "WARNING")
            return None

    def get_dot11be_profile_by_id(self, dot11be_profile_id):
        """
        Retrieve the dot11be profile details based on the dot11be profile id from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            dot11be_profile_id (str): A string containing dot11be profile ID.

        Returns:
            str or None: Profile name string if found, else None.
        """
        self.log(
            f"Retrieving dot11be profile ID for profile: {dot11be_profile_id}",
            "DEBUG",
        )

        param = {"id": dot11be_profile_id}
        func_name = "get80211be_profile_by_id"

        try:
            response = self.execute_get_request("wireless", func_name, param)
            self.log(
                "Response from get dot11be profile API: {0}".format(
                    self.pprint(response)
                ),
                "DEBUG",
            )

            if not response or "response" not in response or not response["response"]:
                self.log(
                    "No valid response received for profile: {0}, response type: {1}".format(
                        dot11be_profile_id, type(response).__name__
                    ),
                    "ERROR",
                )
                return None

            dot11be_profile_name = response.get("response").get("profileName")
            if dot11be_profile_name:
                self.log(
                    "Successfully retrieved dot11be profile name: {0}".format(dot11be_profile_name),
                    "DEBUG",
                )
            else:
                self.log(
                    "Profile name not found in API response for profile: {0}".format(
                        dot11be_profile_id
                    ),
                    "ERROR",
                )
            return dot11be_profile_name

        except Exception as e:
            msg = "Exception occurred while retrieving dot11be profile name for '{0}': ".format(
                dot11be_profile_id
            )
            self.log(msg + str(e), "ERROR")
            self.set_operation_result("failed", False, msg, "INFO")
            return None

    def get_additional_interface(self, interface):
        """
        This function used to get the additional interface details from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            interface (str): A string containing interface name.

        Returns:
            vlan_id: Retrun the VLAN ID for the interface name.
        """
        self.log(
            f"Check the interface name: '{interface}' vlan: {1}", "INFO"
        )
        payload = {
            "limit": 500,
            "offset": 1,
            "interface_name": interface
        }
        try:
            interfaces = self.execute_get_request(
                "wireless", "get_interfaces", payload
            )
            if interfaces and isinstance(interfaces.get("response"), list):
                vlan_id = interfaces["response"][0].get("vlanId")
                self.log(
                    f"Interface '{interface}' with VLAN '{vlan_id}' exists.",
                    "DEBUG",
                )
                return vlan_id

            self.log(
                f"Interface details for '{interface}' not found ",
                "INFO",
            )
        except Exception as e:
            msg = "An error occurred during Additional interface Check: {0}".format(
                str(e)
            )
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        This method prepares the parameters required for retrieving and managing
        wireless profile configurations such as Day n template, SSID, AP zone
        and sites list in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.

        Parameters:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('gathered').

        Returns:
            self: The current instance of the class with updated 'want' attributes.
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator added to want: {0}".format(
                self.pprint(want["yaml_config_generator"])
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Network Profile wireless operations."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Retrieves the current state of network wireless profile from the Cisco Catalyst Center.
        This method fetches the existing configurations for wireless profiles
        such as Day n template and sites list

        Parameters:
            config (dict): The configuration data for the network elements.

        Returns:
            object: An instance of the class with updated attributes:
                self.have: A dictionary containing the current state of network wireless profiles.
                self.msg: A message describing the retrieval result.
                self.status: The status of the retrieval (either "success" or "failed").
        """
        self.log(
            "Retrieving current state of network wireless profiles from Cisco Catalyst Center.",
            "INFO",
        )

        if config and isinstance(config, dict):
            if config.get("generate_all_configurations", False):
                self.log("Collecting all wireless profile details", "INFO")
                self.collect_all_wireless_profile_list()
                if not self.have.get("wireless_profile_names"):
                    self.msg = "No existing wireless profiles found in Cisco Catalyst Center."
                    self.status = "success"
                    return self

                self.collect_site_and_template_details(self.have.get("wireless_profile_names", []))
            global_filters = config.get("global_filters")
            if global_filters:
                profile_name_list = global_filters.get("profile_name_list", [])
                day_n_template_list = global_filters.get("day_n_template_list", [])
                site_list = global_filters.get("site_list", [])
                ssid_list = global_filters.get("ssid_list", [])
                ap_zone_list = global_filters.get("ap_zone_list", [])
                feature_template_list = global_filters.get("feature_template_list", [])
                additional_interface_list = global_filters.get("additional_interface_list", [])

                if profile_name_list and isinstance(profile_name_list, list):
                    self.log(f"Collecting given wireless profile details for {profile_name_list}", "INFO")
                    self.collect_all_wireless_profile_list(profile_name_list)
                    self.collect_site_and_template_details(self.have.get("wireless_profile_names", []))

                if (
                    day_n_template_list and isinstance(day_n_template_list, list) or
                    site_list and isinstance(site_list, list) or
                    ssid_list and isinstance(ssid_list, list) or
                    ap_zone_list and isinstance(ap_zone_list, list) or
                    feature_template_list and isinstance(feature_template_list, list) or
                    additional_interface_list and isinstance(additional_interface_list, list)
                ):
                    self.log(f"Collecting profile details based on filters: {global_filters}", "INFO")
                    self.collect_all_wireless_profile_list()
                    self.collect_site_and_template_details(self.have.get("wireless_profile_names", []))

        self.log("Current State (have): {0}".format(self.pprint(self.have)), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        return self

    def get_diff_gathered(self):
        """
        Executes the merge operations for various network profile configurations in the Cisco Catalyst Center.
        This method processes additions and updates for SSIDs, interfaces, AP zones, CLI Templates,
        Site lists and profile names. It logs detailed information about each operation,
        updates the result status, and returns a consolidated result.
        """

        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
        operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]

        # Iterate over operations and process them
        self.log("Beginning iteration over defined operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                "Iteration {0}: Checking parameters for {1} operation with param_key '{2}'.".format(
                    index, operation_name, param_key
                ),
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Iteration {0}: Parameters found for {1}. Starting processing.".format(
                        index, operation_name
                    ),
                    "INFO",
                )
                operation_func(params).check_return_status()
            else:
                self.log(
                    "Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                        index, operation_name
                    ),
                    "WARNING",
                )

        end_time = time.time()
        self.log(
            "Completed 'get_diff_gathered' operation in {0:.2f} seconds.".format(
                end_time - start_time
            ),
            "DEBUG",
        )

        return self


def main():
    """main entry point for module execution"""
    # Define the specification for the module"s arguments
    element_spec = {
        "dnac_host": {"required": True, "type": "str"},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "dnac_log": {"type": "bool", "default": False},
        "validate_response_schema": {"type": "bool", "default": True},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_network_profile_wireless_playbook_generator = NetworkProfileWirelessPlaybookGenerator(module)
    if (
        ccc_network_profile_wireless_playbook_generator.compare_dnac_versions(
            ccc_network_profile_wireless_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_network_profile_wireless_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for NETWORK PROFILE WIRELESS Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_network_profile_wireless_playbook_generator.get_ccc_version()
            )
        )
        ccc_network_profile_wireless_playbook_generator.set_operation_result(
            "failed", False, ccc_network_profile_wireless_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_network_profile_wireless_playbook_generator.params.get("state")
    # Check if the state is valid
    if state not in ccc_network_profile_wireless_playbook_generator.supported_states:
        ccc_network_profile_wireless_playbook_generator.status = "invalid"
        ccc_network_profile_wireless_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_network_profile_wireless_playbook_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_network_profile_wireless_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_network_profile_wireless_playbook_generator.validated_config:
        ccc_network_profile_wireless_playbook_generator.reset_values()
        ccc_network_profile_wireless_playbook_generator.get_want(
            config, state).check_return_status()
        ccc_network_profile_wireless_playbook_generator.get_have(
            config).check_return_status()
        ccc_network_profile_wireless_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_network_profile_wireless_playbook_generator.result)


if __name__ == "__main__":
    main()

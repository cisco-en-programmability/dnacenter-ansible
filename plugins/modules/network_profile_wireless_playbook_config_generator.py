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
module: network_profile_wireless_playbook_config_generator
short_description: >-
  Generate YAML configurations playbook for
  'network_profile_wireless_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the
    'network_profile_wireless_workflow_manager' module, reducing
    the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
  - Supports complete network wireless profile by
    collecting all wireless profiles config from Cisco Catalyst Center.
  - Enables targeted extraction using filters (profile names,
    Day-N templates, site hierarchies, SSIDs, AP zones, feature
    templates, or additional interfaces).
  - Auto-generates timestamped YAML filenames when file path not
    specified.
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
      - A list of filters for generating YAML playbook compatible
        with the 'network_profile_wireless_playbook_config_generator'
        module.
      - Filters specify which components to include in the YAML
        configuration file.
      - Either 'generate_all_configurations' or 'global_filters'
        must be specified to identify target wireless profiles.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML
            configurations for all wireless profiles and all
            supported features.
          - This mode discovers all managed devices in Cisco
            Catalyst Center and extracts all supported
            configurations.
          - When enabled, the config parameter becomes optional
            and will use default values if not provided.
          - A default filename will be generated automatically
            if file_path is not specified.
          - This is useful for complete network wireless profile
            and documentation.
          - Any provided global_filters will be IGNORED in this
            mode.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current
            working directory with a default file name
            C(<module_name>playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
          - For example,
            'network_profile_wireless_playbook_config_2025-11-12_21-43-26.yml'.
          - Supports both absolute and relative file paths.
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML
            configuration file.
          - These filters apply to all components unless overridden
            by component-specific filters.
          - At least one filter type must be specified to identify
            target devices.
          - Filter priority (highest to lowest) is profile_name_list,
            day_n_template_list, site_list, ssid_list, ap_zone_list,
            feature_template_list, additional_interface_list.
          - Only the highest priority filter with valid data will
            be processed.
        type: dict
        required: false
        suboptions:
          profile_name_list:
            description:
              - List of wireless profile names to extract
                configurations from.
              - HIGHEST PRIORITY - Used first if provided with
                valid data.
              - Wireless Profile names must match those registered
                in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Example ["Campus_Wireless_Profile",
                "Enterprise_Wireless_Profile"]
              - Module will fail if any specified profile does not
                exist in Catalyst Center.
            type: list
            elements: str
            required: false
          day_n_template_list:
            description:
              - List of Day-N templates to filter wireless profiles.
              - MEDIUM-HIGH PRIORITY - Only used if profile_name_list
                is not provided.
              - Retrieves all wireless profiles containing any of
                the specified templates.
              - Case-sensitive and must be exact matches.
              - Example ["evpn_l2vn_anycast_template",
                "Wireless_Controller_Config"]
              - Requires retrieving all profiles first, then
                filtering based on template assignments.
            type: list
            elements: str
            required: false
          site_list:
            description:
              - List of site hierarchies to filter wireless profiles.
              - MEDIUM PRIORITY - Only used if neither
                profile_name_list nor day_n_template_list are
                provided.
              - Retrieves all wireless profiles assigned to any of
                the specified sites.
              - Case-sensitive and must be exact matches.
              - Example ["Global/India/Chennai/Main_Office",
                "Global/USA/San_Francisco/Regional_HQ"]
              - Requires retrieving all profiles first, then
                filtering based on site assignments.
            type: list
            elements: str
            required: false
          ssid_list:
            description:
              - List of SSIDs to filter wireless profiles.
              - MEDIUM-LOW PRIORITY - Only used if profile_name_list,
                day_n_template_list, and site_list are not provided.
              - Retrieves all wireless profiles containing any of
                the specified SSIDs.
              - Case-sensitive and must be exact matches.
              - Example ["Guest_WiFi", "Corporate_WiFi"]
            type: list
            elements: str
            required: false
          ap_zone_list:
            description:
              - List of AP zones to filter wireless profiles.
              - LOW PRIORITY - Only used if higher priority filters
                are not provided.
              - Retrieves all wireless profiles containing any of
                the specified AP zones.
              - Case-sensitive and must be exact matches.
              - Example ["Branch_AP_Zone", "HQ_AP_Zone"]
            type: list
            elements: str
            required: false
          feature_template_list:
            description:
              - List of feature templates to filter wireless profiles.
              - LOWER PRIORITY - Only used if higher priority filters
                are not provided.
              - Retrieves all wireless profiles containing any of
                the specified feature templates.
              - Case-sensitive and must be exact matches.
              - Example ["Default AAA_Radius_Attributes_Configuration",
                "Default CleanAir 6GHz Design"]
            type: list
            elements: str
            required: false
          additional_interface_list:
            description:
              - List of additional interfaces to filter wireless profiles.
              - LOWEST PRIORITY - Only used if all other filters
                are not provided.
              - Retrieves all wireless profiles containing any of
                the specified additional interfaces.
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
    GET /dna/intent/api/v1/wireless/profile
    GET /dna/intent/api/v1/interfaces
  - Minimum Cisco Catalyst Center version required is 2.3.7.9 for
    YAML playbook generation support.
  - Filter priority hierarchy ensures only one filter type is
    processed per execution.
  - Module creates YAML file compatible with
    'network_profile_wireless_workflow_manager' module for
    automation workflows.
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Wireless Profiles
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  cisco.dnac.network_profile_wireless_playbook_config_generator:
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
  description: >-
    A dictionary with the response returned by the Cisco Catalyst
    Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "YAML config generation Task succeeded for module
         'network_profile_wireless_workflow_manager'.": {
            "file_path":
             "tmp/network_profile_wireless_workflow_playbook_templatebase.yml"
          }
        },
      "msg": {
        "YAML config generation Task succeeded for module
         'network_profile_wireless_workflow_manager'.": {
            "file_path":
             "tmp/network_profile_wireless_workflow_playbook_templatebase.yml"
          }
        }
    }

# Case_2: Error Scenario
response_2:
  description: >-
    A string with the response returned by the Cisco Catalyst
    Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "No configurations or components to process for
                   module 'network_profile_wireless_workflow_manager'.
                   Verify input filters or configuration.",
      "msg": "No configurations or components to process for module
              'network_profile_wireless_workflow_manager'.
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
        This function performs comprehensive validation of input configuration parameters
        by checking parameter presence, validating against expected schema specification,
        verifying allowed keys to prevent invalid parameters, ensuring minimum requirements
        for wireless profile playbook generation, and setting validated configuration for
        downstream processing workflows.

        Returns:
            object: An instance of the class with updated attributes:
                self.msg: A message describing the validation result.
                self.status: The status of the validation (either "success" or "failed").
                self.validated_config: If successful, a validated version of the "config" parameter.
        """
        self.log(
            "Starting validation of playbook configuration parameters. Checking "
            "configuration availability, schema compliance, and minimum requirements "
            "for wireless profile playbook generation workflow.",
            "DEBUG"
        )

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "INFO")
            return self

        self.log(
            f"Configuration found with {len(self.config)} entries. "
            "Proceeding with schema validation "
            "against expected parameter specification.",
            "DEBUG"
        )

        # Define expected schema for configuration parameters
        temp_spec = {
            "generate_all_configurations": {
                "type": "bool",
                "required": False,
                "default": False
            },
            "file_path": {
                "type": "str",
                "required": False
            },
            "global_filters": {
                "type": "dict",
                "required": False
            },
        }

        allowed_keys = set(temp_spec.keys())
        self.log(
            "Checking for invalid keys in configuration. Allowed keys: {0}".format(
                list(allowed_keys)
            ),
            "DEBUG"
        )

        # Validate that only allowed keys are present in each configuration item
        self.log(
            "Starting per-item key validation to check for invalid/unknown parameters.",
            "DEBUG"
        )

        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                "Validating configuration item {0}/{1} for type and allowed keys.".format(
                    config_index, len(self.config)
                ),
                "DEBUG"
            )
            if not isinstance(config_item, dict):
                self.msg = (
                    "Configuration item at index {0} must be a dictionary, got: {1}. "
                    "Please check your playbook configuration format.".format(
                        config_index, type(config_item).__name__
                    )
                )
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Check for invalid keys
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            if invalid_keys:
                self.msg = (
                    "Invalid parameters found in playbook configuration at item {0}: {1}. "
                    "Only the following parameters are allowed: {2}. "
                    "Please remove the invalid parameters and try again.".format(
                        config_index, list(invalid_keys), list(allowed_keys)
                    )
                )
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                "Configuration item {0}/{1} passed key validation. All keys are valid.".format(
                    config_index, len(self.config)
                ),
                "DEBUG"
            )

        self.log(
            "Completed per-item key validation. All {0} configuration item(s) have valid "
            "parameter keys.".format(len(self.config)),
            "INFO"
        )

        # Validate minimum requirements (generate_all or global_filters)
        self.log(
            "Validating minimum requirements to ensure either generate_all_configurations "
            "or global_filters is provided.",
            "DEBUG"
        )

        try:
            self.validate_minimum_requirement_for_global_filters(self.config)
            self.log(
                "Minimum requirements validation passed. Configuration has either "
                "generate_all_configurations or valid global_filters.",
                "INFO"
            )
        except Exception as e:
            self.msg = (
                "Minimum requirements validation failed: {0}. Please ensure either "
                "generate_all_configurations is true or global_filters is provided with "
                "at least one filter list.".format(str(e))
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Perform schema-based validation using validate_list_of_dicts
        self.log(
            "Starting schema-based validation using validate_list_of_dicts(). Validating "
            "parameter types, defaults, and required fields against schema: {0}".format(temp_spec),
            "DEBUG"
        )

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        self.log(
            "Schema validation completed. Valid configurations: {0}, Invalid parameters: {1}".format(
                len(valid_temp) if valid_temp else 0,
                bool(invalid_params)
            ),
            "DEBUG"
        )

        if invalid_params:
            self.msg = (
                "Invalid parameters found during schema validation: {0}. Please check "
                "parameter types and values. Expected types: generate_all_configurations "
                "(bool), file_path (str), global_filters (dict).".format(invalid_params)
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Validate global_filters structure if provided
        self.log(
            "Validating global_filters structure for configuration items that include filters.",
            "DEBUG"
        )
        for config_index, config_item in enumerate(valid_temp, start=1):
            global_filters = config_item.get("global_filters")

            if global_filters is not None:
                if not isinstance(global_filters, dict):
                    self.msg = (
                        "global_filters at configuration item {0} must be a dictionary, "
                        "got: {1}. Please correct the configuration format.".format(
                            config_index, type(global_filters).__name__
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                allowed_filter_keys = {
                    "profile_name_list", "day_n_template_list", "site_list",
                    "ssid_list", "ap_zone_list", "feature_template_list",
                    "additional_interface_list"
                }
                filter_keys = set(global_filters.keys())
                invalid_filter_keys = filter_keys - allowed_filter_keys

                if invalid_filter_keys:
                    self.msg = (
                        "Invalid filter keys found in global_filters at item {0}: {1}. "
                        "Allowed filter keys are: {2}. Please remove invalid filters.".format(
                            config_index, list(invalid_filter_keys), list(allowed_filter_keys)
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                self.log(
                    "global_filters at item {0} passed structure validation. "
                    "Filter keys present: {1}".format(config_index, list(filter_keys)),
                    "DEBUG"
                )
            else:
                self.log(
                    "Configuration item {0} does not contain global_filters. Skipping "
                    "filter structure validation.".format(config_index),
                    "DEBUG"
                )

        # Set validated configuration and return success
        self.validated_config = valid_temp

        self.msg = (
            "Successfully validated {0} configuration item(s) for network profile wireless "
            "playbook generation. Validated configuration: {1}".format(
                len(valid_temp), str(valid_temp)
            )
        )

        self.log(
            "Input validation completed successfully. Total items validated: {0}, "
            "Items with generate_all: {1}, Items with global_filters: {2}".format(
                len(valid_temp),
                sum(1 for item in valid_temp if item.get("generate_all_configurations")),
                sum(1 for item in valid_temp if item.get("global_filters"))
            ),
            "INFO"
        )

        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_elements_schema(self):
        """
        Constructs workflow filter schema for network wireless profile elements.

        This function defines the complete schema specification for wireless profile
        workflow manager operations including filter specifications for profile names,
        Day-N templates, sites, SSIDs, AP zones, feature templates, and additional
        interfaces enabling consistent parameter validation and YAML generation
        throughout the module lifecycle.

        Args:
            None: Schema constructed from predefined specifications.

        Returns:
            dict: Dictionary containing global_filters schema configuration with:
                - profile_name_list: List of wireless profile names for filtering
                - day_n_template_list: List of Day-N template names for filtering
                - site_list: List of site hierarchical names for filtering
                - ssid_list: List of SSID names for filtering
                - ap_zone_list: List of AP zone names for filtering
                - feature_template_list: List of feature template names for filtering
                - additional_interface_list: List of interface names for filtering
        """
        self.log(
            "Constructing workflow filter schema for network wireless profile elements. "
            "Schema defines filter specifications for seven filter types (profile names, "
            "Day-N templates, sites, SSIDs, AP zones, feature templates, additional "
            "interfaces) enabling parameter validation and targeted wireless profile "
            "extraction from Catalyst Center.",
            "DEBUG"
        )

        schema = {
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

        return schema

    def collect_all_wireless_profile_list(self, profile_names=None):
        """
        Retrieves wireless profile configurations from Cisco Catalyst Center.

        This function fetches wireless profile details using paginated API calls with
        configurable offset and limit parameters, optionally filtering by profile names
        for targeted retrieval, populating class attributes with profile lists, profile
        information dictionaries, and profile name collections for downstream processing
        in YAML generation workflow.

        Args:
            profile_names (list, optional): List of wireless profile names for filtering.
                                        If provided, validates existence and retrieves
                                        only specified profiles with error handling for
                                        non-existent profiles. If None, retrieves all
                                        wireless profiles from Catalyst Center.

        Returns:
            object: Self instance with updated attributes:
                    - self.have["wireless_profile_names"]: List of profile name strings
                    - self.have["wireless_profile_list"]: List of profile dictionaries
                    from API response
                    - self.have["wireless_profile_info"]: Dictionary mapping profile IDs
                    to detailed profile information
                    - Exits with failure if specified profile_names not found in
                    Catalyst Center
        """
        self.log(
            f"Starting wireless profile retrieval workflow with profile name filter: {profile_names}. "
            "Workflow includes paginated API calls with offset/limit parameters, optional "
            "profile name validation, profile information fetching, and class attribute "
            "population for YAML generation.",
            "DEBUG"
        )

        self.have["wireless_profile_names"], self.have["wireless_profile_list"] = [], []
        self.have["wireless_profile_info"] = {}
        offset = 1
        limit = 500

        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
        self.log(
            "Starting paginated profile retrieval loop with "
            f"retry count: {resync_retry_count} seconds, "
            f"retry interval: {resync_retry_interval} seconds. "
            "Loop fetches profiles in batches until all "
            "pages retrieved or timeout reached.",
            "DEBUG"
        )

        while resync_retry_count > 0:
            self.log(
                f"Executing API call to retrieve wireless profiles with offset={offset}, "
                f"limit={limit}. API method: get_network_profile('Wireless', offset, limit). "
                "Fetching batch of profiles from Catalyst Center.",
                "DEBUG"
            )

            profiles = self.get_network_profile("Wireless", offset, limit)
            if not profiles:
                self.log(
                    f"No profile data received from API call with offset={offset}. Either no "
                    "more profiles available or API returned empty response. Exiting "
                    "pagination loop.",
                    "DEBUG"
                )
                break

            self.log(
                f"Received {len(profiles)} profile(s) from API call with offset={offset}. Extending "
                "wireless_profile_list with retrieved profiles for accumulation across "
                "pagination cycles.",
                "DEBUG"
            )

            self.have["wireless_profile_list"].extend(profiles)

            if len(profiles) < limit:
                self.log(
                    f"Received {len(profiles)} profile(s), which is less than limit ({limit}). This "
                    "indicates last page of results. Exiting pagination loop to prevent "
                    "unnecessary API calls.",
                    "DEBUG"
                )
                break

            self.log(
                f"Received full batch of {limit} profiles matching limit. More profiles may "
                f"exist. Incrementing offset from {offset} to {offset + limit} for next API request to "
                "retrieve subsequent page.",
                "DEBUG"
            )

            offset += limit  # Increment offset for pagination
            self.log(
                f"Pausing execution for {resync_retry_interval} seconds "
                "before next API call to respect rate "
                "limiting and prevent API throttling. "
                f"Decrementing retry count by {resync_retry_interval} "
                "seconds.",
                "DEBUG"
            )

            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval

        if self.have["wireless_profile_list"]:
            self.log(
                "Pagination completed. Total {0} wireless profile(s) retrieved from "
                "Catalyst Center. Profile list: {1}. Proceeding with profile name "
                "filtering or full profile processing.".format(
                    len(self.have["wireless_profile_list"]),
                    self.pprint(self.have["wireless_profile_list"])
                ),
                "DEBUG"
            )

            # Filter profiles based on provided profile names
            if profile_names:
                self.log(
                    f"Profile name filter provided with {len(profile_names)} "
                    f"profile(s): {profile_names}. Validating "
                    "each profile name exists in retrieved profile list and fetching "
                    "detailed information for matched profiles.",
                    "DEBUG"
                )

                filtered_profiles = []
                non_existing_profiles = []

                for profile_index, profile in enumerate(profile_names, start=1):
                    self.log(
                        f"Processing profile filter {profile_index}/{len(profile_names)}: '{profile}'."
                        " Checking existence in "
                        f"wireless_profile_list with {len(self.have['wireless_profile_list'])} total profiles using "
                        "value_exists() method.",
                        "DEBUG"
                    )

                    if self.value_exists(self.have["wireless_profile_list"], "name", profile):
                        self.log(
                            f"Profile {profile_index}/{len(profile_names)} '{profile}' "
                            "found in wireless_profile_list. "
                            "Extracting profile ID for detailed information retrieval.",
                            "DEBUG"
                        )

                        profile_id = self.get_value_by_key(self.have["wireless_profile_list"],
                                                           "name", profile, "id")
                        if profile_id:
                            self.log(
                                f"Profile ID '{profile_id}' extracted for profile '{profile}'. Adding to "
                                "filtered_profiles list and fetching detailed profile "
                                "information using get_wireless_profile() API.",
                                "DEBUG"
                            )

                            filtered_profiles.append(profile)

                            profile_info = self.get_wireless_profile(profile)

                            self.log(
                                f"Fetched detailed wireless profile information for '{profile}' "
                                f"(ID: {profile_id}): {profile_info}. Storing in wireless_profile_info "
                                "dictionary with profile_id as key.",
                                "DEBUG"
                            )

                            self.have.setdefault("wireless_profile_info", {})[
                                profile_id
                            ] = profile_info
                            self.log(
                                f"Profile {profile_index}/{len(profile_names)} '{profile}' "
                                "not found in wireless_profile_list with "
                                f"{len(self.have['wireless_profile_list'])} profiles. "
                                "Adding to non_existing_profiles list for batch "
                                "error reporting.",
                                "WARNING"
                            )
                        else:
                            self.log(
                                f"Profile ID not found for profile '{profile}' despite existence "
                                "check passing. This indicates data inconsistency. Adding "
                                "to non_existing_profiles for error reporting.",
                                "WARNING"
                            )
                            non_existing_profiles.append(profile)
                    else:
                        non_existing_profiles.append(profile)
                        self.log(f"Wireless profile not found: {profile}", "WARNING")

                if non_existing_profiles:
                    not_exist_profile = ", ".join(non_existing_profiles)
                    self.msg = (
                        f"Profile name validation failed. {len(non_existing_profiles)} profile(s) not found in "
                        f"Catalyst Center: {not_exist_profile}. Total profiles requested: {len(profile_names)}, "
                        f"Found: {len(filtered_profiles)}. Please verify the profile names and try again."
                    )
                    self.log(self.msg, "ERROR")

                if filtered_profiles:
                    self.log(
                        f"Profile name filtering completed successfully. {len(filtered_profiles)} profile(s) "
                        f"validated and matched: {filtered_profiles}. "
                        "Setting wireless_profile_names to "
                        "filtered list for downstream processing.",
                        "DEBUG"
                    )
                    self.have["wireless_profile_names"] = filtered_profiles
            else:
                self.log(
                    "No profile name filter provided. Processing all "
                    f"{len(self.have['wireless_profile_list'])} retrieved "
                    "wireless profiles. Iterating through wireless_profile_list to extract "
                    "IDs, names, and fetch detailed information for each profile.",
                    "DEBUG"
                )

                for profile_index, profile in enumerate(
                    self.have["wireless_profile_list"], start=1
                ):
                    profile_id = profile.get("id")
                    profile_name = profile.get("name")
                    self.log(
                        f"Processing profile {profile_index}/{len(self.have['wireless_profile_list'])}: "
                        f"'{profile_name}' (ID: {profile_id}). Adding to "
                        "wireless_profile_names list and fetching detailed profile "
                        "information.",
                        "DEBUG"
                    )
                    self.have["wireless_profile_names"].append(profile_name)
                    profile_info = self.get_wireless_profile(profile_name)
                    self.log(
                        f"Fetched detailed wireless profile information for '{profile_name}' "
                        f"(ID: {profile_id}): {self.pprint(profile_info)}. "
                        "Storing in wireless_profile_info dictionary.",
                        "DEBUG"
                    )
                    self.have.setdefault("wireless_profile_info", {})[
                        profile_id] = profile_info
                self.log(
                    "All profile processing completed without filters. Total profiles "
                    "processed: {0}. Wireless profile names: {1}. Profile information "
                    "dictionary contains {2} entries.".format(
                        len(self.have["wireless_profile_names"]),
                        self.have["wireless_profile_names"],
                        len(self.have["wireless_profile_info"])
                    ),
                    "DEBUG"
                )
        else:
            self.log(
                "No wireless profiles retrieved from Catalyst Center after pagination "
                "completed. wireless_profile_list is empty. This may indicate no profiles "
                "exist or API access issues.",
                "WARNING"
            )

        self.log(
            "Wireless profile collection workflow completed. Returning self instance with "
            "populated attributes: wireless_profile_names ({0} entries), "
            "wireless_profile_list ({1} entries), wireless_profile_info ({2} entries).".format(
                len(self.have.get("wireless_profile_names", [])),
                len(self.have.get("wireless_profile_list", [])),
                len(self.have.get("wireless_profile_info", {}))
            ),
            "INFO"
        )
        return self

    def collect_site_and_template_details(self, profile_names):
        """
        Retrieves template and site assignment details for wireless profiles.

        This function fetches Day-N CLI template names and site hierarchical assignments
        for specified wireless profiles by querying Catalyst Center APIs, constructing
        profile ID to template name mappings for Day-N template documentation, building
        site ID to name dictionaries for site hierarchy representation, and populating
        class attributes with template and site details for downstream YAML generation
        workflow.

        Args:
            profile_names (list): List of wireless profile name strings to retrieve
                                template and site assignments for targeted detail
                                collection. Must contain valid profile names existing
                                in wireless_profile_list.

        Returns:
            object: Self instance with updated attributes:
                    - self.have["wireless_profile_templates"]: Dictionary mapping profile
                    IDs to lists of CLI template names
                    - self.have["wireless_profile_sites"]: Dictionary mapping profile IDs
                    to site ID-to-name dictionaries with hierarchical paths
                    - Logs warnings for profiles without templates or site assignments
        """
        self.log(
            f"Starting template and site detail collection for {len(profile_names)} wireless profile(s): "
            f"{profile_names}. Workflow retrieves Day-N CLI templates and site assignments per "
            "profile using profile IDs for API calls.",
            "DEBUG"
        )

        profiles_processed = 0
        profiles_skipped = 0

        self.log(
            f"Initializing iteration through {len(profile_names)} profile name(s) to fetch templates and "
            "sites. Each profile requires profile ID extraction and two API calls for "
            "template and site retrieval.",
            "DEBUG"
        )

        for profile_index, each_profile in enumerate(profile_names, start=1):
            self.log(
                f"Processing profile {profile_index}/{len(profile_names)}: '{each_profile}'. "
                "Extracting profile ID from "
                "wireless_profile_list for API parameter construction.",
                "DEBUG"
            )
            profile_id = self.get_value_by_key(
                self.have["wireless_profile_list"],
                "name",
                each_profile,
                "id",
            )

            if not profile_id:
                profiles_skipped += 1
                self.log(
                    f"Profile {profile_index}/{len(profile_names)} '{each_profile}' "
                    "ID not found in wireless_profile_list with "
                    f"{len(self.have['wireless_profile_list'])} entries. "
                    "Skipping template and site retrieval for this profile. "
                    f"Total skipped: {profiles_skipped}",
                    "WARNING"
                )
                continue
            self.log(
                f"Profile ID '{profile_id}' extracted for profile "
                f"'{each_profile}'. Retrieving CLI templates "
                "using get_templates_for_profile() API call.",
                "DEBUG"
            )

            templates = self.get_templates_for_profile(profile_id)
            if templates:
                template_names = [
                    template.get("name") for template in templates
                ]
                self.have.setdefault("wireless_profile_templates", {})[
                    profile_id
                ] = template_names
                self.log(
                    f"Retrieved {len(template_names)} CLI template(s) for "
                    f"profile '{each_profile}' (ID: {profile_id}): {template_names}. "
                    "Storing template names in wireless_profile_templates dictionary.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"No CLI templates found for profile {profile_index}/{len(profile_names)} "
                    f"'{each_profile}' (ID: {profile_id}). "
                    "get_templates_for_profile() returned empty response. Profile may "
                    "not have Day-N templates assigned.",
                    "WARNING"
                )

            self.log(
                f"Retrieving site assignments for profile '{each_profile}' "
                f"(ID: {profile_id}) using "
                "get_site_lists_for_profile() API call.",
                "DEBUG"
            )
            site_list = self.get_site_lists_for_profile(
                each_profile, profile_id)
            if not site_list:
                self.log(
                    f"No site assignments found for profile {profile_index}/{len(profile_names)} "
                    f"'{each_profile}' (ID: {profile_id}). "
                    "get_site_lists_for_profile() returned empty response. Profile may "
                    "not be assigned to any sites.",
                    "WARNING"
                )
                continue

            self.log(
                f"Received {len(site_list)} site assignment(s) for "
                f"profile '{each_profile}' (ID: {profile_id}). "
                "Extracting site IDs for site ID-to-name mapping construction.",
                "DEBUG"
            )
            site_id_list = [site.get("id") for site in site_list]
            self.log(
                f"Extracted {len(site_id_list)} site ID(s) from site assignments: {site_id_list}. Calling "
                "get_site_id_name_mapping() to resolve site IDs to hierarchical "
                "site names.",
                "DEBUG"
            )
            site_id_name_mapping = self.get_site_id_name_mapping(site_id_list)
            self.log(
                f"Site ID-to-name mapping created for profile '{each_profile}' "
                f"with {len(site_id_name_mapping)} site(s): "
                f"{self.pprint(site_id_name_mapping)}. Storing mapping "
                "in wireless_profile_sites dictionary.",
                "DEBUG"
            )
            self.have.setdefault("wireless_profile_sites", {})[
                profile_id
            ] = site_id_name_mapping
            log_msg = f"Retrieved site list for wireless profile '{each_profile}': {site_id_name_mapping}"
            self.log(log_msg, "DEBUG")

            profiles_processed += 1

            self.log(
                "Completed processing profile {0}/{1} '{2}'. Total profiles processed: "
                "{3}, skipped: {4}. Template count: {5}, Site count: {6}".format(
                    profile_index, len(profile_names), each_profile, profiles_processed,
                    profiles_skipped,
                    len(self.have.get("wireless_profile_templates", {}).get(profile_id, [])),
                    len(self.have.get("wireless_profile_sites", {}).get(profile_id, {}))
                ),
                "DEBUG"
            )

        self.log(
            "Template and site detail collection completed successfully. Processed "
            "{0}/{1} profile(s), skipped {2} profile(s). Total templates collected: {3}, "
            "Total sites collected: {4}. Returning self instance with populated "
            "wireless_profile_templates and wireless_profile_sites dictionaries.".format(
                profiles_processed, len(profile_names), profiles_skipped,
                len(self.have.get("wireless_profile_templates", {})),
                len(self.have.get("wireless_profile_sites", {}))
            ),
            "INFO"
        )

        return self

    def process_global_filters(self, global_filters):
        """
        Processes global filters to extract matching wireless profile configurations.

        This function applies hierarchical filter priority (profile names > Day-N
        templates > sites > SSIDs > AP zones > feature templates > additional interfaces)
        to identify and extract wireless profile configurations from Catalyst Center by
        iterating through filter types in priority order, matching filter criteria against
        cached profile data, processing matched profiles to extract complete configuration
        details, and aggregating processed configurations into final list for YAML
        generation workflow.

        Args:
            global_filters (dict): Global filter configuration dictionary containing:
                                - profile_name_list (list, optional): Profile names for
                                    highest priority filtering
                                - day_n_template_list (list, optional): Day-N template
                                    names for template-based filtering
                                - site_list (list, optional): Site hierarchical names
                                    for site-based filtering
                                - ssid_list (list, optional): SSID names for SSID-based
                                    filtering
                                - ap_zone_list (list, optional): AP zone names for
                                    zone-based filtering
                                - feature_template_list (list, optional): Feature
                                    template design names for template-based filtering
                                - additional_interface_list (list, optional): Interface
                                    names for interface-based filtering

        Returns:
            list | None: List of dictionaries containing processed profile configurations
                        with profile_name, day_n_templates, site_names, ssid_details,
                        ap_zones, feature_template_designs, and additional_interfaces
                        based on filter matches. Returns None if no profiles match
                        provided filters.
        """
        self.log(
            "Starting global filter processing with hierarchical priority (profile names > "
            "Day-N templates > sites > SSIDs > AP zones > feature templates > additional "
            f"interfaces). Filters provided: {global_filters}. Processing applies first matching filter "
            "type only.",
            "DEBUG"
        )

        profile_names = global_filters.get("profile_name_list")
        day_n_templates = global_filters.get("day_n_template_list")
        site_list = global_filters.get("site_list")
        ssid_list = global_filters.get("ssid_list")
        ap_zone_list = global_filters.get("ap_zone_list")
        feature_template_list = global_filters.get("feature_template_list")
        additional_interface_list = global_filters.get("additional_interface_list")
        final_list = []
        self.log(
            "Filter extraction completed. Profile names: {0}, Day-N templates: {1}, "
            "Sites: {2}, SSIDs: {3}, AP zones: {4}, Feature templates: {5}, Additional "
            "interfaces: {6}. Proceeding with hierarchical filter evaluation.".format(
                bool(profile_names), bool(day_n_templates), bool(site_list),
                bool(ssid_list), bool(ap_zone_list), bool(feature_template_list),
                bool(additional_interface_list)
            ),
            "DEBUG"
        )

        if profile_names and isinstance(profile_names, list):
            self.log(
                f"Applying HIGHEST PRIORITY filter: profile_name_list with {len(profile_names)} profile(s): "
                f"{profile_names}. Matching against wireless_profile_names with "
                f"{len(self.have.get('wireless_profile_names', []))} cached profile(s). "
                "Processing only profiles present in both lists.",
                "DEBUG"
            )

            profiles_matched = 0

            for profile_index, profile in enumerate(self.have["wireless_profile_names"], start=1):
                if profile in profile_names:
                    self.log(
                        f"Profile {profile_index}/{len(self.have['wireless_profile_names'])} "
                        f"'{profile}' found in profile_name_list filter. "
                        "Extracting profile ID for detailed configuration processing.",
                        "DEBUG"
                    )
                    profile_id = self.get_value_by_key(
                        self.have["wireless_profile_list"],
                        "name", profile, "id",
                    )
                    if profile_id:
                        self.log(
                            f"Profile ID '{profile_id}' extracted for profile '{profile}'. Calling "
                            "process_profile_info() to extract complete configuration "
                            "including templates, sites, SSIDs, AP zones, feature "
                            "templates, and interfaces.",
                            "DEBUG"
                        )
                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        profiles_matched += 1

                        self.log(
                            f"Profile configuration processed successfully for '{profile}'. "
                            f"Total profiles matched: {profiles_matched}. "
                            f"Configuration: {each_profile_config}",
                            "DEBUG"
                        )
                    else:
                        self.log(
                            f"Profile ID not found for profile '{profile}' in wireless_profile_list. "
                            "Skipping configuration extraction for this profile.",
                            "WARNING"
                        )

            self.log(
                f"Profile name list filtering completed. Matched {profiles_matched} "
                f"profile(s) from {len(profile_names)} "
                f"filter(s). Final configurations collected: {len(final_list)}. "
                "Skipping remaining filter "
                "types due to hierarchical priority.",
                "INFO"
            )
        elif day_n_templates and isinstance(day_n_templates, list):
            self.log(
                "Applying SECOND PRIORITY filter: day_n_template_list "
                f"with {len(day_n_templates)} template(s): "
                f"{len(day_n_templates)}. Matching against wireless_profile_templates "
                f"with {len(self.have.get('wireless_profile_templates', {}))} cached profile(s). "
                "Processing profiles containing any matching Day-N templates.",
                "DEBUG"
            )

            day_n_template_matches = 0
            unmatched_day_n_templates = []
            for template_index, given_template in enumerate(day_n_templates, start=1):
                self.log(
                    f"Processing Day-N template filter {template_index}/{len(day_n_templates)}: '{given_template}'. "
                    "Iterating through wireless_profile_templates to find profiles containing this template.",
                    "DEBUG"
                )

                profiles_matched = 0

                for profile_index, (profile_id, templates) in enumerate(
                    self.have.get("wireless_profile_templates", {}).items(), start=1
                ):
                    self.log(
                        f"Checking profile {profile_index}/"
                        f"{len(self.have.get('wireless_profile_templates', {}))} (ID: "
                        f"{profile_id}) with {len(templates)} template(s): {templates}. "
                        "Testing for any template match in day_n_template_list filter.",
                        "DEBUG"
                    )

                    if given_template in templates:
                        self.log(
                            f"Profile ID '{profile_id}' contains matching Day-N template(s): {given_template}. "
                            "Calling process_profile_info() to extract complete configuration.",
                            "DEBUG"
                        )

                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        profiles_matched += 1

                        self.log(
                            "Profile configuration processed successfully for profile ID '{0}'. "
                            "Total profiles matched: {1}. Configuration: {2}".format(
                                profile_id, profiles_matched, each_profile_config
                            ),
                            "DEBUG"
                        )

                if profiles_matched == 0:
                    self.msg = (
                        f"No profiles matched Day-N template filter '{given_template}' "
                        "after checking all profiles. "
                        "This template may not be associated with any profiles.")
                    self.log(self.msg, "WARNING")
                    unmatched_day_n_templates.append(given_template)
                else:
                    day_n_template_matches += 1
                    self.log(
                        f"Day-N template filter '{given_template}' matched {profiles_matched} profile(s). "
                        f"Total Day-N template filters matched so far: {day_n_template_matches}. "
                        f"Configurations collected so far: {len(final_list)}.",
                        "DEBUG"
                    )

            if unmatched_day_n_templates:
                self.msg = (
                    f"The following Day-N template filter(s) did not match any profiles: "
                    f"{unmatched_day_n_templates}. Verify these templates exist in Catalyst Center "
                    "and are associated with profiles."
                )
                self.log(self.msg, "WARNING")

            self.log(
                f"Day-N template list filtering completed. Matched {day_n_template_matches} "
                f"profile(s) from {len(day_n_templates)} "
                f"template filter(s). Final configurations collected: "
                f"{len(final_list)}. Skipping remaining "
                "filter types due to hierarchical priority.",
                "INFO"
            )
        elif site_list and isinstance(site_list, list):
            self.log(
                "Applying THIRD PRIORITY filter: site_list with "
                f"{len(site_list)} site(s): {site_list}. "
                "Matching against wireless_profile_sites with "
                f"{len(self.have.get('wireless_profile_sites', {}))} cached profile(s). "
                "Processing profiles assigned to any matching sites.",
                "DEBUG"
            )

            matched_sites = 0
            unmatched_sites = []
            for site_index, given_site in enumerate(site_list, start=1):
                self.log(
                    f"Processing site filter {site_index}/{len(site_list)}: '{given_site}'. "
                    "Iterating through wireless_profile_sites to find profiles assigned to this site.",
                    "DEBUG"
                )

                profiles_matched = 0

                for profile_index, (profile_id, sites) in enumerate(
                    self.have.get("wireless_profile_sites", {}).items(), start=1
                ):
                    self.log(
                        f"Checking profile {profile_index}/{len(self.have.get('wireless_profile_sites', {}))} "
                        f"(ID: {profile_id}) with {len(sites)} site assignment(s): {list(sites.values())}. "
                        "Testing for any site match in site_list filter.",
                        "DEBUG"
                    )

                    if given_site in sites.values():
                        self.log(
                            f"Profile ID '{profile_id}' assigned to matching site(s): {given_site}. Calling "
                            "process_profile_info() to extract complete configuration.",
                            "DEBUG"
                        )

                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        profiles_matched += 1

                        self.log(
                            f"Profile configuration processed successfully for profile ID '{profile_id}'. "
                            f"Total profiles matched: {profiles_matched}. Configuration: {each_profile_config}",
                            "DEBUG"
                        )

                if profiles_matched == 0:
                    self.msg = (
                        f"No profiles matched site filter '{given_site}' after checking all profiles. "
                        "This site may not be associated with any profiles.")
                    self.log(self.msg, "WARNING")
                    unmatched_sites.append(given_site)
                else:
                    matched_sites += 1
                    self.log(
                        f"Site filter '{given_site}' matched {profiles_matched} profile(s). "
                        f"Total site filters matched so far: {matched_sites}. "
                        f"Configurations collected so far: {len(final_list)}.",
                        "DEBUG"
                    )

            if unmatched_sites:
                self.msg = (
                    f"The following site filter(s) did not match any profiles: "
                    f"{unmatched_sites}. Verify these sites exist in Catalyst Center "
                    "and are associated with profiles."
                )
                self.log(self.msg, "WARNING")

            unique_data = {d["profile_name"]: d for d in final_list}.values()
            final_list = list(unique_data)

            self.log(
                f"Site list filtering completed. Matched {matched_sites} "
                f"profile(s) from {len(site_list)} site "
                "filter(s). Final configurations collected: "
                f"{len(final_list)}. Skipping remaining filter "
                "types due to hierarchical priority.",
                "INFO"
            )
        elif ssid_list and isinstance(ssid_list, list):
            self.log(
                "Applying FOURTH PRIORITY filter: ssid_list with "
                f"{len(ssid_list)} SSID(s): {ssid_list}. "
                "Matching against wireless_profile_info ssidDetails "
                f"with {len(self.have.get('wireless_profile_info', {}))} cached "
                "profile(s). Processing profiles containing any matching SSIDs.",
                "DEBUG"
            )

            ssid_matched = 0
            unmatched_ssids = []
            for given_ssid in ssid_list:
                self.log(
                    f"Processing SSID filter '{given_ssid}' against wireless_profile_info. "
                    f"Iterating through {len(self.have.get('wireless_profile_info', {}))} profiles to find matches.",
                    "DEBUG"
                )

                profiles_matched = 0

                for profile_index, (profile_id, profile_info) in enumerate(
                    self.have.get("wireless_profile_info", {}).items(), start=1
                ):
                    ssid_details = profile_info.get("ssidDetails", [])

                    self.log(
                        f"Checking profile {profile_index}/{len(self.have.get('wireless_profile_info', {}))} "
                        f"(ID: {profile_id}) with {len(ssid_details)} SSID detail(s). "
                        "Extracting SSID names for matching against ssid_list filter.",
                        "DEBUG"
                    )

                    if any(ssid.get("ssidName") == given_ssid for ssid in ssid_details):
                        self.log(
                            f"Profile ID '{profile_id}' contains matching "
                            f"SSID(s): {given_ssid}. Calling "
                            "process_profile_info() to extract complete configuration.",
                            "DEBUG"
                        )

                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        profiles_matched += 1

                        self.log(
                            "Profile configuration processed successfully "
                            f"for profile ID '{profile_id}'. "
                            f"Total profiles matched: {profiles_matched}. "
                            f"Configuration: {each_profile_config}",
                            "DEBUG"
                        )

                if profiles_matched == 0:
                    self.msg = (
                        f"No profiles matched SSID filter '{given_ssid}' after checking all profiles. "
                        "This SSID may not be associated with any profiles.")
                    self.log(self.msg, "WARNING")
                    unmatched_ssids.append(given_ssid)
                else:
                    ssid_matched += 1
                    self.log(
                        f"SSID filter '{given_ssid}' matched {profiles_matched} profile(s). "
                        f"Total SSID filters matched so far: {ssid_matched}. "
                        f"Configurations collected so far: {len(final_list)}.",
                        "DEBUG"
                    )

            if unmatched_ssids:
                self.msg = (
                    f"The following SSID filter(s) did not match any profiles: "
                    f"{unmatched_ssids}. Verify these SSIDs exist in Catalyst Center "
                    "and are associated with profiles."
                )
                self.log(self.msg, "WARNING")

            unique_data = {d["profile_name"]: d for d in final_list}.values()
            final_list = list(unique_data)

            self.log(
                f"SSID list filtering completed. Matched {ssid_matched} "
                f"profile(s) from {len(ssid_list)} SSID "
                f"filter(s). Final configurations collected: {len(final_list)}. "
                "Skipping remaining filter "
                "types due to hierarchical priority.",
                "INFO"
            )
        elif ap_zone_list and isinstance(ap_zone_list, list):
            self.log(
                f"Applying FIFTH PRIORITY filter: ap_zone_list with {len(ap_zone_list)} "
                f"AP zone(s): {ap_zone_list}. "
                "Matching against wireless_profile_info apZones with "
                f"{len(self.have.get('wireless_profile_info', {}))} cached profile(s). "
                "Processing profiles containing any matching AP zones.",
                "DEBUG"
            )

            ap_zone_matched = 0
            unmatched_apzones = []
            for given_ap_zone in ap_zone_list:
                self.log(
                    f"Processing AP zone filter '{given_ap_zone}' against wireless_profile_info. "
                    f"Iterating through {len(self.have.get('wireless_profile_info', {}))} "
                    "profiles to find matches.",
                    "DEBUG"
                )
                profiles_matched = 0

                for profile_index, (profile_id, profile_info) in enumerate(
                    self.have.get("wireless_profile_info", {}).items(), start=1
                ):
                    ap_zones = profile_info.get("apZones", [])

                    self.log(
                        f"Checking profile {profile_index}/{len(self.have.get('wireless_profile_info', {}))} "
                        f"(ID: {profile_id}) with {len(ap_zones)} AP zone(s). Extracting "
                        "AP zone names for matching against ap_zone_list filter.",
                        "DEBUG"
                    )

                    if any(ap_zone.get("apZoneName") == given_ap_zone for ap_zone in ap_zones):
                        self.log(
                            f"Profile ID '{profile_id}' contains matching "
                            f"AP zone(s): {given_ap_zone}. Calling "
                            "process_profile_info() to extract complete configuration.",
                            "DEBUG"
                        )

                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        profiles_matched += 1

                        self.log(
                            f"Profile configuration processed successfully for profile ID '{profile_id}'. "
                            f"Total profiles matched: {profiles_matched}. "
                            f"Configuration: {each_profile_config}",
                            "DEBUG"
                        )

                if profiles_matched == 0:
                    self.msg = (
                        f"No profiles matched AP zone filter '{given_ap_zone}' "
                        "after checking all profiles. "
                        "This AP zone may not be associated with any profiles.")
                    self.log(self.msg, "WARNING")
                    unmatched_apzones.append(given_ap_zone)
                else:
                    ap_zone_matched += 1
                    self.log(
                        f"AP zone filter '{given_ap_zone}' matched {profiles_matched} profile(s). "
                        f"Total AP zone filters matched so far: {ap_zone_matched}. "
                        f"Configurations collected so far: {len(final_list)}.",
                        "DEBUG"
                    )

            if unmatched_apzones:
                self.msg = (
                    f"The following AP zone filter(s) did not match any profiles: "
                    f"{unmatched_apzones}. Verify these AP zones exist in Catalyst Center "
                    "and are associated with profiles."
                )
                self.log(self.msg, "WARNING")

            unique_data = {d["profile_name"]: d for d in final_list}.values()
            final_list = list(unique_data)

            self.log(
                f"AP zone list filtering completed. Matched {ap_zone_matched} "
                f"profile(s) from {len(ap_zone_list)} AP zone "
                f"filter(s). Final configurations collected: {len(final_list)}. "
                "Skipping remaining filter "
                "types due to hierarchical priority.",
                "INFO"
            )
        elif feature_template_list and isinstance(feature_template_list, list):
            self.log(
                f"Applying SIXTH PRIORITY filter: feature_template_list "
                f"with {len(feature_template_list)} template(s): "
                f"{feature_template_list}. Matching against wireless_profile_info featureTemplates "
                f"with {len(self.have.get('wireless_profile_info', {}))} cached "
                "profile(s). Processing profiles containing any matching feature templates.",
                "DEBUG"
            )

            matched_feature_templates = 0
            un_matched_feature_templates = []
            for template in feature_template_list:
                self.log(
                    f"Processing feature template filter '{template}' against wireless_profile_info. "
                    f"Iterating through {len(self.have.get('wireless_profile_info', {}))} profiles to find matches.",
                    "DEBUG"
                )

                profiles_matched = 0

                for profile_index, (profile_id, profile_info) in enumerate(
                    self.have.get("wireless_profile_info", {}).items(), start=1
                ):
                    feature_templates = profile_info.get("featureTemplates", [])

                    self.log(
                        f"Checking profile {profile_index}/{len(self.have.get('wireless_profile_info', {}))} "
                        f"(ID: {profile_id}) with {len(feature_templates)} feature template(s). "
                        "Extracting design names for matching against feature_template_list "
                        "filter.",
                        "DEBUG"
                    )

                    if any(
                        feature_template.get("designName") == template
                        for feature_template in feature_templates
                    ):
                        self.log(
                            f"Profile ID '{profile_id}' contains matching feature "
                            f"template(s): {template}. "
                            "Calling process_profile_info() to extract complete configuration.",
                            "DEBUG"
                        )

                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        profiles_matched += 1

                        self.log(
                            f"Profile configuration processed successfully for profile ID '{profile_id}'. "
                            f"Total profiles matched: {profiles_matched}. "
                            f"Configuration: {each_profile_config}",
                            "DEBUG"
                        )

                if profiles_matched == 0:
                    self.msg = (
                        f"No profiles matched feature template filter '{template}' "
                        "after checking all profiles. "
                        "This feature template may not be associated with any profiles.")
                    un_matched_feature_templates.append(template)
                    self.log(self.msg, "WARNING")
                else:
                    matched_feature_templates += 1
                    self.log(
                        f"Feature template filter '{template}' matched {profiles_matched} profile(s). "
                        f"Total feature template filters matched so far: {matched_feature_templates}. "
                        f"Configurations collected so far: {len(final_list)}.",
                        "DEBUG"
                    )

            if un_matched_feature_templates:
                self.msg = (
                    f"The following feature template filter(s) did not match any profiles: "
                    f"{un_matched_feature_templates}. Verify these templates exist in Catalyst Center "
                    "and are associated with profiles."
                )
                self.log(self.msg, "WARNING")

            unique_data = {d["profile_name"]: d for d in final_list}.values()
            final_list = list(unique_data)

            self.log(
                "Feature template list filtering completed. Matched "
                f"{matched_feature_templates} profile(s) from {len(feature_template_list)} "
                f"feature template filter(s). Final configurations collected: {len(final_list)}. Skipping "
                "remaining filter types due to hierarchical priority.",
                "INFO"
            )
        elif additional_interface_list and isinstance(additional_interface_list, list):
            self.log(
                f"Applying LOWEST PRIORITY filter: additional_interface_list with {len(additional_interface_list)} "
                f"interface(s): {additional_interface_list}. Matching against wireless_profile_info "
                f"additionalInterfaces with {len(self.have.get('wireless_profile_info', {}))} "
                "cached profile(s). Processing profiles "
                "containing any matching interfaces.",
                "DEBUG"
            )

            matched_interfaces = 0
            unmatched_interfaces = []

            for given_interface in additional_interface_list:
                self.log(
                    f"Processing additional interface filter '{given_interface}' "
                    "against wireless_profile_info. "
                    f"Iterating through {len(self.have.get('wireless_profile_info', {}))} "
                    "profiles to find matches.",
                    "DEBUG"
                )

                profiles_matched = 0

                for profile_index, (profile_id, profile_info) in enumerate(
                    self.have.get("wireless_profile_info", {}).items(), start=1
                ):
                    additional_interfaces = profile_info.get("additionalInterfaces", [])

                    self.log(
                        f"Checking profile {profile_index}/{len(self.have.get('wireless_profile_info', {}))} "
                        f"(ID: {profile_id}) with {len(additional_interfaces)} additional interface(s): "
                        f"{additional_interfaces}. Testing for any interface match in additional_interface_list "
                        "filter.",
                        "DEBUG"
                    )

                    if given_interface in additional_interfaces:
                        self.log(
                            f"Profile ID '{profile_id}' contains matching "
                            f"additional interface(s): {given_interface}. "
                            "Calling process_profile_info() to extract complete configuration.",
                            "DEBUG"
                        )

                        each_profile_config = self.process_profile_info(profile_id, final_list)
                        profiles_matched += 1

                        self.log(
                            f"Profile configuration processed successfully for profile ID '{profile_id}'. "
                            f"Total profiles matched: {profiles_matched}. Configuration: {each_profile_config}",
                            "DEBUG"
                        )

                if profiles_matched == 0:
                    self.msg = (
                        f"No profiles matched additional interface filter '{given_interface}' after checking all profiles. "
                        "This interface may not be associated with any profiles.")
                    unmatched_interfaces.append(given_interface)
                    self.log(self.msg, "WARNING")
                else:
                    matched_interfaces += 1
                    self.log(
                        f"Additional interface filter '{given_interface}' matched {profiles_matched} profile(s). "
                        f"Total additional interface filters matched so far: {matched_interfaces}. "
                        f"Configurations collected so far: {len(final_list)}.",
                        "DEBUG"
                    )

            if unmatched_interfaces:
                self.msg = (
                    f"The following additional interface filter(s) did not match any profiles: "
                    f"{unmatched_interfaces}. Verify these interfaces exist in Catalyst Center "
                    "and are associated with profiles."
                )
                self.log(self.msg, "WARNING")

            unique_data = {d["profile_name"]: d for d in final_list}.values()
            final_list = list(unique_data)

            self.log(
                "Additional interface list filtering completed. "
                f"Matched {matched_interfaces} profile(s) from "
                f"{len(additional_interface_list)} interface filter(s). "
                f"Final configurations collected: {len(final_list)}. All filter "
                "types processed.",
                "INFO"
            )
        else:
            self.log(
                "No specific global filters provided or no filters matched expected list "
                "types. No filter-based processing performed. Filters received: {global_filters}",
                "WARNING"
            )

        if not final_list:
            self.log(
                "Global filter processing completed with zero profile matches. No profiles "
                "matched provided filter criteria across all filter types. Verify filter "
                "values match existing Catalyst Center configurations. Returning None to "
                "indicate no matching configurations.",
                "WARNING"
            )
            return None

        self.log(
            f"Global filter processing completed successfully. Total {len(final_list)} profile "
            "configuration(s) extracted and aggregated. Returning final_list for YAML "
            "generation workflow.",
            "INFO"
        )

        return final_list

    def process_profile_info(self, profile_id, final_list):
        """
        Processes and aggregates wireless profile configuration details.

        This function extracts complete wireless profile configuration by retrieving
        profile information from cached profile data, collecting CLI template names
        associated with profile, extracting site assignments with hierarchical names,
        parsing SSID details with fabric and VLAN configurations, processing AP zone
        configurations with RF profiles, extracting feature template designs with SSID
        mappings, and processing additional interface configurations with VLAN IDs for
        comprehensive profile documentation in YAML generation workflow.

        Args:
            profile_id (str): UUID of wireless profile to process for configuration
                            extraction from cached wireless_profile_info dictionary.
            final_list (list): Accumulator list for collecting processed profile
                            configurations across multiple profile processing calls
                            enabling batch profile aggregation.

        Returns:
            dict: Dictionary containing processed profile configuration with:
                - profile_name (str): Wireless profile name
                - day_n_templates (list, optional): CLI template names if assigned
                - site_names (list, optional): Site hierarchical paths if assigned
                - ssid_details (list, optional): Parsed SSID configurations with
                    fabric, VLAN, interface, and anchor group settings
                - additional_interfaces (list, optional): Interface configurations
                    with VLAN IDs
                - ap_zones (list, optional): AP zone configurations with SSIDs and
                    RF profiles
                - feature_template_designs (list, optional): Feature template designs
                    with SSID associations
                Returns empty dict if profile_id not found in cached profile info.
        """
        self.log(
            f"Starting wireless profile configuration processing for profile ID '{profile_id}'. "
            "Extracting CLI templates, sites, SSIDs, AP zones, feature templates, and "
            "additional interfaces from cached profile information for comprehensive "
            "YAML documentation.",
            "DEBUG"
        )

        each_profile_config = {}
        profile_info = self.have.get("wireless_profile_info", {}).get(profile_id)

        if not profile_info:
            self.log(
                f"No profile information found in cache for profile ID '{profile_id}'. Profile may "
                "not exist or cache incomplete. Returning empty configuration dictionary "
                f"and skipping processing. Available profile IDs: {list(self.have.get('wireless_profile_info', {}).keys())}",
                "WARNING"
            )
            return each_profile_config

        self.log(
            f"Profile information retrieved successfully for profile ID '{profile_id}'. Profile "
            f"data: {self.pprint(profile_info)}. Proceeding with CLI template extraction.",
            "DEBUG"
        )

        self.log(
            f"Extracting CLI template details for profile ID '{profile_id}' from "
            "wireless_profile_templates cache with "
            f"{len(self.have.get('wireless_profile_templates', {}))} cached profile(s).",
            "DEBUG"
        )
        cli_template_details = self.have.get(
            "wireless_profile_templates", {}).get(profile_id)
        if cli_template_details and isinstance(cli_template_details, list):
            if len(cli_template_details) > 0:
                each_profile_config["day_n_templates"] = cli_template_details
                self.log(
                    f"CLI template details extracted for profile ID '{profile_id}': "
                    f"{len(cli_template_details)} template(s) "
                    f"found. Templates: {cli_template_details}. Added to "
                    "configuration under 'day_n_templates' key.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"CLI template list exists for profile ID '{profile_id}' but is empty. No "
                    "templates assigned to profile. Skipping day_n_templates addition.",
                    "DEBUG"
                )
        else:
            self.log(
                f"No CLI template details found for profile ID '{profile_id}' in cache or data type "
                f"invalid (expected list, got {type(cli_template_details).__name__}). "
                "Profile may not have Day-N templates "
                "assigned.",
                "DEBUG"
            )

        self.log(
            f"Extracting site assignment details for profile ID '{profile_id}' from "
            f"wireless_profile_sites cache with {len(self.have.get('wireless_profile_sites', {}))} "
            "cached profile(s).",
            "DEBUG"
        )
        site_details = self.have.get("wireless_profile_sites", {}).get(profile_id)

        if site_details and isinstance(site_details, dict):
            site_list = list(site_details.values())

            if site_list:
                each_profile_config["site_names"] = site_list

                self.log(
                    "Site assignment details extracted for profile "
                    f"ID '{profile_id}': {len(site_list)} site(s) "
                    f"found. Sites: {site_list}. Added to configuration under 'site_names' key with "
                    "hierarchical paths.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"Site details dictionary exists for profile ID '{profile_id}' but contains no "
                    "site assignments. Empty dictionary received. Skipping site_names "
                    "addition.",
                    "DEBUG"
                )
        else:
            self.log(
                f"No site assignment details found for profile ID '{profile_id}' in cache or data "
                f"type invalid (expected dict, got {type(site_details).__name__}). "
                "Profile may not be assigned to any sites.",
                "DEBUG"
            )

        self.log(
            "Extracting wireless profile name from profile information for profile ID "
            f"'{profile_id}'. Profile name is mandatory field for YAML configuration.",
            "DEBUG"
        )

        each_profile_config["profile_name"] = profile_info.get("wirelessProfileName")

        self.log(
            f"Profile name extracted: '{each_profile_config['profile_name']}'. "
            "Added to configuration under 'profile_name' "
            "key as primary identifier for wireless profile.",
            "DEBUG"
        )

        self.log(
            f"Extracting component details from profile information for profile ID '{profile_id}'. "
            "Components include: ssidDetails, additionalInterfaces, apZones, "
            "featureTemplates for parsing and transformation.",
            "DEBUG"
        )

        ssid_details = profile_info.get("ssidDetails", "")
        additional_interfaces = profile_info.get("additionalInterfaces", "")
        ap_zones = profile_info.get("apZones", "")
        feature_template_designs = profile_info.get("featureTemplates", "")
        self.log(
            "Component extraction completed. SSID details: {0} item(s), Additional "
            "interfaces: {1} item(s), AP zones: {2} item(s), Feature templates: {3} "
            "item(s). Proceeding with component parsing.".format(
                len(ssid_details) if isinstance(ssid_details, list) else "N/A",
                len(additional_interfaces) if isinstance(additional_interfaces, list) else "N/A",
                len(ap_zones) if isinstance(ap_zones, list) else "N/A",
                len(feature_template_designs) if isinstance(feature_template_designs, list) else "N/A"
            ),
            "DEBUG"
        )

        self.log(
            f"Parsing SSID details for profile ID '{profile_id}' using parse_profile_info() with "
            "profile_key 'ssid_details'. Extracting SSID names, fabric settings, VLAN "
            "configurations, and interface mappings.",
            "DEBUG"
        )

        parsed_ssids = self.parse_profile_info(ssid_details, "ssid_details")
        if parsed_ssids:
            each_profile_config["ssid_details"] = parsed_ssids
            self.log(
                "SSID parsing completed successfully for profile ID "
                f"'{profile_id}'. Parsed {len(parsed_ssids)} "
                f"SSID configuration(s): {self.pprint(parsed_ssids)}. "
                "Added to configuration under 'ssid_details' "
                "key.",
                "DEBUG"
            )
        else:
            self.log(
                f"SSID parsing returned no results for profile ID '{profile_id}'. No SSID "
                "configurations parsed from ssidDetails. Skipping ssid_details addition.",
                "DEBUG"
            )

        self.log(
            f"Parsing additional interface details for profile ID '{profile_id}' using "
            "parse_profile_info() with profile_key 'additional_interfaces'. Extracting "
            "interface names and VLAN ID mappings.".format(profile_id),
            "DEBUG"
        )
        parsed_interfaces = self.parse_profile_info(
            additional_interfaces, "additional_interfaces")

        if parsed_interfaces:
            each_profile_config["additional_interfaces"] = parsed_interfaces

            self.log(
                f"Additional interface parsing completed successfully for profile ID '{profile_id}'. "
                "Parsed {len(parsed_interfaces)} interface configuration(s): "
                f"{self.pprint(parsed_interfaces)}. Added to configuration under "
                "'additional_interfaces' key.",
                "DEBUG"
            )
        else:
            self.log(
                f"Additional interface parsing returned no results for profile ID '{profile_id}'. "
                "No interface configurations parsed from additionalInterfaces. Skipping "
                "additional_interfaces addition.",
                "DEBUG"
            )

        self.log(
            f"Parsing AP zone details for profile ID '{profile_id}' using parse_profile_info() "
            "with profile_key 'ap_zones'. Extracting zone names, SSID associations, and "
            "RF profile mappings.",
            "DEBUG"
        )
        parsed_ap_zones = self.parse_profile_info(ap_zones, "ap_zones")

        if parsed_ap_zones:
            each_profile_config["ap_zones"] = parsed_ap_zones

            self.log(
                f"AP zone parsing completed successfully for profile ID '{profile_id}'. "
                f"Parsed {len(parsed_ap_zones)} "
                f"AP zone configuration(s): {self.pprint(parsed_ap_zones)}. "
                "Added to configuration under 'ap_zones' key.",
                "DEBUG"
            )
        else:
            self.log(
                f"AP zone parsing returned no results for profile ID '{profile_id}'. No AP zone "
                "configurations parsed from apZones. Skipping ap_zones addition.",
                "DEBUG"
            )

        self.log(
            f"Parsing feature template design details for profile ID '{profile_id}' using "
            "parse_profile_info() with profile_key 'feature_template_designs'. Extracting "
            "design names and SSID associations.",
            "DEBUG"
        )
        parsed_feature_templates = self.parse_profile_info(
            feature_template_designs, "feature_template_designs")

        if parsed_feature_templates:
            each_profile_config["feature_template_designs"] = parsed_feature_templates

            self.log(
                f"Feature template parsing completed successfully for profile ID '{profile_id}'. "
                f"Parsed {len(parsed_feature_templates)} feature template "
                f"configuration(s): {self.pprint(parsed_feature_templates)}. Added to configuration "
                "under 'feature_template_designs' key.",
                "DEBUG"
            )
        else:
            self.log(
                f"Feature template parsing returned no results for profile ID '{profile_id}'. No "
                "feature template configurations parsed from featureTemplates. Skipping "
                "feature_template_designs addition.",
                "DEBUG"
            )

        if each_profile_config:
            self.log(
                "Profile configuration processing completed successfully "
                f"for profile '{each_profile_config.get('profile_name')}' "
                f"(ID: {profile_id}). Configuration contains {len(each_profile_config)} "
                f"key(s): {list(each_profile_config.keys())}. Appending to final_list "
                "for aggregation.",
                "DEBUG"
            )

            self.log(
                f"Complete processed configuration for profile '{each_profile_config['profile_name']}': "
                f"{self.pprint(each_profile_config)}. Adding to final_list accumulator.",
                "DEBUG"
            )

            final_list.append(each_profile_config)

            self.log(
                "Profile configuration appended to final_list. Total configurations in "
                f"final_list: {len(final_list)}",
                "DEBUG"
            )
        else:
            self.log(
                f"Profile configuration dictionary is empty for profile ID '{profile_id}'. No "
                "configuration components extracted during processing. Not appending to "
                "final_list.",
                "WARNING"
            )

        self.log(
            "Returning processed configuration dictionary for "
            f"profile ID '{profile_id}' with {len(each_profile_config)} "
            "key(s). Dictionary ready for YAML serialization in generation workflow.",
            "DEBUG"
        )

        return each_profile_config

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates YAML configuration file for network wireless profile config generator.

        This function orchestrates complete YAML playbook generation by determining
        output file path (user-provided or auto-generated), processing auto-discovery
        mode flags to override filters for complete infrastructure extraction,
        collecting profile configurations with CLI templates and site assignments,
        parsing profile components (SSIDs, AP zones, feature templates, additional
        interfaces) for each profile, aggregating configurations into unified structure,
        and writing formatted YAML file with comprehensive header comments for
        compatibility with network_profile_wireless_workflow_manager module.

        Args:
            yaml_config_generator (dict): Configuration parameters containing:
                                        - generate_all_configurations (bool, optional):
                                        Auto-discovery mode flag enabling complete
                                        infrastructure extraction
                                        - file_path (str, optional): Output YAML file
                                        path, defaults to auto-generated timestamped
                                        filename if not provided
                                        - global_filters (dict, optional): Filter
                                        criteria with profile_name_list,
                                        day_n_template_list, site_list, ssid_list,
                                        ap_zone_list, feature_template_list,
                                        additional_interface_list for targeted
                                        extraction

        Returns:
            object: Self instance with updated attributes:
                    - self.msg: Operation result message with status and file path
                    - self.status: Operation status ("success", "failed", or "ok")
                    - self.result: Complete operation result for module exit
                    - Operation result set via set_operation_result()
        """
        self.log(
            "Starting YAML configuration generation workflow for network wireless profile "
            "playbook. Workflow includes file path determination, "
            "auto-discovery mode processing, profile configuration collection, "
            "component parsing, and YAML file writing with header comments.",
            "DEBUG"
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log(
                "Auto-discovery mode enabled (generate_all_configurations=True). Will "
                "extract all wireless profiles with CLI templates, site assignments, "
                "SSIDs, AP zones, feature templates, and additional interfaces without "
                "filter restrictions for complete network wireless profile configuration.",
                "INFO"
            )
        else:
            self.log(
                "Targeted extraction mode (generate_all_configurations=False). Will "
                "apply provided global filters for selective profile and component "
                "retrieval based on filter criteria.",
                "DEBUG"
            )

        self.log(
            "Determining output file path for YAML configuration. Checking for "
            "user-provided file_path parameter or generating default timestamped "
            "filename.",
            "DEBUG"
        )

        file_path = yaml_config_generator.get("file_path")

        if not file_path:
            self.log(
                "No file_path provided in configuration. Generating default filename "
                "with pattern <module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml in "
                "current working directory.",
                "DEBUG"
            )

            file_path = self.generate_filename()

            self.log(
                f"Default filename generated: {file_path}. File will be created in current "
                "working directory.",
                "DEBUG"
            )
        else:
            self.log(
                f"Using user-provided file_path: {file_path}. File will be created at "
                "specified location with directory creation if needed.",
                "DEBUG"
            )

        self.log(
            f"YAML configuration file path determined: {file_path}. Path will be used for "
            "write_dict_to_yaml() operation.",
            "INFO"
        )

        self.log("Initializing filter dictionaries", "DEBUG")
        # Set empty filters to retrieve everything
        global_filters = {}
        final_list = []
        if generate_all:
            self.log(
                "Auto-discovery mode: Extracting all wireless profiles from cached "
                f"wireless_profile_names with {len(self.have.get('wireless_profile_names', []))} "
                "profile(s). Iterating through profiles "
                "to collect CLI templates, sites, SSIDs, AP zones, feature templates, "
                "and additional interfaces.",
                "INFO"
            )

            profiles_processed = 0

            for profile_index, each_profile_name in enumerate(
                self.have.get("wireless_profile_names", []), start=1
            ):
                self.log(
                    f"Processing profile {profile_index}/{len(self.have.get('wireless_profile_names', []))}:"
                    f" '{each_profile_name}'. Initializing configuration "
                    "dictionary for profile component collection.",
                    "DEBUG"
                )
                each_profile_config = {}
                each_profile_config["profile_name"] = each_profile_name

                self.log(
                    f"Extracting profile ID for profile '{each_profile_name}' from wireless_profile_list "
                    f"with {len(self.have.get('wireless_profile_list', []))}"
                    " cached profile(s) for component retrieval.",
                    "DEBUG"
                )

                profile_id = self.get_value_by_key(
                    self.have["wireless_profile_list"],
                    "name",
                    each_profile_name,
                    "id",
                )

                if not profile_id:
                    self.log(
                        f"Profile ID not found for profile '{each_profile_name}' in wireless_profile_list. "
                        "Profile may not exist or cache may be incomplete. "
                        "Skipping component extraction for this profile.",
                        "WARNING"
                    )
                    continue

                self.log(
                    f"Profile ID '{profile_id}' extracted for profile "
                    f"'{each_profile_name}'. Retrieving CLI "
                    "template details from wireless_profile_templates cache.",
                    "DEBUG"
                )
                cli_template_details = self.have.get(
                    "wireless_profile_templates", {}).get(profile_id)
                if cli_template_details and isinstance(cli_template_details, list):
                    each_profile_config["day_n_templates"] = cli_template_details

                    self.log(
                        f"CLI template details added for profile '{each_profile_name}': "
                        f"{len(cli_template_details)} template(s) "
                        f"found. Templates: {cli_template_details}",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"No CLI template details found for profile '{each_profile_name}'"
                        f" (ID: {profile_id}) or "
                        "invalid data type. Profile may not have Day-N templates "
                        "assigned.",
                        "DEBUG"
                    )

                self.log(
                    f"Retrieving site assignment details for profile '{each_profile_name}' (ID: {profile_id}) "
                    "from wireless_profile_sites cache.",
                    "DEBUG"
                )
                site_details = self.have.get(
                    "wireless_profile_sites", {}).get(profile_id)

                if site_details and isinstance(site_details, dict):
                    each_profile_config["site_names"] = list(site_details.values())

                    self.log(
                        f"Site details added for profile '{each_profile_name}': "
                        f"{len(each_profile_config['site_names'])} site(s) found. "
                        f"Sites: {each_profile_config['site_names']}",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"No site assignment details found for profile '{each_profile_name}' (ID: {profile_id}) "
                        "or invalid data type. Profile may not be assigned to any "
                        "sites.",
                        "DEBUG"
                    )

                self.log(
                    f"Retrieving complete profile information for profile '{each_profile_name}' "
                    f"(ID: {profile_id}) from wireless_profile_info cache for component "
                    "parsing.",
                    "DEBUG"
                )
                profile_info = self.have.get("wireless_profile_info", {}).get(profile_id)

                if profile_info:
                    self.log(
                        f"Processing profile information for profile '{each_profile_name}': {self.pprint(profile_info)}. "
                        "Extracting ssidDetails, additionalInterfaces, apZones, "
                        "featureTemplates for parsing.",
                        "DEBUG"
                    )
                    ssid_details = profile_info.get("ssidDetails", "")
                    additional_interfaces = profile_info.get("additionalInterfaces", "")
                    ap_zones = profile_info.get("apZones", "")
                    feature_template_designs = profile_info.get("featureTemplates", "")
                    self.log(
                        "Component extraction completed for profile '{0}'. SSID "
                        "details: {1} item(s), Additional interfaces: {2} item(s), "
                        "AP zones: {3} item(s), Feature templates: {4} item(s). "
                        "Proceeding with component parsing.".format(
                            each_profile_name,
                            len(ssid_details) if isinstance(ssid_details, list) else "N/A",
                            len(additional_interfaces) if isinstance(additional_interfaces, list) else "N/A",
                            len(ap_zones) if isinstance(ap_zones, list) else "N/A",
                            len(feature_template_designs) if isinstance(feature_template_designs, list) else "N/A"
                        ),
                        "DEBUG"
                    )

                    parsed_ssids = self.parse_profile_info(ssid_details, "ssid_details")
                    if parsed_ssids:
                        each_profile_config["ssid_details"] = parsed_ssids
                        self.log(
                            f"SSID parsing completed for profile '{each_profile_name}'. Parsed {len(parsed_ssids)} "
                            "SSID configuration(s).",
                            "DEBUG"
                        )

                    parsed_interfaces = self.parse_profile_info(
                        additional_interfaces, "additional_interfaces")
                    if parsed_interfaces:
                        each_profile_config["additional_interfaces"] = parsed_interfaces
                        self.log(
                            f"Additional interface parsing completed for profile '{each_profile_name}'. "
                            f"Parsed {len(parsed_interfaces)} interface configuration(s).",
                            "DEBUG"
                        )

                    parsed_ap_zones = self.parse_profile_info(ap_zones, "ap_zones")
                    if parsed_ap_zones:
                        each_profile_config["ap_zones"] = parsed_ap_zones
                        self.log(
                            f"AP zone parsing completed for profile '{each_profile_name}'. "
                            f"Parsed {len(parsed_ap_zones)} "
                            "AP zone configuration(s).",
                            "DEBUG"
                        )

                    parsed_feature_templates = self.parse_profile_info(
                        feature_template_designs, "feature_template_designs")
                    if parsed_feature_templates:
                        each_profile_config["feature_template_designs"] = parsed_feature_templates
                        self.log(
                            f"Feature template parsing completed for profile '{each_profile_name}'. "
                            f"Parsed {len(parsed_feature_templates)} feature template configuration(s).",
                            "DEBUG"
                        )
                else:
                    self.log(
                        f"No profile information found in cache for profile '{each_profile_name}' "
                        f"(ID: {profile_id}). Skipping component parsing.",
                        "WARNING"
                    )
                    self.log(
                        "Profile ID not found for profile '{0}' in wireless_profile_list. "
                        "Skipping component collection for this profile.".format(
                            each_profile_name
                        ),
                        "WARNING"
                    )

                profiles_processed += 1
                self.log(
                    f"Profile configuration processing completed for '{each_profile_name}'. "
                    f"Configuration contains {len(each_profile_config)} key(s): "
                    f"{list(each_profile_config.keys())}. Appending to final_list.",
                    "DEBUG"
                )
                final_list.append(each_profile_config)

            self.log(
                "Auto-discovery mode profile collection completed. Processed "
                f"{profiles_processed}/{len(self.have.get('wireless_profile_names', []))} "
                f"profile(s). Total configurations collected: {len(final_list)}. "
                f"Configurations: {self.pprint(final_list)}",
                "INFO"
            )
        else:
            # we get ALL configurations
            self.log(
                "Targeted extraction mode: Extracting global_filters from "
                "yaml_config_generator parameters for filter-based profile retrieval.",
                "DEBUG"
            )
            if yaml_config_generator.get("global_filters"):
                self.log(
                    "Warning: generate_all_configurations is False but global_filters "
                    "provided. This is expected for targeted extraction. Filters will be "
                    "applied to retrieve matching profiles.",
                    "DEBUG"
                )

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            if global_filters:
                self.log(
                    f"Global filters provided: {global_filters}. Calling process_global_filters() to "
                    "apply hierarchical filter matching (profile names > Day-N templates "
                    "> sites > SSIDs > AP zones > feature templates > additional "
                    "interfaces).",
                    "DEBUG"
                )
                final_list = self.process_global_filters(global_filters)

                if final_list:
                    self.log(
                        f"Filter-based profile collection completed. Retrieved {len(final_list)} "
                        "matching profile configuration(s) from global filters.",
                        "INFO"
                    )
                else:
                    self.log(
                        f"No profiles matched provided global filters: {global_filters}. Verify filter "
                        "values match existing Catalyst Center configurations.",
                        "WARNING"
                    )
            else:
                self.log(
                    "No global_filters provided in targeted extraction mode. No profiles "
                    "will be collected. Verify configuration includes either "
                    "generate_all_configurations=True or global_filters.",
                    "WARNING"
                )

        if not final_list:
            self.log(
                f"No configurations retrieved after processing. Auto-discovery mode: {generate_all}, "
                f"Global filters provided: {bool(yaml_config_generator.get('global_filters'))}. "
                "All filters may have excluded available "
                "profiles or no profiles exist in Catalyst Center.",
                "WARNING"
            )

            self.msg = (
                "No configurations or components to process for module '{0}'. Verify "
                "input filters or configuration.".format(self.module_name)
            )
            self.set_operation_result("ok", False, self.msg, "INFO")

            self.log(
                "YAML generation skipped due to no configurations. Returning with 'ok' "
                "status and informational message about filter validation.",
                "INFO"
            )

        self.log(
            "Constructing final YAML configuration dictionary with 'config' key. "
            f"Dictionary will contain {len(final_list)} profile configuration(s) ready for YAML "
            "serialization.",
            "DEBUG"
        )

        final_dict = {"config": final_list}

        self.log(
            "Final YAML configuration dictionary created successfully. Dictionary "
            f"structure: {self.pprint(final_dict)}. Proceeding with write_dict_to_yaml() operation.",
            "DEBUG"
        )

        if self.write_dict_to_yaml(final_dict, file_path):
            self.log(
                f"YAML file write operation succeeded. File created at: {file_path}. File "
                f"contains {len(final_list)} wireless profile configuration(s) with header comments "
                "and formatted structure.",
                "INFO"
            )

            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")

            self.log(
                "YAML configuration generation completed successfully. Summary - "
                f"File: {file_path}, Profiles: {len(final_list)}, "
                f"Auto-discovery: {generate_all}. Operation result set "
                "to 'success'.",
                "INFO"
            )
        else:
            self.log(
                f"YAML file write operation failed for file path: {file_path}. Check file "
                f"permissions, disk space, and path validity. Configurations ready but "
                f"not written: {len(final_list)}",
                "ERROR"
            )

            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

            self.log(
                "YAML configuration generation failed due to file write error. "
                "Operation result set to 'failed'. Returning instance with error state.",
                "ERROR"
            )

        return self

    def parse_profile_info(self, profile_info, profile_key):
        """
        Parses wireless profile component information into playbook format.

        This function transforms raw API response data for profile components (SSIDs,
        AP zones, feature templates, additional interfaces) into structured
        configurations compatible with network_profile_wireless_workflow_manager module
        by extracting component-specific fields, resolving ID references to names using
        helper APIs (dot11be profiles, interface VLANs), filtering null/empty values,
        and constructing playbook-ready dictionaries with snake_case keys for consistent
        YAML generation workflow.

        Args:
            profile_info (list | dict): Raw profile component data from API response
                                    containing component details in camelCase format.
            profile_key (str): Component type identifier determining parsing logic:
                            - "ssid_details": SSID configurations with fabric, VLAN,
                                interface, and anchor group settings
                            - "ap_zones": AP zone configurations with SSIDs and RF
                                profile mappings
                            - "feature_template_designs": Feature template designs with
                                SSID associations
                            - "additional_interfaces": Interface configurations with
                                VLAN ID mappings

        Returns:
            list | None: List of dictionaries containing parsed component configurations
                        with snake_case keys ready for YAML serialization. Returns None
                        if profile_info empty, profile_key invalid, or no valid
                        components parsed.
        """
        self.log(
            f"Starting profile information parsing for component type '{profile_key}'. Profile "
            f"data type: {type(profile_info).__name__}, Component determines "
            "field extraction and transformation "
            "logic for playbook compatibility.",
            "DEBUG"
        )

        if not (profile_info or profile_key):
            self.log(
                "Profile parsing skipped - missing required parameters. Profile info "
                f"provided: {bool(profile_info)}, Profile key provided: {bool(profile_key)}."
                " Both parameters required for "
                "parsing operation.",
                "WARNING"
            )
            return None

        if profile_key == "ssid_details" and isinstance(profile_info, list):
            self.log(
                f"Parsing SSID details component with {len(profile_info)} SSID item(s). Extracting SSID "
                "names, fabric settings, VLAN configurations, interface mappings, anchor "
                "groups, and flex connect settings for each SSID.",
                "DEBUG"
            )
            parsed_ssid = []
            ssids_processed = 0
            ssids_skipped = 0

            for ssid_index, ssid in enumerate(profile_info, start=1):
                self.log(
                    f"Processing SSID {ssid_index}/{len(profile_info)}. Extracting required and optional fields "
                    "for YAML configuration.",
                    "DEBUG"
                )

                each_parsed_ssid = {}
                ssid_name = ssid.get("ssidName")
                if ssid_name:
                    each_parsed_ssid["ssid_name"] = ssid_name

                    self.log(
                        f"SSID {ssid_index}/{len(profile_info)} name extracted: '{ssid_name}'."
                        " Proceeding with optional "
                        "field extraction.",
                        "DEBUG"
                    )
                else:
                    ssids_skipped += 1

                    self.log(
                        f"SSID {ssid_index}/{len(profile_info)} skipped - missing required 'ssidName' field. SSID "
                        f"data: {ssid}. Total SSIDs skipped: {ssids_skipped}",
                        "WARNING"
                    )
                    continue

                self.log(
                    f"Extracting dot11be profile for SSID '{ssid_name}'. Checking dot11beProfileId "
                    "field for profile ID to name resolution.",
                    "DEBUG"
                )
                dot11be_profile_id = ssid.get("dot11beProfileId")

                if dot11be_profile_id:
                    self.log(
                        f"dot11be profile ID found for SSID '{ssid_name}': {dot11be_profile_id}. Calling "
                        "get_dot11be_profile_by_id() to resolve profile name.",
                        "DEBUG"
                    )

                    dot11be_profile_name = self.get_dot11be_profile_by_id(dot11be_profile_id)

                    if dot11be_profile_name:
                        each_parsed_ssid["dot11be_profile_name"] = dot11be_profile_name

                        self.log(
                            f"dot11be profile name resolved for SSID '{ssid_name}':"
                            f" {dot11be_profile_name}. Added to "
                            "configuration.",
                            "DEBUG"
                        )
                    else:
                        self.log(
                            f"dot11be profile name resolution failed for SSID '{ssid_name}' with "
                            f"profile ID {dot11be_profile_id}. Field will be omitted from configuration.",
                            "WARNING"
                        )
                else:
                    self.log(
                        f"No dot11be profile ID found for SSID '{ssid_name}'. Skipping dot11be "
                        "profile name extraction.",
                        "DEBUG"
                    )

                self.log(
                    f"Extracting fabric enablement status for SSID '{ssid_name}'. Converting "
                    "enableFabric boolean to True/False for playbook compatibility.",
                    "DEBUG"
                )

                enable_fabric = ssid.get("enableFabric")
                each_parsed_ssid["enable_fabric"] = True if enable_fabric else False

                self.log(
                    f"Fabric status set to {each_parsed_ssid['enable_fabric']} for SSID '{ssid_name}'.",
                    "DEBUG"
                )

                self.log(
                    f"Extracting optional VLAN and interface configurations for SSID '{ssid_name}'. "
                    "Fields include vlanGroupName, interfaceName, anchorGroupName, and flex "
                    "connect settings.",
                    "DEBUG"
                )

                vlan_group_name = ssid.get("vlanGroupName")
                if vlan_group_name:
                    each_parsed_ssid["vlan_group_name"] = vlan_group_name

                    self.log(
                        f"VLAN group name '{vlan_group_name}' added for SSID '{ssid_name}'.",
                        "DEBUG"
                    )

                interface_name = ssid.get("interfaceName")
                if interface_name:
                    each_parsed_ssid["interface_name"] = interface_name

                    self.log(
                        f"Interface name '{interface_name}' added for SSID '{ssid_name}'.",
                        "DEBUG"
                    )

                anchor_group_name = ssid.get("anchorGroupName")
                if anchor_group_name:
                    each_parsed_ssid["anchor_group_name"] = anchor_group_name
                    self.log(
                        f"Anchor group name '{anchor_group_name}' added for SSID '{ssid_name}'.",
                        "DEBUG"
                    )

                self.log(
                    f"Extracting flex connect configuration for SSID '{ssid_name}'. Checking "
                    "enableFlexConnect and localToVlan settings.",
                    "DEBUG"
                )
                flex_connect = ssid.get("flexConnect", {}).get("enableFlexConnect")

                local_to_vlan = ssid.get("flexConnect", {}).get("localToVlan")
                if flex_connect:
                    each_parsed_ssid["local_to_vlan"] = local_to_vlan

                    self.log(
                        f"Flex connect enabled for SSID '{ssid_name}' with local_to_vlan: {local_to_vlan}.",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"Flex connect not enabled for SSID '{ssid_name}'. Skipping local_to_vlan "
                        "extraction.",
                        "DEBUG"
                    )

                ssids_processed += 1

                self.log(
                    f"SSID {ssid_index}/{len(profile_info)} '{ssid_name}' "
                    f"parsed successfully with {len(each_parsed_ssid)} field(s): {list(each_parsed_ssid.keys())}. "
                    f"Adding to parsed SSID list. Total SSIDs processed: {ssids_processed}",
                    "DEBUG"
                )

                parsed_ssid.append(each_parsed_ssid)

            self.log(
                f"SSID details parsing completed. Processed {ssids_processed}/{len(profile_info)}"
                f" SSID(s), skipped {ssids_skipped}. "
                f"Total parsed configurations: {len(parsed_ssid)}. Returning SSID list for YAML "
                "generation.",
                "INFO"
            )
            return parsed_ssid

        if profile_key == "ap_zones" and isinstance(profile_info, list):
            self.log(
                f"Parsing AP zone details component with {len(profile_info)} AP zone item(s). Extracting "
                "zone names, SSID associations, and RF profile mappings for each zone.",
                "DEBUG"
            )
            parsed_ap_zones = []
            zones_processed = 0
            zones_skipped = 0

            for zone_index, ap_zone in enumerate(profile_info, start=1):
                self.log(
                    f"Processing AP zone {zone_index}/{len(profile_info)}. Extracting required zone name and "
                    "optional SSID/RF profile fields.",
                    "DEBUG"
                )
                each_ap_zone = {}
                ap_zone_name = ap_zone.get("apZoneName")
                if not ap_zone_name:
                    zones_skipped += 1

                    self.log(
                        f"AP zone {zone_index}/{len(profile_info)} skipped - missing required 'apZoneName' field. "
                        f"Zone data: {ap_zone}. Total zones skipped: {zones_skipped}",
                        "WARNING"
                    )
                    continue

                each_ap_zone["ap_zone_name"] = ap_zone_name
                self.log(
                    f"AP zone {zone_index}/{len(profile_info)} name "
                    f"extracted: '{ap_zone_name}'. Proceeding with optional "
                    "field extraction.",
                    "DEBUG"
                )

                self.log(
                    f"Extracting SSID associations for AP zone '{ap_zone_name}'. Checking ssids list "
                    "for zone-specific SSID mappings.",
                    "DEBUG"
                )

                ssids = ap_zone.get("ssids", [])
                if ssids and isinstance(ssids, list):
                    each_ap_zone["ssids"] = ssids

                    self.log(
                        "AP zone '{0}' has {1} associated SSID(s): {2}. Added to "
                        "configuration.".format(ap_zone_name, len(ssids), ssids),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No SSID associations found for AP zone '{0}'. Zone will have no "
                        "SSID mappings in configuration.".format(ap_zone_name),
                        "DEBUG"
                    )

                self.log(
                    f"Extracting RF profile for AP zone '{ap_zone_name}'. Checking rfProfileName field "
                    "for radio frequency profile assignment.",
                    "DEBUG"
                )

                rf_profile_name = ap_zone.get("rfProfileName")
                if rf_profile_name:
                    each_ap_zone["rf_profile_name"] = rf_profile_name

                    self.log(
                        f"RF profile '{rf_profile_name}' added for AP zone '{ap_zone_name}'.",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"No RF profile found for AP zone '{ap_zone_name}'. RF profile field will be "
                        "omitted from configuration.",
                        "DEBUG"
                    )

                zones_processed += 1

                self.log(
                    f"AP zone {zone_index}/{len(profile_info)} '{ap_zone_name}' parsed "
                    f"successfully with {len(each_ap_zone)} field(s): {list(each_ap_zone.keys())}. "
                    f"Adding to parsed AP zone list. Total zones processed: {zones_processed}",
                    "DEBUG"
                )

                parsed_ap_zones.append(each_ap_zone)

            self.log(
                f"AP zone details parsing completed. Processed "
                f"{zones_processed}/{len(profile_info)} zone(s), skipped "
                f"{zones_skipped}. Total parsed configurations: "
                f"{len(parsed_ap_zones)}. Returning AP zone list for YAML "
                "generation.",
                "INFO"
            )

            return parsed_ap_zones

        if profile_key == "feature_template_designs" and isinstance(profile_info, list):
            self.log(
                f"Parsing feature template design details component with {len(profile_info)} template "
                "item(s). Extracting design names and SSID associations for each "
                "template.",
                "DEBUG"
            )

            parsed_feature_template = []
            templates_processed = 0
            templates_skipped = 0
            for template_index, feature_template in enumerate(profile_info, start=1):
                self.log(
                    f"Processing feature template {template_index}/{len(profile_info)}. "
                    f"Extracting design name and "
                    "optional SSID associations.",
                    "DEBUG"
                )

                each_feature_template = {}
                feature_templates = feature_template.get("designName")
                if feature_templates:
                    each_feature_template["feature_templates"] = [feature_templates]

                    self.log(
                        f"Feature template {template_index}/{len(profile_info)} "
                        f"design name extracted: '{feature_templates}'. Wrapping "
                        "in list format for playbook compatibility.",
                        "DEBUG"
                    )
                else:
                    templates_skipped += 1

                    self.log(
                        f"Feature template {template_index}/{len(profile_info)} "
                        "skipped - missing required 'designName' "
                        f"field. Template data: {feature_template}. "
                        f"Total templates skipped: {templates_skipped}",
                        "WARNING"
                    )
                    continue

                self.log(
                    f"Extracting SSID associations for feature template '{feature_templates}'. Checking "
                    "ssids list for template-specific SSID mappings.",
                    "DEBUG"
                )

                ssids = feature_template.get("ssids")
                if ssids and isinstance(ssids, list):
                    each_feature_template["ssids"] = ssids

                    self.log(
                        f"Feature template '{feature_templates}' has {len(ssids)}"
                        f" associated SSID(s): {ssids}. Added to "
                        "configuration.",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"No SSID associations found for feature template '{feature_templates}'. Template "
                        "will have no SSID mappings in configuration.",
                        "DEBUG"
                    )

                templates_processed += 1

                self.log(
                    f"Feature template {template_index}/{len(profile_info)} '{feature_templates}' "
                    f"parsed successfully with {len(each_feature_template)} field(s): "
                    f"{list(each_feature_template.keys())}. Adding to parsed feature template list. Total templates "
                    f"processed: {templates_processed}", "DEBUG"
                )

                parsed_feature_template.append(each_feature_template)

            self.log(
                f"Feature template details parsing completed. "
                f"Processed {templates_processed}/{len(profile_info)} template(s), "
                f"skipped {templates_skipped}. Total parsed configurations: "
                f"{len(parsed_feature_template)}. Returning feature template "
                "list for YAML generation.",
                "INFO"
            )

            return parsed_feature_template

        if profile_key == "additional_interfaces" and isinstance(profile_info, list):
            self.log(
                f"Parsing additional interface details component with {len(profile_info)} interface "
                "item(s). Extracting interface names and VLAN ID mappings for each "
                "interface.",
                "DEBUG"
            )

            parsed_interfaces = []
            interfaces_processed = 0
            interfaces_skipped = 0

            for interface_index, interface in enumerate(profile_info, start=1):
                self.log(
                    f"Processing additional interface {interface_index}/{len(profile_info)}: '{interface}'. Calling "
                    "get_additional_interface() to resolve VLAN ID.",
                    "DEBUG"
                )
                each_interface = {}
                vlan_id = self.get_additional_interface(interface)
                if vlan_id:
                    each_interface["interface_name"] = interface
                    each_interface["vlan_id"] = vlan_id

                    interfaces_processed += 1

                    self.log(
                        f"Interface {interface_index}/{len(profile_info)} '{interface}' "
                        f"resolved to VLAN ID {vlan_id}. Adding to parsed "
                        f"interface list. Total interfaces processed: {interfaces_processed}",
                        "DEBUG"
                    )

                    parsed_interfaces.append(each_interface)
                else:
                    interfaces_skipped += 1

                    self.log(
                        f"Interface {interface_index}/{len(profile_info)} "
                        f"'{interface}' skipped - VLAN ID resolution failed. "
                        f"get_additional_interface() returned None. Total interfaces "
                        f"skipped: {interfaces_skipped}",
                        "WARNING"
                    )

            self.log(
                "Additional interface details parsing completed. "
                f"Processed {interfaces_processed}/{len(profile_info)} "
                f"interface(s), skipped {interfaces_skipped}. "
                f"Total parsed configurations: {len(parsed_interfaces)}. Returning "
                "interface list for YAML generation.",
                "INFO"
            )

            return parsed_interfaces

        else:
            self.log(
                f"Profile parsing failed - unknown profile key '{profile_key}' or invalid data type "
                f"{type(profile_info).__name__}. Supported profile keys: ssid_details, ap_zones, "
                "feature_template_designs, additional_interfaces. Expected list type for "
                "profile_info.",
                "WARNING"
            )
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
        Retrieves VLAN ID for specified interface from Cisco Catalyst Center.

        This function resolves interface name to VLAN ID by executing API call to
        wireless interfaces endpoint with interface name parameter, extracting VLAN ID
        from first matching interface in paginated response, handling cases where
        interface not found or API response invalid, and logging interface details for
        network wireless profile configuration documentation in YAML generation workflow.

        Args:
            interface (str): Interface name to resolve VLAN ID for matching against
                            Catalyst Center wireless interface configurations.

        Returns:
            int | None: VLAN ID integer if interface found and valid response received.
                    Returns None if interface not found, response invalid, or API
                    call fails enabling graceful degradation in additional interface
                    parsing workflow.
        """
        self.log(
            f"Starting VLAN ID resolution for interface name '{interface}'. Constructing API "
            "request with pagination parameters (limit=500, offset=1) and interface "
            "name filter for wireless interface lookup.",
            "DEBUG"
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
            self.log(
                f"API response received for interface '{interface}'. "
                f"Response type: {type(interfaces).__name__}, "
                "Validating response structure for interface list extraction.",
                "DEBUG"
            )

            if interfaces and isinstance(interfaces.get("response"), list):
                if len(interfaces["response"]) > 0:
                    vlan_id = interfaces["response"][0].get("vlanId")

                    self.log(
                        f"VLAN ID extracted successfully for interface '{interface}': VLAN {vlan_id}. "
                        "Using first matching interface from response "
                        f"list with {len(interfaces['response'])} "
                        "total interface(s). Returning VLAN ID for additional interface "
                        "configuration.",
                        "DEBUG"
                    )
                    return vlan_id
                else:
                    self.log(
                        f"API response for interface '{interface}' contains empty interface list. "
                        "No matching interfaces found in Catalyst Center. Returning None "
                        "to skip this interface in configuration.",
                        "INFO"
                    )
                    return None
            else:
                self.log(
                    f"Invalid or empty API response received for interface '{interface}'. Response "
                    "validation failed - missing 'response' key or invalid type (expected "
                    f"list, got {type(interfaces.get('response')).__name__}). "
                    "Returning None to skip interface.",
                    "INFO"
                )
                return None
        except Exception as e:
            msg = (
                f"Exception occurred during VLAN ID resolution for interface '{interface}'. "
                f"Exception type: {type(e).__name__}, Exception message: {str(e)}. API call or response "
                "processing failed. Failing and exiting workflow."
            )
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

    def get_want(self, config, state):
        """
        Constructs desired state parameters for wireless profile operations.

        This function creates API call parameters based on specified state by validating
        input configuration against expected schema, processing global filters and
        generation flags, constructing yaml_config_generator parameters with file path
        and filter specifications, and populating want dictionary for downstream YAML
        generation workflow execution in get_diff_gathered operation.

        Args:
            config (dict): Configuration data containing:
                        - generate_all_configurations (bool, optional): Auto-discovery
                            mode flag for complete infrastructure extraction
                        - file_path (str, optional): Output YAML file path
                        - global_filters (dict, optional): Filter criteria with
                            profile_name_list, day_n_template_list, site_list,
                            ssid_list, ap_zone_list, feature_template_list,
                            additional_interface_list
            state (str): Desired state for operation, must be 'gathered' to construct parameters for
                         network wireless profile configuration extraction workflow.

        Returns:
            object: Self instance with updated attributes:
                    - self.want: Dictionary containing yaml_config_generator parameters
                    for API calls
                    - self.msg: Operation result message describing parameter collection
                    - self.status: Operation status set to "success"
        """
        self.log(
            "Starting desired state parameter construction for API calls with state "
            f"'{state}'. Workflow includes configuration validation, filter processing, and "
            "yaml_config_generator parameter preparation for network wireless profile config "
            "extraction.",
            "DEBUG"
        )

        self.validate_params(config)
        self.log(
            "Configuration validation completed successfully. Proceeding with want "
            "dictionary construction for yaml_config_generator parameters.",
            "DEBUG"
        )

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator parameters added to want "
            f"dictionary: {self.pprint(want['yaml_config_generator'])}. Dictionary "
            "contains complete configuration for YAML generation including filters and "
            "file path specifications.",
            "INFO"
        )

        self.want = want
        self.log(
            f"Desired state (want) constructed successfully with {len(self.want)} parameter key(s): "
            f"{list(self.want.keys())}. Want dictionary ready for get_diff_gathered operation execution.",
            "INFO"
        )
        self.msg = (
            "Successfully collected all parameters from the playbook for Network Profile "
            "wireless operations."
        )
        self.status = "success"
        self.log(
            "Parameter construction completed with status 'success'. Returning self "
            "instance with populated want dictionary for method chaining in workflow "
            "execution.",
            "DEBUG"
        )
        return self

    def get_have(self, config):
        """
        Retrieves current wireless profile state from Cisco Catalyst Center.

        This function fetches existing wireless profile configurations including profile
        details, CLI templates, site assignments, SSIDs, AP zones, feature templates,
        and additional interfaces by determining collection mode (auto-discovery vs
        filtered), collecting profile lists based on generation flags and filters,
        retrieving site and template details for matched profiles, and populating have
        dictionary with current state for YAML generation workflow.

        Args:
            config (dict): Configuration data containing:
                        - generate_all_configurations (bool, optional): Auto-discovery
                            mode flag enabling complete profile collection
                        - global_filters (dict, optional): Filter criteria with
                            profile_name_list, day_n_template_list, site_list, ssid_list,
                            ap_zone_list, feature_template_list, additional_interface_list
                            for targeted extraction

        Returns:
            object: Self instance with updated attributes:
                    - self.have: Dictionary containing current wireless profile state with
                    wireless_profile_names, wireless_profile_list, wireless_profile_info,
                    wireless_profile_templates, wireless_profile_sites
                    - self.msg: Operation result message describing retrieval status
                    - Operation completes with success status
        """
        self.log(
            "Starting current state retrieval for wireless profiles from Catalyst Center. "
            "Workflow includes mode determination (auto-discovery vs filtered), profile "
            "collection, site/template detail retrieval, and have dictionary population.",
            "DEBUG"
        )

        if not (config and isinstance(config, dict)):
            self.log(
                "Configuration not provided or invalid type (expected dict, got {0}). "
                "Skipping current state retrieval and returning empty have state.".format(
                    type(config).__name__
                ),
                "WARNING"
            )
            self.msg = "No configuration provided for current state retrieval."
            return self

        self.log(
            "Configuration received with type verification passed. Checking for "
            "generate_all_configurations flag to determine collection mode.",
            "DEBUG"
        )

        if config.get("generate_all_configurations", False):
            self.log(
                "Auto-discovery mode enabled (generate_all_configurations=True). "
                "Collecting all wireless profile details without filter restrictions for "
                "complete network wireless profile configuration extraction.",
                "INFO"
            )
            self.collect_all_wireless_profile_list()
            if not self.have.get("wireless_profile_names"):
                self.log(
                    "No wireless profiles found in Catalyst Center after collection. "
                    "wireless_profile_names list is empty. Setting success status and "
                    "returning with informational message.",
                    "INFO"
                )
                self.msg = "No existing wireless profiles found in Cisco Catalyst Center."
                self.status = "success"
                return self

            self.log(
                f"Wireless profiles collected successfully: {len(self.have.get('wireless_profile_names', []))} "
                "profile(s) found. "
                "Proceeding with site and template detail collection for all profiles.",
                "DEBUG"
            )

            self.collect_site_and_template_details(self.have.get("wireless_profile_names", []))
            self.log(
                "Auto-discovery mode collection completed. Total profiles processed: {0}. "
                "Site details collected for {1} profile(s), template details for {2} "
                "profile(s).".format(
                    len(self.have.get("wireless_profile_names", [])),
                    len(self.have.get("wireless_profile_sites", {})),
                    len(self.have.get("wireless_profile_templates", {}))
                ),
                "INFO"
            )

        else:
            self.log(
                "Checking for global_filters in configuration for targeted extraction mode. "
                "Filters enable selective profile collection based on criteria.",
                "DEBUG"
            )

            global_filters = config.get("global_filters")
            if global_filters:
                self.log(
                    f"Global filters provided: {global_filters}. Extracting filter criteria for profile "
                    "name list, day-N templates, sites, SSIDs, AP zones, feature templates, "
                    "and additional interfaces.",
                    "DEBUG"
                )
                profile_name_list = global_filters.get("profile_name_list", [])
                day_n_template_list = global_filters.get("day_n_template_list", [])
                site_list = global_filters.get("site_list", [])
                ssid_list = global_filters.get("ssid_list", [])
                ap_zone_list = global_filters.get("ap_zone_list", [])
                feature_template_list = global_filters.get("feature_template_list", [])
                additional_interface_list = global_filters.get("additional_interface_list", [])

                if profile_name_list and isinstance(profile_name_list, list):
                    self.log(
                        f"Profile name list filter provided with {len(profile_name_list)} "
                        f"profile(s): {profile_name_list}. "
                        "Collecting wireless profile details for specified profiles only.",
                        "INFO"
                    )
                    self.collect_all_wireless_profile_list(profile_name_list)
                    self.collect_site_and_template_details(self.have.get("wireless_profile_names", []))
                    self.log(
                        f"Profile name list filtering completed. "
                        f"Collected {len(self.have.get('wireless_profile_names', []))} matching "
                        "profile(s).",
                        "DEBUG"
                    )

                if (
                    day_n_template_list and isinstance(day_n_template_list, list) or
                    site_list and isinstance(site_list, list) or
                    ssid_list and isinstance(ssid_list, list) or
                    ap_zone_list and isinstance(ap_zone_list, list) or
                    feature_template_list and isinstance(feature_template_list, list) or
                    additional_interface_list and isinstance(additional_interface_list, list)
                ):
                    self.log(
                        "Component-based filters provided (day-N templates, sites, SSIDs, AP "
                        "zones, feature templates, or additional interfaces). Collecting all "
                        f"wireless profiles for subsequent filter matching: {global_filters}",
                        "INFO"
                    )
                    self.collect_all_wireless_profile_list()
                    self.collect_site_and_template_details(self.have.get("wireless_profile_names", []))
                    self.log(
                        "Component-based filtering preparation completed. "
                        f"Collected {len(self.have.get('wireless_profile_names', []))} total "
                        "profile(s) for filter matching in process_global_filters().",
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No global_filters provided in configuration. No additional profile "
                        "collection performed beyond auto-discovery mode processing.",
                        "DEBUG"
                    )

            self.log(
                "Current state (have) retrieval completed successfully. Have dictionary "
                "contains: wireless_profile_names ({0} entries), wireless_profile_list "
                "({1} entries), wireless_profile_info ({2} entries), "
                "wireless_profile_templates ({3} entries), wireless_profile_sites ({4} "
                "entries).".format(
                    len(self.have.get("wireless_profile_names", [])),
                    len(self.have.get("wireless_profile_list", [])),
                    len(self.have.get("wireless_profile_info", {})),
                    len(self.have.get("wireless_profile_templates", {})),
                    len(self.have.get("wireless_profile_sites", {}))
                ),
                "INFO"
            )

        self.msg = "Successfully retrieved the details from the system"

        self.log(
            "Returning self instance with populated have dictionary for YAML generation "
            "workflow. Current state ready for diff calculation in get_diff_gathered.",
            "DEBUG"
        )
        return self

    def get_diff_gathered(self):
        """
        Executes YAML configuration generation workflow for gathered state.

        This function orchestrates complete YAML playbook generation workflow by
        iterating through defined operations (yaml_config_generator), checking for
        operation parameters in want dictionary, executing operation functions with
        parameter validation, tracking execution timing for performance monitoring,
        and handling operation status checking for error propagation throughout the
        workflow execution lifecycle.

        Args:
            None: Uses self.want dictionary populated by get_want() containing
                yaml_config_generator parameters for operation execution.

        Returns:
            object: Self instance with updated attributes:
                    - self.msg: Operation result message from yaml_config_generator
                    - self.status: Operation status ("success", "failed", or "ok")
                    - self.result: Complete operation result with file path and summary
                    - Operation timing logged for performance analysis
        """
        self.log(
            "Starting gathered state workflow execution for YAML playbook generation. "
            "Workflow orchestrates yaml_config_generator operation by checking want "
            "dictionary for parameters, executing generation function, validating "
            "operation status, and tracking execution timing for performance monitoring.",
            "DEBUG"
        )

        start_time = time.time()
        self.log(
            f"Workflow execution start time captured: {start_time}. Timing metrics will track "
            "complete operation duration from parameter checking through YAML file "
            "generation for performance analysis and optimization.",
            "DEBUG"
        )

        operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]

        # Iterate over operations and process them
        operations_executed = 0
        operations_skipped = 0

        self.log(
            "Initializing operation execution counters. Counters track successful "
            "executions and skipped operations for workflow summary reporting.",
            "DEBUG"
        )

        for operation_index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                f"Processing operation {operation_index}/{len(operations)}: "
                f"'{operation_name}' with parameter key '{param_key}'. "
                "Checking want dictionary for operation parameters to determine if "
                "execution should proceed or skip this operation.",
                "DEBUG"
            )

            params = self.want.get(param_key)
            if params:
                self.log(
                    f"Operation {operation_index}/{len(operations)} '{operation_name}' "
                    "parameters found in want dictionary. "
                    "Starting operation execution with parameter validation and status "
                    "checking for error propagation. Parameters will be passed to "
                    f"{operation_func.__name__}() function.",
                    "INFO"
                )

                self.log(
                    f"Executing operation function {operation_func.__name__}() "
                    "with parameters. Function will "
                    "perform YAML generation workflow including file path determination, "
                    "configuration retrieval, data transformation, and file writing. "
                    "check_return_status() will validate operation result.",
                    "DEBUG"
                )

                try:
                    operation_func(params).check_return_status()
                    operations_executed += 1

                    self.log(
                        f"Operation {operation_index}/{len(operations)} '{operation_name}' "
                        "completed successfully. "
                        "check_return_status() validation passed without errors. "
                        "Operation result available in self.result for final module "
                        f"output. Total operations executed: {operations_executed}",
                        "INFO"
                    )

                except Exception as e:
                    self.log(
                        f"Operation {operation_index}/{len(operations)} '{operation_name}' "
                        f"failed with exception: {str(e)}. Exception "
                        f"type: {type(e).__name__}. Setting operation result to 'failed' and propagating "
                        "error through check_return_status() for immediate workflow "
                        "termination.",
                        "ERROR"
                    )

                    self.set_operation_result(
                        "success", False,
                        self.msg,
                        "ERROR",
                        f"{operation_name} operation failed: {str(e)}"
                    ).check_return_status()
            else:
                operations_skipped += 1

                self.log(
                    f"Operation {operation_index}/{len(operations)} '{operation_name}' "
                    "skipped - no parameters found in want "
                    f"dictionary for parameter key '{param_key}'. This operation will not "
                    "execute in current workflow iteration. Total operations skipped: "
                    f"{operations_skipped}"
                )

        end_time = time.time()
        execution_duration = end_time - start_time

        self.log(
            "Gathered state workflow execution completed successfully. Total execution "
            f"time: {execution_duration:.2f} seconds. Workflow processed {len(operations)} "
            f"operation(s): {operations_executed} executed, "
            f"{operations_skipped} skipped. Operation results available in self.result for module exit.",
            "INFO"
        )

        self.log(
            f"Performance metrics - Start time: {start_time}, End time: {end_time}, "
            f"Duration: {execution_duration:.2f}s, "
            f"Operations executed: {operations_executed}, Operations skipped: {operations_skipped}. "
            "Metrics provide timing "
            "analysis for workflow optimization and performance monitoring.",
            "DEBUG"
        )

        self.log(
            "Returning self instance for method chaining. Instance contains complete "
            "operation results with msg, status, result attributes populated by "
            "yaml_config_generator execution for module exit and user feedback.",
            "DEBUG"
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center network wireless profile playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for network wireless profile playbook configuration.
    Purpose:
        Initializes and executes the network wireless profile playbook generator
        workflow to extract existing network configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create NetworkProfileWirelessPlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 2.3.7.9)
        5. Validate and sanitize state parameter
        6. Execute input parameter validation
        7. Process each configuration item in the playbook
        8. Execute state-specific operations (gathered workflow)
        9. Return results via module.exit_json()

    Module Arguments:
        Connection Parameters:
            - dnac_host (str, required): Catalyst Center hostname/IP
            - dnac_port (str, default="443"): HTTPS port
            - dnac_username (str, default="admin"): Authentication username
            - dnac_password (str, required, no_log): Authentication password
            - dnac_verify (bool, default=True): SSL certificate verification

        API Configuration:
            - dnac_version (str, default="2.2.3.3"): Catalyst Center version
            - dnac_api_task_timeout (int, default=1200): API timeout (seconds)
            - dnac_task_poll_interval (int, default=2): Poll interval (seconds)
            - validate_response_schema (bool, default=True): Schema validation

        Logging Configuration:
            - dnac_debug (bool, default=False): Debug mode
            - dnac_log (bool, default=False): Enable file logging
            - dnac_log_level (str, default="WARNING"): Log level
            - dnac_log_file_path (str, default="dnac.log"): Log file path
            - dnac_log_append (bool, default=True): Append to log file

        Playbook Configuration:
            - config (list[dict], required): Configuration parameters list
            - state (str, default="gathered", choices=["gathered"]): Workflow state

    Version Requirements:
        - Minimum Catalyst Center version: 2.3.7.9
        - Introduced APIs for network profile wireless retrieval:
            * Network Wireless Profile list (retrieves_the_list_of_network_profiles_for_sites_v1)
            * Profile assigned to sites (retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1)
            * All available CLI templates (gets_the_templates_available_v1)
            * CLI Templates attached to the profiles (retrieve_cli_templates_attached_to_a_network_profile_v1)
            * Wireless profile details (get_wireless_profile)
            * Interface details (get_interfaces)

    Supported States:
        - gathered: Extract existing network profile wireless and generate YAML playbook
        - Future: merged, deleted, replaced (reserved for future use)

    Error Handling:
        - Version compatibility failures: Module exits with error
        - Invalid state parameter: Module exits with error
        - Input validation failures: Module exits with error
        - Configuration processing errors: Module exits with error
        - All errors are logged and returned via module.fail_json()

    Return Format:
        Success: module.exit_json() with result containing:
            - changed (bool): Whether changes were made
            - msg (str): Operation result message
            - response (dict): Detailed operation results
            - operation_summary (dict): Execution statistics

        Failure: module.fail_json() with error details:
            - failed (bool): True
            - msg (str): Error message
            - error (str): Detailed error information
    """
    # Record module initialization start time for performance tracking
    module_start_time = time.time()

    # Define the specification for the module's arguments
    # This structure defines all parameters accepted by the module with their types,
    # defaults, and validation rules
    element_spec = {
        # ============================================
        # Catalyst Center Connection Parameters
        # ============================================
        "dnac_host": {
            "required": True,
            "type": "str"
        },
        "dnac_port": {
            "type": "str",
            "default": "443"
        },
        "dnac_username": {
            "type": "str",
            "default": "admin",
            "aliases": ["user"]
        },
        "dnac_password": {
            "type": "str",
            "no_log": True  # Prevent password from appearing in logs
        },
        "dnac_verify": {
            "type": "bool",
            "default": True
        },

        # ============================================
        # API Configuration Parameters
        # ============================================
        "dnac_version": {
            "type": "str",
            "default": "2.2.3.3"
        },
        "dnac_api_task_timeout": {
            "type": "int",
            "default": 1200
        },
        "dnac_task_poll_interval": {
            "type": "int",
            "default": 2
        },
        "validate_response_schema": {
            "type": "bool",
            "default": True
        },

        # ============================================
        # Logging Configuration Parameters
        # ============================================
        "dnac_debug": {
            "type": "bool",
            "default": False
        },
        "dnac_log_level": {
            "type": "str",
            "default": "WARNING"
        },
        "dnac_log_file_path": {
            "type": "str",
            "default": "dnac.log"
        },
        "dnac_log_append": {
            "type": "bool",
            "default": True
        },
        "dnac_log": {
            "type": "bool",
            "default": False
        },

        # ============================================
        # Playbook Configuration Parameters
        # ============================================
        "config": {
            "required": True,
            "type": "list",
            "elements": "dict"
        },
        "state": {
            "default": "gathered",
            "choices": ["gathered"]
        },
    }

    # Initialize the Ansible module with argument specification
    # supports_check_mode=True allows module to run in check mode (dry-run)
    module = AnsibleModule(
        argument_spec=element_spec,
        supports_check_mode=True
    )

    # Create initial log entry with module initialization timestamp
    # Note: Logging is not yet available since object isn't created
    initialization_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_start_time)
    )

    # Initialize the NetworkProfileWirelessPlaybookGenerator object
    # This creates the main orchestrator for network profile wireless config extraction
    ccc_network_profile_wireless_playbook_generator = NetworkProfileWirelessPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_network_profile_wireless_playbook_generator.log(
        "Starting Ansible module execution for network profile wireless playbook config"
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_network_profile_wireless_playbook_generator.log(
        "Module initialized with parameters: dnac_host={0}, dnac_port={1}, "
        "dnac_username={2}, dnac_verify={3}, dnac_version={4}, state={5}, "
        "config_items={6}".format(
            module.params.get("dnac_host"),
            module.params.get("dnac_port"),
            module.params.get("dnac_username"),
            module.params.get("dnac_verify"),
            module.params.get("dnac_version"),
            module.params.get("state"),
            len(module.params.get("config", []))
        ),
        "DEBUG"
    )

    # ============================================
    # Version Compatibility Check
    # ============================================
    ccc_network_profile_wireless_playbook_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.7.9 for network wireless profile APIs".format(
            ccc_network_profile_wireless_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    if (ccc_network_profile_wireless_playbook_generator.compare_dnac_versions(
            ccc_network_profile_wireless_playbook_generator.get_ccc_version(), "2.3.7.9") < 0):

        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for Network profile wireless module. Supported versions start "
            "from '2.3.7.9' onwards. Version '2.3.7.9' introduces APIs for retrieving "
            "network profile wireless including SSIDs, interfaces, AP zones, feature templates, "
            "additional interfaces, and the following global filters: profile_name_list, "
            "day_n_template_list, site_list, ssid_list, ap_zone_list, feature_template_list, "
            "and additional_interface_list from the Catalyst Center.".format(
                ccc_network_profile_wireless_playbook_generator.get_ccc_version()
            )
        )

        ccc_network_profile_wireless_playbook_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_network_profile_wireless_playbook_generator.msg = error_msg
        ccc_network_profile_wireless_playbook_generator.set_operation_result(
            "failed", False, ccc_network_profile_wireless_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_network_profile_wireless_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required network profile wireless APIs".format(
            ccc_network_profile_wireless_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_network_profile_wireless_playbook_generator.params.get("state")

    ccc_network_profile_wireless_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_network_profile_wireless_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_network_profile_wireless_playbook_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_network_profile_wireless_playbook_generator.supported_states
            )
        )

        ccc_network_profile_wireless_playbook_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_network_profile_wireless_playbook_generator.status = "invalid"
        ccc_network_profile_wireless_playbook_generator.msg = error_msg
        ccc_network_profile_wireless_playbook_generator.check_return_status()

    ccc_network_profile_wireless_playbook_generator.log(
        "State validation passed - using state '{0}' for workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_network_profile_wireless_playbook_generator.log(
        "Starting comprehensive input parameter validation for playbook configuration",
        "INFO"
    )

    ccc_network_profile_wireless_playbook_generator.validate_input().check_return_status()

    ccc_network_profile_wireless_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = ccc_network_profile_wireless_playbook_generator.validated_config

    ccc_network_profile_wireless_playbook_generator.log(
        "Starting configuration processing loop - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        ccc_network_profile_wireless_playbook_generator.log(
            "Processing configuration item {0}/{1} for state '{2}'".format(
                config_index, len(config_list), state
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_network_profile_wireless_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_network_profile_wireless_playbook_generator.reset_values()
        # Collect desired state (want) from configuration
        ccc_network_profile_wireless_playbook_generator.log(
            "Collecting desired state parameters from configuration item {0}".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_network_profile_wireless_playbook_generator.get_want(
            config, state
        ).check_return_status()

        ccc_network_profile_wireless_playbook_generator.get_have(
            config).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_network_profile_wireless_playbook_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1}".format(state, config_index),
            "INFO"
        )
        ccc_network_profile_wireless_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_network_profile_wireless_playbook_generator.log(
            "Successfully completed processing for configuration item {0}/{1}".format(
                config_index, len(config_list)
            ),
            "INFO"
        )

    # ============================================
    # Module Completion and Exit
    # ============================================
    module_end_time = time.time()
    module_duration = module_end_time - module_start_time

    completion_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_end_time)
    )

    ccc_network_profile_wireless_playbook_generator.log(
        "Module execution completed successfully at timestamp {0}. Total execution "
        "time: {1:.2f} seconds. Processed {2} configuration item(s) with final "
        "status: {3}".format(
            completion_timestamp,
            module_duration,
            len(config_list),
            ccc_network_profile_wireless_playbook_generator.status
        ),
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_network_profile_wireless_playbook_generator.log(
        "Exiting Ansible module with result: {0}".format(
            ccc_network_profile_wireless_playbook_generator.result
        ),
        "DEBUG"
    )

    module.exit_json(**ccc_network_profile_wireless_playbook_generator.result)


if __name__ == "__main__":
    main()

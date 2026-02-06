#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Access Point workflow Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: brownfield_accesspoint_playbook_generator
short_description: >-
  Generate YAML configurations playbook for
  'accesspoint_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the
    'accesspoint_workflow_manager' module, reducing
    the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
  - Supports complete brownfield infrastructure discovery by
    collecting all access point configurations from Cisco Catalyst Center.
  - Enables targeted extraction using filters (site hierarchies,
    provisioned hostnames, AP configurations, or MAC addresses).
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
        with the 'brownfield_accesspoint_playbook_generator'
        module.
      - Filters specify which components to include in the YAML
        configuration file.
      - Either 'generate_all_configurations' or 'global_filters'
        must be specified to identify target access points.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML
            configurations for all access point provisioning and
            configuration features.
          - This mode discovers all managed access points in Cisco
            Catalyst Center and extracts all supported
            configurations.
          - When enabled, the config parameter becomes optional
            and will use default values if not provided.
          - A default filename will be generated automatically
            if file_path is not specified.
          - This is useful for complete brownfield infrastructure
            discovery and documentation.
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
            'accesspoint_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml'.
          - For example,
            'accesspoint_workflow_manager_playbook_2025-04-22_21-43-26.yml'.
          - Supports both absolute and relative file paths.
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML
            configuration file.
          - These filters apply to all components unless overridden
            by component-specific filters.
          - At least one filter type must be specified to identify
            target access points.
          - Filter priority (highest to lowest) is site_list,
            provision_hostname_list, accesspoint_config_list,
            accesspoint_provision_config_list,
            accesspoint_provision_config_mac_list.
          - Only the highest priority filter with valid data will
            be processed.
        type: dict
        required: false
        suboptions:
          site_list:
            description:
              - List of floor site hierarchies to extract AP
                configurations from.
              - HIGHEST PRIORITY - Used first if provided with
                valid data.
              - Site hierarchies must match those registered
                in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all access
                point configurations.
              - Example ["Global/USA/SAN JOSE/SJ_BLD20/FLOOR1",
                "Global/USA/SAN JOSE/SJ_BLD20/FLOOR2"]
              - Module will extract APs provisioned to these
                specific floor sites.
            type: list
            elements: str
            required: false
          provision_hostname_list:
            description:
              - List of access point hostnames with provisioned
                configurations to the floor.
              - MEDIUM-HIGH PRIORITY - Only used if site_list
                is not provided.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all provisioned
                access points.
              - Example ["test_ap_1", "test_ap_2"]
              - Retrieves provisioning details for specified AP
                hostnames.
            type: list
            elements: str
            required: false
          accesspoint_config_list:
            description:
              - List of access point hostnames to extract
                configurations from.
              - MEDIUM PRIORITY - Only used if site_list and
                provision_hostname_list are not provided.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all configured
                access points.
              - Example ["Test_ap_1", "Test_ap_2"]
              - Retrieves AP configuration details for specified
                hostnames.
            type: list
            elements: str
            required: false
          accesspoint_provision_config_list:
            description:
              - List of access point hostnames assigned to floors
                with both provisioning and configuration data.
              - MEDIUM-LOW PRIORITY - Only used if higher priority
                filters are not provided.
              - Case-sensitive and must be exact matches.
              - Example ["Test_ap_1", "Test_ap_2"]
              - Retrieves combined provisioning and configuration
                details.
            type: list
            elements: str
            required: false
          accesspoint_provision_config_mac_list:
            description:
              - List of access point MAC addresses assigned to
                floors with provisioning and configuration data.
              - LOWEST PRIORITY - Only used if no other filters
                are provided.
              - Case-sensitive and must be exact matches.
              - Example ["a4:88:73:d4:dd:80", "a4:88:73:d4:dd:81"]
              - Retrieves AP details by MAC address filtering.
            type: list
            elements: str
            required: false
requirements:
  - dnacentersdk >= 2.10.10
  - python >= 3.9
notes:
  - This module utilizes the following SDK methods
    devices.get_device_list
    wireless.get_access_point_configuration
    sites.get_site
    sda.get_device_info
    sites.assign_devices_to_site
    wireless.ap_provision
    wireless.configure_access_points
    sites.get_membership
  - The following API paths are used
    GET /dna/intent/api/v1/network-device
    GET /dna/intent/api/v1/site
    GET /dna/intent/api/v1/business/sda/device
    GET /dna/intent/api/v1/membership/{siteId}
  - Minimum Cisco Catalyst Center version required is 2.3.5.3 for
    YAML playbook generation support.
  - Filter priority hierarchy ensures only one filter type is
    processed per execution.
  - Module creates YAML file compatible with
    'accesspoint_workflow_manager' module for
    automation workflows.
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Access Point provision and configuration
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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

- name: Auto-generate YAML Configuration for all Access Point provision and configuration with custom file path
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
      - file_path: "tmp/brownfield_accesspoint_workflow_playbook.yml"
        generate_all_configurations: true

- name: Generate YAML Configuration with file path based on site list filters
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
      - file_path: "tmp/brownfield_accesspoint_workflow_playbook_site_base.yml"
        global_filters:
          site_list:
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR1
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR2

- name: Generate YAML provision config with file path based on hostname list filters
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          provision_hostname_list:
            - test_ap_1
            - test_ap_2

- name: Generate YAML Configuration with file path based on hostname list
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          accesspoint_config_list:
            - Test_ap_1
            - Test_ap_2

- name: Generate YAML provision and configuration with default file path based on hostname list
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          accesspoint_provision_config_list:
            - Test_ap_1
            - Test_ap_2

- name: Generate YAML accesspoint provision Configuration based on MAC Address list
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          accesspoint_provision_config_mac_list:
            - a4:88:73:d4:dd:80
            - a4:88:73:d4:dd:81
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
         'accesspoint_workflow_manager'.": {
            "file_path":
             "tmp/brownfield_accesspoint_workflow_playbook_templatebase.yml"
          }
        },
      "msg": {
        "YAML config generation Task succeeded for module
         'accesspoint_workflow_manager'.": {
            "file_path":
             "tmp/brownfield_accesspoint_workflow_playbook_templatebase.yml"
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
                   module 'accesspoint_workflow_manager'.
                   Verify input filters or configuration.",
      "msg": "No configurations or components to process for module
              'accesspoint_workflow_manager'.
              Verify input filters or configuration."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
import time
import copy

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
from collections import OrderedDict


if HAS_YAML:
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class AccessPointPlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.module_name = "accesspoint_workflow_manager"
        self.module_schema = self.get_workflow_elements_schema()
        self.log("Initialized AccessPointPlaybookGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False
        self.have["devices_details"], self.have["all_ap_config"], self.have["all_detailed_config"] = [], [], []
        self.have["all_provision_config"], self.have["unprocessed"] = [], []

    def validate_input(self):
        """
        Validates the input configuration parameters for the brownfield access point playbook.

        This function performs comprehensive validation of playbook configuration parameters,
        ensuring all inputs meet schema requirements, type constraints, and business logic
        rules before processing. It validates structure, allowed keys, minimum requirements,
        and filter configurations.

        Args:
            None (uses self.config from class instance)

        Returns:
            object: Self instance with updated attributes:
                - self.status: "success" or "failed" validation status
                - self.msg: Detailed validation result message
                - self.validated_config: Validated and normalized configuration list

        Side Effects:
            - Calls validate_list_of_dicts() for schema validation
            - Calls validate_minimum_requirements() for business logic validation
            - Calls set_operation_result() to update operation status
            - Logs validation progress at DEBUG, INFO, ERROR levels

        Validation Steps:
            1. Check configuration availability (empty config is valid)
            2. Define expected schema with allowed parameters
            3. Validate each config item is a dictionary
            4. Check for invalid/unknown parameter keys
            5. Validate minimum requirements (generate_all or global_filters)
            6. Perform schema-based validation (types, defaults, required fields)
            7. Validate global_filters structure if provided
            8. Ensure at least one filter list has values
            9. Validate filter values are lists of strings
            10. Store validated configuration and return success

        Allowed Parameters:
            - generate_all_configurations (bool, optional, default=False):
                Auto-generate for all access points
            - file_path (str, optional):
                Custom output path for YAML file
            - global_filters (dict, optional):
                Filter criteria for targeted extraction

        Global Filters Structure:
            - site_list (list[str]): Floor site hierarchies
            - provision_hostname_list (list[str]): Provisioned AP hostnames
            - accesspoint_config_list (list[str]): AP configuration hostnames
            - accesspoint_provision_config_list (list[str]): Combined provision/config hostnames
            - accesspoint_provision_config_mac_list (list[str]): AP MAC addresses

        Error Conditions:
            - Configuration item not a dictionary → TYPE ERROR
            - Invalid parameter keys found → INVALID PARAMS ERROR
            - No generate_all and no global_filters → MISSING REQUIREMENT ERROR
            - Invalid parameter types in schema validation → TYPE VALIDATION ERROR
            - global_filters not a dictionary → STRUCTURE ERROR
            - No valid filter lists with values → EMPTY FILTERS ERROR
            - Filter value not a list → FILTER TYPE ERROR

        Notes:
            - Empty configuration (self.config is None/empty) returns success
            - validate_list_of_dicts applies type coercion and defaults
            - Filter priority not validated here (handled in process_global_filters)
            - At least one filter must have values when global_filters provided
        """
        self.log(
            "Starting comprehensive input validation for brownfield access point playbook "
            "configuration. Validation will check parameter structure, types, and business "
            "logic constraints before proceeding with AP configuration extraction workflow.",
            "INFO"
        )

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = (
                "Configuration is not available in the playbook for validation. Empty "
                "configuration is valid - module will use defaults if invoked."
            )
            self.log(self.msg, "INFO")
            return self

        self.log(
            f"Configuration provided with {len(self.config)} item(s). Starting detailed "
            f"validation process for each configuration item.",
            "INFO"
        )

        # Expected schema for configuration parameters
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
            f"Defined validation schema with {len(allowed_keys)} allowed parameter(s): "
            f"{list(allowed_keys)}. Any parameters outside this set will trigger validation error.",
            "DEBUG"
        )

        # Validate that only allowed keys are present in each configuration item
        self.log(
            "Starting per-item key validation to check for invalid/unknown parameters.",
            "DEBUG"
        )

        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                f"Validating configuration item {config_index}/{len(self.config)} for type "
                f"and allowed keys.",
                "DEBUG"
            )

            if not isinstance(config_item, dict):
                self.msg = (
                    f"Configuration item {config_index}/{len(self.config)} must be a dictionary, "
                    f"got: {type(config_item).__name__}. Each configuration entry must be a "
                    f"dictionary with valid parameters."
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Check for invalid keys
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            if invalid_keys:
                self.msg = (
                    f"Invalid parameters found in playbook configuration: {list(invalid_keys)}. "
                    f"Only the following parameters are allowed: {list(allowed_keys)}. "
                    f"Please remove the invalid parameters and try again."
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                f"Configuration item {config_index}/{len(self.config)} passed key validation. "
                f"All keys are valid.",
                "DEBUG"
            )

        self.log(
            f"Completed per-item key validation. All {len(self.config)} configuration item(s) "
            f"have valid parameter keys.",
            "INFO"
        )

        # Validate minimum requirements (generate_all or global_filters)
        self.log(
            "Validating minimum requirements to ensure either generate_all_configurations "
            "or global_filters is provided.",
            "DEBUG"
        )

        try:
            self.validate_minimum_requirements(self.config)
            self.log(
                "Minimum requirements validation passed. Configuration has either "
                "generate_all_configurations or valid global_filters.",
                "INFO"
            )
        except Exception as e:
            self.msg = (
                f"Minimum requirements validation failed: {str(e)}. Please ensure either "
                f"generate_all_configurations is true or global_filters is provided with "
                f"at least one filter list."
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Perform schema-based validation using validate_list_of_dicts
        self.log(
            f"Starting schema-based validation using validate_list_of_dicts(). Validating "
            f"parameter types, defaults, and required fields against schema: {temp_spec}",
            "DEBUG"
        )

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        self.log(
            f"Schema validation completed. Valid configurations: "
            f"{len(valid_temp) if valid_temp else 0}, Invalid parameters: {bool(invalid_params)}",
            "DEBUG"
        )

        if invalid_params:
            self.msg = (
                f"Invalid parameters found during schema validation: {invalid_params}. Please check "
                f"parameter types and values. Expected types: generate_all_configurations "
                f"(bool), file_path (str), global_filters (dict)."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Validate global_filters structure if provided
        self.log(
            "Validating global_filters structure for configuration items that include filters.",
            "DEBUG"
        )

        for config_index, config_item in enumerate(valid_temp, start=1):
            global_filters = config_item.get("global_filters")

            if global_filters:
                self.log(
                    f"Configuration item {config_index}/{len(valid_temp)} has global_filters. "
                    f"Validating filter structure.",
                    "DEBUG"
                )

                if not isinstance(global_filters, dict):
                    self.msg = (
                        f"global_filters in configuration item {config_index}/{len(valid_temp)} "
                        f"must be a dictionary, got: {type(global_filters).__name__}. Please "
                        f"provide global_filters as a dictionary with filter lists."
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Check that at least one filter list is provided and has values
                valid_filter_keys = [
                    "site_list",
                    "provision_hostname_list",
                    "accesspoint_config_list",
                    "accesspoint_provision_config_list",
                    "accesspoint_provision_config_mac_list"
                ]
                provided_filters = {
                    key: global_filters.get(key)
                    for key in valid_filter_keys
                    if global_filters.get(key)
                }

                if not provided_filters:
                    self.msg = (
                        f"global_filters in configuration item {config_index}/{len(valid_temp)} "
                        f"provided but no valid filter lists have values. At least one of the "
                        f"following must be provided: {valid_filter_keys}. Please add at least "
                        f"one filter list with values."
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Validate that filter values are lists
                for filter_key, filter_value in provided_filters.items():
                    if not isinstance(filter_value, list):
                        self.msg = (
                            f"global_filters.{filter_key} in configuration item "
                            f"{config_index}/{len(valid_temp)} must be a list, got: "
                            f"{type(filter_value).__name__}. Please provide filter as a list "
                            f"of strings."
                        )
                        self.log(self.msg, "ERROR")
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                self.log(
                    f"Configuration item {config_index}/{len(valid_temp)} global_filters "
                    f"structure validated successfully. Provided filters: "
                    f"{list(provided_filters.keys())}",
                    "INFO"
                )
            else:
                self.log(
                    f"Configuration item {config_index}/{len(valid_temp)} does not have "
                    f"global_filters. Assuming generate_all_configurations mode.",
                    "DEBUG"
                )

        # Set validated configuration and return success
        self.validated_config = valid_temp

        self.msg = (
            f"Successfully validated {len(valid_temp)} configuration item(s) for access point "
            f"playbook generation. Validated configuration: {str(valid_temp)}"
        )

        self.log(
            f"Input validation completed successfully. Total items validated: {len(valid_temp)}, "
            f"Items with generate_all: "
            f"{sum(1 for item in valid_temp if item.get('generate_all_configurations'))}, "
            f"Items with global_filters: {sum(1 for item in valid_temp if item.get('global_filters'))}",
            "INFO"
        )

        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def validate_params(self, config):
        """
        Validates individual configuration parameters for brownfield access point generation.

        This function performs detailed validation of configuration parameters including
        file path validation and directory creation. It ensures the output file path is
        accessible and creates necessary directories if they don't exist.

        Args:
            config (dict): Configuration parameters dictionary containing:
                          - file_path (str, optional): Custom output path for YAML file
                          - generate_all_configurations (bool, optional): Auto-generate flag
                          - global_filters (dict, optional): Filter criteria

        Returns:
            object: Self instance with updated attributes:
                   - self.status: "success" or "failed" validation status
                   - self.msg: Detailed validation result or error message

        Side Effects:
            - Creates directories using os.makedirs() if file_path directory doesn't exist
            - Logs validation progress at DEBUG, INFO, ERROR levels
            - Updates self.status with validation result

        Validation Steps:
            1. Check configuration is not empty/None
            2. Extract and validate file_path if provided
            3. Check if parent directory exists
            4. Create directory structure if needed (with error handling)
            5. Return success status

        Error Conditions:
            - Empty/None configuration → EMPTY CONFIG ERROR
            - Directory creation fails → DIRECTORY CREATION ERROR

        Notes:
            - If no file_path provided, validation passes (default filename will be generated later)
            - Uses os.makedirs(exist_ok=True) to handle concurrent directory creation safely
            - Parent directory validation only occurs if file_path is provided
            - Validates accessibility but not write permissions (handled during actual write)
        """
        self.log(
            f"Starting validation of configuration parameters for access point playbook generation. "
            f"Configuration contains {len(config.keys()) if config else 0} parameter(s). Will "
            f"validate file path accessibility and create necessary directories if needed.",
            "DEBUG"
        )

        # Check for required parameters
        if not config:
            self.msg = (
                "Configuration cannot be empty. At least one parameter (generate_all_configurations "
                "or global_filters) must be provided for playbook generation."
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.log(
            f"Configuration validation passed basic checks. Configuration keys: {list(config.keys())}",
            "DEBUG"
        )

        # Validate file_path if provided
        file_path = config.get("file_path")

        if file_path:
            self.log(
                f"Custom file_path provided: '{file_path}'. Validating path accessibility and "
                f"checking if parent directory exists or needs to be created.",
                "INFO"
            )

            import os
            directory = os.path.dirname(file_path)

            if directory:
                self.log(
                    f"Extracted parent directory from file_path: '{directory}'. Checking if "
                    f"directory exists in filesystem.",
                    "DEBUG"
                )

                if not os.path.exists(directory):
                    self.log(
                        f"Parent directory '{directory}' does not exist. Attempting to create "
                        f"directory structure with os.makedirs().",
                        "INFO"
                    )

                    try:
                        os.makedirs(directory, exist_ok=True)
                        self.log(
                            f"Successfully created directory: '{directory}'. File path validation "
                            f"completed - YAML output will be written to '{file_path}'.",
                            "INFO"
                        )
                    except Exception as e:
                        self.msg = (
                            f"Cannot create directory for file_path: '{directory}'. Error: {str(e)}. "
                            f"Please verify you have write permissions and the path is valid."
                        )
                        self.log(self.msg, "ERROR")
                        self.status = "failed"
                        return self
                else:
                    self.log(
                        f"Parent directory '{directory}' already exists. File path validation "
                        f"passed - YAML output will be written to '{file_path}'.",
                        "DEBUG"
                    )
            else:
                self.log(
                    f"No parent directory specified in file_path ('{file_path}'). File will be "
                    f"created in current working directory.",
                    "DEBUG"
                )
        else:
            self.log(
                "No custom file_path provided in configuration. Default filename will be generated "
                "automatically during YAML generation using timestamp pattern.",
                "DEBUG"
            )

        self.log(
            "Configuration parameters validation completed successfully. All provided parameters "
            "are valid and accessible. Proceeding with access point configuration extraction.",
            "INFO"
        )
        self.status = "success"
        return self

    def get_want(self, config, state):
        """
        Prepares desired state parameters for access point configuration extraction workflow.

        This function processes validated configuration data and constructs the 'want' state
        dictionary that drives the brownfield access point playbook generation workflow. It
        validates parameters, organizes configuration data, and prepares API call parameters
        based on the specified operational state.

        Args:
            config (dict): Validated configuration data containing:
                          - file_path (str, optional): Custom YAML output path
                          - generate_all_configurations (bool, optional): Auto-generate mode flag
                          - global_filters (dict, optional): Filter criteria for targeted extraction
            state (str): Desired operational state ("gathered" for brownfield extraction)

        Returns:
            object: Self instance with updated attributes:
                   - self.want: Dictionary containing prepared parameters for API operations
                   - self.status: "success" after successful parameter preparation
                   - self.msg: Success message describing parameter collection

        Side Effects:
            - Calls validate_params() to validate configuration parameters
            - Updates self.want with yaml_config_generator parameters
            - Logs parameter preparation progress at INFO level
            - Updates self.status and self.msg for operation tracking

        Want Structure:
            {
                "yaml_config_generator": {
                    "file_path": <custom_path_or_None>,
                    "generate_all_configurations": <bool>,
                    "global_filters": {
                        "site_list": [...],
                        "provision_hostname_list": [...],
                        "accesspoint_config_list": [...],
                        "accesspoint_provision_config_list": [...],
                        "accesspoint_provision_config_mac_list": [...]
                    }
                }
            }

        Supported States:
            - gathered: Extract existing AP configurations from Catalyst Center
            - Future: merged, deleted, replaced (reserved for future implementation)

        Workflow Integration:
            1. Called after validate_input() completes successfully
            2. Validates individual config parameters via validate_params()
            3. Constructs want dictionary with yaml_config_generator parameters
            4. Want dictionary used by get_diff_gathered() for configuration extraction
            5. Enables yaml_config_generator() to process filters and generate YAML

        Notes:
            - validate_params() must pass before want construction
            - All configuration keys passed directly to yaml_config_generator
            - State parameter logged but not currently used in logic (reserved for future states)
            - Want structure optimized for YAML generation workflow
        """
        self.log(
            f"Starting desired state (want) parameter preparation for access point configuration "
            f"extraction. Operational state: '{state}'. Configuration contains "
            f"{len(config.keys()) if config else 0} parameter(s). Will validate parameters and "
            f"construct want dictionary for API operations.",
            "INFO"
        )

        # Validate configuration parameters
        self.log(
            f"Calling validate_params() to ensure configuration parameters are valid and "
            f"accessible before constructing want state.",
            "DEBUG"
        )
        self.validate_params(config)

        if self.status == "failed":
            self.log(
                f"Parameter validation failed in validate_params(). Cannot proceed with want "
                f"state construction. Error: {self.msg}",
                "ERROR"
            )
            return self

        self.log(
            "Parameter validation completed successfully. Proceeding with want state construction.",
            "DEBUG"
        )

        # Initialize want dictionary
        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config

        self.log(
            f"Added yaml_config_generator to want state with configuration: "
            f"{self.pprint(want['yaml_config_generator'])}. This configuration will drive "
            f"the YAML generation workflow including filter processing and file output.",
            "INFO"
        )

        # Store want state
        self.want = want

        self.log(
            f"Desired State (want) construction completed successfully. Want structure: "
            f"{self.pprint(self.want)}. This will be used by get_diff_gathered() to orchestrate "
            f"access point configuration extraction workflow.",
            "INFO"
        )

        self.msg = (
            f"Successfully collected all parameters from playbook for access point configuration "
            f"operations. Operational state: '{state}', Parameter count: {len(config.keys())}, "
            f"Generate all mode: {config.get('generate_all_configurations', False)}, "
            f"Has global_filters: {bool(config.get('global_filters'))}"
        )
        self.status = "success"

        return self

    def get_have(self, config):
        """
        Retrieves current access point configuration state from Cisco Catalyst Center.

        This function queries Catalyst Center APIs to collect existing access point configurations
        including AP details, radio settings, provisioning status, and site assignments. It supports
        two operational modes: generate_all (complete discovery) and filtered (targeted extraction
        based on global_filters). Results are stored in self.have for downstream processing.

        Args:
            config (dict): Configuration data containing operational mode and filters:
                          - generate_all_configurations (bool, optional): Complete discovery mode
                          - global_filters (dict, optional): Filter criteria for targeted extraction
                            * site_list: Floor site hierarchies
                            * provision_hostname_list: Provisioned AP hostnames
                            * accesspoint_config_list: AP configuration hostnames
                            * accesspoint_provision_config_list: Combined provision/config hostnames
                            * accesspoint_provision_config_mac_list: AP MAC addresses

        Returns:
            object: Self instance with updated attributes:
                   - self.have["all_ap_config"]: List of AP configuration dictionaries
                   - self.have["all_detailed_config"]: Complete AP metadata with IDs
                   - self.status: "success" after retrieval completion
                   - self.msg: Result description message

        Side Effects:
            - Calls get_current_config() to fetch AP configurations from Catalyst Center
            - Updates self.have dictionary with retrieved configurations
            - Logs retrieval progress at INFO, DEBUG levels
            - Updates self.status and self.msg for operation tracking

        Operational Modes:
            Generate All Mode (generate_all_configurations=true):
                - Retrieves ALL access points from Catalyst Center
                - No filtering applied
                - Discovers complete brownfield infrastructure
                - Ignores any provided global_filters

            Filtered Mode (global_filters provided):
                - Retrieves only APs matching filter criteria
                - Applies hierarchical filter priority (site > hostname > MAC)
                - Supports multiple filter types simultaneously
                - Validates filter values exist in Catalyst Center

        Data Collection:
            For each access point:
                1. Retrieve device details (MAC, hostname, model, site)
                2. Fetch AP configuration (admin status, radio settings, LED config)
                3. Parse radio configuration (2.4GHz, 5GHz, 6GHz, XOR, Tri)
                4. Extract provisioning details (site assignment, RF profile)
                5. Store parsed configuration in all_ap_config
                6. Store complete metadata in all_detailed_config

        Have Structure:
            {
                "all_ap_config": [
                    {
                        "mac_address": "aa:bb:cc:dd:ee:ff",
                        "ap_name": "AP-Floor1-001",
                        "admin_status": "Enabled",
                        "led_status": "Enabled",
                        "location": "Global/USA/Building1/Floor1",
                        "2.4ghz_radio": {...},
                        "5ghz_radio": {...},
                        "rf_profile": "HIGH",
                        "site": {...}
                    }
                ],
                "all_detailed_config": [
                    {
                        "id": "<uuid>",
                        "eth_mac_address": "aa:bb:cc:dd:ee:ff",
                        "configuration": {...},
                        ...
                    }
                ]
            }

        Error Handling:
            - No APs found: Returns success with empty have structure
            - API failures: Logged and propagated to get_current_config()
            - Invalid config structure: Type validation before processing

        Notes:
            - get_current_config() handles API pagination and error handling
            - Both generate_all and global_filters can coexist (filters ignored in generate_all mode)
            - Empty results are valid (e.g., no APs provisioned yet)
            - Have state used by yaml_config_generator() for YAML file creation
        """
        self.log(
            f"Starting retrieval of current access point configuration state from Cisco Catalyst "
            f"Center. Configuration mode: {'generate_all' if config.get('generate_all_configurations') else 'filtered'}. "
            f"Will query Catalyst Center APIs to collect existing AP configurations including "
            f"device details, radio settings, provisioning status, and site assignments.",
            "INFO"
        )

        # Validate config parameter
        if not config or not isinstance(config, dict):
            self.msg = (
                f"Invalid configuration provided to get_have(). Expected dictionary, got "
                f"{type(config).__name__}. Cannot proceed with AP configuration retrieval."
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.log(
            f"Configuration validation passed. Configuration contains {len(config.keys())} "
            f"parameter(s): {list(config.keys())}. Determining operational mode.",
            "DEBUG"
        )

        # Process generate_all_configurations mode
        if config.get("generate_all_configurations", False):
            self.log(
                "Generate all configurations mode detected (generate_all_configurations=True). "
                "Will retrieve ALL access points from Catalyst Center without applying any filters. "
                "This mode discovers complete brownfield infrastructure. Any provided global_filters "
                "will be IGNORED.",
                "INFO"
            )

            self.have["all_ap_config"] = self.get_current_config(config)

            if not self.have.get("all_ap_config"):
                self.msg = (
                    "No existing access point configurations found in Cisco Catalyst Center. "
                    "This may indicate: (1) No APs are provisioned, (2) APs exist but have no "
                    "configurations, or (3) API query returned empty results."
                )
                self.log(self.msg, "WARNING")
                self.status = "success"
                return self

            self.log(
                f"Successfully collected all AP configurations in generate_all mode. Total APs "
                f"retrieved: {len(self.have.get('all_ap_config', []))}. Configurations: "
                f"{self.pprint(self.have.get('all_ap_config'))}",
                "INFO"
            )

        # Process global_filters mode
        global_filters = config.get("global_filters")
        if global_filters:
            self.log(
                f"Global filters mode detected. Provided filters: {global_filters}. Will retrieve "
                f"only access points matching the specified filter criteria. Filter priority: "
                f"site_list > provision_hostname_list > accesspoint_config_list > "
                f"accesspoint_provision_config_list > accesspoint_provision_config_mac_list.",
                "INFO"
            )

            # Validate global_filters structure
            if not isinstance(global_filters, dict):
                self.msg = (
                    f"Invalid global_filters structure. Expected dictionary, got "
                    f"{type(global_filters).__name__}. Cannot proceed with filtered retrieval."
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            # Check if any filter has values
            has_filter_values = any(
                global_filters.get(key)
                for key in [
                    "site_list",
                    "provision_hostname_list",
                    "accesspoint_config_list",
                    "accesspoint_provision_config_list",
                    "accesspoint_provision_config_mac_list"
                ]
            )

            if not has_filter_values:
                self.msg = (
                    "global_filters provided but no filter lists contain values. At least one "
                    "filter must have values for targeted extraction. Please provide at least one "
                    "non-empty filter list."
                )
                self.log(self.msg, "WARNING")
                self.status = "success"
                return self

            self.log(
                f"Global filters validation passed. At least one filter contains values. "
                f"Calling get_current_config() with filters to retrieve matching APs.",
                "DEBUG"
            )

            self.have["all_ap_config"] = self.get_current_config(global_filters)

            if not self.have.get("all_ap_config"):
                self.msg = (
                    f"No access point configurations found matching the provided global filters: "
                    f"{global_filters}. This may indicate: (1) Filter values don't match existing "
                    f"APs, (2) APs exist but have no configurations, or (3) Filters are too restrictive."
                )
                self.log(self.msg, "WARNING")
                self.status = "success"
                return self

            self.log(
                f"Successfully collected filtered AP configurations. Total APs matching filters: "
                f"{len(self.have.get('all_ap_config', []))}. Applied filters: {list(global_filters.keys())}",
                "INFO"
            )

        # Log current state
        self.log(
            f"Current State (have) retrieval completed. Have structure contains: "
            f"all_ap_config ({len(self.have.get('all_ap_config', []))} APs), "
            f"all_detailed_config ({len(self.have.get('all_detailed_config', []))} detailed records), "
            f"devices_details ({len(self.have.get('devices_details', []))} devices). "
            f"Full have state: {self.pprint(self.have)}",
            "INFO"
        )

        self.msg = (
            f"Successfully retrieved current access point configuration state from Catalyst Center. "
            f"Total APs collected: {len(self.have.get('all_ap_config', []))}, "
            f"Operational mode: {'generate_all' if config.get('generate_all_configurations') else 'filtered'}"
        )
        self.status = "success"

        return self

    def get_workflow_elements_schema(self):
        """
        Returns the mapping configuration for access point workflow manager.
        Returns:
            dict: A dictionary containing network elements and global filters configuration with validation rules.
        """
        return {
            "global_filters": {
                "site_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "provision_hostname_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_config_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_provision_config_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_provision_config_mac_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            }
        }

    def get_current_config(self, input_config):
        """
        Retrieves the current configuration of an access point and site related details
        from Cisco Catalyst Center.

        Parameters:
          - self (object): An instance of the class containing the method.
          - input_config (dict): A dictionary containing the input configuration details.
        Returns:
            - tuple: A tuple containing a boolean indicating if the access point exists
                and a dictionary of the current configuration details.
        Description:
            Queries the Cisco Catalyst Center for the existence of an Access Point
            using the provided input configuration details such as MAC address,
            management IP address, or hostname. If found, it retrieves the current
            Access Point configuration and returns it.
        """
        self.log("Starting to retrieve current configuration with input: {0}".format(
            self.pprint(input_config)), "INFO")

        collect_all_config = []
        collect_all_config_details = []
        current_configuration = self.get_accesspoint_details()
        self.log("Retrieved current access point details: {0}".format(
            self.pprint(current_configuration)), "INFO")

        if not current_configuration or not isinstance(current_configuration, list):
            self.msg = "No access point details found in Cisco Catalyst Center."
            self.status = "success"
            return

        for ap_detail in current_configuration:
            eth_mac_address = ap_detail.get("eth_mac_address")
            current_eth_configuration = self.get_accesspoint_configuration(
                eth_mac_address)

            if not current_eth_configuration:
                self.log(f"No configuration found for access point with MAC address: {eth_mac_address}",
                         "WARNING")
                continue

            ap_detail["configuration"] = current_eth_configuration
            parsed_config = self.parse_accesspoint_configuration(current_eth_configuration, ap_detail)
            self.log(f"Parsed configuration for access point with MAC address {eth_mac_address}: {parsed_config}",
                     "INFO")
            collect_all_config.append(parsed_config)
            collect_all_config_details.append(ap_detail)

        self.log("Completed parsing all current configuration: {0}".format(
            self.pprint(collect_all_config)), "INFO")
        self.have["all_detailed_config"] = copy.deepcopy(collect_all_config_details)

        return collect_all_config

    def get_accesspoint_details(self):
        """
        Retrieves the current details of all access point devices in Cisco Catalyst Center.

        Parameters:
        - self (object): An instance of the class containing the method.

        Returns:
        A tuple containing a boolean indicating if the devices exists and a
        dictionary of the current inventory details

        Description:
        Retrieve all access point device details from Cisco Catalyst Center.
        """
        response_all = []
        offset = 1
        limit = 500
        api_family, api_function, param_key = "devices", "get_device_list", "family"
        request_params = {param_key: "Unified AP", "offset": offset, "limit": limit}
        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))

        while resync_retry_count > 0:
            self.log(f"Sending initial API request: Family='{api_family}', Function='{api_function}', Params={request_params}",
                     "DEBUG")

            response = self.execute_get_request(api_family, api_function, request_params)
            if not response:
                self.log("No data received from API (Offset={0}). Exiting pagination.".
                         format(request_params["offset"]), "DEBUG")
                break

            self.log("Received {0} devices(s) from API (Offset={1}).".format(
                len(response.get("response")), request_params["offset"]), "DEBUG")
            device_list = response.get("response")
            if device_list and isinstance(device_list, list):
                self.log("Processing device list: {0}".format(
                    self.pprint(device_list)), "DEBUG")
                required_data_list = []
                for device_response in device_list:
                    required_data = {
                        "id": device_response.get("id"),
                        "associated_wlc_ip": device_response.get("associatedWlcIp"),
                        "eth_mac_address": device_response.get("apEthernetMacAddress"),
                        "mac_address": device_response.get("macAddress"),
                        "hostname": device_response.get("hostname"),
                        "management_ip_address": device_response.get("managementIpAddress"),
                        "model": device_response.get("platformId"),
                        "serial_number": device_response.get("serialNumber"),
                        "site_hierarchy": device_response.get("snmpLocation"),
                        "reachability_status": device_response.get("reachabilityStatus"),
                        "type": device_response.get("type")
                    }
                    required_data_list.append(required_data)

            response_all.extend(required_data_list)

            if len(response.get("response")) < limit:
                self.log("Received less than limit ({0}) results, assuming last page. Exiting pagination.".
                         format(len(response.get("response"))), "DEBUG")
                break

            offset += limit
            request_params["offset"] = offset  # Increment offset for pagination
            self.log("Incrementing offset to {0} for next API request.".format(
                request_params["offset"]), "DEBUG")

            self.log(
                "Pauses execution for {0} seconds.".format(resync_retry_interval),
                "INFO",
            )
            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval

        if response_all:
            self.log("Total {0} accesspoint(s) details retrieved. {1}".format(
                len(response_all), self.pprint(response_all)), "DEBUG")
        else:
            self.log("No accesspoint details found for the Unified AP.", "WARNING")

        return response_all

    def get_accesspoint_configuration(self, eth_mac_address):
        """
        Retrieves the current configuration of an access point from Cisco Catalyst Center.

        Parameters:
            eth_mac_address (str): The Ethernet MAC address of the access point.

        Returns:
            dict: A dictionary containing the current configuration details of the access point.

        Description:
            Queries the Cisco Catalyst Center for the configuration of an access point
            using its Ethernet MAC address. If found, it retrieves the current configuration
            details and returns them.
        """
        self.log("Starting to retrieve access point configuration for MAC: {0}".format(
            eth_mac_address), "INFO")

        if not eth_mac_address:
            self.msg = "Ethernet MAC address is required to retrieve access point configuration."
            self.log(self.msg, "ERROR")
            return None

        api_family, api_function, param_key = "wireless", "get_access_point_configuration", "key"
        request_params = {param_key: eth_mac_address}

        self.log(f"Sending initial API request: Family='{api_family}', Function='{api_function}', Params={request_params}",
                 "DEBUG")
        response = self.execute_get_request(api_family, api_function, request_params)
        if not response:
            self.log("No data received from access point config API.", "DEBUG")
            return None

        current_eth_configuration = self.camel_to_snake_case(response)
        self.log("Received API response from get_access_point_configuration: {0}".format(
            self.pprint(current_eth_configuration)), "INFO")

        return current_eth_configuration

    def parse_accesspoint_configuration(self, accesspoint_config, ap_details):
        """
        Parses the access point configuration details.

        Parameters:
            accesspoint_config (dict): The access point configuration details.
            ap_details (dict): Additional details about the access point.

        Returns:
            dict: A dictionary containing the parsed access point configuration details.
        """
        self.log("Starting to parse access point configuration: {0} and details: {1}".format(
            self.pprint(accesspoint_config), self.pprint(ap_details)), "INFO")

        parsed_config = {}
        if not accesspoint_config or not isinstance(accesspoint_config, dict):
            self.log("Invalid access point configuration provided for parsing.", "ERROR")
            return parsed_config

        list_of_ap_keys_to_parse = ["mac_address", "ap_name", "admin_status",
                                    "led_status", "led_brightness_level",
                                    "ap_mode", "location",
                                    "failover_priority", "secondary_controller_name",
                                    "secondary_ip_address", "tertiary_controller_name",
                                    "tertiary_ip_address", "primary_ip_address",
                                    "primary_controller_name"]

        for each_key in list_of_ap_keys_to_parse:
            if each_key == "location":
                if accesspoint_config.get(each_key) == "default location":
                    parsed_config["is_assigned_site_as_location"] = "Enabled"
                else:
                    parsed_config["location"] = accesspoint_config.get(each_key)
            elif each_key in ["tertiary_controller_name", "secondary_controller_name", "primary_controller_name"]:
                if accesspoint_config.get(each_key) in ["Clear", None, ""]:
                    parsed_config[each_key] = "Inherit from site / Clear"
                else:
                    parsed_config[each_key] = accesspoint_config.get(each_key)
            elif each_key in ["secondary_ip_address", "tertiary_ip_address", "primary_ip_address"]:
                if accesspoint_config.get(each_key) != "0.0.0.0":
                    parsed_config[each_key] = {
                        "address": accesspoint_config.get(each_key)}
            else:
                parsed_config[each_key] = accesspoint_config.get(each_key)

        if parsed_config["primary_controller_name"] in ["Inherit from site / Clear", "Clear", None, ""]:
            del parsed_config["secondary_controller_name"]
            del parsed_config["tertiary_controller_name"]
            del parsed_config["primary_controller_name"]

        parsed_config["clean_air_si_2.4ghz"] = "Disabled"
        parsed_config["clean_air_si_5ghz"] = "Disabled"
        parsed_config["clean_air_si_6ghz"] = "Disabled"

        radio_config = accesspoint_config.get("radio_dtos")
        if radio_config and isinstance(radio_config, list):
            self.log(f"Parsing radio configuration from access point configuration: {radio_config}",
                     "INFO")
            parsed_all_radios = {}
            for radio in radio_config:
                parsed_radio = {}
                radio_config_key = None
                list_of_radio_keys_to_parse = ["if_type_value", "admin_status", "radio_role_assignment",
                                               "channel", "radio_band", "power_assignment_mode", "clean_air_si",
                                               "channel_width", "powerlevel", "channel_assignment_mode",
                                               "channel_number", "custom_power_level",
                                               "antenna_gain"]
                for each_radio_key in list_of_radio_keys_to_parse:
                    if each_radio_key == "if_type_value":
                        if radio.get(each_radio_key) == "2.4 GHz":
                            radio_config_key = "2.4ghz_radio"
                        elif radio.get(each_radio_key) == "5 GHz":
                            radio_config_key = "5ghz_radio"
                        elif radio.get(each_radio_key) == "6 GHz":
                            radio_config_key = "6ghz_radio"
                        elif radio.get(each_radio_key) == "Dual Radio":
                            radio_config_key = "xor_radio"
                        elif radio.get(each_radio_key) == "Tri Radio":
                            radio_config_key = "tri_radio"
                        else:
                            radio_config_key = "if_type_value"
                    elif each_radio_key == "powerlevel":
                        parsed_radio["power_level"] = radio.get(each_radio_key)
                    elif each_radio_key == "clean_air_si":
                        if radio.get(each_radio_key) == "Enabled":
                            if radio_config_key == "2.4ghz_radio":
                                parsed_config["clean_air_si_2.4ghz"] = "Enabled"
                            elif radio_config_key == "5ghz_radio":
                                parsed_config["clean_air_si_5ghz"] = "Enabled"
                            elif radio_config_key == "6ghz_radio":
                                parsed_config["clean_air_si_6ghz"] = "Enabled"
                    else:
                        if radio.get(each_radio_key) is not None:
                            parsed_radio[each_radio_key] = radio.get(each_radio_key)

                if parsed_radio.get("power_assignment_mode") == "Global":
                    del parsed_radio["power_level"]

                if parsed_radio.get("channel_assignment_mode") == "Global":
                    del parsed_radio["channel_number"]

                if radio_config_key:
                    parsed_all_radios[radio_config_key] = parsed_radio

            parsed_config.update(parsed_all_radios)

        if accesspoint_config.get("provisioning_status"):
            self.log("Access point is provisioned, parsing additional configuration details.", "INFO")
            site_hierarchy = ap_details.get("site_hierarchy")
            if site_hierarchy and site_hierarchy not in ["default-location", "default location"]:
                parent_path, floor = site_hierarchy.rsplit("/", 1)
                parsed_config["rf_profile"] = "HIGH"
                parsed_config["site"] = {}
                parsed_config["site"]["floor"] = {}
                parsed_config["site"]["floor"]["parent_name"] = parent_path
                parsed_config["site"]["floor"]["name"] = floor

        self.log("Completed parsing access point configuration: {0}".format(
            self.pprint(parsed_config)), "INFO")
        return parsed_config

    def get_diff_gathered(self):
        """
        Gathers access point configuration details from Cisco Catalyst Center and generates YAML playbook.

        Returns:
            self: Returns the current object with status and result set.
        """
        self.log("Starting brownfield access point configuration gathering process", "INFO")

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

        if self.have.get("unprocessed"):
            self.msg = "Some access point configurations were not processed: " + str(self.have.get("unprocessed"))
            self.set_operation_result("failed", False, self.msg, "WARNING")

        return self

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters,
        processes the data and writes the YAML content to a specified file.
        It dynamically handles multiple access points configuration and their respective filters.

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
            self.log("Generate all access point configurations from Catalyst Center", "INFO")

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
            self.log("Preparing to collect all configurations for access point configuration workflow.",
                     "DEBUG")
            final_list = self.have.get("all_ap_config", [])
            self.log(f"All configurations collected for generate_all_configurations mode: {final_list}", "DEBUG")

        else:
            # we get ALL configurations
            self.log("Overriding any provided filters to retrieve based on global filters", "INFO")
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True",
                         "WARNING")

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            if global_filters:
                final_list = self.process_global_filters(global_filters)

        if not final_list:
            self.msg = "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name
            )
            self.set_operation_result("success", False, self.msg, "INFO")
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

    def process_global_filters(self, global_filters):
        """
        Process global filters for access point configuration workflow.

        Parameters:
            global_filters (dict): A dictionary containing global filter parameters.

        Returns:
            dict: A dictionary containing processed global filter parameters.
        """
        self.log(f"Processing global filters: {global_filters}", "DEBUG")

        site_list = global_filters.get("site_list")
        provision_hostname_list = global_filters.get("provision_hostname_list")
        accesspoint_config_list = global_filters.get("accesspoint_config_list")
        accesspoint_provision_config_list = global_filters.get("accesspoint_provision_config_list")
        accesspoint_provision_config_mac_list = global_filters.get("accesspoint_provision_config_mac_list")
        final_list = []
        unprocessed_aps = []

        if not self.have.get("all_ap_config"):
            self.msg = "No access points configuration found in the catalyst center."
            self.log(self.msg, "WARNING")
            self.fail_and_exit(self.msg)

        if site_list and isinstance(site_list, list):
            self.log(f"Filtering access point configuration based on site_list: {site_list}",
                     "DEBUG")
            if len(site_list) == 1 and site_list[0].lower() == "all":
                final_list = self.have.get("all_ap_config", [])
            else:
                ap_config_site_list = []
                for floor in site_list:
                    ap_site_exist = self.find_multiple_dict_by_key_value(
                        self.have.get("all_ap_config", []), "location", floor)

                    if not ap_site_exist:
                        self.log(f"Given site hierarchy not exist : {floor}", "WARNING")
                        unprocessed_aps.append(floor + ": Unable to find the configuration for the site hierarchy in the catalyst center.")
                        continue

                    ap_config_site_list.extend(ap_site_exist)
                final_list = ap_config_site_list
            self.log(f"Access points configuration collected for site list {site_list}: {final_list}", "DEBUG")

        elif provision_hostname_list and isinstance(provision_hostname_list, list):
            self.log(f"Filtering access point provision based on hostname list: {provision_hostname_list}",
                     "DEBUG")

            if len(provision_hostname_list) == 1 and provision_hostname_list[0].lower() == "all":
                ap_exist = self.find_multiple_dict_by_key_value(
                    self.have["all_ap_config"], "rf_profile", "HIGH")
                if not ap_exist:
                    self.log("No provisioned access points found in the catalyst center.", "WARNING")
                    self.msg = "No provisioned access points found in the catalyst center."
                    self.fail_and_exit(self.msg)

                provisioned_aps = []
                for each_ap in ap_exist:
                    provision_config = {
                        "mac_address": each_ap.get("mac_address"),
                        "rf_profile": each_ap.get("rf_profile"),
                        "site": each_ap.get("site")
                    }
                    provisioned_aps.append(provision_config)
                final_list = provisioned_aps
            else:
                provisioned_aps = []
                for each_host in provision_hostname_list:
                    self.log(f"Check provision AP config exist for : {each_host}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_host)
                    if not ap_exist:
                        self.log(f"Given provision access point hostname not exist : {each_host}", "WARNING")
                        unprocessed_aps.append(each_host + ": Unable to find the hostname in the catalyst center.")
                        continue
                    provisioned_aps.append({
                        "mac_address": ap_exist[0].get("mac_address"),
                        "rf_profile": ap_exist[0].get("rf_profile"),
                        "site": ap_exist[0].get("site")
                    })

                if not provisioned_aps:
                    self.msg = "No provisioned access points found in the catalyst center."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = provisioned_aps
            self.log(f"Access points configuration collected for provision access point list {provision_hostname_list}: {final_list}",
                     "DEBUG")

        elif accesspoint_config_list and isinstance(accesspoint_config_list, list):
            self.log(f"Filtering access point configuration based on ap config list: {accesspoint_config_list}",
                     "DEBUG")
            ap_config_list = []
            keys_to_remove = ["rf_profile", "site"]

            if len(accesspoint_config_list) == 1 and accesspoint_config_list[0].lower() == "all":
                ap_config_list = copy.deepcopy(self.have.get("all_ap_config", []))
                for each_ap in ap_config_list:
                    for key in keys_to_remove:
                        if each_ap.get(key):
                            del each_ap[key]
                self.log(f"All access point configurations found for 'all' filter. {ap_config_list}", "INFO")
                final_list = ap_config_list
            else:
                for each_ap in accesspoint_config_list:
                    self.log(f"Check real access point exist for : {each_ap}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_ap)

                    if not ap_exist:
                        self.log(f"Given provision access point hostname not exist : {each_ap}", "WARNING")
                        unprocessed_aps.append(each_ap + ": Unable to find the hostname in the catalyst center.")
                        continue

                    for each_ap in ap_exist:
                        for key in keys_to_remove:
                            if each_ap.get(key):
                                del each_ap[key]

                    ap_config_list.extend(ap_exist)
                    self.log(f"Given access point hostname exist : {ap_exist}", "INFO")

                if not ap_config_list:
                    self.msg = f"No access points found matching the provided list. {accesspoint_config_list}."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = ap_config_list
            self.log(f"Access points configuration collected for ap configuration list {accesspoint_config_list}: {final_list}",
                     "DEBUG")

        elif accesspoint_provision_config_list and isinstance(accesspoint_provision_config_list, list):
            self.log(f"Filtering access point configuration based on hostname list: {accesspoint_provision_config_list}",
                     "DEBUG")
            if len(accesspoint_provision_config_list) == 1 and accesspoint_provision_config_list[0].lower() == "all":
                final_list = self.have.get("all_ap_config", [])
                self.log(f"All access point configurations found for 'all' filter. {final_list}", "INFO")
            else:
                collected_aps = []
                for each_host_name in accesspoint_provision_config_list:
                    self.log(f"Check access point configuration exist for : {each_host_name}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_host_name)

                    if not ap_exist:
                        self.log(f"Given provision access point hostname not exist : {each_host_name}", "WARNING")
                        unprocessed_aps.append(each_host_name + ": Unable to find the hostname in the catalyst center.")
                        continue

                    collected_aps.extend(ap_exist)
                    self.log(f"Given access point configuration exist : {ap_exist}", "INFO")

                if not collected_aps:
                    self.msg = "No access points found matching the provided hostname list."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = collected_aps

            self.log(f"Access point configuration collected for given hostname list {accesspoint_provision_config_list}: {final_list}",
                     "DEBUG")

        elif accesspoint_provision_config_mac_list and isinstance(accesspoint_provision_config_mac_list, list):
            self.log(f"Filtering access point configuration based on mac address list: {accesspoint_provision_config_mac_list}",
                     "DEBUG")
            if len(accesspoint_provision_config_mac_list) == 1 and accesspoint_provision_config_mac_list[0].lower() == "all":
                final_list = self.have.get("all_ap_config", [])
                self.log(f"All access point configurations found for 'all' filter. {final_list}", "INFO")
            else:
                collected_aps = []
                for each_mac in accesspoint_provision_config_mac_list:
                    self.log(f"Check access point configuration exist for : {each_mac}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "mac_address", each_mac)

                    if not ap_exist:
                        self.log(f"Given provision access point mac address not exist : {each_mac}", "WARNING")
                        unprocessed_aps.append(each_mac + ": Unable to find configuration for the MAC address in the catalyst center.")
                        continue

                    collected_aps.extend(ap_exist)
                    self.log(f"Given access point configuration exist : {ap_exist}", "INFO")

                if not collected_aps:
                    self.msg = "No access points found matching the provided mac address list."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = collected_aps

            self.log(f"Access point configuration collected for given mac address list {accesspoint_provision_config_mac_list}: {final_list}",
                     "DEBUG")

        else:
            self.log("No specific global filters provided, processing all access points configuration.", "DEBUG")

        if unprocessed_aps:
            self.msg = {
                "The following access points could not be processed:": unprocessed_aps
            }
            self.log(self.msg, "WARNING")
            self.have["unprocessed"] = unprocessed_aps

        if not final_list:
            self.log("No access points position found in the catalyst center.", "WARNING")
            return None

        return final_list


def main():
    """
    Main entry point for the Cisco Catalyst Center brownfield access point playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield access point configurations.

    Purpose:
        Initializes and executes the brownfield access point playbook generator
        workflow to extract existing AP configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create AccessPointPlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 2.3.5.3)
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
        - Minimum Catalyst Center version: 2.3.5.3
        - Introduced APIs for access point configuration retrieval:
            * Network device list (get_device_list)
            * AP configuration (get_access_point_configuration)
            * Site details (get_site)
            * Device info (get_device_info)
            * AP provisioning (ap_provision)
            * AP configuration (configure_access_points)

    Supported States:
        - gathered: Extract existing AP configurations and generate YAML playbook
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

    # Initialize the AccessPointPlaybookGenerator object
    # This creates the main orchestrator for brownfield AP configuration extraction
    ccc_accesspoint_playbook_generator = AccessPointPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_accesspoint_playbook_generator.log(
        f"Starting Ansible module execution for brownfield access point playbook "
        f"generator at timestamp {initialization_timestamp}",
        "INFO"
    )

    ccc_accesspoint_playbook_generator.log(
        f"Module initialized with parameters: dnac_host={module.params.get('dnac_host')}, "
        f"dnac_port={module.params.get('dnac_port')}, "
        f"dnac_username={module.params.get('dnac_username')}, "
        f"dnac_verify={module.params.get('dnac_verify')}, "
        f"dnac_version={module.params.get('dnac_version')}, "
        f"state={module.params.get('state')}, "
        f"config_items={len(module.params.get('config', []))}",
        "DEBUG"
    )

    # ============================================
    # Version Compatibility Check
    # ============================================
    ccc_accesspoint_playbook_generator.log(
        f"Validating Catalyst Center version compatibility - checking if version "
        f"{ccc_accesspoint_playbook_generator.get_ccc_version()} meets minimum requirement "
        f"of 2.3.5.3 for access point configuration APIs",
        "INFO"
    )

    if (ccc_accesspoint_playbook_generator.compare_dnac_versions(
            ccc_accesspoint_playbook_generator.get_ccc_version(), "2.3.5.3") < 0):

        error_msg = (
            f"The specified Catalyst Center version "
            f"'{ccc_accesspoint_playbook_generator.get_ccc_version()}' does not support the YAML "
            f"playbook generation for Access Point Workflow Manager module. Supported versions start "
            f"from '2.3.5.3' onwards. Version '2.3.5.3' introduces APIs for retrieving "
            f"access point configurations or the following global filters: site_list, "
            f"provision_hostname_list, accesspoint_config_list, accesspoint_provision_config_list, "
            f"and accesspoint_provision_config_mac_list from the Catalyst Center."
        )

        ccc_accesspoint_playbook_generator.log(
            f"Version compatibility check failed: {error_msg}",
            "ERROR"
        )

        ccc_accesspoint_playbook_generator.msg = error_msg
        ccc_accesspoint_playbook_generator.set_operation_result(
            "failed", False, ccc_accesspoint_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_accesspoint_playbook_generator.log(
        f"Version compatibility check passed - Catalyst Center version "
        f"{ccc_accesspoint_playbook_generator.get_ccc_version()} supports "
        f"all required access point configuration APIs",
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_accesspoint_playbook_generator.params.get("state")

    ccc_accesspoint_playbook_generator.log(
        f"Validating requested state parameter: '{state}' against supported states: "
        f"{ccc_accesspoint_playbook_generator.supported_states}",
        "DEBUG"
    )

    if state not in ccc_accesspoint_playbook_generator.supported_states:
        error_msg = (
            f"State '{state}' is invalid for this module. Supported states are: "
            f"{ccc_accesspoint_playbook_generator.supported_states}. "
            f"Please update your playbook to use one of the supported states."
        )

        ccc_accesspoint_playbook_generator.log(
            f"State validation failed: {error_msg}",
            "ERROR"
        )

        ccc_accesspoint_playbook_generator.status = "invalid"
        ccc_accesspoint_playbook_generator.msg = error_msg
        ccc_accesspoint_playbook_generator.check_return_status()

    ccc_accesspoint_playbook_generator.log(
        f"State validation passed - using state '{state}' for workflow execution",
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_accesspoint_playbook_generator.log(
        "Starting comprehensive input parameter validation for playbook configuration",
        "INFO"
    )

    ccc_accesspoint_playbook_generator.validate_input().check_return_status()

    ccc_accesspoint_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = ccc_accesspoint_playbook_generator.validated_config

    ccc_accesspoint_playbook_generator.log(
        f"Starting configuration processing loop - will process {len(config_list)} configuration "
        f"item(s) from playbook",
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        ccc_accesspoint_playbook_generator.log(
            f"Processing configuration item {config_index}/{len(config_list)} for state '{state}'",
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_accesspoint_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_accesspoint_playbook_generator.reset_values()

        # Collect desired state (want) from configuration
        ccc_accesspoint_playbook_generator.log(
            f"Collecting desired state parameters from configuration item {config_index}",
            "DEBUG"
        )
        ccc_accesspoint_playbook_generator.get_want(
            config, state
        ).check_return_status()

        # Collect current state (have) from Catalyst Center
        ccc_accesspoint_playbook_generator.log(
            f"Collecting current state from Catalyst Center for configuration item {config_index}",
            "DEBUG"
        )
        ccc_accesspoint_playbook_generator.get_have(
            config
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_accesspoint_playbook_generator.log(
            f"Executing state-specific operation for '{state}' workflow on "
            f"configuration item {config_index}",
            "INFO"
        )
        ccc_accesspoint_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_accesspoint_playbook_generator.log(
            f"Successfully completed processing for configuration item {config_index}/{len(config_list)}",
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

    ccc_accesspoint_playbook_generator.log(
        f"Module execution completed successfully at timestamp {completion_timestamp}. "
        f"Total execution time: {module_duration:.2f} seconds. Processed {len(config_list)} "
        f"configuration item(s) with final status: {ccc_accesspoint_playbook_generator.status}",
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_accesspoint_playbook_generator.log(
        f"Exiting Ansible module with result: {ccc_accesspoint_playbook_generator.result}",
        "DEBUG"
    )

    module.exit_json(**ccc_accesspoint_playbook_generator.result)


if __name__ == "__main__":
    main()

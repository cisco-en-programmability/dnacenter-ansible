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
module: accesspoint_playbook_config_generator
short_description: >-
  Generate YAML configurations playbook for
  'accesspoint_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the
    'accesspoint_workflow_manager' module, reducing
    the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
  - Supports complete access point playbook config generation by
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
        with the 'accesspoint_playbook_config_generator'
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
          - This is useful for complete access point playbook config
            generation and documentation.
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
            'accesspoint_playbook_config_2025-04-22_21-43-26.yml'.
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
  cisco.dnac.accesspoint_playbook_config_generator:
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
  cisco.dnac.accesspoint_playbook_config_generator:
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
      - file_path: "tmp/accesspoint_workflow_playbook.yml"
        generate_all_configurations: true

- name: Generate YAML Configuration with file path based on site list filters
  cisco.dnac.accesspoint_playbook_config_generator:
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
      - file_path: "tmp/accesspoint_workflow_playbook_site_base.yml"
        global_filters:
          site_list:
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR1
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR2

- name: Generate YAML provision config with file path based on hostname list filters
  cisco.dnac.accesspoint_playbook_config_generator:
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
  cisco.dnac.accesspoint_playbook_config_generator:
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
  cisco.dnac.accesspoint_playbook_config_generator:
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
  cisco.dnac.accesspoint_playbook_config_generator:
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
             "tmp/accesspoint_workflow_playbook_templatebase.yml"
          }
        },
      "msg": {
        "YAML config generation Task succeeded for module
         'accesspoint_workflow_manager'.": {
            "file_path":
             "tmp/accesspoint_workflow_playbook_templatebase.yml"
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
        Validates the input configuration parameters for the access point playbook config generator.

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
            "Starting comprehensive input validation for access point playbook config generator "
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
            self.validate_minimum_requirement_for_global_filters(self.config)
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
        Validates individual configuration parameters for access point playbook config generator.

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
        dictionary that drives the access point playbook config generator workflow. It
        validates parameters, organizes configuration data, and prepares API call parameters
        based on the specified operational state.

        Args:
            config (dict): Validated configuration data containing:
                          - file_path (str, optional): Custom YAML output path
                          - generate_all_configurations (bool, optional): Auto-generate mode flag
                          - global_filters (dict, optional): Filter criteria for targeted extraction
            state (str): Desired operational state ("gathered" for config extraction)

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
            "Calling validate_params() to ensure configuration parameters are valid and "
            "accessible before constructing want state.",
            "DEBUG"
        )
        self.validate_params(config)

        if self.status == "failed":
            self.log(
                "Parameter validation failed in validate_params(). Cannot proceed with want "
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
                - Discovers complete wireless access point
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
                "This mode discovers complete wireless access point configurations. Any provided global_filters "
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
                "Global filters validation passed. At least one filter contains values. "
                "Calling get_current_config() with filters to retrieve matching APs.",
                "DEBUG"
            )

            self.have["all_ap_config"] = self.get_current_config(global_filters)

            if not self.have.get("all_ap_config"):
                self.msg = (
                    "No access point configurations found matching the provided global filters: "
                    f"{global_filters}. This may indicate: (1) Filter values don't match existing "
                    "APs, (2) APs exist but have no configurations, or (3) Filters are too restrictive."
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
        Retrieves the schema configuration for access point workflow manager components.

        This function defines the complete validation schema for global filters used in access
        point playbook generation, specifying allowed filter types, data structures, and
        validation rules for site-based, hostname-based, and MAC address-based filtering.

        Args:
            None (uses self context for potential future expansion)

        Returns:
            dict: Schema configuration dictionary with global_filters structure containing
                validation rules for site_list, provision_hostname_list, accesspoint_config_list,
                accesspoint_provision_config_list, and accesspoint_provision_config_mac_list
                filter types. All filters optional with list[str] type requirement.

        Filter Types:
            - site_list: Floor site hierarchies for location-based filtering
            - provision_hostname_list: Provisioned AP hostnames
            - accesspoint_config_list: AP configuration hostnames
            - accesspoint_provision_config_list: Combined provision/config hostnames
            - accesspoint_provision_config_mac_list: AP MAC addresses

        Usage:
            - Called during class initialization (__init__)
            - Schema stored in self.module_schema for validation
            - Used by validate_input() for parameter validation
            - Defines contract for global_filters structure

        Notes:
            - All filters are optional (required=False)
            - All filters expect list of strings (type="list", elements="str")
            - At least one filter must have values when global_filters provided
            - Schema enables dynamic filter validation without hardcoded checks
        """
        self.log(
            "Defining validation schema for access point workflow manager. Schema includes "
            "global_filters structure with five filter types: site_list, provision_hostname_list, "
            "accesspoint_config_list, accesspoint_provision_config_list, and "
            "accesspoint_provision_config_mac_list. All filters are optional list[str] types "
            "enabling flexible AP filtering for playbook config generation.",
            "DEBUG"
        )

        schema = {
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

        self.log(
            f"Schema definition completed successfully. Schema contains {len(schema)} top-level "
            f"key(s) with {len(schema['global_filters'])} filter type(s). This schema enables "
            "structured validation of AP filtering parameters during playbook configuration "
            "validation workflow.",
            "DEBUG"
        )

        return schema

    def get_current_config(self, input_config):
        """
        Retrieves and parses current access point configurations from Cisco Catalyst Center.

        This function orchestrates the complete AP configuration retrieval workflow by fetching
        device details, querying AP configurations, and parsing radio settings for all discovered
        access points. It handles API pagination, error recovery, and configuration normalization
        to produce standardized AP configuration data for YAML generation.

        Args:
            input_config (dict): Configuration parameters containing operational mode and filters:
                                - generate_all_configurations (bool, optional): Complete discovery mode
                                - global_filters (dict, optional): Filter criteria for targeted extraction
                                Note: input_config determines which APs to retrieve but doesn't filter
                                      at this level - filtering happens in process_global_filters()

        Returns:
            list: List of parsed AP configuration dictionaries with structure:
                 [{
                     "mac_address": "aa:bb:cc:dd:ee:ff",
                     "ap_name": "AP-Floor1-001",
                     "admin_status": "Enabled",
                     "led_status": "Enabled",
                     "location": "Global/USA/Building1/Floor1",
                     "2.4ghz_radio": {...},
                     "5ghz_radio": {...},
                     "rf_profile": "HIGH",
                     "site": {...}
                 }]
                 Returns empty list if no APs found or API errors occur.

        Configuration Components:
            Device Details (from get_accesspoint_details):
                - id, eth_mac_address, mac_address, hostname
                - management_ip_address, model, serial_number
                - site_hierarchy, reachability_status, type

            AP Configuration (from get_accesspoint_configuration):
                - mac_address, ap_name, admin_status, led_status
                - ap_mode, location, failover_priority
                - Controller settings (primary, secondary, tertiary)
                - Radio configurations (2.4GHz, 5GHz, 6GHz, XOR, Tri)

            Parsed Configuration (from parse_accesspoint_configuration):
                - Normalized field names and values
                - Radio settings organized by frequency band
                - Clean Air SI per band
                - Provisioning details (site, RF profile)

        Error Handling:
            - No AP devices found: Returns empty list with status success
            - AP configuration fetch fails: Logs warning and skips AP
            - Invalid device list structure: Returns None with warning
            - API connectivity issues: Propagated from get_accesspoint_details()

        Notes:
            - input_config parameter logged but not used for filtering at this level
            - All discovered APs are processed regardless of input_config filters
            - Filtering applied later in process_global_filters() function
            - Empty results are valid (e.g., no APs configured in Catalyst Center)
            - self.have["all_detailed_config"] preserves complete metadata for troubleshooting
        """
        self.log(
            "Starting comprehensive access point configuration retrieval from Cisco Catalyst "
            f"Center. Input configuration: {self.pprint(input_config)}. This operation will "
            "query device inventory APIs to discover all Unified APs, fetch detailed "
            "configurations for each AP, and parse radio settings to produce normalized "
            "configuration data for YAML playbook generation.",
            "INFO"
        )

        # Initialize collection lists
        collect_all_config = []
        collect_all_config_details = []

        # Retrieve all AP device details from Catalyst Center
        self.log(
            "Calling get_accesspoint_details() to retrieve complete device inventory for all "
            "Unified AP devices in Catalyst Center. This API call queries the network device "
            "list with family filter 'Unified AP' to discover AP MAC addresses, hostnames, "
            "models, and site assignments required for configuration retrieval.",
            "DEBUG"
        )

        current_configuration = self.get_accesspoint_details()

        self.log(
            "Retrieved access point device details from Catalyst Center. Device list contains "
            f"{len(current_configuration) if current_configuration else 0} AP device(s). "
            f"Device details: {self.pprint(current_configuration)}",
            "INFO"
        )

        # Validate device list is not empty and has correct structure
        if not current_configuration or not isinstance(current_configuration, list):
            self.msg = (
                "No access point device details found in Cisco Catalyst Center inventory. "
                "This indicates either: (1) No Unified APs are registered in Catalyst Center, "
                "(2) API permissions insufficient to query device inventory, or (3) Device "
                "family filter 'Unified AP' returned empty results. Verify APs are onboarded "
                "to Catalyst Center before running access point playbook config generation."
            )
            self.log(self.msg, "WARNING")
            self.status = "success"
            return []

        self.log(
            f"Device inventory validation passed. Found {len(current_configuration)} Unified AP "
            "device(s) in Catalyst Center inventory. Starting configuration retrieval loop to "
            "fetch detailed AP configurations for each device by Ethernet MAC address.",
            "INFO"
        )

        # Iterate through each AP device and fetch configurations
        for ap_index, ap_detail in enumerate(current_configuration, start=1):
            eth_mac_address = ap_detail.get("eth_mac_address")

            self.log(
                f"Processing AP device {ap_index}/{len(current_configuration)}: Ethernet MAC "
                f"address '{eth_mac_address}', hostname '{ap_detail.get('hostname')}', model "
                f"'{ap_detail.get('model')}'. Calling get_accesspoint_configuration() to retrieve "
                "detailed configuration including radio settings, admin status, LED config, and "
                "controller assignments.",
                "DEBUG"
            )

            current_eth_configuration = self.get_accesspoint_configuration(eth_mac_address)

            if not current_eth_configuration:
                self.log(
                    f"No configuration found for access point {ap_index}/{len(current_configuration)} "
                    f"with Ethernet MAC address '{eth_mac_address}', hostname "
                    f"'{ap_detail.get('hostname')}'. This AP may not have a complete configuration "
                    "in Catalyst Center or API query failed. Skipping this AP and continuing with "
                    "next device in inventory.",
                    "WARNING"
                )
                continue

            self.log(
                f"Successfully retrieved configuration for AP {ap_index}/{len(current_configuration)} "
                f"with Ethernet MAC '{eth_mac_address}'. Configuration contains admin status, radio "
                "settings, LED configuration, and controller details. Attaching configuration to "
                "device details and calling parse_accesspoint_configuration() for normalization.",
                "DEBUG"
            )

            # Attach configuration to device details
            ap_detail["configuration"] = current_eth_configuration

            # Parse and normalize configuration structure
            self.log(
                f"Parsing configuration for AP {ap_index}/{len(current_configuration)} with MAC "
                f"'{eth_mac_address}'. Parser will normalize field names, organize radio settings "
                "by frequency band, extract provisioning details, and produce standardized "
                "configuration structure for YAML generation.",
                "DEBUG"
            )

            parsed_config = self.parse_accesspoint_configuration(
                current_eth_configuration, ap_detail
            )

            self.log(
                f"Successfully parsed configuration for AP {ap_index}/{len(current_configuration)} "
                f"with Ethernet MAC '{eth_mac_address}'. Parsed configuration: {parsed_config}. "
                "Adding parsed config to collection list for YAML generation.",
                "INFO"
            )

            # Store parsed configuration and detailed metadata
            collect_all_config.append(parsed_config)
            collect_all_config_details.append(ap_detail)

            self.log(
                f"Completed processing for AP {ap_index}/{len(current_configuration)}. Current "
                f"collection statistics - Parsed configs: {len(collect_all_config)}, Detailed "
                f"metadata records: {len(collect_all_config_details)}",
                "DEBUG"
            )

        # Store detailed configuration for troubleshooting reference
        self.log(
            "Storing complete detailed configuration metadata in self.have['all_detailed_config'] "
            "for troubleshooting and reference. Detailed configs include raw API responses, "
            "device UUIDs, and unparsed configuration data. Total detailed records: "
            f"{len(collect_all_config_details)}",
            "DEBUG"
        )

        self.have["all_detailed_config"] = copy.deepcopy(collect_all_config_details)

        self.log(
            "Completed access point configuration retrieval and parsing workflow. Final "
            f"statistics - Total APs in inventory: {len(current_configuration)}, Successfully "
            f"retrieved configs: {len(collect_all_config)}, Failed/skipped APs: "
            f"{len(current_configuration) - len(collect_all_config)}. Parsed configurations: "
            f"{self.pprint(collect_all_config)}",
            "INFO"
        )

        return collect_all_config

    def get_accesspoint_details(self):
        """
        Retrieves complete device inventory for all Unified AP devices in Cisco Catalyst Center.

        This function queries the Catalyst Center network device API with pagination to discover
        all access points registered in the system. It extracts essential device metadata including
        MAC addresses, hostnames, models, site assignments, and reachability status for downstream
        configuration retrieval and YAML generation workflows.

        Args:
            None (uses self.payload for API configuration parameters)

        Returns:
            list: List of AP device detail dictionaries with structure:
                 [{
                     "id": "<device_uuid>",
                     "associated_wlc_ip": "10.1.1.1",
                     "eth_mac_address": "aa:bb:cc:dd:ee:ff",
                     "mac_address": "aa:bb:cc:dd:ee:ff",
                     "hostname": "AP-Floor1-001",
                     "management_ip_address": "10.1.2.1",
                     "model": "AIR-AP2802I-B-K9",
                     "serial_number": "FCW2234G0QZ",
                     "site_hierarchy": "Global/USA/Building1/Floor1",
                     "reachability_status": "Reachable",
                     "type": "Unified AP"
                 }]
                 Returns empty list if no APs found or API errors occur.
        """
        self.log(
            "Starting comprehensive Unified AP device inventory retrieval from Cisco Catalyst "
            "Center. Initializing pagination loop to query network device API with family filter "
            "'Unified AP'. This operation will discover all access points registered in Catalyst "
            "Center and extract device metadata (MAC addresses, hostnames, models, sites) required "
            "for configuration retrieval workflow.",
            "INFO"
        )

        # Initialize collection variables
        response_all = []
        offset = 1
        limit = 500

        # API call configuration
        api_family, api_function, param_key = "devices", "get_device_list", "family"
        request_params = {param_key: "Unified AP", "offset": offset, "limit": limit}

        # Timeout and retry configuration from payload
        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))

        self.log(
            f"Pagination configuration initialized. Starting offset: {offset}, page size limit: "
            f"{limit} devices, API timeout: {resync_retry_count} seconds, retry interval: "
            f"{resync_retry_interval} seconds. API call parameters: family='Unified AP', "
            f"offset={offset}, limit={limit}. Loop will continue until all devices retrieved or "
            "timeout exhausted.",
            "DEBUG"
        )

        page_number = 1
        total_devices_collected = 0

        # Pagination loop to retrieve all AP devices
        while resync_retry_count > 0:
            self.log(
                f"Requesting AP device inventory page {page_number} from Catalyst Center API. "
                f"API call parameters - Family: '{api_family}', Function: '{api_function}', "
                f"Params: {request_params}. This request targets Unified AP devices with offset "
                f"{offset} (starting index) and limit {limit} (max devices per page). Remaining "
                f"timeout: {resync_retry_count} seconds.",
                "DEBUG"
            )

            # Execute API request
            response = self.execute_get_request(api_family, api_function, request_params)

            if not response:
                self.log(
                    f"No data received from Catalyst Center API for page {page_number} (offset={offset}). "
                    "API returned None or empty response. This indicates either end of available "
                    "devices or potential API connectivity issue. Exiting pagination loop to prevent "
                    "unnecessary API calls and return collected data.",
                    "DEBUG"
                )
                break

            # Extract device list from response
            device_list = response.get("response")

            if not device_list or not isinstance(device_list, list):
                self.log(
                    f"Invalid or empty device list received from API for page {page_number}. "
                    f"Expected list of devices, got {type(device_list).__name__}. Breaking "
                    "pagination loop.",
                    "WARNING"
                )
                break

            page_device_count = len(device_list)
            total_devices_collected += page_device_count

            self.log(
                f"Successfully retrieved {page_device_count} Unified AP device(s) from Catalyst "
                f"Center API for page {page_number} (offset={offset}). Cumulative devices collected "
                f"across all pages: {total_devices_collected}. API response contains valid device "
                "data with IDs, MAC addresses, hostnames, and site assignments.",
                "DEBUG"
            )

            # Process and normalize device data
            self.log(
                f"Processing device list for page {page_number}. Extracting and normalizing device "
                "metadata including ID, MAC addresses, hostname, model, site hierarchy, and "
                "reachability status. Converting camelCase API field names to snake_case for "
                f"internal use. Device list: {self.pprint(device_list)}",
                "DEBUG"
            )

            required_data_list = []
            for device_index, device_response in enumerate(device_list, start=1):
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

                self.log(
                    f"Normalized device {device_index}/{page_device_count} on page {page_number}: "
                    f"hostname='{required_data.get('hostname')}', eth_mac='{required_data.get('eth_mac_address')}', "
                    f"model='{required_data.get('model')}', site='{required_data.get('site_hierarchy')}', "
                    f"reachability='{required_data.get('reachability_status')}'",
                    "DEBUG"
                )

            # Append normalized data to collection
            response_all.extend(required_data_list)

            self.log(
                f"Appended {page_device_count} normalized device record(s) to collection. Current "
                f"total devices in collection: {len(response_all)}. Normalized data includes "
                "complete device metadata for downstream configuration retrieval.",
                "DEBUG"
            )

            # Check for last page (received fewer devices than limit)
            if page_device_count < limit:
                self.log(
                    f"Received device count ({page_device_count}) is less than configured page size "
                    f"limit ({limit}). This indicates the last page of device inventory has been "
                    "retrieved. No additional Unified AP devices available in Catalyst Center. "
                    "Exiting pagination loop to complete inventory collection operation.",
                    "DEBUG"
                )
                break

            # Increment offset for next page
            offset += limit
            request_params["offset"] = offset
            page_number += 1

            self.log(
                f"Incrementing pagination offset to {offset} for next API request (page {page_number}). "
                f"Next API call will retrieve devices starting from index {offset}, continuing "
                "sequential collection of Unified AP inventory from Catalyst Center.",
                "DEBUG"
            )

            # Rate limiting sleep to prevent API throttling
            self.log(
                f"Pausing execution for {resync_retry_interval} second(s) before next API request "
                "to prevent API rate limiting and throttling by Catalyst Center. This delay ensures "
                "stable API performance and prevents HTTP 429 (Too Many Requests) errors during "
                "large device inventory retrieval.",
                "INFO"
            )
            time.sleep(resync_retry_interval)

            # Decrement timeout counter
            resync_retry_count = resync_retry_count - resync_retry_interval

            self.log(
                "Decremented retry timeout counter after sleep interval. Remaining timeout: "
                f"{resync_retry_count} seconds, next timeout check in: {resync_retry_interval} "
                "seconds. Pagination loop will exit if timeout exhausted before all devices retrieved.",
                "DEBUG"
            )

        # Final logging based on collection results
        if response_all:
            self.log(
                "AP device inventory retrieval completed successfully. Total Unified AP device(s) "
                f"retrieved: {len(response_all)} across {page_number} page(s) of API responses. "
                "Device inventory contains complete metadata (ID, MAC addresses, hostnames, models, "
                "sites, reachability status) for all access points registered in Catalyst Center. "
                f"Inventory data: {self.pprint(response_all)}",
                "INFO"
            )
        else:
            self.log(
                "No Unified AP devices found in Cisco Catalyst Center inventory after pagination "
                "loop completion. The device collection is empty. This indicates either: (1) No "
                "access points are onboarded to Catalyst Center, (2) API permissions insufficient "
                "to query device inventory, or (3) Family filter 'Unified AP' returned no matches. "
                "Verify access points are registered in Catalyst Center before running access point "
                "playbook config generation.",
                "WARNING"
            )

        return response_all

    def get_accesspoint_configuration(self, eth_mac_address):
        """
        Retrieves detailed configuration for a specific access point from Cisco Catalyst Center.

        Queries the Catalyst Center wireless API to fetch complete configuration details for
        an access point identified by its Ethernet MAC address. Configuration includes radio
        settings (2.4GHz, 5GHz, 6GHz, XOR, Tri-band), admin status, LED brightness, AP mode,
        location, failover priority, and WLC controller assignments (primary, secondary, tertiary).

        Args:
            eth_mac_address (str): Ethernet MAC address of target access point.
                                  Format: "aa:bb:cc:dd:ee:ff" (colon-separated hexadecimal).
                                  This is the apEthernetMacAddress from device inventory.
                                  Required for API query; returns None if missing.

        Returns:
            dict: AP configuration with camelCase keys converted to snake_case. Structure:
                 {
                     "mac_address": "aa:bb:cc:dd:ee:ff",
                     "ap_name": "AP-Floor1-001",
                     "admin_status": "Enabled",
                     "led_status": "Enabled",
                     "led_brightness_level": 5,
                     "ap_mode": "Local",
                     "location": "Building1-Floor1-Zone1",
                     "failover_priority": "Low",
                     "primary_controller_name": "WLC-Primary",
                     "primary_ip_address": {"address": "10.1.1.1"},
                     "secondary_controller_name": "WLC-Secondary",
                     "secondary_ip_address": {"address": "10.1.1.2"},
                     "tertiary_controller_name": "WLC-Tertiary",
                     "tertiary_ip_address": {"address": "10.1.1.3"},
                     "radio_configurations": [
                         {
                             "radio_role_assignment": "AUTO",
                             "admin_status": "Enabled",
                             "antenna_name": "AIR-ANT2513P4M-N",
                             "channel_number": 36,
                             "channel_width": "20 MHz",
                             "power_assignment_mode": "Global",
                             "radio_band": "5 GHz",
                             "clean_air_si": "Enabled"
                         }
                     ],
                     "is_assigned_site_as_location": True,
                     "mesh_dto": {...},
                     "ap_height": 10.5
                 }
                 Returns None if no configuration found or API error.

        Side Effects:
            - Calls execute_get_request() with wireless.get_access_point_configuration API
            - Converts response camelCase to snake_case via camel_to_snake_case()
            - Logs API request/response at INFO/DEBUG levels
            - Returns None on validation failures (missing MAC, API errors)

        API Configuration:
            - API Family: "wireless"
            - API Function: "get_access_point_configuration"
            - Parameter: key=eth_mac_address
            - Response: Single AP configuration dictionary
            - Authentication: Inherited from self.dnac._session

        Error Handling:
            - Missing eth_mac_address: Returns None with ERROR log
            - No API response: Returns None with DEBUG log (AP may not exist)
            - Invalid API response: Returns None (logged by execute_get_request)
            - Network errors: Propagated from execute_get_request()

        Usage Context:
            Called from get_current_config() in loop iterating all AP devices:
                for ap_detail in current_configuration:
                    eth_mac = ap_detail.get("eth_mac_address")
                    config = self.get_accesspoint_configuration(eth_mac)

        Notes:
            - eth_mac_address must match value from get_accesspoint_details()
            - Configuration snapshot reflects current state at query time
            - Radio configurations list varies by AP model (1-3 radios)
            - Tertiary controller may be null if not configured
            - Snake_case conversion ensures consistency with module conventions
            - None return indicates AP has no retrievable configuration
        """
        self.log(
            "Starting access point configuration retrieval from Cisco Catalyst Center for AP "
            f"with Ethernet MAC address '{eth_mac_address}'. This API call will query the wireless "
            "configuration endpoint to retrieve complete AP settings including radio configurations "
            "(2.4GHz, 5GHz, 6GHz), admin status, LED settings, AP mode, location, failover priority, "
            "and WLC controller assignments.",
            "INFO"
        )

        # Validate required parameter
        if not eth_mac_address:
            self.msg = (
                "Ethernet MAC address is required to retrieve access point configuration from "
                "Cisco Catalyst Center. No MAC address provided in function call. Cannot proceed "
                "with API query. Verify device inventory contains valid 'eth_mac_address' field "
                "from get_accesspoint_details() response."
            )
            self.log(self.msg, "ERROR")
            return None

        self.log(
            f"Ethernet MAC address validation passed: '{eth_mac_address}'. Preparing API request "
            "to query Catalyst Center wireless configuration endpoint with MAC address as key "
            "parameter. Request will retrieve current operational configuration for this AP.",
            "DEBUG"
        )

        # API call configuration
        api_family, api_function, param_key = "wireless", "get_access_point_configuration", "key"
        request_params = {param_key: eth_mac_address}

        self.log(
            "Sending AP configuration API request to Cisco Catalyst Center. API Family: "
            f"'{api_family}', Function: '{api_function}', Parameters: {request_params}. This call "
            "queries the wireless configuration database for AP with Ethernet MAC "
            f"'{eth_mac_address}' and retrieves complete operational settings.",
            "DEBUG"
        )

        # Execute API request
        response = self.execute_get_request(api_family, api_function, request_params)

        if not response:
            self.log(
                "No configuration data received from Catalyst Center API for access point with "
                f"Ethernet MAC address '{eth_mac_address}'. API returned None or empty response. "
                "This indicates either: (1) AP does not exist in Catalyst Center inventory, "
                "(2) AP has no configuration stored, (3) MAC address format incorrect, or "
                "(4) API connectivity issue. Returning None to skip this AP in processing loop.",
                "DEBUG"
            )
            return None

        self.log(
            "Successfully received API response from Catalyst Center for AP with Ethernet MAC "
            f"address '{eth_mac_address}'. Response contains configuration data with camelCase "
            "field names. Converting field names from camelCase to snake_case for internal "
            f"consistency and YAML generation. Raw API response structure: {self.pprint(response)}",
            "DEBUG"
        )

        # Convert camelCase to snake_case for consistency
        current_eth_configuration = self.camel_to_snake_case(response)

        self.log(
            "Successfully retrieved and transformed access point configuration for Ethernet MAC "
            f"address '{eth_mac_address}'. Configuration includes: AP name, admin status, LED "
            "settings, AP mode, location, failover priority, controller assignments (primary, "
            "secondary, tertiary), and radio configurations for all frequency bands. Snake_case "
            f"converted configuration: {self.pprint(current_eth_configuration)}",
            "INFO"
        )

        return current_eth_configuration

    def parse_accesspoint_configuration(self, accesspoint_config, ap_details):
        """
        Parses and normalizes access point configuration data for YAML generation.

        This function transforms raw AP configuration data from Catalyst Center API into a
        normalized structure suitable for Ansible YAML playbook generation. It extracts and
        organizes AP settings, radio configurations, controller assignments, and provisioning
        details while applying field name normalization and value transformation rules.

        Args:
            accesspoint_config (dict): Raw AP configuration from get_accesspoint_configuration().
                                      Contains camelCase API response fields converted to snake_case
                                      including mac_address, ap_name, admin_status, led_status,
                                      radio_dtos, primary/secondary/tertiary controller settings.
            ap_details (dict): Device inventory details from get_accesspoint_details().
                              Contains id, eth_mac_address, hostname, model, serial_number,
                              site_hierarchy, reachability_status, and attached configuration.

        Returns:
            dict: Normalized AP configuration dictionary with structure:
                 {
                     "mac_address": "aa:bb:cc:dd:ee:ff",
                     "ap_name": "AP-Floor1-001",
                     "admin_status": "Enabled",
                     "led_status": "Enabled",
                     "led_brightness_level": 5,
                     "ap_mode": "Local",
                     "location": "Building1-Floor1-Zone1",
                     "failover_priority": "Low",
                     "primary_controller_name": "WLC-Primary",
                     "primary_ip_address": {"address": "10.1.1.1"},
                     "secondary_controller_name": "WLC-Secondary",
                     "secondary_ip_address": {"address": "10.1.1.2"},
                     "tertiary_controller_name": "WLC-Tertiary",
                     "tertiary_ip_address": {"address": "10.1.1.3"},
                     "2.4ghz_radio": {...},
                     "5ghz_radio": {...},
                     "6ghz_radio": {...},
                     "xor_radio": {...},
                     "tri_radio": {...},
                     "clean_air_si_2.4ghz": "Enabled",
                     "clean_air_si_5ghz": "Enabled",
                     "clean_air_si_6ghz": "Disabled",
                     "rf_profile": "HIGH",
                     "site": {
                         "floor": {
                             "parent_name": "Global/USA/Building1",
                             "name": "Floor1"
                         }
                     },
                     "is_assigned_site_as_location": "Enabled"
                 }
                 Returns empty dict if invalid input provided.

        Data Transformations:
            Field Extractions:
                - radio_dtos → per-band radio configuration dictionaries
                - site_hierarchy → site.floor.parent_name + site.floor.name
                - if_type_value → radio key mapping

        Notes:
            - Clean Air SI defaults to "Disabled" for all bands, then enabled per radio
            - Controller inheritance follows hierarchical rules (primary → secondary → tertiary)
            - Provisioned APs require valid site_hierarchy for site extraction
            - Empty parsed_config valid for APs with minimal configuration
        """
        self.log(
            "Starting comprehensive access point configuration parsing. Input configuration: "
            f"{self.pprint(accesspoint_config)}, Device details: {self.pprint(ap_details)}. "
            "Parser will normalize field names, organize radio settings by frequency band, "
            "extract provisioning details, apply controller inheritance rules, and produce "
            "standardized configuration structure for YAML playbook generation.",
            "INFO"
        )

        parsed_config = {}
        if not accesspoint_config or not isinstance(accesspoint_config, dict):
            self.log(
                "Invalid access point configuration provided for parsing. Expected dictionary, "
                f"got {type(accesspoint_config).__name__}. Cannot proceed with configuration "
                "normalization. Returning empty parsed configuration.",
                "ERROR"
            )
            return parsed_config

        self.log(
            "Configuration validation passed. Configuration is valid dictionary with "
            f"{len(accesspoint_config.keys())} field(s). Beginning field-by-field parsing and "
            "normalization process.",
            "DEBUG"
        )

        list_of_ap_keys_to_parse = ["mac_address", "ap_name", "admin_status",
                                    "led_status", "led_brightness_level",
                                    "ap_mode", "location",
                                    "failover_priority", "secondary_controller_name",
                                    "secondary_ip_address", "tertiary_controller_name",
                                    "tertiary_ip_address", "primary_ip_address",
                                    "primary_controller_name"]

        self.log(
            f"Defined {len(list_of_ap_keys_to_parse)} AP configuration fields to parse: "
            f"{list_of_ap_keys_to_parse}. Starting field extraction and transformation loop.",
            "DEBUG"
        )

        for key_index, each_key in enumerate(list_of_ap_keys_to_parse, start=1):
            if each_key == "location":
                if accesspoint_config.get(each_key) == "default location":
                    parsed_config["is_assigned_site_as_location"] = "Enabled"
                    self.log(
                        f"Field {key_index}/{len(list_of_ap_keys_to_parse)} '{each_key}': Value is "
                        "'default location', setting is_assigned_site_as_location='Enabled'. Site "
                        "will be used as AP location.",
                        "DEBUG"
                    )
                else:
                    parsed_config["location"] = accesspoint_config.get(each_key)
                    self.log(
                        f"Field {key_index}/{len(list_of_ap_keys_to_parse)} '{each_key}': Custom "
                        f"location '{accesspoint_config.get(each_key)}' assigned to AP.",
                        "DEBUG"
                    )
            elif each_key in ["tertiary_controller_name", "secondary_controller_name", "primary_controller_name"]:
                if accesspoint_config.get(each_key) in ["Clear", None, ""]:
                    parsed_config[each_key] = "Inherit from site / Clear"
                    self.log(
                        f"Field {key_index}/{len(list_of_ap_keys_to_parse)} '{each_key}': Value is "
                        f"'{accesspoint_config.get(each_key)}', setting to 'Inherit from site / Clear'. "
                        "Controller assignment will inherit from site configuration.",
                        "DEBUG"
                    )
                else:
                    parsed_config[each_key] = accesspoint_config.get(each_key)
                    self.log(
                        f"Field {key_index}/{len(list_of_ap_keys_to_parse)} '{each_key}': Valid "
                        f"controller name '{accesspoint_config.get(each_key)}' assigned.",
                        "DEBUG"
                    )
            elif each_key in ["secondary_ip_address", "tertiary_ip_address", "primary_ip_address"]:
                if accesspoint_config.get(each_key) != "0.0.0.0":
                    parsed_config[each_key] = {
                        "address": accesspoint_config.get(each_key)}
                    self.log(
                        f"Field {key_index}/{len(list_of_ap_keys_to_parse)} '{each_key}': Valid IP "
                        f"address '{accesspoint_config.get(each_key)}' wrapped in address structure.",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"Field {key_index}/{len(list_of_ap_keys_to_parse)} '{each_key}': IP is "
                        f"'0.0.0.0' (unconfigured), skipping field addition to parsed config.",
                        "DEBUG"
                    )
            else:
                parsed_config[each_key] = accesspoint_config.get(each_key)
                self.log(
                    f"Field {key_index}/{len(list_of_ap_keys_to_parse)} '{each_key}': Value "
                    f"'{accesspoint_config.get(each_key)}' copied directly to parsed config.",
                    "DEBUG"
                )

        # Apply controller inheritance rules
        if parsed_config.get("primary_controller_name") in ["Inherit from site / Clear", "Clear", None, ""]:
            self.log(
                f"Primary controller set to inherit mode ('{parsed_config.get('primary_controller_name')}'). "
                f"Removing all controller fields (primary, secondary, tertiary) from parsed config as "
                f"per inheritance rules. AP will use site-level controller assignments.",
                "DEBUG"
            )
            del parsed_config["secondary_controller_name"]
            del parsed_config["tertiary_controller_name"]
            del parsed_config["primary_controller_name"]

        # Initialize Clean Air SI fields (will be updated from radio configs)
        parsed_config["clean_air_si_2.4ghz"] = "Disabled"
        parsed_config["clean_air_si_5ghz"] = "Disabled"
        parsed_config["clean_air_si_6ghz"] = "Disabled"

        self.log(
            "Initialized Clean Air SI fields to 'Disabled' for all bands (2.4GHz, 5GHz, 6GHz). "
            "These will be updated to 'Enabled' if radio configurations specify Clean Air SI.",
            "DEBUG"
        )

        # Parse radio configurations
        radio_config = accesspoint_config.get("radio_dtos")
        if radio_config and isinstance(radio_config, list):
            self.log(
                f"Radio configuration found with {len(radio_config)} radio(s). Starting radio "
                "configuration parsing to extract radio settings for each frequency band. "
                f"Radio data: {radio_config}",
                "INFO"
            )
            parsed_all_radios = {}
            for radio_index, radio in enumerate(radio_config, start=1):
                parsed_radio = {}
                radio_config_key = None
                list_of_radio_keys_to_parse = ["if_type_value", "admin_status", "radio_role_assignment",
                                               "channel", "radio_band", "power_assignment_mode", "clean_air_si",
                                               "channel_width", "powerlevel", "channel_assignment_mode",
                                               "channel_number", "custom_power_level",
                                               "antenna_gain"]

                self.log(
                    f"Processing radio {radio_index}/{len(radio_config)} with {len(list_of_radio_keys_to_parse)} "
                    f"potential fields to extract. Radio data: {radio}",
                    "DEBUG"
                )

                for field_index, each_radio_key in enumerate(list_of_radio_keys_to_parse, start=1):
                    if each_radio_key == "if_type_value":
                        if_type = radio.get(each_radio_key)
                        if if_type == "2.4 GHz":
                            radio_config_key = "2.4ghz_radio"
                        elif if_type == "5 GHz":
                            radio_config_key = "5ghz_radio"
                        elif if_type == "6 GHz":
                            radio_config_key = "6ghz_radio"
                        elif if_type == "Dual Radio":
                            radio_config_key = "xor_radio"
                        elif if_type == "Tri Radio":
                            radio_config_key = "tri_radio"
                        else:
                            radio_config_key = "if_type_value"

                        self.log(
                            f"Radio {radio_index}/{len(radio_config)} field {field_index}/{len(list_of_radio_keys_to_parse)} "
                            f"'{each_radio_key}': Mapped if_type_value '{if_type}' to radio key '{radio_config_key}'.",
                            "DEBUG"
                        )
                    elif each_radio_key == "powerlevel":
                        parsed_radio["power_level"] = radio.get(each_radio_key)
                        self.log(
                            f"Radio {radio_index}/{len(radio_config)} field {field_index}/{len(list_of_radio_keys_to_parse)} "
                            f"'{each_radio_key}': Renamed to 'power_level' with value '{radio.get(each_radio_key)}'.",
                            "DEBUG"
                        )
                    elif each_radio_key == "clean_air_si":
                        if radio.get(each_radio_key) == "Enabled":
                            if radio_config_key == "2.4ghz_radio":
                                parsed_config["clean_air_si_2.4ghz"] = "Enabled"
                            elif radio_config_key == "5ghz_radio":
                                parsed_config["clean_air_si_5ghz"] = "Enabled"
                            elif radio_config_key == "6ghz_radio":
                                parsed_config["clean_air_si_6ghz"] = "Enabled"

                            self.log(
                                f"Radio {radio_index}/{len(radio_config)} field {field_index}/{len(list_of_radio_keys_to_parse)} "
                                f"'{each_radio_key}': Clean Air SI enabled for radio '{radio_config_key}', "
                                f"updated global clean_air_si_{radio_config_key.replace('_radio', '')} field.",
                                "DEBUG"
                            )
                        else:
                            self.log(
                                f"Radio {radio_index}/{len(radio_config)} field {field_index}/{len(list_of_radio_keys_to_parse)} "
                                f"'{each_radio_key}': Clean Air SI disabled for this radio, no update to global field.",
                                "DEBUG"
                            )
                    else:
                        if radio.get(each_radio_key) is not None:
                            parsed_radio[each_radio_key] = radio.get(each_radio_key)
                            self.log(
                                f"Radio {radio_index}/{len(radio_config)} field "
                                f"{field_index}/{len(list_of_radio_keys_to_parse)} "
                                f"'{each_radio_key}': Value '{radio.get(each_radio_key)}' added to radio config.",
                                "DEBUG"
                            )

                # Apply radio-specific rules
                if parsed_radio.get("power_assignment_mode") == "Global":
                    if "power_level" in parsed_radio:
                        del parsed_radio["power_level"]
                    self.log(
                        f"Radio {radio_index}/{len(radio_config)}: Power assignment mode is 'Global', "
                        f"removed 'power_level' field as power is controlled globally.",
                        "DEBUG"
                    )

                if parsed_radio.get("channel_assignment_mode") == "Global":
                    if "channel_number" in parsed_radio:
                        del parsed_radio["channel_number"]
                    self.log(
                        f"Radio {radio_index}/{len(radio_config)}: Channel assignment mode is 'Global', "
                        f"removed 'channel_number' field as channel is controlled globally.",
                        "DEBUG"
                    )

                if radio_config_key:
                    parsed_all_radios[radio_config_key] = parsed_radio
                    self.log(
                        f"Radio {radio_index}/{len(radio_config)}: Successfully parsed radio configuration "
                        f"for '{radio_config_key}'. Parsed radio: {parsed_radio}",
                        "DEBUG"
                    )

            # Add all parsed radio configurations to main config
            parsed_config.update(parsed_all_radios)
            self.log(
                f"Successfully parsed and added {len(parsed_all_radios)} radio configuration(s) "
                f"to AP config. Radio keys: {list(parsed_all_radios.keys())}",
                "INFO"
            )
        else:
            self.log(
                "No radio configuration found in access point config (radio_dtos is None or empty). "
                "AP configuration will not include radio settings.",
                "WARNING"
            )

        # Parse provisioning details if AP is provisioned
        if accesspoint_config.get("provisioning_status"):
            self.log(
                "Access point has provisioning_status=True, indicating AP is provisioned to a site. "
                "Parsing additional provisioning configuration details including site hierarchy and "
                "RF profile settings.",
                "INFO"
            )
            site_hierarchy = ap_details.get("site_hierarchy")
            if site_hierarchy and site_hierarchy not in ["default-location", "default location"]:
                self.log(
                    f"Valid site hierarchy found: '{site_hierarchy}'. Parsing to extract parent "
                    "site path and floor name for site assignment configuration.",
                    "DEBUG"
                )

                try:
                    parent_path, floor = site_hierarchy.rsplit("/", 1)
                    parsed_config["rf_profile"] = "HIGH"
                    parsed_config["site"] = {}
                    parsed_config["site"]["floor"] = {}
                    parsed_config["site"]["floor"]["parent_name"] = parent_path
                    parsed_config["site"]["floor"]["name"] = floor

                    self.log(
                        f"Successfully parsed site hierarchy. Parent path: '{parent_path}', Floor: "
                        f"'{floor}', RF Profile: 'HIGH'. Provisioning details added to parsed config.",
                        "INFO"
                    )
                except ValueError:
                    self.log(
                        f"Failed to parse site hierarchy '{site_hierarchy}'. Site path does not "
                        "contain '/' separator for parent/floor split. Skipping site provisioning "
                        "details in parsed config.",
                        "WARNING"
                    )
            else:
                self.log(
                    f"Site hierarchy is default or invalid ('{site_hierarchy}'). Skipping site "
                    "provisioning details extraction.",
                    "DEBUG"
                )
        else:
            self.log(
                "Access point is not provisioned (provisioning_status=False/None). No site "
                "hierarchy or RF profile will be added to parsed configuration.",
                "DEBUG"
            )

        self.log(
            "Completed comprehensive access point configuration parsing. Parsed configuration "
            f"contains {len(parsed_config.keys())} field(s) including AP settings, radio "
            "configurations, controller assignments, and provisioning details. Final parsed "
            f"config: {self.pprint(parsed_config)}",
            "INFO"
        )
        return parsed_config

    def get_diff_gathered(self):
        """
        Orchestrates access point playbook config generation.

        This function serves as the main workflow orchestrator for the 'gathered' state operation,
        coordinating the execution of YAML configuration generation from existing Catalyst Center
        AP configurations. It manages operation timing, parameter validation, function dispatch,
        and result aggregation for the playbook config generation workflow.

        Args:
            None (uses self.want for operation parameters)

        Returns:
            object: Self instance with updated attributes:
                   - self.status: "success" or "failed" operation status
                   - self.msg: Result message describing operation outcome
                   - self.result: Operation result dictionary with status details

        Side Effects:
            - Calls yaml_config_generator() for YAML file generation
            - Calls check_return_status() to validate operation results
            - Logs workflow progress at INFO, DEBUG, WARNING levels
            - Tracks operation execution time with start/end timestamps
            - Updates self.status and self.msg based on operation outcomes
            - Sets operation_result via set_operation_result() if unprocessed APs exist

        Operations Processed:
            1. yaml_config_generator:
               - Param Key: "yaml_config_generator"
               - Function: self.yaml_config_generator()
               - Purpose: Generate YAML playbook from gathered AP configs
               - Required Params: file_path, generate_all_configurations, global_filters

        Error Handling:
            - Missing parameters: Logs WARNING, skips operation (not treated as error)
            - Unprocessed APs: Sets failed status with WARNING message
            - Operation failures: Detected via check_return_status()
            - Exceptions: Propagated to caller (main() function)

        Notes:
            - Only "gathered" state currently implemented (access point config extraction)
            - Operations list extensible for future state implementations
            - Timing logged at DEBUG level for performance monitoring
            - Empty operations list valid (no-op scenario)
            - check_return_status() may raise exceptions on critical failures
        """
        self.log(
            "Starting comprehensive access point configuration gathering and YAML "
            "playbook config generation workflow. This operation will orchestrate YAML config generation "
            "from existing Catalyst Center AP configurations, including parameter validation, "
            "function dispatch, and result aggregation. Workflow execution time will be tracked "
            "for performance monitoring.",
            "INFO"
        )

        start_time = time.time()
        self.log(
            f"Workflow start time recorded: {start_time}. Beginning 'get_diff_gathered' operation "
            "to process access point configuration extraction and YAML generation.",
            "DEBUG"
        )

        # Define operations to execute in sequence
        operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]

        self.log(
            f"Defined {len(operations)} operation(s) for processing in get_diff_gathered workflow. "
            f"Operations: {[(op[1], op[0]) for op in operations]}. Beginning sequential iteration "
            "to check parameters and execute each operation.",
            "DEBUG"
        )

        # Iterate over operations and process them
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                f"Processing operation {index}/{len(operations)}: '{operation_name}' with parameter "
                f"key '{param_key}'. Checking if parameters exist in self.want dictionary for "
                "this operation.",
                "DEBUG"
            )

            params = self.want.get(param_key)
            if params:
                self.log(
                    f"Operation {index}/{len(operations)}: '{operation_name}' - Parameters found "
                    f"in self.want. Parameter count: {len(params.keys()) if isinstance(params, dict) else 'N/A'}, "
                    f"Parameters: {params}. Starting operation execution by calling {operation_func.__name__}().",
                    "INFO"
                )

                operation_func(params).check_return_status()

                self.log(
                    f"Operation {index}/{len(operations)}: '{operation_name}' - Execution completed. "
                    "check_return_status() validation passed. Operation processed successfully without "
                    "raising exceptions.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"Operation {index}/{len(operations)}: '{operation_name}' - No parameters found "
                    f"in self.want for param_key '{param_key}'. Skipping operation execution. This "
                    "may indicate: (1) Operation not requested in playbook, (2) Parameters filtered "
                    "out during validation, or (3) Operation not applicable to current workflow.",
                    "WARNING"
                )

        end_time = time.time()
        execution_duration = end_time - start_time

        self.log(
            f"Completed 'get_diff_gathered' operation processing. Workflow end time: {end_time}, "
            f"Total execution duration: {execution_duration:.2f} seconds. All {len(operations)} "
            "operation(s) processed (executed or skipped based on parameter availability). "
            "Checking for unprocessed APs to determine final workflow status.",
            "DEBUG"
        )

        # Check for unprocessed APs and set failure status if any exist
        if self.have.get("unprocessed"):
            unprocessed_count = len(self.have.get("unprocessed"))
            self.msg = (
                f"Brownfield AP gathering workflow completed with partial success. {unprocessed_count} "
                "access point configuration(s) were not processed due to filter mismatches or "
                "missing data in Catalyst Center. Unprocessed AP identifiers: "
                f"{str(self.have.get('unprocessed'))}. Verify filter values match existing APs "
                "and check Catalyst Center inventory for missing configurations."
            )
            self.set_operation_result("failed", False, self.msg, "WARNING")

            self.log(
                f"Setting workflow status to 'failed' due to {unprocessed_count} unprocessed AP(s). "
                "This indicates filter mismatches or incomplete AP data in Catalyst Center. Review "
                f"unprocessed list for troubleshooting: {self.have.get('unprocessed')}",
                "WARNING"
            )

        return self

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates Ansible-compatible YAML playbook from gathered access point configurations.

        This function orchestrates the complete YAML generation workflow by processing global
        filters, aggregating AP configurations, and writing formatted YAML content to file.
        It supports two operational modes: generate_all (complete discovery) and filtered
        (targeted extraction based on site, hostname, or MAC filters).

        Args:
            yaml_config_generator (dict): YAML generation configuration containing:
                - file_path (str, optional): Custom output file path for YAML
                - generate_all_configurations (bool, optional, default=False):
                    Generate YAML for ALL APs in Catalyst Center
                - global_filters (dict, optional): Filter criteria for targeted extraction
                    * site_list: Floor site hierarchies
                    * provision_hostname_list: Provisioned AP hostnames
                    * accesspoint_config_list: AP configuration hostnames
                    * accesspoint_provision_config_list: Combined provision/config hostnames
                    * accesspoint_provision_config_mac_list: AP MAC addresses

        Returns:
            object: Self instance with updated attributes:
                   - self.status: "success" or "failed" generation status
                   - self.msg: Result message dictionary with file_path
                   - self.result: Operation result with changed status

        Operational Modes:
            Generate All Mode (generate_all_configurations=True):
                - Retrieves ALL AP configurations from self.have
                - No filtering applied, ignores global_filters if provided
                - Logs warning if global_filters provided (filters ignored)

            Filtered Mode (global_filters provided):
                - Applies hierarchical filter priority
                - Calls process_global_filters() to match APs
                - Supports site, hostname, MAC address filtering
                - Returns only APs matching filter criteria

        Filter Priority (in process_global_filters):
            1. site_list (highest priority)
            2. provision_hostname_list
            3. accesspoint_config_list
            4. accesspoint_provision_config_list
            5. accesspoint_provision_config_mac_list (lowest priority)

        File Naming:
            - Custom path: Uses yaml_config_generator["file_path"] if provided
            - Auto-generated: Calls generate_filename() to create timestamp-based name
                             Format: accesspoint_workflow_manager_<timestamp>.yaml

        Error Handling:
            - No configurations found: Returns success with INFO message (no-op)
            - Invalid global_filters: Handled by process_global_filters()
            - YAML write failure: Sets failed status with ERROR message
            - Empty file_path: Falls back to auto-generated filename

        Notes:
            - generate_all mode overrides any provided global_filters
            - Empty final_list is valid (e.g., filters too restrictive)
            - Module name hardcoded to self.module_name for messages
            - write_dict_to_yaml() handles file I/O and formatting
            - Operation result includes file_path in message for verification
        """
        self.log(
            "Starting comprehensive YAML playbook generation workflow for access point "
            f"configurations. Input parameters: {yaml_config_generator}. This operation will "
            "process filters, aggregate AP configurations, and generate Ansible-compatible YAML "
            "playbook file for access point playbook config automation.",
            "DEBUG"
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log(
                "Generate all configurations mode enabled (generate_all_configurations=True). Will "
                "collect ALL access point configurations from Cisco Catalyst Center without applying "
                "any filter criteria. This mode performs complete access point configuration extraction.",
                "INFO"
            )

        # Determine output file path
        self.log(
            "Determining output file path for YAML configuration playbook. Checking if custom "
            "file_path provided in input parameters or if default filename generation needed.",
            "DEBUG"
        )

        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No custom file_path provided by user in configuration parameters. Generating "
                "default filename using timestamp pattern for unique playbook identification.",
                "DEBUG"
            )
            file_path = self.generate_filename()
            self.log(
                f"Generated default filename: '{file_path}'. YAML playbook will be written to this "
                "auto-generated path with timestamp-based naming convention.",
                "INFO"
            )
        else:
            self.log(
                f"Using user-provided custom file_path: '{file_path}'. YAML playbook output will "
                "be written to specified location. Ensure parent directory exists and is writable.",
                "DEBUG"
            )

        self.log(
            f"YAML configuration file path finalized: '{file_path}'. File will be created at "
            f"this location after configuration aggregation and formatting.",
            "DEBUG"
        )

        # Initialize filter dictionaries and result list
        self.log(
            "Initializing filter dictionaries and result collection lists for AP configuration "
            "processing. Empty filters indicate no specific criteria - collect all APs.",
            "DEBUG"
        )

        global_filters = {}
        final_list = []

        # Process generate_all mode
        if generate_all:
            self.log(
                "Executing generate_all_configurations workflow. Retrieving complete AP configuration "
                "list from self.have['all_ap_config'] without filter application. This will include "
                "ALL access points discovered in Catalyst Center inventory.",
                "DEBUG"
            )

            final_list = self.have.get("all_ap_config", [])

            self.log(
                f"Collected {len(final_list)} access point configuration(s) in generate_all mode. "
                f"All discovered APs will be included in YAML playbook. Configuration list: {final_list}",
                "DEBUG"
            )

            # Check if global_filters provided (will be ignored)
            if yaml_config_generator.get("global_filters"):
                self.log(
                    "WARNING: global_filters provided in configuration parameters but generate_all_configurations "
                    "mode is enabled (True). Global filters WILL BE IGNORED and all AP configurations "
                    "will be included in YAML output. To use filters, set generate_all_configurations=False.",
                    "WARNING"
                )

        # Process filtered mode
        else:
            self.log(
                "Generate all mode disabled (generate_all_configurations=False). Checking for "
                "global_filters parameter to determine targeted extraction criteria. Filtered mode "
                "will apply hierarchical filter priority to match specific APs.",
                "INFO"
            )

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}

            if global_filters:
                self.log(
                    "Global filters detected in configuration parameters. Filter types provided: "
                    f"{list(global_filters.keys())}. Calling process_global_filters() to apply "
                    "hierarchical filter matching and extract targeted AP configurations. Filters: "
                    f"{global_filters}",
                    "INFO"
                )

                final_list = self.process_global_filters(global_filters)

                if final_list:
                    self.log(
                        f"Filter processing completed successfully. Matched {len(final_list)} access "
                        "point configuration(s) against provided global filters. Filtered APs will "
                        "be included in YAML playbook.",
                        "INFO"
                    )
                else:
                    self.log(
                        "Filter processing completed but NO access points matched the provided "
                        f"global filters: {global_filters}. This may indicate: (1) Filter values "
                        "don't match existing APs, (2) Filters too restrictive, or (3) No APs "
                        "configured in Catalyst Center. Empty final_list will trigger no-op message.",
                        "WARNING"
                    )
            else:
                self.log(
                    "No global_filters provided in configuration parameters and generate_all mode "
                    "disabled. This configuration is invalid - at least one of generate_all_configurations "
                    "or global_filters must be specified. Final list will be empty.",
                    "WARNING"
                )

        # Validate final_list is not empty
        if not final_list:
            self.msg = (
                f"No configurations or components found to process for module '{self.module_name}'. "
                "This indicates either: (1) No access points discovered in Catalyst Center, "
                "(2) Global filters didn't match any APs, or (3) Invalid configuration parameters. "
                "Verify input filters match existing AP inventory and check Catalyst Center has "
                "onboarded access points. No YAML file will be generated."
            )
            self.set_operation_result("success", False, self.msg, "INFO")

            self.log(
                "YAML generation workflow completed with no-op status. Final configuration list "
                "is empty - no YAML playbook generated. Check filter criteria or Catalyst Center "
                "AP inventory for troubleshooting.",
                "INFO"
            )
            return self

        # Wrap configurations in {"config": list} structure for Ansible compatibility
        final_dict = {"config": final_list}

        self.log(
            f"Created final YAML dictionary structure with {len(final_list)} AP configuration(s) "
            "wrapped in 'config' key for Ansible playbook compatibility. Final dictionary ready "
            f"for YAML serialization: {final_dict}",
            "DEBUG"
        )

        # Write dictionary to YAML file
        self.log(
            "Calling write_dict_to_yaml() to serialize final configuration dictionary and write "
            f"YAML content to file '{file_path}'. This will create formatted YAML playbook with "
            "proper indentation and structure.",
            "DEBUG"
        )

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                f"YAML config generation task succeeded for module '{self.module_name}'.": {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")

            self.log(
                f"YAML playbook file successfully created at '{file_path}'. File contains "
                f"{len(final_list)} access point configuration(s) in Ansible-compatible format. "
                "Playbook ready for automation workflows.",
                "INFO"
            )
        else:
            self.msg = {
                f"YAML config generation task failed for module '{self.module_name}'.": {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

            self.log(
                f"YAML playbook file creation FAILED for path '{file_path}'. write_dict_to_yaml() "
                "returned False, indicating file write error. Verify: (1) Parent directory exists, "
                "(2) Write permissions sufficient, (3) Disk space available, (4) Path is valid. "
                "Check system logs for detailed error information.",
                "ERROR"
            )

        return self

    def process_global_filters(self, global_filters):
        """
        Applies hierarchical global filters to access point configurations for targeted extraction.

        This function processes user-defined filter criteria to match and extract specific AP
        configurations from the complete inventory. It implements a hierarchical filter priority
        system where only ONE filter type is processed (highest priority wins), supporting
        site-based, hostname-based, and MAC address-based filtering with special handling for
        provisioned vs. configured APs.

        Args:
            global_filters (dict): Filter criteria dictionary containing one or more filter types:
                - site_list (list[str]): Floor site hierarchies for location-based filtering
                - provision_hostname_list (list[str]): Provisioned AP hostnames
                - accesspoint_config_list (list[str]): AP configuration hostnames
                - accesspoint_provision_config_list (list[str]): Combined provision/config hostnames
                - accesspoint_provision_config_mac_list (list[str]): AP MAC addresses

        Returns:
            list: Filtered AP configuration dictionaries matching criteria. Structure varies by filter:
                 Site Filter: Returns complete AP configs from matching sites
                 Provision Filter: Returns minimal {mac_address, rf_profile, site} dicts
                 Config Filter: Returns full configs with rf_profile/site removed
                 Combined Filter: Returns complete AP configs matching hostnames
                 MAC Filter: Returns complete AP configs matching MAC addresses
                 Returns None if no matches found or errors occur.

        Side Effects:
            - Calls find_multiple_dict_by_key_value() to search AP configurations
            - Updates self.have["unprocessed"] with filter mismatches
            - Calls fail_and_exit() on critical errors (no APs in inventory)
            - Logs filtering progress at INFO, DEBUG, WARNING levels

        Filter Priority (Hierarchical - First Match Wins):
            1. site_list (HIGHEST - location-based filtering)
            2. provision_hostname_list (AP provisioning to sites)
            3. accesspoint_config_list (AP configuration settings)
            4. accesspoint_provision_config_list (combined provision + config)
            5. accesspoint_provision_config_mac_list (LOWEST - MAC address-based)

        Special Filter Values:
            - ["all"] (case-insensitive): Matches ALL APs for that filter type
            - Empty list or missing: Filter type skipped
            - Only ONE filter type processed per call (hierarchical priority)

        Filter Type Behaviors:
            site_list:
                - Matches APs by "location" field
                - ["all"]: Returns all AP configs unchanged
                - Specific sites: Returns APs from matching site hierarchies
                - Mismatches: Logged in unprocessed list

            provision_hostname_list:
                - Matches APs with rf_profile="HIGH" (provisioned indicator)
                - ["all"]: Returns minimal provision configs for all provisioned APs
                - Specific hosts: Returns provision configs for matching hostnames
                - Returns: {mac_address, rf_profile, site} structure only
                - Mismatches: Logged in unprocessed list

            accesspoint_config_list:
                - Matches APs by "ap_name" field
                - ["all"]: Returns all configs with rf_profile/site removed
                - Specific names: Returns configs for matching AP names
                - Removes: rf_profile and site keys from each config
                - Mismatches: Logged in unprocessed list

            accesspoint_provision_config_list:
                - Matches APs by "ap_name" field
                - ["all"]: Returns all AP configs unchanged
                - Specific hosts: Returns full configs for matching hostnames
                - Returns: Complete AP configurations
                - Mismatches: Logged in unprocessed list

            accesspoint_provision_config_mac_list:
                - Matches APs by "mac_address" field
                - ["all"]: Returns all AP configs unchanged
                - Specific MACs: Returns full configs for matching MAC addresses
                - Returns: Complete AP configurations
                - Mismatches: Logged in unprocessed list

        Error Handling:
            - No APs in self.have["all_ap_config"]: Calls fail_and_exit() with CRITICAL error
            - Filter value not found: Logs WARNING, adds to unprocessed list, continues
            - All filter values invalid: Calls fail_and_exit() with empty results error
            - Multiple filters provided: Only processes highest priority filter

        Unprocessed Tracking:
            - Each filter mismatch appended to unprocessed_aps list
            - Format: "<identifier>: Unable to find <type> in the catalyst center."
            - Unprocessed list stored in self.have["unprocessed"] at function end
            - Logged at WARNING level with full list details

        Notes:
            - Only ONE filter type processed per invocation (hierarchy enforced)
            - "all" filter value is case-insensitive ("all", "ALL", "All" all work)
            - Provision filter returns minimal structure (mac, rf_profile, site only)
            - Config filter removes provisioning fields (rf_profile, site)
            - deep copy used for config filter to avoid modifying self.have data
            - Empty results trigger fail_and_exit() to halt workflow
        """
        self.log(
            "Starting comprehensive global filter processing for access point configuration "
            f"extraction. Provided global filters: {global_filters}. This operation will apply "
            "hierarchical filter priority (site > provision_hostname > config > combined > MAC) "
            "to match and extract targeted AP configurations from complete inventory.",
            "DEBUG"
        )

        # Extract filter lists from global_filters dictionary
        site_list = global_filters.get("site_list")
        provision_hostname_list = global_filters.get("provision_hostname_list")
        accesspoint_config_list = global_filters.get("accesspoint_config_list")
        accesspoint_provision_config_list = global_filters.get("accesspoint_provision_config_list")
        accesspoint_provision_config_mac_list = global_filters.get("accesspoint_provision_config_mac_list")

        final_list = []
        unprocessed_aps = []

        self.log(
            f"Extracted filter types from global_filters: site_list={bool(site_list)}, "
            f"provision_hostname_list={bool(provision_hostname_list)}, "
            f"accesspoint_config_list={bool(accesspoint_config_list)}, "
            f"accesspoint_provision_config_list={bool(accesspoint_provision_config_list)}, "
            f"accesspoint_provision_config_mac_list={bool(accesspoint_provision_config_mac_list)}. "
            "Hierarchical priority will determine which filter type is processed.",
            "DEBUG"
        )

        # Validate AP configuration inventory exists
        if not self.have.get("all_ap_config"):
            self.msg = (
                "No access points configuration found in Cisco Catalyst Center inventory. "
                "self.have['all_ap_config'] is empty or None. Cannot proceed with filter processing. "
                "Verify: (1) APs onboarded to Catalyst Center, (2) get_current_config() executed "
                "successfully, (3) API permissions sufficient. Halting workflow with critical error."
            )
            self.log(self.msg, "WARNING")
            self.fail_and_exit(self.msg)

        self.log(
            f"AP configuration inventory validation passed. Found {len(self.have.get('all_ap_config'))} "
            "access point configuration(s) in self.have['all_ap_config']. Proceeding with "
            "hierarchical filter matching.",
            "DEBUG"
        )

        # FILTER PRIORITY 1: site_list (location-based filtering)
        if site_list and isinstance(site_list, list):
            self.log(
                f"Processing HIGHEST priority filter: site_list with {len(site_list)} site(s). "
                "Will match APs by 'location' field against provided site hierarchies. Site list: "
                f"{site_list}",
                "DEBUG"
            )

            if len(site_list) == 1 and site_list[0].lower() == "all":
                self.log(
                    "Special filter value 'all' detected in site_list. Returning ALL access point "
                    "configurations from inventory without filtering. This matches all sites.",
                    "INFO"
                )
                final_list = self.have.get("all_ap_config", [])
            else:
                ap_config_site_list = []
                for site_index, floor in enumerate(site_list, start=1):
                    self.log(
                        f"Processing site filter {site_index}/{len(site_list)}: '{floor}'. Searching "
                        f"AP configurations for location field matching this site hierarchy.",
                        "DEBUG"
                    )

                    ap_site_exist = self.find_multiple_dict_by_key_value(
                        self.have.get("all_ap_config", []), "location", floor)

                    if not ap_site_exist:
                        self.log(
                            f"Site filter {site_index}/{len(site_list)}: Site hierarchy '{floor}' NOT "
                            f"found in AP configurations. No APs assigned to this site. Adding to "
                            f"unprocessed list.",
                            "WARNING"
                        )
                        unprocessed_aps.append(f"{floor}: Unable to find the configuration for the site hierarchy in the catalyst center.")
                        continue

                    self.log(
                        f"Site filter {site_index}/{len(site_list)}: Found {len(ap_site_exist)} AP(s) "
                        f"with location matching '{floor}'. Adding to filtered collection.",
                        "INFO"
                    )
                    ap_config_site_list.extend(ap_site_exist)

                final_list = ap_config_site_list

            self.log(
                f"Site list filtering completed. Collected {len(final_list)} AP configuration(s) "
                f"matching site filter criteria: {site_list}. Filtered configurations: {final_list}",
                "DEBUG"
            )

        # FILTER PRIORITY 2: provision_hostname_list (provisioned AP filtering)
        elif provision_hostname_list and isinstance(provision_hostname_list, list):
            self.log(
                "Processing SECOND priority filter: provision_hostname_list with "
                f"{len(provision_hostname_list)} hostname(s). Will match provisioned APs (rf_profile='HIGH') "
                f"and return minimal provision configs. Hostname list: {provision_hostname_list}",
                "DEBUG"
            )

            if len(provision_hostname_list) == 1 and provision_hostname_list[0].lower() == "all":
                self.log(
                    "Special filter value 'all' detected in provision_hostname_list. Collecting ALL "
                    "provisioned access points (rf_profile='HIGH') from inventory.",
                    "INFO"
                )

                ap_exist = self.find_multiple_dict_by_key_value(
                    self.have["all_ap_config"], "rf_profile", "HIGH")

                if not ap_exist:
                    self.log(
                        "No provisioned access points found in Catalyst Center inventory. No APs "
                        "have rf_profile='HIGH'. Halting workflow with critical error.",
                        "WARNING"
                    )
                    self.msg = "No provisioned access points found in the catalyst center."
                    self.fail_and_exit(self.msg)

                provisioned_aps = []
                for ap_index, each_ap in enumerate(ap_exist, start=1):
                    provision_config = {
                        "mac_address": each_ap.get("mac_address"),
                        "rf_profile": each_ap.get("rf_profile"),
                        "site": each_ap.get("site")
                    }
                    provisioned_aps.append(provision_config)

                    self.log(
                        f"Provisioned AP {ap_index}/{len(ap_exist)}: Extracted minimal provision "
                        f"config - MAC: '{each_ap.get('mac_address')}', RF Profile: '{each_ap.get('rf_profile')}', "
                        f"Site: {each_ap.get('site')}",
                        "DEBUG"
                    )

                final_list = provisioned_aps
                self.log(
                    f"Collected {len(final_list)} provisioned AP configuration(s) for 'all' filter.",
                    "INFO"
                )
            else:
                provisioned_aps = []
                for host_index, each_host in enumerate(provision_hostname_list, start=1):
                    self.log(
                        f"Processing provision hostname filter {host_index}/{len(provision_hostname_list)}: "
                        f"'{each_host}'. Checking if provisioned AP config exists in inventory.",
                        "INFO"
                    )

                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_host)

                    if not ap_exist:
                        self.log(
                            f"Provision hostname filter {host_index}/{len(provision_hostname_list)}: "
                            f"Hostname '{each_host}' NOT found in AP configurations. Adding to unprocessed list.",
                            "WARNING"
                        )
                        unprocessed_aps.append(f"{each_host}: Unable to find the hostname in the catalyst center.")
                        continue

                    self.log(
                        f"Provision hostname filter {host_index}/{len(provision_hostname_list)}: "
                        f"Found AP '{each_host}'. Extracting minimal provision config.",
                        "INFO"
                    )

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

            self.log(
                f"Provision hostname list filtering completed. Collected {len(final_list)} provisioned "
                f"AP configuration(s) for hostnames: {provision_hostname_list}. Filtered configs: {final_list}",
                "DEBUG"
            )

        # FILTER PRIORITY 3: accesspoint_config_list (configuration-only filtering)
        elif accesspoint_config_list and isinstance(accesspoint_config_list, list):
            self.log(
                "Processing THIRD priority filter: accesspoint_config_list with "
                f"{len(accesspoint_config_list)} AP name(s). Will match APs and remove rf_profile/site "
                f"fields from configs. AP name list: {accesspoint_config_list}",
                "DEBUG"
            )

            ap_config_list = []
            keys_to_remove = ["rf_profile", "site"]

            if len(accesspoint_config_list) == 1 and accesspoint_config_list[0].lower() == "all":
                self.log(
                    "Special filter value 'all' detected in accesspoint_config_list. Collecting ALL "
                    "AP configurations and removing provisioning fields (rf_profile, site).",
                    "INFO"
                )

                ap_config_list = copy.deepcopy(self.have.get("all_ap_config", []))
                for ap_index, each_ap in enumerate(ap_config_list, start=1):
                    for key in keys_to_remove:
                        if each_ap.get(key):
                            del each_ap[key]

                    self.log(
                        f"AP config {ap_index}/{len(ap_config_list)}: Removed provisioning fields "
                        f"from AP '{each_ap.get('ap_name')}'. Config ready for configuration-only operations.",
                        "DEBUG"
                    )

                self.log(
                    f"Collected {len(ap_config_list)} AP configuration(s) for 'all' filter with "
                    f"provisioning fields removed. Configs: {ap_config_list}",
                    "INFO"
                )
                final_list = ap_config_list
            else:
                for ap_name_index, each_ap_name in enumerate(accesspoint_config_list, start=1):
                    self.log(
                        f"Processing AP config filter {ap_name_index}/{len(accesspoint_config_list)}: "
                        f"'{each_ap_name}'. Checking if AP config exists in inventory.",
                        "INFO"
                    )

                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_ap_name)

                    if not ap_exist:
                        self.log(
                            f"AP config filter {ap_name_index}/{len(accesspoint_config_list)}: AP name "
                            f"'{each_ap_name}' NOT found in configurations. Adding to unprocessed list.",
                            "WARNING"
                        )
                        unprocessed_aps.append(f"{each_ap_name}: Unable to find the hostname in the catalyst center.")
                        continue

                    self.log(
                        f"AP config filter {ap_name_index}/{len(accesspoint_config_list)}: Found AP "
                        f"'{each_ap_name}'. Removing provisioning fields and adding to collection.",
                        "INFO"
                    )

                    for each_ap in ap_exist:
                        for key in keys_to_remove:
                            if each_ap.get(key):
                                del each_ap[key]

                    ap_config_list.extend(ap_exist)

                if not ap_config_list:
                    self.msg = f"No access points found matching the provided list. {accesspoint_config_list}."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = ap_config_list

            self.log(
                f"Access point config list filtering completed. Collected {len(final_list)} AP "
                f"configuration(s) for AP names: {accesspoint_config_list}. Filtered configs: {final_list}",
                "DEBUG"
            )

        # FILTER PRIORITY 4: accesspoint_provision_config_list (combined provision + config filtering)
        elif accesspoint_provision_config_list and isinstance(accesspoint_provision_config_list, list):
            self.log(
                "Processing FOURTH priority filter: accesspoint_provision_config_list with "
                f"{len(accesspoint_provision_config_list)} hostname(s). Will match APs and return "
                f"complete configs (provision + configuration). Hostname list: {accesspoint_provision_config_list}",
                "DEBUG"
            )

            if len(accesspoint_provision_config_list) == 1 and accesspoint_provision_config_list[0].lower() == "all":
                self.log(
                    "Special filter value 'all' detected in accesspoint_provision_config_list. "
                    "Returning ALL AP configurations (complete with provision + config fields).",
                    "INFO"
                )
                final_list = self.have.get("all_ap_config", [])
                self.log(
                    f"Collected {len(final_list)} complete AP configuration(s) for 'all' filter. "
                    f"Configs: {final_list}",
                    "INFO"
                )
            else:
                collected_aps = []
                for host_index, each_host_name in enumerate(accesspoint_provision_config_list, start=1):
                    self.log(
                        f"Processing combined filter {host_index}/{len(accesspoint_provision_config_list)}: "
                        f"'{each_host_name}'. Checking if complete AP config exists in inventory.",
                        "INFO"
                    )

                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_host_name)

                    if not ap_exist:
                        self.log(
                            f"Combined filter {host_index}/{len(accesspoint_provision_config_list)}: "
                            f"Hostname '{each_host_name}' NOT found in configurations. Adding to unprocessed list.",
                            "WARNING"
                        )
                        unprocessed_aps.append(f"{each_host_name}: Unable to find the hostname in the catalyst center.")
                        continue

                    self.log(
                        f"Combined filter {host_index}/{len(accesspoint_provision_config_list)}: Found "
                        f"AP '{each_host_name}'. Adding complete config to collection. Config: {ap_exist}",
                        "INFO"
                    )

                    collected_aps.extend(ap_exist)

                if not collected_aps:
                    self.msg = "No access points found matching the provided hostname list."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = collected_aps

            self.log(
                f"Access point provision config list filtering completed. Collected {len(final_list)} "
                f"complete AP configuration(s) for hostnames: {accesspoint_provision_config_list}. "
                f"Filtered configs: {final_list}",
                "DEBUG"
            )

        # FILTER PRIORITY 5: accesspoint_provision_config_mac_list (MAC address filtering)
        elif accesspoint_provision_config_mac_list and isinstance(accesspoint_provision_config_mac_list, list):
            self.log(
                "Processing LOWEST priority filter: accesspoint_provision_config_mac_list with "
                f"{len(accesspoint_provision_config_mac_list)} MAC address(es). Will match APs by "
                f"'mac_address' field and return complete configs. MAC list: {accesspoint_provision_config_mac_list}",
                "DEBUG"
            )

            if len(accesspoint_provision_config_mac_list) == 1 and accesspoint_provision_config_mac_list[0].lower() == "all":
                self.log(
                    "Special filter value 'all' detected in accesspoint_provision_config_mac_list. "
                    "Returning ALL AP configurations without MAC-based filtering.",
                    "INFO"
                )
                final_list = self.have.get("all_ap_config", [])
                self.log(
                    f"Collected {len(final_list)} AP configuration(s) for 'all' filter. Configs: {final_list}",
                    "INFO"
                )
            else:
                collected_aps = []
                for mac_index, each_mac in enumerate(accesspoint_provision_config_mac_list, start=1):
                    self.log(
                        f"Processing MAC filter {mac_index}/{len(accesspoint_provision_config_mac_list)}: "
                        f"'{each_mac}'. Checking if AP config with this MAC exists in inventory.",
                        "INFO"
                    )

                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "mac_address", each_mac)

                    if not ap_exist:
                        self.log(
                            f"MAC filter {mac_index}/{len(accesspoint_provision_config_mac_list)}: MAC "
                            f"address '{each_mac}' NOT found in configurations. Adding to unprocessed list.",
                            "WARNING"
                        )
                        unprocessed_aps.append(
                            f"{each_mac}: Unable to find configuration for the MAC address in the catalyst center.")
                        continue

                    self.log(
                        f"MAC filter {mac_index}/{len(accesspoint_provision_config_mac_list)}: Found AP "
                        f"with MAC '{each_mac}'. Adding complete config to collection. Config: {ap_exist}",
                        "INFO"
                    )

                    collected_aps.extend(ap_exist)

                if not collected_aps:
                    self.msg = "No access points found matching the provided mac address list."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = collected_aps

            self.log(
                f"Access point MAC address list filtering completed. Collected {len(final_list)} AP "
                f"configuration(s) for MAC addresses: {accesspoint_provision_config_mac_list}. "
                f"Filtered configs: {final_list}",
                "DEBUG"
            )

        # No specific filters provided
        else:
            self.log(
                "No specific global filters provided in filter dictionary. No filter criteria matched "
                "hierarchical priority (site_list, provision_hostname_list, accesspoint_config_list, "
                "accesspoint_provision_config_list, accesspoint_provision_config_mac_list). Final list "
                "will remain empty.",
                "DEBUG"
            )

        # Handle unprocessed APs
        if unprocessed_aps:
            self.msg = {
                "The following access points could not be processed:": unprocessed_aps
            }
            self.log(
                f"Filter processing completed with {len(unprocessed_aps)} unprocessed AP identifier(s). "
                "These APs/sites/MACs did not match any configurations in Catalyst Center inventory. "
                f"Unprocessed list: {self.msg}",
                "WARNING"
            )
            self.have["unprocessed"] = unprocessed_aps

        # Validate final_list is not empty
        if not final_list:
            self.log(
                "No access points matched the provided global filter criteria. Final filtered list "
                "is empty. This may indicate: (1) Filter values don't match existing APs, "
                "(2) Filters too restrictive, or (3) No APs in Catalyst Center. Returning None.",
                "WARNING"
            )
            return None

        self.log(
            "Global filter processing completed successfully. Final filtered list contains "
            f"{len(final_list)} access point configuration(s) matching filter criteria. Returning "
            "filtered configurations for YAML generation.",
            "INFO"
        )

        return final_list


def main():
    """
    Main entry point for the Cisco Catalyst Center access point playbook config generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for access point configurations.

    Purpose:
        Initializes and executes the access point playbook config generator
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
    # This creates the main orchestrator for access point configuration extraction
    ccc_accesspoint_playbook_generator = AccessPointPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_accesspoint_playbook_generator.log(
        f"Starting Ansible module execution for access point playbook config "
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

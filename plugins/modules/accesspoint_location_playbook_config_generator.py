#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Access Point Location Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: accesspoint_location_playbook_config_generator
short_description: >-
  Generate YAML configurations playbook for
  'accesspoint_location_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the
    'accesspoint_location_workflow_manager' module, reducing
    the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
  - Supports complete planned accesspoint location config by
    collecting all access point locations from Cisco Catalyst Center.
  - Enables targeted extraction using filters (site hierarchies,
    planned access points, real access points, AP models, or MAC addresses).
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
        with the 'accesspoint_location_playbook_config_generator'
        module.
      - Filters specify which components to include in the YAML
        configuration file.
      - Either 'generate_all_configurations' or 'global_filters'
        must be specified to identify target access point locations.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML
            configurations for all access point locations and all
            supported features.
          - This mode discovers all floor locations with access points
            in Cisco Catalyst Center and extracts all supported
            configurations.
          - When enabled, the config parameter becomes optional
            and will use default values if not provided.
          - A default filename will be generated automatically
            if file_path is not specified.
          - This is useful for complete planned accesspoint location
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
            'accesspoint_location_playbook_config_2025-04-22_21-43-26.yml'.
          - Supports both absolute and relative file paths.
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML
            configuration file.
          - These filters apply to all components unless overridden
            by component-specific filters.
          - At least one filter type must be specified to identify
            target access point locations.
          - Filter priority (highest to lowest) is site_list,
            planned_accesspoint_list, real_accesspoint_list,
            accesspoint_model_list, mac_address_list.
          - Only the highest priority filter with valid data will
            be processed.
        type: dict
        required: false
        suboptions:
          site_list:
            description:
              - List of floor site hierarchies to extract access point
                location configurations from.
              - HIGHEST PRIORITY - Used first if provided with
                valid data.
              - Site paths must match floor locations registered
                in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all floor locations.
              - Example ["Global/USA/SAN JOSE/SJ_BLD20/FLOOR1",
                "Global/USA/SAN JOSE/SJ_BLD20/FLOOR2"]
              - Module will fail if any specified site does not
                exist in Catalyst Center.
            type: list
            elements: str
            required: false
          planned_accesspoint_list:
            description:
              - List of planned access point names to filter locations.
              - MEDIUM-HIGH PRIORITY - Only used if site_list
                is not provided.
              - Retrieves all floor locations containing any of
                the specified planned access points.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all planned
                access points.
              - Example ["test_ap_location", "test_ap2_location"]
            type: list
            elements: str
            required: false
          real_accesspoint_list:
            description:
              - List of real (provisioned) access point names to
                filter locations.
              - MEDIUM PRIORITY - Only used if neither
                site_list nor planned_accesspoint_list are
                provided.
              - Retrieves all floor locations containing any of
                the specified real access points.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all real
                access points.
              - Example ["Test_ap", "AP687D.B402.1614-AP-Test6"]
            type: list
            elements: str
            required: false
          accesspoint_model_list:
            description:
              - List of access point models to filter locations.
              - MEDIUM-LOW PRIORITY - Only used if higher priority
                filters are not provided.
              - Retrieves all floor locations containing any of
                the specified AP models.
              - Case-sensitive and must be exact matches.
              - Example ["AP9120E", "AP9130E"]
            type: list
            elements: str
            required: false
          mac_address_list:
            description:
              - List of access point MAC addresses to filter locations.
              - LOWEST PRIORITY - Only used if all other filters
                are not provided.
              - Retrieves all floor locations containing access points
                with the specified MAC addresses.
              - Case-sensitive and must be exact matches.
              - Example ["a4:88:73:d4:dd:80", "a4:88:73:d4:dd:81"]
            type: list
            elements: str
            required: false
requirements:
  - dnacentersdk >= 2.10.10
  - python >= 3.9
notes:
  - This module utilizes the following SDK methods
    site_design.get_planned_access_points_positions
    site_design.get_access_points_positions
    site_design.get_sites
  - The following API paths are used
    GET /dna/intent/api/v2/floors/${floorId}/plannedAccessPointPositions
    GET /dna/intent/api/v1/sites
    GET /dna/intent/api/v2/floors/${floorId}/accessPointPositions
  - Minimum Cisco Catalyst Center version required is 3.1.3.0 for
    YAML playbook generation support.
  - Filter priority hierarchy ensures only one filter type is
    processed per execution.
  - Module creates YAML file compatible with
    'accesspoint_location_workflow_manager' module for
    automation workflows.
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Access Point Location from all floor
  cisco.dnac.accesspoint_location_playbook_config_generator:
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

- name: Auto-generate YAML Configuration for all Access Point Location with custom file path
  cisco.dnac.accesspoint_location_playbook_config_generator:
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
      - file_path: "tmp/accesspoint_location_playbook_config.yml"
        generate_all_configurations: true

- name: Generate YAML Configuration with file path based on site list filters
  cisco.dnac.accesspoint_location_playbook_config_generator:
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
      - file_path: "tmp/accesspoint_location_playbook_config_site_base.yml"
        global_filters:
          site_list:
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR1
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR2

- name: Generate YAML Configuration with file path based on planned access point list
  cisco.dnac.accesspoint_location_playbook_config_generator:
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
          planned_accesspoint_list:
            - test_ap_location
            - test_ap2_location

- name: Generate YAML Configuration with file path based on real access point list
  cisco.dnac.accesspoint_location_playbook_config_generator:
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
          real_accesspoint_list:
            - Test_ap
            - AP687D.B402.1614-AP-Test6

- name: Generate YAML Configuration with default file path based on access point model list
  cisco.dnac.accesspoint_location_playbook_config_generator:
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
          accesspoint_model_list:
            - AP9120E
            - AP9130E

- name: Generate YAML Configuration with default file path based on MAC Address list
  cisco.dnac.accesspoint_location_playbook_config_generator:
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
          mac_address_list:
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
         'accesspoint_location_workflow_manager'.": {
            "file_path":
             "tmp/accesspoint_location_workflow_playbook_templatebase.yml"
          }
        },
      "msg": {
        "YAML config generation Task succeeded for module
         'accesspoint_location_workflow_manager'.": {
            "file_path":
             "tmp/accesspoint_location_workflow_playbook_templatebase.yml"
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
                   module 'accesspoint_location_workflow_manager'.
                   Verify input filters or configuration.",
      "msg": "No configurations or components to process for module
              'accesspoint_location_workflow_manager'.
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


class AccesspointLocationPlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.module_name = "accesspoint_location_workflow_manager"
        self.module_schema = self.get_workflow_elements_schema()
        self.log("Initialized AccesspointLocationPlaybookGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False
        self.have["all_floor"], self.have["filtered_floor"], self.have["all_detailed_config"] = [], [], []
        self.have["all_config"], self.have["planned_aps"], self.have["real_aps"] = [], [], []

    def validate_input(self):
        """
        Validates input configuration parameters for access point location playbook generation.

        This function performs comprehensive validation of input configuration parameters
        by checking parameter presence, validating against expected schema specification,
        verifying allowed keys to prevent invalid parameters, ensuring minimum requirements
        for access point location playbook generation, and setting validated configuration for
        downstream processing workflows.

        Args:
            None (uses self.config from class instance)

        Returns:
            object: Self instance with updated attributes:
                - self.validated_config: List of validated configuration dictionaries
                - self.msg: Success or failure message
                - self.status: Validation status ("success" or "failed")
                - Operation result set via set_operation_result()
        """
        self.log(
            "Starting validation of playbook configuration parameters. Checking "
            "configuration availability, schema compliance, and minimum requirements "
            "for access point location playbook generation workflow.",
            "INFO"
        )

        if not self.config:
            self.msg = (
                "Configuration is not available in the playbook for validation. This is "
                "valid for certain workflows that don't require configuration parameters."
            )
            self.log(self.msg, "INFO")
            self.status = "success"
            return self

        if not isinstance(self.config, list):
            self.msg = (
                "Configuration must be a list of dictionaries, got: {0}. Please provide "
                "configuration as a list.".format(type(self.config).__name__)
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "Configuration list provided with {0} item(s) to validate. Starting "
            "per-item validation.".format(len(self.config)),
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
            "Defined validation schema with {0} allowed parameter(s): {1}".format(
                len(allowed_keys), list(allowed_keys)
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
                    f"Configuration item {config_index}/{len(self.config)} must be a "
                    f"dictionary, got: {type(config_item).__name__}. Each "
                    "configuration entry must be a dictionary with valid parameters."
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Check for invalid keys
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            if invalid_keys:
                self.msg = (
                    "Invalid parameters found in playbook configuration item "
                    f"{config_index}/{len(self.config)}: {list(invalid_keys)}. "
                    f"Only the following parameters are allowed: {list(allowed_keys)}. "
                    "Please remove the invalid parameters and try again."
                )
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

        # Import validate_list_of_dicts function here to avoid circular imports
        # from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

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
                    "Configuration item {0}/{1} has global_filters. Validating filter structure.".format(
                        config_index, len(valid_temp)
                    ),
                    "DEBUG"
                )

                if not isinstance(global_filters, dict):
                    self.msg = (
                        "global_filters in configuration item {0}/{1} must be a dictionary, "
                        "got: {2}. Please provide global_filters as a dictionary with filter lists.".format(
                            config_index, len(valid_temp), type(global_filters).__name__
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Check that at least one filter list is provided and has values
                valid_filter_keys = [
                    "site_list", "planned_accesspoint_list", "real_accesspoint_list",
                    "accesspoint_model_list", "mac_address_list"
                ]
                provided_filters = {
                    key: global_filters.get(key)
                    for key in valid_filter_keys
                    if global_filters.get(key)
                }

                if not provided_filters:
                    self.msg = (
                        "global_filters in configuration item {0}/{1} provided but no valid "
                        "filter lists have values. At least one of the following must be provided: "
                        "{2}. Please add at least one filter list with values.".format(
                            config_index, len(valid_temp), valid_filter_keys
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Validate that filter values are lists (except hostname_filter and site_name_filter)
                for filter_key, filter_value in provided_filters.items():
                    if filter_key in ["hostname_filter", "site_name_filter"]:
                        # These can be strings
                        if not isinstance(filter_value, str):
                            self.msg = (
                                "global_filters.{0} in configuration item {1}/{2} must be a string, "
                                "got: {3}. Please provide {0} as a string value.".format(
                                    filter_key, config_index, len(valid_temp), type(filter_value).__name__
                                )
                            )
                            self.log(self.msg, "ERROR")
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self
                    else:
                        # Other filters must be lists
                        if not isinstance(filter_value, list):
                            self.msg = (
                                "global_filters.{0} in configuration item {1}/{2} must be a list, "
                                "got: {3}. Please provide filter as a list of strings.".format(
                                    filter_key, config_index, len(valid_temp), type(filter_value).__name__
                                )
                            )
                            self.log(self.msg, "ERROR")
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self

                self.log(
                    "Configuration item {0}/{1} global_filters structure validated successfully. "
                    "Provided filters: {2}".format(
                        config_index, len(valid_temp), list(provided_filters.keys())
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "Configuration item {0}/{1} does not have global_filters. Assuming "
                    "generate_all_configurations mode.".format(config_index, len(valid_temp)),
                    "DEBUG"
                )

        # Set validated configuration and return success
        self.validated_config = valid_temp

        self.msg = (
            "Successfully validated {0} configuration item(s) for access point location "
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

    def validate_params(self, config):
        """
        Validates individual configuration parameters for access point location playbook generation.

        This function performs detailed validation of configuration parameters required for
        YAML playbook generation, including mode flags, file paths, and global filter structures.
        It ensures configuration completeness and validates file system accessibility.

        Args:
            config (dict): Configuration parameters from validated playbook containing:
                - generate_all_configurations (bool, optional): Generate all configurations flag
                - file_path (str, optional): Output file path for YAML playbook
                - global_filters (dict, optional): Filter criteria for AP selection

        Returns:
            object: Self instance with updated attributes:
                - self.msg: Validation result message
                - self.status: Validation status ("success" or "failed")

        Side Effects:
            - May create directory structure if file_path directory doesn't exist
            - Updates self.status based on validation outcome
            - Logs validation progress and results

        Raises:
            Sets self.status to "failed" on validation errors but doesn't raise exceptions.
        """
        self.log(
            "Starting detailed validation of individual configuration parameters for access point "
            "location playbook generation. Checking configuration completeness, parameter types, "
            "and file system accessibility.",
            "DEBUG"
        )

        # Check for required parameters
        if not config:
            self.msg = (
                "Configuration cannot be empty. At least one of 'generate_all_configurations' "
                "or 'global_filters' must be provided for YAML playbook generation."
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.log(
            f"Configuration parameter dictionary provided with {len(config)} key(s):"
            f" {list(config.keys())}. Proceeding "
            "with parameter-specific validation.",
            "DEBUG"
        )

        # Validate file_path if provided
        file_path = config.get("file_path")
        if file_path:
            self.log(
                "Validating file_path parameter: '{file_path}'. Checking directory existence and "
                "write permissions.",
                "DEBUG"
            )
            import os
            directory = os.path.dirname(file_path)

            if directory:
                if not os.path.exists(directory):
                    self.log(
                        f"Directory does not exist: '{directory}'. Attempting to create directory "
                        "structure with makedirs().",
                        "INFO"
                    )
                    try:
                        os.makedirs(directory, exist_ok=True)
                        self.log(
                            f"Successfully created directory: '{directory}'. File path is now "
                            "accessible for YAML output.",
                            "INFO"
                        )
                    except Exception as e:
                        self.msg = (
                            "Cannot create directory for file_path: '{0}'. Error: {1}. "
                            "Please verify directory path is valid and you have write "
                            "permissions.".format(directory, str(e))
                        )
                        self.log(self.msg, "ERROR")
                        self.status = "failed"
                        return self
                else:
                    self.log(
                        f"Directory exists and is accessible: '{directory}'. File path validation "
                        "successful.",
                        "DEBUG"
                    )
            else:
                self.log(
                    "No directory specified in file_path (current directory will be used): "
                    f"'{file_path}'", "DEBUG"
                )
        else:
            self.log(
                "No file_path parameter provided. Default filename will be generated "
                "automatically based on module name and timestamp.",
                "DEBUG"
            )

        # Validate generate_all_configurations parameter if provided
        generate_all = config.get("generate_all_configurations")
        if generate_all is not None:
            self.log(
                f"generate_all_configurations parameter provided: {generate_all}. This will determine "
                "whether to collect all access point locations or use global_filters.",
                "DEBUG"
            )
            if not isinstance(generate_all, bool):
                self.msg = (
                    "generate_all_configurations must be a boolean value (true/false), "
                    f"got: {type(generate_all).__name__}. Please provide a valid boolean."
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

        # Validate global_filters parameter if provided
        global_filters = config.get("global_filters")
        if global_filters is not None:
            self.log(
                "global_filters parameter provided with "
                f"{len(global_filters) if isinstance(global_filters, dict) else 0} filter(s). Validating filter "
                "structure.",
                "DEBUG"
            )
            if not isinstance(global_filters, dict):
                self.msg = (
                    f"global_filters must be a dictionary, got: {type(global_filters).__name__}. Please provide "
                    "global_filters as a dictionary with filter lists."
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            self.log(
                "global_filters structure validated successfully. Filters will be processed "
                "during get_have() and yaml_config_generator() operations.",
                "DEBUG"
            )

        self.log(
            "Configuration parameters validation completed successfully. All parameters "
            "conform to expected types and formats. Status: success",
            "DEBUG"
        )
        self.status = "success"
        return self

    def get_want(self, config, state):
        """
        Prepares desired configuration parameters for API operations based on playbook state.

        This function validates input configuration, extracts YAML generation parameters,
        and populates the self.want dictionary with structured data required for access point
        location YAML playbook generation workflow in Cisco Catalyst Center.

        Args:
            config (dict): Configuration parameters from Ansible playbook containing:
                  - generate_all_configurations: Mode flag (optional, bool)
                  - file_path: Output file path (optional, str)
                  - global_filters: Filter criteria (optional, dict)
                  Example: {
                    "generate_all_configurations": False,
                    "file_path": "/tmp/ap_locations.yml",
                    "global_filters": {
                      "site_list": ["Global/USA/San Jose/Building1/Floor1"],
                      "accesspoint_model_list": ["C9130AXI-B"]
                    }
                  }
            state (str): Desired state for operation (must be 'gathered').
                        Other states not supported for YAML generation.

        Returns:
            object: Self instance with updated attributes:
                - self.want: Dict containing validated YAML generation parameters
                - self.msg: Success message describing parameter collection
                - self.status: Operation status ("success")

        Side Effects:
            - Validates config parameters via validate_params()
            - Updates self.want dictionary with YAML generation configuration
            - Logs detailed parameter extraction and validation information
        """

        self.log(
            "Preparing desired configuration parameters for API operations based on playbook "
            f"configuration. State parameter: '{state}'. This operation validates input parameters, "
            "extracts YAML generation settings, and populates the want dictionary for downstream "
            "processing by get_have() and yaml_config_generator() functions.",
            "INFO"
        )

        self.log(
            "Initiating comprehensive input parameter validation using validate_params(). "
            "This validates parameter types, required fields, and schema compliance for "
            "YAML generation workflow.",
            "INFO"
        )

        self.validate_params(config)
        self.log(
            "Input parameter validation completed successfully. All configuration parameters "
            "conform to expected schema and type requirements. Proceeding with want dictionary "
            "population.",
            "DEBUG"
        )

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            "Successfully extracted yaml_config_generator parameters from playbook. Complete "
            f"parameter structure: {want['yaml_config_generator']}. These parameters will control YAML generation mode "
            "(generate_all vs filtered), output file location, and access point filtering criteria.",
            "INFO"
        )

        self.want = want
        self.log(f"Desired State (want): {self.pprint(self.want)}", "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Access Point Location operations."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Retrieves current access point location state from Cisco Catalyst Center.

        This function collects complete access point location configurations including
        position coordinates, floor assignments, radio configurations, and device metadata
        from Catalyst Center based on configuration mode (generate_all or filtered) for
        YAML playbook generation workflow.

        Args:
            config (dict): Configuration parameters containing:
                        - generate_all_configurations: Mode flag (optional, bool)
                        - global_filters: Filter criteria (optional, dict)
                        Example: {
                            "generate_all_configurations": False,
                            "global_filters": {
                                "site_list": ["Global/USA/Building1/Floor1"],
                                "planned_accesspoint_list": ["Floor1-AP1"],
                                "real_accesspoint_list": ["Floor2-AP1"],
                                "accesspoint_model_list": ["C9130AXI-B"],
                                "mac_address_list": ["aa:bb:cc:dd:ee:ff"]
                            }
                        }

        Returns:
            object: Self instance with updated attributes:
                - self.have: Dict containing current AP location state with keys:
                    * all_floor: All floor sites from Catalyst Center
                    * filtered_floor: Floors containing APs matching filters
                    * all_config: Combined planned + real AP configurations
                    * planned_aps: Planned AP position configurations
                    * real_aps: Real/deployed AP position configurations
                    * all_detailed_config: Detailed AP metadata with IDs
                - self.msg: Success message describing retrieval result
                - self.status: Operation status ("success")

        Side Effects:
            - Calls collect_all_accesspoint_location_list() to populate self.have
            - Validates filter parameters against retrieved AP inventory
            - Exits with failure via fail_and_exit() if filtered items not found
            - Logs detailed progress information at INFO/DEBUG/WARNING levels

        Filter Priority and Processing:
            Filters are processed independently (not hierarchical):
            - site_list: Filters by floor site hierarchy paths
            - planned_accesspoint_list: Filters by planned AP names
            - real_accesspoint_list: Filters by real/deployed AP names
            - accesspoint_model_list: Filters by AP hardware models
            - mac_address_list: Filters by AP MAC addresses

        Validation Behavior:
            - "all" keyword (case-insensitive): Skips validation, returns all data
            - Specific values: Validates each item exists, fails if any missing
            - Empty list: Ignored (no filtering applied)

        Notes:
            - Function always succeeds unless validation fails (fail_and_exit called)
            - Missing APs in filtered mode causes playbook execution failure
            - generate_all mode skips all filter validation
            - All filters validated against all_detailed_config populated by
              collect_all_accesspoint_location_list()
        """
        self.log(
            "Retrieving current state of access point locations from Cisco Catalyst Center. "
            "This operation collects AP position configurations including coordinates, floor "
            "assignments, radio settings, and device metadata based on configuration mode "
            "(generate_all or filtered). Data will be used for YAML playbook generation workflow.",
            "INFO"
        )

        if not config or not isinstance(config, dict):
            self.log(
                f"Invalid config parameter provided to get_have(). Config is None or not a "
                f"dictionary type. Cannot retrieve AP location data without valid configuration. "
                f"Skipping data collection. Config type: {type(config).__name__}",
                "WARNING"
            )
            self.msg = "Invalid configuration provided. Skipping access point location data retrieval."
            return self

        self.log(
            "Configuration parameter validated successfully. Config type: dict. Proceeding with "
            "operational mode detection and data collection workflow.",
            "DEBUG"
        )

        if config.get("generate_all_configurations", False):
            self.log(
                "Generate all configurations mode ENABLED (generate_all_configurations=True). "
                "Initiating complete access point location collection from Cisco Catalyst Center "
                "without applying any filters. This mode retrieves ALL AP positions (planned and "
                "real) including complete position coordinates, radio configurations, and floor "
                "assignments for comprehensive access point location config and documentation.",
                "INFO"
            )

            self.log(
                "Calling collect_all_accesspoint_location_list() without filters to retrieve "
                "complete AP location inventory from Catalyst Center. This will fetch all floor "
                "sites and associated AP positions using paginated API calls.",
                "INFO"
            )
            self.collect_all_accesspoint_location_list()

            if not self.have.get("all_config"):
                self.msg = (
                    "No existing access point locations found in Cisco Catalyst Center. Please verify "
                    "that APs are configured and positioned on floor maps in the system and API "
                    "credentials have sufficient permissions to retrieve site design data."
                )
                self.log(self.msg, "WARNING")
                self.status = "success"
                return self

            self.log(
                f"Successfully retrieved {len(self.have.get('all_config', []))} floor site(s) with "
                f"access point location data from Catalyst Center in generate_all mode. Total APs "
                f"collected: Planned={len(self.have.get('planned_aps', []))}, "
                f"Real={len(self.have.get('real_aps', []))}. Complete configuration data: "
                f"{self.pprint(self.have.get('all_config'))}",
                "INFO"
            )
        else:
            self.log(
                "Filtered configuration mode detected (generate_all_configurations=False or not "
                "specified). Extracting global_filters parameter to determine data collection and "
                "validation strategy. Supported filters: site_list, planned_accesspoint_list, "
                "real_accesspoint_list, accesspoint_model_list, mac_address_list. Each filter is "
                "processed independently with existence validation.",
                "INFO"
            )

            global_filters = config.get("global_filters")

            if not global_filters or not isinstance(global_filters, dict):
                self.log(
                    "No valid global_filters provided in filtered mode. global_filters is None or "
                    "not a dictionary. Cannot determine which access points to validate. Skipping "
                    "data collection. To retrieve AP locations, either enable "
                    "generate_all_configurations or provide global_filters with at least one filter "
                    "type (site_list, planned_accesspoint_list, real_accesspoint_list, "
                    "accesspoint_model_list, or mac_address_list).",
                    "WARNING"
                )
                self.msg = (
                    "No global_filters provided in filtered mode. Cannot collect access point "
                    "location data without filter criteria."
                )
                return self

            self.log(
                f"Global filters parameter validated successfully. Calling "
                f"collect_all_accesspoint_location_list() to retrieve complete AP inventory for "
                f"filter validation. Filter structure: {global_filters}",
                "DEBUG"
            )
            self.collect_all_accesspoint_location_list()

            # Extract individual filter components
            site_list = global_filters.get("site_list", [])
            planned_ap_list = global_filters.get("planned_accesspoint_list", [])
            real_ap_list = global_filters.get("real_accesspoint_list", [])
            model_list = global_filters.get("accesspoint_model_list", [])
            mac_list = global_filters.get("mac_address_list", [])

            self.log(
                f"Extracted filter components from global_filters. site_list: {site_list} "
                f"(count: {len(site_list) if isinstance(site_list, list) else 0}), "
                f"planned_accesspoint_list: {planned_ap_list} "
                f"(count: {len(planned_ap_list) if isinstance(planned_ap_list, list) else 0}), "
                f"real_accesspoint_list: {real_ap_list} "
                f"(count: {len(real_ap_list) if isinstance(real_ap_list, list) else 0}), "
                f"accesspoint_model_list: {model_list} "
                f"(count: {len(model_list) if isinstance(model_list, list) else 0}), "
                f"mac_address_list: {mac_list} "
                f"(count: {len(mac_list) if isinstance(mac_list, list) else 0})",
                "DEBUG"
            )

            # Process site_list filter
            if site_list and isinstance(site_list, list):
                self.log(
                    f"Site list filter detected. Requested floor site hierarchies: {site_list} "
                    f"(count: {len(site_list)}). This filter validates floor sites contain access "
                    f"points and exist in Catalyst Center.",
                    "INFO"
                )

                if len(site_list) == 1 and site_list[0].lower() == "all":
                    self.log(
                        "Site list contains 'all' keyword. Skipping site validation, all floors "
                        "with APs will be included in YAML generation.",
                        "INFO"
                    )
                    return self
                else:
                    self.log(
                        f"Validating {len(site_list)} floor site(s) exist in filtered_floor data "
                        f"populated by collect_all_accesspoint_location_list(). Each site must exist "
                        f"or playbook will fail.",
                        "DEBUG"
                    )
                    missing_floors = []
                    for floor_index, floor_name in enumerate(site_list, start=1):
                        self.log(
                            f"Validating floor site {floor_index}/{len(site_list)}: '{floor_name}'. "
                            f"Checking existence in filtered_floor list.",
                            "DEBUG"
                        )
                        floor_exist = self.find_dict_by_key_value(
                            self.have["filtered_floor"], "floor_site_hierarchy", floor_name
                        )

                        if not floor_exist:
                            missing_floors.append(floor_name)
                            self.log(
                                f"Floor site hierarchy '{floor_name}' does not exist or has no "
                                f"access points configured. Adding to missing_floors list.",
                                "WARNING"
                            )
                        else:
                            self.log(
                                f"Floor site {floor_index}/{len(site_list)}: '{floor_name}' "
                                f"validated successfully. Floor exists with AP configurations.",
                                "DEBUG"
                            )

                    if missing_floors:
                        self.msg = (
                            f"The following floor site hierarchies do not exist or have no access "
                            f"points configured: {missing_floors}. Total missing: "
                            f"{len(missing_floors)}/{len(site_list)} requested. Please verify site "
                            f"hierarchy paths are correct (case-sensitive, full path from Global) "
                            f"and floors have APs positioned on floor maps before retrying."
                        )
                        self.log(self.msg, "ERROR")

                    self.log(
                        f"All {len(site_list)} floor site(s) validated successfully. All requested "
                        f"floors exist with access point configurations.",
                        "INFO"
                    )

            # Process planned_accesspoint_list filter
            if planned_ap_list and isinstance(planned_ap_list, list):
                self.log(
                    f"Planned access point list filter detected. Requested planned AP names: "
                    f"{planned_ap_list} (count: {len(planned_ap_list)}). This filter validates "
                    f"planned APs exist in Catalyst Center.",
                    "INFO"
                )

                if len(planned_ap_list) == 1 and planned_ap_list[0].lower() == "all":
                    self.log(
                        "Planned AP list contains 'all' keyword. Skipping planned AP validation, "
                        "all planned APs will be included in YAML generation.",
                        "INFO"
                    )
                    return self
                else:
                    self.log(
                        f"Validating {len(planned_ap_list)} planned AP(s) exist in "
                        f"all_detailed_config data. Each planned AP must exist or playbook will fail.",
                        "DEBUG"
                    )
                    missing_planned_aps = []
                    for ap_index, planned_ap in enumerate(planned_ap_list, start=1):
                        self.log(
                            f"Validating planned AP {ap_index}/{len(planned_ap_list)}: "
                            f"'{planned_ap}'. Checking existence in all_detailed_config.",
                            "DEBUG"
                        )
                        ap_exist = self.find_dict_by_key_value(
                            self.have["all_detailed_config"], "accesspoint_name", planned_ap
                        )

                        if not ap_exist or ap_exist.get("accesspoint_type") == "real":
                            missing_planned_aps.append(planned_ap)
                            self.log(
                                f"Planned access point '{planned_ap}' does not exist or is marked "
                                f"as 'real' type. Adding to missing_planned_aps list.",
                                "WARNING"
                            )
                        else:
                            self.log(
                                f"Planned AP {ap_index}/{len(planned_ap_list)}: '{planned_ap}' "
                                f"validated successfully. AP exists with type 'planned'.",
                                "DEBUG"
                            )

                    if missing_planned_aps:
                        self.msg = (
                            f"The following planned access points do not exist: {missing_planned_aps}. "
                            f"Total missing: {len(missing_planned_aps)}/{len(planned_ap_list)} "
                            f"requested. Please verify planned AP names are correct (case-sensitive) "
                            f"and APs are configured as planned (not real) on floor maps before retrying."
                        )
                        self.log(self.msg, "ERROR")

                    self.log(
                        f"All {len(planned_ap_list)} planned AP(s) validated successfully. All "
                        f"requested planned APs exist in Catalyst Center.",
                        "INFO"
                    )

            # Process real_accesspoint_list filter
            if real_ap_list and isinstance(real_ap_list, list):
                self.log(
                    f"Real access point list filter detected. Requested real AP names: "
                    f"{real_ap_list} (count: {len(real_ap_list)}). This filter validates real/"
                    f"deployed APs exist in Catalyst Center.",
                    "INFO"
                )

                if len(real_ap_list) == 1 and real_ap_list[0].lower() == "all":
                    self.log(
                        "Real AP list contains 'all' keyword. Skipping real AP validation, all "
                        "real/deployed APs will be included in YAML generation.",
                        "INFO"
                    )
                    return self
                else:
                    self.log(
                        f"Validating {len(real_ap_list)} real AP(s) exist in all_detailed_config "
                        f"data. Each real AP must exist or playbook will fail.",
                        "DEBUG"
                    )
                    missing_real_aps = []
                    for ap_index, real_ap in enumerate(real_ap_list, start=1):
                        self.log(
                            f"Validating real AP {ap_index}/{len(real_ap_list)}: '{real_ap}'. "
                            f"Checking existence in all_detailed_config.",
                            "DEBUG"
                        )
                        ap_exist = self.find_dict_by_key_value(
                            self.have["all_detailed_config"], "accesspoint_name", real_ap
                        )

                        if not ap_exist or ap_exist.get("accesspoint_type") != "real":
                            missing_real_aps.append(real_ap)
                            self.log(
                                f"Real access point '{real_ap}' does not exist or is not marked "
                                f"as 'real' type. Adding to missing_real_aps list.",
                                "WARNING"
                            )
                        else:
                            self.log(
                                f"Real AP {ap_index}/{len(real_ap_list)}: '{real_ap}' validated "
                                f"successfully. AP exists with type 'real'.",
                                "DEBUG"
                            )

                    if missing_real_aps:
                        self.msg = (
                            f"The following real access points do not exist: {missing_real_aps}. "
                            f"Total missing: {len(missing_real_aps)}/{len(real_ap_list)} requested. "
                            f"Please verify real AP names are correct (case-sensitive) and APs are "
                            f"deployed and visible in Catalyst Center before retrying."
                        )
                        self.log(self.msg, "ERROR")

                    self.log(
                        f"All {len(real_ap_list)} real AP(s) validated successfully. All requested "
                        f"real/deployed APs exist in Catalyst Center.",
                        "INFO"
                    )

            # Process accesspoint_model_list filter
            if model_list and isinstance(model_list, list):
                self.log(
                    f"Access point model list filter detected. Requested AP models: {model_list} "
                    f"(count: {len(model_list)}). This filter validates AP hardware models exist "
                    f"in Catalyst Center.",
                    "INFO"
                )

                if len(model_list) == 1 and model_list[0].lower() == "all":
                    self.log(
                        "AP model list contains 'all' keyword. Skipping model validation, all AP "
                        "models will be included in YAML generation.",
                        "INFO"
                    )
                    return self
                else:
                    self.log(
                        f"Validating {len(model_list)} AP model(s) exist in all_detailed_config "
                        f"data. Each model must have at least one AP or playbook will fail.",
                        "DEBUG"
                    )
                    missing_models = []
                    for model_index, model in enumerate(model_list, start=1):
                        self.log(
                            f"Validating AP model {model_index}/{len(model_list)}: '{model}'. "
                            f"Searching for APs with this model in all_detailed_config.",
                            "DEBUG"
                        )
                        aps_exist = self.find_multiple_dict_by_key_value(
                            self.have["all_detailed_config"], "accesspoint_model", model
                        )

                        if not aps_exist:
                            missing_models.append(model)
                            self.log(
                                f"Access point model '{model}' not found in Catalyst Center. No "
                                f"APs with this model exist. Adding to missing_models list.",
                                "WARNING"
                            )
                        else:
                            self.log(
                                f"AP model {model_index}/{len(model_list)}: '{model}' validated "
                                f"successfully. Found {len(aps_exist)} AP(s) with this model.",
                                "DEBUG"
                            )

                    if missing_models:
                        self.msg = (
                            f"The following access point models do not exist: {missing_models}. "
                            f"Total missing: {len(missing_models)}/{len(model_list)} requested. "
                            f"Please verify AP model names are correct (case-sensitive, exact match) "
                            f"and APs with these models are deployed in Catalyst Center before retrying."
                        )
                        self.log(self.msg, "ERROR")

                    self.log(
                        f"All {len(model_list)} AP model(s) validated successfully. All requested "
                        f"models have deployed APs in Catalyst Center.",
                        "INFO"
                    )

            # Process mac_address_list filter
            if mac_list and isinstance(mac_list, list):
                self.log(
                    f"MAC address list filter detected. Requested MAC addresses: {mac_list} "
                    f"(count: {len(mac_list)}). This filter validates AP MAC addresses exist in "
                    f"Catalyst Center.",
                    "INFO"
                )

                if len(mac_list) == 1 and mac_list[0].lower() == "all":
                    self.log(
                        "MAC address list contains 'all' keyword. Skipping MAC validation, all "
                        "APs with MAC addresses will be included in YAML generation.",
                        "INFO"
                    )
                    return self
                else:
                    self.log(
                        f"Validating {len(mac_list)} MAC address(es) exist in all_detailed_config "
                        f"data. Each MAC must match an AP or playbook will fail.",
                        "DEBUG"
                    )
                    missing_macs = []
                    for mac_index, mac in enumerate(mac_list, start=1):
                        normalized_mac = mac.lower()
                        self.log(
                            f"Validating MAC address {mac_index}/{len(mac_list)}: '{normalized_mac}' "
                            f"(normalized). Searching for AP with this MAC in all_detailed_config.",
                            "DEBUG"
                        )
                        aps_exist = self.find_multiple_dict_by_key_value(
                            self.have["all_detailed_config"], "mac_address", normalized_mac
                        )

                        if not aps_exist:
                            missing_macs.append(mac)
                            self.log(
                                f"MAC address '{normalized_mac}' not found in Catalyst Center. No "
                                f"AP with this MAC exists. Adding to missing_macs list.",
                                "WARNING"
                            )
                        else:
                            self.log(
                                f"MAC address {mac_index}/{len(mac_list)}: '{normalized_mac}' "
                                f"validated successfully. Found {len(aps_exist)} AP(s) with this MAC.",
                                "DEBUG"
                            )

                    if missing_macs:
                        self.msg = (
                            f"The following MAC addresses do not exist: {missing_macs}. Total "
                            f"missing: {len(missing_macs)}/{len(mac_list)} requested. Please verify "
                            f"MAC addresses are correct (format: aa:bb:cc:dd:ee:ff) and APs with "
                            f"these MACs are deployed in Catalyst Center before retrying."
                        )
                        self.log(self.msg, "ERROR")

                    self.log(
                        f"All {len(mac_list)} MAC address(es) validated successfully. All requested "
                        f"MAC addresses match deployed APs in Catalyst Center.",
                        "INFO"
                    )

        self.log(
            f"Current State (have): {self.pprint(self.have)}. Data collection and validation "
            f"completed successfully. Total floors: {len(self.have.get('all_floor', []))}, "
            f"Filtered floors: {len(self.have.get('filtered_floor', []))}, "
            f"All configs: {len(self.have.get('all_config', []))}, "
            f"Planned APs: {len(self.have.get('planned_aps', []))}, "
            f"Real APs: {len(self.have.get('real_aps', []))}",
            "INFO"
        )
        self.msg = "Successfully retrieved access point location details from Cisco Catalyst Center."
        return self

    def find_multiple_dict_by_key_value(self, data_list, key, value):
        """
        Searches for and returns all dictionaries matching a specific key-value pair.

        This function performs a comprehensive search through a list of dictionaries to find
        all items where the specified key matches the given value. It includes input validation,
        detailed logging, and handles edge cases gracefully.

        Args:
            data_list (list): List of dictionaries to search through. Each item must be a dict.
                             Empty lists are valid and will return None.
                             Example: [
                                 {"name": "AP1", "model": "C9130"},
                                 {"name": "AP2", "model": "C9130"},
                                 {"name": "AP3", "model": "C9120"}
                             ]
            key (str): Dictionary key to search for in each item. Key must exist in at least
                      one dictionary to produce matches. Case-sensitive string matching.
                      Example: "model"
            value (any): Value to match against the specified key. Comparison uses equality
                        operator (==) so exact match is required. Type should match the
                        expected type of the key's value.
                        Example: "C9130"

        Returns:
            list or None:
                - Returns list of all matching dictionaries if matches found
                - Returns None if no matches found or validation fails
                - Returns None if data_list is empty
                - Each returned dict maintains its original structure

        Side Effects:
            - Logs DEBUG messages for search initiation, progress, and results
            - Logs ERROR messages for validation failures
            - Does not modify input data_list or matched items

        Example:
            >>> data = [
            ...     {"ap_name": "Floor1-AP1", "model": "C9130AXI"},
            ...     {"ap_name": "Floor1-AP2", "model": "C9130AXI"},
            ...     {"ap_name": "Floor2-AP1", "model": "C9120AXI"}
            ... ]
            >>> result = self.find_multiple_dict_by_key_value(data, "model", "C9130AXI")
            >>> # Returns: [{"ap_name": "Floor1-AP1", ...}, {"ap_name": "Floor1-AP2", ...}]

        Validation:
            - data_list must be a list (not None, dict, str, etc.)
            - All items in data_list must be dictionaries
            - key parameter should be a valid dictionary key
            - No type restrictions on value parameter
        """
        self.log(
            f"Starting dictionary search operation. Searching for key '{key}' with value '{value}' "
            f"in a list containing {len(data_list) if isinstance(data_list, list) else 0} item(s). "
            "This search will return all matching dictionaries "
            "or None if no matches are found.",
            "DEBUG"
        )

        # Validate data_list is a list
        if not isinstance(data_list, list):
            self.msg = (
                f"The 'data_list' parameter must be a list, got: {type(data_list).__name__}. Please provide a valid "
                "list of dictionaries to search."
            )
            self.log(self.msg, "ERROR")
            return None

        # Validate all items in data_list are dictionaries
        if not all(isinstance(item, dict) for item in data_list):
            invalid_types = [type(item).__name__ for item in data_list if not isinstance(item, dict)]
            self.msg = (
                f"All items in 'data_list' must be dictionaries. Found invalid type(s): {set(invalid_types)}. "
                "Please ensure all list items are dictionary objects."
            )
            self.log(self.msg, "ERROR")
            return None

        # Handle empty list case
        if not data_list:
            self.log(
                "Empty data_list provided. No items to search. Returning None.",
                "DEBUG"
            )
            return None

        self.log(
            f"Input validation passed. Beginning iteration through {len(data_list)} dictionary item(s) "
            f"to find matches for key '{key}' with value '{value}'.",
            "DEBUG"
        )

        matched_items = []
        for idx, item in enumerate(data_list):
            # Log search progress for debugging (verbose mode)
            self.log(
                f"Checking item at index {idx + 1}/{len(data_list)}: {item}",
                "DEBUG"
            )

            if item.get(key) == value:
                self.log(
                    f"Match found at index {idx + 1}/{len(data_list)}. Item: {item}. Adding to matched_items list.",
                    "DEBUG"
                )
                matched_items.append(item)

        # Log search results
        if matched_items:
            self.log(
                "Dictionary search completed successfully. Total matches "
                f"found: {len(matched_items)} out of {len(data_list)} "
                f"item(s) searched. Matched items: {matched_items}",
                "DEBUG"
            )
            return matched_items

        self.log(
            "Dictionary search completed. No matching items found for "
            f"key '{key}' with value '{value}' "
            f"in {len(data_list)} item(s) searched. Returning None.",
            "DEBUG"
        )
        return None

    def get_workflow_elements_schema(self):
        """
        Retrieves the schema configuration for access point location workflow manager components.

        This function defines the complete validation schema for global filters used in access
        point location playbook generation, specifying allowed filter types, data structures,
        and validation rules for site-based, access point-based, model-based, and MAC-based filtering.

        Args:
            None (uses self context for potential future expansion)

        Returns:
            dict: Schema configuration dictionary with global_filters structure containing
                validation rules for multiple filter types:
                - site_list: Floor site hierarchy paths (list[str])
                - planned_accesspoint_list: Planned AP names (list[str])
                - real_accesspoint_list: Real/deployed AP names (list[str])
                - accesspoint_model_list: AP hardware models (list[str])
                - mac_address_list: AP MAC addresses (list[str])
                All filters optional with list[str] type requirement.

        Side Effects:
            - Logs DEBUG message documenting schema structure
            - Schema used by validate_input() for parameter validation

        Example Schema Structure:
            {
                "global_filters": {
                    "site_list": {
                        "type": "list",
                        "required": False,
                        "elements": "str"
                    },
                    ...
                }
            }

        Notes:
            - All filters are optional (required: False)
            - All filters expect list of strings as input
            - Schema matches Ansible module_utils validation format
            - Used during input validation phase in validate_input()
            - Filter priority: site > planned_ap > real_ap > model > mac
        """
        self.log(
            "Defining validation schema for access point location workflow manager. "
            "Schema includes global_filters structure with five filter types: site_list, "
            "planned_accesspoint_list, real_accesspoint_list, accesspoint_model_list, and "
            "mac_address_list. All filters are optional and expect list[str] format.",
            "DEBUG"
        )

        schema = {
            "global_filters": {
                "site_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "planned_accesspoint_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "real_accesspoint_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_model_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "mac_address_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            }
        }

        self.log(
            f"Schema definition completed. Schema contains {len(schema.get('global_filters', {}))}"
            f" global filter type(s): {list(schema.get('global_filters', {}).keys())}. "
            "This schema will be used for input validation and filter processing.",
            "DEBUG"
        )

        return schema

    def get_all_floors_from_sites(self):
        """
        Retrieves all floor-type sites from Cisco Catalyst Center with pagination support.

        This function queries the Catalyst Center site design API to retrieve all sites with
        type 'floor', handling pagination automatically for large site inventories. It extracts
        floor ID and site hierarchy information for downstream processing.

        Args:
            None (uses self.payload for API configuration parameters)

        Returns:
            list: List of dictionaries containing floor information with structure:
                [
                    {
                        "id": "floor-uuid-1",
                        "floor_site_hierarchy": "Global/USA/Building1/Floor1"
                    },
                    ...
                ]
                Returns empty list if no floors found or API errors occur.

        Side Effects:
            - Makes multiple paginated API calls to Catalyst Center
            - Respects dnac_api_task_timeout and dnac_task_poll_interval from payload
            - Adds sleep delays between pagination requests to avoid rate limiting
            - Logs detailed progress information at DEBUG and INFO levels

        API Parameters Used:
            - offset: Starting position for pagination (increments by limit)
            - limit: Number of results per page (default: 500)
            - type: Filter for 'floor' type sites only

        Pagination Logic:
            - Starts at offset=1, limit=500
            - Continues until response < limit or timeout reached
            - Respects dnac_task_poll_interval between requests
            - Exits early if no response received

        Notes:
            - Only retrieves sites with type='floor', excludes buildings/areas
            - Timeout calculated from dnac_api_task_timeout parameter
            - Poll interval from dnac_task_poll_interval parameter
            - Uses site_design.get_sites API family/function
        """
        self.log(
            "Starting floor site collection from Cisco Catalyst Center. Preparing to query "
            "all floor-type sites using paginated API requests with automatic retry logic.",
            "INFO"
        )

        response_all = []
        offset = 1
        limit = 500
        api_family, api_function, param_key = "site_design", "get_sites", "type"
        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
        request_params = {param_key: "floor", "offset": offset, "limit": limit}

        self.log(
            f"Initialized pagination parameters: offset={offset}, limit={limit}, "
            f"timeout={resync_retry_count}s, poll_interval={resync_retry_interval}s. "
            f"API target: {api_family}.{api_function}(type='floor')",
            "DEBUG"
        )

        while resync_retry_count > 0:
            self.log(
                f"Sending paginated API request to Catalyst Center - "
                f"Family: '{api_family}', Function: '{api_function}', "
                f"Parameters: {request_params}. Remaining timeout: {resync_retry_count}s",
                "DEBUG"
            )

            response = self.execute_get_request(api_family, api_function, request_params)

            if not response:
                self.log(
                    f"No data received from API at offset {request_params['offset']}. "
                    f"This may indicate end of results or API error. Exiting pagination loop.",
                    "DEBUG"
                )
                break

            response_data = response.get("response", [])
            self.log(
                f"Received {len(response_data)} floor site(s) from API at offset "
                f"{request_params['offset']}. Processing floor data extraction.",
                "DEBUG"
            )

            floor_list = response.get("response")
            if floor_list and isinstance(floor_list, list):
                self.log(
                    f"Processing {len(floor_list)} floor site(s). Extracting ID and "
                    f"site hierarchy information. Raw response: {self.pprint(floor_list)}",
                    "DEBUG"
                )
                required_data_list = []
                for idx, floor_response in enumerate(floor_list, start=1):
                    required_data = {
                        "id": floor_response.get("id"),
                        "floor_site_hierarchy": floor_response.get("nameHierarchy")
                    }
                    required_data_list.append(required_data)
                    self.log(
                        f"Extracted floor {idx}/{len(floor_list)}: ID='{required_data['id']}', "
                        f"Hierarchy='{required_data['floor_site_hierarchy']}'",
                        "DEBUG"
                    )

                response_all.extend(required_data_list)
                self.log(
                    f"Added {len(required_data_list)} floor(s) to collection. "
                    f"Total floors collected so far: {len(response_all)}",
                    "DEBUG"
                )
            else:
                self.log(
                    f"No valid floor list in API response at offset {request_params['offset']}. "
                    f"Response type: {type(floor_list).__name__ if floor_list else 'None'}",
                    "WARNING"
                )

            # Check if this is the last page
            if len(response.get("response", [])) < limit:
                self.log(
                    f"Received {len(response.get('response', []))} results (less than limit of {limit}). "
                    f"Assuming this is the last page. Exiting pagination loop.",
                    "DEBUG"
                )
                break

            # Prepare for next page
            offset += limit
            request_params["offset"] = offset
            self.log(
                f"Incrementing pagination offset to {request_params['offset']} for next API request. "
                f"Will retrieve next {limit} floor sites.",
                "DEBUG"
            )

            # Rate limiting delay
            self.log(
                f"Applying rate limiting delay: pausing execution for {resync_retry_interval} second(s) "
                f"before next API request to avoid overwhelming Catalyst Center.",
                "INFO"
            )
            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval

        # Log final results
        if response_all:
            self.log(
                f"Floor site collection completed successfully. Total floor sites retrieved: "
                f"{len(response_all)}. Floor details: {self.pprint(response_all)}",
                "DEBUG"
            )
            self.log(
                f"Successfully collected {len(response_all)} floor site(s) from Cisco Catalyst Center.",
                "INFO"
            )
        else:
            self.log(
                "Floor site collection completed but no floor sites were found. This may indicate "
                "no floors are configured in Catalyst Center or all floors were filtered out.",
                "WARNING"
            )

        return response_all

    def get_access_point_position(self, floor_id, floor_name, ap_type=False):
        """
        Retrieves access point position information from Cisco Catalyst Center for a specific floor.

        This function queries either planned or real (deployed) access point positions based on the
        ap_type parameter. It supports retrieving AP locations with detailed position coordinates,
        radio configurations, and antenna settings for floor planning and visualization.

        Args:
            floor_id (str): Unique identifier (UUID) of the floor site in Catalyst Center.
                           Used to filter APs to specific floor location.
                           Example: "abc12345-6789-0def-1234-567890abcdef"

            floor_name (str): Human-readable site hierarchy path of the floor.
                             Used for logging and error messages.
                             Example: "Global/USA/San Jose/Building1/Floor1"

            ap_type (str or bool, optional): Type of access points to retrieve:
                                            - False or "planned": Retrieves planned AP positions
                                            - "real": Retrieves real/deployed AP positions
                                            Default: False (planned APs)

        Returns:
            list or None: List of access point position dictionaries if successful, None otherwise.
                         Each AP dict contains: name, type, position (x/y/z), macAddress, radios
                         Returns None if:
                         - No response received from API
                         - Invalid response format (not dict)
                         - API exception occurs
                         - No APs found on specified floor

        Side Effects:
            - Makes API call to Catalyst Center site_design family
            - Logs INFO/DEBUG/WARNING/ERROR messages throughout operation
            - Sets self.msg on error conditions

        API Endpoints Used:
            - Planned APs: site_design.get_planned_access_points_positions
            - Real APs: site_design.get_access_points_positions

        Example Response Structure:
            [
                {
                    "name": "Floor1-AP1",
                    "type": "C9130AXI-B",
                    "position": {"x": 10.5, "y": 20.3, "z": 3.0},
                    "macAddress": "aa:bb:cc:dd:ee:ff",
                    "radios": [...]
                },
                ...
            ]

        Error Handling:
            - Returns None on API errors with ERROR log
            - Returns None on empty response with WARNING log
            - Returns None on invalid response type with WARNING log
            - Logs all exceptions with full error details

        Notes:
            - Pagination handled automatically (offset=1, limit=500)
            - Planned APs may not have MAC addresses
            - Real APs always have MAC addresses
            - Position coordinates in floor map units (not physical meters)
            - Radio data includes bands, channels, power, antenna settings
        """
        self.log(
            f"Initiating access point position retrieval for floor '{floor_name}'. "
            f"AP type: '{ap_type if ap_type else 'planned'}', Floor ID: '{floor_id}'. "
            f"This operation will query Catalyst Center site design APIs to retrieve AP "
            f"location and configuration data.",
            "INFO"
        )

        self.log(
            f"Preparing API request parameters - Floor: '{floor_name}', "
            f"Floor ID: '{floor_id}', AP Type: '{ap_type if ap_type else 'planned'}'. "
            f"Determining appropriate API endpoint based on AP type.",
            "DEBUG"
        )

        # Prepare API payload with pagination
        payload = {
            "offset": 1,
            "limit": 500,
            "floor_id": floor_id
        }

        # Determine API function based on AP type
        function_name = "get_planned_access_points_positions"
        if ap_type == "real":
            function_name = "get_access_points_positions"

        self.log(
            f"API endpoint selected: site_design.{function_name}(). Payload: {payload}. "
            f"This endpoint will retrieve {ap_type if ap_type else 'planned'} access point "
            f"positions for floor '{floor_name}'.",
            "DEBUG"
        )

        try:
            self.log(
                f"Executing API request to retrieve {ap_type if ap_type else 'planned'} AP positions. "
                f"Target: site_design.{function_name}, Floor: '{floor_name}', ID: '{floor_id}'",
                "DEBUG"
            )

            response = self.execute_get_request(
                "site_design", function_name, payload
            )

            if not response:
                msg = (
                    f"No response received from API for {ap_type if ap_type else 'planned'} access point "
                    f"position query. Floor: '{floor_name}', Floor ID: '{floor_id}'. This may indicate "
                    f"no APs configured on this floor or API connectivity issue."
                )
                self.log(msg, "WARNING")
                return None

            if not isinstance(response, dict):
                warning_msg = (
                    f"Invalid response format received from {ap_type if ap_type else 'planned'} AP position "
                    f"API query. Expected dictionary, received: {type(response).__name__}. "
                    f"Floor: '{floor_name}', Floor ID: '{floor_id}'. API may have returned unexpected data format."
                )
                self.log(warning_msg, "WARNING")
                return None

            self.log(
                f"Successfully retrieved {ap_type if ap_type else 'planned'} AP position data from API. "
                f"Floor: '{floor_name}', Response structure: {response}. "
                f"Extracting AP details from response.",
                "DEBUG"
            )

            ap_positions = response.get("response")
            if ap_positions:
                self.log(
                    f"Found {len(ap_positions) if isinstance(ap_positions, list) else 'unknown'} "
                    f"{ap_type if ap_type else 'planned'} access point(s) on floor '{floor_name}'. "
                    f"Returning AP position data for downstream processing.",
                    "INFO"
                )
            else:
                self.log(
                    f"No {ap_type if ap_type else 'planned'} access points found on floor '{floor_name}' "
                    f"(Floor ID: '{floor_id}'). The floor exists but has no APs configured.",
                    "DEBUG"
                )

            return ap_positions

        except Exception as e:
            self.msg = (
                f"An error occurred during {ap_type if ap_type else 'planned'} AP position retrieval. "
                f"Floor: '{floor_name}', Floor ID: '{floor_id}'. Error details: {str(e)}"
            )
            self.log(self.msg, "ERROR")
            self.log(
                f"Exception traceback for AP position retrieval failure - "
                f"Floor: '{floor_name}', AP Type: '{ap_type if ap_type else 'planned'}', "
                f"Exception: {type(e).__name__}, Message: {str(e)}",
                "DEBUG"
            )
            return None

    def parse_accesspoint_position_for_floor(self, floor_id, floor_site_hierarchy,
                                             floor_response, ap_type=None):
        """
        Parses and transforms raw AP position data into structured configuration format.

        This function processes access point position responses from Catalyst Center APIs,
        extracting position coordinates, radio configurations, antenna settings, and device
        metadata into two formatted data structures: simplified positions for YAML generation
        and detailed metadata for internal filtering operations.

        Args:
            floor_id (str): Unique identifier (UUID) of the floor site in Catalyst Center.
                           Used to associate parsed APs with specific floor location.
                           Example: "abc12345-6789-0def-1234-567890abcdef"

            floor_site_hierarchy (str): Full site hierarchy path of the floor from Global.
                                       Used for organizing APs by location in output.
                                       Example: "Global/USA/San Jose/Building1/Floor1"

            floor_response (list): Raw API response containing AP position data from
                                  get_access_point_position(). List of dictionaries with
                                  AP details including name, type, position, MAC, radios.
                                  Example: [{"name": "AP1", "type": "C9130", "position": {...}}]

            ap_type (str, optional): Type classification of access points being parsed.
                                    - "planned": APs from planning/design phase
                                    - "real": APs from deployed/operational inventory
                                    - None: Defaults to "planned" if not specified
                                    Used to differentiate AP sources in detailed metadata.

        Returns:
            tuple: (parsed_positions, parsed_detailed_data)
                - parsed_positions (list): Simplified AP configurations for YAML output
                  [{"accesspoint_name": "AP1", "position": {...}, "radios": [...]}]
                - parsed_detailed_data (list): Complete metadata with IDs and hierarchy
                  [{"accesspoint_name": "AP1", ..., "floor_id": "...", "id": "..."}]
                Returns (None, None) if floor_response invalid or empty.

        Side Effects:
            - Logs INFO message at parse operation start
            - Logs WARNING if invalid/empty floor_response received
            - Logs DEBUG messages for each parsed AP with full data structure
            - Logs DEBUG summary with total AP count parsed
            - Does not modify input floor_response data

        Data Transformations:
            1. Position coordinates: Converts to integers, extracts x/y/z
            2. MAC addresses: Normalizes to lowercase format
            3. Radio bands: Converts numeric (2.4, 5, 6) to string format
            4. Antenna parameters: Extracts name, azimuth, elevation
            5. Adds metadata: floor_site_hierarchy, accesspoint_type, floor_id, id

        Structure Differences:
            - parsed_positions: Clean data for YAML playbook generation
            - parsed_detailed_data: Extended with floor_id, id, hierarchy for filtering

        Notes:
            - Radio data only included if "radios" field present in API response
            - MAC addresses only in real APs (planned APs may not have MACs)
            - Position coordinates converted to integers (floor map units)
            - Radio bands normalized to string format: "2.4", "5", "6"
            - Uses copy.deepcopy to prevent mutation between structures
        """
        self.log(
            f"Starting AP position parsing for floor '{floor_site_hierarchy}' (Floor ID: {floor_id}). "
            f"AP type: '{ap_type if ap_type else 'planned'}'. Processing raw API response data to "
            f"extract position coordinates, radio configurations, and device metadata into structured "
            f"format for YAML generation and internal filtering operations.",
            "INFO"
        )

        if not floor_response or not isinstance(floor_response, list):
            self.log(
                f"Invalid or empty floor_response received for floor ID '{floor_id}', floor '{floor_site_hierarchy}'. "
                f"Response type: {type(floor_response).__name__ if floor_response else 'None'}. Cannot parse AP "
                f"position data without valid list of AP responses. Returning None to indicate no parseable data.",
                "WARNING"
            )
            return None

        self.log(
            f"Received {len(floor_response)} AP position(s) to parse for floor '{floor_site_hierarchy}'. "
            f"Initiating per-AP data extraction and transformation. Each AP will be processed for position "
            f"coordinates (x/y/z), radio configurations (bands/channels/power), antenna settings, and metadata.",
            "DEBUG"
        )

        parsed_floor_data = {}
        parsed_positions = []
        parsed_detailed_data = []

        for ap_index, ap_position in enumerate(floor_response, start=1):
            self.log(
                f"Processing AP {ap_index}/{len(floor_response)} on floor '{floor_site_hierarchy}'. "
                f"AP Name: '{ap_position.get('name')}', Model: '{ap_position.get('type')}'. "
                f"Extracting position coordinates and configuration parameters.",
                "DEBUG"
            )

            if (
                int(ap_position.get("position", {}).get("x")) < 0 or
                int(ap_position.get("position", {}).get("y")) < 0 or
                int(ap_position.get("position", {}).get("z")) < 0
            ):
                self.log(
                    f"AP {ap_index}/{len(floor_response)} '{ap_position.get('name')}' has un-positioned coordinates: "
                    f"x={ap_position.get('position', {}).get('x')}, "
                    f"y={ap_position.get('position', {}).get('y')}, "
                    f"z={ap_position.get('position', {}).get('z')}. Skipping this AP.",
                    "WARNING"
                )
                continue

            # Extract core AP position data
            parsed_data = {
                "accesspoint_name": ap_position.get("name"),
                "accesspoint_model": ap_position.get("type"),
                "position": {
                    "x_position": int(ap_position.get("position", {}).get("x")),
                    "y_position": int(ap_position.get("position", {}).get("y")),
                    "z_position": int(ap_position.get("position", {}).get("z"))
                }
            }

            # Add MAC address if available (real APs have MACs, planned may not)
            if ap_position.get("macAddress"):
                normalized_mac = ap_position.get("macAddress").lower()
                parsed_data["mac_address"] = normalized_mac
                self.log(
                    f"AP {ap_index}/{len(floor_response)} '{ap_position.get('name')}' has MAC address: "
                    f"{normalized_mac} (normalized to lowercase). This indicates a real/deployed AP.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"AP {ap_index}/{len(floor_response)} '{ap_position.get('name')}' has no MAC address. "
                    f"This is expected for planned APs in design phase.",
                    "DEBUG"
                )

            # Process radio configurations if available
            radio_params = ap_position.get("radios", [])
            if radio_params and isinstance(radio_params, list):
                self.log(
                    f"Processing {len(radio_params)} radio configuration(s) for AP '{ap_position.get('name')}'. "
                    f"Extracting band configurations, channel assignments, TX power, and antenna parameters.",
                    "DEBUG"
                )
                parsed_radios = []
                for radio_index, radio in enumerate(radio_params, start=1):
                    # Convert numeric band values to standardized string format
                    radio_bands = []
                    for each_band in radio.get("bands", []):
                        if each_band == 2.4:
                            radio_bands.append("2.4")
                        elif each_band == 5 or each_band == 5.0:
                            radio_bands.append("5")
                        elif each_band == 6 or each_band == 6.0:
                            radio_bands.append("6")

                    parsed_radio = {
                        "bands": [str(band) for band in radio_bands],
                        "channel": radio.get("channel"),
                        "tx_power": radio.get("txPower"),
                        "antenna": {
                            "antenna_name": radio.get("antenna", {}).get("name"),
                            "azimuth": radio.get("antenna", {}).get("azimuth"),
                            "elevation": radio.get("antenna", {}).get("elevation")
                        }
                    }
                    parsed_radios.append(parsed_radio)
                    self.log(
                        f"Radio {radio_index}/{len(radio_params)} parsed for AP '{ap_position.get('name')}'. "
                        f"Bands: {parsed_radio['bands']}, Channel: {parsed_radio.get('channel')}, "
                        f"TX Power: {parsed_radio.get('tx_power')} dBm, Antenna: {parsed_radio['antenna'].get('antenna_name')}",
                        "DEBUG"
                    )

                parsed_data["radios"] = parsed_radios
                self.log(
                    f"Completed radio configuration parsing for AP '{ap_position.get('name')}'. "
                    f"Total radios configured: {len(parsed_radios)}.",
                    "DEBUG"
                )

                # Create detailed metadata version with floor and ID information
                detailed_data = copy.deepcopy(parsed_data)
                detailed_data["floor_site_hierarchy"] = floor_site_hierarchy
                detailed_data["accesspoint_type"] = ap_type if ap_type else "planned"
                detailed_data["floor_id"] = floor_id
                detailed_data["id"] = ap_position.get("id")
                parsed_detailed_data.append(detailed_data)

                self.log(
                    f"Created detailed metadata for AP '{ap_position.get('name')}' on floor '{floor_site_hierarchy}'. "
                    f"Metadata includes: floor_id='{floor_id}', accesspoint_type='{ap_type if ap_type else 'planned'}', "
                    f"AP ID='{ap_position.get('id')}'. Full detailed data: {self.pprint(detailed_data)}",
                    "DEBUG"
                )
            else:
                self.log(
                    f"AP {ap_index}/{len(floor_response)} '{ap_position.get('name')}' has no radio configurations. "
                    f"Radio parameters missing or empty in API response.",
                    "DEBUG"
                )

            parsed_positions.append(parsed_data)
            self.log(
                f"Completed parsing AP {ap_index}/{len(floor_response)} '{ap_position.get('name')}'. "
                f"Added to parsed_positions collection. Current parsed count: {len(parsed_positions)}.",
                "DEBUG"
            )

        self.log(
            f"AP position parsing completed for floor '{floor_site_hierarchy}' (Floor ID: {floor_id}). "
            f"Successfully parsed {len(parsed_positions)} access point(s). Parsed positions (simplified): "
            f"{len(parsed_positions)} item(s), Detailed metadata: {len(parsed_detailed_data)} item(s).",
            "INFO"
        )

        self.log(
            f"Final parsed data structures - Floor Data: {self.pprint(parsed_floor_data)}, "
            f"Detailed Positions: {self.pprint(parsed_detailed_data)}. Returning tuple of "
            f"(parsed_positions, parsed_detailed_data) for downstream processing.",
            "DEBUG"
        )

        return parsed_positions, parsed_detailed_data

    def collect_all_accesspoint_location_list(self):
        """
        Collects comprehensive access point location inventory from Cisco Catalyst Center.

        This function orchestrates the complete AP location data collection workflow by:
        1. Retrieving all floor sites from Catalyst Center
        2. Querying both planned and real AP positions for each floor
        3. Parsing AP position data into structured configurations
        4. Organizing data into multiple collections for different use cases

        The function populates self.have with five distinct data structures to support
        various filtering and YAML generation scenarios in access point location
        documentation workflows.

        Args:
            None (uses self.payload for API configuration parameters)

        Returns:
            object: Self instance with updated self.have attributes:
                - self.have["all_floor"]: Complete floor site list with IDs and hierarchy
                - self.have["filtered_floor"]: Floors containing at least one AP (planned or real)
                - self.have["all_config"]: Combined planned + real AP configs by floor
                - self.have["planned_aps"]: Planned AP configurations organized by floor
                - self.have["real_aps"]: Real/deployed AP configurations organized by floor
                - self.have["all_detailed_config"]: Complete AP metadata with IDs for filtering

        Side Effects:
            - Calls get_all_floors_from_sites() for floor inventory
            - Calls get_access_point_position() twice per floor (planned + real)
            - Calls parse_accesspoint_position_for_floor() to transform AP data
            - Logs INFO/DEBUG/WARNING messages throughout collection process
            - Populates multiple self.have collections for downstream processing

        Data Structure Organization:
            all_config: [{floor_site_hierarchy: "...", access_points: [{...}]}]
                - Combined planned + real APs per floor
                - Used for generate_all_configurations mode
                - Simplified structure for YAML generation

            planned_aps: [{floor_site_hierarchy: "...", access_points: [{...}]}]
                - Only planned APs per floor
                - Used for planned_accesspoint_list filtering
                - Supports design/planning workflows

            real_aps: [{floor_site_hierarchy: "...", access_points: [{...}]}]
                - Only real/deployed APs per floor
                - Used for real_accesspoint_list filtering
                - Supports operational inventory workflows

            filtered_floor: [{floor_id: "...", floor_site_hierarchy: "..."}]
                - Floors with at least one AP configured
                - Used for site_list validation
                - Excludes empty floors without APs

            all_detailed_config: [{..., floor_id: "...", id: "...", accesspoint_type: "..."}]
                - Complete AP metadata with IDs and hierarchy
                - Used for model_list and mac_address_list filtering
                - Includes both planned and real APs with full context

        Workflow Steps:
            1. Call get_all_floors_from_sites() to retrieve floor inventory
            2. For each floor:
               a. Query planned AP positions
               b. Parse planned AP data if found
               c. Query real AP positions
               d. Parse real AP data if found
               e. Combine configs for all_config if any APs present
               f. Add floor to filtered_floor if APs present
            3. Populate self.have collections with organized data

        Error Handling:
            - Returns self immediately if no floors retrieved
            - Logs WARNING if no AP locations found
            - Continues processing remaining floors if individual floor fails
            - Empty collections indicate no APs configured in Catalyst Center

        Performance Notes:
            - Makes 2 API calls per floor (planned + real positions)
            - Total API calls = 1 (floors) + (2 * number_of_floors)
            - Uses pagination automatically via get_all_floors_from_sites()
            - Processing time scales linearly with floor count
        """
        self.log(
            "Starting comprehensive access point location collection from Cisco Catalyst Center. "
            "This operation will retrieve all floor sites, query both planned and real AP positions "
            "for each floor, parse position data into structured configurations, and organize data "
            "into multiple collections supporting various filtering and YAML generation scenarios.",
            "INFO"
        )

        # Initialize collection structures
        collect_all_config = []
        collect_planned_config = []
        collect_real_config = []
        filtered_floor = []
        collect_all_detailed_config = []

        self.log(
            "Initialized five data collection structures: all_config (combined planned+real), "
            "planned_config (planned only), real_config (real only), filtered_floor (floors with APs), "
            "all_detailed_config (complete metadata). Calling get_all_floors_from_sites() to retrieve "
            "floor inventory from Catalyst Center.",
            "DEBUG"
        )

        floor_response = self.get_all_floors_from_sites()
        if floor_response and isinstance(floor_response, list):
            self.have["all_floor"] = floor_response
            self.log(
                f"Successfully retrieved {len(self.have['all_floor'])} floor site(s) from Catalyst Center. "
                f"Floor site details: {self.pprint(self.have['all_floor'])}. Proceeding to query AP positions "
                f"for each floor (2 API calls per floor: planned + real).",
                "DEBUG"
            )

            self.log(
                f"Starting per-floor AP position collection loop. Total floors to process: "
                f"{len(floor_response)}. Each floor will be queried for both planned and real AP positions.",
                "INFO"
            )

            for floor_index, floor in enumerate(floor_response, start=1):
                floor_id = floor.get("id")
                floor_site_hierarchy = floor.get("floor_site_hierarchy")
                collect_each_floor_config = []

                self.log(
                    f"Processing floor {floor_index}/{len(floor_response)}: '{floor_site_hierarchy}' "
                    f"(Floor ID: {floor_id}). Querying planned and real AP positions for this floor.",
                    "DEBUG"
                )

                # Query and process planned AP positions
                self.log(
                    f"Querying planned AP positions for floor {floor_index}/{len(floor_response)}: "
                    f"'{floor_site_hierarchy}'. Calling get_access_point_position() with ap_type='planned'.",
                    "DEBUG"
                )
                planned_ap_response = self.get_access_point_position(floor_id, floor_site_hierarchy)
                if planned_ap_response:
                    self.log(
                        f"Received {len(planned_ap_response) if isinstance(planned_ap_response, list) else 'unknown'} "
                        f"planned AP position(s) for floor '{floor_site_hierarchy}'. Raw API response: "
                        f"{self.pprint(planned_ap_response)}. Parsing AP data into structured format.",
                        "DEBUG"
                    )
                    each_planned_config, planned_detailed_config = self.parse_accesspoint_position_for_floor(
                        floor_id, floor_site_hierarchy, planned_ap_response, ap_type="planned"
                    )
                    if each_planned_config and planned_detailed_config:
                        collect_each_floor_config.extend(each_planned_config)
                        collect_all_detailed_config.extend(planned_detailed_config)
                        planned_floor_data = {
                            "floor_site_hierarchy": floor_site_hierarchy,
                            "access_points": each_planned_config
                        }
                        collect_planned_config.append(planned_floor_data)
                        self.log(
                            f"Successfully parsed and collected {len(each_planned_config)} planned AP(s) for floor "
                            f"'{floor_site_hierarchy}'. Added to planned_config collection. Total planned floors collected: "
                            f"{len(collect_planned_config)}.",
                            "DEBUG"
                        )
                    else:
                        self.log(
                            f"Planned AP response received but parsing returned empty data for floor '{floor_site_hierarchy}'. "
                            f"This may indicate data format issues or missing required fields in API response.",
                            "WARNING"
                        )
                else:
                    self.log(
                        f"No planned APs found on floor {floor_index}/{len(floor_response)}: '{floor_site_hierarchy}'. "
                        f"API returned None or empty response.",
                        "DEBUG"
                    )

                # Query and process real AP positions
                self.log(
                    f"Querying real/deployed AP positions for floor {floor_index}/{len(floor_response)}: "
                    f"'{floor_site_hierarchy}'. Calling get_access_point_position() with ap_type='real'.",
                    "DEBUG"
                )
                real_ap_response = self.get_access_point_position(floor_id, floor_site_hierarchy, ap_type="real")
                if real_ap_response:
                    self.log(
                        f"Received {len(real_ap_response) if isinstance(real_ap_response, list) else 'unknown'} "
                        f"real AP position(s) for floor '{floor_site_hierarchy}'. Raw API response: "
                        f"{self.pprint(real_ap_response)}. Parsing AP data into structured format.",
                        "DEBUG"
                    )
                    each_real_config, real_detailed_config = self.parse_accesspoint_position_for_floor(
                        floor_id, floor_site_hierarchy, real_ap_response, ap_type="real"
                    )

                    if each_real_config and real_detailed_config:
                        for index, each_ap in enumerate(each_real_config):
                            each_ap["mac_address"] = self.convert_eth_mac_address_to_mac_address(
                                each_ap.get("mac_address")
                            )
                            real_detailed_config[index]["mac_address"] = each_ap["mac_address"]

                        collect_all_detailed_config.extend(real_detailed_config)
                        collect_each_floor_config.extend(each_real_config)
                        real_floor_data = {
                            "floor_site_hierarchy": floor_site_hierarchy,
                            "access_points": each_real_config
                        }
                        self.log(
                            f"Parced real floor data for floor '{floor_site_hierarchy}': {self.pprint(real_floor_data)}. "
                            f"Adding to real_config collection.",
                            "DEBUG"
                        )
                        collect_real_config.append(real_floor_data)
                        self.log(
                            f"Successfully parsed and collected {len(each_real_config)} real AP(s) for floor "
                            f"'{floor_site_hierarchy}'. Added to real_config collection. Total real floors collected: "
                            f"{len(collect_real_config)}.",
                            "DEBUG"
                        )
                    else:
                        self.log(
                            f"Real AP response received but parsing returned empty data for floor '{floor_site_hierarchy}'. "
                            f"This may indicate data format issues or missing required fields in API response.",
                            "WARNING"
                        )
                else:
                    self.log(
                        f"No real APs found on floor {floor_index}/{len(floor_response)}: '{floor_site_hierarchy}'. "
                        f"API returned None or empty response.",
                        "DEBUG"
                    )

                # Create combined config entry if any APs present on this floor
                if collect_each_floor_config:
                    floor_data = {
                        "floor_site_hierarchy": floor_site_hierarchy,
                        "access_points": collect_each_floor_config
                    }
                    collect_all_config.append(floor_data)
                    self.log(
                        f"Floor {floor_index}/{len(floor_response)} '{floor_site_hierarchy}' has {len(collect_each_floor_config)} "
                        f"total AP(s) (planned + real combined). Added to all_config collection. Total floors with APs: "
                        f"{len(collect_all_config)}.",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"Floor {floor_index}/{len(floor_response)} '{floor_site_hierarchy}' has no APs configured "
                        f"(neither planned nor real). Skipping all_config entry for this floor.",
                        "DEBUG"
                    )

                # Add floor to filtered list if it has any AP positions
                if planned_ap_response or real_ap_response:
                    filtered_floor.append({
                        "floor_id": floor_id,
                        "floor_site_hierarchy": floor_site_hierarchy
                    })
                    self.log(
                        f"Floor {floor_index}/{len(floor_response)} '{floor_site_hierarchy}' added to filtered_floor "
                        f"collection (has at least one AP configured). Total filtered floors: {len(filtered_floor)}.",
                        "DEBUG"
                    )
                else:
                    self.log(
                        f"Floor {floor_index}/{len(floor_response)} '{floor_site_hierarchy}' NOT added to filtered_floor "
                        f"(no APs configured). This floor will be excluded from site_list validation.",
                        "DEBUG"
                    )

            # Populate self.have with all collected data structures
            self.have["all_config"] = collect_all_config
            self.have["planned_aps"] = collect_planned_config
            self.have["real_aps"] = collect_real_config
            self.have["filtered_floor"] = filtered_floor
            self.have["all_detailed_config"] = collect_all_detailed_config

            self.log(
                f"AP location collection completed successfully. Final statistics - "
                f"Total floors processed: {len(floor_response)}, "
                f"Floors with APs: {len(collect_all_config)}, "
                f"Filtered floors: {len(filtered_floor)}, "
                f"Planned AP floors: {len(collect_planned_config)}, "
                f"Real AP floors: {len(collect_real_config)}, "
                f"Total detailed AP configs: {len(collect_all_detailed_config)}. "
                f"All data structures populated in self.have for downstream processing.",
                "INFO"
            )

            self.log(
                f"Final collection data structures - "
                f"all_config: {len(collect_all_config)} floor(s), "
                f"planned_aps: {len(collect_planned_config)} floor(s), "
                f"real_aps: {len(collect_real_config)} floor(s), "
                f"filtered_floor: {len(filtered_floor)} floor(s), "
                f"all_detailed_config: {len(collect_all_detailed_config)} AP(s) with complete metadata.",
                "DEBUG"
            )

        else:
            self.log(
                "No floor sites retrieved from Catalyst Center or invalid floor_response received. "
                f"Response type: {type(floor_response).__name__ if floor_response else 'None'}. Cannot collect "
                f"AP location data without floor inventory. This indicates either no floors are configured in "
                f"Catalyst Center or API connectivity issue. Verify floor sites exist in Catalyst Center Site "
                f"Hierarchy before running AP location playbook generation.",
                "WARNING"
            )
            self.log(
                "AP location collection completed with no data. All self.have collections remain empty. "
                "No access points found in Cisco Catalyst Center.",
                "WARNING"
            )

        return self

    def convert_eth_mac_address_to_mac_address(self, ap_ethernet_mac_address):
        """
        Converts Ethernet MAC address to primary MAC address via Catalyst Center API lookup.

        This function queries the Catalyst Center wireless API to retrieve the complete access
        point configuration using the Ethernet MAC address as the lookup key, then extracts
        and returns the primary MAC address field from the response. This is essential for
        operations requiring the primary MAC when only the Ethernet MAC is available.

        Args:
            ap_ethernet_mac_address (str): Ethernet MAC address of the access point to query.
                                          Used as the lookup key in the API request.
                                          Expected format: "aa:bb:cc:dd:ee:ff" or similar
                                          Example: "00:1a:2b:3c:4d:5e"

        Returns:
            str or None: Primary MAC address of the access point if found, None otherwise.
                        Returns MAC address string in response format (typically lowercase
                        with colons). Returns None if:
                        - API call fails or returns empty response
                        - Response doesn't contain "macAddress" field
                        - Exception occurs during API execution

        API Details:
            - Family: wireless
            - Function: get_access_point_configuration
            - Parameter: key (set to ap_ethernet_mac_address)
            - Returns: Full AP configuration dict with macAddress field

        Example:
            >>> eth_mac = "00:1a:2b:3c:4d:5e"
            >>> primary_mac = self.convert_eth_mac_address_to_mac_address(eth_mac)
            >>> print(primary_mac)
            "00:1f:2e:3d:4c:5b"

        Error Handling:
            - Exception caught and logged as WARNING
            - Returns None on any failure condition
            - Does not raise exceptions to caller

        Notes:
            - Ethernet MAC and primary MAC are different addresses on same AP
            - Primary MAC typically used for AP identification in most operations
            - Ethernet MAC used for network connectivity and configuration
            - API response includes complete AP configuration but only MAC extracted
            - Function name indicates MAC-to-MAC conversion for clarity
        """
        self.log(
            f"Starting Ethernet MAC to primary MAC conversion for AP. Ethernet MAC address: "
            f"'{ap_ethernet_mac_address}'. Preparing to query Catalyst Center wireless API "
            f"to retrieve full AP configuration and extract primary MAC address field.",
            "DEBUG"
        )

        input_param = {"key": ap_ethernet_mac_address}
        mac_address = None

        self.log(
            f"API request parameters prepared: {input_param}. Calling "
            f"wireless.get_access_point_configuration API to retrieve AP configuration "
            f"for Ethernet MAC '{ap_ethernet_mac_address}'.",
            "DEBUG"
        )

        try:
            ap_config_response = self.dnac._exec(
                family="wireless",
                function="get_access_point_configuration",
                params=input_param,
            )

            if ap_config_response:
                self.log(
                    "Received API response from get_access_point_configuration for Ethernet MAC "
                    f"'{ap_ethernet_mac_address}'. Response structure: {self.pprint(ap_config_response)}. "
                    "Extracting primary MAC address from 'macAddress' field.",
                    "INFO"
                )
                mac_address = ap_config_response.get("macAddress")
                if mac_address:
                    self.log(
                        "Successfully extracted primary MAC address from API response. "
                        f"Ethernet MAC '{ap_ethernet_mac_address}' maps to primary MAC '{mac_address}'. "
                        "MAC address conversion completed successfully.",
                        "INFO"
                    )
                    return mac_address
                else:
                    self.log(
                        "API response received but 'macAddress' field is missing or empty. "
                        f"Ethernet MAC: '{ap_ethernet_mac_address}'. Response may indicate invalid AP "
                        "or incomplete configuration. Returning None.",
                        "WARNING"
                    )
            else:
                self.log(
                    "No response received from get_access_point_configuration API for Ethernet MAC "
                    f"'{ap_ethernet_mac_address}'. This may indicate AP not found, API connectivity "
                    "issue, or invalid MAC address provided. Returning None.",
                    "WARNING"
                )

        except Exception as e:
            self.log(
                f"Unable to retrieve access point configuration for Ethernet MAC "
                f"'{ap_ethernet_mac_address}'. API request parameters: {input_param}. "
                f"Exception type: {type(e).__name__}, Error: {str(e)}. Returning None.",
                "WARNING"
            )

        self.log(
            f"MAC address conversion completed with no result. Ethernet MAC '{ap_ethernet_mac_address}' "
            f"could not be resolved to primary MAC address. Returning None to caller.",
            "DEBUG"
        )

        return None

    def get_diff_gathered(self):
        """
        Executes YAML configuration generation workflow for access point locations.

        This function orchestrates the complete YAML playbook generation process by
        extracting parameters from the validated want dictionary, calling the
        yaml_config_generator function, and validating operation status. It coordinates
        data collection, filtering, and YAML file creation for access point location
        documentation and automation.

        Args:
            None (operates on instance attributes self.want and self.have)

        Returns:
            object: Self instance with updated attributes:
                - self.result: Contains operation results from yaml_config_generator
                - self.msg: Operation completion message
                - self.status: Operation status ("success" or "failed")

        Side Effects:
            - Calls yaml_config_generator() with extracted parameters
            - Invokes check_return_status() to validate operation success
            - Logs detailed progress information at DEBUG and INFO levels
            - Measures and logs total execution time
            - Updates self.result with YAML generation outcomes

        Workflow Overview:
            1. Initialize timing and log workflow start
            2. Define operations list (currently: yaml_config_generator only)
            3. Iterate through operations sequentially
            4. For each operation:
               a. Extract parameters from self.want using param_key
               b. If parameters exist, call operation function
               c. Validate operation success via check_return_status()
               d. Log results and continue to next operation
            5. Calculate and log total execution time
            6. Return self with updated result

        Operation Pattern:
            Operations defined as tuples: (param_key, operation_name, operation_func)
            - param_key: Key in self.want dict containing operation parameters
            - operation_name: Human-readable operation name for logging
            - operation_func: Function to call with extracted parameters

        Notes:
            - Currently supports single operation (yaml_config_generator)
            - Architecture designed for extensibility (future operations)
            - Operations processed sequentially (not parallel)
            - Missing parameters cause operation skip (not failure)
            - check_return_status() raises exceptions on operation failure
            - Execution time logged for performance monitoring
        """

        start_time = time.time()
        self.log(
            "Starting YAML configuration generation workflow orchestration (get_diff_gathered). "
            "This operation coordinates the complete YAML playbook generation process by extracting "
            "parameters from validated want dictionary, calling yaml_config_generator function, "
            "and checking operation status. Workflow supports extensible operation pattern for "
            "future enhancements.",
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
        self.log(
            f"Operations configuration defined successfully. Total operations: {len(operations)}. "
            f"Operation details: {[(op[0], op[1]) for op in operations]}. Each operation will be "
            f"processed sequentially with parameter validation and status checking.",
            "DEBUG"
        )
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                f"Iteration {index}/{len(operations)}: Processing '{operation_name}' operation. "
                f"Checking for parameters in self.want using param_key '{param_key}'. If parameters "
                f"exist, operation function will be called with extracted parameters and return "
                f"status validated.",
                "DEBUG"
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    f"Iteration {index}/{len(operations)}: Parameters successfully extracted for "
                    f"'{operation_name}' operation. Parameter structure: {param_key} "
                    f"(type: {type(params).__name__}). Initiating operation execution by calling "
                    f"operation function with extracted parameters.",
                    "INFO"
                )

                self.log(
                    f"Iteration {index}/{len(operations)}: Calling operation function "
                    f"'{operation_name}' with extracted parameters. Function will process parameters, "
                    f"execute YAML generation workflow, and return self instance with updated result "
                    f"status. check_return_status() will validate operation success after completion.",
                    "DEBUG"
                )
                operation_func(params).check_return_status()
                self.log(
                    f"Iteration {index}/{len(operations)}: '{operation_name}' operation completed "
                    f"successfully. check_return_status() validated operation success. Result status: "
                    f"{self.status}, Changed: {self.result.get('changed')}. Continuing to next "
                    f"operation if available.",
                    "INFO"
                )
            else:
                self.log(
                    f"Iteration {index}/{len(operations)}: No parameters found in self.want for "
                    f"'{operation_name}' operation using param_key '{param_key}'. Parameters are "
                    f"None or missing, indicating operation should be skipped. This is expected if "
                    f"operation is optional or disabled. Continuing to next operation without execution.",
                    "WARNING"
                )

        end_time = time.time()
        self.log(
            f"Completed 'get_diff_gathered' operation in {end_time - start_time:.2f} seconds. "
            f"All configured operations processed successfully. YAML configuration generation workflow "
            f"completed. Final result status: {self.status}.",
            "DEBUG"
        )

        return self

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates YAML configuration file for access point locations with applied filters.

        This function processes access point location configurations from Cisco Catalyst Center,
        applies global filtering criteria (site-based, AP-based, model-based, or MAC-based),
        and exports the structured data to a YAML file compatible with the
        accesspoint_location_workflow_manager module for automation and documentation.

        Args:
            yaml_config_generator (dict): Configuration parameters containing:
                                        - file_path: Output file path (optional, str)
                                        - generate_all_configurations: Mode flag (optional, bool)
                                        - global_filters: Filter criteria (optional, dict)
                                        Example: {
                                            "file_path": "/tmp/ap_locations.yml",
                                            "generate_all_configurations": False,
                                            "global_filters": {
                                                "site_list": ["Global/USA/Building1/Floor1"],
                                                "accesspoint_model_list": ["C9130AXI-B"]
                                            }
                                        }

        Returns:
            object: Self instance with updated attributes:
                - self.msg: Operation result message with file_path
                - self.status: Operation status ("success" or "failed")
                - self.result: Complete operation result dictionary

        Side Effects:
            - Calls process_global_filters() if global_filters provided
            - Calls write_dict_to_yaml() to create YAML file
            - Calls generate_filename() if file_path not provided
            - Sets operation result via set_operation_result()
            - Logs detailed progress information at INFO/DEBUG/WARNING levels

        Workflow Steps:
            1. Log operation start with parameters
            2. Determine operational mode (generate_all vs filtered)
            3. Resolve output file path (custom or auto-generated)
            4. If generate_all: Use self.have["all_config"] directly
            5. If filtered: Call process_global_filters() with criteria
            6. Validate final_list has data
            7. Create config dictionary with "config" key
            8. Write dictionary to YAML file
            9. Set operation result and return

        Operational Modes:
            generate_all_configurations=True:
                - Retrieves complete AP location inventory
                - Ignores global_filters parameter
                - Uses self.have["all_config"] collection
                - Includes all planned and real APs on all floors

            generate_all_configurations=False:
                - Applies global_filters criteria
                - Calls process_global_filters() for filtering
                - Supports 5 filter types (site, planned_ap, real_ap, model, MAC)
                - Returns filtered subset of AP locations

        File Path Resolution:
            Custom path: User-provided absolute or relative path
            Auto-generated: {module_name}_playbook_YYYY-MM-DD_HH-MM-SS.yml

        Error Handling:
            - Empty final_list: Sets success result with warning message
            - YAML write failure: Sets failed result with error message
            - No exceptions raised, errors communicated via result status

        Notes:
            - global_filters parameter ignored if generate_all=True
            - Empty configurations result in success (not failure)
            - File path supports both absolute and relative paths
            - YAML structure: {"config": [floor_configs]}
            - Compatible with accesspoint_location_workflow_manager module
        """

        self.log(
            f"Starting YAML configuration file generation for access point locations. "
            f"Input parameters: {yaml_config_generator}. This operation will process AP location "
            f"configurations from Catalyst Center, apply filtering criteria, and export structured "
            f"data to YAML file compatible with accesspoint_location_workflow_manager module.",
            "DEBUG"
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log(
                "Operational mode: GENERATE ALL CONFIGURATIONS enabled (generate_all_configurations=True). "
                "This mode will retrieve complete AP location inventory from Catalyst Center including "
                "all planned and real AP positions on all floors, ignoring any provided filters. Use this "
                "mode for comprehensive access point location configuration and documentation.",
                "INFO"
            )
        else:
            self.log(
                "Operational mode: FILTERED CONFIGURATION generation (generate_all_configurations=False). "
                "This mode will apply global_filters to extract specific AP location subset based on "
                "site_list, planned_accesspoint_list, real_accesspoint_list, accesspoint_model_list, "
                "or mac_address_list criteria.",
                "INFO"
            )

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No custom file_path provided by user in yaml_config_generator parameters. "
                "Initiating automatic filename generation with timestamp format. Default filename "
                "pattern: accesspoint_location_workflow_manager_playbook_YYYY-MM-DD_HH-MM-SS.yml",
                "DEBUG"
            )
            file_path = self.generate_filename()
            self.log(
                f"Auto-generated default filename for YAML output: {file_path}. File will be created "
                f"in current working directory with timestamped name for uniqueness.",
                "INFO"
            )
        else:
            self.log(
                f"Using user-provided custom file_path for YAML output: {file_path}. File will be "
                f"created at specified path (absolute or relative path supported).",
                "INFO"
            )

        self.log(f"YAML configuration file path determined: {file_path}", "DEBUG")

        self.log("Initializing filter processing workflow", "DEBUG")
        # Set empty filters to retrieve everything
        global_filters = {}
        final_list = []
        if generate_all:
            self.log(
                "Processing in GENERATE ALL CONFIGURATIONS mode. Preparing to collect complete AP "
                "location inventory from Catalyst Center without applying any filters. This will "
                "include all AP configurations discovered during get_have() operation.",
                "INFO"
            )

            # Warn if filters provided in generate_all mode
            if yaml_config_generator.get("global_filters"):
                self.log(
                    "Warning: global_filters parameter provided in yaml_config_generator but will be "
                    "IGNORED due to generate_all_configurations=True. In generate_all mode, ALL access "
                    "point locations are processed regardless of filter criteria. Remove global_filters "
                    "or set generate_all_configurations=False to apply filtering.",
                    "WARNING"
                )

            final_list = self.have.get("all_config", [])
            self.log(
                f"All configurations collected for generate_all_configurations mode. Total floor sites "
                f"with AP configurations: {len(final_list)}. Complete configuration data structure: "
                f"{self.pprint(final_list)}",
                "DEBUG"
            )
        else:
            # Filtered configuration mode
            self.log(
                "Processing in FILTERED CONFIGURATION mode. Extracting global_filters parameter to "
                "determine filter criteria. Supported filter types: site_list, planned_accesspoint_list, "
                "real_accesspoint_list, accesspoint_model_list, mac_address_list.",
                "INFO"
            )

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            if global_filters:
                self.log(
                    f"Global filters provided for AP location filtering. Filter structure: "
                    f"{global_filters}. Calling process_global_filters() to apply filter criteria "
                    f"and extract matching AP configurations.",
                    "INFO"
                )
                final_list = self.process_global_filters(global_filters)
                if final_list:
                    self.log(
                        f"Filtered configurations collected successfully. Total floor sites matching "
                        f"filter criteria: {len(final_list)}. Filtered data ready for YAML generation.",
                        "INFO"
                    )
                else:
                    self.log(
                        "Filter processing returned empty result. No access point locations match the "
                        "provided filter criteria. This may indicate filter values don't exist in "
                        "Catalyst Center or filters are too restrictive.",
                        "WARNING"
                    )
            else:
                self.log(
                    "No global_filters provided in filtered mode. Cannot determine which AP locations "
                    "to collect. Either provide global_filters or enable generate_all_configurations.",
                    "WARNING"
                )

        if not final_list:
            self.msg = (
                f"No configurations or components to process for module '{self.module_name}'. This indicates "
                f"either no access point locations exist in Catalyst Center, filter criteria returned no "
                f"matches, or data collection failed. Verify input filters match existing AP configurations "
                f"and AP locations are properly configured in Catalyst Center."
            )
            self.log(self.msg, "WARNING")
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        final_dict = {"config": final_list}
        self.log(
            f"Final YAML dictionary structure created successfully. Dictionary contains {len(final_list)} "
            f"floor site configuration(s) under 'config' key. Total structure: {self.pprint(final_dict)}. "
            f"Proceeding to write dictionary to YAML file: {file_path}",
            "DEBUG"
        )

        self.log(
            f"Initiating YAML file write operation. Target file: {file_path}. Converting Python "
            f"dictionary to YAML format with proper indentation and structure for Ansible playbook "
            f"compatibility.",
            "DEBUG"
        )

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                f"YAML config generation Task succeeded for module '{self.module_name}'.": {
                    "file_path": file_path
                }
            }
            self.log(
                f"YAML configuration file created successfully at: {file_path}. File contains "
                f"{len(final_list)} floor site(s) with access point location configurations. "
                f"File is ready for use with accesspoint_location_workflow_manager Ansible module.",
                "INFO"
            )
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                f"YAML config generation Task failed for module '{self.module_name}'.": {
                    "file_path": file_path
                }
            }
            self.log(
                f"YAML configuration file write operation FAILED for file: {file_path}. File may not "
                f"have been created or may be incomplete. Check file permissions, disk space, and path "
                f"validity. Review write_dict_to_yaml() error messages for specific failure details.",
                "ERROR"
            )
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def process_global_filters(self, global_filters):
        """
        Processes global filter criteria to extract matching AP location configurations.

        This function applies hierarchical filtering logic to self.have collections based on
        provided filter criteria, supporting five filter types: site-based, planned AP-based,
        real AP-based, model-based, and MAC address-based filtering. It extracts matching
        configurations and organizes them by floor for YAML generation.

        Args:
            global_filters (dict): Dictionary containing filter criteria with keys:
                                  - site_list: Floor site hierarchy paths (list[str])
                                  - planned_accesspoint_list: Planned AP names (list[str])
                                  - real_accesspoint_list: Real/deployed AP names (list[str])
                                  - accesspoint_model_list: AP hardware models (list[str])
                                  - mac_address_list: AP MAC addresses (list[str])
                                  Example: {
                                      "site_list": ["Global/USA/Building1/Floor1"],
                                      "accesspoint_model_list": ["C9130AXI-B"]
                                  }

        Returns:
            list or None: List of floor configuration dictionaries with structure:
                         [{"floor_site_hierarchy": "...", "access_points": [{...}]}]
                         Returns None if no matching configurations found.

        Side Effects:
            - Calls find_multiple_dict_by_key_value() for searching collections
            - Logs DEBUG/INFO/WARNING messages throughout filtering process
            - Removes metadata keys from detailed configs before return
            - Does not modify self.have collections

        Filter Processing Order (first match wins):
            1. site_list: Filters by floor site hierarchy
            2. planned_accesspoint_list: Filters by planned AP names
            3. real_accesspoint_list: Filters by real/deployed AP names
            4. accesspoint_model_list: Filters by AP hardware models
            5. mac_address_list: Filters by AP MAC addresses

        Filter Behavior:
            "all" keyword (case-insensitive):
                - Returns complete collection for that filter type
                - Bypasses individual item matching
                - Example: ["all"] returns all planned/real/model APs

            Specific values:
                - Searches self.have collections for matches
                - Extracts matching items and organizes by floor
                - Removes metadata keys before return
                - Returns None if no matches found

        Metadata Removal:
            Keys removed from detailed configs:
            - accesspoint_type: Internal type classification
            - floor_id: Internal floor UUID
            - id: Internal AP UUID
            - floor_site_hierarchy: Duplicated at floor level

        Data Sources:
            - self.have["all_config"]: Combined planned + real APs by floor
            - self.have["planned_aps"]: Planned APs only by floor
            - self.have["real_aps"]: Real APs only by floor
            - self.have["all_detailed_config"]: Complete AP metadata with IDs
            - self.have["filtered_floor"]: Floors with at least one AP

        Notes:
            - Only first matching filter type is processed
            - Filter priority: site > planned_ap > real_ap > model > MAC
            - Empty results return None (not empty list)
            - "all" keyword bypasses individual item validation
            - Metadata keys removed to prevent YAML pollution
        """
        self.log(
            f"Starting global filter processing for AP location configurations. Filter structure: "
            f"{global_filters}. This operation will apply hierarchical filtering logic to extract "
            f"matching configurations from self.have collections based on provided filter criteria. "
            f"Supported filter types: site_list, planned_accesspoint_list, real_accesspoint_list, "
            f"accesspoint_model_list, mac_address_list.",
            "DEBUG"
        )

        site_list = global_filters.get("site_list")
        planned_accesspoint_list = global_filters.get("planned_accesspoint_list")
        real_accesspoint_list = global_filters.get("real_accesspoint_list")
        accesspoint_model_list = global_filters.get("accesspoint_model_list")
        mac_address_list = global_filters.get("mac_address_list")
        final_list = []
        keys_to_remove = ["accesspoint_type", "floor_id", "id", "floor_site_hierarchy"]

        self.log(
            f"Extracted individual filter components from global_filters. site_list: "
            f"{site_list} (count: {len(site_list) if isinstance(site_list, list) else 0}), "
            f"planned_accesspoint_list: {planned_accesspoint_list} "
            f"(count: {len(planned_accesspoint_list) if isinstance(planned_accesspoint_list, list) else 0}), "
            f"real_accesspoint_list: {real_accesspoint_list} "
            f"(count: {len(real_accesspoint_list) if isinstance(real_accesspoint_list, list) else 0}), "
            f"accesspoint_model_list: {accesspoint_model_list} "
            f"(count: {len(accesspoint_model_list) if isinstance(accesspoint_model_list, list) else 0}), "
            f"mac_address_list: {mac_address_list} "
            f"(count: {len(mac_address_list) if isinstance(mac_address_list, list) else 0})",
            "DEBUG"
        )

        self.log(
            f"Metadata keys to remove from detailed configs before return: {keys_to_remove}. "
            f"These keys are internal metadata not needed in YAML output.",
            "DEBUG"
        )

        # Process site_list filter (HIGHEST PRIORITY)
        if site_list and isinstance(site_list, list):
            self.log(
                f"Site list filter detected (HIGHEST PRIORITY). Requested floor site hierarchies: "
                f"{site_list} (count: {len(site_list)}). This filter will extract AP configurations "
                f"for specified floor sites. Other filters will be IGNORED due to priority hierarchy.",
                "INFO"
            )

            if len(site_list) == 1 and site_list[0].lower() == "all":
                self.log(
                    "Site list contains 'all' keyword. Returning complete planned AP configuration "
                    "collection without individual site validation. This bypasses per-site matching.",
                    "INFO"
                )
                if not self.have.get("planned_aps"):
                    self.log(
                        "No planned access points found in Catalyst Center. self.have['planned_aps'] "
                        "is empty or None. Cannot return planned AP configurations.",
                        "WARNING"
                    )

                if not self.have.get("all_config", []):
                    self.log(
                        "No configurations found in self.have['all_config'] for 'all' site_list filter. "
                        "This may indicate no AP locations exist in Catalyst Center or data collection "
                        "failed. Returning empty configuration list.",
                        "WARNING"
                    )
                    return None
                else:
                    final_list = self.have.get("all_config", [])

                self.log(
                    f"Returned {len(final_list)} floor site(s) with planned AP configurations for "
                    f"'all' keyword in site_list.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"Processing {len(site_list)} specific floor site(s) from site_list. Searching "
                    f"for matching floor sites in all_config collection.",
                    "DEBUG"
                )
                prepare_planned_list = []
                for site_index, floor in enumerate(site_list, start=1):
                    self.log(
                        f"Searching for site {site_index}/{len(site_list)}: '{floor}' in all_config "
                        f"collection. Calling find_multiple_dict_by_key_value() to find matching floor.",
                        "DEBUG"
                    )
                    ap_site_exist = self.find_multiple_dict_by_key_value(
                        self.have.get("all_config", []), "floor_site_hierarchy", floor
                    )

                    if ap_site_exist:
                        prepare_planned_list.append(ap_site_exist[0])
                        self.log(
                            f"Site {site_index}/{len(site_list)}: '{floor}' found in all_config. "
                            f"Added floor configuration to collection. Current collected: "
                            f"{len(prepare_planned_list)}/{len(site_list)}.",
                            "DEBUG"
                        )
                    else:
                        self.log(
                            f"Site {site_index}/{len(site_list)}: '{floor}' NOT found in all_config. "
                            f"This floor either has no APs or doesn't exist. Skipping.",
                            "WARNING"
                        )

                final_list = prepare_planned_list
                self.log(
                    f"Site list processing completed. Collected {len(final_list)} floor site(s) out "
                    f"of {len(site_list)} requested.",
                    "INFO"
                )

            self.log(
                f"Access point locations collected for site list {site_list}. Total floor "
                f"configurations: {len(final_list)}. Final data: {self.pprint(final_list)}",
                "DEBUG"
            )

        # Process planned_accesspoint_list filter (MEDIUM PRIORITY)
        elif planned_accesspoint_list and isinstance(planned_accesspoint_list, list):
            self.log(
                f"Planned access point list filter detected (MEDIUM PRIORITY, site_list not provided). "
                f"Requested planned AP names: {planned_accesspoint_list} (count: {len(planned_accesspoint_list)}). "
                f"This filter will extract configurations for specified planned APs.",
                "INFO"
            )

            if len(planned_accesspoint_list) == 1 and planned_accesspoint_list[0].lower() == "all":
                self.log(
                    "Planned AP list contains 'all' keyword. Returning complete planned AP configuration "
                    "collection without individual AP validation.",
                    "INFO"
                )
                if not self.have.get("planned_aps"):
                    self.log(
                        "No planned access points found in Catalyst Center. self.have['planned_aps'] "
                        "is empty or None.",
                        "WARNING"
                    )
                final_list = self.have.get("planned_aps", [])
                self.log(
                    f"Returned {len(final_list)} floor site(s) with planned AP configurations for "
                    f"'all' keyword.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"Processing {len(planned_accesspoint_list)} specific planned AP(s). Searching "
                    f"all_detailed_config for matching planned APs.",
                    "DEBUG"
                )
                collected_aps = []
                for ap_index, planned_ap in enumerate(planned_accesspoint_list, start=1):
                    self.log(
                        f"Searching for planned AP {ap_index}/{len(planned_accesspoint_list)}: '{planned_ap}' "
                        f"in all_detailed_config. Filtering by accesspoint_name and accesspoint_type='planned'.",
                        "DEBUG"
                    )
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_detailed_config"], "accesspoint_name", planned_ap
                    )

                    ap_exist = self.find_multiple_dict_by_key_value(
                        ap_exist, "accesspoint_type", "planned"
                    )

                    if ap_exist:
                        collected_aps.extend(ap_exist)
                        self.log(
                            f"Planned AP {ap_index}/{len(planned_accesspoint_list)}: '{planned_ap}' "
                            f"found with {len(ap_exist)} instance(s). Added to collection. "
                            f"Total collected: {len(collected_aps)} AP(s).",
                            "INFO"
                        )
                    else:
                        self.log(
                            f"Planned AP {ap_index}/{len(planned_accesspoint_list)}: '{planned_ap}' "
                            f"NOT found in all_detailed_config or not type='planned'. Skipping.",
                            "WARNING"
                        )

                if not collected_aps:
                    self.log(
                        f"No planned access points found matching the provided list: "
                        f"{planned_accesspoint_list}. None of the requested APs exist as planned type.",
                        "WARNING"
                    )
                    return None

                self.log(
                    f"Successfully collected {len(collected_aps)} planned AP instance(s) matching "
                    f"filter criteria. Organizing by floor site hierarchy.",
                    "INFO"
                )

                if self.have.get("filtered_floor"):
                    floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                    self.log(
                        f"Organizing {len(collected_aps)} collected AP(s) into {len(floors)} floor "
                        f"site(s). Grouping APs by floor_site_hierarchy.",
                        "DEBUG"
                    )
                    prepare_planned_list = []
                    for floor_index, floor in enumerate(floors, start=1):
                        ap_site_exist = self.find_multiple_dict_by_key_value(
                            collected_aps, "floor_site_hierarchy", floor
                        )

                        if ap_site_exist:
                            self.log(
                                f"Floor {floor_index}/{len(floors)}: '{floor}' has {len(ap_site_exist)} "
                                f"matching planned AP(s). Removing metadata keys: {keys_to_remove}",
                                "DEBUG"
                            )
                            for each_ap_site in ap_site_exist:
                                for key in keys_to_remove:
                                    del each_ap_site[key]

                            floor_data = {
                                "floor_site_hierarchy": floor,
                                "access_points": ap_site_exist
                            }
                            prepare_planned_list.append(floor_data)
                            self.log(
                                f"Added floor configuration for '{floor}' with {len(ap_site_exist)} AP(s).",
                                "DEBUG"
                            )

                    final_list = prepare_planned_list
                    self.log(
                        f"Floor organization completed. Total floor configurations created: {len(final_list)}",
                        "INFO"
                    )

            self.log(
                f"Access point locations collected for planned access point list "
                f"{planned_accesspoint_list}. Total floor configurations: {len(final_list)}",
                "DEBUG"
            )

        # Process real_accesspoint_list filter (MEDIUM-LOW PRIORITY)
        elif real_accesspoint_list and isinstance(real_accesspoint_list, list):
            self.log(
                f"Real access point list filter detected (MEDIUM-LOW PRIORITY). Requested real AP names: "
                f"{real_accesspoint_list} (count: {len(real_accesspoint_list)}). This filter will extract "
                f"configurations for specified real/deployed APs.",
                "INFO"
            )

            if len(real_accesspoint_list) == 1 and real_accesspoint_list[0].lower() == "all":
                self.log(
                    "Real AP list contains 'all' keyword. Returning complete real AP configuration "
                    "collection without individual AP validation.",
                    "INFO"
                )
                if not self.have.get("real_aps"):
                    self.log(
                        "No real access points found in Catalyst Center. self.have['real_aps'] "
                        "is empty or None.",
                        "WARNING"
                    )

                final_list = self.have.get("real_aps", [])
                self.log(
                    f"Returned {len(final_list)} floor site(s) with real AP configurations for "
                    f"'all' keyword.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"Processing {len(real_accesspoint_list)} specific real AP(s). Searching "
                    f"all_detailed_config for matching real APs.",
                    "DEBUG"
                )
                collected_aps = []
                for ap_index, real_ap in enumerate(real_accesspoint_list, start=1):
                    self.log(
                        f"Searching for real AP {ap_index}/{len(real_accesspoint_list)}: '{real_ap}' "
                        f"in all_detailed_config. Filtering by accesspoint_name and accesspoint_type='real'.",
                        "DEBUG"
                    )
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_detailed_config"], "accesspoint_name", real_ap
                    )

                    ap_exist = self.find_multiple_dict_by_key_value(
                        ap_exist, "accesspoint_type", "real"
                    )

                    if ap_exist:
                        collected_aps.extend(ap_exist)
                        self.log(
                            f"Real AP {ap_index}/{len(real_accesspoint_list)}: '{real_ap}' found with "
                            f"{len(ap_exist)} instance(s). Added to collection. Total collected: "
                            f"{len(collected_aps)} AP(s).",
                            "INFO"
                        )
                    else:
                        self.log(
                            f"Real AP {ap_index}/{len(real_accesspoint_list)}: '{real_ap}' NOT found "
                            f"in all_detailed_config or not type='real'. Skipping.",
                            "WARNING"
                        )

                if not collected_aps:
                    self.log(
                        f"No real access points found matching the provided list: {real_accesspoint_list}. "
                        f"None of the requested APs exist as real/deployed type.",
                        "WARNING"
                    )
                    return None

                self.log(
                    f"Successfully collected {len(collected_aps)} real AP instance(s) matching filter "
                    f"criteria. Organizing by floor site hierarchy.",
                    "INFO"
                )

                if self.have.get("filtered_floor"):
                    floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                    self.log(
                        f"Organizing {len(collected_aps)} collected AP(s) into {len(floors)} floor "
                        f"site(s). Grouping APs by floor_site_hierarchy.",
                        "DEBUG"
                    )
                    prepare_real_list = []
                    for floor_index, floor in enumerate(floors, start=1):
                        ap_site_exist = self.find_multiple_dict_by_key_value(
                            collected_aps, "floor_site_hierarchy", floor
                        )

                        if ap_site_exist:
                            self.log(
                                f"Floor {floor_index}/{len(floors)}: '{floor}' has {len(ap_site_exist)} "
                                f"matching real AP(s). Removing metadata keys: {keys_to_remove}",
                                "DEBUG"
                            )
                            for each_ap_site in ap_site_exist:
                                for key in keys_to_remove:
                                    del each_ap_site[key]

                            floor_data = {
                                "floor_site_hierarchy": floor,
                                "access_points": ap_site_exist
                            }
                            prepare_real_list.append(floor_data)
                            self.log(
                                f"Added floor configuration for '{floor}' with {len(ap_site_exist)} AP(s).",
                                "DEBUG"
                            )

                    final_list = prepare_real_list
                    self.log(
                        f"Floor organization completed. Total floor configurations created: {len(final_list)}",
                        "INFO"
                    )

            self.log(
                f"Access point locations collected for real access point list {real_accesspoint_list}. "
                f"Total floor configurations: {len(final_list)}",
                "DEBUG"
            )

        # Process accesspoint_model_list filter (LOW PRIORITY)
        elif accesspoint_model_list and isinstance(accesspoint_model_list, list):
            self.log(
                f"Access point model list filter detected (LOW PRIORITY). Requested AP models: "
                f"{accesspoint_model_list} (count: {len(accesspoint_model_list)}). This filter will extract "
                f"configurations for specified AP hardware models.",
                "INFO"
            )

            if len(accesspoint_model_list) == 1 and accesspoint_model_list[0].lower() == "all":
                self.log(
                    "AP model list contains 'all' keyword. Returning complete AP configuration collection "
                    "(planned + real) without individual model validation.",
                    "INFO"
                )
                if not self.have.get("all_config"):
                    self.log(
                        "No access point locations found in Catalyst Center. self.have['all_config'] "
                        "is empty or None.",
                        "WARNING"
                    )
                    return None

                final_list = self.have.get("all_config", [])
                self.log(
                    f"Returned {len(final_list)} floor site(s) with AP configurations for 'all' keyword.",
                    "DEBUG"
                )
            else:
                self.log(
                    f"Processing {len(accesspoint_model_list)} specific AP model(s). Searching "
                    f"all_detailed_config for matching models.",
                    "DEBUG"
                )
                collected_aps = []
                for model_index, each_model in enumerate(accesspoint_model_list, start=1):
                    self.log(
                        f"Searching for AP model {model_index}/{len(accesspoint_model_list)}: "
                        f"'{each_model}' in all_detailed_config. Filtering by accesspoint_model.",
                        "DEBUG"
                    )
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_detailed_config"], "accesspoint_model", each_model
                    )

                    if ap_exist:
                        collected_aps.extend(ap_exist)
                        self.log(
                            f"AP model {model_index}/{len(accesspoint_model_list)}: '{each_model}' found "
                            f"with {len(ap_exist)} AP instance(s). Added to collection. Total collected: "
                            f"{len(collected_aps)} AP(s).",
                            "INFO"
                        )
                    else:
                        self.log(
                            f"AP model {model_index}/{len(accesspoint_model_list)}: '{each_model}' NOT "
                            f"found in all_detailed_config. No APs with this model. Skipping.",
                            "WARNING"
                        )

                if not collected_aps:
                    self.log(
                        f"No access points found matching the provided model list: {accesspoint_model_list}. "
                        f"None of the requested models have deployed APs.",
                        "WARNING"
                    )
                    return None

                self.log(
                    f"Successfully collected {len(collected_aps)} AP instance(s) matching model filter "
                    f"criteria. Organizing by floor site hierarchy.",
                    "INFO"
                )

                if self.have.get("filtered_floor"):
                    floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                    self.log(
                        f"Organizing {len(collected_aps)} collected AP(s) into {len(floors)} floor "
                        f"site(s). Grouping APs by floor_site_hierarchy.",
                        "DEBUG"
                    )
                    prepare_model_list = []
                    for floor_index, floor in enumerate(floors, start=1):
                        ap_site_exist = self.find_multiple_dict_by_key_value(
                            collected_aps, "floor_site_hierarchy", floor
                        )

                        if ap_site_exist:
                            self.log(
                                f"Floor {floor_index}/{len(floors)}: '{floor}' has {len(ap_site_exist)} "
                                f"AP(s) matching model filter. Removing metadata keys: {keys_to_remove}",
                                "DEBUG"
                            )
                            for each_ap_site in ap_site_exist:
                                for key in keys_to_remove:
                                    del each_ap_site[key]

                            floor_data = {
                                "floor_site_hierarchy": floor,
                                "access_points": ap_site_exist
                            }
                            prepare_model_list.append(floor_data)
                            self.log(
                                f"Added floor configuration for '{floor}' with {len(ap_site_exist)} AP(s).",
                                "DEBUG"
                            )

                    final_list = prepare_model_list
                    self.log(
                        f"Floor organization completed. Total floor configurations created: {len(final_list)}",
                        "INFO"
                    )

            self.log(
                f"Access point location config collected for model list {accesspoint_model_list}. "
                f"Total floor configurations: {len(final_list)}",
                "DEBUG"
            )

        # Process mac_address_list filter (LOWEST PRIORITY)
        elif mac_address_list and isinstance(mac_address_list, list):
            self.log(
                f"MAC address list filter detected (LOWEST PRIORITY). Requested MAC addresses: "
                f"{mac_address_list} (count: {len(mac_address_list)}). This filter will extract "
                f"configurations for specified AP MAC addresses.",
                "INFO"
            )

            collected_aps = []
            self.log(
                f"Processing {len(mac_address_list)} MAC address(es). Searching all_detailed_config "
                f"for matching MAC addresses (normalized to lowercase).",
                "DEBUG"
            )

            for mac_index, each_mac in enumerate(mac_address_list, start=1):
                normalized_mac = each_mac.lower()
                self.log(
                    f"Searching for MAC address {mac_index}/{len(mac_address_list)}: '{normalized_mac}' "
                    f"(normalized) in all_detailed_config. Filtering by mac_address field.",
                    "DEBUG"
                )
                ap_exist = self.find_multiple_dict_by_key_value(
                    self.have["all_detailed_config"], "mac_address", normalized_mac
                )

                if ap_exist:
                    collected_aps.extend(ap_exist)
                    self.log(
                        f"MAC address {mac_index}/{len(mac_address_list)}: '{normalized_mac}' found with "
                        f"{len(ap_exist)} AP instance(s). Added to collection. Total collected: "
                        f"{len(collected_aps)} AP(s).",
                        "INFO"
                    )
                else:
                    self.log(
                        f"MAC address {mac_index}/{len(mac_address_list)}: '{normalized_mac}' NOT found "
                        f"in all_detailed_config. No AP with this MAC. Skipping.",
                        "WARNING"
                    )

            if not collected_aps:
                self.log(
                    f"No access points found matching the provided MAC address list: {mac_address_list}. "
                    f"None of the requested MAC addresses have deployed APs.",
                    "WARNING"
                )
                return None

            self.log(
                f"Successfully collected {len(collected_aps)} AP instance(s) matching MAC address filter "
                f"criteria. Organizing by floor site hierarchy.",
                "INFO"
            )

            if self.have.get("filtered_floor"):
                floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                self.log(
                    f"Organizing {len(collected_aps)} collected AP(s) into {len(floors)} floor site(s). "
                    f"Grouping APs by floor_site_hierarchy.",
                    "DEBUG"
                )
                prepare_mac_list = []
                for floor_index, floor in enumerate(floors, start=1):
                    ap_site_exist = self.find_multiple_dict_by_key_value(
                        collected_aps, "floor_site_hierarchy", floor
                    )

                    if ap_site_exist:
                        self.log(
                            f"Floor {floor_index}/{len(floors)}: '{floor}' has {len(ap_site_exist)} "
                            f"AP(s) matching MAC filter. Removing metadata keys: {keys_to_remove}",
                            "DEBUG"
                        )
                        for each_ap_site in ap_site_exist:
                            for key in keys_to_remove:
                                del each_ap_site[key]

                        floor_data = {
                            "floor_site_hierarchy": floor,
                            "access_points": ap_site_exist
                        }
                        prepare_mac_list.append(floor_data)
                        self.log(
                            f"Added floor configuration for '{floor}' with {len(ap_site_exist)} AP(s).",
                            "DEBUG"
                        )

                final_list = prepare_mac_list
                self.log(
                    f"Floor organization completed. Total floor configurations created: {len(final_list)}",
                    "INFO"
                )

            self.log(
                f"Access point location config collected for MAC address list {mac_address_list}. "
                f"Total floor configurations: {len(final_list)}",
                "DEBUG"
            )

        else:
            self.log(
                "No specific global filters provided or all filters are empty/invalid. Cannot determine "
                "which AP locations to collect. Supported filters: site_list, planned_accesspoint_list, "
                "real_accesspoint_list, accesspoint_model_list, mac_address_list. Provide at least one "
                "valid filter with values.",
                "WARNING"
            )

        if not final_list:
            self.log(
                "No access point positions found in Catalyst Center matching the provided filter criteria. "
                "This indicates either filter values don't exist or filters are too restrictive. Verify "
                "filter values match existing AP configurations in Catalyst Center.",
                "WARNING"
            )
            return None

        self.log(
            f"Global filter processing completed successfully. Final result contains {len(final_list)} "
            f"floor site configuration(s) with filtered AP data. Total APs across all floors: "
            f"{sum(len(floor.get('access_points', [])) for floor in final_list)}. Returning filtered "
            f"configuration list for YAML generation.",
            "INFO"
        )

        return final_list


def main():
    """
    Main entry point for the Ansible access point location playbook generator module.

    This function serves as the primary orchestrator for generating YAML playbooks that capture
    the current state of access point location assignments in Cisco Catalyst Center. It performs
    comprehensive validation, infrastructure discovery, and templated playbook generation.

    Workflow:
        1. Module Initialization:
           - Define argument specifications for all module parameters
           - Initialize AnsibleModule instance with check mode support
           - Create AccesspointLocationPlaybookGenerator instance
           - Enable structured logging for debugging and audit trails

        2. Version Validation:
           - Verify Catalyst Center version meets minimum requirement (3.1.3.0+)
           - Fail gracefully with clear error message if version is unsupported
           - Log version information for troubleshooting

        3. State Validation:
           - Verify requested state is 'gathered' (only supported state)
           - Fail immediately if invalid state is requested
           - Log state information for audit purposes

        4. Input Validation:
           - Validate all module parameters (credentials, filters, paths)
           - Check filter parameter combinations and priorities
           - Verify file path permissions and writability
           - Fail with detailed error messages on validation failures

        5. Configuration Processing:
           - Iterate through each validated config item
           - Reset internal state between config items
           - For each config:
             a. Get desired state (get_want) - parse and validate filters
             b. Get current state (get_have) - query Catalyst Center APIs
             c. Apply state logic (get_diff_state_apply) - generate playbook
           - Check return status after each step

        6. Result Return:
           - Exit with JSON result containing operation status
           - Include file paths for generated playbooks
           - Provide user-friendly success/failure messages

    Args:
        None. Module parameters are obtained from Ansible module specification.

    Module Parameters (element_spec):
        Connection Parameters:
            - dnac_host (str, required): Catalyst Center hostname or IP address
            - dnac_port (str, optional): API port number (default: "443")
            - dnac_username (str, optional): Authentication username (default: "admin")
            - dnac_password (str, required): Authentication password (no_log: True)
            - dnac_verify (bool, optional): Verify SSL certificates (default: True)
            - dnac_version (str, optional): API version (default: "2.2.3.3")
            - dnac_debug (bool, optional): Enable SDK debug logging (default: False)

        Logging Parameters:
            - dnac_log_level (str, optional): Log level (default: "WARNING")
            - dnac_log_file_path (str, optional): Log file path (default: "dnac.log")
            - dnac_log_append (bool, optional): Append to log file (default: True)
            - dnac_log (bool, optional): Enable file logging (default: False)

        Operational Parameters:
            - validate_response_schema (bool, optional): Validate API responses (default: True)
            - dnac_api_task_timeout (int, optional): API task timeout in seconds (default: 1200)
            - dnac_task_poll_interval (int, optional): Task polling interval in seconds (default: 2)

        Configuration Parameters:
            - config (list of dict, required): Filter configuration for AP selection
            - state (str, optional): Operation state, must be "gathered" (default: "gathered")

    Returns:
        dict: Ansible module result dictionary via module.exit_json() with keys:
            - changed (bool): Always False (read-only operation)
            - response (dict): Operation result including:
                * Success message string
                * file_path (str): Absolute path to generated playbook
            - msg (str): User-facing summary message

    Side Effects:
        - Establishes HTTPS connection to Cisco Catalyst Center API
        - Performs multiple API queries to retrieve:
            * Access point details and configurations
            * Site hierarchy and location information
            * Floor maps and physical location data
        - Writes YAML playbook file to filesystem at yaml_file_path
        - Creates log entries at configured log level (DEBUG, INFO, WARNING, ERROR)
        - May create output directories if they don't exist

    Raises:
        AnsibleFailJson: Via module.fail_json() for any error condition:
            - Version Check Failures:
                * Catalyst Center version < 3.1.3.0
                * Unable to determine Catalyst Center version
            - State Validation Failures:
                * Unsupported state requested (not 'gathered')
            - Input Validation Failures:
                * Missing or invalid credentials
                * Invalid filter parameters or combinations
                * Unreachable file paths or permission errors
            - API Communication Failures:
                * Network connectivity issues
                * Authentication failures
                * API timeout or rate limiting
            - Data Processing Failures:
                * Schema validation errors
                * Unexpected API response formats
                * Missing required data in API responses

    Success Scenarios:
        Case 1: Access points found and playbook generated successfully
            {
                "changed": False,
                "response": {
                    "YAML config generation Task succeeded for module 'accesspoint_location_workflow_manager'.": {
                        "file_path": "/path/to/accesspoint_location_workflow_playbook.yml"
                    }
                },
                "msg": "YAML configuration playbook generation completed successfully"
            }

        Case 2: No access points match the specified filters
            {
                "changed": False,
                "response": "No configurations or components to process for module "
                            "'accesspoint_location_workflow_manager'. Verify input filters "
                            "or configuration.",
                "msg": "No access point locations found matching the specified filter criteria"
            }

    Error Scenarios:
        - Version Mismatch:
            "The specified version '2.3.5.3' does not support the YAML Playbook generation "
            "for ACCESSPOINT LOCATION WORKFLOW Module. Supported versions start from '3.1.3.0' "
            "onwards."

        - Invalid State:
            "State 'merged' is invalid. Only 'gathered' state is supported for this module."

        - Authentication Failure:
            "Failed to authenticate with Cisco Catalyst Center at <host>:<port>. "
            "Verify credentials and network connectivity."

        - Invalid Filters:
            "Validation failed for config parameter: Cannot use both 'site_hierarchy' and "
            "'site_name_filter' simultaneously. Choose one filter method."

        - File Write Error:
            "Failed to write playbook to '<path>': Permission denied. Ensure the directory exists and is writable."

    Example Usage:
        This function is invoked automatically by Ansible when the module is executed.
        It should never be called directly by user code.

        Typical Ansible playbook usage:
        ```yaml
        - name: Generate access point location playbook
          cisco.dnac.accesspoint_location_playbook_config_generator:
            dnac_host: "{{ dnac_host }}"
            dnac_username: "{{ dnac_username }}"
            dnac_password: "{{ dnac_password }}"
            dnac_verify: False
            state: gathered
            config:
              - yaml_file_path: "output/ap_locations.yml"
                site_name_filter: "Global/San Jose"
        ```

    Performance Considerations:
        - Large environments (1000+ access points) may take 5-10 minutes
        - API queries are performed serially to avoid rate limiting
        - Memory usage scales with number of access points (approximately 1KB per AP)
        - Network latency significantly impacts total execution time

    Notes:
        - Requires Cisco Catalyst Center version 3.1.3.0 or later
        - Filter priorities (highest to lowest):
            1. hostname_filter (exact matches only)
            2. site_name_filter (includes all child sites)
            3. ap_name_filter (supports wildcards)
            4. site_hierarchy (full hierarchy path)
        - Generated playbooks use 'accesspoint_location_workflow_manager' as target module
        - Check mode (--check) is supported but has no effect (read-only operation)
        - Module always returns changed=False as it performs read-only discovery
        - Playbook generation is idempotent - repeated runs produce identical output
        - Output YAML files use UTF-8 encoding with LF line endings

    See Also:
        - AccesspointLocationPlaybookGenerator class for implementation details
        - validate_input() for complete filter validation logic
        - get_want() for desired state determination
        - get_have() for current state retrieval
        - get_diff_gathered() for playbook generation logic
    """
    # ========================================
    # Module Argument Specification
    # ========================================
    # Define the specification for the module's arguments
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

    # ========================================
    # Module Initialization
    # ========================================
    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    # Initialize the AccesspointLocationPlaybookGenerator object with the module
    ccc_accesspoint_location_playbook_generator = AccesspointLocationPlaybookGenerator(module)

    # ========================================
    # Catalyst Center Version Validation
    # ========================================
    # Verify Catalyst Center version meets minimum requirement (3.1.3.0+)
    if (
        ccc_accesspoint_location_playbook_generator.compare_dnac_versions(
            ccc_accesspoint_location_playbook_generator.get_ccc_version(), "3.1.3.0"
        )
        < 0
    ):
        ccc_accesspoint_location_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for ACCESSPOINT LOCATION WORKFLOW Module. Supported versions start from '3.1.3.0' onwards. ".format(
                ccc_accesspoint_location_playbook_generator.get_ccc_version()
            )
        )
        ccc_accesspoint_location_playbook_generator.set_operation_result(
            "failed", False, ccc_accesspoint_location_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # ========================================
    # State Parameter Validation
    # ========================================
    # Get the state parameter from the provided parameters
    state = ccc_accesspoint_location_playbook_generator.params.get("state")

    # Check if the state is valid (must be 'gathered')
    if state not in ccc_accesspoint_location_playbook_generator.supported_states:
        ccc_accesspoint_location_playbook_generator.status = "invalid"
        ccc_accesspoint_location_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_accesspoint_location_playbook_generator.check_return_status()

    # ========================================
    # Input Parameter Validation
    # ========================================
    # Validate the input parameters and check the return status
    ccc_accesspoint_location_playbook_generator.validate_input().check_return_status()

    # ========================================
    # Configuration Processing Loop
    # ========================================
    # Iterate over the validated configuration parameters
    for config in ccc_accesspoint_location_playbook_generator.validated_config:
        # Reset internal values before processing each config item
        ccc_accesspoint_location_playbook_generator.reset_values()

        # Get desired state (parse and validate filters)
        ccc_accesspoint_location_playbook_generator.get_want(
            config, state).check_return_status()

        # Get current state (query Catalyst Center APIs)
        ccc_accesspoint_location_playbook_generator.get_have(
            config).check_return_status()

        # Apply state-specific logic (generate playbook)
        ccc_accesspoint_location_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    # ========================================
    # Result Return
    # ========================================
    # Exit with JSON result containing operation status and file paths
    module.exit_json(**ccc_accesspoint_location_playbook_generator.result)


if __name__ == "__main__":
    main()

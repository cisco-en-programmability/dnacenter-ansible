#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbooks for Assurance Issue Operations in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Megha Kandari, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_assurance_issue_playbook_generator
short_description: Generate YAML playbook for 'assurance_issue_workflow_manager' module.
description:
- Generates YAML configurations compatible with the `assurance_issue_workflow_manager`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the user-defined issue definitions
  configured on the Cisco Catalyst Center.
- Supports extraction of User-Defined Issue Definitions configurations.
version_added: 6.45.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Megha Kandari (@kandarimegha)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `assurance_issue_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - Global filters identify target settings by issue name or device type.
    - Component-specific filters allow selection of specific assurance issue features and detailed filtering.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - When set to True, automatically generates YAML configurations for all assurance issue components.
        - This mode discovers all configured assurance issues in Cisco Catalyst Center and extracts all supported configurations.
        - When enabled, the config parameter becomes optional and will use default values if not provided.
        - A default filename will be generated automatically if file_path is not specified.
        - This is useful for complete brownfield assurance issue discovery and documentation.
        - Includes User-Defined Issue Definitions only.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Absolute or relative path for the output YAML configuration file.
        - If not specified, a timestamped filename is auto-generated in the format C(brownfield_assurance_issue_YYYYMMDD_HHMMSS.yml).
        - Parent directories are created automatically if they do not exist.
        type: str
        required: false
      component_specific_filters:
        description:
        - Filters to specify which assurance issue components and features to include in the YAML configuration file.
        - Allows granular selection of specific components and their parameters.
        - If not specified, all supported assurance issue components will be extracted.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are ["assurance_user_defined_issue_settings"]
            - If not specified, all supported components are included.
            - Example ["assurance_user_defined_issue_settings"]
            type: list
            elements: str
            required: false
            choices: ["assurance_user_defined_issue_settings",]
          assurance_user_defined_issue_settings:
            description:
            - User-defined issue settings to filter by issue name or enabled status.
            type: list
            elements: dict
            required: false
            suboptions:
              name:
                description:
                - User-defined issue name to filter by name.
                type: str
                required: false
              is_enabled:
                description:
                - Filter by enabled status (true/false).
                type: bool
                required: false

requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - issues.AssuranceSettings.get_all_the_custom_issue_definitions_based_on_the_given_filters

- Paths used are
    - GET /dna/intent/api/v1/customIssueDefinitions

"""

EXAMPLES = r"""
# Example 3: Generate YAML Configuration with default file path for all user-defined issues
- name: Generate YAML Configuration for user-defined issues
  cisco.dnac.brownfield_assurance_issue_playbook_generator:
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
      - component_specific_filters:
          components_list: ["assurance_user_defined_issue_settings"]

# Example 2: Generate YAML Configuration for all user-defined issue components
- name: Generate complete user-defined issue configuration
  cisco.dnac.brownfield_assurance_issue_playbook_generator:
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
      - file_path: "/tmp/complete_assurance_config.yml"
        generate_all_configurations: true

# Example 3: Filter by specific issue name
- name: Generate YAML for specific issue by name
  cisco.dnac.brownfield_assurance_issue_playbook_generator:
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
      - file_path: "/tmp/high_cpu_issue.yml"
        component_specific_filters:
          assurance_user_defined_issue_settings:
            - name: "High CPU Usage"

# Example 4: Filter by enabled status
- name: Generate YAML for only enabled issues
  cisco.dnac.brownfield_assurance_issue_playbook_generator:
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
      - file_path: "/tmp/enabled_issues.yml"
        component_specific_filters:
          assurance_user_defined_issue_settings:
            - is_enabled: true

# Example 5: Filter by name and enabled status
- name: Generate YAML for specific enabled issue
  cisco.dnac.brownfield_assurance_issue_playbook_generator:
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
      - file_path: "/tmp/specific_enabled_issue.yml"
        component_specific_filters:
          assurance_user_defined_issue_settings:
            - name: "Memory Leak Detection"
              is_enabled: true
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "message": "YAML config generation succeeded for module 'assurance_issue_workflow_manager'.",
          "file_path": "/tmp/assurance_issue_config.yml",
          "configurations_generated": 15,
          "operation_summary": {
            "total_components_processed": 25,
            "total_successful_operations": 22,
            "total_failed_operations": 3,
            "components_with_complete_success": ["assurance_user_defined_issue_settings"],
            "components_with_partial_success": [],
            "components_with_complete_failure": [],
            "success_details": [
              {
                "component": "assurance_user_defined_issue_settings",
                "status": "success",
                "issues_processed": 15
              }
            ],
            "failure_details": []
          }
        },
      "msg": "YAML config generation succeeded for module 'assurance_issue_workflow_manager'."
    }

# Case_2: No Configurations Found Scenario
response_2:
  description: A dictionary with the response when no configurations are found
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "message": "No configurations or components to process for module 'assurance_issue_workflow_manager'. Verify input filters or configuration.",
          "operation_summary": {
            "total_components_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "components_with_complete_success": [],
            "components_with_partial_success": [],
            "components_with_complete_failure": [],
            "success_details": [],
            "failure_details": []
          }
        },
      "msg": "No configurations or components to process for module 'assurance_issue_workflow_manager'. Verify input filters or configuration."
    }

# Case_3: Error Scenario
response_3:
  description: A dictionary with error details when YAML generation fails
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "message": "YAML config generation failed for module 'assurance_issue_workflow_manager'.",
          "file_path": "/tmp/assurance_issue_config.yml",
          "operation_summary": {
            "total_components_processed": 2,
            "total_successful_operations": 1,
            "total_failed_operations": 1,
            "components_with_complete_success": ["assurance_user_defined_issue_settings"],
            "components_with_partial_success": [],
            "components_with_complete_failure": [],
            "success_details": [
              {
                "component": "assurance_user_defined_issue_settings",
                "status": "success",
                "issues_processed": 10
              }
            ],
            "failure_details": []
          }
        },
      "msg": "YAML config generation failed for module 'assurance_issue_workflow_manager'."
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
import os
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
from collections import OrderedDict


class AssuranceIssuePlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for assurance issues deployed within the Cisco Catalyst Center using the GET APIs.
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            The method does not return a value.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "assurance_issue_workflow_manager"

        # Initialize class-level variables to track successes and failures
        self.operation_successes = []
        self.operation_failures = []
        self.total_components_processed = 0

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False

        # Add state mapping
        self.get_diff_state_apply = {
            "gathered": self.get_diff_gathered,
        }

    def validate_input(self):
        """
        Validates the input configuration parameters for the brownfield assurance issue playbook.

        This method performs comprehensive validation of all module configuration parameters
        including global filters, component-specific filters, file paths, and authentication
        credentials to ensure they meet the required format and constraints before processing.

        Returns:
            object: An instance of the class with updated attributes:
                self.msg (str): A message describing the validation result.
                self.status (str): The status of the validation ("success" or "failed").
                self.validated_config (dict): If successful, a validated version of the config.
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
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        allowed_keys = set(temp_spec.keys())

        # Validate that only allowed keys are present in the configuration
        for config_item in self.config:
            if not isinstance(config_item, dict):
                self.msg = "Configuration item must be a dictionary, got: {0}".format(type(config_item).__name__)
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
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.validate_minimum_requirements(self.config)

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def validate_params(self, config):
        """
        Validates individual configuration parameters for brownfield assurance issue generation.

        Args:
            config (dict): Configuration parameters

        Returns:
            self: Current instance with validation status updated.
        """
        self.log("Starting validation of configuration parameters", "DEBUG")

        # Check for required parameters
        if not config:
            self.msg = "Configuration cannot be empty"
            self.status = "failed"
            return self

        # Validate file_path if provided
        file_path = config.get("file_path")
        if file_path:
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                try:
                    os.makedirs(directory, exist_ok=True)
                    self.log("Created directory: {0}".format(directory), "INFO")
                except Exception as e:
                    self.msg = "Cannot create directory for file_path: {0}. Error: {1}".format(directory, str(e))
                    self.status = "failed"
                    return self

        # Validate component_specific_filters with safe access
        component_filters = config.get("component_specific_filters", {}) or {}
        if component_filters:
            components_list = component_filters.get("components_list", [])
            # Ensure module_schema is available
            if not hasattr(self, 'module_schema') or not self.module_schema:
                self.module_schema = self.get_workflow_elements_schema()
            supported_components = list(self.module_schema.get("issue_elements", {}).keys())

            for component in components_list:
                if component not in supported_components:
                    self.msg = "Unsupported component: {0}. Supported components: {1}".format(
                        component, supported_components)
                    self.status = "failed"
                    return self

        self.log("Configuration parameters validation completed successfully", "DEBUG")
        self.status = "success"
        return self

    def get_workflow_elements_schema(self):
        """
        Returns the mapping configuration for assurance issue workflow manager.
        Returns:
            dict: A dictionary containing issue elements and global filters configuration with validation rules.
        """
        return {
            "issue_elements": {
                "assurance_user_defined_issue_settings": {
                    "filters": {
                        "name": {
                            "type": "str",
                            "required": False
                        },
                        "is_enabled": {
                            "type": "bool",
                            "required": False
                        }
                    },
                    "reverse_mapping_function": self.user_defined_issue_reverse_mapping_function,
                    "api_function": "get_all_the_custom_issue_definitions_based_on_the_given_filters",
                    "api_family": "issues",
                    "get_function_name": self.get_user_defined_issues,
                },

            },
            "global_filters": {
                "issue_name_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "device_type_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            },
        }

    def convert_ordereddict(self, data, _depth=0, _seen=None):
        """
        Recursively converts OrderedDict and nested dict/list structures to regular dict.

        Processes nested data structures containing OrderedDict objects and converts
        them to regular Python dictionaries for cleaner YAML serialization output.
        Handles lists, tuples, sets, and scalar values appropriately.

        Args:
            data: Data structure to convert. Can be OrderedDict, dict, list, tuple,
                set, or scalar values (str, int, float, bool, None).
            _depth (int, internal): Current recursion depth (for recursion tracking).
            _seen (set, internal): Set of processed object IDs (for circular reference detection).

        Returns:
            Converted data structure with all OrderedDict instances replaced by regular dict.
            - dict/OrderedDict → dict
            - list → list (with converted elements)
            - tuple → tuple (with converted elements)
            - set → set (with converted elements)
            - scalar values → returned as-is

        Notes:
            - Recursively processes nested structures
            - Detects and handles circular references (returns None for circular refs)
            - Warns if recursion depth exceeds 100 levels
            - Since Python 3.7+, regular dicts preserve insertion order, making
            OrderedDict conversion primarily for YAML serialization compatibility
        """
        self.log(
            "Converting data structure to regular dict for YAML output, "
            "type: {0}, depth: {1}".format(type(data).__name__, _depth),
            "DEBUG"
        )

        # Initialize circular reference tracking
        if _seen is None:
            _seen = set()

        # Check recursion depth
        if _depth > 100:
            self.log(
                "Deep recursion detected (depth={0}) during OrderedDict conversion".format(_depth),
                "WARNING"
            )

        # Handle dict and OrderedDict (OrderedDict is subclass of dict)
        if isinstance(data, dict):
            # Check for circular reference
            obj_id = id(data)
            if obj_id in _seen:
                self.log(
                    "Circular reference detected in dict/OrderedDict at depth {0}".format(_depth),
                    "WARNING"
                )
                return None

            _seen.add(obj_id)
            result = {
                key: self.convert_ordereddict(value, _depth + 1, _seen)
                for key, value in data.items()
            }
            _seen.discard(obj_id)

            self.log(
                "Converted dict/OrderedDict with {0} key(s) at depth {1}".format(len(result), _depth),
                "DEBUG"
            )
            return result

        # Handle lists
        elif isinstance(data, list):
            obj_id = id(data)
            if obj_id in _seen:
                self.log(
                    "Circular reference detected in list at depth {0}".format(_depth),
                    "WARNING"
                )
                return None

            _seen.add(obj_id)
            result = [
                self.convert_ordereddict(item, _depth + 1, _seen)
                for item in data
            ]
            _seen.discard(obj_id)

            self.log(
                "Converted list with {0} element(s) at depth {1}".format(len(result), _depth),
                "DEBUG"
            )
            return result

        # Handle tuples (preserve immutability)
        elif isinstance(data, tuple):
            result = tuple(
                self.convert_ordereddict(item, _depth + 1, _seen)
                for item in data
            )
            self.log(
                "Converted tuple with {0} element(s) at depth {1}".format(len(result), _depth),
                "DEBUG"
            )
            return result

        # Handle sets
        elif isinstance(data, set):
            result = {
                self.convert_ordereddict(item, _depth + 1, _seen)
                for item in data
            }
            self.log(
                "Converted set with {0} element(s) at depth {1}".format(len(result), _depth),
                "DEBUG"
            )
            return result

        # Handle scalar values (str, int, float, bool, None, etc.)
        else:
            self.log(
                "Returning scalar value of type {0} at depth {1}".format(type(data).__name__, _depth),
                "DEBUG"
            )
            return data

    def generate_yaml_header_comments(self, file_path, operation_summary):
        """
        Generate header comments with Catalyst Center source information and summary statistics.
        Args:
            file_path (str): Path where the YAML file will be saved
            operation_summary (dict): Summary of operations performed containing:
                - total_components_processed (int)
                - total_successful_operations (int)
                - total_failed_operations (int)
                - components_with_complete_success (list)
                - components_with_partial_success (list)
                - components_with_complete_failure (list)
        Returns:
            str: Formatted header comments
        """
        self.log(
            "Generating YAML header comments for file_path: {0}".format(file_path),
            "DEBUG"
        )

        if not operation_summary or not isinstance(operation_summary, dict):
            self.log(
                "Operation summary is None or invalid, using default empty values",
                "WARNING"
            )
            operation_summary = {
                'total_components_processed': 0,
                'total_successful_operations': 0,
                'total_failed_operations': 0,
                'components_with_complete_success': [],
                'components_with_partial_success': [],
                'components_with_complete_failure': []
            }
        try:
            from datetime import datetime

            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Get Catalyst Center connection details (safely)
            dnac_host = getattr(self, 'dnac_host', 'Unknown')
            dnac_version = getattr(self, 'dnac_version', 'Unknown')
            module_name = getattr(self, 'module_name', 'assurance_issue_workflow_manager')

            self.log(
                "Retrieved connection details - host: {0}, version: {1}, module: {2}".format(
                    dnac_host, dnac_version, module_name
                ),
                "DEBUG"
            )

            # Cache operation summary values to avoid repeated .get() calls
            total_processed = operation_summary.get('total_components_processed', 0)
            total_success = operation_summary.get('total_successful_operations', 0)
            total_failed = operation_summary.get('total_failed_operations', 0)
            complete_success = operation_summary.get('components_with_complete_success', [])
            partial_success = operation_summary.get('components_with_partial_success', [])
            complete_failure = operation_summary.get('components_with_complete_failure', [])

            # Format component lists (show "None" if empty)
            complete_success_str = ', '.join(complete_success) if complete_success else 'None'
            partial_success_str = ', '.join(partial_success) if partial_success else 'None'
            complete_failure_str = ', '.join(complete_failure) if complete_failure else 'None'

            # Define header separator width
            SEPARATOR_WIDTH = 80

            # Build header comments
            header_lines = [
                "# " + "=" * SEPARATOR_WIDTH,
                "# Cisco Catalyst Center - Assurance Issue Configuration Export",
                "# " + "=" * SEPARATOR_WIDTH,
                "#",
                "# Generated by: Brownfield Assurance Issue Playbook Generator",
                "# Generation Date: {0}".format(timestamp),
                "# Source Catalyst Center: {0}".format(dnac_host),
                "# Catalyst Center Version: {0}".format(dnac_version),
                "# Target Module: {0}".format(module_name),
                "#",
                "# Summary Statistics:",
                "#   - Total Components Processed: {0}".format(total_processed),
                "#   - Successful Operations: {0}".format(total_success),
                "#   - Failed Operations: {0}".format(total_failed),
                "#   - Output File: {0}".format(file_path),
                "#",
                "# Components with Complete Success: {0}".format(complete_success_str),
                "# Components with Partial Success: {0}".format(partial_success_str),
                "# Components with Complete Failure: {0}".format(complete_failure_str),
                "#",
                "# Note: This configuration represents user-defined issue settings",
                "#       exported from Cisco Catalyst Center.",
                "#       Review and modify as needed before applying.",
                "# " + "=" * SEPARATOR_WIDTH,
                ""
            ]

            header_content = "\n".join(header_lines)
            self.log(
                "Successfully generated YAML header with {0} lines".format(len(header_lines)),
                "DEBUG"
            )

            return header_content

        except (AttributeError, KeyError, TypeError, ImportError) as e:
            self.log(
                "Error generating detailed header comments: {0}. Using minimal fallback.".format(
                    str(e)
                ),
                "WARNING"
            )
            fallback_header = (
                "# Generated by Brownfield Assurance Issue Playbook Generator\n"
            )
            self.log("Returning fallback header due to exception", "DEBUG")
            return fallback_header

    def write_yaml_with_comments(self, data, file_path, operation_summary):
        """
        Write YAML data to file with header comments and clean formatting.
        Args:
            data: Data to write to YAML file
            file_path (str): Path where the YAML file will be saved
            operation_summary (dict): Summary of operations for header
        Returns:
            bool: True if successful, False otherwise
        """
        self.log(
            "Writing YAML configuration to file: {0}".format(file_path),
            "DEBUG"
        )

        # Validate and normalize file path (prevent path traversal)
        file_path = os.path.abspath(file_path)
        if ".." in file_path:
            self.log(
                "Invalid file_path: path traversal detected in {0}".format(
                    file_path
                ),
                "ERROR"
            )
            return False

        # Warn if file already exists
        if os.path.exists(file_path):
            self.log(
                "File {0} already exists and will be overwritten".format(
                    file_path
                ),
                "WARNING"
            )

        # Log data size
        data_size_info = "{0} top-level keys".format(
            len(data.keys())
        ) if isinstance(data, dict) else "unknown structure"
        self.log(
            "Processing YAML data with {0}".format(data_size_info),
            "DEBUG"
        )

        # Convert OrderedDict to regular dict for clean output
        self.log(
            "Converting OrderedDict structures to regular dict for clean YAML",
            "DEBUG"
        )

        try:
            # Convert OrderedDict to regular dict for clean output
            clean_data = self.convert_ordereddict(data)
            self.log(
                "Generating YAML header comments with operation summary",
                "DEBUG"
            )

            # Generate header comments
            header_comments = self.generate_yaml_header_comments(file_path, operation_summary)
            self.log("Serializing configuration data to YAML format", "DEBUG")

            # Generate YAML content
            if HAS_YAML:
                yaml_content = yaml.dump(
                    clean_data,
                    default_flow_style=False,
                    indent=2,
                    width=120,
                    allow_unicode=True,
                    sort_keys=False,
                    explicit_start=True  # Add '---' at start
                )
            else:
                # Fallback to basic string representation
                yaml_content = str(clean_data)

            # Combine header and content
            full_content = header_comments + yaml_content

            # Check and warn about large file size
            content_size_mb = len(full_content) / (1024 * 1024)
            if content_size_mb > 10:
                self.log(
                    "Generated YAML file is large ({0:.2f} MB). "
                    "Writing may take time.".format(content_size_mb),
                    "WARNING"
                )

            # Write to file with UTF-8 encoding
            self.log(
                "Writing {0} bytes to file: {1}".format(
                    len(full_content),
                    file_path
                ),
                "DEBUG"
            )

            # Write to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(full_content)

            self.log("Successfully wrote YAML with header comments to: {}".format(file_path), "INFO")
            return True

        except (IOError, OSError, PermissionError) as e:
            self.log(
                "Failed to write YAML file to {0}: {1}".format(
                    file_path, str(e)
                ),
                "ERROR"
            )
            return False

        except yaml.YAMLError as e:
            self.log(
                "Failed to serialize data to YAML format: {0}".format(str(e)),
                "ERROR"
            )
            return False

        except Exception as e:
            self.log(
                "Unexpected error writing YAML to {0}: {1}".format(
                    file_path, str(e)
                ),
                "ERROR"
            )
            return False

    def user_defined_issue_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for user-defined issue configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for user-defined issue details
        """
        self.log("Generating reverse mapping specification for user-defined issues.", "DEBUG")

        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "is_enabled": {"type": "bool", "source_key": "isEnabled"},
            "priority": {"type": "str", "source_key": "priority"},
            "is_notification_enabled": {"type": "bool", "source_key": "isNotificationEnabled"},
            "rules": {
                "type": "list",
                "source_key": "rules",
                "options": OrderedDict({
                    "severity": {"type": "int", "source_key": "severity"},
                    "facility": {"type": "str", "source_key": "facility"},
                    "mnemonic": {"type": "str", "source_key": "mnemonic"},
                    "pattern": {"type": "str", "source_key": "pattern"},
                    "occurrences": {"type": "int", "source_key": "occurrences"},
                    "duration_in_minutes": {"type": "int", "source_key": "durationInMinutes"},
                })
            },
        })

    def reset_operation_tracking(self):
        """
        Reset operation tracking variables for a new brownfield configuration generation operation.
        """
        self.log("Resetting operation tracking variables for new operation", "DEBUG")
        self.operation_successes = []
        self.operation_failures = []
        self.total_components_processed = 0
        self.log("Operation tracking variables reset successfully", "DEBUG")

    def add_success(self, component, additional_info=None):
        """
        Record a successful operation for component processing in operation tracking.

        Args:
            component (str): Issue component that was successfully processed.
            additional_info (dict, optional): Extra information about the successful operation.
        """
        self.log("Creating success entry for component {0}".format(component), "DEBUG")
        success_entry = {
            "component": component,
            "status": "success"
        }

        if additional_info:
            self.log("Adding additional information to success entry: {0}".format(additional_info), "DEBUG")
            success_entry.update(additional_info)

        self.operation_successes.append(success_entry)
        self.log("Successfully added success entry for component {0}. Total successes: {1}".format(
            component, len(self.operation_successes)), "DEBUG")

    def add_failure(self, component, error_info):
        """
        Record a failed operation for component processing in operation tracking.

        Args:
            component (str): Issue component that failed processing.
            error_info (dict): Detailed error information.
        """
        self.log("Creating failure entry for component {0}".format(component), "DEBUG")
        failure_entry = {
            "component": component,
            "status": "failed",
            "error_info": error_info
        }

        self.operation_failures.append(failure_entry)
        self.log("Successfully added failure entry for component {0}: {1}. Total failures: {2}".format(
            component, error_info.get("error_message", "Unknown error"), len(self.operation_failures)), "ERROR")

    def get_operation_summary(self):
        """
        Returns a summary of all operations performed.
        Returns:
            dict: Summary containing successes, failures, and statistics.
        """
        self.log("Generating operation summary from {0} successes and {1} failures".format(
            len(self.operation_successes), len(self.operation_failures)), "DEBUG")

        unique_successful_components = set()
        unique_failed_components = set()

        self.log("Processing successful operations to extract unique component information", "DEBUG")
        for success in self.operation_successes:
            unique_successful_components.add(success.get("component", "unknown"))

        self.log("Processing failed operations to extract unique component information", "DEBUG")
        for failure in self.operation_failures:
            unique_failed_components.add(failure.get("component", "unknown"))

        self.log("Calculating component categorization based on success and failure patterns", "DEBUG")
        partial_success_components = unique_successful_components.intersection(unique_failed_components)
        self.log("Components with partial success (both successes and failures): {0}".format(
            len(partial_success_components)), "DEBUG")

        complete_success_components = unique_successful_components - unique_failed_components
        self.log("Components with complete success (only successes): {0}".format(
            len(complete_success_components)), "DEBUG")

        complete_failure_components = unique_failed_components - unique_successful_components
        self.log("Components with complete failure (only failures): {0}".format(
            len(complete_failure_components)), "DEBUG")

        summary = {
            "total_components_processed": self.total_components_processed,
            "total_successful_operations": len(self.operation_successes),
            "total_failed_operations": len(self.operation_failures),
            "components_with_complete_success": list(complete_success_components),
            "components_with_partial_success": list(partial_success_components),
            "components_with_complete_failure": list(complete_failure_components),
            "success_details": self.operation_successes,
            "failure_details": self.operation_failures
        }

        self.log("Operation summary generated successfully with {0} total components processed".format(
            summary["total_components_processed"]), "INFO")

        return summary

    def get_user_defined_issues(self, issue_element, filters):
        """
        Fetches custom issue definitions by calling the Catalyst Center API with various
        filter combinations. When no specific filters are provided, retrieves all issues
        across all priority levels (P1-P4) and enabled statuses (true/false), resulting
        in 8 API calls.
        Args:
            issue_element (dict): API configuration containing:
                - api_family (str): API family name (e.g., "issues")
                - api_function (str): API function name
                - reverse_mapping_function (callable): Function to transform response
            filters (dict): Filter structure containing:
                - component_specific_filters (dict, optional): Component-specific filters
                with assurance_user_defined_issue_settings list containing:
                    - name (str, optional): Issue name to filter
                    - is_enabled (bool, optional): Enabled status filter
        Returns:
            dict: Dictionary containing:
                - assurance_user_defined_issue_settings (list): List of transformed issue dicts
                - operation_summary (dict): Operation tracking summary with success/failure details
        """
        self.log("Starting to retrieve user-defined issues with filters: {0}".format(filters), "DEBUG")

        # Safety check for filters
        if not filters:
            self.log(
                "No filters provided, using empty filter dictionary and fetching all issues",
                "DEBUG"
            )
            filters = {}

        final_user_issues = []
        api_family = issue_element.get("api_family")
        api_function = issue_element.get("api_function")

        self.log("Getting user-defined issues using family '{0}' and function '{1}'.".format(
            api_family, api_function), "INFO")

        params = {}
        component_specific_filters = filters.get("component_specific_filters", {})
        if component_specific_filters:
            component_specific_filters = component_specific_filters.get("assurance_user_defined_issue_settings", [])
        else:
            component_specific_filters = []

        self.log(
            "Component-specific filters count: {0}".format(len(component_specific_filters)),
            "DEBUG"
        )

        try:
            if component_specific_filters:
                self.log(
                    "Processing {0} component-specific filter(s)".format(
                        len(component_specific_filters)
                    ),
                    "INFO"
                )
                for filter_index, filter_param in enumerate(component_specific_filters, start=1):
                    self.log(
                        "Processing filter {0}/{1}: {2}".format(
                            filter_index, len(component_specific_filters), filter_param
                        ),
                        "DEBUG"
                    )
                    base_params = {}
                    for key, value in filter_param.items():
                        if key == "name":
                            base_params["name"] = value
                        elif key == "is_enabled":
                            base_params["isEnabled"] = str(value).lower()

                    # If specific filters are provided, use them directly
                    if base_params:
                        self.log(
                            "Retrieving issues with specific filters: {0}".format(base_params),
                            "INFO"
                        )
                        user_issue_details = self.execute_get_with_pagination(api_family, api_function, base_params)
                        self.log("Retrieved user-defined issue details with filters {0}: {1}".format(base_params, len(user_issue_details)), "INFO")
                        final_user_issues.extend(user_issue_details)
                    else:
                        self.log(
                            "No valid filters in filter_param, fetching all priority/enabled combinations",
                            "WARNING"
                        )
                        final_user_issues.extend(
                            self._fetch_all_priority_enabled_combinations(api_family, api_function)
                        )
            else:
                # No component-specific filters, fetch all combinations
                self.log(
                    "No component-specific filters provided, fetching all priority/enabled combinations",
                    "INFO"
                )
                final_user_issues.extend(
                    self._fetch_all_priority_enabled_combinations(api_family, api_function)
                )

            # Track success
            self.add_success("assurance_user_defined_issue_settings", {
                "issues_processed": len(final_user_issues)
            })

            # Apply reverse mapping
            reverse_mapping_function = issue_element.get("reverse_mapping_function")
            reverse_mapping_spec = reverse_mapping_function()

            # Transform using inherited modify_parameters function
            issue_details = self.modify_parameters(reverse_mapping_spec, final_user_issues)
            self.log(
                "Transformed {0} issue(s) using reverse mapping".format(len(issue_details)),
                "DEBUG"
            )

            # Post-process to ensure severity values are integers, not strings
            if issue_details and isinstance(issue_details, list):
                for issue in issue_details:
                    if isinstance(issue, dict) and "rules" in issue and isinstance(issue["rules"], list):
                        for rule in issue["rules"]:
                            if isinstance(rule, dict) and "severity" in rule:
                                # Ensure severity is an integer
                                try:
                                    rule["severity"] = int(rule["severity"])
                                except (ValueError, TypeError):
                                    self.log("Warning: Could not convert severity to int: {0}".format(rule["severity"]), "WARNING")

            return {
                "assurance_user_defined_issue_settings": issue_details,
                "operation_summary": self.get_operation_summary()
            }

        except Exception as e:
            self.log("Error retrieving user-defined issues: {0}".format(str(e)), "ERROR")
            self.add_failure("assurance_user_defined_issue_settings", {
                "error_type": "api_error",
                "error_message": str(e)
            })
            return {
                "assurance_user_defined_issue_settings": [],
                "operation_summary": self.get_operation_summary()
            }

    def _fetch_all_priority_enabled_combinations(self, api_family, api_function):
        """
        Fetches user-defined issues for all priority and enabled status combinations.

        Helper method to retrieve issues across all priority levels (P1-P4) and
        enabled statuses (true/false), making 8 API calls total.

        Args:
            api_family (str): API family name for the API call
            api_function (str): API function name for the API call

        Returns:
            list: Combined list of all user-defined issues from all API calls
        """
        priorities = ["P1", "P2", "P3", "P4"]
        enabled_statuses = ["true", "false"]
        all_issues = []

        total_calls = len(priorities) * len(enabled_statuses)
        self.log(
            "Fetching issues for all priority/enabled combinations ({0} API calls)".format(
                total_calls
            ),
            "INFO"
        )

        call_count = 0
        for priority in priorities:
            for enabled_status in enabled_statuses:
                call_count += 1
                params = {
                    "priority": priority,
                    "isEnabled": enabled_status
                }
                self.log(
                    "API call {0}/{1}: Retrieving issues with priority={2}, enabled={3}".format(
                        call_count, total_calls, priority, enabled_status
                    ),
                    "DEBUG"
                )

                try:
                    user_issue_details = self.execute_get_with_pagination(
                        api_family, api_function, params
                    )
                    if user_issue_details:
                        self.log(
                            "Retrieved {0} issue(s) for priority={1}, enabled={2}".format(
                                len(user_issue_details), priority, enabled_status
                            ),
                            "INFO"
                        )
                        all_issues.extend(user_issue_details)
                    else:
                        self.log(
                            "No issues found for priority={0}, enabled={1}".format(
                                priority, enabled_status
                            ),
                            "DEBUG"
                        )
                except Exception as e:
                    self.log(
                        "Failed to retrieve issues for priority={0}, enabled={1}: {2}".format(
                            priority, enabled_status, str(e)
                        ),
                        "WARNING"
                    )
                    # Continue to next combination

        self.log(
            "Completed fetching all combinations, total issues retrieved: {0}".format(
                len(all_issues)
            ),
            "INFO"
        )

        return all_issues

    def _ensure_severity_integers(self, issue_details):
        """
        Ensures severity values in issue rules are integers.

        Post-processes issue details to convert severity values to integers,
        logging warnings for any conversion failures.

        Args:
            issue_details (list): List of issue detail dictionaries to process

        Notes:
            - Modifies issue_details in-place
            - Logs warnings for values that cannot be converted to int
        """
        if not issue_details or not isinstance(issue_details, list):
            return

        self.log(
            "Post-processing {0} issue(s) to ensure severity values are integers".format(
                len(issue_details)
            ),
            "DEBUG"
        )

        conversion_count = 0
        error_count = 0

        for issue in issue_details:
            if not isinstance(issue, dict):
                continue

            rules = issue.get("rules")
            if not rules or not isinstance(rules, list):
                continue

            for rule in rules:
                if not isinstance(rule, dict):
                    continue

            for rule in rules:
                if not isinstance(rule, dict):
                    continue

                if "severity" in rule:
                    original_value = rule["severity"]
                    if not isinstance(original_value, int):
                        try:
                            rule["severity"] = int(original_value)
                            conversion_count += 1
                            self.log(
                                "Converted severity from {0} to {1}".format(
                                    type(original_value).__name__, rule["severity"]
                                ),
                                "DEBUG"
                            )
                        except (ValueError, TypeError) as e:
                            error_count += 1
                            self.log(
                                "Could not convert severity to int: {0} (type: {1}), error: {2}".format(
                                    original_value, type(original_value).__name__, str(e)
                                ),
                                "WARNING"
                            )

        if conversion_count > 0:
            self.log(
                "Successfully converted {0} severity value(s) to integers".format(
                    conversion_count
                ),
                "INFO"
            )

        if error_count > 0:
            self.log(
                "Failed to convert {0} severity value(s) to integers".format(error_count),
                "WARNING"
            )

    def get_diff_gathered(self):
        """
        Gathers assurance issue configurations from Cisco Catalyst Center and generates YAML playbook.

            Orchestrates the brownfield discovery process by:
            1. Determining file path (user-provided or auto-generated)
            2. Identifying components to process (all or filtered)
            3. Retrieving configurations for each component via API calls
            4. Building YAML structure with proper formatting
            5. Writing YAML file with header comments and operation summary
        Returns:
            self: Current instance with updated attributes:
                - self.status: "success" or "failed"
                - self.msg: Operation result message
                - self.result: Dictionary containing response details, file_path,
                configurations count, and operation_summary

        """
        self.log("Gathering assurance issue configurations from Cisco Catalyst Center "
                 "to generate YAML playbook", "INFO")

        # Reset operation tracking
        self.reset_operation_tracking()

        # Get validated configuration
        config = self.validated_config[0] if self.validated_config else {}
        self.log(
            "Processing configuration with generate_all={0}, components_filter={1}".format(
                config.get("generate_all_configurations", False),
                "specified" if config.get("component_specific_filters") else "none"
            ),
            "DEBUG"
        )

        # Determine file path
        file_path = config.get("file_path")
        if not file_path:
            file_path = self.generate_filename()
            self.log("No file_path provided, using auto-generated filename: {0}".format(file_path), "INFO")

        # Ensure directory exists
        self.ensure_directory_exists(file_path)

        # Get generate_all_configurations flag
        self.generate_all_configurations = config.get("generate_all_configurations", False)

        # Build configuration data structure
        all_configs = []

        # Get component filters with safe access
        component_filters = config.get("component_specific_filters", {}) or {}
        components_list = component_filters.get("components_list", [])

        # Validate components_list to check for unexpected components
        if components_list:
            expected_components = ["assurance_user_defined_issue_settings"]
            unexpected_components = [comp for comp in components_list if comp not in expected_components]
            if unexpected_components:
                self.msg = (
                    "Invalid components found in components_list: {0}. "
                    "Only the following components are supported: {1}. "
                    "Please remove the invalid components and try again.".format(
                        unexpected_components, expected_components
                    )
                )
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        # If generate_all_configurations or no components specified, process all
        if self.generate_all_configurations or not components_list:
            self.log(
                "No components specified or generate_all enabled, "
                "processing all available components",
                "INFO"
            )
            # Ensure module_schema is available
            if not hasattr(self, 'module_schema') or not self.module_schema:
                self.module_schema = self.get_workflow_elements_schema()
            # Get all component names from issue_elements in schema
            issue_elements = self.module_schema.get("issue_elements", {})
            components_list = list(issue_elements.keys())

        self.log(
            "Processing {0} component(s): {1}".format(
                len(components_list), components_list
            ),
            "INFO"
        )

        for index, component_name in enumerate(components_list, start=1):
            self.log(
                "Processing component {0}/{1}: {2}".format(
                    index, len(components_list), component_name
                ),
                "INFO"
            )
            self.total_components_processed += 1
            self.log("Processing component: {0}".format(component_name), "INFO")

            # Ensure module_schema is available and valid
            if not hasattr(self, 'module_schema') or not self.module_schema:
                self.module_schema = self.get_workflow_elements_schema()

            # Add debugging for schema structure
            self.log("Current module_schema structure: {0}".format(self.module_schema.keys()), "DEBUG")
            issue_elements = self.module_schema.get("issue_elements", {})
            self.log("Available issue_elements keys: {0}".format(list(issue_elements.keys())), "DEBUG")

            issue_element = issue_elements.get(component_name)
            if not issue_element:
                self.log("Component {0} not found in schema. Available components: {1}".format(
                    component_name, list(issue_elements.keys())), "ERROR")
                continue

            get_function = issue_element.get("get_function_name")
            if not get_function:
                self.log("No get function found for component {0}".format(component_name), "WARNING")
                continue

            self.log("About to call get function {0} for component {1}".format(
                get_function.__name__ if hasattr(get_function, '__name__') else str(get_function), component_name), "DEBUG")

            # Call the appropriate get function with proper filter structure
            filters_structure = {
                "global_filters": config.get("global_filters", {}),
                "component_specific_filters": config.get("component_specific_filters", {})
            }

            try:
                result = get_function(issue_element, filters_structure)
                self.log("Get function completed for component {0}, result type: {1}".format(component_name, type(result)), "DEBUG")
            except Exception as e:
                self.log("Error calling get function for component {0}: {1}".format(component_name, str(e)), "ERROR")
                continue

            # Check if result is valid before accessing
            if not result:
                self.log("Get function for component {0} returned None or empty result".format(component_name), "WARNING")
                continue

            # Extract the component data
            component_data = result.get(component_name, [])
            if component_data:
                self.log(
                    "Building YAML structure with {0} component configuration(s)".format(
                        len(all_configs)
                    ),
                    "INFO"
                )
                all_configs.append({component_name: component_data})

        # Generate final YAML structure
        yaml_config = {}

        # Always generate template structure when generate_all_configurations is True
        if self.generate_all_configurations:
            self.log("Building comprehensive YAML structure with all components using brownfield pattern", "DEBUG")
            # Create list of component configurations following brownfield pattern
            final_list = []
            issue_elements = self.module_schema.get("issue_elements", {})

            for component_name in issue_elements.keys():
                self.log("Processing component: {0}".format(component_name), "DEBUG")
                # Check if we have data for this component
                component_data = None
                for config_item in all_configs:
                    if component_name in config_item:
                        component_data = config_item[component_name]
                        break

                # Create component dictionary with proper structure
                component_dict = {}
                if component_data:
                    component_dict[component_name] = component_data
                else:
                    component_dict[component_name] = []

                final_list.append(component_dict)

            yaml_config = {"config": final_list}
        elif all_configs:
            # Create individual component dictionaries for non-generate_all mode
            final_list = []
            for config_item in all_configs:
                final_list.append(config_item)

            yaml_config = {"config": final_list}
        else:
            # Generate empty template structure when no configurations found and not in generate_all mode
            final_list = []
            issue_elements = self.module_schema.get("issue_elements", {})
            for component_name in issue_elements.keys():
                component_dict = {component_name: []}
                final_list.append(component_dict)
            yaml_config = {"config": final_list}

        # Write to YAML file with header comments
        if yaml_config:
            operation_summary = self.get_operation_summary()
            self.log(
                "Writing YAML configuration to file: {0}".format(file_path),
                "INFO"
            )
            success = self.write_yaml_with_comments(yaml_config, file_path, operation_summary)
            if success:
                if all_configs:
                    self.msg = "YAML config generation succeeded for module '{0}'.".format(self.module_name)
                else:
                    self.msg = "YAML config generation completed for module '{0}' with empty template (no configurations found).".format(self.module_name)
                self.result["response"] = {
                    "message": self.msg,
                    "file_path": file_path,
                    "configurations_generated": len(all_configs),
                    "operation_summary": operation_summary
                }
                self.result["msg"] = self.msg
                self.status = "success"
            else:
                self.msg = "Failed to write YAML configuration to file: {0}".format(file_path)
                self.result["response"] = {"message": self.msg}
                self.result["msg"] = self.msg
                self.status = "failed"
        else:
            operation_summary = self.get_operation_summary()
            self.msg = "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name)
            self.result["response"] = {
                "message": self.msg,
                "operation_summary": operation_summary
            }
            self.result["msg"] = self.msg
            self.status = "success"

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
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "validate_response_schema": {"type": "bool", "default": True},
        "state": {"type": "str", "default": "gathered", "choices": ["gathered"]},
        "config": {"type": "list", "required": True, "elements": "dict"},
    }

    # Initialize the Ansible module with the defined argument spec
    module = AnsibleModule(
        argument_spec=element_spec,
        supports_check_mode=False
    )

    # Create an instance of the workflow manager class
    catalystcenter_assurance_issue = AssuranceIssuePlaybookGenerator(module)

    # Get the state parameter from the module; default to 'gathered'
    state = module.params.get("state")

    # Check if the state is valid
    if state not in catalystcenter_assurance_issue.supported_states:
        catalystcenter_assurance_issue.status = "failed"
        catalystcenter_assurance_issue.msg = "State '{0}' is not supported. Supported states: {1}".format(
            state, catalystcenter_assurance_issue.supported_states
        )
        catalystcenter_assurance_issue.result["msg"] = catalystcenter_assurance_issue.msg
        catalystcenter_assurance_issue.module.fail_json(**catalystcenter_assurance_issue.result)

    # Validate the input parameters
    catalystcenter_assurance_issue.validate_input().check_return_status()

    # Get the function mapped to the current state and execute it
    catalystcenter_assurance_issue.get_diff_state_apply[state]().check_return_status()

    # Exit with the result
    catalystcenter_assurance_issue.module.exit_json(**catalystcenter_assurance_issue.result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
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
- The YAML configurations generated represent the user-defined issue definitions and
  system issue settings configured on the Cisco Catalyst Center.
- Supports extraction of User-Defined Issue Definitions and System Issue Settings configurations.
version_added: 6.20.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Megha Kandari (@kandarimegha)
- Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst
      Center after applying the playbook config.
    type: bool
    default: false
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
        - Includes User-Defined Issue Definitions and System Issue Settings.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name "assurance_issue_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "assurance_issue_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
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
            - Valid values are ["assurance_user_defined_issue_settings", "assurance_system_issue_settings"]
            - If not specified, all supported components are included.
            - Example ["assurance_user_defined_issue_settings", "assurance_system_issue_settings"]
            type: list
            elements: str
            required: false
            choices: ["assurance_user_defined_issue_settings", "assurance_system_issue_settings"]
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
          assurance_system_issue_settings:
            description:
            - System issue settings to filter by device type or issue name.
            type: list
            elements: dict
            required: false
            suboptions:
              device_type:
                description:
                - Device type to filter system issues (e.g., ROUTER, SWITCH, UNIFIED_AP).
                type: str
                required: false
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - issues.AssuranceSettings.get_all_the_custom_issue_definitions_based_on_the_given_filters
    - issues.AssuranceSettings.returns_all_issue_trigger_definitions_for_given_filters
- Paths used are
    - GET /dna/intent/api/v1/customIssueDefinitions
    - GET /dna/intent/api/v1/systemIssueDefinitions
"""

EXAMPLES = r"""
# Generate YAML Configuration with default file path for all user-defined issues
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

# Generate YAML Configuration for system issues with specific device types
- name: Generate YAML Configuration for system issues
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
      - file_path: "/tmp/assurance_issue_config.yml"
        global_filters:
          device_type_list: ["UNIFIED_AP", "ROUTER"]
        component_specific_filters:
          components_list: ["assurance_system_issue_settings"]

# Generate YAML Configuration for all assurance issue components
- name: Generate complete assurance issue configuration
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
            "components_with_complete_failure": ["assurance_system_issue_settings"],
            "success_details": [],
            "failure_details": [
              {
                "component": "assurance_system_issue_settings",
                "status": "failed",
                "error_info": {
                  "error_type": "api_error",
                  "error_message": "Failed to retrieve system issue definitions",
                  "error_code": "API_ERROR"
                }
              }
            ]
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
            self.log(self.msg, "ERROR")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

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
            import os
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
                "assurance_system_issue_settings": {
                    "filters": {
                        "name": {
                            "type": "str",
                            "required": False
                        },
                        "device_type": {
                            "type": "str",
                            "required": False
                        }
                    },
                    "reverse_mapping_function": self.system_issue_reverse_mapping_function,
                    "api_function": "returns_all_issue_trigger_definitions_for_given_filters",
                    "api_family": "issues",
                    "get_function_name": self.get_system_issues,
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

    def epoch_to_datetime(self, epoch_time):
        """
        Convert epoch timestamp to datetime string.
        Args:
            epoch_time: Epoch timestamp in milliseconds
        Returns:
            str: Formatted datetime string or None if invalid
        """
        try:
            if epoch_time and epoch_time != 0:
                import datetime
                # Handle both seconds and milliseconds timestamps
                if epoch_time > 1e10:  # Likely milliseconds
                    timestamp = epoch_time / 1000
                else:  # Likely seconds
                    timestamp = epoch_time

                dt = datetime.datetime.fromtimestamp(timestamp)
                return dt.strftime("%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError, OverflowError):
            pass
        return None

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

    def system_issue_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for system issue configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for system issue details
        """
        self.log("Generating reverse mapping specification for system issues.", "DEBUG")

        return OrderedDict({
            "name": {"type": "str", "source_key": "displayName"},
            "device_type": {"type": "str", "source_key": "deviceType"},
            "description": {"type": "str", "source_key": "description"},
            "issue_enabled": {"type": "bool", "source_key": "issueEnabled"},
            "priority": {"type": "str", "source_key": "priority"},
            "synchronize_to_health_threshold": {"type": "bool", "source_key": "synchronizeToHealthThreshold"},
            "threshold_value": {"type": "str", "source_key": "thresholdValue"},
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
        Retrieves user-defined issue definitions based on the provided filters.
        Args:
            issue_element (dict): A dictionary containing the API family and function for retrieving user-defined issues.
            filters (dict): A dictionary containing global_filters and component_specific_filters.
        Returns:
            dict: A dictionary containing the modified details of user-defined issues.
        """
        self.log("Starting to retrieve user-defined issues with filters: {0}".format(filters), "DEBUG")

        # Safety check for filters
        if not filters:
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

        try:
            if component_specific_filters:
                for filter_param in component_specific_filters:
                    base_params = {}
                    for key, value in filter_param.items():
                        if key == "name":
                            base_params["name"] = value
                        elif key == "is_enabled":
                            base_params["isEnabled"] = str(value).lower()

                    # If specific filters are provided, use them directly
                    if base_params:
                        user_issue_details = self.execute_get_with_pagination(api_family, api_function, base_params)
                        self.log("Retrieved user-defined issue details with filters {0}: {1}".format(base_params, len(user_issue_details)), "INFO")
                        final_user_issues.extend(user_issue_details)
                    else:
                        # If no specific filters, iterate through all priority and enabled combinations
                        priorities = ["P1", "P2", "P3", "P4"]
                        enabled_statuses = ["true", "false"]

                        for priority in priorities:
                            for enabled_status in enabled_statuses:
                                params = {
                                    "priority": priority,
                                    "isEnabled": enabled_status
                                }
                                self.log("Retrieving user-defined issues with priority {0} and enabled={1}".format(priority, enabled_status), "DEBUG")

                                user_issue_details = self.execute_get_with_pagination(api_family, api_function, params)
                                self.log("Retrieved {0} user-defined issues for priority {1}, enabled={2}".format(
                                    len(user_issue_details), priority, enabled_status), "INFO")
                                final_user_issues.extend(user_issue_details)
            else:
                # Execute API calls for all combinations of priority and enabled status
                priorities = ["P1", "P2", "P3", "P4"]
                enabled_statuses = ["true", "false"]

                for priority in priorities:
                    for enabled_status in enabled_statuses:
                        params = {
                            "priority": priority,
                            "isEnabled": enabled_status
                        }
                        self.log("Retrieving user-defined issues with priority {0} and enabled={1}".format(priority, enabled_status), "DEBUG")

                        user_issue_details = self.execute_get_with_pagination(api_family, api_function, params)
                        self.log("Retrieved {0} user-defined issues for priority {1}, enabled={2}".format(
                            len(user_issue_details), priority, enabled_status), "INFO")
                        final_user_issues.extend(user_issue_details)

            # Track success
            self.add_success("assurance_user_defined_issue_settings", {
                "issues_processed": len(final_user_issues)
            })

            # Apply reverse mapping
            reverse_mapping_function = issue_element.get("reverse_mapping_function")
            reverse_mapping_spec = reverse_mapping_function()

            # Transform using inherited modify_parameters function
            issue_details = self.modify_parameters(reverse_mapping_spec, final_user_issues)

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

    def get_system_issues(self, issue_element, filters):
        """
        Retrieves system issue definitions based on the provided filters.
        Args:
            issue_element (dict): A dictionary containing the API family and function for retrieving system issues.
            filters (dict): A dictionary containing global_filters and component_specific_filters.
        Returns:
            dict: A dictionary containing the modified details of system issues.
        """
        self.log("Starting to retrieve system issues with filters: {0}".format(filters), "DEBUG")

        # Add null checks
        if not issue_element:
            self.log("Error: issue_element is None or empty", "ERROR")
            return {
                "assurance_system_issue_settings": [],
                "operation_summary": self.get_operation_summary()
            }

        if not filters:
            self.log("Error: filters is None or empty", "ERROR")
            return {
                "assurance_system_issue_settings": [],
                "operation_summary": self.get_operation_summary()
            }

        final_system_issues = []
        api_family = issue_element.get("api_family")
        api_function = issue_element.get("api_function")

        if not api_family or not api_function:
            self.log("Error: api_family or api_function is missing. api_family={0}, api_function={1}".format(
                api_family, api_function), "ERROR")
            return {
                "assurance_system_issue_settings": [],
                "operation_summary": self.get_operation_summary()
            }

        self.log("Getting system issues using family '{0}' and function '{1}'.".format(
            api_family, api_function), "INFO")

        # Determine device types to query
        device_types = []
        global_filters = filters.get("global_filters") or {}
        device_type_list = global_filters.get("device_type_list", [])

        component_specific_filters = filters.get("component_specific_filters") or {}
        component_specific_filters = component_specific_filters.get(
            "assurance_system_issue_settings", [])

        if device_type_list:
            device_types = device_type_list
        elif component_specific_filters:
            for filter_param in component_specific_filters:
                device_type = filter_param.get("device_type")
                if device_type and device_type not in device_types:
                    device_types.append(device_type)

        # If no device types specified, use common device types
        if not device_types:
            device_types = ["UNIFIED_AP", "SWITCH_AND_HUB", "ROUTER", "WIRELESS_CONTROLLER", "WIRELESS_CLIENT", "WIRED_CLIENT"]
            self.log("No device types specified, using default device types: {0}".format(device_types), "DEBUG")

        try:
            # Try to get all system issues for each device type and enabled state
            self.log("Attempting to retrieve system issues for device types: {0}".format(device_types), "DEBUG")

            for issue_enabled in ["true", "false"]:
                for device_type in device_types:
                    try:
                        self.log("Calling API for device_type: {0}, issue_enabled: {1}".format(device_type, issue_enabled), "DEBUG")
                        params = {"deviceType": device_type, "issueEnabled": issue_enabled}
                        response = self.execute_get_with_pagination(
                            api_family,
                            api_function,
                            params
                        )

                        self.log("API response received for device_type {0}, issue_enabled {1}: {2}".format(
                            device_type, issue_enabled, type(response)), "DEBUG")

                        if response:
                            self.log("Retrieved {0} system issues for device_type {1}, issue_enabled {2}".format(
                                len(response), device_type, issue_enabled), "DEBUG")
                            final_system_issues.extend(response)
                        else:
                            self.log("No response for device_type {0}, issue_enabled {1}".format(
                                device_type, issue_enabled), "DEBUG")
                    except Exception as api_error:
                        self.log("API error for device_type {0}, issue_enabled {1}: {2}".format(
                            device_type, issue_enabled, str(api_error)), "WARNING")
                        continue

            self.log("Total system issues retrieved: {0}".format(len(final_system_issues)), "INFO")

            # Track success
            self.add_success("assurance_system_issue_settings", {
                "issues_processed": len(final_system_issues)
            })

            # Apply reverse mapping
            reverse_mapping_function = issue_element.get("reverse_mapping_function")
            if not reverse_mapping_function:
                self.log("Error: reverse_mapping_function is None for issue_element", "ERROR")
                return {
                    "assurance_system_issue_settings": [],
                    "operation_summary": self.get_operation_summary()
                }

            reverse_mapping_spec = reverse_mapping_function()
            if not reverse_mapping_spec:
                self.log("Error: reverse_mapping_spec is None", "ERROR")
                return {
                    "assurance_system_issue_settings": [],
                    "operation_summary": self.get_operation_summary()
                }

            # Transform using inherited modify_parameters function
            self.log("About to call modify_parameters with reverse_mapping_spec: {0}, final_system_issues count: {1}".format(
                type(reverse_mapping_spec), len(final_system_issues)), "DEBUG")
            issue_details = self.modify_parameters(reverse_mapping_spec, final_system_issues)
            self.log("modify_parameters returned: {0}".format(type(issue_details)), "DEBUG")

            if issue_details is None:
                self.log("Error: modify_parameters returned None", "ERROR")
                return {
                    "assurance_system_issue_settings": [],
                    "operation_summary": self.get_operation_summary()
                }

            return {
                "assurance_system_issue_settings": issue_details,
                "operation_summary": self.get_operation_summary()
            }

        except Exception as e:
            self.log("Error retrieving system issues: {0}".format(str(e)), "ERROR")
            self.add_failure("assurance_system_issue_settings", {
                "error_type": "api_error",
                "error_message": str(e)
            })
            return {
                "assurance_system_issue_settings": [],
                "operation_summary": self.get_operation_summary()
            }

    def get_diff_gathered(self):
        """
        Gathers assurance issue configurations from Cisco Catalyst Center and generates YAML playbook.
        Returns:
            self: Returns the current object with status and result set.
        """
        self.log("Starting brownfield assurance issue configuration gathering process", "INFO")

        # Reset operation tracking
        self.reset_operation_tracking()

        # Get validated configuration
        config = self.validated_config[0] if self.validated_config else {}

        # Determine file path
        file_path = config.get("file_path")
        if not file_path:
            file_path = self.generate_filename()
            self.log("Using default filename: {0}".format(file_path), "INFO")

        # Ensure directory exists
        self.ensure_directory_exists(file_path)

        # Get generate_all_configurations flag
        self.generate_all_configurations = config.get("generate_all_configurations", False)

        # Build configuration data structure
        all_configs = []

        # Get component filters with safe access
        component_filters = config.get("component_specific_filters", {}) or {}
        components_list = component_filters.get("components_list", [])

        # If generate_all_configurations or no components specified, process all
        if self.generate_all_configurations or not components_list:
            # Ensure module_schema is available
            if not hasattr(self, 'module_schema') or not self.module_schema:
                self.module_schema = self.get_workflow_elements_schema()
            # Get all component names from issue_elements in schema
            issue_elements = self.module_schema.get("issue_elements", {})
            components_list = list(issue_elements.keys())

        self.log("Processing components: {0}".format(components_list), "INFO")

        for component_name in components_list:
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
                all_configs.append({component_name: component_data})

        # Generate final YAML structure
        yaml_config = []

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

            yaml_config.append({"config": final_list})
        elif all_configs:
            # Create individual component dictionaries for non-generate_all mode
            final_list = []
            for config_item in all_configs:
                final_list.append(config_item)

            yaml_config.append({"config": final_list})
        else:
            # Generate empty template structure when no configurations found and not in generate_all mode
            final_list = []
            issue_elements = self.module_schema.get("issue_elements", {})
            for component_name in issue_elements.keys():
                component_dict = {component_name: []}
                final_list.append(component_dict)
            yaml_config.append({"config": final_list})

        # Write to YAML file
        if yaml_config:
            success = self.write_dict_to_yaml(yaml_config, file_path)
            if success:
                operation_summary = self.get_operation_summary()
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
        "config_verify": {"type": "bool", "default": False},
        "state": {"type": "str", "default": "gathered", "choices": ["gathered"]},
        "config": {"type": "list", "required": True, "elements": "dict"},
    }

    # Initialize the Ansible module with the defined argument spec
    module = AnsibleModule(
        argument_spec=element_spec,
        supports_check_mode=False
    )

    # Create an instance of the workflow manager class
    dnac_assurance_issue = AssuranceIssuePlaybookGenerator(module)

    # Get the state parameter from the module; default to 'gathered'
    state = module.params.get("state")

    # Check if the state is valid
    if state not in dnac_assurance_issue.supported_states:
        dnac_assurance_issue.status = "failed"
        dnac_assurance_issue.msg = "State '{0}' is not supported. Supported states: {1}".format(
            state, dnac_assurance_issue.supported_states
        )
        dnac_assurance_issue.result["msg"] = dnac_assurance_issue.msg
        dnac_assurance_issue.module.fail_json(**dnac_assurance_issue.result)

    # Validate the input parameters
    dnac_assurance_issue.validate_input().check_return_status()

    # Get the function mapped to the current state and execute it
    dnac_assurance_issue.get_diff_state_apply[state]().check_return_status()

    # Exit with the result
    dnac_assurance_issue.module.exit_json(**dnac_assurance_issue.result)


if __name__ == "__main__":
    main()

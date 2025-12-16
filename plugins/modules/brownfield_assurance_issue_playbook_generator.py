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
      global_filters:
        description:
        - Global filters to apply when generating the YAML configuration file.
        - These filters identify which assurance issues to extract configurations from.
        - At least one filter type must be specified to identify target settings.
        type: dict
        required: false
        suboptions:
          issue_name_list:
            description:
            - List of issue names to extract configurations from.
            - Can be applied to both user-defined and system issue definitions.
            - Issue names must match those configured in Catalyst Center.
            - Example ["High CPU Usage Alert", "AP Frequent Reboots", "Interface Down"]
            type: list
            elements: str
            required: false
          device_type_list:
            description:
            - List of device types to extract system issue configurations from.
            - Valid values include ROUTER, SWITCH, WIRELESS_CONTROLLER, UNIFIED_AP, etc.
            - Only applicable to system issue settings.
            - Example ["UNIFIED_AP", "SWITCH", "ROUTER"]
            type: list
            elements: str
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
            - Valid values are ["assurance_issue", "assurance_user_defined_issue_settings", "assurance_system_issue_settings"]
            - If not specified, all supported components are included.
            - Example ["assurance_issue", "assurance_user_defined_issue_settings", "assurance_system_issue_settings"]
            type: list
            elements: str
            required: false
            choices: ["assurance_issue", "assurance_user_defined_issue_settings", "assurance_system_issue_settings"]
          assurance_issue:
            description:
            - Active assurance issues to filter by issue name, priority, status, device, or site.
            type: list
            elements: dict
            required: false
            suboptions:
              issue_name:
                description:
                - Issue name to filter by specific issue title.
                type: str
                required: false
              priority:
                description:
                - Issue priority to filter by (P1, P2, P3, P4).
                type: str
                required: false
                choices: ["P1", "P2", "P3", "P4"]
              issue_status:
                description:
                - Issue status to filter by (ACTIVE, RESOLVED, IGNORED).
                type: str
                required: false
                choices: ["ACTIVE", "RESOLVED", "IGNORED"]
              device_name:
                description:
                - Device name to filter issues by specific device.
                type: str
                required: false
              site_hierarchy:
                description:
                - Site hierarchy to filter issues by location.
                type: str
                required: false
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
              name:
                description:
                - System issue name to filter by name.
                type: str
                required: false
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
          device_type_list: ["UNIFIED_AP", "SWITCH"]
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

# Generate YAML Configuration with specific issue name filters
- name: Generate YAML Configuration for specific issues
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
      - file_path: "/tmp/specific_issues.yml"
        global_filters:
          issue_name_list: ["High CPU Usage Alert", "AP Frequent Reboots"]
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

        # Validate component_specific_filters
        component_filters = config.get("component_specific_filters", {})
        if component_filters:
            components_list = component_filters.get("components_list", [])
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
                "assurance_issue": {
                    "filters": {
                        "issue_name": {
                            "type": "str",
                            "required": False
                        },
                        "priority": {
                            "type": "str",
                            "required": False
                        },
                        "issue_status": {
                            "type": "str",
                            "required": False
                        },
                        "device_name": {
                            "type": "str",
                            "required": False
                        },
                        "site_hierarchy": {
                            "type": "str",
                            "required": False
                        }
                    },
                    "reverse_mapping_function": self.active_issue_reverse_mapping_function,
                    "api_function": "get_the_details_of_issues_for_given_set_of_filters",
                    "api_family": "issues",
                    "get_function_name": self.get_active_issues,
                },
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

    def active_issue_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for active issue configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for active issue details
        """
        self.log("Generating reverse mapping specification for active issues.", "DEBUG")

        return OrderedDict({
            "issue_name": {"type": "str", "source_key": "summary"},
            "issue_process_type": {"type": "str", "source_key": "issueProcessType", "default": "resolution"},
            "ignore_duration": {"type": "str", "source_key": "ignoreDuration"},
            # "start_datetime": {"type": "str", "source_key": "firstOccurredTime"},
            # "end_datetime": {"type": "str", "source_key": "mostRecentOccurredTime"},
            "priority": {"type": "str", "source_key": "priority"},
            "issue_status": {"type": "str", "source_key": "status"},
            "site_hierarchy": {"type": "str", "source_key": "siteHierarchy"},
            # "device_name": {"type": "str", "source_key": "nwDeviceName"},
            # "mac_address": {"type": "str", "source_key": "macAddress"},
            "network_device_ip_address": {"type": "str", "source_key": "managementIpAddr"},
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

    def get_active_issues(self, issue_element, filters):
        """
        Retrieves active issues based on the provided filters.
        Args:
            issue_element (dict): A dictionary containing the API family and function for retrieving active issues.
            filters (dict): A dictionary containing global_filters and component_specific_filters.
        Returns:
            dict: A dictionary containing the modified details of active issues.
        """
        self.log("Starting to retrieve active issues with filters: {0}".format(filters), "DEBUG")

        # Ensure filters and issue_element are not None
        if filters is None:
            filters = {}
        if issue_element is None:
            issue_element = {}

        api_family = issue_element.get("api_family")
        api_function = issue_element.get("api_function")

        self.log("Getting active issues using family '{0}' and function '{1}'.".format(
            api_family, api_function), "INFO")

        # Build API parameters from filters
        params = {}

        # Set required time parameters for active issues API
        # Get issues from the last 24 hours by default
        import time
        current_time_ms = int(time.time() * 1000)  # Current time in milliseconds
        twenty_four_hours_ms = 24 * 60 * 60 * 1000  # 24 hours in milliseconds
        start_time_ms = current_time_ms - twenty_four_hours_ms

        params["startTime"] = start_time_ms
        params["endTime"] = current_time_ms
        params["limit"] = 500  # Set a reasonable limit
        params["offset"] = 0   # Start from beginning

        self.log("Using time window: startTime={0}, endTime={1}".format(start_time_ms, current_time_ms), "DEBUG")

        # Apply global filters if present
        global_filters = filters.get("global_filters", {})
        if global_filters is None:
            global_filters = {}
        if global_filters.get("issue_name_list"):
            params["name"] = ",".join(global_filters["issue_name_list"])  # Changed from issueName to name

        # Apply component-specific filters
        component_specific_dict = filters.get("component_specific_filters", {})
        if component_specific_dict is None:
            component_specific_dict = {}
        component_specific_filters = component_specific_dict.get("assurance_issue", [])
        if component_specific_filters:
            for filter_param in component_specific_filters:
                for key, value in filter_param.items():
                    if key == "issue_name":
                        params["name"] = value  # Changed from issueName to name
                    elif key == "priority":
                        params["priority"] = value
                    elif key == "issue_status":
                        params["status"] = value  # Changed from issueStatus to status
                    elif key == "device_name":
                        params["deviceName"] = value
                    elif key == "site_hierarchy":
                        params["siteHierarchy"] = value

        try:
            # Use direct API call instead of pagination for debugging
            self.log("Retrieving active issues using direct API call with parameters: {0}".format(params), "DEBUG")

            # Try direct API call first to understand response structure
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params=params,
            )

            self.log("Raw API response type: {0}".format(type(response)), "DEBUG")
            self.log("Raw API response: {0}".format(response), "DEBUG")

            if response is None:
                self.log("API call returned None. The API function may not be available.", "WARNING")
                self.add_success("assurance_issue", {
                    "issues_processed": 0,
                    "message": "No data returned from API"
                })
                return {"assurance_issue": []}

            # Extract data properly
            if isinstance(response, dict):
                active_issue_details = response.get("response", [])
            elif isinstance(response, list):
                active_issue_details = response
            else:
                active_issue_details = []

            if not isinstance(active_issue_details, list):
                active_issue_details = [active_issue_details] if active_issue_details else []

            self.log("Retrieved active issue details: {0} issues".format(len(active_issue_details)), "INFO")
            if active_issue_details:
                self.log("First issue sample: {0}".format(active_issue_details[0]), "DEBUG")

            # Track success
            self.add_success("assurance_issue", {
                "issues_processed": len(active_issue_details)
            })

            # Apply reverse mapping
            reverse_mapping_function = issue_element.get("reverse_mapping_function")
            reverse_mapping_spec = reverse_mapping_function()

            self.log("Reverse mapping spec: {0}".format(reverse_mapping_spec), "DEBUG")

            # Transform using inherited modify_parameters function
            self.log("About to call modify_parameters with {0} active issue details".format(len(active_issue_details)), "DEBUG")
            issue_details = self.modify_parameters(reverse_mapping_spec, active_issue_details)
            self.log("modify_parameters completed successfully", "DEBUG")

            # Post-process to convert epoch timestamps to datetime with better error handling
            if issue_details and isinstance(issue_details, list):
                for i, issue in enumerate(issue_details):
                    if isinstance(issue, dict):
                        try:
                            if "start_datetime" in issue and issue["start_datetime"]:
                                start_time = issue["start_datetime"]
                                self.log("Converting start_datetime {0} (type: {1})".format(start_time, type(start_time)), "DEBUG")
                                issue["start_datetime"] = self.epoch_to_datetime(start_time)
                            if "end_datetime" in issue and issue["end_datetime"]:
                                end_time = issue["end_datetime"]
                                self.log("Converting end_datetime {0} (type: {1})".format(end_time, type(end_time)), "DEBUG")
                                issue["end_datetime"] = self.epoch_to_datetime(end_time)
                        except Exception as e:
                            self.log("Error processing timestamps for issue {0}: {1}".format(i, str(e)), "ERROR")
                            # Continue processing other issues even if timestamp conversion fails
                    else:
                        self.log("Warning: Issue {0} is not a dict, it's {1}: {2}".format(i, type(issue), issue), "WARNING")

            return {
                "assurance_issue": issue_details,
            }

        except Exception as e:
            error_msg = "Failed to retrieve active issues: {0}".format(str(e))
            self.log(error_msg, "ERROR")
            self.add_failure("assurance_issue", {
                "error_type": "api_error",
                "error_message": error_msg,
                "error_code": "ACTIVE_ISSUES_RETRIEVAL_FAILED"
            })
            return {
                "assurance_issue": [],
            }

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

        final_user_issues = []
        api_family = issue_element.get("api_family")
        api_function = issue_element.get("api_function")

        self.log("Getting user-defined issues using family '{0}' and function '{1}'.".format(
            api_family, api_function), "INFO")

        params = {}
        component_specific_filters = filters.get("component_specific_filters", {}).get(
            "assurance_user_defined_issue_settings", [])

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

        component_specific_filters = filters.get("component_specific_filters", {}).get(
            "assurance_system_issue_settings", [])

        if device_type_list:
            device_types = device_type_list
        elif component_specific_filters:
            for filter_param in component_specific_filters:
                device_type = filter_param.get("device_type")
                if device_type and device_type not in device_types:
                    device_types.append(device_type)

        # If no device types specified, use common device types

        try:
            # Try to get all system issues without device type filtering first
            self.log("Attempting to retrieve all system issues without device type filtering", "DEBUG")
            for issue_enabled in ["true", "false"]:
                response = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    params={"deviceType": device_types, "issueEnabled": issue_enabled},
                )

            if response and response.get("response"):
                issues = response.get("response")
                self.log("Retrieved {0} total system issues".format(len(issues)), "INFO")
                final_system_issues.extend(issues)
            else:
                self.log("No response or empty response from system issues API", "WARNING")

            self.log("Total system issues retrieved: {0}".format(len(final_system_issues)), "INFO")

            # Track success
            self.add_success("assurance_system_issue_settings", {
                "issues_processed": len(final_system_issues)
            })

            # Apply reverse mapping
            reverse_mapping_function = issue_element.get("reverse_mapping_function")
            reverse_mapping_spec = reverse_mapping_function()

            # Transform using inherited modify_parameters function
            issue_details = self.modify_parameters(reverse_mapping_spec, final_system_issues)

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

        # Get component filters
        component_filters = config.get("component_specific_filters", {})
        components_list = component_filters.get("components_list", [])

        # If generate_all_configurations or no components specified, process all
        if self.generate_all_configurations or not components_list:
            components_list = list(self.module_schema.get("issue_elements", {}).keys())

        self.log("Processing components: {0}".format(components_list), "INFO")

        for component_name in components_list:
            self.total_components_processed += 1
            self.log("Processing component: {0}".format(component_name), "INFO")

            issue_element = self.module_schema["issue_elements"].get(component_name)
            if not issue_element:
                self.log("Component {0} not found in schema".format(component_name), "WARNING")
                continue

            get_function = issue_element.get("get_function_name")
            if not get_function:
                self.log("No get function found for component {0}".format(component_name), "WARNING")
                continue

            # Call the appropriate get function
            result = get_function(issue_element, config)

            # Extract the component data
            component_data = result.get(component_name, [])
            if component_data:
                all_configs.append({component_name: component_data})

        # Generate final YAML structure
        yaml_config = []
        if all_configs:
            # Merge all component configurations
            merged_config = {}
            for config_item in all_configs:
                merged_config.update(config_item)

            yaml_config.append({"config": [merged_config]})

        # Write to YAML file
        if yaml_config:
            success = self.write_dict_to_yaml(yaml_config, file_path)
            if success:
                operation_summary = self.get_operation_summary()
                self.msg = "YAML config generation succeeded for module '{0}'.".format(self.module_name)
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

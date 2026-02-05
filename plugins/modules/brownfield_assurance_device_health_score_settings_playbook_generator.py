#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for brownfield YAML playbook generation from Cisco Catalyst Center device health score settings.

This module extracts existing device health score configurations including KPI thresholds, overall health
inclusion flags, and issue threshold synchronization settings from Cisco Catalyst Center and generates YAML
playbooks compatible with the assurance_device_health_score_settings_workflow_manager module for brownfield
infrastructure documentation, configuration backup, migration planning, and multi-site deployment
standardization.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Megha Kandari, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_assurance_device_health_score_settings_playbook_generator
short_description: Generate YAML configurations playbook for 'assurance_device_health_score_settings_workflow_manager' module.
description:
  - Generates YAML configuration playbooks compatible with the
    C(assurance_device_health_score_settings_workflow_manager) module from existing
    Cisco Catalyst Center configurations.
  - Extracts device health score settings including device family KPI thresholds,
    overall health inclusion flags, and issue threshold synchronization settings
    from Catalyst Center.
  - Reduces manual effort in creating Ansible playbooks for brownfield
    infrastructure by automatically discovering and documenting existing
    configurations.
  - Supports auto-discovery mode to extract all configured device health score
    settings across all device families.
  - Supports targeted extraction using device family filters for specific
    infrastructure components.
  - Uses multiple API calls with C(includeForOverallHealth) parameter variations
    (both true and false) to ensure complete data extraction from Catalyst Center.
  - When device families are specified in filters, executes separate API calls
    for each device family for optimal data retrieval and filtering.
  - When no device families are specified, retrieves all available device health
    score settings from the system for complete brownfield discovery.
  - Generated YAML files include comprehensive header comments with metadata,
    generation timestamp, source system details, configuration summary statistics,
    and usage instructions.
  - Supports modern nested filter structures (C(component_specific_filters)) for backward compatibility.
  - Provides detailed operation summaries including success and failure statistics,
    device family categorization (complete success, partial success, complete
    failure), and comprehensive error reporting for troubleshooting.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Megha Kandari (@mekandar)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - The desired state of Cisco Catalyst Center after module completion.
    - Only C(gathered) state is supported for brownfield configuration extraction.
    - In C(gathered) state, the module extracts existing device health score
      settings from Catalyst Center and generates a YAML playbook file.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - List of configuration parameters for generating YAML playbooks compatible
      with the C(assurance_device_health_score_settings_workflow_manager) module.
    - Defines filters to specify which device families and KPI settings to
      include in the generated YAML configuration file.
    - Supports auto-discovery mode to automatically extract all configured
      device health score settings without manual filter specification.
    - When C(generate_all_configurations) is enabled, filter parameters become
      optional and defaults are applied automatically.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - Enables auto-discovery mode to automatically generate YAML configurations
          for all device families and all available KPI settings configured in
          Cisco Catalyst Center.
        - When enabled (C(true)), the module discovers all device health score
          settings without requiring manual filter specification.
        - Overrides any provided C(component_specific_filters)
          to ensure complete infrastructure discovery.
        - Useful for brownfield documentation, infrastructure audits, and
          comprehensive configuration backups.
        - When enabled with no C(file_path) specified, generates a default
          timestamped filename in the current working directory.
        - Setting to C(false) requires explicit filter specification via
          C(component_specific_filters) for targeted extraction.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Absolute or relative path where the generated YAML configuration file
          will be saved.
        - If not provided, the module generates a default filename in the current
          working directory with the format
          C(<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml).
        - Example default filename C(assurance_device_health_score_settings_workflow_manager_playbook_2026-01-24_12-33-20.yml).
        - The directory path will be created automatically if it does not exist.
        - Supports both absolute paths (C(/tmp/config.yml)) and relative paths
          (C(./configs/health_score.yml)).
        - File will be overwritten if it already exists at the specified path.
        type: str
        required: false
      component_specific_filters:
        description:
        - Dictionary of filters to specify which device families and KPI settings
          to include in the generated YAML configuration file.
        - Allows granular selection of specific device families and their
          associated KPI configurations.
        - If not specified and C(generate_all_configurations) is C(false), all
          configured device health score settings will be extracted.
        - Supports both modern nested structure (C(device_health_score_settings))
          and legacy flat structure (C(device_families)) for backward
          compatibility.
        - Can contain C(components_list) to specify which components to process,
          C(device_families) for direct device family filtering, or nested
          C(device_health_score_settings) for component-specific filtering.
        required: false
        suboptions:
          components_list:
            description:
            - List of component types to extract from Catalyst Center.
            - Currently supports only C(device_health_score_settings) component.
            - When specified without nested C(device_health_score_settings)
              filters, extracts all device families for the specified component.
            - Determines which component processing workflows to execute during
              YAML generation.
            - Future versions may support additional component types for expanded
              brownfield extraction capabilities.
            type: list
            elements: str
            required: false
            choices:
            - device_health_score_settings
          device_health_score_settings:
            description:
            - Nested dictionary for device health score settings specific filters.
            - Provides fine-grained control over device families and KPI settings
              to extract from Catalyst Center.
            - Allows targeting specific device families without extracting all
              configured settings.
            - Modern recommended approach for filter specification in new
              playbooks.
            type: dict
            required: false
            suboptions:
              device_families:
                description:
                - List of specific device family names to extract KPI threshold
                  settings for using modern nested filter format.
                - Valid device family names include C(UNIFIED_AP) for wireless
                  access points, C(ROUTER) for routing devices, C(SWITCH) or
                  C(SWITCH_AND_HUB) for switching infrastructure,
                  C(WIRELESS_CONTROLLER) for wireless LAN controllers,
                  C(WIRELESS_SENSOR) for wireless sensors, C(MERAKI_DASHBOARD)
                  for Meraki devices, C(FIREWALL) for firewall appliances, and
                  other Catalyst Center supported device types.
                - If not specified, all device families with configured KPI
                  threshold settings will be extracted for comprehensive
                  brownfield documentation.
                - Each device family may have different KPI metrics and
                  thresholds based on device capabilities and health monitoring
                  requirements.
                - Example filter C(["UNIFIED_AP", "ROUTER", "SWITCH_AND_HUB",
                  "WIRELESS_CONTROLLER"]) extracts settings for wireless and
                  wired infrastructure.
                - Device family names are case-sensitive and must match exact
                  names used in Catalyst Center.
                type: list
                elements: str
                required: false

requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
- PyYAML >= 5.1
notes:
- SDK Method used is devices.Devices.get_all_health_score_definitions_for_given_filters
- Path used is GET /dna/intent/api/v1/device-health/health-score/definitions
- Module requires Catalyst Center version 2.3.7.9 or higher for device health
  score settings support.
- Generated YAML files include comprehensive header comments with generation
  metadata, configuration summary statistics, and usage instructions.
- The module executes multiple API calls with C(includeForOverallHealth)
  parameter variations (true and false) to ensure complete KPI data extraction.
- When device families are specified, separate API calls are made for each
  device family for optimal performance and data filtering.
- Operation summaries include detailed success/failure statistics with device
  family categorization for troubleshooting and validation.
- Supports both auto-discovery mode (C(generate_all_configurations=true)) for
  complete infrastructure extraction and targeted mode with filters for
  specific components.
- Check mode is supported but does not perform actual YAML file generation;
  it validates parameters and returns expected operation results.
- The module is idempotent; running multiple times with the same parameters
  generates identical YAML content (except generation timestamp in header).
- Generated YAML files can be used directly with
  C(assurance_device_health_score_settings_workflow_manager) module to apply
  configurations to other Catalyst Center instances.
- Device family names are case-sensitive and must match exact names used in
  Catalyst Center (e.g., C(UNIFIED_AP) not C(unified_ap)).
- KPI names in generated YAML use user-friendly format (e.g., C(CPU Utilization))
  rather than internal API format (e.g., C(cpuUtilizationThreshold)) for
  improved readability.
- The module handles connection timeouts, API errors, and invalid responses
  with comprehensive error messages and operation summaries.
- Large-scale deployments with many device families and KPIs may require
  increased C(dnac_api_task_timeout) values for complete data extraction.
- Generated YAML structure follows ordered dictionary format to maintain
  consistent key ordering across multiple generations.

seealso:
- module: cisco.dnac.assurance_device_health_score_settings_workflow_manager
  description: Workflow manager module for applying device health score settings
               to Catalyst Center.
"""

EXAMPLES = r"""

- name: Generate YAML Configuration for all device health score settings
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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

- name: Generate YAML Configuration with custom file path
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/assurance_health_score_settings.yml"

- name: Generate YAML Configuration for all device health score components
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/assurance_health_score_settings.yml"
        component_specific_filters:
          components_list: ["device_health_score_settings"]

- name: Generate YAML Configuration for specific device families
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/specific_device_health_score_settings.yml"
        component_specific_filters:
          components_list: ["device_health_score_settings"]
          device_health_score_settings:
            device_families: ["UNIFIED_AP", "ROUTER", "SWITCH_AND_HUB", "WIRELESS_CONTROLLER"]

- name: Generate YAML Configuration using legacy filter format
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/legacy_device_health_score_settings.yml"
        component_specific_filters:
          device_families: ["UNIFIED_AP", "ROUTER"]
"""

RETURN = r"""
# Case_1: Successful YAML Generation with Complete Configuration Extraction
response_1:
  description:
  - Response returned when YAML configuration generation completes successfully
    with all requested device health score settings extracted and written to file.
  - Includes comprehensive operation summary with success statistics, device
    family categorization, and detailed configuration metrics.
  - Generated YAML file contains formatted playbook compatible with
    C(assurance_device_health_score_settings_workflow_manager) module.
  returned: always
  type: dict
  sample:
    response:
      message: >-
        YAML config generation succeeded for module
        'assurance_device_health_score_settings_workflow_manager'.
      file_path: /tmp/assurance_health_score_settings.yml
      configurations_generated: 15
      operation_summary:
        total_device_families_processed: 3
        total_kpis_processed: 15
        total_successful_operations: 15
        total_failed_operations: 0
        device_families_with_complete_success:
        - UNIFIED_AP
        - ROUTER
        - SWITCH
        device_families_with_partial_success: []
        device_families_with_complete_failure: []
        success_details:
        - device_family: UNIFIED_AP
          kpi_name: Interference 6 GHz
          status: success
          threshold_value: 80.0
          include_for_overall_health: true
        - device_family: UNIFIED_AP
          kpi_name: CPU Utilization
          status: success
          threshold_value: 85.0
          include_for_overall_health: true
        - device_family: ROUTER
          kpi_name: Memory Utilization
          status: success
          threshold_value: 90.0
          include_for_overall_health: true
        failure_details: []
    msg: >-
      YAML config generation succeeded for module
      'assurance_device_health_score_settings_workflow_manager'.

# Case_2: Successful Generation with Partial Failures
response_2:
  description:
  - Response returned when YAML generation completes but some device families
    or KPI configurations encountered errors during extraction.
  - Operation status is C(failed) but file is still generated with successfully
    retrieved configurations.
  - C(operation_summary.failure_details) contains specific error information
    for troubleshooting failed extractions.
  - C(device_families_with_partial_success) lists families with both successful
    and failed KPI retrievals.
  returned: always
  type: dict
  sample:
    response:
      message: >-
        YAML config generation completed with failures for module
        'assurance_device_health_score_settings_workflow_manager'.
        Check operation_summary for details.
      file_path: /tmp/assurance_health_score_settings.yml
      configurations_generated: 12
      operation_summary:
        total_device_families_processed: 3
        total_kpis_processed: 12
        total_successful_operations: 12
        total_failed_operations: 3
        device_families_with_complete_success:
        - UNIFIED_AP
        device_families_with_partial_success:
        - ROUTER
        - SWITCH
        device_families_with_complete_failure: []
        success_details:
        - device_family: UNIFIED_AP
          kpi_name: Air Quality 5 GHz
          status: success
          threshold_value: 75.0
          include_for_overall_health: true
        - device_family: ROUTER
          kpi_name: CPU Utilization
          status: success
          threshold_value: 85.0
          include_for_overall_health: true
        failure_details:
        - device_family: ROUTER
          kpi_name: Unknown KPI
          status: failed
          error_info:
            error_type: kpi_retrieval_error
            error_message: KPI configuration not available in Catalyst Center
            error_code: KPI_NOT_FOUND
        - device_family: SWITCH
          kpi_name: Invalid Metric
          status: failed
          error_info:
            error_type: api_error
            error_message: API timeout while retrieving KPI settings
            error_code: API_TIMEOUT_ERROR
    msg: >-
      YAML config generation completed with failures for module
      'assurance_device_health_score_settings_workflow_manager'.
      Check operation_summary for details.

# Case_3: No Configurations Found Scenario
response_3:
  description:
  - Response returned when no device health score settings configurations are
    found matching the specified filters or in the Catalyst Center system.
  - Operation status is C(ok) indicating successful execution but no data
    available to generate.
  - Empty YAML file may be created with header comments but no configuration
    content.
  - C(operation_summary) shows zero counts for all metrics.
  returned: always
  type: dict
  sample:
    response:
      message: >-
        No configurations or components to process for module
        'assurance_device_health_score_settings_workflow_manager'.
        Verify input filters or configuration.
      file_path: >-
        assurance_device_health_score_settings_workflow_manager_playbook_2026-02-04_14-30-15.yml
      operation_summary:
        total_device_families_processed: 0
        total_kpis_processed: 0
        total_successful_operations: 0
        total_failed_operations: 0
        device_families_with_complete_success: []
        device_families_with_partial_success: []
        device_families_with_complete_failure: []
        success_details: []
        failure_details: []
    msg: >-
      No configurations or components to process for module
      'assurance_device_health_score_settings_workflow_manager'.
      Verify input filters or configuration.

# Case_4: Complete Failure Scenario
response_4:
  description:
  - Response returned when YAML generation fails completely due to system
    errors, API failures, or file write issues.
  - No configurations successfully retrieved or file could not be written to
    specified path.
  - C(device_families_with_complete_failure) lists all families that failed
    entirely without any successful KPI retrievals.
  - Check C(failure_details) for specific error information and error codes.
  returned: always
  type: dict
  sample:
    response:
      message: >-
        YAML config generation failed for module
        'assurance_device_health_score_settings_workflow_manager' -
        unable to write to file.
      file_path: /tmp/assurance_health_score_settings.yml
      operation_summary:
        total_device_families_processed: 2
        total_kpis_processed: 0
        total_successful_operations: 0
        total_failed_operations: 8
        device_families_with_complete_success: []
        device_families_with_partial_success: []
        device_families_with_complete_failure:
        - UNIFIED_AP
        - ROUTER
        success_details: []
        failure_details:
        - device_family: UNIFIED_AP
          kpi_name: UNKNOWN
          status: failed
          error_info:
            error_type: api_error
            error_message: Connection timeout to Catalyst Center API
            error_code: CONNECTION_TIMEOUT
        - device_family: ROUTER
          kpi_name: UNKNOWN
          status: failed
          error_info:
            error_type: authentication_error
            error_message: Invalid credentials or insufficient permissions
            error_code: AUTH_FAILED
    msg: >-
      YAML config generation failed for module
      'assurance_device_health_score_settings_workflow_manager' -
      unable to write to file.

# Case_5: Invalid Parameter Validation Failure
response_5:
  description:
  - Response returned when playbook configuration parameters fail validation
    before YAML generation begins.
  - Occurs when invalid filter parameters, incorrect data types, or
    unsupported component names are provided.
  - No API calls executed and no file generation attempted.
  - Error message provides specific validation failure details and allowed
    parameter values.
  returned: always
  type: dict
  sample:
    response:
      message: >-
        Invalid component_specific_filters parameter(s) found: invalid_param.
        Allowed parameters are: components_list, device_families,
        device_health_score_settings.
    msg: >-
      Invalid component_specific_filters parameter(s) found: invalid_param.
      Allowed parameters are: components_list, device_families,
      device_health_score_settings.

msg:
  description:
  - Human-readable message describing the operation result.
  - Indicates success, failure, or informational status of YAML generation.
  - Matches the C(message) field in response dictionary for consistency.
  - Provides high-level summary without detailed operation_summary metrics.
  returned: always
  type: str
  sample: >
    YAML config generation succeeded for module
    'assurance_device_health_score_settings_workflow_manager'.
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
from collections import OrderedDict
import os
import time


try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None


if HAS_YAML:
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class AssuranceDeviceHealthScorePlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    Brownfield playbook generator for Cisco Catalyst Center device health score settings.

    This class orchestrates automated YAML playbook generation for device health score
    settings by extracting existing configurations from Cisco Catalyst Center via REST APIs
    and transforming them into Ansible playbooks compatible with the
    assurance_device_health_score_settings_workflow_manager module.

    The generator supports both auto-discovery mode (extracting all configured settings)
    and targeted extraction mode (filtering by device families and KPI settings) to
    facilitate brownfield infrastructure documentation, configuration backup, migration
    planning, and multi-site deployment standardization workflows.

    Key Capabilities:
    - Extracts device family KPI thresholds, overall health inclusion flags, and issue
      threshold synchronization settings from Catalyst Center
    - Executes multiple API calls with includeForOverallHealth parameter variations
      (both true and false) to ensure complete data extraction
    - Generates YAML files with comprehensive header comments including metadata,
      generation timestamp, configuration summary statistics, and usage instructions
    - Provides detailed operation summaries with success/failure statistics, device
      family categorization (complete success, partial success, complete failure),
      and comprehensive error reporting for troubleshooting
    - Supports legacy filter formats (global_filters) and modern nested filter
      structures (component_specific_filters) for backward compatibility
    - Transforms internal API KPI names to user-friendly format for improved
      playbook readability and maintainability

    Inheritance:
        DnacBase: Provides Cisco Catalyst Center API connectivity, authentication,
                  request execution, logging infrastructure, and common utility methods
        BrownFieldHelper: Provides parameter transformation utilities, reverse mapping
                         functions, and configuration processing helpers for brownfield
                         operations

    Class-Level Attributes:
        supported_states (list): List of supported Ansible states, currently ['gathered']
                                for configuration extraction workflow
        module_schema (dict): Network elements schema configuration mapping API families,
                             functions, filters, and reverse mapping specifications
        module_name (str): Target workflow manager module name for generated playbooks
                          ('assurance_device_health_score_settings_workflow_manager')
        operation_successes (list): Tracking list for successful KPI configuration
                                   retrievals with device family and threshold details
        operation_failures (list): Tracking list for failed operations with error
                                  information, error codes, and failure context
        total_device_families_processed (int): Counter for unique device families
                                              processed during retrieval operations
        total_kpis_processed (int): Counter for total KPI configurations processed
                                   across all device families
        generate_all_configurations (bool): Flag indicating auto-discovery mode enabling
                                           complete infrastructure extraction

    Workflow Execution:
        1. validate_input() - Validates playbook configuration parameters and filters
        2. get_want() - Constructs desired state parameters from validated configuration
        3. get_diff_gathered() - Orchestrates YAML generation workflow execution
        4. yaml_config_generator() - Generates YAML file with header and configurations
        5. get_device_health_score_settings() - Retrieves settings via API calls
        6. apply_health_score_filters() - Applies component-specific filtering
        7. write_dict_to_yaml() - Writes formatted YAML with header comments to file

    Notes:
        - The class is idempotent; multiple runs with same parameters generate identical
          YAML content (except generation timestamp in header comments)
        - Check mode is supported but does not perform actual file generation; validates
          parameters and returns expected operation results
        - Large-scale deployments with many device families may require increased
          dnac_api_task_timeout values for complete data extraction
        - Generated YAML files use OrderedDumper for consistent key ordering across
          multiple generations
        - Device family names are case-sensitive and must match exact names used in
          Catalyst Center (e.g., 'UNIFIED_AP' not 'unified_ap')
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
        self.module_name = "assurance_device_health_score_settings_workflow_manager"

        # Initialize class-level variables to track successes and failures
        self.operation_successes = []
        self.operation_failures = []
        self.total_device_families_processed = 0

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False

    def validate_input(self):
        """
        This function performs comprehensive validation of configuration parameters provided
        through the Ansible playbook, ensuring all required fields are present, parameter
        names are correct without typos, data types match expected specifications, and values
        conform to module schema requirements. Validates both top-level parameters and nested
        component-specific filters with detailed error reporting for invalid configurations.

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
            self.log(self.msg, "ERROR")
            return self

        self.log(
            "Configuration data available in playbook with {0} configuration item(s). "
            "Proceeding with parameter schema definition and validation workflow. "
            "Configuration structure will be validated against expected parameter "
            "specifications.".format(len(self.config)),
            "DEBUG"
        )

        # Expected schema for configuration parameters
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
            "component_specific_filters": {
                "type": "dict",
                "required": False
            },
            "global_filters": {
                "type": "dict",
                "required": False
            },
        }

        # Pre-validation: Check for invalid parameter names (typos)
        self.log(
            "Starting pre-validation stage to check for invalid parameter names and typos in "
            "playbook configuration. This early validation stage catches common errors like "
            "misspelled parameter names before detailed type and value validation. Allowed "
            "parameter names: {0}.".format(", ".join(sorted(temp_spec.keys()))),
            "DEBUG"
        )
        allowed_param_names = set(temp_spec.keys())
        self.log(
            "Extracted allowed parameter names set with {0} parameter(s): {1}. Iterating through "
            "{2} configuration item(s) to identify invalid parameter names not in allowed set.".format(
                len(allowed_param_names), sorted(allowed_param_names), len(self.config)
            ),
            "DEBUG"
        )
        for config_index, config_item in enumerate(self.config, start=1):
            if isinstance(config_item, dict):
                self.log(
                    "Pre-validating configuration item {0}/{1} for parameter name correctness. "
                    "Configuration item keys: {2}. Checking against allowed parameter names to "
                    "identify typos or invalid parameters.".format(
                        config_index, len(self.config), list(config_item.keys())
                    ),
                    "DEBUG"
                )
                invalid_params = set(config_item.keys()) - allowed_param_names
                if invalid_params:
                    self.msg = (
                        "Invalid parameters detected in playbook configuration item {0}/{1}: "
                        "{2}. These parameter names are not recognized by the module. Please "
                        "check for typos in parameter names. Allowed parameters are: {3}.".format(
                            config_index, len(self.config), sorted(invalid_params),
                            ", ".join(sorted(allowed_param_names))
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

        self.validate_minimum_requirements(self.config)
        self.log(
            "Minimum requirements validation completed. Configuration meets minimum parameter "
            "requirements for module operation. Proceeding to detailed parameter type and value "
            "validation using validate_list_of_dicts() function.",
            "DEBUG"
        )

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        self.log(
            "validate_list_of_dicts() execution completed. Validation result: valid_temp type={0}, "
            "invalid_params count={1}. Checking for validation failures requiring error handling "
            "and user notification.".format(
                type(valid_temp).__name__, len(invalid_params) if invalid_params else 0
            ),
            "DEBUG"
        )

        if invalid_params:
            allowed_params = sorted(temp_spec.keys())
            self.msg = (
                "Invalid parameters in playbook configuration: {0}. These parameters failed "
                "validation due to incorrect types, missing required fields, or invalid values. "
                "Allowed parameters are: {1}. Please verify parameter names are spelled correctly "
                "and check for typos in parameter names.".format(
                    invalid_params, ", ".join(allowed_params)
                )
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "All parameters passed detailed validation successfully. No type errors, missing "
            "required fields, or invalid values detected. Configuration conforms to module "
            "schema requirements and is ready for processing.",
            "INFO"
        )

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        self.log(
            "Input validation workflow completed successfully. Returning self instance for "
            "method chaining with check_return_status(). Instance contains validated_config "
            "ready for get_want() processing and operation execution.",
            "DEBUG"
        )
        return self

    def validate_component_specific_filters(self, component_specific_filters):
        """
        This function performs comprehensive validation of component_specific_filters
        configuration provided through playbook parameters, ensuring dictionary structure,
        validating parameter names against allowed options, checking components_list format
        and values, validating device_families parameter in both direct and nested formats,
        and verifying nested device_health_score_settings structure with detailed error
        reporting for configuration issues.

        Args:
            component_specific_filters (dict): Component filters configuration containing:
                - components_list (list, optional): List of component names to process
                - device_families (list, optional): Direct device families filter
                - device_health_score_settings (dict, optional): Nested filters with:
                - device_families (list, optional): Device families within settings

        Returns:
            bool: True if validation passes successfully, False if validation fails with
                operation result set to failed and error message logged.
        """
        self.log(
            "Starting validation of component_specific_filters structure and parameters. "
            "This validation ensures component_specific_filters is properly formatted as "
            "dictionary, contains only allowed parameter names, components_list contains "
            "valid component choices, and device_families parameters are properly structured "
            "in both direct and nested formats. Comprehensive error reporting provided for "
            "configuration issues.",
            "DEBUG"
        )
        if not isinstance(component_specific_filters, dict):
            self.msg = (
                "component_specific_filters must be a dictionary. Received type: {0}. "
                "Please provide component_specific_filters as dictionary structure with "
                "valid parameter keys and values conforming to module schema requirements."
            ).format(type(component_specific_filters).__name__)
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return False

        # Define allowed component filter parameters
        allowed_component_params = {
            'device_families',
            'components_list',
            'device_health_score_settings'
        }

        self.log(
            "Checking for invalid parameter names in component_specific_filters. Provided "
            "parameters: {0}. Comparing against allowed parameters to identify typos or "
            "unsupported configuration options.".format(
                ", ".join(sorted(component_specific_filters.keys()))
            ),
            "DEBUG"
        )

        # Check for invalid parameters
        invalid_params = set(component_specific_filters.keys()) - allowed_component_params
        if invalid_params:
            self.msg = (
                "Invalid component_specific_filters parameter(s) found: {0}. "
                "Allowed parameters are: {1}"
            ).format(
                ", ".join(sorted(invalid_params)),
                ", ".join(sorted(allowed_component_params))
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return False

        self.log(
            "component_specific_filters parameter name validation passed. All provided "
            "parameters are recognized and allowed by module schema. Proceeding with "
            "components_list validation if parameter is present.",
            "DEBUG"
        )

        # Validate components_list if provided
        if 'components_list' in component_specific_filters:
            self.log(
                "components_list parameter found in component_specific_filters. Starting "
                "validation of components_list structure and values. This parameter specifies "
                "which components to include in YAML configuration extraction.",
                "DEBUG"
            )
            components_list = component_specific_filters['components_list']
            self.log(
                "Validating components_list is list type. Type received: {0}. List type "
                "is required for components_list parameter.".format(
                    type(components_list).__name__
                ),
                "DEBUG"
            )
            if not isinstance(components_list, list):
                self.msg = (
                    "component_specific_filters.components_list must be a list. Received "
                    "type: {0}. Please provide components_list as list of component name "
                    "strings conforming to module schema requirements."
                ).format(type(components_list).__name__)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

            self.log(
                "components_list type validation passed. Proceeding with element type "
                "validation to ensure all list entries are strings. Total components: {0}.".format(
                    len(components_list)
                ),
                "DEBUG"
            )

            # Check if all elements are strings
            for component_index, component in enumerate(components_list, start=1):
                self.log(
                    "Validating component {0}/{1} in components_list. Component value: '{2}', "
                    "Type: {3}. String type is required for all components_list entries.".format(
                        component_index, len(components_list), component,
                        type(component).__name__
                    ),
                    "DEBUG"
                )
                if not isinstance(component, str):
                    self.msg = (
                        "All components_list entries must be strings. Component at index {0} "
                        "has invalid type: {1}. Component value: '{2}'. Please ensure all "
                        "components_list entries are string values."
                    ).format(
                        component_index - 1, type(component).__name__, component
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return False

                self.log(
                    "All components_list entries validated as string type successfully. Proceeding "
                    "with component name validation against allowed choices to ensure only supported "
                    "components are specified.",
                    "DEBUG"
                )

            # Validate component names against allowed choices
            valid_components = ["device_health_score_settings"]
            for component_index, component in enumerate(components_list, start=1):
                self.log(
                    "Validating component {0}/{1} against allowed choices. Component: '{2}'. "
                    "Checking if component is in valid_components list.".format(
                        component_index, len(components_list), component
                    ),
                    "DEBUG"
                )
                if component not in valid_components:
                    self.msg = (
                        "Invalid component '{0}' found in components_list at index {1}. "
                        "Supported components are: {2}. Please check your configuration and "
                        "use only valid component names. This component name is not recognized "
                        "by module schema for device health score settings operations."
                    ).format(component, component_index - 1, valid_components)
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                    return False

        self.log(
            "components_list validation completed successfully. All {0} component(s) are "
            "valid and supported by module schema. Components validated: {1}.".format(
                len(components_list), ", ".join(components_list)
            ),
            "DEBUG"
        )

        # Validate device_families if provided (direct usage)
        if 'device_families' in component_specific_filters:
            self.log(
                "device_families parameter found at top level of component_specific_filters. "
                "Starting validation of device_families parameter structure and values using "
                "validate_device_families_parameter() method. This represents direct device "
                "family filtering without nested structure.",
                "DEBUG"
            )
            if not self.validate_device_families_parameter(component_specific_filters['device_families']):
                self.log(
                    "device_families parameter validation failed. validate_device_families_parameter() "
                    "returned False indicating validation errors. Operation result already set "
                    "to failed with error details. Returning False to indicate validation failure.",
                    "ERROR"
                )
                return False

        self.log(
            "Direct device_families parameter validation passed successfully. Parameter "
            "structure and values conform to module schema requirements.",
            "DEBUG"
        )

        # Validate device_health_score_settings if provided (nested structure)
        if 'device_health_score_settings' in component_specific_filters:
            self.log(
                "device_health_score_settings parameter found in component_specific_filters. "
                "Starting validation of nested device_health_score_settings structure. This "
                "represents nested filtering configuration for device health score settings "
                "component with component-specific filter parameters.",
                "DEBUG"
            )
            device_health_score_settings = component_specific_filters['device_health_score_settings']
            if not isinstance(device_health_score_settings, dict):
                self.msg = (
                    "component_specific_filters.device_health_score_settings must be a "
                    "dictionary. Received type: {0}. Please provide device_health_score_settings "
                    "as dictionary structure with valid nested parameter keys and values."
                ).format(type(device_health_score_settings).__name__)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

            self.log(
                "device_health_score_settings dictionary type validation passed. Proceeding with "
                "nested parameter validation including device_families and other component-specific "
                "filter options.",
                "DEBUG"
            )
            # Validate device_families within device_health_score_settings
            if 'device_families' in device_health_score_settings:
                self.log(
                    "device_families parameter found within nested device_health_score_settings "
                    "structure. Starting validation using validate_device_families_parameter() "
                    "method to ensure proper list structure and string element types.",
                    "DEBUG"
                )
                if not self.validate_device_families_parameter(device_health_score_settings['device_families']):
                    if not self.validate_device_families_parameter(
                        device_health_score_settings['device_families']
                    ):
                        self.log(
                            "Nested device_families parameter validation failed. "
                            "validate_device_families_parameter() returned False. Operation result "
                            "already set to failed. Returning False to indicate validation failure.",
                            "ERROR"
                        )
                    return False

            self.log(
                "Nested device_families parameter validation passed successfully. Parameter "
                "structure and values within device_health_score_settings conform to schema.",
                "DEBUG"
            )

            # Check for invalid nested parameters
            allowed_nested_params = {'device_families'}
            self.log(
                "Allowed nested parameters within device_health_score_settings defined: {0}. "
                "Total allowed nested parameters: {1}. Checking for invalid or unrecognized "
                "parameter names in nested structure.".format(
                    ", ".join(sorted(allowed_nested_params)),
                    len(allowed_nested_params)
                ),
                "DEBUG"
            )
            invalid_nested_params = set(device_health_score_settings.keys()) - allowed_nested_params
            if invalid_nested_params:
                self.msg = (
                    "Invalid device_health_score_settings parameter(s) found: {0}. These "
                    "nested parameter names are not recognized within device_health_score_settings "
                    "structure. Allowed parameters are: {1}. Please check for typos and ensure "
                    "only supported nested parameters are used."
                ).format(
                    ", ".join(sorted(invalid_nested_params)),
                    ", ".join(sorted(allowed_nested_params))
                )
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False
            self.log(
                "device_health_score_settings nested parameter validation passed. All nested "
                "parameters are recognized and allowed by module schema.",
                "DEBUG"
            )

        self.log(
            "component_specific_filters validation completed successfully. All validation "
            "checks passed including dictionary type validation, parameter name validation, "
            "components_list validation, and device_families validation in both direct and "
            "nested formats. Configuration conforms to module schema requirements.",
            "INFO"
        )

        return True

    def validate_device_families_parameter(self, device_families):
        """
        This function performs validation of device_families parameter ensuring proper list
        structure and string element types for device family names used in filtering device
        health score settings configurations.
        Args:
            device_families: The device_families parameter to validate.
        Returns:
            bool: True if validation passes, False otherwise.
        """
        self.log(
            "Starting validation of device_families parameter structure and element types. "
            "This validation ensures device_families is properly formatted as list with string "
            "elements for device family name filtering in device health score settings retrieval.",
            "DEBUG"
        )
        if not isinstance(device_families, list):
            self.msg = (
                "device_families parameter must be a list. Received type: {0}. Please provide "
                "device_families as list of string device family names conforming to module "
                "schema requirements for device health score settings filtering."
            ).format(type(device_families).__name__)
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return False

        self.log(
            "device_families list type validation passed. Proceeding with element type validation "
            "to ensure all list entries are strings. Total device families: {0}.".format(
                len(device_families)
            ),
            "DEBUG"
        )

        # Check if all elements are strings
        for family_index, family in enumerate(device_families, start=1):
            self.log(
                "Validating device family {0}/{1} in device_families list. Family value: '{2}', "
                "Type: {3}. String type is required for all device_families entries.".format(
                    family_index, len(device_families), family, type(family).__name__
                ),
                "DEBUG"
            )
            if not isinstance(family, str):
                self.msg = (
                    "All device_families entries must be strings. Device family at index {0} "
                    "has invalid type: {1}. Family value: '{2}'. Please ensure all device_families "
                    "entries are string values representing valid device family names."
                ).format(family_index - 1, type(family).__name__, family)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

        self.log(
            "All device_families entries validated as string type successfully. Total {0} device "
            "families validated: {1}. Parameter structure conforms to module schema requirements.".format(
                len(device_families), ", ".join(device_families)
            ),
            "INFO"
        )

        self.log(
            "device_families parameter validation completed successfully. Returning True to "
            "indicate successful validation with proper list structure and string element types.",
            "DEBUG"
        )

        return True

    def get_workflow_elements_schema(self):
        """
        Constructs and returns workflow element schema configuration for device health
        score settings operations.

        This function defines the complete schema specification for device health score
        settings workflow manager operations including API configuration, filter
        specifications, reverse mapping functions, and operation functions. Provides
        centralized configuration mapping for network elements enabling consistent
        parameter validation, API execution, and data transformation throughout the
        module lifecycle.

        Returns:
            dict: Dictionary containing network_elements schema configuration with:
                - device_health_score_settings: Complete configuration including:
                    - filters: Parameter specifications for API filtering
                    - reverse_mapping_function: Function for API to user format transformation
                    - api_function: API method name for retrieving health score definitions
                    - api_family: SDK family name for API execution
                    - get_function_name: Method reference for retrieving configurations
        """
        self.log(
            "Constructing workflow elements schema configuration for device health score "
            "settings operations. This schema defines API configuration, filter specifications, "
            "reverse mapping functions, and operation functions enabling consistent parameter "
            "validation, API execution, and data transformation throughout module lifecycle.",
            "DEBUG"
        )  # Construct schema dictionary with network elements configuration
        schema_config = {
            "network_elements": {
                "device_health_score_settings": {
                    "filters": {
                        "device_families": {
                            "type": "list",
                            "required": False,
                            "elements": "str"
                        },
                    },
                    "reverse_mapping_function": (
                        self.device_health_score_settings_reverse_mapping_function
                    ),
                    "api_function": (
                        "get_all_health_score_definitions_for_given_filters"
                    ),
                    "api_family": "devices",
                    "get_function_name": self.get_device_health_score_settings,
                }
            }
        }

        self.log(
            "Returning workflow elements schema configuration for use in parameter validation, "
            "API execution, and data transformation operations throughout module workflow.",
            "DEBUG"
        )

        return schema_config

    def device_health_score_settings_reverse_mapping_function(self, requested_filters=None):
        """
        Returns reverse mapping specification for device health score settings.

        This function generates the reverse mapping specification used to transform API
        response data from Cisco Catalyst Center internal format to user-friendly format
        compatible with assurance_device_health_score_settings_workflow_manager module.
        Provides ordered dictionary structure defining transformation rules for device
        family, KPI names, thresholds, and health score settings parameters.

        Args:
            requested_filters (dict, optional): Dictionary of specific filters to apply
                                               during transformation. Currently not used
                                               but reserved for future filtering capabilities.

        Returns:
            dict: Ordered dictionary containing reverse mapping specifications with:
                  - device_health_score: List transformation rules including:
                    - device_family: Device family name mapping
                    - kpi_name: KPI name transformation with user-friendly names
                    - include_for_overall_health: Boolean flag for health inclusion
                    - threshold_value: Numeric threshold value
                    - synchronize_to_issue_threshold: Boolean sync flag
        """
        self.log(
            "Generating reverse mapping specification for transforming device health score "
            "settings from API response format to user-friendly format. Input filters: {0}. "
            "This specification defines transformation rules for device family, KPI names, "
            "thresholds, and health score parameters compatible with "
            "assurance_device_health_score_settings_workflow_manager module.".format(
                requested_filters
            ),
            "DEBUG"
        )
        return self.get_device_health_score_reverse_mapping_spec()

    def get_kpi_name_reverse_mapping(self):
        """
        Returns mapping from internal API names to user-friendly KPI names.

        This function provides reverse mapping specification transforming internal API KPI
        names (as returned by Catalyst Center) to user-friendly KPI names (as expected by
        assurance_device_health_score_settings_workflow_manager module). Maps technical
        threshold parameter names to human-readable KPI identifiers for consistent
        configuration management and playbook generation.

        Returns:
            dict: Dictionary mapping internal API KPI names to user-friendly names with:
                - Keys: Internal API threshold parameter names (e.g., 'cpuUtilizationThreshold')
                - Values: User-friendly KPI display names (e.g., 'CPU Utilization')
        """
        self.log(
            "Returning reverse KPI name mapping specification transforming internal API "
            "threshold names to user-friendly KPI names for playbook generation. Total "
            "mappings defined: 44 KPI names covering device health metrics.",
            "DEBUG"
        )

        return {
            "linkErrorThreshold": "Link Error",
            "rssiThreshold": "Connectivity RSSI",
            "snrThreshold": "Connectivity SNR",
            "rf_airQuality_2_4GThreshold": "Air Quality 2.4 GHz",
            "rf_airQuality_5GThreshold": "Air Quality 5 GHz",
            "rf_airQuality_6GThreshold": "Air Quality 6 GHz",
            "cpuUtilizationThreshold": "CPU Utilization",
            "rf_interference_2_4GThreshold": "Interference 2.4 GHz",
            "rf_interference_5GThreshold": "Interference 5 GHz",
            "rf_interference_6GThreshold": "Interference 6 GHz",
            "rf_noise_2_4GThreshold": "Noise 2.4 GHz",
            "rf_noise_5GThreshold": "Noise 5 GHz",
            "rf_noise_6GThreshold": "Noise 6 GHz",
            "rf_utilization_2_4GThreshold": "RF Utilization 2.4 GHz",
            "rf_utilization_5GThreshold": "RF Utilization 5 GHz",
            "rf_utilization_6GThreshold": "RF Utilization 6 GHz",
            "freeMbufThreshold": "Free Mbuf",
            "freeTimerThreshold": "Free Timer",
            "packetPool": "Packet Pool",
            "WQEPool": "WQE Pool",
            "aaaServerReachability": "AAA server reachability",
            "bgpBgpSiteThreshold": "BGP Session from Border to Control Plane (BGP)",
            "bgpPubsubSiteThreshold": "BGP Session from Border to Control Plane (PubSub)",
            "bgpPeerInfraVnThreshold": "BGP Session from Border to Peer Node for INFRA VN",
            "bgpPeerThreshold": "BGP Session from Border to Peer Node",
            "bgpTcpThreshold": "BGP Session from Border to Transit Control Plane",
            "bgpEvpnThreshold": "BGP Session to Spine",
            "ctsEnvDataThreshold": "Cisco TrustSec environment data download status",
            "fabricReachability": "Fabric Control Plane Reachability",
            "multicastRPReachability": "Fabric Multicast RP Reachability",
            "fpcLinkScoreThreshold": "Extended Node Connectivity",
            "infraLinkAvailabilityThreshold": "Inter-device Link Availability",
            "defaultRouteThreshold": "Internet Availability",
            "linkDiscardThreshold": "Link Discard",
            "linkUtilizationThreshold": "Link Utilization",
            "lispTransitConnScoreThreshold": "LISP Session from Border to Transit Site Control Plane",
            "lispCpConnScoreThreshold": "LISP Session Status",
            "memoryUtilizationThreshold": "Memory Utilization",
            "peerThreshold": "Peer Status",
            "pubsubTransitSessionScoreThreshold": "Pub-Sub Session from Border to Transit Site Control Plane",
            "pubsubInfraVNSessionScoreThreshold": "Pub-Sub Session Status for INFRA VN",
            "pubsubSessionThreshold": "Pub-Sub Session Status",
            "remoteRouteThreshold": "Remote Internet Availability",
            "vniStatusThreshold": "VNI Status",
            "fwConnThreshold": "Firewall Connection"
        }

    def transform_kpi_name(self, internal_kpi_name):
        """
        Transforms internal API KPI name to user-friendly display name.

        This function converts technical threshold parameter names from Catalyst Center
        API responses to human-readable KPI names for playbook generation and user
        presentation using reverse mapping specification.

        Args:
            internal_kpi_name (str): Internal API KPI name from Catalyst Center response
                                    (e.g., 'cpuUtilizationThreshold', 'rssiThreshold')

        Returns:
            str: User-friendly KPI display name (e.g., 'CPU Utilization', 'Connectivity RSSI')
                Returns original name if no mapping found.
        """
        self.log(
            "Transforming KPI name from internal API format to user-friendly format. "
            "Input KPI name: '{0}'. Retrieving reverse mapping specification.".format(
                internal_kpi_name
            ),
            "DEBUG"
        )
        kpi_mapping = self.get_kpi_name_reverse_mapping()
        user_friendly_name = kpi_mapping.get(internal_kpi_name, internal_kpi_name)
        self.log(
            "KPI name transformation completed. Internal name: '{0}' -> User-friendly name: "
            "'{1}'. Mapping found: {2}.".format(
                internal_kpi_name, user_friendly_name, internal_kpi_name in kpi_mapping
            ),
            "DEBUG"
        )
        return user_friendly_name

    def get_device_health_score_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for device health score settings.

        This function generates ordered dictionary structure defining transformation
        rules for converting API response format to user-friendly playbook format
        compatible with assurance_device_health_score_settings_workflow_manager module.
        Specifies field mappings, data types, source keys, and transformation functions
        for device family, KPI names, thresholds, and health score parameters.

        Returns:
            OrderedDict: Reverse mapping specification with:
                        - device_health_score: List transformation rules including:
                        - device_family: Device family name mapping
                        - kpi_name: KPI name with user-friendly transformation
                        - include_for_overall_health: Boolean flag mapping
                        - threshold_value: Numeric threshold mapping
                        - synchronize_to_issue_threshold: Boolean sync flag mapping
        """
        self.log(
            "Constructing reverse mapping specification for transforming device health "
            "score settings from API response format to user-friendly playbook format. "
            "Specification includes field mappings for device_family, kpi_name with "
            "transformation function, include_for_overall_health, threshold_value, and "
            "synchronize_to_issue_threshold parameters.",
            "DEBUG"
        )

        return OrderedDict({
            "device_health_score": {
                "type": "list",
                "elements": "dict",
                "source_key": "response",
                "options": OrderedDict({
                    "device_family": {
                        "type": "str",
                        "source_key":
                        "deviceFamily"
                    },
                    "kpi_name": {
                        "type": "str",
                        "source_key": "name",
                        "transform": self.transform_kpi_name
                    },
                    "include_for_overall_health": {
                        "type": "bool",
                        "source_key": "includeForOverallHealth"
                    },
                    "threshold_value": {
                        "type": "float",
                        "source_key": "thresholdValue"
                    },
                    "synchronize_to_issue_threshold": {
                        "type": "bool",
                        "source_key": "synchronizeToIssueThreshold"
                    }
                })
            }
        })

    def reset_operation_tracking(self):
        """
        Resets operation tracking variables for new operation session.

        This function initializes all operation tracking counters and lists to zero
        and empty states respectively, preparing the instance for a fresh operation
        tracking session for device health score settings retrieval and processing.

        Returns:
            None: Function performs state reset without return value.
        """
        self.log(
            "Resetting operation tracking variables to initial state. Setting "
            "operation_successes=[], operation_failures=[], "
            "total_device_families_processed=0, total_kpis_processed=0 for new "
            "operation session tracking.", "DEBUG"
        )
        self.operation_successes = []
        self.operation_failures = []
        self.total_device_families_processed = 0
        self.total_kpis_processed = 0
        self.log("Operation tracking variables reset successfully", "DEBUG")

    def add_success(self, device_family, kpi_name, additional_info=None):
        """
        Adds successful operation to tracking list for operation summary reporting.

        This function records a successful KPI configuration retrieval operation by
        creating a success entry with device family, KPI name, and optional additional
        information, then appending it to the operation successes tracking list for
        consolidated operation summary generation.

        Args:
            device_family (str): Device family name (e.g., 'UNIFIED_AP', 'ROUTER')
            kpi_name (str): User-friendly KPI name that succeeded (e.g., 'CPU Utilization')
            additional_info (dict, optional): Additional success details like threshold_value,
                                            include_for_overall_health flags

        Returns:
            None: Function performs tracking state update without return value.
        """
        self.log(
            "Recording successful operation for device family '{0}', KPI '{1}' with "
            "additional_info: {2}. Creating success entry for operation tracking.".format(
                device_family, kpi_name, additional_info
            ),
            "DEBUG"
        )
        success_entry = {
            "device_family": device_family,
            "kpi_name": kpi_name,
            "status": "success"
        }

        if additional_info:
            self.log("Adding additional information to success entry: {0}".format(additional_info), "DEBUG")
            success_entry.update(additional_info)

        self.operation_successes.append(success_entry)
        self.log(
            "Successfully recorded success entry for device family '{0}', KPI '{1}'. "
            "Total successful operations: {2}.".format(
                device_family, kpi_name, len(self.operation_successes)
            ),
            "DEBUG"
        )

    def add_failure(self, device_family, kpi_name, error_info):
        """
        Adds failed operation to tracking list for operation summary reporting.

        This function records a failed KPI configuration retrieval or processing operation
        by creating a failure entry with device family, KPI name, and error information,
        then appending it to the operation failures tracking list for consolidated error
        reporting and operation summary generation.

        Args:
            device_family (str): Device family name where failure occurred (e.g.,
                            'UNIFIED_AP', 'ROUTER')
            kpi_name (str): User-friendly KPI name that failed (e.g., 'CPU Utilization')
            error_info (dict): Error details containing error_type, error_message, and
                            error_code for failure analysis

        Returns:
            None: Function performs tracking state update without return value.
        """
        self.log(
            "Recording failed operation for device family '{0}', KPI '{1}' with error: "
            "{2}. Creating failure entry for operation tracking.".format(
                device_family, kpi_name, error_info.get("error_message", "Unknown error")
            ),
            "DEBUG"
        )
        failure_entry = {
            "device_family": device_family,
            "kpi_name": kpi_name,
            "status": "failed",
            "error_info": error_info
        }

        self.operation_failures.append(failure_entry)
        self.log(
            "Successfully recorded failure entry for device family '{0}', KPI '{1}': "
            "{2}. Total failed operations: {3}.".format(
                device_family, kpi_name,
                error_info.get("error_message", "Unknown error"),
                len(self.operation_failures)
            ),
            "ERROR"
        )

    def get_operation_summary(self):
        """
        Generates comprehensive summary of all operations performed during retrieval.

        This function compiles operation statistics from tracked successes and failures,
        categorizes device families by completion status, and generates consolidated
        summary report for operation result tracking and user feedback.

        Returns:
            dict: Operation summary containing:
                - total_device_families_processed: Count of unique device families
                - total_kpis_processed: Count of KPIs processed
                - total_successful_operations: Count of successful operations
                - total_failed_operations: Count of failed operations
                - device_families_with_complete_success: List of fully successful families
                - device_families_with_partial_success: List of partially successful families
                - device_families_with_complete_failure: List of completely failed families
                - success_details: List of all successful operation entries
                - failure_details: List of all failed operation entries
        """
        self.log(
            "Generating operation summary from tracked successes ({0} entries) and "
            "failures ({1} entries) for consolidated reporting.".format(
                len(self.operation_successes), len(self.operation_failures)
            ),
            "DEBUG"
        )

        unique_successful_families = set()
        unique_failed_families = set()

        self.log(
            "Extracting unique device families from {0} successful operation entries "
            "to identify families with at least one successful KPI configuration.".format(
                len(self.operation_successes)
            ),
            "DEBUG"
        )
        for success_index, success in enumerate(self.operation_successes, start=1):
            device_family = success["device_family"]
            unique_successful_families.add(device_family)

            self.log(
                "Processing success entry {0}/{1}: device_family='{2}', "
                "kpi_name='{3}', added to successful families set.".format(
                    success_index, len(self.operation_successes),
                    device_family, success.get("kpi_name")
                ),
                "DEBUG"
            )

        self.log(
            "Extracted {0} unique device families from successful operations: {1}.".format(
                len(unique_successful_families), sorted(unique_successful_families)
            ),
            "DEBUG"
        )

        self.log(
            "Extracting unique device families from {0} failed operation entries "
            "to identify families with at least one failed KPI configuration.".format(
                len(self.operation_failures)
            ),
            "DEBUG"
        )

        self.log("Processing failed operations to extract unique device family information", "DEBUG")
        for failure_index, failure in enumerate(self.operation_failures, start=1):
            device_family = failure["device_family"]
            unique_failed_families.add(device_family)

            self.log(
                "Processing failure entry {0}/{1}: device_family='{2}', "
                "kpi_name='{3}', error='{4}', added to failed families set.".format(
                    failure_index, len(self.operation_failures),
                    device_family, failure.get("kpi_name"),
                    failure.get("error_info", {}).get("error_message", "Unknown")
                ),
                "DEBUG"
            )

        self.log(
            "Extracted {0} unique device families from failed operations: {1}.".format(
                len(unique_failed_families), sorted(unique_failed_families)
            ),
            "DEBUG"
        )

        self.log(
            "Calculating device family categorization by analyzing success and "
            "failure patterns. Categories: partial success (both successes and "
            "failures), complete success (only successes), complete failure "
            "(only failures).",
            "DEBUG"
        )

        self.log("Calculating device family categorization based on success and failure patterns", "DEBUG")
        partial_success_families = unique_successful_families.intersection(unique_failed_families)
        self.log(
            "Identified {0} device families with partial success (both successful "
            "and failed operations): {1}. These families have mixed results with "
            "some KPIs succeeding and others failing.".format(
                len(partial_success_families), sorted(partial_success_families)
            ),
            "DEBUG"
        )

        complete_success_families = unique_successful_families - unique_failed_families
        self.log(
            "Identified {0} device families with complete success (only successful "
            "operations): {1}. These families have all KPI configurations retrieved "
            "successfully without any failures.".format(
                len(complete_success_families), sorted(complete_success_families)
            ),
            "DEBUG"
        )

        complete_failure_families = unique_failed_families - unique_successful_families
        self.log(
            "Identified {0} device families with complete failure (only failed "
            "operations): {1}. These families have all KPI configuration retrievals "
            "failed without any successes.".format(
                len(complete_failure_families), sorted(complete_failure_families)
            ),
            "DEBUG"
        )

        total_families = len(
            unique_successful_families.union(unique_failed_families)
        )

        self.log(
            "Constructing consolidated operation summary dictionary with statistics "
            "and categorization results. Total unique device families processed: {0}.".format(
                total_families
            ),
            "DEBUG"
        )

        summary = {
            "total_device_families_processed": total_families,
            "total_kpis_processed": self.total_kpis_processed,
            "total_successful_operations": len(self.operation_successes),
            "total_failed_operations": len(self.operation_failures),
            "device_families_with_complete_success": list(complete_success_families),
            "device_families_with_partial_success": list(partial_success_families),
            "device_families_with_complete_failure": list(complete_failure_families),
            "success_details": self.operation_successes,
            "failure_details": self.operation_failures
        }

        self.log(
            "Operation summary generated successfully. Statistics: Total families={0}, "
            "Total KPIs={1}, Successful operations={2}, Failed operations={3}, "
            "Complete success families={4}, Partial success families={5}, "
            "Complete failure families={6}.".format(
                summary["total_device_families_processed"],
                summary["total_kpis_processed"],
                summary["total_successful_operations"],
                summary["total_failed_operations"],
                len(summary["device_families_with_complete_success"]),
                len(summary["device_families_with_partial_success"]),
                len(summary["device_families_with_complete_failure"])
            ),
            "INFO"
        )

        return summary

    def get_device_health_score_settings(self, network_element, filters):
        """
        Retrieves device health score settings from Cisco Catalyst Center.

        This function orchestrates complete device health score settings retrieval by
        executing API calls with includeForOverallHealth parameter variations, processing
        device family filters, applying reverse mapping transformations, and tracking
        operation statistics for comprehensive configuration extraction.

        Args:
            network_element (dict): Network element configuration containing:
                                - api_family: SDK family name for API execution
                                - api_function: API method name for health score retrieval
                                - reverse_mapping_function: Function for data transformation
            filters (dict): Filters containing component_specific_filters with:
                        - device_health_score_settings.device_families: List of families
                        - components_list: List of components to process

        Returns:
            dict: Dictionary containing:
                - device_health_score_settings: List of transformed health score configs
                - operation_summary: Statistics with successes, failures, and metrics
        """
        self.log(
            "Starting device health score settings retrieval from Catalyst Center. "
            "Network element API family: {0}, API function: {1}. Applied filters: {2}. "
            "This operation will execute API calls with includeForOverallHealth variations "
            "to retrieve complete KPI configuration data.".format(
                network_element.get("api_family"), network_element.get("api_function"),
                filters
            ),
            "INFO"
        )

        self.log("Resetting operation tracking for new retrieval session", "DEBUG")
        self.reset_operation_tracking()

        # Extract API configuration
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log("API family: {0}, API function: {1}".format(api_family, api_function), "DEBUG")

        # Prepare API parameters
        api_params = {}
        component_specific_filters = filters.get("component_specific_filters", {})

        # Support both global_filters and component_specific_filters structures
        device_families = []

        # Check for nested device_health_score_settings structure
        health_score_filters = component_specific_filters.get("device_health_score_settings", {})
        if health_score_filters.get("device_families"):
            device_families = health_score_filters["device_families"]
            self.log(
                "Found {0} device families in device_health_score_settings filters: {1}. "
                "Will execute separate API calls for each device family.".format(
                    len(device_families), device_families
                ),
                "DEBUG"
            )
        # Check for components_list - if only components_list is present without device_families
        components_list = component_specific_filters.get("components_list", [])
        if "device_health_score_settings" in components_list:
            if not device_families:
                self.log(
                    "components_list contains device_health_score_settings without "
                    "device families filter. Will retrieve all device families from "
                    "Catalyst Center.",
                    "DEBUG"
                )
            else:
                self.log(
                    "components_list contains device_health_score_settings with {0} "
                    "device families: {1}.".format(
                        len(device_families), device_families
                    ),
                    "DEBUG"
                )

        try:
            # Collect all response data from multiple API calls
            all_response_data = []

            # Determine if device families are specified
            has_device_families = bool(device_families)

            # Define includeForOverallHealth variations to ensure complete data extraction
            include_variations = [True, False]
            self.log(
                "Starting API calls with {0} includeForOverallHealth variations to "
                "ensure complete KPI data extraction. Variations: {1}.".format(
                    len(include_variations), include_variations
                ),
                "DEBUG"
            )

            # Loop through includeForOverallHealth values with enumerate
            for include_index, include_for_overall_health in enumerate(
                include_variations, start=1
            ):
                self.log(
                    "Processing includeForOverallHealth variation {0}/{1}: value={2}. "
                    "This variation retrieves KPIs with includeForOverallHealth={2}.".format(
                        include_index, len(include_variations), include_for_overall_health
                    ),
                    "DEBUG"
                )
                self.log("Processing includeForOverallHealth: {0}".format(include_for_overall_health), "DEBUG")

                if has_device_families:
                    self.log(
                        "Device families filter active with {0} families. Starting "
                        "individual API calls for each device family with "
                        "includeForOverallHealth={1}.".format(
                            len(device_families), include_for_overall_health
                        ),
                        "DEBUG"
                    )
                    # If device families are specified, make API calls for each device family
                    # Make API calls for each device family with enumerate
                    for family_index, device_family in enumerate(
                        device_families, start=1
                    ):
                        self.log(
                            "Executing API call for device family {0}/{1}: '{2}' with "
                            "includeForOverallHealth={3} (variation {4}/{5}). Preparing "
                            "API parameters for targeted retrieval.".format(
                                family_index, len(device_families), device_family,
                                include_for_overall_health, include_index,
                                len(include_variations)
                            ),
                            "DEBUG"
                        )
                        api_params = {
                            "deviceType": device_family,
                            "includeForOverallHealth": include_for_overall_health,
                        }

                        self.log(
                            "API parameters for device family '{0}': {1}. Executing "
                            "GET request to {2}.{3}().".format(
                                device_family, api_params, api_family, api_function
                            ),
                            "DEBUG"
                        )
                        response = self.execute_get_request(api_family, api_function, api_params)
                        self.log(
                            "API response received for device family '{0}' ({1}/{2}). "
                            "Response status: {3}.".format(
                                device_family, family_index, len(device_families),
                                "success" if response else "no_data"
                            ),
                            "DEBUG"
                        )

                        if response and response.get("response"):
                            response_data = response.get("response", [])
                            all_response_data.extend(response_data)
                            self.log(
                                "Successfully retrieved {0} KPI configurations for "
                                "device family '{1}' with includeForOverallHealth={2}. "
                                "Total collected: {3} items.".format(
                                    len(response_data), device_family,
                                    include_for_overall_health,
                                    len(all_response_data)
                                ),
                                "DEBUG"
                            )
                        else:
                            self.log(
                                "No data returned for device family '{0}' with "
                                "includeForOverallHealth={1}.".format(
                                    device_family, include_for_overall_health
                                ),
                                "DEBUG"
                            )
                else:
                    # If no device families specified, make API call without deviceType filter
                    self.log(
                        "No device families filter specified. Executing single API call "
                        "without deviceType filter to retrieve all device families with "
                        "includeForOverallHealth={0} (variation {1}/{2}).".format(
                            include_for_overall_health, include_index,
                            len(include_variations)
                        ),
                        "DEBUG"
                    )

                    api_params = {
                        "includeForOverallHealth": include_for_overall_health,
                    }

                    self.log(
                        "API parameters for global retrieval: {0}. Executing GET "
                        "request.".format(api_params),
                        "DEBUG"
                    )
                    response = self.execute_get_request(api_family, api_function, api_params)

                    if response and response.get("response"):
                        response_data = response.get("response", [])
                        all_response_data.extend(response_data)
                        self.log(
                            "Successfully retrieved {0} KPI configurations with "
                            "includeForOverallHealth={1}. Total collected: {2} items.".format(
                                len(response_data), include_for_overall_health,
                                len(all_response_data)
                            ),
                            "DEBUG"
                        )

            self.log(
                "API retrieval completed. Total response data collected: {0} KPI "
                "configurations across all API calls.".format(len(all_response_data)),
                "INFO"
            )

            # Log first few items for debugging
            if all_response_data and len(all_response_data) > 0:
                self.log(
                    "Sample KPI configuration item: {0}".format(all_response_data[0]),
                    "DEBUG"
                )
            self.log("Processing {0} health score definitions from API".format(len(all_response_data)), "DEBUG")

            # Update response_data to use collected data
            response_data = all_response_data

            # Since API returns filtered data based on parameters, no additional filtering needed
            self.log("Using API response data directly: {0} health score settings".format(len(response_data)), "DEBUG")

            if response_data:
                self.log(
                    "Processing {0} health score definitions for statistics tracking "
                    "and reverse mapping transformation.".format(len(response_data)),
                    "DEBUG"
                )
                # Track statistics and process KPI configurations
                device_families = set()
                self.log(
                    "Starting KPI configuration processing loop for {0} items.".format(
                        len(response_data)
                    ),
                    "DEBUG"
                )

                for kpi_index, item in enumerate(response_data, start=1):
                    device_family = item.get("deviceFamily")
                    device_families.add(device_family)

                    # Get user-friendly KPI name for tracking
                    kpi_internal_name = item.get("name")
                    kpi_user_name = self.get_kpi_name_reverse_mapping().get(
                        kpi_internal_name, kpi_internal_name
                    )

                    self.log(
                        "Processing KPI {0}/{1}: device_family='{2}', "
                        "kpi_name='{3}' (internal: '{4}'), threshold={5}, "
                        "include_for_overall_health={6}.".format(
                            kpi_index, len(response_data), device_family,
                            kpi_user_name, kpi_internal_name,
                            item.get("thresholdValue"),
                            item.get("includeForOverallHealth")
                        ),
                        "DEBUG"
                    )

                    self.add_success(
                        device_family,
                        kpi_user_name,
                        {
                            "threshold_value": item.get("thresholdValue"),
                            "include_for_overall_health": item.get(
                                "includeForOverallHealth"
                            )
                        }
                    )

                self.total_device_families_processed = len(device_families)
                self.total_kpis_processed = len(response_data)
                self.log(
                    "Statistics tracking completed. Unique device families: {0}, "
                    "Total KPIs: {1}.".format(
                        self.total_device_families_processed,
                        self.total_kpis_processed
                    ),
                    "INFO"
                )

                # Apply reverse mapping
                reverse_mapping_function = network_element.get("reverse_mapping_function")
                reverse_mapping_spec = reverse_mapping_function()

                self.log(
                    "Applying reverse mapping to transform {0} API responses to "
                    "user-friendly format using modify_parameters().".format(
                        len(response_data)
                    ),
                    "DEBUG"
                )
                transformed_data = self.modify_parameters(
                    reverse_mapping_spec,
                    [{"response": response_data}]
                )

                # Extract the device_health_score list from the transformed data
                device_health_score_list = []
                if transformed_data and len(transformed_data) > 0:
                    device_health_score_list = transformed_data[0].get("device_health_score", [])

                self.log(
                    "Reverse mapping transformation completed. Generated {0} "
                    "device health score configurations.".format(
                        len(device_health_score_list)
                    ),
                    "INFO"
                )
                final_result = {
                    "device_health_score_settings": device_health_score_list,
                    "operation_summary": self.get_operation_summary()
                }

                self.log(
                    "Device health score settings retrieval completed successfully. "
                    "Total configurations: {0}, Device families: {1}.".format(
                        len(device_health_score_list),
                        self.total_device_families_processed
                    ),
                    "INFO"
                )
                return final_result

            else:
                self.log(
                    "No health score settings found in API responses after {0} API "
                    "calls. Returning empty result.".format(
                        len(include_variations) *
                        (len(device_families) if has_device_families else 1)
                    ),
                    "WARNING"
                )
        except Exception as e:
            error_msg = (
                "Exception occurred during device health score settings retrieval: "
                "{0}. Exception type: {1}.".format(str(e), type(e).__name__)
            )
            self.log(error_msg, "ERROR")
            self.add_failure("UNKNOWN", "UNKNOWN", {
                "error_type": "exception",
                "error_message": error_msg,
                "error_code": "API_EXCEPTION_ERROR"
            })

        return {
            "device_health_score_settings": [],
            "operation_summary": self.get_operation_summary()
        }

    def apply_health_score_filters(self, response_data, component_specific_filters):
        """
        Applies component-specific filters to device health score settings data.

        This function filters raw API response data based on component-specific filter
        criteria including device families and KPI names, supporting both global_filters
        and nested device_health_score_settings filter structures for backward
        compatibility.

        Args:
            response_data (list): Raw response data from API containing health score
                                definitions with deviceFamily, kpiName, and other fields
            component_specific_filters (dict): Component-specific filters containing:
                                            - global_filters.device_families: Legacy
                                                device family list
                                            - device_health_score_settings.device_families:
                                                Nested device family list
                                            - device_health_score_settings.kpi_names: KPI
                                                name filter list
                                            - components_list: List of components to
                                                process

        Returns:
            list: Filtered device health score settings data matching filter criteria,
                empty list if no data matches or input is empty.
        """
        self.log(
            "Starting device health score settings filtering with {0} input items and "
            "filters: {1}. Filtering extracts configurations matching specified device "
            "families and KPI names from API response data.".format(
                len(response_data) if response_data else 0, component_specific_filters
            ),
            "DEBUG"
        )

        if not response_data:
            self.log(
                "No response data provided for filtering. Returning empty list without "
                "applying filters.",
                "DEBUG"
            )
            return []

        filtered_data = response_data[:]
        original_count = len(filtered_data)
        self.log(
            "Extracting device families filter from multiple possible filter structures "
            "(global_filters, device_health_score_settings, components_list) for backward "
            "compatibility support.",
            "DEBUG"
        )

        # Support both global_filters and component_specific_filters structures
        device_families = []

        # Check for global_filters structure
        global_filters = component_specific_filters.get("global_filters", {})
        if global_filters.get("device_families"):
            device_families = global_filters["device_families"]
            self.log(
                "Found {0} device families in legacy global_filters structure: {1}. "
                "Using for filtering criteria.".format(
                    len(device_families), device_families
                ),
                "DEBUG"
            )

        # Check for nested device_health_score_settings structure
        health_score_filters = component_specific_filters.get("device_health_score_settings", {})
        if not device_families and health_score_filters.get("device_families"):
            device_families = health_score_filters["device_families"]
            self.log(
                "Found {0} device families in nested device_health_score_settings "
                "structure: {1}. Using for filtering criteria.".format(
                    len(device_families), device_families
                ),
                "DEBUG"
            )

        # Check for components_list - if present, get all device families
        components_list = component_specific_filters.get("components_list", [])
        if "device_health_score_settings" in components_list and not device_families:
            self.log(
                "components_list contains device_health_score_settings without device "
                "families filter. Skipping device family filtering to retrieve all "
                "available families.",
                "DEBUG"
            )

        self.log(
            "Final device families filter determined: {0}. Filter will be applied: {1}.".format(
                device_families if device_families else "None (all families)",
                bool(device_families)
            ),
            "DEBUG"
        )
        if device_families:
            self.log(
                "Applying device families filter to {0} items. Filtering for families: "
                "{1}. Items not matching will be excluded.".format(
                    len(filtered_data), device_families
                ),
                "DEBUG"
            )
            filtered_data = [
                item for item in filtered_data
                if item.get("deviceFamily") in device_families
            ]
            self.log(
                "Device families filter applied successfully. Items before filter: {0}, "
                "after filter: {1}, items removed: {2}.".format(
                    original_count, len(filtered_data), original_count - len(filtered_data)
                ),
                "DEBUG"
            )

        # Apply KPI names filter
        self.log(
            "Extracting KPI names filter from health_score_filters or top-level "
            "component_specific_filters for KPI-level filtering.",
            "DEBUG"
        )
        kpi_names = health_score_filters.get("kpi_names", component_specific_filters.get("kpi_names", []))
        if kpi_names:
            self.log(
                "Applying KPI names filter to {0} items. Filtering for KPI names: {1}. "
                "Items not matching will be excluded.".format(
                    len(filtered_data), kpi_names
                ),
                "DEBUG"
            )
            pre_kpi_count = len(filtered_data)
            filtered_data = [
                item for item in filtered_data
                if item.get("kpiName") in kpi_names
            ]
            self.log(
                "KPI names filter applied successfully. Items before filter: {0}, "
                "after filter: {1}, items removed: {2}.".format(
                    pre_kpi_count, len(filtered_data), pre_kpi_count - len(filtered_data)
                ),
                "DEBUG"
            )
        else:
            self.log(
                "No KPI names filter specified. Skipping KPI-level filtering. All KPIs "
                "for matching device families will be included.",
                "DEBUG"
            )

        self.log(
            "Health score settings filtering completed successfully. Final result: {0} "
            "items from original {1} items. Filters applied: device_families={2}, "
            "kpi_names={3}.".format(
                len(filtered_data), original_count, bool(device_families), bool(kpi_names)
            ),
            "INFO"
        )
        return filtered_data

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates YAML configuration file for device health score settings.

        This function orchestrates the complete YAML generation workflow including file path
        determination, filter processing, configuration retrieval from Catalyst Center,
        data transformation using reverse mapping specifications, operation summary
        consolidation, and YAML file generation with comprehensive header comments.
        Supports auto-discovery mode and targeted filtering with detailed error handling.

        Args:
            yaml_config_generator (dict): Configuration parameters containing:
                                         - file_path (str, optional): Output file path
                                         - generate_all_configurations (bool, optional): Auto-discovery mode
                                         - component_specific_filters (dict, optional): Targeted extraction
                                         - global_filters (dict, optional): Legacy filter
                                           format support

        Returns:
            object: Self instance with updated attributes:
                   - self.msg: Operation result message with file path and statistics
                   - self.status: Operation status ("success", "failed", or "ok")
                   - Operation result set via set_operation_result()
        """
        self.log(
            "Starting YAML configuration generation workflow with parameters: {0}. "
            "Workflow orchestrates file path determination, filter processing, "
            "configuration retrieval, operation summary consolidation, and YAML file "
            "generation with header comments.".format(yaml_config_generator),
            "DEBUG"
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        self.log(
            "Auto-discovery mode evaluation: generate_all_configurations={0}. When "
            "enabled, overrides all filters to retrieve complete device health score "
            "settings inventory from Catalyst Center for brownfield documentation.".format(
                generate_all
            ),
            "DEBUG"
        )
        if generate_all:
            self.log(
                "Auto-discovery mode enabled. Will process all device health score "
                "settings without filtering restrictions for complete infrastructure "
                "discovery and documentation.",
                "INFO"
            )

        self.log(
            "Determining output file path for YAML configuration. Checking if user "
            "provided file_path parameter in playbook configuration.",
            "DEBUG"
        )
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No file_path provided in playbook configuration. Generating default "
                "filename with module name and timestamp for unique identification.",
                "DEBUG"
            )
            file_path = self.generate_filename()
            self.log(
                "Generated default filename: {0}. File will be created in current "
                "working directory.".format(file_path),
                "DEBUG"
            )
        else:
            self.log(
                "Using user-provided file_path: {0}. Path may be absolute or relative "
                "to current working directory.".format(file_path),
                "DEBUG"
            )

        self.log(
            "YAML configuration output file path determined: {0}. Path will be used "
            "for writing final configuration with header comments.".format(file_path),
            "INFO"
        )

        if generate_all:
            self.log(
                "Auto-discovery mode active. Overriding any user-provided filters to "
                "retrieve all device health score settings from Catalyst Center. "
                "component_specific_filters will be set to empty dictionary.",
                "INFO"
            )
            component_specific_filters = {}
        else:
            self.log(
                "Standard mode active. Processing user-provided filters for targeted "
                "device health score settings retrieval. Checking component_specific_filters "
                "and global_filters parameters.",
                "DEBUG"
            )

            component_specific_filters = (
                yaml_config_generator.get("component_specific_filters") or {}
            )

            # Support legacy global_filters structure
            global_filters = yaml_config_generator.get("global_filters")

            if global_filters and not component_specific_filters:
                self.log(
                    "Found global_filters parameter without component_specific_filters. "
                    "Using legacy filter structure for backward compatibility support. "
                    "global_filters: {0}".format(global_filters),
                    "DEBUG"
                )
                component_specific_filters = {"global_filters": global_filters}

            self.log(
                "Component specific filters determined: {0}. Filters will be applied "
                "during device health score settings retrieval for targeted configuration "
                "extraction.".format(component_specific_filters),
                "DEBUG"
            )

        self.log(
            "Retrieving supported network elements schema configuration from module "
            "schema definition. Schema contains API configuration, filter specifications, "
            "and reverse mapping functions for each component.",
            "DEBUG"
        )
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        self.log(
            "Initializing final configuration list and consolidated operation summary "
            "tracking structures. These structures will accumulate configurations and "
            "statistics from all processed components.",
            "DEBUG"
        )
        final_list = []
        consolidated_operation_summary = {
            "total_device_families_processed": 0,
            "total_kpis_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "device_families_with_complete_success": [],
            "device_families_with_partial_success": [],
            "device_families_with_complete_failure": [],
            "success_details": [],
            "failure_details": []
        }

        self.log(
            "Tracking structures initialized successfully. final_list=[], "
            "consolidated_operation_summary with zero counters ready for accumulation.",
            "DEBUG"
        )

        # Process device health score settings
        component = "device_health_score_settings"
        self.log(
            "Starting processing for component: {0}. Retrieving network element "
            "configuration from module schema for API execution and data transformation.".format(
                component
            ),
            "INFO"
        )
        network_element = module_supported_network_elements.get(component)

        if network_element:
            self.log(
                "Network element configuration found for component {0}. Configuration "
                "includes api_family={1}, api_function={2}, and reverse mapping function. "
                "Preparing component-specific filter structure.".format(
                    component,
                    network_element.get("api_family"),
                    network_element.get("api_function")
                ),
                "DEBUG"
            )

            # Prepare component filters structure
            self.log(
                "Constructing component filter structure with component_specific_filters "
                "for API execution. Structure format: {{'component_specific_filters': "
                "{0}}}.".format(component_specific_filters),
                "DEBUG"
            )
            # Pass the component_specific_filters directly to match the expected structure
            component_filters = {
                "component_specific_filters": component_specific_filters
            }

            self.log("Executing component operation function to retrieve details", "DEBUG")
            operation_func = network_element.get("get_function_name")
            details = operation_func(network_element, component_filters)
            self.log(
                "Component operation function execution completed for {0}. Retrieved "
                "configurations count: {1}, operation_summary available: {2}.".format(
                    component,
                    len(details.get("device_health_score_settings", [])),
                    bool(details.get("operation_summary"))
                ),
                "INFO"
            )

            # Process retrieved configurations
            if details and details.get("device_health_score_settings"):
                config_count = len(details["device_health_score_settings"])

                self.log(
                    "Adding {0} device health score configurations from component {1} "
                    "to final list. Configurations include device_family, kpi_name, "
                    "threshold_value, and other settings.".format(
                        config_count, component
                    ),
                    "DEBUG"
                )

                final_list.extend(details["device_health_score_settings"])

                self.log(
                    "Successfully added configurations to final list. Total configurations "
                    "in final_list: {0}.".format(len(final_list)),
                    "DEBUG"
                )
            else:
                self.log(
                    "No device_health_score_settings configurations found in component "
                    "operation response for {0}. final_list remains unchanged.".format(
                        component
                    ),
                    "WARNING"
                )

            # Consolidate operation summary
            if details and details.get("operation_summary"):
                self.log(
                    "Consolidating operation summary from component {0} response. "
                    "Summary includes success/failure statistics and device family "
                    "categorization for comprehensive reporting.".format(component),
                    "DEBUG"
                )
                summary = details["operation_summary"]
                consolidated_operation_summary.update(summary)
                self.log(
                    "Operation summary consolidated successfully. Statistics: "
                    "total_device_families_processed={0}, total_kpis_processed={1}, "
                    "total_successful_operations={2}, total_failed_operations={3}.".format(
                        consolidated_operation_summary["total_device_families_processed"],
                        consolidated_operation_summary["total_kpis_processed"],
                        consolidated_operation_summary["total_successful_operations"],
                        consolidated_operation_summary["total_failed_operations"]
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "No operation_summary available in component response for {0}. "
                    "Consolidated summary retains initial zero values.".format(component),
                    "DEBUG"
                )
        else:
            self.log(
                "Network element configuration not found for component {0} in module "
                "schema. Component will be skipped in processing workflow.".format(
                    component
                ),
                "ERROR"
            )

        self.log(
            "Creating final dictionary structure for YAML output. Structure follows "
            "assurance_device_health_score_settings_workflow_manager expected format "
            "with config list containing device_health_score configurations.",
            "DEBUG"
        )
        final_dict = OrderedDict()

        # Format the configuration properly according to the required structure
        # Changed to match expected format: config: - device_health_score: [list]
        if final_list:
            self.log(
                "Formatting {0} configurations into expected YAML structure: config -> "
                "list with device_health_score key. Structure matches module input "
                "requirements.".format(len(final_list)),
                "DEBUG"
            )
            final_dict["config"] = [{"device_health_score": final_list}]
        else:
            self.log(
                "No configurations available in final_list. Creating empty YAML "
                "structure: config -> list with empty device_health_score array.",
                "WARNING"
            )
            final_dict["config"] = [{"device_health_score": []}]

        if not final_list:
            self.log(
                "No configurations found to process after component retrieval. Setting "
                "appropriate result message indicating no data available for specified "
                "filters or auto-discovery mode.",
                "WARNING"
            )

            self.msg = {
                "message": (
                    "No configurations or components to process for module '{0}'. "
                    "Verify input filters or configuration.".format(self.module_name)
                ),
                "file_path": file_path,
                "operation_summary": consolidated_operation_summary
            }

            self.log(
                "Setting operation result to 'ok' status for empty configuration "
                "scenario. Result message: {0}".format(self.msg["message"]),
                "INFO"
            )

            self.set_operation_result("ok", False, self.msg, "INFO")
            return self
        else:
            self.log(
                "YAML file write operation failed. Unable to write configuration to "
                "file path: {0}. Check file permissions, directory existence, and disk "
                "space availability.".format(file_path),
                "ERROR"
            )

            self.msg = {
                "message": (
                    "YAML config generation failed for module '{0}' - unable to write "
                    "to file.".format(self.module_name)
                ),
                "file_path": file_path,
                "operation_summary": consolidated_operation_summary
            }

            self.log(
                "Setting operation result to 'failed' with changed=True due to file "
                "write failure. Message: {0}".format(self.msg["message"]),
                "ERROR"
            )

            self.set_operation_result("failed", True, self.msg, "ERROR")

        self.log(
            "Final dictionary structure created successfully with {0} total "
            "configurations. Dictionary ready for YAML serialization with header "
            "comments.".format(len(final_list)),
            "INFO"
        )

        # Determine if operation should be considered failed based on partial or complete failures
        has_partial_failures = len(consolidated_operation_summary["device_families_with_partial_success"]) > 0
        has_complete_failures = len(consolidated_operation_summary["device_families_with_complete_failure"]) > 0
        has_any_failures = consolidated_operation_summary["total_failed_operations"] > 0

        self.log(
            "Evaluating operation status for failure detection. Partial failures: {0}, "
            "Complete failures: {1}, Total failed operations: {2}. Status determination "
            "will affect final result reporting.".format(
                has_partial_failures, has_complete_failures,
                consolidated_operation_summary["total_failed_operations"]
            ),
            "DEBUG"
        )

        # Write YAML file with header
        self.log(
            "Initiating YAML file write operation to path: {0}. Operation includes "
            "header comment generation with metadata and configuration summary, followed "
            "by YAML serialization of final_dict structure.".format(file_path),
            "INFO"
        )

        self.log("Attempting to write final dictionary to YAML file", "DEBUG")
        if self.write_dict_to_yaml(final_dict, file_path):
            self.log(
                "YAML file write operation completed successfully. File created at: {0} "
                "with {1} configurations and header comments.".format(
                    file_path, len(final_list)
                ),
                "INFO"
            )
            self.log(
                "YAML file write operation completed successfully. File created at: {0} "
                "with {1} configurations and header comments.".format(
                    file_path, len(final_list)
                ),
                "INFO"
            )

            # Determine final operation status
            if has_partial_failures or has_complete_failures or has_any_failures:
                self.log(
                    "Operation contains failures detected. Setting final status to "
                    "'failed' for comprehensive error reporting. Partial failures: {0}, "
                    "Complete failures: {1}, Total failures: {2}.".format(
                        has_partial_failures, has_complete_failures, has_any_failures
                    ),
                    "WARNING"
                )

                self.msg = {
                    "message": (
                        "YAML config generation completed with failures for module "
                        "'{0}'. Check operation_summary for details.".format(
                            self.module_name
                        )
                    ),
                    "file_path": file_path,
                    "configurations_generated": len(final_list),
                    "operation_summary": consolidated_operation_summary
                }

                self.log(
                    "Setting operation result to 'failed' with changed=True. Message: "
                    "{0}. Users should review operation_summary for failure details.".format(
                        self.msg["message"]
                    ),
                    "ERROR"
                )
                self.set_operation_result("failed", True, self.msg, "ERROR")
            else:
                self.log(
                    "Setting operation result to 'success' with changed=True. Generated "
                    "YAML file contains {0} configurations at {1}.".format(
                        len(final_list), file_path
                    ),
                    "INFO"
                )
                self.msg = {
                    "message": "YAML config generation succeeded for module '{0}'.".format(self.module_name),
                    "file_path": file_path,
                    "configurations_generated": len(final_list),
                    "operation_summary": consolidated_operation_summary
                }
                self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.log(
                "Operation completed successfully without failures. All {0} device "
                "families processed successfully with {1} total KPI configurations.".format(
                    consolidated_operation_summary["total_device_families_processed"],
                    consolidated_operation_summary["total_kpis_processed"]
                ),
                "INFO"
            )

            self.msg = {
                "message": (
                    "YAML config generation succeeded for module '{0}'.".format(
                        self.module_name
                    )
                ),
                "file_path": file_path,
                "configurations_generated": len(final_list),
                "operation_summary": consolidated_operation_summary
            }

            self.log(
                "Setting operation result to 'success' with changed=True. Generated "
                "YAML file contains {0} configurations at {1}.".format(
                    len(final_list), file_path
                ),
                "INFO"
            )
            self.set_operation_result("failed", True, self.msg, "ERROR")

        self.log(
            "YAML configuration generation workflow completed. Final status: {0}, "
            "Configurations generated: {1}, File path: {2}.".format(
                "success" if not (has_partial_failures or has_complete_failures or
                                  has_any_failures) and len(final_list) > 0 else "failed",
                len(final_list), file_path
            ),
            "INFO"
        )
        return self

    def get_want(self, config, state):
        """
        Prepares API call parameters based on playbook configuration and state.

        This function validates playbook configuration parameters, processes
        component-specific filters, sets auto-discovery mode flags, and constructs
        the want dictionary containing yaml_config_generator parameters for
        downstream YAML generation operations in the gathered state workflow.

        Args:
            config (dict): Playbook configuration containing:
                        - generate_all_configurations (bool, optional): Auto-discovery
                            mode flag
                        - file_path (str, optional): Output YAML file path
                        - component_specific_filters (dict, optional): Filtering
                            criteria for device families and KPI settings
            state (str): Desired state for module operation, only 'gathered'
                        supported for configuration extraction

        Returns:
            object: Self instance with updated attributes:
                - self.want: Dictionary with yaml_config_generator parameters
                - self.msg: Operation result message
                - self.status: Operation status ("success" or "failed")
        """

        self.log(
            "Preparing API call parameters for state '{0}' with configuration: {1}. "
            "Workflow validates component filters, sets auto-discovery mode, and "
            "constructs want dictionary for YAML generation operations.".format(
                state, config
            ),
            "INFO"
        )

        self.log(
            "Validating playbook configuration parameters to ensure component-specific "
            "filters conform to schema requirements and contain valid parameter names, "
            "types, and values.",
            "DEBUG"
        )
        self.validate_params(config)

        self.log(
            "Extracting component_specific_filters from configuration for validation. "
            "Filters determine which device families and KPI settings to extract.",
            "DEBUG"
        )
        component_filters = config.get("component_specific_filters")

        if component_filters:
            if not self.validate_component_specific_filters(component_filters):
                self.log(
                    "Component-specific filters validation failed. Invalid filter "
                    "structure or parameters detected. Setting operation result to "
                    "failed and returning early.",
                    "ERROR"
                )
                self.set_operation_result(
                    "failed",
                    False,
                    "Invalid component_specific_filters provided.",
                    "ERROR",
                )
                return self

            self.log(
                "Component-specific filters validation passed successfully. Filters "
                "conform to schema requirements with valid structure and parameters.",
                "DEBUG"
            )
        else:
            self.log(
                "No component_specific_filters provided in configuration. Will use "
                "default behavior or auto-discovery mode if enabled.",
                "DEBUG"
            )

        # Set generate_all_configurations after validation
        self.generate_all_configurations = config.get("generate_all_configurations", False)
        # Set generate_all_configurations mode after validation
        generate_all = config.get("generate_all_configurations", False)

        self.log(
            "Setting auto-discovery mode flag from configuration. "
            "generate_all_configurations={0}. When enabled, overrides all filters to "
            "retrieve complete device health score settings inventory.".format(
                generate_all
            ),
            "DEBUG"
        )

        self.generate_all_configurations = generate_all

        self.log(
            "Auto-discovery mode configured: {0}. Class-level flag set for access by "
            "downstream YAML generation workflow functions.".format(
                self.generate_all_configurations
            ),
            "INFO"
        )

        self.log(
            "Constructing want dictionary with yaml_config_generator parameters. "
            "Dictionary contains complete configuration for YAML generation including "
            "file path, filters, and auto-discovery mode settings.",
            "DEBUG"
        )
        self.log("Set generate_all_configurations mode: {0}".format(self.generate_all_configurations), "DEBUG")

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config

        self.log(
            "yaml_config_generator parameters added to want dictionary: {0}. "
            "Parameters include generate_all_configurations={1}, file_path={2}, "
            "component_specific_filters={3}.".format(
                want["yaml_config_generator"],
                config.get("generate_all_configurations", False),
                config.get("file_path", "default"),
                bool(config.get("component_specific_filters"))
            ),
            "DEBUG"
        )

        self.want = want
        self.log(
            "Want dictionary constructed successfully with complete configuration "
            "parameters ready for get_diff_gathered workflow execution. Desired state: "
            "{0}".format(str(self.want)),
            "INFO"
        )

        self.msg = (
            "Successfully collected all parameters from playbook for Assurance Device "
            "Health Score Settings operations. Configuration validated and want "
            "dictionary prepared for YAML generation workflow."
        )
        self.status = "success"

        self.log(
            "Parameter preparation completed successfully. Operation status: {0}, "
            "Message: {1}. Returning self instance for method chaining.".format(
                self.status, self.msg
            ),
            "INFO"
        )

        return self

    def generate_filename(self):
        """
        Generates default filename with module name and timestamp for YAML output.

        This function creates a timestamped filename following the pattern
        module_name_playbook_YYYY-MM-DD_HH-MM-SS.yml for unique identification
        when file_path is not provided in playbook configuration.

        Returns:
            str: Generated filename with format
                assurance_device_health_score_settings_workflow_manager_playbook_2026-01-24_12-33-20.yml
        """
        self.log(
            "Generating default filename for YAML configuration file. Using module "
            "name '{0}' and current timestamp for unique identification.".format(
                self.module_name
            ),
            "DEBUG"
        )
        import datetime
        timestamp = datetime.datetime.now()
        self.log(
            "Current timestamp captured: {0}. Formatting as YYYY-MM-DD_HH-MM-SS for "
            "filename component.".format(timestamp.strftime("%Y-%m-%d %H:%M:%S")),
            "DEBUG"
        )
        filename = "{0}_playbook_{1}.yml".format(
            self.module_name,
            timestamp.strftime("%Y-%m-%d_%H-%M-%S")
        )
        self.log(
            "Default filename generated successfully: {0}. File will be created in "
            "current working directory if no custom path provided.".format(filename),
            "INFO"
        )
        return filename

    def generate_playbook_header(self, data_dict):
        """
        Generates header comments for YAML playbook file with metadata and summary.

        This function creates comprehensive header comments including generation timestamp,
        source system information, configuration summary statistics, device family counts,
        KPI metrics, and usage instructions for the generated YAML playbook file compatible
        with assurance_device_health_score_settings_workflow_manager module.

        Args:
            data_dict (dict): Configuration dictionary containing:
                            - config: List with device_health_score configurations
                            including device_family, kpi_name, threshold_value, and
                            other health score settings

        Returns:
            str: Multi-line header comment string formatted for YAML file with metadata,
                statistics, and usage instructions separated by decorative borders.
        """
        self.log(
            "Generating playbook header comments with metadata and configuration summary. "
            "Header includes generation timestamp, source system details, device family "
            "statistics, KPI counts, and usage instructions for workflow manager module.",
            "DEBUG"
        )
        import datetime

        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log(
            "Current timestamp captured for header: {0}. Timestamp identifies when "
            "configuration was extracted from Catalyst Center.".format(timestamp),
            "DEBUG"
        )

        self.log(
            "Analyzing configuration dictionary to calculate summary statistics. "
            "Extracting device_health_score list from config structure for device family "
            "and KPI counting.",
            "DEBUG"
        )

        # Calculate summary information
        device_health_score_list = []
        if data_dict.get("config"):
            self.log(
                "Processing {0} config items to extract device_health_score configurations.".format(
                    len(data_dict["config"])
                ),
                "DEBUG"
            )

            for config_index, config_item in enumerate(data_dict["config"], start=1):
                if config_item.get("device_health_score"):
                    device_health_score_list = config_item["device_health_score"]
                    self.log(
                        "Found device_health_score list at config item {0}/{1} with {2} "
                        "configurations.".format(
                            config_index, len(data_dict["config"]),
                            len(device_health_score_list)
                        ),
                        "DEBUG"
                    )
                    break

        total_configurations = len(device_health_score_list)
        self.log(
            "Total configurations counted: {0}. Starting device family and KPI name "
            "extraction for summary statistics.".format(total_configurations),
            "DEBUG"
        )
        device_families = set()
        kpi_names = set()

        for config in device_health_score_list:
            self.log(
                "Iterating through {0} configurations to extract unique device families and "
                "KPI names for summary header.".format(total_configurations),
                "DEBUG"
            )

            for config_index, config in enumerate(device_health_score_list, start=1):
                device_family = config.get("device_family")
                kpi_name = config.get("kpi_name")

                if device_family:
                    device_families.add(device_family)

                if kpi_name:
                    kpi_names.add(kpi_name)

                if config_index % 10 == 0 or config_index == total_configurations:
                    self.log(
                        "Processed {0}/{1} configurations. Current unique families: {2}, "
                        "unique KPIs: {3}.".format(
                            config_index, total_configurations, len(device_families),
                            len(kpi_names)
                        ),
                        "DEBUG"
                    )

        self.log(
            "Configuration analysis completed. Unique device families: {0} ({1}), "
            "Unique KPIs: {2}.".format(
                len(device_families), sorted(device_families), len(kpi_names)
            ),
            "DEBUG"
        )

        self.log(
            "Extracting DNAC host information from module parameters for header metadata. "
            "Checking multiple parameter sources (self.params, self.dnac_host, "
            "self.module.params).",
            "DEBUG"
        )

        # Get DNAC host information
        dnac_host = 'Unknown'
        if hasattr(self, 'params') and self.params:
            dnac_host = self.params.get('dnac_host', 'Unknown')
            self.log(
                "DNAC host extracted from self.params: {0}".format(dnac_host),
                "DEBUG"
            )
        elif hasattr(self, 'dnac_host'):
            dnac_host = self.dnac_host
            self.log(
                "DNAC host extracted from self.dnac_host: {0}".format(dnac_host),
                "DEBUG"
            )
        elif hasattr(self, 'module') and self.module and hasattr(
            self.module, 'params'
        ):
            dnac_host = self.module.params.get('dnac_host', 'Unknown')
            self.log(
                "DNAC host extracted from self.module.params: {0}".format(dnac_host),
                "DEBUG"
            )

        self.log(
            "DNAC host information determined: {0}. Building header comment lines with "
            "metadata, summary statistics, and usage instructions.".format(dnac_host),
            "DEBUG"
        )

        # Build header comments
        header_lines = [
            "# " + "=" * 80,
            "# Cisco Catalyst Center - Device Health Score Settings Configuration",
            "# " + "=" * 80,
            "#",
            "# Generated by: Cisco DNA Center Ansible Collection",
            "# Source: Cisco Catalyst Center (CatC)",
            "# DNAC Host: {0}".format(dnac_host),
            "# Generated on: {0}".format(timestamp),
            "#",
            "# Configuration Summary:",
            "#   Total KPI Configurations: {0}".format(total_configurations),
            "#   Device Families: {0}".format(", ".join(sorted(device_families)) if device_families else "None"),
            "#   Unique KPIs: {0}".format(len(kpi_names)),
            "#",
            "# This playbook contains device health score settings extracted from",
            "# Cisco Catalyst Center and can be used with the",
            "# cisco.dnac.assurance_device_health_score_settings_workflow_manager module",
            "# to apply the same configurations to other Catalyst Center instances.",
            "#",
            "# " + "=" * 80,
            ""
        ]
        self.log("Header comment lines constructed successfully with {0} lines including "
                 "borders, metadata, summary (Total KPIs: {1}, Families: {2}, Unique KPIs: {3}), "
                 "and usage instructions.".format(
                     len(header_lines), total_configurations, len(device_families),
                     len(kpi_names)
                 ),
                 "INFO"
                 )

        header_string = "\n".join(header_lines)

        self.log(
            "Playbook header generated successfully with {0} characters. Header ready "
            "for YAML file writing.".format(len(header_string)),
            "DEBUG"
        )

        return "\n".join(header_lines)

    def write_dict_to_yaml(self, data_dict, file_path):
        """
        Writes dictionary to YAML file with header comments and proper formatting.

        This function creates directory structure if needed, generates comprehensive
        header comments with metadata and statistics, serializes dictionary data to
        YAML format using OrderedDumper for consistent key ordering, and handles file
        write operations with comprehensive error handling and logging.

        Args:
            data_dict (dict): Configuration dictionary containing:
                            - config: List with device_health_score configurations
                            including device_family, kpi_name, threshold_value, and
                            other health score settings for YAML serialization
            file_path (str): Absolute or relative path where YAML file should be saved,
                            including filename with .yml extension

        Returns:
            bool: True if file write operation succeeds with header and data written
                successfully, False if any exception occurs during directory creation,
                header generation, or YAML serialization with error logged.
        """
        self.log(
            "Starting YAML file write operation to path: {0}. Operation includes "
            "directory creation if needed, header comment generation with metadata, "
            "and YAML serialization with OrderedDumper for consistent formatting.".format(
                file_path
            ),
            "DEBUG"
        )
        try:
            self.log(
                "Extracting directory path from file_path: {0}. Checking if directory "
                "structure exists or needs creation for file write operation.".format(
                    file_path
                ),
                "DEBUG"
            )
            # Create directory if it doesn't exist
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                self.log(
                    "Directory path does not exist: {0}. Creating directory structure "
                    "recursively using os.makedirs() to enable file write.".format(
                        directory
                    ),
                    "DEBUG"
                )
                os.makedirs(directory)
                self.log(
                    "Successfully created directory structure: {0}. Directory ready for "
                    "YAML file write operation.".format(directory),
                    "DEBUG"
                )
            else:
                self.log(
                    "Directory path exists or file_path is in current directory: {0}. "
                    "Proceeding with file write operation without directory creation.".format(
                        directory if directory else "current directory"
                    ),
                    "DEBUG"
                )

            self.log(
                "Opening file for write operation: {0}. File will be created or "
                "overwritten with generated header comments and YAML content.".format(
                    file_path
                ),
                "DEBUG"
            )

            with open(file_path, 'w') as yaml_file:
                self.log(
                    "File opened successfully for writing. Generating playbook header "
                    "comments with timestamp, source system details, configuration "
                    "summary, and usage instructions using generate_playbook_header().",
                    "DEBUG"
                )
                # Write header comments
                header = self.generate_playbook_header(data_dict)
                self.log(
                    "Playbook header generated successfully with {0} characters. Writing "
                    "header comments to file before YAML content for documentation and "
                    "context.".format(len(header)),
                    "DEBUG"
                )
                yaml_file.write(header)
                self.log(
                    "Header comments written successfully to file. Proceeding with YAML "
                    "serialization of configuration dictionary. Checking YAML library "
                    "availability and OrderedDumper support for consistent key ordering.",
                    "DEBUG"
                )

                # Write YAML content
                if HAS_YAML and OrderedDumper:
                    self.log(
                        "YAML library and OrderedDumper available. Using OrderedDumper "
                        "for YAML serialization to maintain consistent key ordering in "
                        "output file with default_flow_style=False and indent=2.",
                        "DEBUG"
                    )
                    yaml.dump(data_dict, yaml_file, Dumper=OrderedDumper,
                              default_flow_style=False, indent=2)
                else:
                    self.log(
                        "OrderedDumper not available. Using standard YAML dumper for "
                        "serialization with default_flow_style=False and indent=2. Key "
                        "ordering may vary from expected format.",
                        "WARNING"
                    )
                    yaml.dump(data_dict, yaml_file, default_flow_style=False, indent=2)
                    self.log(
                        "YAML content serialized and written to file successfully. Dictionary "
                        "data converted to YAML format with proper indentation and structure.",
                        "DEBUG"
                    )

            self.log(
                "YAML file write operation completed successfully. File created at: {0} "
                "with header comments and {1} configuration(s). File ready for use with "
                "assurance_device_health_score_settings_workflow_manager module.".format(
                    file_path,
                    len(data_dict.get("config", [{}])[0].get("device_health_score", []))
                ),
                "INFO"
            )
            return True
        except Exception as e:
            self.log(
                "Exception occurred during YAML file write operation: {0}. Exception "
                "type: {1}. Failed to write configuration to file path: {2}. Check "
                "file permissions, directory existence, disk space, and path validity.".format(
                    str(e), type(e).__name__, file_path
                ),
                "ERROR"
            )

            self.log(
                "YAML file write operation failed. Returning False to indicate failure. "
                "User should verify file path, permissions, and system resources before "
                "retrying operation.",
                "ERROR"
            )
            self.log("Failed to write YAML file: {0}".format(str(e)), "ERROR")
            return False

    def get_diff_gathered(self):
        """
        Executes YAML configuration generation workflow for gathered state.

        This function orchestrates the complete YAML playbook generation workflow by
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
            "Workflow execution start time captured: {0}. Timing metrics will track "
            "complete operation duration from parameter checking through YAML file "
            "generation for performance analysis and optimization.".format(
                start_time
            ),
            "DEBUG"
        )

        self.log(
            "Defining operations list for gathered state workflow. Operations include "
            "yaml_config_generator with parameter key, display name, and function "
            "reference for iteration and execution.",
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
            "Operations list defined successfully with {0} operation(s). Starting "
            "iteration through operations to execute YAML generation workflow with "
            "parameter validation and status checking.".format(len(operations)),
            "DEBUG"
        )
        for operation_index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                "Processing operation {0}/{1}: '{2}' with parameter key '{3}'. "
                "Checking want dictionary for operation parameters to determine if "
                "execution should proceed or skip this operation.".format(
                    operation_index, len(operations), operation_name, param_key
                ),
                "DEBUG"
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Operation {0}/{1} '{2}' parameters found in want dictionary: {3}. "
                    "Starting operation execution with parameter validation and status "
                    "checking for error propagation. Parameters will be passed to "
                    "{4}() function.".format(
                        operation_index, len(operations), operation_name,
                        bool(params), operation_func.__name__
                    ),
                    "INFO"
                )

                self.log(
                    "Executing operation function {0}() with parameters. Function will "
                    "perform YAML generation workflow including file path determination, "
                    "configuration retrieval, data transformation, and file writing. "
                    "check_return_status() will validate operation completion.".format(
                        operation_func.__name__
                    ),
                    "DEBUG"
                )
                operation_func(params).check_return_status()
                self.log(
                    "Operation {0}/{1} '{2}' completed successfully. check_return_status() "
                    "validation passed without errors. Operation result available in "
                    "self.result for final module output.".format(
                        operation_index, len(operations), operation_name
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "Operation {0}/{1} '{2}' skipped - no parameters found in want "
                    "dictionary for parameter key '{3}'. This operation will not execute "
                    "in current workflow iteration.".format(
                        operation_index, len(operations), operation_name, param_key
                    ),
                    "WARNING"
                )

        end_time = time.time()
        execution_duration = end_time - start_time

        self.log(
            "Gathered state workflow execution completed successfully. Total execution "
            "time: {0:.2f} seconds. Workflow processed {1} operation(s) with parameter "
            "validation, operation execution, and status checking for YAML playbook "
            "generation.".format(
                execution_duration, len(operations)
            ),
            "INFO"
        )

        self.log(
            "Performance metrics - Start time: {0}, End time: {1}, Duration: {2:.2f}s. "
            "Metrics provide timing analysis for workflow optimization and performance "
            "monitoring across different infrastructure scales.".format(
                start_time, end_time, execution_duration
            ),
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
    Main entry point for the Cisco Catalyst Center brownfield device health score settings playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield device health score settings extraction.

    Purpose:
        Initializes and executes the brownfield device health score settings playbook generator
        workflow to extract existing device health score configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create AssuranceDeviceHealthScorePlaybookGenerator instance
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
        - Introduced APIs for device health score settings retrieval:
            * get_all_health_score_definitions_for_given_filters

    Supported States:
        - gathered: Extract existing device health score settings and generate YAML playbook
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

    # Initialize the AssuranceDeviceHealthScorePlaybookGenerator object
    # This creates the main orchestrator for brownfield device health score settings extraction
    ccc_brownfield_assurance_device_health_score_settings = AssuranceDeviceHealthScorePlaybookGenerator(
        module)

    # Log module initialization after object creation (now logging is available)
    ccc_brownfield_assurance_device_health_score_settings.log(
        "Starting Ansible module execution for brownfield device health score settings playbook "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_brownfield_assurance_device_health_score_settings.log(
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
    ccc_brownfield_assurance_device_health_score_settings.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.7.9 for device health score settings APIs".format(
            ccc_brownfield_assurance_device_health_score_settings.get_ccc_version()
        ),
        "INFO"
    )

    if (ccc_brownfield_assurance_device_health_score_settings.compare_dnac_versions(
            ccc_brownfield_assurance_device_health_score_settings.get_ccc_version(), "2.3.7.9") < 0):

        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for Device Health Score Settings module. Supported versions start "
            "from '2.3.7.9' onwards. Version '2.3.7.9' introduces APIs for retrieving "
            "device health score settings including KPI thresholds, overall health "
            "inclusion flags, and issue threshold synchronization settings from "
            "the Catalyst Center.".format(
                ccc_brownfield_assurance_device_health_score_settings.get_ccc_version()
            )
        )

        ccc_brownfield_assurance_device_health_score_settings.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_brownfield_assurance_device_health_score_settings.msg = error_msg
        ccc_brownfield_assurance_device_health_score_settings.set_operation_result(
            "failed", False, ccc_brownfield_assurance_device_health_score_settings.msg, "ERROR"
        ).check_return_status()

    ccc_brownfield_assurance_device_health_score_settings.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required device health score settings APIs".format(
            ccc_brownfield_assurance_device_health_score_settings.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_brownfield_assurance_device_health_score_settings.params.get("state")

    ccc_brownfield_assurance_device_health_score_settings.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_brownfield_assurance_device_health_score_settings.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_brownfield_assurance_device_health_score_settings.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_brownfield_assurance_device_health_score_settings.supported_states
            )
        )

        ccc_brownfield_assurance_device_health_score_settings.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_brownfield_assurance_device_health_score_settings.status = "invalid"
        ccc_brownfield_assurance_device_health_score_settings.msg = error_msg
        ccc_brownfield_assurance_device_health_score_settings.check_return_status()

    ccc_brownfield_assurance_device_health_score_settings.log(
        "State validation passed - using state '{0}' for workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_brownfield_assurance_device_health_score_settings.log(
        "Starting comprehensive input parameter validation for playbook configuration",
        "INFO"
    )

    ccc_brownfield_assurance_device_health_score_settings.validate_input().check_return_status()

    ccc_brownfield_assurance_device_health_score_settings.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = ccc_brownfield_assurance_device_health_score_settings.validated_config

    ccc_brownfield_assurance_device_health_score_settings.log(
        "Starting configuration processing loop - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        ccc_brownfield_assurance_device_health_score_settings.log(
            "Processing configuration item {0}/{1} for state '{2}'".format(
                config_index, len(config_list), state
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_brownfield_assurance_device_health_score_settings.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_brownfield_assurance_device_health_score_settings.reset_values()

        # Collect desired state (want) from configuration
        ccc_brownfield_assurance_device_health_score_settings.log(
            "Collecting desired state parameters from configuration item {0}".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_brownfield_assurance_device_health_score_settings.get_want(
            config, state
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_brownfield_assurance_device_health_score_settings.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1}".format(state, config_index),
            "INFO"
        )
        ccc_brownfield_assurance_device_health_score_settings.get_diff_state_apply[state](
        ).check_return_status()

        ccc_brownfield_assurance_device_health_score_settings.log(
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

    ccc_brownfield_assurance_device_health_score_settings.log(
        "Module execution completed successfully at timestamp {0}. Total execution "
        "time: {1:.2f} seconds. Processed {2} configuration item(s) with final "
        "status: {3}".format(
            completion_timestamp,
            module_duration,
            len(config_list),
            ccc_brownfield_assurance_device_health_score_settings.status
        ),
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_brownfield_assurance_device_health_score_settings.log(
        "Exiting Ansible module with result: {0}".format(
            ccc_brownfield_assurance_device_health_score_settings.result
        ),
        "DEBUG"
    )

    module.exit_json(**ccc_brownfield_assurance_device_health_score_settings.result)


if __name__ == "__main__":
    main()

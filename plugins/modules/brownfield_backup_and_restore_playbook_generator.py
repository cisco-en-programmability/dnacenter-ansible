#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module for generating backup and restore configuration playbooks
from Cisco Catalyst Center.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Priyadharshini B, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_backup_and_restore_playbook_generator
short_description: Generate YAML playbook for 'backup_and_restore_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the
    backup_and_restore_workflow_manager module, reducing manual playbook
    creation effort and enabling programmatic modifications.
  - Represents NFS server configurations and backup storage configurations
    for backup and restore operations on Cisco Catalyst Center.
  - Supports extraction of NFS configurations, backup storage configurations
    with encryption and retention policies.
  - Generated YAML format is directly usable with
    backup_and_restore_workflow_manager module for infrastructure as code.

version_added: 6.44.0
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Priyadharshini B (@pbalaku2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
      - Desired state of Cisco Catalyst Center after module execution.
      - Only gathered state is supported for extracting configurations.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
      - A list of filters for generating YAML playbook compatible with the `backup_and_restore_workflow_manager`
        module.
      - Filters specify which components to include in the YAML configuration file.
      - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name  "<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
          - For example, "backup_and_restore_workflow_manager_playbook_2026-01-27_14-21-41.yml".
          - Supports both absolute and relative paths.
        type: str
      generate_all_configurations:
        description:
          - Generate YAML configuration for all available backup and restore components.
          - When set to true, generates configuration for both NFS configurations and backup storage configurations.
          - Takes precedence over component_specific_filters if both are specified.
          - If set to true and no component_specific_filters are provided, defaults to including all components.
        type: bool
        default: false
      component_specific_filters:
        description:
          - Filters to specify which components to include in the YAML configuration
            file.
          - If "components_list" is specified, only those components are included,
            regardless of other filters.
          - Ignored when generate_all_configurations is set to true.
        type: dict
        suboptions:
          components_list:
            description:
              - List of components to include in the YAML configuration file.
              - Valid values are
                - NFS Configuration "nfs_configuration"
                - Backup Storage Configuration "backup_storage_configuration"
              - If not specified, all components are included.
              - Supports multiple filter entries for filtering multiple
                NFS servers.
            type: list
            elements: str
            choices: ['nfs_configuration', 'backup_storage_configuration']
          nfs_configuration:
            description:
              - NFS configuration details to filter NFS servers.
              - Both server_ip and source_path must be provided together for filtering.
              - If not specified, all NFS configurations are included.
            type: list
            elements: dict
            suboptions:
              server_ip:
                description:
                  - Server IP address of the NFS server.
                  - Must be provided along with source_path for filtering.
                  - Used for exact match filtering of NFS configurations.
                type: str
                required: true
              source_path:
                description:
                  - Source path on the NFS server.
                  - Must be provided along with server_ip for filtering.
                  - Used for exact match filtering of NFS configurations.
                type: str
                required: true
          backup_storage_configuration:
            description:
              - Backup storage configuration filtering options by server type only.
              - If not specified, all backup storage configurations are included.
              - Only server_type filtering is supported for backup storage.
              - Other filter parameters like mount_path or retention_period
                are not supported.
            type: list
            elements: dict
            suboptions:
              server_type:
                description:
                  - Server type for filtering backup configurations.
                  - NFS type represents network-based backup storage.
                  - PHYSICAL_DISK type represents local disk backup storage.
                type: str
                choices: ['NFS', 'PHYSICAL_DISK']

requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
- SDK Methods used are
  - backup.Backup.get_all_n_f_s_configurations
  - backup.Backup.get_backup_configuration
- Paths used are
  - GET /dna/system/api/v1/backupNfsConfigurations
  - GET /dna/system/api/v1/backupConfiguration

- Requires Cisco Catalyst Center version 3.1.3.0 or higher
- Only supports gathered state for extracting existing configurations
- NFS filtering requires both server_ip and source_path together
- Backup storage filtering only supports server_type parameter
- Generated YAML file format is compatible with
  backup_and_restore_workflow_manager module
- File path supports both absolute and relative paths
- Default filename includes timestamp for uniqueness
- NFS details correlation matches backup mount paths with NFS
  destination paths automatically
- Empty configurations return success with idempotent behavior
- Module does not modify Catalyst Center configuration

seealso:
- module: cisco.dnac.backup_and_restore_workflow_manager
  description: Module to manage backup and restore NFS configurations in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with both NFS and backup storage configurations
  cisco.dnac.brownfield_backup_and_restore_playbook_generator:
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
      - file_path: "/tmp/catc_backup_restore_config.yaml"
        component_specific_filters:
          components_list:
            - "nfs_configuration"
            - "backup_storage_configuration"

- name: Generate YAML for NFS-type backup storage only filtering by server_type
  cisco.dnac.brownfield_backup_and_restore_playbook_generator:
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
      - file_path: "/tmp/catc_backup_storage_config.yaml"
        component_specific_filters:
          components_list: ["backup_storage_configuration"]
          backup_storage_configuration:
            - server_type: "NFS"

- name: Generate YAML for specific NFS server using exact match on server_ip and source_path
  cisco.dnac.brownfield_backup_and_restore_playbook_generator:
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
      - file_path: "/tmp/catc_specific_nfs_config.yaml"
        component_specific_filters:
          components_list: ["nfs_configuration"]
          nfs_configuration:
            - server_ip: "172.27.17.90"
              source_path: "/home/nfsshare/backups/TB30"

- name: Generate YAML for all configurations without filtering useful for complete system documentation
  cisco.dnac.brownfield_backup_and_restore_playbook_generator:
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
      - file_path: "/tmp/catc_backup_restore_config.yaml"
        generate_all_configurations: true

- name: Generate YAML Configuration for multiple NFS servers (each must have both server_ip and source_path)
  cisco.dnac.brownfield_backup_and_restore_playbook_generator:
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
      - file_path: "/tmp/catc_multiple_nfs_config.yaml"
        component_specific_filters:
          components_list: ["nfs_configuration"]
          nfs_configuration:
            - server_ip: "172.27.17.90"
              source_path: "/home/nfsshare/backups/TB30"
            - server_ip: "172.27.17.91"
              source_path: "/home/nfsshare/backups/TB31"

- name: Generate YAML Configuration for Physical Disk backup storage only
  cisco.dnac.brownfield_backup_and_restore_playbook_generator:
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
      - file_path: "/tmp/catc_physical_disk_backup.yaml"
        component_specific_filters:
          components_list: ["backup_storage_configuration"]
          backup_storage_configuration:
            - server_type: "NFS"
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: |
    Response from YAML configuration generation operation with execution
    statistics and status information.
  returned: always
  type: dict
  contains:
    msg:
      description: Status message describing operation outcome
      returned: always
      type: str
      sample: |
        YAML configuration file generated successfully for module
        backup_and_restore_workflow_manager
    response:
      description: Detailed operation results and statistics
      returned: always
      type: dict
      contains:
        components_processed:
          description: Number of components successfully retrieved
          returned: always
          type: int
          sample: 2
        components_skipped:
          description: |
            Number of components skipped due to errors or no data
            available
          returned: always
          type: int
          sample: 0
        configurations_count:
          description: Total configuration items across all components
          returned: always
          type: int
          sample: 5
        file_path:
          description: Absolute path to generated YAML file
          returned: on_success
          type: str
          sample: "/tmp/backup_restore_config.yaml"
        message:
          description: Detailed status message with operation summary
          returned: always
          type: str
          sample: |
            YAML configuration file generated successfully for module
            backup_and_restore_workflow_manager
        status:
          description: Operation status indicating success or failure
          returned: always
          type: str
          choices: ['success', 'failed']
    status:
      description: Overall operation status
      returned: always
      type: str
      choices: ['success', 'failed']

# Case_2: Idempotency Scenario
response_2:
  description: |
    No configurations found scenario treated as successful idempotent
    operation
  returned: when_no_configs_found
  type: dict
  sample:
    msg: |
      No backup and restore configurations found to process for module
      backup_and_restore_workflow_manager. Verify that NFS servers or
      backup configurations are set up in Catalyst Center.
    response:
      components_processed: 0
      components_skipped: 1
      configurations_count: 0
      message: |
        No backup and restore configurations found to process for module
        backup_and_restore_workflow_manager. Verify that NFS servers or
        backup configurations are set up in Catalyst Center.
      status: "success"
    status: "success"

# Case_3: Failure Scenario
response_3:
  description: |
    Operation failed due to invalid parameters, API errors, or file
    write issues
  returned: on_failure
  type: dict
  sample:
    msg: "Failed to write YAML configuration to file: /invalid/path"
    response:
      message: "Failed to write YAML configuration to file: /invalid/path"
      status: "failed"
    status: "failed"
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


class BackupRestorePlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    Class for generating brownfield YAML playbooks for backup and restore configurations
    from Cisco Catalyst Center.

    This class orchestrates the complete workflow for extracting backup and restore
    configurations from Catalyst Center and generating YAML playbook files compatible
    with the backup_and_restore_workflow_manager module. Handles NFS server configurations,
    backup storage configurations, component filtering, API data retrieval, transformation,
    and YAML file generation with comprehensive error handling and validation.

    Purpose:
        - Retrieves backup and restore configurations from Catalyst Center APIs
        - Transforms API responses to user-friendly YAML format
        - Generates playbook files for infrastructure as code workflows
        - Supports component-specific filtering (NFS and backup storage)
        - Validates parameters and handles errors gracefully
        - Provides detailed logging and operation tracking

    Inherits From:
        - DnacBase: Provides Catalyst Center SDK connectivity and base operations
        - BrownFieldHelper: Provides YAML generation and file handling utilities

    Supported Components:
        - nfs_configuration: NFS server details with paths, ports, and versions
        - backup_storage_configuration: Backup storage with encryption and retention

    Key Operations:
        - Validate input parameters against schema requirements
        - Retrieve configurations using Catalyst Center SDK methods
        - Apply component-specific filters for targeted extraction
        - Transform API responses to YAML-compatible structures
        - Generate timestamped YAML files with complete configurations
        - Track processing statistics and execution metrics

    Integration:
        - Uses backup.Backup.get_all_n_f_s_configurations API
        - Uses backup.Backup.get_backup_configuration API
        - Generates YAML compatible with backup_and_restore_workflow_manager module
        - Supports Catalyst Center version 3.1.3.0 and higher

    Workflow:
        1. Initialize with module parameters and connection details
        2. Validate input configuration and component selections
        3. Retrieve configurations from Catalyst Center for specified components
        4. Apply filters to extract specific configurations
        5. Transform API responses using specification mappings
        6. Generate YAML file with structured playbook content
        7. Return execution results with statistics and file path

    Attributes:
        supported_states (list): Valid states for module operation (['gathered'])
        module_schema (dict): Component mapping with API details and specifications
        module_name (str): Reference module name for generated playbooks
        validated_config (list): Validated input configuration parameters
        want (dict): Desired state configuration for processing
        result (dict): Execution results with status and response data

    Example Usage:
        generator = BackupRestorePlaybookGenerator(module)
        generator.validate_input().check_return_status()
        generator.get_want(config, 'gathered').check_return_status()
        generator.get_diff_gathered().check_return_status()
    """

    def __init__(self, module):
        """
        Initialize an instance of the BackupRestorePlaybookGenerator class.

        Description:
            Sets up the class instance with module configuration, supported states,
            module schema mapping, and module name for backup and restore operations.

        Args:
            module (AnsibleModule): The Ansible module instance containing configuration
                parameters and methods for module execution.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.backup_restore_workflow_manager_mapping()
        self.module_name = "backup_and_restore_workflow_manager"

    def validate_input(self):
        """
        Validates the input configuration parameters for the backup and restore playbook.

        Description:
            Performs comprehensive validation of input configuration parameters to ensure
            they conform to the expected schema. Validates parameter types, requirements,
            and structure for backup and restore configuration generation.

        Args:
            None: Uses self.config from the instance.

        Returns:
            object: Self instance with updated attributes:
                - self.msg (str): Message describing the validation result.
                - self.status (str): Status of validation ("success" or "failed").
                - self.validated_config (list): Validated configuration parameters if successful.
        """
        self.log(
            "Starting validation of input configuration parameters for backup and restore "
            "playbook generation. This operation validates parameter structure, types, allowed "
            "keys, and minimum requirements to ensure configuration conforms to expected schema "
            "before proceeding with YAML generation workflow.",
            "DEBUG"
        )

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "file_path": {"type": "str", "required": False},
            "generate_all_configurations": {"type": "bool", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        allowed_keys = set(temp_spec.keys())

        self.log(
            "Allowed parameter keys extracted from schema: {0}. Any keys outside this set will "
            "trigger validation failure with detailed error message showing allowed vs invalid keys.".format(
                list(allowed_keys)
            ),
            "DEBUG"
        )

        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                "Validating config item {0}/{1}. Checking type and allowed keys. Config item type: {2}".format(
                    config_index, len(self.config), type(config_item).__name__
                ),
                "DEBUG"
            )
            if not isinstance(config_item, dict):
                self.msg = "Configuration item must be a dictionary, got: {0}".format(type(config_item).__name__)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Check for invalid keys
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            self.log(
                "Config item {0} keys: {1}. Checking for invalid keys by comparing against allowed "
                "keys set. Invalid keys (if any) will be the difference between config_keys and "
                "allowed_keys.".format(config_index, list(config_keys)),
                "DEBUG"
            )

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
            self.log(
                "Config item {0} passed allowed keys validation. All keys ({1}) are recognized "
                "parameters. Proceeding to type validation.".format(config_index, list(config_keys)),
                "DEBUG"
            )

        self.log(
            "Allowed keys validation completed successfully for all {0} config item(s). No invalid "
            "or unknown parameters detected. Proceeding with type validation using validate_list_of_dicts().".format(
                len(self.config)
            ),
            "INFO"
        )

        self.validate_minimum_requirements(self.config)

        self.log(
            "Minimum requirements validation completed. Configuration meets logical requirements "
            "for backup and restore playbook generation. At least one selection criteria (generate_all, "
            "filters, etc.) is present.",
            "DEBUG"
        )

        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self
        self.log(
            "Type validation completed successfully using validate_list_of_dicts(). All parameters "
            "have correct data types matching temp_spec requirements. Validated {0} config item(s).".format(
                len(valid_temp)
            ),
            "INFO"
        )

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = (
            "Successfully validated playbook configuration parameters using 'validated_input'. "
            "Total config items validated: {0}. Configuration structure conforms to expected schema "
            "with correct parameter types and allowed keys. Validated configuration: {1}".format(
                len(valid_temp), str(valid_temp)
            )
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def backup_restore_workflow_manager_mapping(self):
        """
        Constructs comprehensive mapping configuration for backup and restore components.

        Description:
            Creates a structured mapping that defines all supported backup and restore
            components, their associated API functions, filter specifications, and
            processing functions. This mapping serves as the central configuration
            registry for the backup and restore workflow orchestration process.

        Args:
            None: Uses class methods and instance configuration.

        Returns:
            dict: A comprehensive mapping dictionary containing:
                - network_elements (dict): Component configurations with API details,
                  filter specifications, and processing function references.
                - global_filters (dict): Global filter configuration options.
        """
        self.log(
            "Generating backup and restore workflow manager mapping configuration. "
            "This mapping defines all supported backup and restore components including "
            "NFS configuration and backup storage configuration. Each component specifies "
            "its filter schema, API endpoints, transformation specifications, and processing "
            "functions for orchestrated data retrieval and YAML generation workflow.",
            "DEBUG"
        )

        mapping_config = {
            "network_elements": {
                "nfs_configuration": {
                    "filters": {
                        "server_ip": {"type": "str", "required": False},
                        "source_path": {"type": "str", "required": False},
                    },
                    "reverse_mapping_function": self.nfs_configuration_temp_spec(),
                    "api_function": "get_all_n_f_s_configurations",
                    "api_family": "backup",
                    "get_function_name": self.get_nfs_configurations,
                },
                "backup_storage_configuration": {
                    "filters": {
                        "server_type": {"type": "str", "required": False},
                    },
                    "reverse_mapping_function": self.backup_storage_configuration_temp_spec(),
                    "api_function": "get_backup_configuration",
                    "api_family": "backup",
                    "get_function_name": self.get_backup_storage_configurations,
                },
            },
            "global_filters": {},
        }

        self.log(
            "Backup and restore mapping configuration generated successfully. Total "
            "network elements defined: {0}. Components: {1}. Each component includes "
            "filter schemas, API endpoint details, transformation specifications, and "
            "processing function references for comprehensive backup and restore workflow "
            "orchestration.".format(
                len(mapping_config["network_elements"]),
                list(mapping_config["network_elements"].keys())
            ),
            "DEBUG"
        )

        return mapping_config

    def nfs_configuration_temp_spec(self):
        """
        Constructs detailed specification for NFS configuration data transformation.

        Description:
            Creates a comprehensive specification that defines how NFS configuration
            API response fields should be mapped, transformed, and structured in the
            final YAML configuration. Includes server details, paths, ports, and version information.

        Args:
            None: Uses logging methods from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            and source key references for NFS configuration transformations.
        """
        self.log(
            "Generating temporary specification for NFS configuration details. This "
            "specification defines the transformation mapping from Catalyst Center API "
            "response format (camelCase) to user-friendly YAML playbook format (snake_case). "
            "Includes field mappings for server IP, source path, NFS ports, and protocol "
            "version with their corresponding API source paths and data types.",
            "DEBUG"
        )

        nfs_configuration_details = OrderedDict({
            "server_ip": {"type": "str", "source_key": "spec.server"},
            "source_path": {"type": "str", "source_key": "spec.sourcePath"},
            "nfs_port": {"type": "int", "source_key": "spec.nfsPort"},
            "nfs_version": {"type": "str", "source_key": "spec.nfsVersion"},
            "nfs_portmapper_port": {"type": "int", "source_key": "spec.portMapperPort"},
        })
        self.log(
            "NFS configuration specification generated successfully with {0} field mappings. "
            "Fields defined: {1}. Specification provides complete transformation rules for "
            "converting API response data (spec.server, spec.sourcePath, etc.) to playbook "
            "parameters (server_ip, source_path, etc.) for YAML generation workflow.".format(
                len(nfs_configuration_details),
                list(nfs_configuration_details.keys())
            ),
            "DEBUG"
        )

        return nfs_configuration_details

    def extract_nested_value(self, data, key_path):
        """
        Extracts values from nested dictionaries using dot notation paths.

        Description:
            Navigates through nested dictionary structures using dot-separated paths
            to extract specific values. Handles missing keys gracefully by returning
            None when paths don't exist or when encountering type errors.

        Args:
            data (dict): The source dictionary containing nested data structures.
            key_path (str): Dot-separated path to the desired value (e.g., "spec.server").

        Returns:
            any: The value found at the specified path, or None if the path doesn't exist
            or if a type error occurs during navigation.
        """
        self.log(
            "Extracting nested value from data structure using dot notation key path. "
            "Target path: '{0}'. This operation will traverse the nested dictionary "
            "structure by splitting the key path on '.' delimiter and sequentially "
            "accessing each level using safe dict.get() operations. Missing keys or "
            "type errors will result in None return value with appropriate logging.".format(
                key_path
            ),
            "DEBUG"
        )
        try:
            keys = key_path.split('.')
            self.log(
                "Key path '{0}' parsed into {1} component(s): {2}. Beginning sequential "
                "traversal through nested dictionary structure starting from root level.".format(
                    key_path, len(keys), keys
                ),
                "DEBUG"
            )
            result = data

            # Traverse nested structure sequentially using parsed keys
            for key_index, key in enumerate(keys, start=1):
                self.log(
                    "Traversal step {0}/{1}: Accessing key '{2}' at current nesting level. "
                    "Current data type: {3}.".format(
                        key_index, len(keys), key, type(result).__name__
                    ),
                    "DEBUG"
                )
                result = result.get(key)
                if result is None:
                    self.log(
                        "Traversal terminated at step {0}/{1}. Key '{2}' not found in the "
                        "current data level or returned None value. Remaining path: {3}. "
                        "Returning None as extraction result.".format(
                            key_index, len(keys), key,
                            '.'.join(keys[key_index:]) if key_index < len(keys) else "N/A"
                        ),
                        "DEBUG"
                    )
                    return None

            self.log(
                "Successfully completed nested value extraction for key path '{0}'. "
                "Traversed {1} level(s) successfully. Extracted value type: {2}.".format(
                    key_path, len(keys), type(result).__name__
                ),
                "DEBUG"
            )

            return result

        except (AttributeError, TypeError) as e:
            self.log(
                "Key path '{0}' parsed into {1} component(s): {2}. Beginning sequential "
                "traversal through nested dictionary structure starting from root level.".format(
                    key_path, len(keys), keys
                ),
                "DEBUG"
            )
            return None

    def get_nfs_configurations(self, network_element, filters):
        """
        Retrieves NFS configuration details from Cisco Catalyst Center.

        Description:
            Fetches NFS configuration data from the API and applies component-specific
            filters. Validates that both server_ip and source_path are provided together
            for filtering operations. Transforms API responses into structured format
            suitable for YAML generation.

            Args:
                network_element (dict): Configuration mapping containing API endpoint details:
                    - api_family (str): SDK family name ("backup")
                    - api_function (str): SDK method name ("get_all_n_f_s_configurations")
                    - reverse_mapping_function (OrderedDict): Field transformation specification
                filters (dict): Filter criteria containing:
                    - component_specific_filters (dict): Component-level filtering options
                    - nfs_configuration (list): List of NFS filter dictionaries
                        - server_ip (str): NFS server IP address filter
                        - source_path (str): NFS source path filter

            Returns:
                dict: A dictionary containing transformed NFS configurations:
                    - nfs_configuration (list): List of OrderedDict objects with:
                    - server_ip (str): NFS server IP address
                    - source_path (str): NFS source path
                    - nfs_port (int): NFS service port
                    - nfs_version (str): NFS protocol version
                    - nfs_portmapper_port (int): RPC portmapper port
                    Returns operation result dict if filter validation fails

        Returns:
            dict: A dictionary containing:
                - nfs_configuration (list): List of NFS configuration dictionaries
                  with transformed parameters according to the specification.
        """
        self.log(
            "Starting retrieval of NFS configurations from Catalyst Center. Network element "
            "configuration: {0}. Applied filters: {1}. This operation will fetch NFS server "
            "details from the API, apply component-specific filtering if provided, and transform "
            "API response format (camelCase) to user-friendly YAML format (snake_case) for "
            "playbook generation.".format(network_element, filters),
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        nfs_filters = component_specific_filters.get("nfs_configuration", [])

        self.log(
            "Extracted component-specific filters for NFS configuration. Total filter count: {0}. "
            "Filter details: {1}. If filters are provided, both server_ip AND source_path must "
            "be present together in each filter for validation to pass.".format(
                len(nfs_filters), nfs_filters
            ),
            "DEBUG"
        )

        if nfs_filters:
            self.log(
                "Validating NFS configuration filters for required parameters. Each filter must "
                "include both 'server_ip' and 'source_path' together. Checking {0} filter(s) for "
                "compliance with validation requirements.".format(len(nfs_filters)),
                "DEBUG"
            )

            for filter_index, filter_param in enumerate(nfs_filters, start=1):
                self.log(
                    "Validating filter {0}/{1}: {2}. Checking for presence of both 'server_ip' "
                    "and 'source_path' keys in filter dictionary.".format(
                        filter_index, len(nfs_filters), filter_param
                    ),
                    "DEBUG"
                )

                # Check if both required keys are present in the filter
                has_server_ip = "server_ip" in filter_param
                has_source_path = "source_path" in filter_param

                self.log(
                    "Filter {0} validation check: has_server_ip={1}, has_source_path={2}. "
                    "Both must be True for validation to pass.".format(
                        filter_index, has_server_ip, has_source_path
                    ),
                    "DEBUG"
                )

                if not (has_server_ip and has_source_path):
                    error_msg = (
                        "NFS configuration filter validation failed. Filter must include both "
                        "'server_ip' and 'source_path' parameters together for proper NFS server "
                        "identification. Invalid filter at position {0}: {1}. Please provide both "
                        "parameters or remove the filter to retrieve all NFS configurations. "
                        "Missing parameters: {2}.".format(
                            filter_index,
                            filter_param,
                            [k for k in ["server_ip", "source_path"] if k not in filter_param]
                        )
                    )
                    self.log(error_msg, "ERROR")

                    result = self.set_operation_result("failed", False, error_msg, "ERROR")

                    self.msg = error_msg
                    self.result["msg"] = error_msg
                    self.log(
                        "Filter validation failed, returning operation result with error details. "
                        "Operation status: failed. No API call will be made due to invalid filter "
                        "configuration.",
                        "ERROR"
                    )

                    return result
        self.log(
            "All {0} NFS configuration filter(s) passed validation successfully. Each filter "
            "contains both required parameters (server_ip and source_path). Proceeding with "
            "API retrieval and filtering operations.".format(len(nfs_filters)),
            "INFO"
        )

        final_nfs_configs = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting NFS configurations using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )

            self.log(
                "Received API response from Catalyst Center. Response type: {0}. Response structure: {1}. "
                "Parsing response to extract NFS configurations list.".format(
                    type(response).__name__, response
                ),
                "DEBUG"
            )

            if isinstance(response, dict):
                nfs_configs = response.get("response", [])
                self.log(
                    "API response is dictionary format. Extracted 'response' key containing {0} "
                    "NFS configuration(s). Response key exists: {1}.".format(
                        len(nfs_configs) if isinstance(nfs_configs, list) else 0,
                        "response" in response
                    ),
                    "DEBUG"
                )

            else:
                nfs_configs = response if isinstance(response, list) else []
                self.log(
                    "API response is direct list format (not wrapped in dictionary). Total "
                    "configurations: {0}. Response type: {1}.".format(
                        len(nfs_configs) if isinstance(nfs_configs, list) else 0,
                        type(response).__name__
                    ),
                    "DEBUG"
                )

            self.log(
                "Successfully retrieved {0} NFS configuration(s) from Catalyst Center API. "
                "Configurations will be processed for filtering and transformation to YAML format.".format(
                    len(nfs_configs)
                ),
                "INFO"
            )

            if nfs_configs:
                self.log(
                    "Sample NFS configuration structure (first item): {0}. This structure shows "
                    "the API response format with nested 'spec' and 'status' sections that will "
                    "be transformed to user-friendly YAML format.".format(nfs_configs[0]),
                    "DEBUG"
                )
            else:
                self.log(
                    "No NFS configurations found in API response. Retrieved configuration list is "
                    "empty. This may indicate no NFS servers are configured in Catalyst Center for "
                    "backup and restore operations.",
                    "WARNING"
                )

            if nfs_filters:
                self.log(
                    "Applying component-specific filters to retrieved NFS configurations. Filter count: {0}. "
                    "Each configuration will be checked against all filters for matching server_ip and "
                    "source_path. Only configurations matching all criteria will be included in final results.".format(
                        len(nfs_filters)
                    ),
                    "DEBUG"
                )
                filtered_configs = []

                for filter_index, filter_param in enumerate(nfs_filters, start=1):
                    self.log(
                        "Processing filter {0}/{1}: {2}. Checking all {3} retrieved configuration(s) "
                        "for matches against this filter's server_ip and source_path criteria.".format(
                            filter_index, len(nfs_filters), filter_param, len(nfs_configs)
                        ),
                        "DEBUG"
                    )
                    # Check each configuration against current filter
                    for config_index, config in enumerate(nfs_configs, start=1):
                        match = True

                        # Extract spec section from configuration
                        spec = config.get("spec", config)

                        self.log(
                            "Checking NFS configuration {0}/{1} against filter {2}. Configuration spec: {3}. "
                            "Comparing spec.server with filter.server_ip and spec.sourcePath with "
                            "filter.source_path for exact match validation.".format(
                                config_index, len(nfs_configs), filter_index, spec
                            ),
                            "DEBUG"
                        )

                        server_ip_match = spec.get("server") == filter_param.get("server_ip")
                        source_path_match = spec.get("sourcePath") == filter_param.get("source_path")

                        if not (server_ip_match and source_path_match):
                            match = False

                        self.log(
                            "NFS filter matching result for configuration {0}: server_ip comparison "
                            "(spec.server='{1}' vs filter='{2}'): {3}, source_path comparison "
                            "(spec.sourcePath='{4}' vs filter='{5}'): {6}, overall match: {7}.".format(
                                config_index,
                                spec.get("server"),
                                filter_param.get("server_ip"),
                                server_ip_match,
                                spec.get("sourcePath"),
                                filter_param.get("source_path"),
                                source_path_match,
                                match
                            ),
                            "DEBUG"
                        )

                        if match and config not in filtered_configs:
                            filtered_configs.append(config)
                            self.log(
                                "NFS configuration {0} matched filter {1} criteria successfully. Added to "
                                "filtered configurations list. Total filtered configurations: {2}.".format(
                                    config_index, filter_index, len(filtered_configs)
                                ),
                                "INFO"
                            )

                final_nfs_configs = filtered_configs
                self.log(
                    "Filter application completed. Total configurations after filtering: {0} out of {1} "
                    "retrieved. Filtered configurations will proceed to transformation phase.".format(
                        len(final_nfs_configs), len(nfs_configs)
                    ),
                    "INFO"
                )
            else:
                final_nfs_configs = nfs_configs
                self.log(
                    "No component-specific filters provided. Using all {0} retrieved NFS configuration(s) "
                    "for transformation to YAML format. All configurations will be included in final output.".format(
                        len(final_nfs_configs)
                    ),
                    "INFO"
                )

        except Exception as e:
            self.log(
                "Exception occurred during NFS configuration retrieval from API. Error type: {0}, "
                "Error message: {1}. This may indicate network connectivity issues, API endpoint "
                "unavailability, or authentication problems with Catalyst Center.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )

            self.log(
                "API call failed, returning empty NFS configuration list to allow workflow to continue. "
                "No NFS configurations will be included in YAML output due to retrieval failure.",
                "WARNING"
            )
            final_nfs_configs = []

        self.log(
            "Starting transformation of {0} NFS configuration(s) from API response format to "
            "user-friendly YAML format. Transformation will convert camelCase API field names to "
            "snake_case parameter names and restructure nested data for playbook compatibility.".format(
                len(final_nfs_configs)
            ),
            "DEBUG"
        )

        # Retrieve transformation specification for NFS configurations
        nfs_configuration_temp_spec = self.nfs_configuration_temp_spec()

        self.log(
            "Retrieved NFS configuration transformation specification with {0} field mapping(s). "
            "Specification defines source_key paths and data types for each YAML parameter. "
            "Fields to be transformed: {1}.".format(
                len(nfs_configuration_temp_spec),
                list(nfs_configuration_temp_spec.keys())
            ),
            "DEBUG"
        )

        modified_nfs_configs = []
        # Transform each NFS configuration using specification
        for config_index, config in enumerate(final_nfs_configs, start=1):
            self.log(
                "Transforming NFS configuration {0}/{1} using specification-based field mapping. "
                "Original configuration: {2}. Processing {3} field mappings from specification.".format(
                    config_index, len(final_nfs_configs), config, len(nfs_configuration_temp_spec)
                ),
                "DEBUG"
            )

            mapped_config = OrderedDict()

            # Process each field mapping from specification
            for field_index, (key, spec_def) in enumerate(nfs_configuration_temp_spec.items(), start=1):
                source_key = spec_def.get("source_key", key)

                self.log(
                    "Processing field mapping {0}/{1}: YAML parameter '{2}' from API source '{3}'. "
                    "Extracting nested value using dot notation path.".format(
                        field_index, len(nfs_configuration_temp_spec), key, source_key
                    ),
                    "DEBUG"
                )
                # Extract value using nested path traversal
                value = self.extract_nested_value(config, source_key)

                # Fallback to direct field extraction if nested extraction returns None
                if value is None:
                    self.log(
                        "Nested value extraction returned None for field '{0}'. Attempting direct "
                        "field extraction from config.spec as fallback method.".format(key),
                        "DEBUG"
                    )

                    if key == "server_ip":
                        value = config.get("spec", {}).get("server")
                        self.log("Direct extraction for server_ip: {0}".format(value), "DEBUG")
                    elif key == "source_path":
                        value = config.get("spec", {}).get("sourcePath")
                        self.log("Direct extraction for source_path: {0}".format(value), "DEBUG")
                    elif key == "nfs_port":
                        value = config.get("spec", {}).get("nfsPort")
                        self.log("Direct extraction for nfs_port: {0}".format(value), "DEBUG")
                    elif key == "nfs_version":
                        value = config.get("spec", {}).get("nfsVersion")
                        self.log("Direct extraction for nfs_version: {0}".format(value), "DEBUG")
                    elif key == "nfs_portmapper_port":
                        value = config.get("spec", {}).get("portMapperPort")
                        self.log("Direct extraction for nfs_portmapper_port: {0}".format(value), "DEBUG")

                # Apply transformation function and add to mapped configuration
                if value is not None:
                    transform = spec_def.get("transform", lambda x: x)
                    mapped_config[key] = transform(value)

                    self.log(
                        "Field '{0}' successfully mapped with value: {1} (type: {2}). Transformation "
                        "applied: {3}.".format(
                            key, value, type(value).__name__,
                            "custom function" if "transform" in spec_def else "identity"
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Field '{0}' extraction resulted in None value. Skipping field in YAML output "
                        "as no valid data available from API response.".format(key),
                        "DEBUG"
                    )

            # Add mapped configuration to results if not empty
            if mapped_config:
                modified_nfs_configs.append(mapped_config)
                self.log(
                    "Configuration {0} transformation completed successfully. Mapped {1} field(s) to "
                    "YAML format. Transformed configuration: {2}.".format(
                        config_index, len(mapped_config), mapped_config
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "Configuration {0} transformation resulted in empty mapped configuration. "
                    "Skipping configuration as no valid fields could be extracted.".format(config_index),
                    "WARNING"
                )

        modified_nfs_configuration_details = {"nfs_configuration": modified_nfs_configs}
        self.log(
            "NFS configuration transformation completed successfully. Total configurations transformed: {0}. "
            "Final structure contains 'nfs_configuration' key with list of {0} transformed configuration(s) "
            "ready for YAML generation. Modified configuration details: {1}.".format(
                len(modified_nfs_configs), modified_nfs_configuration_details
            ),
            "INFO"
        )

        return modified_nfs_configuration_details

    def backup_storage_configuration_temp_spec(self):
        """
        Constructs detailed specification for backup storage configuration data transformation.

        Description:
            Creates a comprehensive specification for backup storage configurations,
            handling server types, NFS details, retention policies, and encryption settings.
            Includes special transformation functions for complex nested data structures.

        Args:
            None: Uses instance methods for transformation functions.

        Returns:
            OrderedDict: A detailed transformation specification containing:
                - Field mappings from API response to user parameters
                - Data type specifications for each field
                - Special handling flags for complex transformations
                - Transformation function references for nested data
                - Security directives for sensitive data handling
                - Ordered sequence for consistent YAML generation
        """
        self.log(
            "Generating temporary specification for backup storage configuration "
            "details. This specification defines the transformation mapping from "
            "Catalyst Center API response format to user-friendly YAML playbook "
            "format. Includes field mappings for server type, NFS connection details, "
            "data retention policies, and encryption settings with their corresponding "
            "API source paths, data types, and transformation functions. Special "
            "handling configured for nested NFS details correlation and security "
            "flags for sensitive encryption data.",
            "DEBUG"
        )
        # Create ordered specification dictionary with field mappings and transformations
        backup_storage_config_details = OrderedDict({
            "server_type": {
                "type": "str",
                "source_key": "type"
            },
            "nfs_details": {
                "type": "dict",
                "special_handling": True,
                "transform": self.transform_nfs_details
            },
            "data_retention_period": {
                "type": "int",
                "source_key": "dataRetention"
            },
            "encryption_passphrase": {
                "type": "str",
                "source_key": "encryptionPassphrase",
                "no_log": True
            },
        })

        self.log(
            "Backup storage configuration specification generated successfully with "
            "{0} field mappings. Fields defined: {1}. Specification provides complete "
            "transformation rules including special handling for NFS details correlation "
            "(transform_nfs_details function), security flags for encryption passphrase "
            "(no_log=True), and standard field mappings (server_type from 'type', "
            "data_retention_period from 'dataRetention'). This specification enables "
            "converting API response data to playbook parameters for YAML generation "
            "workflow with proper security and transformation handling.".format(
                len(backup_storage_config_details),
                list(backup_storage_config_details.keys())
            ),
            "DEBUG"
        )
        return backup_storage_config_details

    def transform_nfs_details(self, config):
        """
        Transforms backup configuration data to extract NFS connection details.

        Description:
            Processes backup configuration to extract and correlate NFS details by
            matching mount paths with existing NFS configurations. Creates comprehensive
            NFS connection information including server details, ports, and versions.

        Args:
            config (dict): Backup configuration dictionary containing mount path and
                other backup-related settings.

        Returns:
            dict: A dictionary containing NFS connection details:
                - server_ip (str): NFS server IP address.
                - source_path (str): NFS source path.
                - nfs_port (int): NFS service port.
                - nfs_version (str): NFS protocol version.
                - nfs_portmapper_port (int): NFS portmapper port.
        """
        self.log(
            "Transforming NFS details from backup configuration for mount path correlation "
            "with existing NFS server configurations. This operation retrieves all registered "
            "NFS servers, compares their destination mount paths with the backup storage mount "
            "path, and extracts complete server connection details when a match is found. Input "
            "backup configuration: {0}".format(config),
            "DEBUG"
        )
        self.log("Input backup config: {0}".format(config), "DEBUG")

        current_nfs_configs = self.get_nfs_configuration_details()
        self.log(
            "Retrieved {0} NFS configuration(s) from Catalyst Center for mount path correlation. "
            "Each configuration will be checked for matching destination path with backup mount "
            "path to extract server details.".format(len(current_nfs_configs)),
            "DEBUG"
        )
        mount_path = config.get("mountPath")
        self.log(
            "Extracted mount path from backup configuration: '{0}'. This path will be compared "
            "against NFS destination paths (status.destinationPath) to identify matching NFS "
            "server configuration.".format(mount_path),
            "DEBUG"
        )

        self.log("Mount path from backup config: {0}".format(mount_path), "DEBUG")
        self.log("Available NFS configs: {0}".format(len(current_nfs_configs)), "DEBUG")

        nfs_details = {
            "server_ip": None,
            "source_path": None,
            "nfs_port": 2049,
            "nfs_version": "nfs4",
            "nfs_portmapper_port": 111
        }

        match_found = False
        self.log(
            "Starting mount path correlation loop. Iterating through {0} NFS configuration(s) "
            "to find matching destination path. Looking for exact match between backup mount "
            "path '{1}' and NFS status.destinationPath field.".format(
                len(current_nfs_configs), mount_path
            ),
            "DEBUG"
        )

        for nfs_index, nfs_config in enumerate(current_nfs_configs, start=1):
            # Extract destination path from NFS configuration status
            nfs_mount_path = nfs_config.get("status", {}).get("destinationPath")

            self.log(
                "Correlation iteration {0}/{1}: Checking NFS configuration destination path. "
                "NFS destination path: '{2}', Backup mount path: '{3}'. Comparing paths for "
                "exact match (case-sensitive).".format(
                    nfs_index, len(current_nfs_configs), nfs_mount_path, mount_path
                ),
                "DEBUG"
            )
            nfs_mount_path = nfs_config.get("status", {}).get("destinationPath")
            self.log("Checking NFS config mount path: {0} against backup mount path: {1}".format(
                nfs_mount_path, mount_path), "DEBUG")

            if nfs_mount_path == mount_path:
                self.log(
                    "Mount path match found at iteration {0}/{1}. Destination path '{2}' matches "
                    "backup mount path '{3}'. Extracting complete NFS server details from matched "
                    "configuration spec section.".format(
                        nfs_index, len(current_nfs_configs), nfs_mount_path, mount_path
                    ),
                    "INFO"
                )
                spec = nfs_config.get("spec", {})
                self.log(
                    "Extracted spec section from matched NFS configuration. Spec contains server "
                    "connection details: server={0}, sourcePath={1}, nfsPort={2}, nfsVersion={3}, "
                    "portMapperPort={4}. Updating nfs_details dictionary with extracted values.".format(
                        spec.get("server"),
                        spec.get("sourcePath"),
                        spec.get("nfsPort"),
                        spec.get("nfsVersion"),
                        spec.get("portMapperPort")
                    ),
                    "DEBUG"
                )
                nfs_details.update({
                    "server_ip": spec.get("server"),
                    "source_path": spec.get("sourcePath"),
                    "nfs_port": spec.get("nfsPort", 2049),
                    "nfs_version": spec.get("nfsVersion", "nfs4"),
                    "nfs_portmapper_port": spec.get("portMapperPort", 111)
                })
                match_found = True
                self.log(
                    "NFS details successfully extracted from matched configuration. Updated "
                    "nfs_details: server_ip={0}, source_path={1}, nfs_port={2}, nfs_version={3}, "
                    "nfs_portmapper_port={4}. Correlation completed successfully.".format(
                        nfs_details["server_ip"],
                        nfs_details["source_path"],
                        nfs_details["nfs_port"],
                        nfs_details["nfs_version"],
                        nfs_details["nfs_portmapper_port"]
                    ),
                    "INFO"
                )
                break
            else:
                self.log(
                    "Correlation iteration {0}/{1}: No match. NFS destination path '{2}' does "
                    "not match backup mount path '{3}'. Continuing to next NFS configuration.".format(
                        nfs_index, len(current_nfs_configs), nfs_mount_path, mount_path
                    ),
                    "DEBUG"
                )

        if not match_found:
            self.log(
                "Mount path correlation completed without finding matching NFS configuration. "
                "Backup mount path '{0}' does not match any NFS destination paths in {1} "
                "retrieved configuration(s). Returning default nfs_details with None values for "
                "server_ip and source_path. This may indicate NFS configuration mismatch or "
                "cleanup required.".format(mount_path, len(current_nfs_configs)),
                "WARNING"
            )

        self.log(
            "NFS details transformation completed. Correlation status: {0}. Final transformed "
            "nfs_details dictionary: {1}. This data will be used in backup_storage_configuration "
            "YAML output. Match found: {0}, Server IP: {2}, Source path: {3}.".format(
                "success" if match_found else "no match",
                nfs_details,
                nfs_details.get("server_ip"),
                nfs_details.get("source_path")
            ),
            "INFO"
        )

        return nfs_details

    def get_backup_storage_configurations(self, network_element, filters):
        """
        Retrieves backup storage configuration details from Cisco Catalyst Center.

        Description:
            Fetches backup storage configuration data from the API and applies
            component-specific filters. Only supports server_type filtering for
            backup storage configurations. Transforms API responses into structured
            format suitable for YAML generation.

        Args:
            network_element (dict): Configuration mapping containing API family and
                function details for backup storage configuration retrieval.
            filters (dict): Filter criteria containing component-specific filters
                for backup storage configurations.

        Returns:
            dict: A dictionary containing:
                - backup_storage_configuration (list): List of backup storage
                  configuration dictionaries with transformed parameters.
        """
        self.log(
            "Starting retrieval of backup storage configurations from Catalyst Center. "
            "Network element configuration: {0}. Applied filters: {1}. This operation "
            "will fetch backup storage settings from the API, apply component-specific "
            "filtering by server type if provided, and transform API response format to "
            "user-friendly YAML format for playbook generation with special handling for "
            "NFS details correlation.".format(network_element, filters),
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        backup_filters = component_specific_filters.get("backup_storage_configuration", [])

        self.log(
            "Extracted component-specific filters for backup storage configuration. Total "
            "filter count: {0}. Filter details: {1}. Only 'server_type' filter is supported "
            "for backup storage configurations. Other filters (mount_path, retention_period, "
            "etc.) are not allowed and will trigger validation failure.".format(
                len(backup_filters), backup_filters
            ),
            "DEBUG"
        )

        # Validate filter requirements: only server_type filter is supported
        if backup_filters:
            self.log(
                "Validating backup storage configuration filters for supported parameters. "
                "Checking {0} filter(s) for compliance. Only 'server_type' filter is allowed. "
                "Any other filter keys will cause validation failure.".format(len(backup_filters)),
                "DEBUG"
            )

            for filter_index, filter_param in enumerate(backup_filters, start=1):
                self.log(
                    "Validating filter {0}/{1}: {2}. Checking for unsupported filter keys. "
                    "Allowed keys: ['server_type']. Any other keys will be flagged as unsupported.".format(
                        filter_index, len(backup_filters), filter_param
                    ),
                    "DEBUG"
                )

                # Check for unsupported filter keys
                unsupported_filters = []
                for key in filter_param.keys():
                    if key not in ["server_type"]:
                        unsupported_filters.append(key)

                self.log(
                    "Filter {0} validation check: unsupported_filters={1}. If non-empty, "
                    "validation will fail.".format(filter_index, unsupported_filters),
                    "DEBUG"
                )

                if unsupported_filters:
                    error_msg = (
                        "Backup storage configuration filter validation failed. Only 'server_type' "
                        "filter is supported for backup storage configurations. Unsupported filters "
                        "detected: {0}. Invalid filter at position {1}: {2}. Please remove unsupported "
                        "filters or use only 'server_type' filter with values 'NFS' or 'PHYSICAL_DISK'. "
                        "Filters like mount_path, retention_period, encryption_passphrase are not "
                        "supported for filtering backup storage configurations.".format(
                            unsupported_filters, filter_index, filter_param
                        )
                    )
                    self.log(error_msg, "ERROR")

                    # Set operation result to failed and return early
                    result = self.set_operation_result("failed", False, error_msg, "ERROR")

                    self.msg = error_msg
                    self.result["msg"] = error_msg

                    self.log(
                        "Filter validation failed, returning operation result with error details. "
                        "Operation status: failed. No API call will be made due to invalid filter "
                        "configuration.",
                        "ERROR"
                    )

                    return result

            self.log(
                "All {0} backup storage configuration filter(s) passed validation successfully. "
                "All filters contain only supported 'server_type' parameter. Proceeding with API "
                "retrieval and filtering operations.".format(len(backup_filters)),
                "INFO"
            )

        final_backup_configs = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Extracted API endpoint configuration from network element mapping. API family: '{0}', "
            "API function: '{1}'. This configuration will be used to make SDK method call for "
            "retrieving backup storage configuration from Catalyst Center.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )

            self.log(
                "Received API response from Catalyst Center. Response type: {0}. Response data: {1}. "
                "Parsing response to extract backup storage configuration.".format(
                    type(response).__name__, response
                ),
                "DEBUG"
            )

            # Parse API response to extract backup storage configuration
            if response is None:
                self.log(
                    "API response is None {0}. No backup storage configuration available in Catalyst "
                    "Center. This may indicate backup storage has not been configured yet or "
                    "configuration has been removed.".format(response),
                    "WARNING"
                )
                backup_config = {}
            elif isinstance(response, dict):
                backup_config = response.get("response", {})
                self.log(
                    "API response is dictionary format. Extracted 'response' key containing backup "
                    "configuration. Response key exists: {0}. Configuration: {1}.".format(
                        "response" in response, backup_config
                    ),
                    "DEBUG"
                )
            else:
                backup_config = response if isinstance(response, dict) else {}
                self.log(
                    "API response is unexpected format (not dict or None). Response type: {0}. "
                    "Defaulting to empty configuration.".format(type(response).__name__),
                    "WARNING"
                )

            self.log(
                "Successfully parsed backup storage configuration from Catalyst Center API. "
                "Configuration available: {0}. Configuration will be processed for filtering "
                "and transformation to YAML format.".format(bool(backup_config)),
                "INFO"
            )

            # Process configuration if available
            if backup_config:
                # Apply component-specific filters if provided
                if backup_filters:
                    self.log(
                        "Applying component-specific filters to retrieved backup storage configuration. "
                        "Filter count: {0}. Configuration will be checked against all filters for "
                        "matching server_type. Only configurations matching filter criteria will be "
                        "included in final results.".format(len(backup_filters)),
                        "DEBUG"
                    )

                    # Iterate through each filter parameter
                    for filter_index, filter_param in enumerate(backup_filters, start=1):
                        self.log(
                            "Processing filter {0}/{1}: {2}. Checking backup configuration against "
                            "this filter's server_type criteria.".format(
                                filter_index, len(backup_filters), filter_param
                            ),
                            "DEBUG"
                        )

                        match = True

                        # Check each filter criterion
                        for key, value in filter_param.items():
                            if key == "server_type":
                                config_value = backup_config.get("type")

                                self.log(
                                    "Server type filter comparison: filter expects '{0}', configuration "
                                    "has '{1}'. Comparing values for exact match (case-sensitive string "
                                    "comparison).".format(value, config_value),
                                    "DEBUG"
                                )

                                if str(config_value) != str(value):
                                    match = False
                                    self.log(
                                        "Server type mismatch detected. Filter {0} expects server_type='{1}' "
                                        "but configuration has type='{2}'. Configuration will be excluded "
                                        "from results.".format(filter_index, value, config_value),
                                        "DEBUG"
                                    )
                                    break

                        # Add matching configuration to filtered list
                        if match:
                            final_backup_configs = [backup_config]
                            self.log(
                                "Backup storage configuration matched filter {0} criteria successfully. "
                                "Server type matches expected value. Configuration will be included in "
                                "final results and proceed to transformation phase.".format(filter_index),
                                "INFO"
                            )
                            break
                    if not final_backup_configs:
                        self.log(
                            "Filter application completed without matches. Backup storage configuration "
                            "did not match any of {0} provided filter(s). No configurations will be "
                            "included in final results.".format(len(backup_filters)),
                            "INFO"
                        )
                else:
                    final_backup_configs = [backup_config] if backup_config else []
                    self.log(
                        "No component-specific filters provided. Using retrieved backup storage "
                        "configuration without filtering. Configuration will proceed directly to "
                        "transformation phase for YAML generation.",
                        "INFO"
                    )
            else:
                self.log(
                    "No backup storage configuration found in API response. Configuration object is "
                    "empty or None. No configurations will be included in final results.",
                    "INFO"
                )
                final_backup_configs = []

        except Exception as e:
            self.log(
                "Exception occurred during backup storage configuration retrieval from API. Error "
                "type: {0}, Error message: {1}. This may indicate network connectivity issues, API "
                "endpoint unavailability, authentication problems, or API version incompatibility "
                "with Catalyst Center.".format(type(e).__name__, str(e)),
                "ERROR"
            )

            self.log(
                "API call failed, returning empty backup storage configuration list to allow "
                "workflow to continue. No backup storage configurations will be included in YAML "
                "output due to retrieval failure.",
                "WARNING"
            )

            final_backup_configs = []

        self.log(
            "Starting transformation of {0} backup storage configuration(s) from API response "
            "format to user-friendly YAML format. Transformation will convert camelCase API field "
            "names to snake_case parameter names, apply special handling for NFS details correlation, "
            "and structure data for playbook compatibility.".format(len(final_backup_configs)),
            "DEBUG"
        )

        backup_storage_config_temp_spec = self.backup_storage_configuration_temp_spec()

        self.log(
            "Retrieved backup storage configuration transformation specification with {0} field "
            "mapping(s). Specification defines source_key paths, data types, special handling "
            "directives, and security flags for each YAML parameter. Fields to be transformed: {1}.".format(
                len(backup_storage_config_temp_spec),
                list(backup_storage_config_temp_spec.keys())
            ),
            "DEBUG"
        )
        modified_backup_configs = []

        # Transform each backup storage configuration using specification
        for config_index, config in enumerate(final_backup_configs, start=1):
            self.log(
                "Transforming backup storage configuration {0}/{1} using specification-based field "
                "mapping. Original configuration: {2}. Processing {3} field mappings from "
                "specification including special handling for NFS details and security directives "
                "for encryption passphrase.".format(
                    config_index, len(final_backup_configs), config,
                    len(backup_storage_config_temp_spec)
                ),
                "DEBUG"
            )

            mapped_config = OrderedDict()

            # Process each field mapping from specification
            for field_index, (key, spec_def) in enumerate(backup_storage_config_temp_spec.items(), start=1):
                self.log(
                    "Processing field mapping {0}/{1}: YAML parameter '{2}'. Checking for special "
                    "handling requirements. Special handling flag: {3}.".format(
                        field_index, len(backup_storage_config_temp_spec), key,
                        spec_def.get("special_handling", False)
                    ),
                    "DEBUG"
                )

                # Check for special handling requirement (e.g., nfs_details)
                if spec_def.get("special_handling"):
                    self.log(
                        "Field '{0}' requires special handling via transformation function. Extracting "
                        "transform function from specification and calling with complete configuration "
                        "for custom processing (e.g., NFS mount path correlation).".format(key),
                        "DEBUG"
                    )

                    transform = spec_def.get("transform", lambda x: x)
                    value = transform(config)

                    self.log(
                        "Special handling transformation completed for field '{0}'. Transformed value "
                        "type: {1}. Value contains correlated data from external sources (e.g., NFS "
                        "configurations matched by mount path).".format(key, type(value).__name__),
                        "DEBUG"
                    )
                else:
                    # Standard field extraction using source_key
                    source_key = spec_def.get("source_key", key)

                    self.log(
                        "Field '{0}' uses standard extraction from API source key '{1}'. Retrieving "
                        "value using config.get() for safe extraction.".format(key, source_key),
                        "DEBUG"
                    )

                    value = config.get(source_key)

                    # Apply transformation function if specified and value exists
                    if value is not None:
                        transform = spec_def.get("transform", lambda x: x)
                        value = transform(value)

                        self.log(
                            "Standard field '{0}' extracted and transformed. Source key: '{1}', "
                            "Extracted value type: {2}, Transformation applied: {3}.".format(
                                key, source_key, type(value).__name__,
                                "custom function" if "transform" in spec_def else "identity"
                            ),
                            "DEBUG"
                        )

                # Add non-None values to mapped configuration
                if value is not None:
                    mapped_config[key] = value

                    # Log field mapping with security handling for sensitive data
                    if not spec_def.get("no_log", False):
                        self.log(
                            "Field '{0}' successfully mapped with value: {1} (type: {2}). Added to "
                            "YAML output configuration.".format(key, value, type(value).__name__),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "Field '{0}' successfully mapped with value: [REDACTED] (type: {1}). "
                            "Sensitive data masked in logs due to no_log=True security directive. "
                            "Actual value will be included in YAML output but hidden from logs.".format(
                                key, type(value).__name__
                            ),
                            "DEBUG"
                        )
                else:
                    self.log(
                        "Field '{0}' extraction resulted in None value. Skipping field in YAML output "
                        "as no valid data available from API response. This may be expected for optional "
                        "fields or missing configuration data.".format(key),
                        "DEBUG"
                    )

            # Add mapped configuration to results if not empty
            if mapped_config:
                modified_backup_configs.append(mapped_config)
                self.log(
                    "Configuration {0} transformation completed successfully. Mapped {1} field(s) to "
                    "YAML format. Transformed configuration includes: {2}. Configuration added to "
                    "final results list.".format(
                        config_index, len(mapped_config), list(mapped_config.keys())
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "Configuration {0} transformation resulted in empty mapped configuration. "
                    "Skipping configuration as no valid fields could be extracted. This may indicate "
                    "incomplete or invalid backup storage configuration data from API.".format(config_index),
                    "WARNING"
                )

        result = {"backup_storage_configuration": modified_backup_configs}
        self.log(
            "Backup storage configuration transformation completed successfully. Total configurations "
            "transformed: {0}. Final structure contains 'backup_storage_configuration' key with list "
            "of {0} transformed configuration(s) ready for YAML generation. Each configuration includes "
            "server_type, nfs_details (if applicable), retention policy, and encryption settings.".format(
                len(modified_backup_configs)
            ),
            "INFO"
        )

        return result

    def get_nfs_configuration_details(self):
        """
        Retrieves all NFS configurations for backup storage configuration mapping.

        Description:
            Helper method that fetches all available NFS configurations from the
            Cisco Catalyst Center API. Used internally for correlating backup storage
            configurations with their corresponding NFS server details.

        Args:
            None: Uses instance API connection and logging methods.

        Returns:
            Returns:
                list: A list of NFS configuration dictionaries containing:
                    - spec (dict): Server connection details
                    - server (str): NFS server IP address
                    - sourcePath (str): NFS export source path
                    - nfsPort (int): NFS service port
                    - nfsVersion (str): NFS protocol version
                    - portMapperPort (int): RPC portmapper port
                    - status (dict): Mount and state information
                    - destinationPath (str): Mount destination path
                    - state (str): Configuration state
                    Returns empty list if:
                    - No configurations are available
                    - API calls fail for all function names
                    - Response parsing encounters errorsurns an empty list if no configurations
                        are found or if API calls fail.
        """
        self.log(
            "Retrieving NFS configuration details from Catalyst Center for backup storage "
            "configuration correlation. This operation fetches all registered NFS server "
            "configurations including server IPs, source paths, mount destinations, ports, "
            "and protocol versions. Retrieved data will be used to correlate backup mount "
            "paths with NFS destination paths during backup storage configuration transformation.",
            "DEBUG"
        )

        try:
            api_functions = [
                "get_nfs_configurations",
                "get_all_n_f_s_configurations"
            ]

            response = None

            for function_index, api_function in enumerate(api_functions, start=1):
                try:
                    self.log(
                        "Attempting API call {0}/{1} using function '{2}' from backup API family. "
                        "Executing read-only operation (op_modifies=False) to retrieve NFS server "
                        "configurations. Waiting for API response from Catalyst Center.".format(
                            function_index, len(api_functions), api_function
                        ),
                        "DEBUG"
                    )
                    self.log("Trying API function: {0}".format(api_function), "DEBUG")
                    # Execute API call with current function name
                    response = self.dnac._exec(
                        family="backup",
                        function=api_function,
                        op_modifies=False,
                    )

                    self.log(
                        "Received API response {0}/{1} using function '{2}' completed successfully. Received "
                        "response type: {3}. Response data: {4}. Breaking function iteration loop "
                        "as successful response obtained.".format(
                            function_index, len(api_functions), api_function,
                            type(response).__name__, response
                        ),
                        "DEBUG"
                    )

                    successful_function = api_function
                    break

                except Exception as e:
                    self.log(
                        "API call {0}/{1} using function '{2}' failed with error: {3}. Error type: {4}. "
                        "Continuing to next API function in list if available. Remaining functions to "
                        "try: {5}.".format(
                            function_index, len(api_functions), api_function, str(e),
                            type(e).__name__, len(api_functions) - function_index
                        ),
                        "DEBUG"
                    )
                    continue
            if response is None:
                self.log(
                    "All {0} API function attempts failed. No successful response received from any "
                    "function: {1}. Unable to retrieve NFS configurations for backup storage mapping. "
                    "Returning empty configuration list.".format(len(api_functions), api_functions),
                    "WARNING"
                )
                return []

            self.log(
                "Successfully retrieved API response using function '{0}'. Proceeding with response "
                "parsing to extract NFS configuration list. Response will be checked for dict or list "
                "format to handle different API response structures.".format(successful_function),
                "DEBUG"
            )

            if isinstance(response, dict):
                nfs_configs = (
                    response.get("response", [])
                )
                self.log(
                    "API response is dictionary format. Extracted 'response' key containing {0} NFS "
                    "configuration(s). Response structure indicates standard API response format with "
                    "nested 'response' key. Response key exists: {1}.".format(
                        len(nfs_configs) if isinstance(nfs_configs, list) else 0,
                        "response" in response
                    ),
                    "DEBUG"
                )

            else:
                self.log(
                    "API response is direct list format (not wrapped in dictionary). Total "
                    "configurations: {0}. Response type: {1}. Using response directly as NFS "
                    "configurations list without key extraction.".format(
                        len(nfs_configs) if isinstance(nfs_configs, list) else 0,
                        type(response).__name__
                    ),
                    "DEBUG"
                )
                nfs_configs = response if isinstance(response, list) else []

            self.log(
                "Successfully extracted {0} NFS configuration(s) from API response for backup storage "
                "mapping operations. Configurations will be used for correlating backup mount paths "
                "with NFS destination paths during transform_nfs_details() processing.".format(
                    len(nfs_configs)
                ),
                "INFO"
            )

            if nfs_configs and len(nfs_configs) > 0:
                self.log(
                    "Sample NFS configuration structure (first item) for backup mapping: {0}. This "
                    "structure shows the API response format with nested 'spec' and 'status' sections "
                    "that will be used for mount path correlation and NFS details extraction.".format(
                        nfs_configs[0]
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "No NFS configurations found in API response. Retrieved configuration list is "
                    "empty. This may indicate no NFS servers are configured in Catalyst Center or "
                    "all configurations have been removed. Backup storage configuration correlation "
                    "may use default NFS details values.",
                    "WARNING"
                )

            return nfs_configs

        except Exception as e:
            error_message = (
                "Exception occurred during NFS configuration retrieval for backup storage mapping. "
                "Error type: {0}, Error message: {1}. This may indicate network connectivity issues, "
                "API endpoint unavailability, authentication problems, or API version incompatibility "
                "with Catalyst Center. Returning empty NFS configuration list to allow backup storage "
                "configuration processing to continue with default values.".format(
                    type(e).__name__, str(e)
                )
            )
            self.log(error_message, "WARNING")
            self.set_operation_result("failed", False, error_message, "ERROR")

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates comprehensive YAML configuration files for backup and restore settings.

        Description:
            Orchestrates the complete YAML generation process by processing configuration
            parameters, retrieving data for specified components, and creating structured
            YAML files. Handles component validation, data retrieval coordination, and
            file generation with comprehensive error handling and status reporting.

        Args:
            yaml_config_generator (dict): Configuration parameters including:
                - file_path (str, optional): Target file path for YAML output.
                - component_specific_filters (dict): Component filtering options.
                - generate_all_configurations (bool): Flag for including all components.

        Returns:
            object: Self instance with updated status and results:
                - Sets operation result to success with file path information.
                - Sets operation result to failure with error details if issues occur.
        """
        self.log(
            "Starting YAML configuration file generation workflow for backup and restore "
            "components. Input parameters: {0}. This operation will process component filters, "
            "retrieve configurations from Catalyst Center APIs, transform data to user-friendly "
            "format, and generate structured YAML file compatible with backup_and_restore_workflow_manager "
            "module.".format(yaml_config_generator),
            "DEBUG"
        )

        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No custom file path provided in parameters. Generating default file path using "
                "generate_filename() method. Default path will include module name and timestamp "
                "for uniqueness.",
                "DEBUG"
            )

            file_path = self.generate_filename()

            self.log(
                "Generated default file path for YAML output: '{0}'. File will be created at this "
                "location with timestamp-based naming convention to avoid overwrites.".format(file_path),
                "DEBUG"
            )
        else:
            self.log(
                "Using custom file path provided in parameters: '{0}'. YAML configuration will be "
                "written to this specified location. Ensure path is valid and writable.".format(file_path),
                "DEBUG"
            )

        self.log(
            "Final determined file path for YAML generation: '{0}'. All component configurations "
            "will be aggregated and written to this single file.".format(file_path),
            "DEBUG"
        )
        component_specific_filters = (
            yaml_config_generator.get("component_specific_filters") or {}
        )
        self.log(
            "Extracted component-specific filters from generation parameters. Filter configuration: {0}. "
            "These filters will be passed to component retrieval functions for data filtering during "
            "API calls and transformation.".format(component_specific_filters),
            "DEBUG"
        )

        generate_all_configurations = yaml_config_generator.get("generate_all_configurations", False)

        self.log(
            "Generate all configurations flag: {0}. When True, this flag overrides component_specific_filters.components_list "
            "and includes all available components defined in module schema. When False, uses specified "
            "components_list or defaults to all components if list not provided.".format(generate_all_configurations),
            "DEBUG"
        )

        self.log(
            "Component-specific filters: {0}".format(component_specific_filters),
            "DEBUG",
        )
        self.log(
            "Generate all configurations: {0}".format(generate_all_configurations),
            "DEBUG",
        )

        module_supported_network_elements = self.module_schema.get("network_elements", {})

        self.log(
            "Retrieved module schema network elements configuration. Total supported components: {0}. "
            "Supported components: {1}. This schema defines all available components for backup and "
            "restore operations including API functions, filters, and processing functions.".format(
                len(module_supported_network_elements),
                list(module_supported_network_elements.keys())
            ),
            "DEBUG"
        )

        if generate_all_configurations:
            components_list = list(module_supported_network_elements.keys())
            self.log(
                "Using all available components due to generate_all_configurations=True flag. Components "
                "selected for processing: {0}. This includes all components defined in module schema "
                "regardless of component_specific_filters.components_list setting.".format(components_list),
                "INFO"
            )
        else:
            components_list = component_specific_filters.get(
                "components_list", list(module_supported_network_elements.keys())
            )
            self.log(
                "Using components from component_specific_filters.components_list or defaulting to all "
                "components. Selected components for processing: {0}. Total components to process: {1}.".format(
                    components_list, len(components_list)
                ),
                "DEBUG"
            )

        self.log(
            "Final components list determined for YAML generation workflow: {0}. Each component will be "
            "processed sequentially with its specific API function, filters, and transformation logic.".format(
                components_list
            ),
            "DEBUG"
        )

        config_list = []
        components_processed = 0
        components_skipped = 0
        total_configurations = 0

        self.log(
            "Starting component processing loop. Will iterate through {0} component(s): {1}. Each component "
            "will be validated, retrieved, filtered, transformed, and added to config_list for final YAML "
            "generation.".format(len(components_list), components_list),
            "DEBUG"
        )

        for component_index, component in enumerate(components_list, start=1):
            self.log(
                "Processing component {0}/{1}: '{2}'. Starting validation and data retrieval workflow for "
                "this component. Will check schema support, retrieve network element configuration, and "
                "call component-specific get function.".format(
                    component_index, len(components_list), component
                ),
                "INFO"
            )

            network_element = module_supported_network_elements.get(component)

            if not network_element:
                self.log(
                    "Component '{0}' not found in module schema network elements. This component is not "
                    "supported for backup and restore operations. Incrementing components_skipped counter "
                    "and continuing to next component. Available components: {1}.".format(
                        component, list(module_supported_network_elements.keys())
                    ),
                    "WARNING"
                )
                components_skipped += 1
                continue
            self.log(
                "Component '{0}' validated successfully in module schema. Network element configuration "
                "retrieved: {1}. Proceeding with data retrieval and transformation workflow.".format(
                    component, network_element
                ),
                "DEBUG"
            )

            filters = {
                "global_filters": yaml_config_generator.get("global_filters", {}),
                "component_specific_filters": component_specific_filters
            }

            operation_func = network_element.get("get_function_name")
            self.log(
                "Extracted operation function for component '{0}': {1}. This function will be called with "
                "network_element and filters parameters to retrieve and transform component configurations "
                "from Catalyst Center APIs.".format(component, operation_func),
                "DEBUG"
            )

            if callable(operation_func):
                try:
                    self.log(
                        "Operation function for component '{0}' is callable and valid. Initiating retrieval "
                        "workflow by calling {1}(network_element, filters). This will fetch configurations "
                        "from Catalyst Center, apply filters, and transform data to YAML format.".format(
                            component, operation_func.__name__
                        ),
                        "INFO"
                    )
                    result = operation_func(network_element, filters)
                    self.log(
                        "Component retrieval function completed successfully. Result type: {0}. "
                        "Checking result structure for component data. Expected key: '{1}'.".format(
                            type(result).__name__, component
                        ),
                        "DEBUG"
                    )

                    if component in result and result[component]:
                        config_list.append({component: result[component]})
                        config_count = len(result[component])
                        total_configurations += config_count
                        components_processed += 1
                        self.log(
                            "Successfully added {0} configuration(s) for component '{1}' to config_list. "
                            "Updated statistics: components_processed={2}, total_configurations={3}. "
                            "Component data will be included in final YAML output.".format(
                                config_count, component, components_processed, total_configurations
                            ),
                            "INFO"
                        )
                    else:
                        components_skipped += 1
                        self.log(
                            "No configurations found for component '{0}' after retrieval and filtering. "
                            "Result structure: {1}. Incrementing components_skipped counter. This may "
                            "indicate no data available in Catalyst Center or all data filtered out.".format(
                                component, result
                            ),
                            "WARNING"
                        )
                        if generate_all_configurations:
                            config_list.append({component: []})

                except Exception as e:
                    self.log(
                        "Exception occurred during retrieval for component '{0}'. Error type: {1}, Error "
                        "message: {2}. This may indicate API communication issues, authentication problems, "
                        "or data transformation errors. Incrementing components_skipped counter and "
                        "continuing to next component.".format(component, type(e).__name__, str(e)),
                        "ERROR"
                    )
                    components_skipped += 1
                    if generate_all_configurations:
                        config_list.append({component: []})
                        self.log(
                            "Added empty list for component '{0}' to config_list due to "
                            "generate_all_configurations=True. This ensures component presence in YAML "
                            "output even without data.".format(component),
                            "DEBUG"
                        )
            else:
                self.log(
                    "Invalid operation function for component '{0}'. Function is not callable: {1}. This "
                    "indicates configuration error in module schema. Incrementing components_skipped counter "
                    "and continuing to next component.".format(component, operation_func),
                    "ERROR"
                )
                components_skipped += 1

                if generate_all_configurations:
                    config_list.append({component: []})
                    self.log(
                        "Added empty list for component '{0}' to config_list despite invalid function due "
                        "to generate_all_configurations=True flag.".format(component),
                        "DEBUG"
                    )

        self.log(
            "Component processing loop completed. Final statistics: {0} component(s) processed successfully "
            "with data, {1} component(s) skipped (errors or no data). Total configurations retrieved across "
            "all components: {2}. config_list contains {3} component item(s).".format(
                components_processed, components_skipped, total_configurations, len(config_list)
            ),
            "INFO"
        )

        for config_item in config_list:
            for component, data in config_item.items():
                self.log(
                    "Component '{0}' final configuration count: {1} configuration(s). This component's data "
                    "will be included in YAML output with {1} configuration item(s).".format(
                        component, len(data)
                    ),
                    "INFO"
                )

        if not config_list:
            self.log(
                "config_list is empty after processing all components. No configurations were retrieved or "
                "all components skipped. Checking operation status before setting result.",
                "WARNING"
            )
            if self.status != "failed":
                no_config_message = (
                    "No backup and restore configurations found to process for module '{0}'. "
                    "Verify that NFS servers or backup configurations are set up in "
                    "Catalyst Center. Components attempted: {1}. Components processed: {2}, "
                    "Components skipped: {3}.".format(
                        self.module_name, components_list, components_processed, components_skipped
                    )
                )
                response_data = {
                    "components_processed": components_processed,
                    "components_skipped": components_skipped,
                    "configurations_count": 0,
                    "message": no_config_message,
                    "status": "success"
                }
                self.set_operation_result("success", False, no_config_message, "INFO")

                self.msg = response_data
                self.result["response"] = response_data
                self.log(
                    "Set operation result to success with no configurations message. Response data: {0}. "
                    "Returning early from yaml_config_generator (no YAML file will be created).".format(
                        response_data
                    ),
                    "INFO"
                )
            return self

        final_dict = {"config": config_list}
        self.log(
            "Prepared final dictionary for YAML serialization. Dictionary contains {0} component item(s) "
            "with total {1} configuration(s). Structure: {2}. This data will be written to YAML file at "
            "path: '{3}'.".format(
                len(config_list), total_configurations,
                {k: len(v) for item in config_list for k, v in item.items()},
                file_path
            ),
            "DEBUG"
        )

        if self.write_dict_to_yaml(final_dict, file_path):
            self.log(
                "write_dict_to_yaml() returned True indicating successful YAML file creation. File written "
                "to: '{0}'. Checking operation status before setting success result.".format(file_path),
                "DEBUG"
            )
            if self.status != "failed":
                success_message = "YAML configuration file generated successfully for module '{0}'".format(self.module_name)

                response_data = {
                    "components_processed": components_processed,
                    "components_skipped": components_skipped,
                    "configurations_count": total_configurations,
                    "file_path": file_path,
                    "message": success_message,
                    "status": "success"
                }

                self.set_operation_result("success", True, success_message, "INFO")

                self.msg = response_data
                self.result["response"] = response_data
                self.log(
                    "Set operation result to success with changed=True. YAML file generation completed "
                    "successfully. Final response data: {0}.".format(response_data),
                    "INFO"
                )
        else:
            self.log(
                "write_dict_to_yaml() returned False indicating YAML file creation failure. File path: '{0}'. "
                "This may indicate file permission issues, invalid path, or disk space problems. Checking "
                "operation status before setting failure result.".format(file_path),
                "ERROR"
            )
            if self.status != "failed":
                error_message = (
                    "Failed to write YAML configuration to file: '{0}'. Verify file path is valid, "
                    "directory exists, and write permissions are available. Total configurations prepared "
                    "for writing: {1} across {2} component(s).".format(
                        file_path, total_configurations, components_processed
                    )
                )

                self.log(
                    "Constructing failure response with error details and file path. Message: {0}.".format(
                        error_message
                    ),
                    "ERROR"
                )

                response_data = {
                    "message": error_message,
                    "status": "failed"
                }

                self.set_operation_result("failed", False, error_message, "ERROR")
                self.msg = response_data
                self.result["response"] = response_data
                self.log(
                    "Set operation result to failed. YAML file generation workflow failed at file writing "
                    "stage. Response data: {0}.".format(response_data),
                    "ERROR"
                )

        self.log(
            "Completing yaml_config_generator workflow. Returning self instance with updated status, "
            "results, and response data. Operation status: {0}, Changed: {1}.".format(
                self.status, self.result.get("changed", False)
            ),
            "DEBUG"
        )

        return self

    def get_want(self, config, state):
        """
        Processes and validates configuration parameters for API operations.

        Description:
            Transforms input configuration parameters into the internal 'want' structure
            used throughout the module. Validates parameters and prepares configuration
            data for subsequent processing steps in the backup and restore workflow.

        Args:
            config (dict): The configuration data containing generation parameters,
                component filters, and backup/restore settings.
            state (str): The desired state for the operation (should be 'gathered').

        Returns:
            object: Self instance with updated attributes:
                - self.want (dict): Contains validated configuration ready for processing.
                - Status set to success after parameter validation and preparation.
        """
        self.log(
            "Starting parameter processing for API operations with desired state: '{0}'. "
            "This operation prepares configuration parameters by validating input structure, "
            "transforming playbook config into internal 'want' format, and establishing desired "
            "state for YAML configuration file generation from Catalyst Center backup and restore "
            "settings. State indicates operation mode for downstream processing.".format(state),
            "INFO"
        )

        self.validate_params(config)
        self.log(
            "Parameter validation completed successfully. Configuration conforms to module schema "
            "requirements and is ready for processing. Proceeding with 'want' structure creation "
            "for downstream YAML generation workflow.",
            "DEBUG"
        )

        want = {}
        want["yaml_config_generator"] = config
        self.log(
            "Successfully added yaml_config_generator configuration to 'want' structure. "
            "Configuration includes file_path: '{0}', generate_all_configurations: {1}, "
            "component_specific_filters: {2}, global_filters: {3}. This configuration will be "
            "passed to yaml_config_generator() for component retrieval and YAML file generation.".format(
                config.get("file_path", "auto-generated"),
                config.get("generate_all_configurations", False),
                config.get("component_specific_filters", {}),
                config.get("global_filters", {})
            ),
            "INFO"
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.log(
            "Parameter processing completed successfully. 'want' structure established with state: "
            "'{0}'. Returning self instance for method chaining with check_return_status(). Instance "
            "ready for YAML configuration file generation from Catalyst Center backup and restore "
            "components.".format(state),
            "DEBUG"
        )

        return self

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for brownfield template workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.

        Args:
            None: Uses self.want prepared by get_want() for operation parameters.

        Returns:
            object: Self instance with updated attributes:
                - Operation results set via yaml_config_generator()
                - Execution statistics tracked (operations_executed, operations_skipped)
                - Status updated based on operation outcomes
                - Ready for final result return to Ansible module
        """

        start_time = time.time()
        self.log(
            "Starting 'get_diff_gathered' operation for YAML configuration file generation workflow. "
            "This operation orchestrates the complete brownfield playbook generation process by executing "
            "defined workflow operations, processing desired state parameters from get_want(), calling "
            "component retrieval and transformation functions, generating YAML files, and tracking execution "
            "statistics. Operation start time recorded: {0} for performance monitoring.".format(start_time),
            "DEBUG"
        )
        # Define workflow operations
        workflow_operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]
        operations_executed = 0
        operations_skipped = 0

        # Iterate over operations and process them
        self.log(
            "Beginning iteration over {0} defined workflow operation(s) for sequential processing. Each "
            "operation will be validated for parameter availability, executed if applicable, and tracked "
            "for statistics reporting. Iteration uses enumeration starting at 1 for user-friendly logging "
            "and provides detailed progress visibility throughout workflow execution.".format(
                len(workflow_operations)
            ),
            "DEBUG"
        )

        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
        ):
            self.log(
                "Processing workflow operation iteration {0}/{1}. Operation details: parameter key='{2}', "
                "operation name='{3}', operation function={4}. Checking self.want for parameter availability "
                "using key '{2}'. If parameters exist, operation will be executed; otherwise, operation will "
                "be skipped with warning log.".format(
                    index, len(workflow_operations), param_key, operation_name,
                    operation_func.__name__
                ),
                "DEBUG"
            )
            params = self.want.get(param_key)
            self.log(
                "Retrieved parameters for operation '{0}' from self.want using key '{1}'. Parameters exist: "
                "{2}. If parameters found (not None), operation will proceed with execution wrapped in "
                "try-except for error handling. If parameters not found, operation will be skipped and "
                "operations_skipped counter incremented.".format(
                    operation_name, param_key, params is not None
                ),
                "DEBUG"
            )
            if params:
                self.log(
                    "Iteration {0}/{1}: Parameters found for '{2}' operation. Parameter key: '{3}', Parameters: "
                    "{4}. Starting operation processing with comprehensive error handling. Operation function "
                    "{5} will be called with retrieved parameters. Success will increment operations_executed "
                    "counter; exceptions will set failed status and exit workflow.".format(
                        index, len(workflow_operations), operation_name, param_key, params,
                        operation_func.__name__
                    ),
                    "INFO"
                )

                try:
                    self.log(
                        "Executing operation function {0}() for '{1}' operation with parameters. Function call: "
                        "{0}({2}). Operation will perform YAML configuration generation including component "
                        "retrieval, data transformation, filter application, and file writing. Execution wrapped "
                        "in try-except to catch and handle any exceptions gracefully.".format(
                            operation_func.__name__, operation_name, param_key
                        ),
                        "DEBUG"
                    )
                    operation_func(params)
                    operations_executed += 1
                    self.log(
                        "Operation '{0}' completed successfully. Operation function {1}() executed without errors. "
                        "Incremented operations_executed counter to {2}. Total operations processed successfully: "
                        "{2}/{3}. Continuing to next operation in workflow sequence.".format(
                            operation_name, operation_func.__name__, operations_executed,
                            len(workflow_operations)
                        ),
                        "DEBUG"
                    )
                except Exception as e:
                    error_message = (
                        "Operation '{0}' failed during execution with exception. Operation function: {1}(), "
                        "Exception type: {2}, Exception message: {3}. This error indicates failure in YAML "
                        "generation workflow. Setting operation result to 'failed' status and calling "
                        "check_return_status() to exit module with error details.".format(
                            operation_name, operation_func.__name__, type(e).__name__, str(e)
                        )
                    )

                    self.log(error_message, "ERROR")

                    self.log(
                        "Setting operation result to 'failed' due to exception in operation. Result details: "
                        "status='failed', changed=True, message='{1} operation failed: {2}', log_level='ERROR'. "
                        "Calling check_return_status() which will exit module execution with error status and "
                        "provide detailed error information to Ansible controller.".format(
                            operation_name, str(e)
                        ),
                        "ERROR"
                    )
                    self.set_operation_result(
                        "failed", True,
                        "{0} operation failed: {1}".format(operation_name, str(e)),
                        "ERROR"
                    ).check_return_status()

            else:
                operations_skipped += 1
                self.log(
                    "Iteration {0}/{1}: No parameters found for '{2}' operation in self.want using key '{3}'. "
                    "Operation will be skipped as parameters are required for execution. Incremented "
                    "operations_skipped counter to {4}. Total operations skipped: {4}/{5}. This may indicate "
                    "operation not configured in playbook or parameters not provided. Continuing to next operation "
                    "without failure.".format(
                        index, len(workflow_operations), operation_name, param_key,
                        operations_skipped, len(workflow_operations)
                    ),
                    "WARNING"
                )

        end_time = time.time()
        execution_duration = end_time - start_time

        self.log(
            "Completed 'get_diff_gathered' operation execution. Workflow processing finished for all {0} "
            "defined operation(s). Execution statistics: {1} operation(s) executed successfully, {2} operation(s) "
            "skipped due to missing parameters. Operation start time: {3}, end time: {4}, total execution duration: "
            "{5:.2f} seconds. Performance metrics indicate workflow efficiency. Returning self instance for method "
            "chaining and final result processing.".format(
                len(workflow_operations), operations_executed, operations_skipped,
                start_time, end_time, execution_duration
            ),
            "DEBUG"
        )

        self.log(
            "Workflow execution summary: Total operations={0}, Executed={1}, Skipped={2}, Duration={3:.2f}s. "
            "Returning self instance with updated status, results, and execution statistics. Instance ready for "
            "final check_return_status() validation and module exit with comprehensive execution details.".format(
                len(workflow_operations), operations_executed, operations_skipped, execution_duration
            ),
            "INFO"
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center brownfield backup and restore playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield backup and restore configuration extraction.

    Purpose:
        Initializes and executes the brownfield backup and restore playbook generator
        workflow to extract existing NFS configurations and backup storage settings
        from Cisco Catalyst Center and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create BackupRestorePlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 3.1.3.0)
        5. Validate and sanitize state parameter
        6. Execute input parameter validation
        7. Process each configuration item in the playbook
        8. Handle generate_all_configurations and default component logic
        9. Execute state-specific operations (gathered workflow)
        10. Return results via module.exit_json()

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
        - Minimum Catalyst Center version: 3.1.3.0
        - Introduced APIs for backup and restore configuration retrieval:
            * NFS Configuration (get_all_n_f_s_configurations)
            * Backup Storage Configuration (get_backup_configuration)

    Supported States:
        - gathered: Extract existing backup and restore configurations and generate YAML playbook
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
            - msg (str/dict): Operation result message or structured response
            - response (dict): Detailed operation results with statistics
            - status (str): Operation status ("success")

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

    # Initialize the BackupRestorePlaybookGenerator object
    # This creates the main orchestrator for brownfield backup and restore extraction
    ccc_backup_restore_playbook_generator = BackupRestorePlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_backup_restore_playbook_generator.log(
        "Starting Ansible module execution for brownfield backup and restore playbook "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_backup_restore_playbook_generator.log(
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
    ccc_backup_restore_playbook_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 3.1.3.0 for backup and restore APIs".format(
            ccc_backup_restore_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    if (
        ccc_backup_restore_playbook_generator.compare_dnac_versions(
            ccc_backup_restore_playbook_generator.get_ccc_version(), "3.1.3.0"
        )
        < 0
    ):
        ccc_backup_restore_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Backup and Restore Management Module. Supported versions start from '3.1.3.0' onwards. "
            "Version '3.1.3.0' introduces APIs for retrieving backup and restore settings from "
            "the Catalyst Center".format(
                ccc_backup_restore_playbook_generator.get_ccc_version()
            )
        )

        error_msg = ccc_backup_restore_playbook_generator.msg

        ccc_backup_restore_playbook_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_backup_restore_playbook_generator.set_operation_result(
            "failed", False, ccc_backup_restore_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_backup_restore_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required backup and restore APIs".format(
            ccc_backup_restore_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_backup_restore_playbook_generator.params.get("state")

    ccc_backup_restore_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_backup_restore_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_backup_restore_playbook_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_backup_restore_playbook_generator.supported_states
            )
        )

        ccc_backup_restore_playbook_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_backup_restore_playbook_generator.status = "invalid"
        ccc_backup_restore_playbook_generator.msg = error_msg
        ccc_backup_restore_playbook_generator.check_return_status()

    ccc_backup_restore_playbook_generator.log(
        "State validation passed - using state '{0}' for backup and restore workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_backup_restore_playbook_generator.log(
        "Starting comprehensive input parameter validation for backup and restore playbook configuration",
        "INFO"
    )

    ccc_backup_restore_playbook_generator.validate_input().check_return_status()

    ccc_backup_restore_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet backup and restore module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing and Default Handling
    # ============================================
    config_list = ccc_backup_restore_playbook_generator.validated_config

    ccc_backup_restore_playbook_generator.log(
        "Starting configuration processing and default handling - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    # Handle generate_all_configurations and set component defaults
    for config_index, config_item in enumerate(config_list, start=1):
        ccc_backup_restore_playbook_generator.log(
            "Processing configuration item {0}/{1} for generate_all_configurations and default component handling".format(
                config_index, len(config_list)
            ),
            "DEBUG"
        )

        if config_item.get("generate_all_configurations"):
            ccc_backup_restore_playbook_generator.log(
                "Configuration item {0}: generate_all_configurations=True detected. Setting default "
                "components to include both nfs_configuration and backup_storage_configuration".format(
                    config_index
                ),
                "INFO"
            )

            # Set default components when generate_all_configurations is True
            if not config_item.get("component_specific_filters"):
                config_item["component_specific_filters"] = {
                    "components_list": ["nfs_configuration", "backup_storage_configuration"]
                }
                ccc_backup_restore_playbook_generator.log(
                    "Configuration item {0}: Set default component_specific_filters for generate_all mode: {1}".format(
                        config_index, config_item["component_specific_filters"]
                    ),
                    "DEBUG"
                )
            else:
                ccc_backup_restore_playbook_generator.log(
                    "Configuration item {0}: component_specific_filters already provided in generate_all mode - "
                    "using existing filters: {1}".format(
                        config_index, config_item.get("component_specific_filters")
                    ),
                    "DEBUG"
                )

        elif config_item.get("component_specific_filters") is None:
            ccc_backup_restore_playbook_generator.log(
                "Configuration item {0}: No component_specific_filters provided in normal mode. "
                "Applying default configuration to retrieve both NFS and backup storage components".format(
                    config_index
                ),
                "INFO"
            )

            # Existing fallback logic for when no filters are specified
            ccc_backup_restore_playbook_generator.msg = (
                "No component filters specified, defaulting to both nfs_configuration and backup_storage_configuration."
            )

            config_item["component_specific_filters"] = {
                "components_list": ["nfs_configuration", "backup_storage_configuration"]
            }

            ccc_backup_restore_playbook_generator.log(
                "Configuration item {0}: Applied default component_specific_filters: {1}".format(
                    config_index, config_item["component_specific_filters"]
                ),
                "DEBUG"
            )
        else:
            ccc_backup_restore_playbook_generator.log(
                "Configuration item {0}: component_specific_filters already provided in normal mode - "
                "using existing filters: {1}".format(
                    config_index, config_item.get("component_specific_filters")
                ),
                "DEBUG"
            )

    # Update validated config after default handling
    ccc_backup_restore_playbook_generator.validated_config = config_list

    ccc_backup_restore_playbook_generator.log(
        "Configuration preprocessing completed. Updated validated_config with default component "
        "handling. Final configuration count: {0}".format(len(config_list)),
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    final_config_list = ccc_backup_restore_playbook_generator.validated_config

    ccc_backup_restore_playbook_generator.log(
        "Starting configuration processing loop - will process {0} final configuration "
        "item(s) after default handling".format(len(final_config_list)),
        "INFO"
    )

    for config_index, config_item in enumerate(final_config_list, start=1):
        components_list = config_item.get("component_specific_filters", {}).get("components_list", "all")

        ccc_backup_restore_playbook_generator.log(
            "Processing configuration item {0}/{1} for state '{2}' with components: {3}".format(
                config_index, len(final_config_list), state, components_list
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_backup_restore_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_backup_restore_playbook_generator.reset_values()

        # Collect desired state (want) from configuration
        ccc_backup_restore_playbook_generator.log(
            "Collecting desired state parameters from configuration item {0} - "
            "building want dictionary for backup and restore operations".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_backup_restore_playbook_generator.get_want(
            config_item, state
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_backup_restore_playbook_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1} - will retrieve NFS configurations and "
            "backup storage settings from Catalyst Center".format(state, config_index),
            "INFO"
        )
        ccc_backup_restore_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_backup_restore_playbook_generator.log(
            "Successfully completed processing for configuration item {0}/{1} - "
            "backup and restore data extraction and YAML generation completed".format(
                config_index, len(final_config_list)
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

    ccc_backup_restore_playbook_generator.log(
        "Backup and restore playbook generator module execution completed successfully "
        "at timestamp {0}. Total execution time: {1:.2f} seconds. Processed {2} "
        "configuration item(s) with final status: {3}".format(
            completion_timestamp,
            module_duration,
            len(final_config_list),
            ccc_backup_restore_playbook_generator.status
        ),
        "INFO"
    )

    ccc_backup_restore_playbook_generator.log(
        "Final module result summary: changed={0}, msg_type={1}, response_available={2}".format(
            ccc_backup_restore_playbook_generator.result.get("changed", False),
            type(ccc_backup_restore_playbook_generator.result.get("msg")).__name__,
            "response" in ccc_backup_restore_playbook_generator.result
        ),
        "DEBUG"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_backup_restore_playbook_generator.log(
        "Exiting Ansible module with result containing backup and restore extraction results",
        "DEBUG"
    )

    module.exit_json(**ccc_backup_restore_playbook_generator.result)


if __name__ == "__main__":
    main()

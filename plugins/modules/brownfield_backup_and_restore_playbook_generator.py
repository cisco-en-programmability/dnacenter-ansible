#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbook for Backup and Restore NFS Configuration in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Priyadharshini B, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_backup_and_restore_playbook_generator
short_description: Generate YAML playbook for 'backup_and_restore_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the `backup_and_restore_workflow_manager`
    module, reducing the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
  - The YAML configurations generated represent the NFS server configurations and backup
    storage configurations for backup and restore operations configured on the Cisco Catalyst Center.
  - Supports extraction of NFS configurations, backup storage configurations with encryption and retention policies.

version_added: 6.31.0
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Priyadharshini B (@pbalaku2)
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
            a default file name  "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
          - For example, "backup_and_restore_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
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
              - For example, ["nfs_configuration", "backup_storage_configuration"].
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
                type: str
                required: true
              source_path:
                description:
                  - Source path on the NFS server.
                  - Must be provided along with server_ip for filtering.
                type: str
                required: true
          backup_storage_configuration:
            description:
              - Backup storage configuration filtering options by server type only.
              - If not specified, all backup storage configurations are included.
            type: list
            elements: dict
            suboptions:
              server_type:
                description:
                  - Server type to filter backup configurations by server type.
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

- This module requires Cisco Catalyst Center version 3.1.3.0 or higher
- The module only supports the 'gathered' state for extracting existing configurations
- For NFS configuration filtering, both server_ip and source_path must be provided together
- Backup storage configuration filtering only supports server_type filtering
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
          components_list: ["nfs_configuration", "backup_storage_configuration"]

- name: Generate YAML Configuration for backup storage configuration with server type filter
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

- name: Generate YAML Configuration for specific NFS server (both server_ip and source_path required)
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

- name: Generate YAML Configuration for all configurations
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
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "response": String,
          "version": String
        },
      "msg": String
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
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
    A class for generating playbook files for backup and restore NFS configurations in Cisco Catalyst Center using the GET APIs.
    """

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
        self.module_schema = self.backup_restore_workflow_manager_mapping()
        self.module_name = "backup_and_restore_workflow_manager"

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
            self.log(self.msg, "ERROR")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "file_path": {"type": "str", "required": False},
            "generate_all_configurations": {"type": "bool", "required": False},
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

    def backup_restore_workflow_manager_mapping(self):
        """
        Constructs and returns a structured mapping for managing backup and restore NFS configuration elements.
        This mapping includes associated filters, temporary specification functions, API details,
        and fetch function references used in the backup and restore workflow orchestration process.

        Returns:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a component
                (e.g., 'nfs_configuration') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'backup').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
                - "global_filters": An empty list reserved for global filters applicable across all elements.
        """
        return {
            "network_elements": {
                "nfs_configuration": {
                    "filters": {
                        "server_ip": {"type": "str", "required": False},
                        "source_path": {"type": "str", "required": False},
                    },
                    "reverse_mapping_function": self.nfs_configuration_reverse_mapping_function,
                    "api_function": "get_all_n_f_s_configurations",
                    "api_family": "backup",
                    "get_function_name": self.get_nfs_configurations,
                },
                "backup_storage_configuration": {
                    "filters": {
                        "server_type": {"type": "str", "required": False},
                    },
                    "reverse_mapping_function": self.backup_storage_configuration_reverse_mapping_function,
                    "api_function": "get_backup_configuration",
                    "api_family": "backup",
                    "get_function_name": self.get_backup_storage_configurations,
                },
            },
            "global_filters": {},
        }

    def nfs_configuration_reverse_mapping_function(self, requested_features=None):
        """
        Returns the reverse mapping specification for NFS configuration details.
        Args:
            requested_features (list, optional): List of specific features to include (not used for NFS configs).
        Returns:
            dict: A dictionary containing reverse mapping specifications for NFS configuration details
        """
        self.log("Generating reverse mapping specification for NFS configuration details", "DEBUG")
        return self.nfs_configuration_temp_spec()

    def nfs_configuration_temp_spec(self):
        """
        Constructs a temporary specification for NFS configuration details, defining the structure and types of attributes
        that will be used in the YAML configuration file.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of NFS configuration detail attributes.
        """
        self.log("Generating temporary specification for NFS configuration details.", "DEBUG")
        nfs_configuration_details = OrderedDict({
            "server_ip": {"type": "str", "source_key": "spec.server"},
            "source_path": {"type": "str", "source_key": "spec.sourcePath"},
            "nfs_port": {"type": "int", "source_key": "spec.nfsPort"},
            "nfs_version": {"type": "str", "source_key": "spec.nfsVersion"},
            "nfs_portmapper_port": {"type": "int", "source_key": "spec.portMapperPort"},
        })
        return nfs_configuration_details

    def extract_nested_value(self, data, key_path):
        """
        Extracts value from nested dictionary using dot notation.

        Args:
            data (dict): The source dictionary.
            key_path (str): Dot-separated path to the value (e.g., "spec.server").

        Returns:
            The value at the specified path, or None if not found.
        """
        try:
            keys = key_path.split('.')
            result = data
            for key in keys:
                result = result.get(key)
                if result is None:
                    return None
            return result
        except (AttributeError, TypeError):
            return None

    def get_nfs_configurations(self, network_element, filters):
        """
        Retrieves NFS configuration details based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving NFS configurations.
            filters (dict): A dictionary containing global_filters and component_specific_filters.

        Returns:
            dict: A dictionary containing the modified details of NFS configurations.
        """
        self.log(
            "Starting to retrieve NFS configurations with network element: {0} and filters: {1}".format(
                network_element, filters
            ),
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        nfs_filters = component_specific_filters.get("nfs_configuration", [])

        if nfs_filters:
            for filter_param in nfs_filters:
                # Validate that both server_ip and source_path are provided
                if not all(key in filter_param for key in ["server_ip", "source_path"]):
                    error_msg = (
                        "NFS configuration filter must include both server_ip and source_path together. "
                        "Invalid filter: {0}. Please provide both parameters or remove the filter.".format(filter_param)
                    )
                    self.log(error_msg, "ERROR")

                    result = self.set_operation_result("failed", False, error_msg, "ERROR")

                    self.msg = error_msg
                    self.result["msg"] = error_msg

                    return result

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

            self.log("Received API response: {0}".format(response), "DEBUG")

            if isinstance(response, dict):
                nfs_configs = response.get("response", [])
                # Some APIs return data directly in response
                if not nfs_configs and "data" in response:
                    nfs_configs = response.get("data", [])
                # Some APIs return configurations directly
                if not nfs_configs and "configurations" in response:
                    nfs_configs = response.get("configurations", [])
            else:
                nfs_configs = response if isinstance(response, list) else []

            self.log("Retrieved {0} NFS configurations from Catalyst Center".format(len(nfs_configs)), "INFO")

            if nfs_configs:
                self.log("Sample NFS config structure: {0}".format(nfs_configs[0]), "DEBUG")

            if nfs_filters:
                filtered_configs = []

                for filter_param in nfs_filters:
                    for config in nfs_configs:
                        match = True

                        # Handle different possible structures
                        spec = config.get("spec", config)
                        self.log("Checking NFS config spec: {0}".format(spec), "DEBUG")

                        # Check both server_ip and source_path together
                        server_ip_match = spec.get("server") == filter_param.get("server_ip")
                        source_path_match = spec.get("sourcePath") == filter_param.get("source_path")

                        if not (server_ip_match and source_path_match):
                            match = False

                        self.log(
                            "NFS filter check - server_ip: {0} (expected: {1}), source_path: {2} (expected: {3}), match: {4}".format(
                                spec.get("server"), filter_param.get("server_ip"),
                                spec.get("sourcePath"), filter_param.get("source_path"),
                                match
                            ), "DEBUG"
                        )

                        if match and config not in filtered_configs:
                            filtered_configs.append(config)
                            self.log("NFS configuration matched filter criteria", "INFO")

                final_nfs_configs = filtered_configs
            else:
                final_nfs_configs = nfs_configs

        except Exception as e:
            self.log("Error retrieving NFS configurations: {0}".format(str(e)), "ERROR")

            self.log("API call failed, returning empty NFS configuration list", "WARNING")
            final_nfs_configs = []

        # Modify NFS configuration details using temp_spec
        nfs_configuration_temp_spec = self.nfs_configuration_temp_spec()

        modified_nfs_configs = []
        for config in final_nfs_configs:
            mapped_config = OrderedDict()

            for key, spec_def in nfs_configuration_temp_spec.items():
                source_key = spec_def.get("source_key", key)
                value = self.extract_nested_value(config, source_key)

                if value is None:
                    if key == "server_ip":
                        value = (
                            config.get("spec", {}).get("server")
                        )
                    elif key == "source_path":
                        value = (
                            config.get("spec", {}).get("sourcePath") or
                            config.get("sourcePath")
                        )
                    elif key == "nfs_port":
                        value = (
                            config.get("spec", {}).get("nfsPort") or
                            config.get("nfsPort") or
                            config.get("nfs_port", 2049)
                        )  # Default NFS port
                    elif key == "nfs_version":
                        value = (
                            config.get("spec", {}).get("nfsVersion") or
                            config.get("nfsVersion") or
                            config.get("nfs_version", "nfs4")
                        )  # Default version
                    elif key == "nfs_portmapper_port":
                        value = (
                            config.get("spec", {}).get("portMapperPort") or
                            config.get("portMapperPort") or
                            config.get("nfs_portmapper_port", 111)
                        )  # Default portmapper port

                if value is not None:
                    # Apply any transformation if specified
                    transform = spec_def.get("transform", lambda x: x)
                    mapped_config[key] = transform(value)

            if mapped_config:
                modified_nfs_configs.append(mapped_config)

        modified_nfs_configuration_details = {"nfs_configuration": modified_nfs_configs}
        self.log("Modified NFS configuration details: {0}".format(modified_nfs_configuration_details), "INFO")

        return modified_nfs_configuration_details

    def backup_storage_configuration_reverse_mapping_function(self, requested_features=None):
        """
        Returns the reverse mapping specification for backup storage configuration details.
        """
        self.log("Generating reverse mapping specification for backup storage configuration details", "DEBUG")
        return self.backup_storage_configuration_temp_spec()

    def backup_storage_configuration_temp_spec(self):
        """
        Constructs a temporary specification for backup storage configuration details.
        """
        self.log("Generating temporary specification for backup storage configuration details.", "DEBUG")
        backup_storage_config_details = OrderedDict({
            "server_type": {"type": "str", "source_key": "type"},
            "nfs_details": {
                "type": "dict",
                "special_handling": True,
                "transform": self.transform_nfs_details
            },
            "data_retention_period": {"type": "int", "source_key": "dataRetention"},
            "encryption_passphrase": {"type": "str", "source_key": "encryptionPassphrase", "no_log": True},
        })
        return backup_storage_config_details

    def transform_nfs_details(self, config):
        """
        Transforms backup configuration to extract NFS details.
        """
        self.log("Transforming NFS details from backup configuration", "DEBUG")
        self.log("Input backup config: {0}".format(config), "DEBUG")

        # Get current NFS configurations to match mount path with server details
        current_nfs_configs = self.get_nfs_configuration_details()
        mount_path = config.get("mountPath")

        self.log("Mount path from backup config: {0}".format(mount_path), "DEBUG")
        self.log("Available NFS configs: {0}".format(len(current_nfs_configs)), "DEBUG")

        nfs_details = {
            "server_ip": None,
            "source_path": None,
            "nfs_port": 2049,
            "nfs_version": "nfs4",
            "nfs_portmapper_port": 111
        }

        # Find matching NFS configuration by mount path
        match_found = False
        for nfs_config in current_nfs_configs:
            nfs_mount_path = nfs_config.get("status", {}).get("destinationPath")
            self.log("Checking NFS config mount path: {0} against backup mount path: {1}".format(
                nfs_mount_path, mount_path), "DEBUG")

            if nfs_mount_path == mount_path:
                spec = nfs_config.get("spec", {})
                nfs_details.update({
                    "server_ip": spec.get("server"),
                    "source_path": spec.get("sourcePath"),
                    "nfs_port": spec.get("nfsPort", 2049),
                    "nfs_version": spec.get("nfsVersion", "nfs4"),
                    "nfs_portmapper_port": spec.get("portMapperPort", 111)
                })
                match_found = True
                self.log("Found matching NFS config", "INFO")
                break

        # If no match found, try to extract from backup config directly
        if not match_found:
            self.log("No matching NFS config found, trying direct extraction from backup config", "WARNING")

            # Try to extract NFS details directly from backup configuration
            if "nfs" in config.get("type", "").lower():
                # Sometimes backup config contains NFS details directly
                nfs_details.update({
                    "server_ip": (
                        config.get("server") or
                        config.get("nfs", {}).get("server")
                    ),
                    "source_path": (
                        config.get("sourcePath") or
                        config.get("nfs", {}).get("sourcePath")
                    ),
                    "nfs_port": (
                        config.get("nfsPort") or
                        config.get("nfs", {}).get("port") or
                        2049
                    ),
                    "nfs_version": (
                        config.get("nfsVersion") or
                        config.get("nfs", {}).get("version") or
                        "nfs4"
                    ),
                    "nfs_portmapper_port": (
                        config.get("portMapperPort") or
                        config.get("nfs", {}).get("portMapperPort") or
                        111
                    )
                })

                for key, value in nfs_details.items():
                    if value is not None:
                        self.log("Extracted {0}: {1} from backup config directly".format(key, value), "INFO")

        self.log("Final transformed NFS details: {0}".format(nfs_details), "INFO")
        return nfs_details

    def get_backup_storage_configurations(self, network_element, filters):
        """
        Retrieves backup storage configuration details based on filters.
        Only server_type filtering is supported.
        """
        self.log("Starting to retrieve backup storage configurations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        backup_filters = component_specific_filters.get("backup_storage_configuration", [])

        final_backup_configs = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log("Getting backup configuration using family '{0}' and function '{1}'".format(
            api_family, api_function), "INFO")

        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )

            self.log("Received API response: {0}".format(response), "DEBUG")

            if response is None:
                self.log("API response is None - no backup configuration available", "WARNING")
                backup_config = {}
            elif isinstance(response, dict):
                backup_config = response.get("response", {})
                if not backup_config:
                    backup_config = response.get("data", {})
                    if not backup_config:
                        backup_config = response
            else:
                backup_config = response if isinstance(response, dict) else {}

            self.log("Parsed backup configuration from API response: {0}".format(backup_config), "INFO")

            if backup_config:
                # Apply filters if provided (only server_type filtering supported)
                if backup_filters:
                    self.log("Applying backup configuration filters: {0}".format(backup_filters), "DEBUG")

                    for filter_param in backup_filters:
                        # Validate that only supported filters are used
                        unsupported_filters = []
                        for key in filter_param.keys():
                            if key not in ["server_type"]:
                                unsupported_filters.append(key)

                        if unsupported_filters:
                            error_msg = (
                                "Unsupported backup storage configuration filters: {0}. "
                                "Only 'server_type' filter is supported. "
                                "Invalid filter: {1}".format(unsupported_filters, filter_param)
                            )
                            self.log(error_msg, "ERROR")
                            # Set error result AND explicitly update msg
                            result = self.set_operation_result("failed", False, error_msg, "ERROR")

                            # Explicitly ensure msg field is updated to overwrite any previous success message
                            self.msg = error_msg
                            self.result["msg"] = error_msg

                            return result

                        match = True

                        for key, value in filter_param.items():
                            if key == "server_type":
                                config_value = backup_config.get("type")
                                self.log("Filter check - server_type: expected '{0}', found '{1}'".format(
                                    value, config_value), "DEBUG")

                                if str(config_value) != str(value):
                                    match = False
                                    break

                        if match:
                            final_backup_configs = [backup_config]
                            self.log("Backup configuration matched filter criteria", "INFO")
                            break
                else:
                    final_backup_configs = [backup_config] if backup_config else []
                    self.log("No filters applied - including all backup configurations", "INFO")
            else:
                self.log("No backup configuration found", "INFO")
                final_backup_configs = []

        except Exception as e:
            error_message = "Failed to retrieve backup configuration: {0}".format(str(e))
            self.log(error_message, "ERROR")
            self.log("Exception type: {0}".format(type(e).__name__), "ERROR")
            final_backup_configs = []

        self.log("Transforming {0} backup configurations to user format".format(len(final_backup_configs)), "DEBUG")

        backup_storage_config_temp_spec = self.backup_storage_configuration_temp_spec()
        modified_backup_configs = []

        for config_index, config in enumerate(final_backup_configs):
            self.log("Processing backup config {0}: {1}".format(config_index + 1, config), "DEBUG")

            mapped_config = OrderedDict()

            for key, spec_def in backup_storage_config_temp_spec.items():
                source_key = spec_def.get("source_key", key)

                if spec_def.get("special_handling"):
                    transform = spec_def.get("transform", lambda x: x)
                    value = transform(config)
                else:
                    value = config.get(source_key)

                    if value is not None:
                        transform = spec_def.get("transform", lambda x: x)
                        value = transform(value)

                if value is not None:
                    mapped_config[key] = value
                    if not spec_def.get("no_log", False):
                        self.log("Mapped {0}: {1}".format(key, mapped_config[key]), "DEBUG")
                    else:
                        self.log("Mapped {0}: [REDACTED]".format(key), "DEBUG")

            if mapped_config:
                modified_backup_configs.append(mapped_config)
                self.log("Successfully mapped backup config {0}".format(config_index + 1), "DEBUG")

        result = {"backup_storage_configuration": modified_backup_configs}
        self.log("Final backup storage configuration result: {0} configs transformed".format(
            len(modified_backup_configs)), "INFO")

        return result

    def get_nfs_configuration_details(self):
        """
        Helper method to get all NFS configurations for backup storage configuration mapping.
        """
        self.log("Getting NFS configuration details for backup storage mapping", "DEBUG")

        try:
            # Try multiple possible API function names
            api_functions = [
                "get_nfs_configurations",
                "get_all_n_f_s_configurations"
            ]

            response = None
            successful_function = None

            for api_function in api_functions:
                try:
                    self.log("Trying API function: {0}".format(api_function), "DEBUG")
                    response = self.dnac._exec(
                        family="backup",
                        function=api_function,
                        op_modifies=False,
                    )
                    successful_function = api_function
                    self.log("Received API response using function {0}: {1}".format(api_function, response), "DEBUG")
                    break
                except Exception as e:
                    self.log("API function {0} failed: {1}".format(api_function, str(e)), "DEBUG")
                    continue

            if response is None:
                self.log("All NFS API function attempts failed", "WARNING")
                return []

            self.log("Raw NFS API response: {0}".format(response), "DEBUG")

            if isinstance(response, dict):
                nfs_configs = (
                    response.get("response", []) or
                    response.get("data", []) or
                    response.get("configurations", []) or
                    []
                )
            else:
                nfs_configs = response if isinstance(response, list) else []

            self.log("Extracted {0} NFS configurations for backup mapping".format(len(nfs_configs)), "INFO")

            if nfs_configs and len(nfs_configs) > 0:
                self.log("Sample NFS config for backup mapping: {0}".format(nfs_configs[0]), "DEBUG")

            return nfs_configs

        except Exception as e:
            self.log("Error retrieving NFS configurations for backup mapping: {0}".format(str(e)), "WARNING")
            self.log("Exception details: {0}".format(type(e).__name__), "DEBUG")
            return []

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        """
        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        file_path = yaml_config_generator.get("file_path", self.generate_filename())
        self.log("File path determined: {0}".format(file_path), "DEBUG")

        component_specific_filters = (
            yaml_config_generator.get("component_specific_filters") or {}
        )

        # Handle generate_all_configurations flag
        generate_all_configurations = yaml_config_generator.get("generate_all_configurations", False)

        self.log(
            "Component-specific filters: {0}".format(component_specific_filters),
            "DEBUG",
        )
        self.log(
            "Generate all configurations: {0}".format(generate_all_configurations),
            "DEBUG",
        )

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        # Determine which components to process
        if generate_all_configurations:
            components_list = list(module_supported_network_elements.keys())
            self.log("Using all available components due to generate_all_configurations=True: {0}".format(components_list), "INFO")
        else:
            components_list = component_specific_filters.get(
                "components_list", list(module_supported_network_elements.keys())
            )

        self.log("Components to process: {0}".format(components_list), "DEBUG")

        # Create the structured configuration
        config_list = []
        components_processed = 0

        for component in components_list:
            self.log("Processing component: {0}".format(component), "INFO")

            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Skipping unsupported network element: {0}".format(component),
                    "WARNING",
                )
                continue

            filters = {
                "global_filters": yaml_config_generator.get("global_filters", {}),
                "component_specific_filters": component_specific_filters
            }

            operation_func = network_element.get("get_function_name")
            self.log("Operation function for {0}: {1}".format(component, operation_func), "DEBUG")

            if callable(operation_func):
                try:
                    self.log("Calling operation function for component: {0}".format(component), "INFO")
                    result = operation_func(network_element, filters)

                    if result is self:

                        self.log("Validation error occurred in component: {0}".format(component), "ERROR")
                        return self

                    details = result
                    self.log(
                        "Details retrieved for {0}: {1}".format(component, details), "DEBUG"
                    )

                    # Add the component data as a separate list item
                    if component in details and details[component]:
                        # Create a list item with the component as key
                        component_dict = {component: details[component]}
                        config_list.append(component_dict)
                        components_processed += 1
                        self.log("Successfully added {0} configurations for component {1}".format(
                            len(details[component]), component), "INFO")
                    else:
                        self.log(
                            "No data found for component: {0}".format(component), "WARNING"
                        )
                        # Only add empty component if generate_all_configurations is True
                        if generate_all_configurations:
                            component_dict = {component: []}
                            config_list.append(component_dict)

                except Exception as e:
                    self.log(
                        "Error retrieving data for component {0}: {1}".format(component, str(e)),
                        "ERROR"
                    )
                    import traceback
                    self.log("Full traceback: {0}".format(traceback.format_exc()), "DEBUG")
                    if generate_all_configurations:
                        component_dict = {component: []}
                        config_list.append(component_dict)
            else:
                self.log("No callable operation function for component: {0}".format(component), "ERROR")
                # Add empty component if generate_all_configurations is True
                if generate_all_configurations:
                    component_dict = {component: []}
                    config_list.append(component_dict)

        self.log("Processing summary: {0} components processed successfully out of {1}".format(
            components_processed, len(components_list)), "INFO")

        for config_item in config_list:
            for component, data in config_item.items():
                self.log("Component '{0}': {1} configurations".format(component, len(data)), "INFO")

        if not config_list:
            # Only set this message if there's no existing error status
            if self.status != "failed":
                self.msg = (
                    "No configurations found to process for module '{0}'. This may be because:\n"
                    "- No NFS servers or backup configurations are configured in Catalyst Center\n"
                    "- The API is not available in this version\n"
                    "- User lacks required permissions\n"
                    "- API function names have changed"
                ).format(self.module_name)
                self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        # Use the config_list directly (each component is already a separate list item)
        final_dict = config_list
        self.log("Final dictionary created with {0} component items".format(len(config_list)), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            # Only set success message if there's no existing error
            if self.status != "failed":
                self.msg = {
                    "YAML config generation Task succeeded for module '{0}'.".format(
                        self.module_name
                    ): {"file_path": file_path, "components_processed": components_processed}
                }
                self.set_operation_result("success", True, self.msg, "INFO")
        else:
            # Only set this failure if there's no existing error (don't overwrite validation errors)
            if self.status != "failed":
                self.msg = {
                    "YAML config generation Task failed for module '{0}'.".format(
                        self.module_name
                    ): {"file_path": file_path}
                }
                self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.

        Args:
            config (dict): The configuration data for the backup/restore elements.
            state (str): The desired state ('gathered').
        """
        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        want = {}
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator added to want: {0}".format(
                want["yaml_config_generator"]
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_diff_gathered(self):
        """
        Executes the merge operations for backup and restore configurations in the Cisco Catalyst Center.
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
                result = operation_func(params)

                # Check if operation failed and return immediately
                if result.status == "failed":
                    result.check_return_status()

                result.check_return_status()
            else:
                self.log(
                    "Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                        index, operation_name
                    ),
                    "WARNING",
                )

        # Only set final success message if no errors occurred
        if self.status != "failed":
            self.msg = "Successfully collected all parameters from the playbook for Backup Restore operations."
            self.status = "success"

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
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    # Initialize the BackupRestorePlaybookGenerator object with the module
    ccc_backup_restore_playbook_generator = BackupRestorePlaybookGenerator(module)

    # Check version compatibility
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
        ccc_backup_restore_playbook_generator.set_operation_result(
            "failed", False, ccc_backup_restore_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_backup_restore_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_backup_restore_playbook_generator.supported_states:
        ccc_backup_restore_playbook_generator.status = "invalid"
        ccc_backup_restore_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_backup_restore_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_backup_restore_playbook_generator.validate_input().check_return_status()
    config = ccc_backup_restore_playbook_generator.validated_config

    # Handle generate_all_configurations and set defaults
    for config_item in config:
        if config_item.get("generate_all_configurations"):
            # Set default components when generate_all_configurations is True
            if not config_item.get("component_specific_filters"):
                config_item["component_specific_filters"] = {
                    "components_list": ["nfs_configuration", "backup_storage_configuration"]
                }
                ccc_backup_restore_playbook_generator.log("Set default components for generate_all_configurations", "INFO")
        elif config_item.get("component_specific_filters") is None:
            # Existing fallback logic
            ccc_backup_restore_playbook_generator.msg = (
                "No component filters specified, defaulting to both nfs_configuration and backup_storage_configuration."
            )
            config_item["component_specific_filters"] = {
                "components_list": ["nfs_configuration", "backup_storage_configuration"]
            }

    # Update validated config
    ccc_backup_restore_playbook_generator.validated_config = config

    # Iterate over the validated configuration parameters
    for config_item in ccc_backup_restore_playbook_generator.validated_config:
        ccc_backup_restore_playbook_generator.reset_values()
        ccc_backup_restore_playbook_generator.get_want(config_item, state).check_return_status()
        ccc_backup_restore_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_backup_restore_playbook_generator.result)


if __name__ == "__main__":
    main()

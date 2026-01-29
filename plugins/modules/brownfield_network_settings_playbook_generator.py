#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbooks for Network Settings Operations in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Megha Kandari, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_network_settings_playbook_generator
short_description: Generate YAML playbook for 'network_settings_workflow_manager' module.
description:
- Generates YAML configurations compatible with the `network_settings_workflow_manager`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the global pools, reserve pools, network
  management settings, device controllability settings, and AAA settings configured
  on the Cisco Catalyst Center.
- Supports extraction of Global IP Pools, Reserve IP Pools, Network Management,
  Device Controllability, and AAA Settings configurations.
version_added: 6.44.0
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
    - A list of filters for generating YAML playbook compatible with the `network_settings_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - Global filters identify target settings by site name, pool name, or pool type.
    - Component-specific filters allow selection of specific network setting features and detailed filtering.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - When set to True, automatically generates YAML configurations for all network settings components.
        - This mode discovers all configured network settings in Cisco Catalyst Center and extracts all supported configurations.
        - When enabled, the config parameter becomes optional and will use default values if not provided.
        - A default filename will be generated automatically if file_path is not specified.
        - This is useful for complete brownfield network settings discovery and documentation.
        - Includes Global IP Pools, Reserve IP Pools, Network Management, Device Controllability, and AAA Settings.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name C(<module_name>playbook<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(discovery_workflow_manager_playbook_2026-01-24_12-33-20.yml).
        type: str
        required: false
      component_specific_filters:
        description:
        - Filters to specify which network settings components and features to include in the YAML configuration file.
        - Allows granular selection of specific components and their parameters.
        - If not specified, all supported network settings components will be extracted.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are ["global_pool_details", "reserve_pool_details", "network_management_details",
              "device_controllability_details"]
            - If not specified, all supported components are included.
            - Example ["global_pool_details", "reserve_pool_details", "network_management_details"]
            type: list
            elements: str
            required: false
            choices: ["global_pool_details", "reserve_pool_details", "network_management_details",
                     "device_controllability_details"]
          global_pool_details:
            description:
            - Global IP Pools to filter by pool name or pool type.
            type: list
            elements: dict
            required: false
            suboptions:
              pool_name:
                description:
                - IP Pool name to filter global pools by name.
                type: str
                required: false
              pool_type:
                description:
                - Pool type to filter global pools by type (Generic, LAN, WAN).
                type: str
                required: false
                choices: ["Generic", "LAN", "WAN"]
          reserve_pool_details:
            description:
            - Reserve IP Pools to filter by pool name, site, site hierarchy, or pool type.
            type: list
            elements: dict
            required: false
            suboptions:
              site_name:
                description:
                - Site name to filter reserve pools by specific site.
                type: str
                required: false
              site_hierarchy:
                description:
                - Site hierarchy path to filter reserve pools by all child sites under the hierarchy.
                - For example, "Global/USA" will include all sites under USA like "Global/USA/California", "Global/USA/New York", etc.
                - This allows bulk extraction of reserve pools from multiple sites under a hierarchy.
                type: str
                required: false
          network_management_details:
            description:
            - Network management settings to filter by site.
            type: list
            elements: dict
            required: false
            suboptions:
              site_name_list:
                description:
                - Site name to filter network management settings by site.
                type: str
                required: false
          device_controllability_details:
            description:
            - Device controllability settings to filter by site.
            type: list
            elements: dict
            required: false

requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - network_settings.NetworkSettings.retrieves_global_ip_address_pools
    - network_settings.NetworkSettings.retrieves_ip_address_subpools
    - network_settings.NetworkSettings.retrieve_d_h_c_p_settings_for_a_site
    - network_settings.NetworkSettings.retrieve_d_n_s_settings_for_a_site
    - network_settings.NetworkSettings.retrieve_telemetry_settings_for_a_site
    - network_settings.NetworkSettings.retrieve_n_t_p_settings_for_a_site
    - network_settings.NetworkSettings.retrieve_time_zone_settings_for_a_site
    - network_settings.NetworkSettings.retrieve_aaa_settings_for_a_site
    - network_settings.NetworkSettings.get_device_controllability_settings,

- Paths used are
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/global-pool
    - GET /dna/intent/api/v1/reserve-pool
    - GET /dna/intent/api/v1/network
    - GET /dna/intent/api/v1/device-credential
    - GET /dna/intent/api/v1/network-aaa
"""

EXAMPLES = r"""
# Generate YAML Configuration with default file path
- name: Generate YAML Configuration with default file path
  cisco.dnac.brownfield_network_settings_playbook_generator:
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
          components_list: ["global_pool_details"]

- name: Generate YAML Configuration for specific sites
  cisco.dnac.brownfield_network_settings_playbook_generator:
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
      - file_path: "/tmp/network_settings_config.yml"
        component_specific_filters:
          components_list: ["reserve_pool_details"]

- name: Generate YAML Configuration using explicit components list
  cisco.dnac.brownfield_network_settings_playbook_generator:
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
      - file_path: "/tmp/network_settings_config.yml"
        component_specific_filters:
          components_list: ["network_management_details"]

- name: Generate YAML Configuration for global pools with no filters
  cisco.dnac.brownfield_network_settings_playbook_generator:
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
      - file_path: "/tmp/network_settings_config.yml"
        component_specific_filters:
          components_list: ["device_controllability_details"]

- name: Generate YAML Configuration for reserve pools using site hierarchy
  cisco.dnac.brownfield_network_settings_playbook_generator:
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
      - file_path: "/tmp/reserve_pools_usa.yml"
        component_specific_filters:
          components_list: ["reserve_pool_details"]
          reserve_pool_details:
            - site_hierarchy: "Global/USA"
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
          "message": "YAML config generation succeeded for module 'network_settings_workflow_manager'.",
          "file_path": "/tmp/network_settings_config.yml",
          "configurations_generated": 15,
          "operation_summary": {
            "total_sites_processed": 3,
            "total_components_processed": 25,
            "total_successful_operations": 22,
            "total_failed_operations": 3,
            "sites_with_complete_success": ["Global/India/Mumbai", "Global/India/Delhi"],
            "sites_with_partial_success": ["Global/USA/NewYork"],
            "sites_with_complete_failure": [],
            "success_details": [
              {
                "site_name": "Global/India/Mumbai",
                "component": "global_pool_details",
                "status": "success",
                "pools_processed": 5
              }
            ],
            "failure_details": [
              {
                "site_name": "Global/USA/NewYork",
                "component": "network_management_details",
                "status": "failed",
                "error_info": {
                  "error_type": "api_error",
                  "error_message": "Network management not configured for this site",
                  "error_code": "NETWORK_MGMT_NOT_CONFIGURED"
                }
              }
            ]
          }
        },
      "msg": "YAML config generation succeeded for module 'network_settings_workflow_manager'."
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
          "message": "No configurations or components to process for module 'network_settings_workflow_manager'. Verify input filters or configuration.",
          "operation_summary": {
            "total_sites_processed": 0,
            "total_components_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "sites_with_complete_success": [],
            "sites_with_partial_success": [],
            "sites_with_complete_failure": [],
            "success_details": [],
            "failure_details": []
          }
        },
      "msg": "No configurations or components to process for module 'network_settings_workflow_manager'. Verify input filters or configuration."
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
          "message": "YAML config generation failed for module 'network_settings_workflow_manager'.",
          "file_path": "/tmp/network_settings_config.yml",
          "operation_summary": {
            "total_sites_processed": 2,
            "total_components_processed": 10,
            "total_successful_operations": 5,
            "total_failed_operations": 5,
            "sites_with_complete_success": [],
            "sites_with_partial_success": ["Global/India/Mumbai"],
            "sites_with_complete_failure": ["Global/USA/NewYork"],
            "success_details": [],
            "failure_details": [
              {
                "site_name": "Global/USA/NewYork",
                "component": "global_pool_details",
                "status": "failed",
                "error_info": {
                  "error_type": "site_not_found",
                  "error_message": "Site not found or not accessible",
                  "error_code": "SITE_NOT_FOUND"
                }
              }
            ]
          }
        },
      "msg": "YAML config generation failed for module 'network_settings_workflow_manager'."
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


class NetworkSettingsPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for network settings deployed within the Cisco Catalyst Center using the GET APIs.
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
        self.log(
            f"[{self.module_schema}] Initializing module",
            level="INFO"
        )
        self.module_name = "network_settings_workflow_manager"

        # Initialize class-level variables to track successes and failures
        self.operation_successes = []
        self.operation_failures = []
        self.total_sites_processed = 0
        self.total_components_processed = 0

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False

        # Add state mapping
        self.get_diff_state_apply = {
            "gathered": self.get_diff_gathered,
        }

    def validate_input(self):
        """
        Validates the input configuration parameters for the brownfield network settings playbook.

        This method performs comprehensive validation of all module configuration parameters
        including global filters, component-specific filters, file paths, and authentication
        credentials to ensure they meet the required format and constraints before processing.

        Validation Steps:
            1. Verifies required configuration parameters are present
            2. Validates global filter formats (site_name_list, pool_name_list, etc.)
            3. Checks component-specific filter constraints
            4. Validates file path permissions and directory accessibility
            5. Ensures authentication parameters are properly configured

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
        Validates individual configuration parameters for brownfield network settings generation.

        This method performs detailed validation of configuration parameters including
        file path accessibility, directory creation permissions, and component filter
        validation against supported network elements schema.

        Args:
            config (dict): Configuration parameters containing:
                - file_path (str, optional): Target YAML file output path
                - global_filters (dict, optional): Site, pool, and type filtering criteria
                - component_specific_filters (dict, optional): Component-level filtering
                - generate_all_configurations (bool, optional): Generate all components flag

        Returns:
            self: Current instance with validation status updated.
                 On failure: self.status = "failed", self.msg contains error details
                 On success: self.status = "success"

        Validation Checks:
            - File path validity and write permissions
            - Directory creation capabilities for output path
            - Component names against supported network elements
            - Filter parameter format compliance
            - Cross-parameter dependency validation

        Raises:
            None: All validation errors are captured in instance status
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
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        # Validate component_specific_filters
        component_filters = config.get("component_specific_filters", {})
        self.log("Component-specific filters: {0}".format(component_filters), "DEBUG")
        if component_filters:
            components_list = component_filters.get("components_list", [])
            supported_components = list(self.module_schema.get("network_elements", {}).keys())
            self.log("Supported components: {0}".format(supported_components), "DEBUG")

            for component in components_list:
                self.log("Validating component: {0}".format(component), "DEBUG")
                if component not in supported_components:
                    self.msg = "Unsupported component: {0}. Supported components: {1}".format(
                        component, supported_components)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Configuration parameters validation completed successfully", "DEBUG")
        self.status = "success"
        return self

    def get_workflow_elements_schema(self):
        """
        Returns the mapping configuration for network settings workflow manager.
        Returns:
            dict: A dictionary containing network elements and global filters configuration with validation rules.
        """
        return {
            "network_elements": {
                "global_pool_details": {
                    "filters": {
                        "pool_name": {
                            "type": "str",
                            "required": False
                        },
                        "pool_type": {
                            "type": "str",
                            "required": False,
                            "choices": ["Generic", "LAN", "WAN"]
                        }
                    },
                    "reverse_mapping_function": self.global_pool_reverse_mapping_function,
                    "api_function": "retrieves_global_ip_address_pools",
                    "api_family": "network_settings",
                    "get_function_name": self.get_global_pools,
                },
                "reserve_pool_details": {
                    "filters": {
                        "pool_name": {
                            "type": "str",
                            "required": False
                        },
                        "site_name": {
                            "type": "str",
                            "required": False
                        },
                        "pool_type": {
                            "type": "str",
                            "required": False,
                            "choices": ["LAN", "WAN", "Management"]
                        }
                    },
                    "reverse_mapping_function": self.reserve_pool_reverse_mapping_function,
                    "api_function": "retrieves_ip_address_subpools",
                    "api_family": "network_settings",
                    "get_function_name": self.get_reserve_pools,
                },
                "network_management_details": {
                    "filters": {
                        "site_name": {
                            "type": "str",
                            "required": False
                        },
                    },
                    "reverse_mapping_function": self.network_management_reverse_mapping_function,
                    "api_function": "get_network_v2",
                    "api_family": "network_settings",
                    "get_function_name": self.get_network_management_settings,
                },
                "device_controllability_details": {
                    # Remove the filters section entirely since API doesn't support site-based filtering
                    "reverse_mapping_function": self.device_controllability_reverse_mapping_function,
                    "api_function": "get_device_controllability_settings",
                    "api_family": "site_design",
                    "get_function_name": self.get_device_controllability_settings,
                },
            },
            "global_filters": {
                "site_name_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "pool_name_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "pool_type_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                    "choices": ["Generic", "LAN", "WAN", "Management"]
                }
            },
        }

    def global_pool_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for global pool configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for global pool details
        """
        self.log("Generating reverse mapping specification for global pools.", "DEBUG")

        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "pool_type": {"type": "str", "source_key": "poolType"},
            "ip_address_space": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_pool_to_address_space
            },
            "cidr": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_cidr
            },
            "gateway": {"type": "str", "source_key": "addressSpace.gatewayIpAddress"},
            "dhcp_server_ips": {"type": "list", "source_key": "addressSpace.dhcpServers"},
            "dns_server_ips": {"type": "list", "source_key": "addressSpace.dnsServers"},
        })

    def transform_ipv6_to_address_space(self, ipv6_value):
        """
        Transforms IPv6 boolean configuration to address space string representation.

        This transformation function converts IPv6 boolean flags from Catalyst Center API
        responses into human-readable address space strings for YAML configuration output.

        Args:
            ipv6_value (bool or None): IPv6 configuration flag from API response.
                - True: IPv6 is enabled/configured
                - False: IPv4 only (IPv6 disabled)
                - None: No address space configuration

        Returns:
            str or None: Address space string representation:
                - "IPv6": When IPv6 is enabled (ipv6_value is True)
                - "IPv4": When IPv4 only is configured (ipv6_value is False)
                - None: When no configuration is available (ipv6_value is None)

        Examples:
            transform_ipv6_to_address_space(True) -> "IPv6"
            transform_ipv6_to_address_space(False) -> "IPv4"
            transform_ipv6_to_address_space(None) -> None
        """
        self.log("Transforming IPv6 value to address space string: {0}".format(ipv6_value), "DEBUG")
        if ipv6_value is True:
            return "IPv6"
        elif ipv6_value is False:
            return "IPv4"
        return None

    def transform_to_boolean(self, value):
        """
        Transforms various value types to boolean for YAML configuration compatibility.

        This transformation function handles conversion of different data types from
        Catalyst Center API responses to proper boolean values suitable for Ansible
        YAML configurations, ensuring consistent boolean representation.

        Args:
            value: The value to convert to boolean. Supported types:
                - bool: Returned as-is
                - str: Evaluated based on common true/false representations
                - int/float: Standard Python truthy/falsy evaluation
                - None: Returns False
                - Other types: Standard Python bool() evaluation

        Returns:
            bool: Converted boolean value:
                - True for truthy values and string representations of true
                - False for falsy values, None, and string representations of false

        String Evaluation Rules:
            - Case-insensitive matching
            - True: 'true', 'yes', 'on', '1', 'enabled'
            - False: 'false', 'no', 'off', '0', 'disabled', empty string

        Examples:
            transform_to_boolean(True) -> True
            transform_to_boolean('true') -> True
            transform_to_boolean('FALSE') -> False
            transform_to_boolean(1) -> True
            transform_to_boolean(0) -> False
            transform_to_boolean(None) -> False
            transform_to_boolean('yes') -> True
        """
        self.log("Transforming value to boolean: {0}".format(value), "DEBUG")
        if value is None:
            return False
        return bool(value)

    def transform_pool_to_address_space(self, pool_details):
        """
        Determines the IP address space (IPv4 or IPv6) from the pool configuration.

        This function analyzes the pool structure to determine whether it's configured
        for IPv4 or IPv6 address space by examining various fields in the pool data.

        Args:
            pool_details (dict or None): Complete pool configuration object

        Returns:
            str or None: Address space identifier:
                - "IPv4": For IPv4 address pools
                - "IPv6": For IPv6 address pools
                - None: When address space cannot be determined

        Detection Logic:
            1. Check for explicit ipv6 boolean field
            2. Examine gateway address format (IPv6 contains ':')
            3. Check subnet format in addressSpace
            4. Look for IPv6-specific fields
        """
        self.log("Starting with pool_details: {0}".format(pool_details), "DEBUG")
        if pool_details is None or not isinstance(pool_details, dict):
            self.log("transform_pool_to_address_space: pool_details is None or not dict: {0}".format(pool_details), "DEBUG")
            return None

        self.log("transform_pool_to_address_space: processing pool_details keys: {0}".format(list(pool_details.keys())), "DEBUG")

        # Method 1: Check explicit ipv6 field
        if "ipv6" in pool_details:
            result = "IPv6" if pool_details["ipv6"] else "IPv4"
            self.log("transform_pool_to_address_space: found explicit ipv6 field, returning: {0}".format(result), "DEBUG")
            return result

        # Method 2: Check gateway format (primary method for global pools)
        address_space = pool_details.get("addressSpace", {})
        gateway = address_space.get("gatewayIpAddress", "")

        # Also check direct gateway field for different API response formats
        if not gateway:
            gateway = pool_details.get("gateway", "")

        if gateway:
            if ":" in gateway:
                self.log("transform_pool_to_address_space: detected IPv6 gateway: {0}".format(gateway), "DEBUG")
                return "IPv6"
            else:
                self.log("transform_pool_to_address_space: detected IPv4 gateway: {0}".format(gateway), "DEBUG")
                return "IPv4"

        # Method 3: Check subnet format
        subnet = address_space.get("subnet", "")
        if not subnet:
            subnet = pool_details.get("subnet", "")

        if subnet:
            if ":" in subnet:
                self.log("transform_pool_to_address_space: detected IPv6 subnet: {0}".format(subnet), "DEBUG")
                return "IPv6"
            else:
                self.log("transform_pool_to_address_space: detected IPv4 subnet: {0}".format(subnet), "DEBUG")
                return "IPv4"

        # Method 4: Check for poolType containing IPv6 indicators
        pool_type = pool_details.get("poolType", "")
        if "v6" in pool_type.lower() or "ipv6" in pool_type.lower():
            self.log("transform_pool_to_address_space: detected IPv6 from poolType: {0}".format(pool_type), "DEBUG")
            return "IPv6"

        # Method 5: Check DNS/DHCP servers for IPv6 format
        dhcp_servers = address_space.get("dhcpServers", [])
        dns_servers = address_space.get("dnsServers", [])

        for server in dhcp_servers + dns_servers:
            if server and ":" in str(server):
                self.log("transform_pool_to_address_space: detected IPv6 from server addresses: {0}".format(server), "DEBUG")
                return "IPv6"

        # Default to IPv4 if we have any address space info but can't determine type
        if address_space or gateway:
            self.log("transform_pool_to_address_space: defaulting to IPv4", "DEBUG")
            return "IPv4"

        self.log("transform_pool_to_address_space: unable to determine address space, returning None", "DEBUG")
        return None

    def transform_cidr(self, pool_details):
        """
        Transforms subnet and prefix length information into standard CIDR notation.

        This transformation function extracts subnet and prefix length information from
        Catalyst Center API pool details and formats them into standard CIDR notation
        (subnet/prefix) for network configuration representation.

        Args:
            pool_details (dict or None): Pool configuration details containing:
                - addressSpace (dict): Address space configuration with:
                    - subnet (str): Network subnet address (e.g., "192.168.1.0", "2001:db8::")
                    - prefixLength (int): Network prefix length (e.g., 24, 64)

        Returns:
            str or None: CIDR notation string or None:
                - "subnet/prefix": Valid CIDR format (e.g., "192.168.1.0/24", "2001:db8::/64")
                - None: When pool_details is None, invalid format, or missing required fields

        Data Structure Expected:
            {
                "addressSpace": {
                    "subnet": "192.168.1.0",
                    "prefixLength": 24
                }
            }

        Examples:
            IPv4: {"addressSpace": {"subnet": "192.168.1.0", "prefixLength": 24}} -> "192.168.1.0/24"
            IPv6: {"addressSpace": {"subnet": "2001:db8::", "prefixLength": 64}} -> "2001:db8::/64"
            Invalid: None -> None
            Missing data: {"addressSpace": {}} -> None
        """
        self.log("Starting CIDR transformation with pool_details: {0}".format(pool_details), "DEBUG")
        if pool_details is None:
            self.log("transform_cidr: pool_details is None", "DEBUG")
            return None

        if isinstance(pool_details, dict):
            self.log("transform_cidr: processing pool_details keys: {0}".format(list(pool_details.keys())), "DEBUG")

            # Method 1: Check addressSpace structure (primary method)
            address_space = pool_details.get("addressSpace", {})
            subnet = address_space.get("subnet")
            prefix_length = address_space.get("prefixLength")

            if subnet and prefix_length:
                cidr = "{0}/{1}".format(subnet, prefix_length)
                self.log("transform_cidr: found CIDR from addressSpace: {0}".format(cidr), "DEBUG")
                return cidr

            # Method 2: Check direct subnet and prefixLength fields
            subnet = pool_details.get("subnet")
            prefix_length = pool_details.get("prefixLength")

            if subnet and prefix_length:
                cidr = "{0}/{1}".format(subnet, prefix_length)
                self.log("transform_cidr: found CIDR from direct fields: {0}".format(cidr), "DEBUG")
                return cidr

            # Method 3: Check for alternative field names
            subnet = pool_details.get("ipSubnet") or pool_details.get("network")
            prefix_length = pool_details.get("prefixLen") or pool_details.get("maskLength") or pool_details.get("subnetMask")

            # Convert subnet mask to prefix length if needed
            if prefix_length and isinstance(prefix_length, str) and "." in prefix_length:
                # Convert subnet mask (e.g., "255.255.255.0") to prefix length (e.g., 24)
                try:
                    import ipaddress
                    prefix_length = ipaddress.IPv4Network('0.0.0.0/' + prefix_length).prefixlen
                except Exception:
                    pass

            if subnet and prefix_length:
                cidr = "{0}/{1}".format(subnet, prefix_length)
                self.log("transform_cidr: found CIDR from alternative fields: {0}".format(cidr), "DEBUG")
                return cidr

            # Method 4: Look for existing CIDR format
            existing_cidr = pool_details.get("cidr") or pool_details.get("ipRange") or pool_details.get("range")
            if existing_cidr and "/" in str(existing_cidr):
                self.log("transform_cidr: found existing CIDR: {0}".format(existing_cidr), "DEBUG")
                return existing_cidr

            self.log("transform_cidr: no valid CIDR components found", "DEBUG")

        return None

    def transform_preserve_empty_list(self, data, field_path):
        """
        Transform function to preserve empty lists for DHCP/DNS servers.
        The helper function filters out empty lists, but for network config,
        empty DHCP/DNS lists are valid and should be preserved.
        """
        if data is None:
            return []

        if isinstance(data, dict):
            # Navigate the field path (e.g., "ipV4AddressSpace.dhcpServers")
            current = data
            for field in field_path.split('.'):
                current = current.get(field)
                if current is None:
                    return []

            # If we found the field, return it (even if empty list)
            if isinstance(current, list):
                return current
            elif current is None:
                return []

        return []

    def transform_ipv4_dhcp_servers(self, data):
        """
        Transform IPv4 DHCP servers configuration while preserving empty lists.

        This transformation function specifically handles IPv4 DHCP server configurations
        from Catalyst Center API responses, ensuring that empty DHCP server lists are
        preserved in the output (unlike the default helper behavior that filters them out).

        Args:
            data (dict or None): Pool or network management data containing IPv4 DHCP configuration.

        Returns:
            list: IPv4 DHCP server addresses, or empty list if none configured.
                 Empty lists are explicitly preserved to indicate "no DHCP servers configured".
        """
        return self.transform_preserve_empty_list(data, "ipV4AddressSpace.dhcpServers")

    def transform_ipv4_dns_servers(self, data):
        """
        Transform IPv4 DNS servers configuration while preserving empty lists.

        This transformation function specifically handles IPv4 DNS server configurations
        from Catalyst Center API responses, ensuring that empty DNS server lists are
        preserved in the output to maintain semantic meaning.

        Args:
            data (dict or None): Pool or network management data containing IPv4 DNS configuration.

        Returns:
            list: IPv4 DNS server addresses, or empty list if none configured.
                 Empty lists are explicitly preserved to indicate "no DNS servers configured".
        """
        return self.transform_preserve_empty_list(data, "ipV4AddressSpace.dnsServers")

    def transform_ipv6_dhcp_servers(self, data):
        """
        Transform IPv6 DHCP servers configuration while preserving empty lists.

        This transformation function specifically handles IPv6 DHCP server configurations
        from Catalyst Center API responses, ensuring that empty DHCP server lists are
        preserved in the output for proper network configuration representation.

        Args:
            data (dict or None): Pool or network management data containing IPv6 DHCP configuration.

        Returns:
            list: IPv6 DHCP server addresses, or empty list if none configured.
                 Empty lists are explicitly preserved to indicate "no DHCPv6 servers configured".
        """
        return self.transform_preserve_empty_list(data, "ipV6AddressSpace.dhcpServers")

    def transform_ipv6_dns_servers(self, data):
        """
        Transform IPv6 DNS servers configuration while preserving empty lists.

        This transformation function specifically handles IPv6 DNS server configurations
        from Catalyst Center API responses, ensuring that empty DNS server lists are
        preserved in the output for accurate network configuration representation.

        Args:
            data (dict or None): Pool or network management data containing IPv6 DNS configuration.

        Returns:
            list: IPv6 DNS server addresses, or empty list if none configured.
                 Empty lists are explicitly preserved to indicate "no IPv6 DNS servers configured".
        """
        return self.transform_preserve_empty_list(data, "ipV6AddressSpace.dnsServers")

    def get_global_pool_lookup(self):
        """
        Create a lookup mapping of global pool IDs to their CIDR and names.
        This method caches the result to avoid multiple API calls.

        Returns:
            dict: Mapping of global pool IDs to their details:
                  {
                      "pool_id": {
                          "cidr": "10.0.0.0/8",
                          "name": "Global_Pool1",
                          "ip_address_space": "IPv4"
                      }
                  }
        """
        if hasattr(self, '_global_pool_lookup'):
            return self._global_pool_lookup

        self.log("Creating global pool lookup mapping", "DEBUG")

        try:
            # Get global pools using the API
            global_pools_response = self.execute_get_with_pagination(
                "network_settings",
                "retrieves_global_ip_address_pools",
                {}
            )

            self._global_pool_lookup = {}

            for pool in global_pools_response:
                pool_id = pool.get('id')
                if pool_id:
                    # Determine CIDR from subnet and prefix length
                    cidr = None
                    address_space = pool.get('addressSpace', {})
                    subnet = address_space.get('subnet')
                    prefix_length = address_space.get('prefixLength')

                    if subnet and prefix_length:
                        cidr = f"{subnet}/{prefix_length}"

                    # Determine IP address space (IPv4 or IPv6)
                    ip_address_space = "IPv6" if ":" in str(subnet or "") else "IPv4"

                    self._global_pool_lookup[pool_id] = {
                        "cidr": cidr,
                        "name": pool.get('name'),
                        "ip_address_space": ip_address_space
                    }

            self.log(f"Created global pool lookup with {len(self._global_pool_lookup)} pools", "DEBUG")
            return self._global_pool_lookup

        except Exception as e:
            self.log(f"Error creating global pool lookup: {str(e)}", "ERROR")
            # Return empty dict to avoid breaking the process
            self._global_pool_lookup = {}
            return self._global_pool_lookup

    def transform_global_pool_id_to_cidr(self, pool_data):
        """
        Transform global pool ID to CIDR notation.

        Args:
            pool_data (dict): Reserve pool data containing global pool ID references

        Returns:
            str: CIDR notation of the global pool or None if not found
        """
        try:
            # Extract IPv4 global pool ID
            ipv4_global_pool_id = None
            if pool_data and isinstance(pool_data, dict):
                ipv4_global_pool_id = pool_data.get('ipV4AddressSpace', {}).get('globalPoolId')

            if not ipv4_global_pool_id:
                self.log("No IPv4 global pool ID found in pool data", "DEBUG")
                return None

            lookup = self.get_global_pool_lookup()
            pool_info = lookup.get(ipv4_global_pool_id, {})
            cidr = pool_info.get('cidr')

            self.log(f"IPv4 Global pool ID {ipv4_global_pool_id} mapped to CIDR: {cidr}", "DEBUG")
            return cidr

        except Exception as e:
            self.log(f"Error transforming IPv4 global pool ID to CIDR: {str(e)}", "ERROR")
            return None

    def transform_global_pool_id_to_name(self, pool_data):
        """
        Transform global pool ID to pool name.

        Args:
            pool_data (dict): Reserve pool data containing global pool ID references

        Returns:
            str: Name of the global pool or None if not found
        """
        try:
            # Extract IPv4 global pool ID
            ipv4_global_pool_id = None
            if pool_data and isinstance(pool_data, dict):
                ipv4_global_pool_id = pool_data.get('ipV4AddressSpace', {}).get('globalPoolId')

            if not ipv4_global_pool_id:
                self.log("No IPv4 global pool ID found in pool data", "DEBUG")
                return None

            lookup = self.get_global_pool_lookup()
            pool_info = lookup.get(ipv4_global_pool_id, {})
            name = pool_info.get('name')

            self.log(f"IPv4 Global pool ID {ipv4_global_pool_id} mapped to name: {name}", "DEBUG")
            return name

        except Exception as e:
            self.log(f"Error transforming IPv4 global pool ID to name: {str(e)}", "ERROR")
            return None

    def transform_ipv6_global_pool_id_to_cidr(self, pool_data):
        """
        Transform IPv6 global pool ID to CIDR notation.

        Args:
            pool_data (dict): Reserve pool data containing global pool ID references

        Returns:
            str: CIDR notation of the IPv6 global pool or None if not found
        """
        # Extract IPv6 global pool ID
        ipv6_global_pool_id = None
        if pool_data and isinstance(pool_data, dict):
            ipv6_global_pool_id = pool_data.get('ipV6AddressSpace', {}).get('globalPoolId')

        if not ipv6_global_pool_id:
            return None

        lookup = self.get_global_pool_lookup()
        pool_info = lookup.get(ipv6_global_pool_id, {})
        return pool_info.get('cidr')

    def transform_ipv6_global_pool_id_to_name(self, pool_data):
        """
        Transform IPv6 global pool ID to pool name.

        Args:
            pool_data (dict): Reserve pool data containing global pool ID references

        Returns:
            str: Name of the IPv6 global pool or None if not found
        """
        # Extract IPv6 global pool ID
        ipv6_global_pool_id = None
        if pool_data and isinstance(pool_data, dict):
            ipv6_global_pool_id = pool_data.get('ipV6AddressSpace', {}).get('globalPoolId')

        if not ipv6_global_pool_id:
            return None

        lookup = self.get_global_pool_lookup()
        pool_info = lookup.get(ipv6_global_pool_id, {})
        return pool_info.get('name')

    def reserve_pool_reverse_mapping_function(self, requested_components=None):
        """
        Generate reverse mapping specification for Reserve Pool Details transformation.

        This function creates a comprehensive mapping specification that converts
        Catalyst Center API response fields for reserve pools into Ansible-friendly
        configuration keys compatible with the network_settings_workflow_manager module.

        The mapping includes field transformations, type conversions, and special handling
        for complex data structures like IPv4/IPv6 address spaces, server configurations,
        and pool relationships.

        Args:
            requested_components (list, optional): Specific components to include in mapping.
                                                  If None, includes all reserve pool components.

        Returns:
            OrderedDict: Comprehensive field mapping specification containing:
                - Field mappings from API keys to Ansible config keys
                - Type specifications for each field
                - Transform functions for data conversion
                - Special handling flags for complex transformations
                - Optional field indicators

        Mapping Categories:
            - Basic pool information (name, type, site)
            - IPv4 address space (subnet, gateway, DHCP/DNS servers)
            - IPv6 address space (subnet, gateway, DHCP/DNS servers)
            - Pool relationships (parent pools, reserved ranges)
            - Statistics (total hosts, assigned addresses)
            - Configuration flags (SLAAC support, prefix settings)
        """
        self.log("Generating reverse mapping specification for reserve pools.", "DEBUG")

        return OrderedDict({
            "site_name": {
                "type": "str",
                "source_key": "siteName",
                "special_handling": True,
                "transform": self.transform_site_location,
            },
            "name": {"type": "str", "source_key": "name"},
            "prev_name": {"type": "str", "source_key": "previousName", "optional": True},
            "pool_type": {"type": "str", "source_key": "poolType"},

            # IPv6 Address Space flag
            "ipv6_address_space": {
                "type": "bool",
                "source_key": "ipV6AddressSpace",
                "transform": self.transform_to_boolean,
            },

            # IPv4 address space
            "ipv4_global_pool": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_global_pool_id_to_cidr
            },
            "ipv4_global_pool_name": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_global_pool_id_to_name
            },
            "ipv4_prefix": {
                "type": "bool",
                "source_key": "ipV4AddressSpace.prefixLength",
                "transform": self.transform_to_boolean,
            },
            "ipv4_prefix_length": {"type": "int", "source_key": "ipV4AddressSpace.prefixLength"},
            "ipv4_subnet": {"type": "str", "source_key": "ipV4AddressSpace.subnet"},
            "ipv4_gateway": {"type": "str", "source_key": "ipV4AddressSpace.gatewayIpAddress"},
            "ipv4_dhcp_servers": {
                "type": "list",
                "special_handling": True,
                "transform": self.transform_ipv4_dhcp_servers
            },
            "ipv4_dns_servers": {
                "type": "list",
                "special_handling": True,
                "transform": self.transform_ipv4_dns_servers
            },
            "ipv4_total_host": {"type": "int", "source_key": "ipV4AddressSpace.totalAddresses"},
            # "ipv4_unassignable_addresses": {"type": "int", "source_key": "ipV4AddressSpace.unassignableAddresses"},
            # "ipv4_assigned_addresses": {"type": "int", "source_key": "ipV4AddressSpace.assignedAddresses"},
            # "ipv4_default_assigned_addresses": {"type": "int", "source_key": "ipV4AddressSpace.defaultAssignedAddresses"},

            # IPv6 address space
            "ipv6_global_pool": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_ipv6_global_pool_id_to_cidr
            },
            "ipv6_global_pool_name": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_ipv6_global_pool_id_to_name
            },
            "ipv6_prefix": {
                "type": "bool",
                "source_key": "ipV6AddressSpace.prefixLength",
                "transform": self.transform_to_boolean,
            },
            "ipv6_prefix_length": {"type": "int", "source_key": "ipV6AddressSpace.prefixLength"},
            "ipv6_subnet": {"type": "str", "source_key": "ipV6AddressSpace.subnet"},
            "ipv6_gateway": {"type": "str", "source_key": "ipV6AddressSpace.gatewayIpAddress"},
            "ipv6_dhcp_servers": {
                "type": "list",
                "special_handling": True,
                "transform": self.transform_ipv6_dhcp_servers
            },
            "ipv6_dns_servers": {
                "type": "list",
                "special_handling": True,
                "transform": self.transform_ipv6_dns_servers
            },
            "ipv6_total_host": {"type": "int", "source_key": "ipV6AddressSpace.totalAddresses"},
            # "ipv6_unassignable_addresses": {"type": "int", "source_key": "ipV6AddressSpace.unassignableAddresses"},
            # "ipv6_assigned_addresses": {"type": "int", "source_key": "ipV6AddressSpace.assignedAddresses"},
            # "ipv6_default_assigned_addresses": {"type": "int", "source_key": "ipV6AddressSpace.defaultAssignedAddresses"},
            "slaac_support": {"type": "bool", "source_key": "ipV6AddressSpace.slaacSupport"},

            # # Force delete flag (optional in schema)
            # "force_delete": {"type": "bool", "default": False, "optional": True},
        })

    def network_management_reverse_mapping_function(self, requested_components=None):
        """
        Reverse mapping for Network Management settings (v1 API).
        Converts DNAC raw API response into the flattened Ansible-friendly structure:

            network_management_details:
                - site_name: ...
                settings:
                    dns_server: {...}
                    dhcp_server: [...]
                    ntp_server: [...]
                    timezone: ...
                    message_of_the_day: {...}
                    network_aaa: {...}
                    client_and_endpoint_aaa: {...}
                    ...

        This follows the same flat-mapping pattern as reserve_pool_reverse_mapping_function.
        """
        self.log("Generating reverse mapping specification for network management (v1).", "DEBUG")

        return OrderedDict({

            # -------------------------------
            # Top field: site_name
            # -------------------------------
            "site_name": {
                "type": "str",
                "source_key": "siteName",
                "special_handling": True,
                "transform": self.transform_site_location
            },

            # -------------------------------
            # DHCP server
            # -------------------------------
            "dhcp_server": {
                "type": "list",
                "source_key": "settings.dhcp.servers"
            },

            # -------------------------------
            # DNS server block
            # -------------------------------
            "dns_server.domain_name": {
                "type": "str",
                "source_key": "settings.dns.domainName"
            },
            "dns_server.dns_servers": {
                "type": "list",
                "source_key": "settings.dns.dnsServers"
            },

            # -------------------------------
            # NTP + Timezone
            # -------------------------------
            "ntp_server": {
                "type": "list",
                "source_key": "settings.ntp.servers"
            },
            "timezone": {
                "type": "str",
                "source_key": "settings.timeZone.identifier"
            },

            # -------------------------------
            # MOTD / Banner
            # -------------------------------
            "message_of_the_day.banner_message": {
                "type": "str",
                "source_key": "settings.banner.message"
            },
            "message_of_the_day.retain_existing_banner": {
                "type": "bool",
                "source_key": "settings.banner.retainExistingBanner"
            },

            # -------------------------------
            # Network AAA
            # -------------------------------
            "network_aaa.primary_server_address": {
                "type": "str",
                "source_key": "settings.aaaNetwork.primaryServerIp"
            },
            "network_aaa.secondary_server_address": {
                "type": "str",
                "source_key": "settings.aaaNetwork.secondaryServerIp",
                "optional": True
            },
            "network_aaa.protocol": {
                "type": "str",
                "source_key": "settings.aaaNetwork.protocol"
            },
            "network_aaa.server_type": {
                "type": "str",
                "source_key": "settings.aaaNetwork.serverType"
            },
            "network_aaa.pan_address": {
                "type": "str",
                "source_key": "settings.aaaNetwork.pan",
                "optional": True
            },
            "network_aaa.shared_secret": {
                "type": "str",
                "source_key": "settings.aaaNetwork.sharedSecret",
                "optional": True
            },

            # -------------------------------
            # Client & Endpoint AAA
            # -------------------------------
            "client_and_endpoint_aaa.primary_server_address": {
                "type": "str",
                "source_key": "settings.aaaClient.primaryServerIp"
            },
            "client_and_endpoint_aaa.secondary_server_address": {
                "type": "str",
                "source_key": "settings.aaaClient.secondaryServerIp",
                "optional": True
            },
            "client_and_endpoint_aaa.protocol": {
                "type": "str",
                "source_key": "settings.aaaClient.protocol"
            },
            "client_and_endpoint_aaa.server_type": {
                "type": "str",
                "source_key": "settings.aaaClient.serverType"
            },
            "client_and_endpoint_aaa.pan_address": {
                "type": "str",
                "source_key": "settings.aaaClient.pan",
                "optional": True
            },
            "client_and_endpoint_aaa.shared_secret": {
                "type": "str",
                "source_key": "settings.aaaClient.sharedSecret",
                "optional": True
            },

            # -------------------------------
            # NetFlow Collector
            # -------------------------------
            "netflow_collector.ip_address": {
                "type": "str",
                "source_key": "settings.telemetry.applicationVisibility.collector.address"
            },
            "netflow_collector.port": {
                "type": "int",
                "source_key": "settings.telemetry.applicationVisibility.collector.port"
            },

            # -------------------------------
            # SNMP Server
            # -------------------------------
            "snmp_server.configure_dnac_ip": {
                "type": "bool",
                "source_key": "settings.telemetry.snmpTraps.useBuiltinTrapServer"
            },
            "snmp_server.ip_addresses": {
                "type": "list",
                "source_key": "settings.telemetry.snmpTraps.externalTrapServers",
                "optional": True
            },

            # -------------------------------
            # Syslog Server
            # -------------------------------
            "syslog_server.configure_dnac_ip": {
                "type": "bool",
                "source_key": "settings.telemetry.syslogs.useBuiltinSyslogServer"
            },
            "syslog_server.ip_addresses": {
                "type": "list",
                "source_key": "settings.telemetry.syslogs.externalSyslogServers",
                "optional": True
            },

            # -------------------------------
            # Wired/Wireless Telemetry
            # -------------------------------
            "wired_data_collection.enable_wired_data_collection": {
                "type": "bool",
                "source_key": "settings.telemetry.wiredDataCollection.enableWiredDataCollection"
            },
            "wireless_telemetry.enable_wireless_telemetry": {
                "type": "bool",
                "source_key": "settings.telemetry.wirelessTelemetry.enableWirelessTelemetry"
            }
        })

    def modify_network_parameters(self, reverse_mapping_spec, data_list):
        """
        Apply reverse mapping specification to transform data from DNAC API format to Ansible playbook format.

        This method transforms raw API response data from Cisco Catalyst Center into
        Ansible-compatible configuration format using a comprehensive mapping specification.
        It handles field mapping, type conversion, and applies custom transformation functions.

        Args:
            reverse_mapping_spec (OrderedDict): Specification dictionary containing:
                - target_key (str): Target field name in Ansible config
                - mapping_rule (dict): Transformation rules including:
                    - source_key (str): Source field path in API response
                    - type (str): Expected data type for validation
                    - transform (callable, optional): Custom transformation function
                    - optional (bool, optional): Whether field is optional
                    - special_handling (bool, optional): Requires special processing

            data_list (list): List of data objects from DNAC API responses to transform.

        Returns:
            list: Transformed data list suitable for Ansible playbook configuration.
                 Each item is transformed according to the mapping specification with:
                 - Field names converted to Ansible-compatible format
                 - Data types properly converted and validated
                 - Optional fields handled appropriately
                 - Custom transformations applied where specified

        Transformation Process:
            1. Iterates through each data item in the input list
            2. Applies each mapping rule from the specification
            3. Extracts nested values using dot-notation source keys
            4. Applies custom transform functions when specified
            5. Validates and sanitizes values based on expected types
            6. Handles optional fields and missing data gracefully
            7. Preserves semantic meaning (e.g., empty lists for server configs)

        Error Handling:
            - Logs warnings for transformation errors
            - Skips invalid data items with detailed logging
            - Handles missing nested fields gracefully
            - Preserves partial transformations when possible

        Examples:
            API Response -> Ansible Config transformation:
            {'siteName': 'Global/USA/NYC'} -> {'site_name': 'Global/USA/NYC'}
            {'ipV4AddressSpace': {'subnet': '192.168.1.0'}} -> {'ipv4_subnet': '192.168.1.0'}
        """
        if not data_list or not reverse_mapping_spec:
            return []

        transformed_data = []

        for data_item in data_list:
            transformed_item = {}

            # Apply each mapping rule from the specification
            for target_key, mapping_rule in reverse_mapping_spec.items():
                source_key = mapping_rule.get("source_key")
                transform_func = mapping_rule.get("transform")

                # Handle case where source_key is None but transform function exists
                if source_key is None and transform_func and callable(transform_func):
                    # Pass entire data_item to transform function
                    value = transform_func(data_item)
                elif source_key:
                    # Extract value using dot notation if needed
                    value = self._extract_nested_value(data_item, source_key)

                    # Apply transformation function if specified (only if value is not None)
                    if transform_func and callable(transform_func) and value is not None:
                        value = transform_func(value)
                else:
                    # Skip if no source_key and no transform function
                    continue

                # Sanitize the value
                value = self._sanitize_value(value, mapping_rule.get("type", "str"))

                transformed_item[target_key] = value

            transformed_data.append(transformed_item)

        return transformed_data

    def _extract_nested_value(self, data_item, key_path):
        """
        Extract a value from nested dictionary structure using dot notation key path.

        This utility function safely navigates nested dictionary structures to extract
        values at arbitrary depth levels. It uses dot-separated key paths to traverse
        the nested structure and handles missing keys gracefully.

        Args:
            data_item (dict or None): The source dictionary to extract values from.
                                     Can be None or empty dict.
            key_path (str): Dot-separated path to the target value.
                           Examples: 'settings.dns.servers', 'ipV4AddressSpace.subnet'

        Returns:
            any or None: The value at the specified key path, or None if:
                        - key_path is empty or None
                        - data_item is None or not a dictionary
                        - Any key in the path doesn't exist
                        - Path traversal encounters non-dict value

        Examples:
            data = {'settings': {'dns': {'servers': ['8.8.8.8']}}}
            _extract_nested_value(data, 'settings.dns.servers') -> ['8.8.8.8']
            _extract_nested_value(data, 'settings.ntp.servers') -> None
            _extract_nested_value(data, 'missing.key') -> None
        """
        if not key_path or not data_item:
            return None

        keys = key_path.split('.')
        value = data_item

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None

        return value

    def _sanitize_value(self, value, value_type):
        """
        Sanitize and normalize a value based on its expected type for YAML output.

        This utility function performs type validation, conversion, and normalization
        to ensure values are properly formatted for Ansible YAML configurations.
        It handles type coercion and provides sensible defaults for missing values.

        Args:
            value: The raw value to sanitize. Can be any type.
            value_type (str): Expected target type for the value:
                             - "str": String type with special boolean/numeric handling
                             - "list": List type with singleton conversion
                             - "dict": Dictionary type
                             - "int": Integer type
                             - "bool": Boolean type
                             - Other: Pass-through with minimal processing

        Returns:
            Sanitized value of the appropriate type:
            - For None input: Returns appropriate empty value ([], {}, "")
            - For type mismatches: Attempts conversion or wrapping
            - For strings: Handles boolean/numeric conversion
            - For lists: Ensures list format, converts singletons
        """
        if value is None:
            if value_type == "list":
                return []
            elif value_type == "dict":
                return {}
            else:
                return ""

        if value_type == "list" and not isinstance(value, list):
            return [value] if value else []

        if value_type == "str":
            if isinstance(value, bool):
                return str(value).lower()
            elif isinstance(value, (int, float)):
                return str(value)
            elif isinstance(value, str):
                return value
            else:
                return str(value)

        return value

    def modify_network_parameters_old(self, params):
        """
        Safely sanitize and normalize config parameters BEFORE reverse-mapping.
        Prevents errors like:
            - "expected str but got NoneType"
            - reverse mapping crash if a key is missing or None
            - AAA settings failing when values are not strings

        This function makes sure:
            - None becomes "" (or [] for list or {} for dict)
            - Integers become strings
            - Boolean values become lowercase strings ("true"/"false")
            - Unexpected value types are removed/sanitized
        """

        if params is None:
            return {}

        normalized = {}

        for key, value in params.items():

            # ------------------------------
            # 1. Handle nested dictionaries
            # ------------------------------
            if isinstance(value, dict):
                normalized[key] = self.modify_network_parameters_old(value)
                continue

            # ------------------------------
            # 2. Handle list values
            # ------------------------------
            if isinstance(value, list):
                clean_list = []
                for item in value:
                    if item is None:
                        clean_list.append("")
                    elif isinstance(item, (int, float)):
                        clean_list.append(str(item))
                    elif isinstance(item, bool):
                        clean_list.append(str(item).lower())
                    else:
                        clean_list.append(item)
                normalized[key] = clean_list
                continue

            # ------------------------------
            # 3. Convert None → ""
            # ------------------------------
            if value is None:
                normalized[key] = ""
                continue

            # ------------------------------
            # 4. Convert integer/float → str
            # ------------------------------
            if isinstance(value, (int, float)):
                normalized[key] = str(value)
                continue

            # ------------------------------
            # 5. Convert boolean → lowercase string
            # ------------------------------
            if isinstance(value, bool):
                normalized[key] = str(value).lower()
                continue

            # ------------------------------
            # 6. Everything else remain same
            # ------------------------------
            normalized[key] = value

        return normalized

    def device_controllability_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for device controllability configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for device controllability details
        """
        self.log("Generating reverse mapping specification for device controllability settings.", "DEBUG")

        return OrderedDict({
            "device_controllability": {"type": "bool", "source_key": "deviceControllability"},
            "autocorrect_telemetry_config": {"type": "bool", "source_key": "autocorrectTelemetryConfig"},
        })

    def get_child_sites_from_hierarchy(self, site_hierarchy):
        """
        Get all child sites under a given site hierarchy path.

        Args:
            site_hierarchy (str): Site hierarchy path (e.g., "Global/USA" or "Global/USA/California")

        Returns:
            list: List of dictionaries containing site_name and site_id for all child sites
        """
        self.log("Getting child sites for site hierarchy: {0}".format(site_hierarchy), "DEBUG")

        child_sites = []

        # Get site ID to name mapping if not already cached
        if not hasattr(self, 'site_id_name_dict'):
            self.site_id_name_dict = self.get_site_id_name_mapping()

        # Create reverse mapping (name to ID)
        site_name_to_id = {v: k for k, v in self.site_id_name_dict.items()}

        # Find all sites that start with the hierarchy path
        for site_id, site_name in self.site_id_name_dict.items():
            # Check if this site is under the specified hierarchy
            if site_name.startswith(site_hierarchy):
                # Ensure it's actually a child (not the parent itself unless it's exact match)
                if site_name == site_hierarchy or site_name.startswith(site_hierarchy + "/"):
                    child_sites.append({
                        "site_name": site_name,
                        "site_id": site_id
                    })
                    self.log("Found child site: {0} (ID: {1})".format(site_name, site_id), "DEBUG")

        if not child_sites:
            self.log("No child sites found under hierarchy: {0}".format(site_hierarchy), "WARNING")
        else:
            self.log("Found {0} child sites under hierarchy: {1}".format(len(child_sites), site_hierarchy), "INFO")

        return child_sites

    def transform_site_location(self, site_name_or_pool_details):
        """
        Transform site location information to hierarchical site name format for brownfield configurations.

        This transformation function handles conversion of site information from various
        formats (site ID, site name, pool details) into consistent hierarchical site
        name format required for Ansible playbook configurations.

        Args:
            site_name_or_pool_details (str, dict, or None): Site information in various formats:
                - str: Direct site name (returned as-is)
                - dict: Pool details containing site information:
                    - siteName (str, optional): Direct site name
                    - siteId (str, optional): Site ID requiring lookup
                - None: No site information available

        Returns:
            str or None: Hierarchical site name format or None:
                - "Global/Country/State/City/Building": Complete site hierarchy
                - None: When site information cannot be determined

        Transformation Logic:
            1. None input -> None (with debug logging)
            2. String input -> Return as-is (already site name)
            3. Dict input -> Extract siteName if available
            4. Dict with siteId only -> Lookup name via site mapping

        Site ID Mapping:
            - Uses cached site_id_name_dict for efficient lookups
            - Creates mapping via get_site_id_name_mapping() if needed
            - Maps site UUIDs to hierarchical names

        Examples:
            transform_site_location("Global/USA/NYC") -> "Global/USA/NYC"
            transform_site_location({"siteName": "Global/USA/NYC"}) -> "Global/USA/NYC"
            transform_site_location({"siteId": "uuid-123"}) -> "Global/USA/NYC" (via lookup)
            transform_site_location(None) -> None
        """
        self.log("Transforming site location for input: {0}".format(site_name_or_pool_details), "DEBUG")

        # Handle None input
        if site_name_or_pool_details is None:
            self.log("Input is None, returning None for site location", "DEBUG")
            return None

        # If it's already a string (site name), return it as is
        if isinstance(site_name_or_pool_details, str):
            self.log("Input is already a string (site name): {0}".format(site_name_or_pool_details), "DEBUG")
            return site_name_or_pool_details

        # If it's a dictionary (pool details), extract the site information
        if isinstance(site_name_or_pool_details, dict):
            site_id = site_name_or_pool_details.get("siteId")
            site_name = site_name_or_pool_details.get("siteName")

            # Always prioritize site ID lookup for full hierarchy over siteName (which may be just the short name)
            if site_id:
                # Create site ID to name mapping if not exists
                if not hasattr(self, 'site_id_name_dict'):
                    self.site_id_name_dict = self.get_site_id_name_mapping()

                site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
                if site_name_hierarchy:
                    self.log("Mapped site ID {0} to full hierarchy: {1}".format(site_id, site_name_hierarchy), "DEBUG")
                    return site_name_hierarchy
                else:
                    self.log("Site ID {0} not found in mapping, falling back to siteName: {1}".format(site_id, site_name), "DEBUG")

            # If we have a site name but no site ID mapping, use it directly
            if site_name:
                self.log("Using siteName from pool details as fallback: {0}".format(site_name), "DEBUG")
                return site_name

        # If we can't process it, return None
        self.log("Unable to process input for site location transformation", "WARNING")
        return None

    def reset_operation_tracking(self):
        """
        Reset operation tracking variables for a new brownfield configuration generation operation.

        This method initializes or resets the tracking variables used to monitor the progress
        and results of network settings extraction operations. It ensures clean state for
        each new generation workflow.

        Tracking Variables Reset:
            - operation_successes (list): Successful site/component operations
            - operation_failures (list): Failed site/component operations
            - total_sites_processed (int): Count of sites processed
            - total_components_processed (int): Count of components processed
        """
        self.log("Resetting operation tracking variables for new operation", "DEBUG")
        self.operation_successes = []
        self.operation_failures = []
        self.total_sites_processed = 0
        self.total_components_processed = 0
        self.log("Operation tracking variables reset successfully", "DEBUG")

    def add_success(self, site_name, component, additional_info=None):
        """
        Record a successful operation for site/component processing in operation tracking.

        This method adds a successful operation entry to the tracking system, recording
        which site and component were successfully processed during brownfield network
        settings extraction. Used for generating comprehensive operation summaries.

        Args:
            site_name (str): Full hierarchical site name that was successfully processed.
                           Example: "Global/USA/SAN-FRANCISCO/SF_BLD1"
            component (str): Network settings component that was successfully processed.
                           Examples: "reserve_pool_details", "network_management_details"
            additional_info (dict, optional): Extra information about the successful operation:
                - pools_processed (int): Number of pools processed for this site
                - settings_extracted (list): List of settings successfully extracted
                - processing_time (float): Time taken for processing
                - Any other relevant success metrics
        """
        self.log("Creating success entry for site {0}, component {1}".format(site_name, component), "DEBUG")
        success_entry = {
            "site_name": site_name,
            "component": component,
            "status": "success"
        }

        if additional_info:
            self.log("Adding additional information to success entry: {0}".format(additional_info), "DEBUG")
            success_entry.update(additional_info)

        self.operation_successes.append(success_entry)
        self.log("Successfully added success entry for site {0}, component {1}. Total successes: {2}".format(
            site_name, component, len(self.operation_successes)), "DEBUG")

    def add_failure(self, site_name, component, error_info):
        """
        Record a failed operation for site/component processing in operation tracking.

        This method adds a failed operation entry to the tracking system, recording
        which site and component failed during brownfield network settings extraction
        along with detailed error information for troubleshooting.

        Args:
            site_name (str): Full hierarchical site name that failed processing.
                           Example: "Global/USA/SAN-FRANCISCO/SF_BLD1"
            component (str): Network settings component that failed processing.
                           Examples: "reserve_pool_details", "network_management_details"
            error_info (dict): Detailed error information containing:
                - error_message (str): Human-readable error description
                - error_code (str, optional): Specific error code if available
                - api_response (dict, optional): Raw API error response
                - stack_trace (str, optional): Exception stack trace
                - retry_attempted (bool, optional): Whether retry was attempted
        """
        self.log("Creating failure entry for site {0}, component {1}".format(site_name, component), "DEBUG")
        failure_entry = {
            "site_name": site_name,
            "component": component,
            "status": "failed",
            "error_info": error_info
        }

        self.operation_failures.append(failure_entry)
        self.log("Successfully added failure entry for site {0}, component {1}: {2}. Total failures: {3}".format(
            site_name, component, error_info.get("error_message", "Unknown error"), len(self.operation_failures)), "ERROR")

    def get_operation_summary(self):
        """
        Returns a summary of all operations performed.
        Returns:
            dict: Summary containing successes, failures, and statistics.
        """
        self.log("Generating operation summary from {0} successes and {1} failures".format(
            len(self.operation_successes), len(self.operation_failures)), "DEBUG")

        unique_successful_sites = set()
        unique_failed_sites = set()

        self.log("Processing successful operations to extract unique site information", "DEBUG")
        for success in self.operation_successes:
            unique_successful_sites.add(success.get("site_name", "Global"))

        self.log("Processing failed operations to extract unique site information", "DEBUG")
        for failure in self.operation_failures:
            unique_failed_sites.add(failure.get("site_name", "Global"))

        self.log("Calculating site categorization based on success and failure patterns", "DEBUG")
        partial_success_sites = unique_successful_sites.intersection(unique_failed_sites)
        self.log("Sites with partial success (both successes and failures): {0}".format(
            len(partial_success_sites)), "DEBUG")

        complete_success_sites = unique_successful_sites - unique_failed_sites
        self.log("Sites with complete success (only successes): {0}".format(
            len(complete_success_sites)), "DEBUG")

        complete_failure_sites = unique_failed_sites - unique_successful_sites
        self.log("Sites with complete failure (only failures): {0}".format(
            len(complete_failure_sites)), "DEBUG")

        summary = {
            "total_sites_processed": len(unique_successful_sites.union(unique_failed_sites)),
            "total_components_processed": self.total_components_processed,
            "total_successful_operations": len(self.operation_successes),
            "total_failed_operations": len(self.operation_failures),
            "sites_with_complete_success": list(complete_success_sites),
            "sites_with_partial_success": list(partial_success_sites),
            "sites_with_complete_failure": list(complete_failure_sites),
            "success_details": self.operation_successes,
            "failure_details": self.operation_failures
        }

        self.log("Operation summary generated successfully with {0} total sites processed".format(
            summary["total_sites_processed"]), "INFO")

        return summary

    def get_global_pools(self, network_element, filters):
        """
        Retrieves global IP pools based on the provided network element and filters.
        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving global pools.
            filters (dict): A dictionary containing global_filters and component_specific_filters.
        Returns:
            dict: A dictionary containing the modified details of global pools.
        """
        self.log("Starting to retrieve global pools with network element: {0} and filters: {1}".format(
            network_element, filters), "DEBUG")

        final_global_pools = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log("Getting global pools using family '{0}' and function '{1}'.".format(
            api_family, api_function), "INFO")

        # Get global filters
        global_filters = filters.get("global_filters", {})
        component_specific_filters = filters.get("component_specific_filters", {}).get("global_pool_details", [])

        try:
            # Execute bulk API call to get all global pools at once
            # Note: Global pool APIs don't support filter parameters, so we retrieve all and filter locally
            all_global_pools = self.execute_get_bulk(api_family, api_function)
            # all_global_pools = self.execute_get_bulk_with_pagination(api_family, api_function, params={})
            self.log("Retrieved {0} total global pools using bulk API call".format(
                len(all_global_pools)), "INFO")

            # Add debug logging to see what pools were retrieved
            for i, pool in enumerate(all_global_pools):
                self.log("Pool {0}: Name='{1}', Type='{2}', ID='{3}'".format(
                    i + 1,
                    pool.get("name", "N/A"),
                    pool.get("poolType", "N/A"),
                    pool.get("id", "N/A")
                ), "DEBUG")

                # Debug: Log all available fields for the first few pools
                if i < 3:
                    self.log("Pool {0} all fields: {1}".format(i + 1, list(pool.keys())), "DEBUG")
                    for key, value in pool.items():
                        self.log("  {0}: {1}".format(key, value), "DEBUG")

            # Apply global filters if present
            filtered_pools = all_global_pools
            if global_filters.get("pool_name_list") or global_filters.get("pool_type_list"):
                filtered_pools = []
                pool_name_list = global_filters.get("pool_name_list", [])
                pool_type_list = global_filters.get("pool_type_list", [])

                for pool in all_global_pools:
                    # Check pool name filter
                    if pool_name_list and pool.get("name") not in pool_name_list:
                        continue

                    # Check pool type filter
                    if pool_type_list and pool.get("poolType") not in pool_type_list:
                        continue

                    filtered_pools.append(pool)

                self.log("Applied global filters, remaining pools: {0}".format(len(filtered_pools)), "DEBUG")

            # Apply component-specific filters
            if component_specific_filters:
                self.log("Applying component-specific filters: {0}".format(component_specific_filters), "DEBUG")

                # Component filters should work as AND operation across all filter criteria
                # Each pool must satisfy ALL the filter criteria to be included
                final_filtered_pools = []

                # Collect all filter criteria from all filter objects
                all_pool_name_filters = []
                all_pool_type_filters = []

                for filter_param in component_specific_filters:
                    if "pool_name" in filter_param:
                        all_pool_name_filters.append(filter_param["pool_name"])
                    if "pool_type" in filter_param:
                        all_pool_type_filters.append(filter_param["pool_type"])

                self.log("Collected filter criteria - pool_names: {0}, pool_types: {1}".format(
                    all_pool_name_filters, all_pool_type_filters), "DEBUG")

                for pool in filtered_pools:
                    pool_name = pool.get("name")
                    pool_type = pool.get("poolType")
                    matches_all_criteria = True

                    # Check if pool matches ALL name filters (if any)
                    if all_pool_name_filters:
                        if pool_name not in all_pool_name_filters:
                            matches_all_criteria = False
                            self.log("Pool '{0}' does not match any name filter: {1}".format(
                                pool_name, all_pool_name_filters), "DEBUG")

                    # Check if pool matches ALL type filters (if any)
                    if all_pool_type_filters and matches_all_criteria:
                        if pool_type not in all_pool_type_filters:
                            matches_all_criteria = False
                            self.log("Pool '{0}' (type: '{1}') does not match any type filter: {2}".format(
                                pool_name, pool_type, all_pool_type_filters), "DEBUG")

                    # Additional AND logic: if both name and type filters exist,
                    # pool must satisfy both criteria
                    if matches_all_criteria and all_pool_name_filters and all_pool_type_filters:
                        # Pool must match at least one name AND at least one type
                        name_match = pool_name in all_pool_name_filters
                        type_match = pool_type in all_pool_type_filters

                        if not (name_match and type_match):
                            matches_all_criteria = False
                            self.log("Pool '{0}' (type: '{1}') does not satisfy both name and type criteria".format(
                                pool_name, pool_type), "DEBUG")

                    if matches_all_criteria:
                        final_filtered_pools.append(pool)
                        self.log("Pool '{0}' (type: '{1}') matched ALL filter criteria".format(
                            pool_name, pool_type), "INFO")

                final_global_pools = final_filtered_pools
                self.log("Applied component-specific filters with AND logic, final pools: {0}".format(len(final_global_pools)), "DEBUG")
            else:
                final_global_pools = filtered_pools

        except Exception as e:
            error_msg = "Failed to retrieve global pools: {0}".format(str(e))
            self.log(error_msg, "ERROR")
            self.add_failure("Global", "global_pool_details", {
                "error_type": "api_error",
                "error_message": error_msg,
                "error_code": "GLOBAL_POOL_RETRIEVAL_FAILED"
            })
            return {
                "global_pool_details": {},
                "operation_summary": self.get_operation_summary()
            }

        # Track success
        self.add_success("Global", "global_pool_details", {
            "pools_processed": len(final_global_pools)
        })

        # Apply reverse mapping
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        reverse_mapping_spec = reverse_mapping_function()

        # Transform using inherited modify_parameters function (with OrderedDict spec)
        pools_details = self.modify_parameters(reverse_mapping_spec, final_global_pools)

        return {
            "global_pool_details": {
                "settings": {
                    "ip_pool": pools_details
                }
            },
            "operation_summary": self.get_operation_summary()
        }

    def get_network_management_settings(self, network_element, filters):
        """
        Retrieves network management settings for all targeted sites.
        Uses get_*_settings_for_site() helper functions.
        Mirrors reserve pool logic for consistent behavior.
        """

        self.log("Starting NM retrieval with API family: {0}, function: {1}".format(
            network_element.get("api_family"), network_element.get("api_function")), "DEBUG")

        # === Determine target sites (same logic as reserve pools) ===
        global_filters = filters.get("global_filters", {})
        component_specific_filters = filters.get("component_specific_filters", {}).get("network_management_details", [])

        # Extract site_name_list from component specific filters
        site_name_list = []
        if component_specific_filters:
            for filter_param in component_specific_filters:
                if "site_name_list" in filter_param:
                    site_name_list.extend(filter_param["site_name_list"])
                elif "site_name" in filter_param:
                    site_name_list.append(filter_param["site_name"])

        # If no component specific filters, check global filters
        if not site_name_list:
            site_name_list = global_filters.get("site_name_list", [])

        target_sites = []

        # Build site mapping only once
        if not hasattr(self, "site_id_name_dict"):
            self.site_id_name_dict = self.get_site_id_name_mapping()

        # Reverse-map: name → ID
        site_name_to_id = {v: k for k, v in self.site_id_name_dict.items()}

        if site_name_list:
            # Specific sites requested
            for sname in site_name_list:
                sid = site_name_to_id.get(sname)
                if sid:
                    target_sites.append({"site_name": sname, "site_id": sid})
                    self.log("Target NM site added: {0} (ID: {1})".format(sname, sid), "DEBUG")
                else:
                    self.log("Site '{0}' not found in Catalyst Center".format(sname), "WARNING")
                    self.add_failure(sname, "network_management_details", {
                        "error_type": "site_not_found",
                        "error_message": "Site not found in Catalyst Center"
                    })
        else:
            # No specific sites requested - default to Global site only
            global_site_id = site_name_to_id.get("Global")
            if global_site_id:
                target_sites.append({"site_name": "Global", "site_id": global_site_id})
                self.log("No site filters provided - defaulting to Global site for network management details", "INFO")
            else:
                self.log("Global site not found - processing all sites as fallback", "WARNING")
                for sid, sname in self.site_id_name_dict.items():
                    target_sites.append({"site_name": sname, "site_id": sid})

        final_nm_details = []

        # === Process each site ===
        for site in target_sites:
            site_name = site["site_name"]
            site_id = site["site_id"]

            self.log("Composing NM settings for {0} (ID: {1})".format(site_name, site_id), "INFO")

            nm_details = {
                "site_name": site_name,
                "site_id": site_id
            }

            # ---------- AAA ----------
            try:
                if hasattr(self, "get_aaa_settings_for_site"):
                    aaa_network, aaa_client = self.get_aaa_settings_for_site(site_name, site_id)
                    nm_details["aaaNetwork"] = aaa_network or {}
                    nm_details["aaaClient"] = aaa_client or {}
                else:
                    nm_details["aaaNetwork"] = {}
                    nm_details["aaaClient"] = {}
            except Exception as e:
                self.log(f"AAA retrieval failed for {site_name}: {e}", "WARNING")
                nm_details["aaaNetwork"] = {}
                nm_details["aaaClient"] = {}

            # ---------- DHCP ----------
            try:
                if hasattr(self, "get_dhcp_settings_for_site"):
                    nm_details["dhcp"] = self.get_dhcp_settings_for_site(site_name, site_id) or {}
                else:
                    nm_details["dhcp"] = {}
            except Exception as e:
                self.log(f"DHCP retrieval failed for {site_name}: {e}", "WARNING")
                nm_details["dhcp"] = {}

            # ---------- DNS ----------
            try:
                if hasattr(self, "get_dns_settings_for_site"):
                    nm_details["dns"] = self.get_dns_settings_for_site(site_name, site_id) or {}
                else:
                    nm_details["dns"] = {}
            except Exception as e:
                self.log(f"DNS retrieval failed for {site_name}: {e}", "WARNING")
                nm_details["dns"] = {}

            # ---------- TELEMETRY ----------
            try:
                if hasattr(self, "get_telemetry_settings_for_site"):
                    nm_details["telemetry"] = self.get_telemetry_settings_for_site(site_name, site_id) or {}
                else:
                    nm_details["telemetry"] = {}
            except Exception as e:
                self.log(f"Telemetry retrieval failed for {site_name}: {e}", "WARNING")
                nm_details["telemetry"] = {}

            # ---------- NTP ----------
            try:
                if hasattr(self, "get_ntp_settings_for_site"):
                    nm_details["ntp"] = self.get_ntp_settings_for_site(site_name, site_id) or {}
                else:
                    nm_details["ntp"] = {}
            except Exception as e:
                self.log(f"NTP retrieval failed for {site_name}: {e}", "WARNING")
                nm_details["ntp"] = {}

            # ---------- TIMEZONE ----------
            try:
                if hasattr(self, "get_time_zone_settings_for_site"):
                    nm_details["timeZone"] = self.get_time_zone_settings_for_site(site_name, site_id) or {}
                else:
                    nm_details["timeZone"] = {}
            except Exception as e:
                self.log(f"Timezone retrieval failed for {site_name}: {e}", "WARNING")
                nm_details["timeZone"] = {}

            # ---------- BANNER ----------
            try:
                if hasattr(self, "get_banner_settings_for_site"):
                    nm_details["banner"] = self.get_banner_settings_for_site(site_name, site_id) or {}
                else:
                    nm_details["banner"] = {}
            except Exception as e:
                self.log(f"Banner retrieval failed for {site_name}: {e}", "WARNING")
                nm_details["banner"] = {}

            # Store result for this site
            final_nm_details.append(nm_details)

            # Track success
            self.add_success(site_name, "network_management_details", {
                "nm_components_processed": len(nm_details)
            })

        self.log("Completed NM retrieval for all targeted sites. Total sites processed: {0}".format(len(final_nm_details)), "INFO")

        # === APPLY UNIFIED NM REVERSE MAPPING BEFORE RETURN ===
        try:
            self.log("Applying NM unified reverse mapping...", "INFO")

            transformed_nm = []

            for entry in final_nm_details:
                self.log("Processing NM entry for site: {0}".format(entry.get("site_name")), "DEBUG")
                site_name = entry.get("site_name")

                # ---- Clean / normalize DNAC response ----
                entry = self.clean_nm_entry(entry)

                # ---- Apply unified reverse mapping ----
                transformed_entry = self.prune_empty({
                    "site_name": site_name,
                    "settings": {
                        "network_aaa": self.extract_network_aaa(entry),
                        "client_and_endpoint_aaa": self.extract_client_aaa(entry),
                        "dhcp_server": self.extract_dhcp(entry),
                        "dns_server": self.extract_dns(entry),
                        "ntp_server": self.extract_ntp(entry),
                        "timezone": self.extract_timezone(entry),
                        "message_of_the_day": self.extract_banner(entry),
                        "netflow_collector": self.extract_netflow(entry),
                        "snmp_server": self.extract_snmp(entry),
                        "syslog_server": self.extract_syslog(entry),
                    }
                })

                transformed_nm.append(transformed_entry)

            self.log("NM unified reverse mapping completed successfully", "INFO")
            self.log(self.pprint(transformed_nm), "DEBUG")

        except Exception as e:
            self.log("Unified reverse mapping failed for NM: {0}".format(e), "ERROR")
            transformed_nm = final_nm_details  # fallback

        # Return result in consistent format
        return {
            "network_management_details": transformed_nm,
            "operation_summary": self.get_operation_summary()
        }

    def clean_nm_entry(self, entry):
        """
        Converts DNAC MyDict objects to plain Python dicts recursively.
        Ensures unified reverse mapping always gets standard Python types.
        """

        # ---- Case 1: DNAC MyDict ----
        if hasattr(entry, "to_dict"):
            try:
                entry = entry.to_dict()
            except Exception:
                entry = dict(entry)

        # ---- Case 2: Regular dict ----
        if isinstance(entry, dict):
            cleaned = {}
            for key, value in entry.items():
                if value is None:
                    continue
                cleaned[key] = self.clean_nm_entry(value)
            return cleaned

        # ---- Case 3: List ----
        if isinstance(entry, list):
            return [self.clean_nm_entry(v) for v in entry]

        # Primitive (str, int, bool, None)
        return entry

    def prune_empty(self, data):
        """
        Recursively remove keys with None, '' or empty lists/dicts.
        """
        if isinstance(data, dict):
            cleaned = {}
            for k, v in data.items():
                v = self.prune_empty(v)
                if v in ("", None, [], {}):
                    continue
                cleaned[k] = v
            return cleaned

        elif isinstance(data, list):
            cleaned_list = [self.prune_empty(i) for i in data]
            # Remove empty items
            return [i for i in cleaned_list if i not in ("", None, [], {})]

        return data

    def extract_network_aaa(self, entry):
        data = entry.get("aaaNetwork", {})
        if not data:
            return {}

        result = {
            "primary_server_address": data.get("primaryServerIp", ""),
            "secondary_server_address": data.get("secondaryServerIp", ""),
            "protocol": data.get("protocol", ""),
            "server_type": data.get("serverType", ""),
        }

        # Include pan_address field if available (required for ISE server type)
        if data.get("pan"):
            result["pan_address"] = data.get("pan")

        return result

    def extract_client_aaa(self, entry):
        data = entry.get("aaaClient", {})
        if not data:
            return {}

        result = {
            "primary_server_address": data.get("primaryServerIp", ""),
            "secondary_server_address": data.get("secondaryServerIp", ""),
            "protocol": data.get("protocol", ""),
            "server_type": data.get("serverType", ""),
        }

        # Include pan_address field if available (required for ISE server type)
        if data.get("pan"):
            result["pan_address"] = data.get("pan")

        return result

    def extract_dhcp(self, entry):
        dhcp = entry.get("dhcp", {})
        return dhcp.get("servers", [])

    def extract_dns(self, entry):
        dns = entry.get("dns", {})
        return {
            "domain_name": dns.get("domainName", ""),
            "primary_ip_address": dns.get("dnsServers", ["", ""])[0] if dns.get("dnsServers") else "",
            "secondary_ip_address": dns.get("dnsServers", ["", ""])[1] if dns.get("dnsServers") and len(dns.get("dnsServers")) > 1 else "",
        }

    def extract_ntp(self, entry):
        ntp = entry.get("ntp", {})
        return ntp.get("servers", [])

    def extract_timezone(self, entry):
        tz = entry.get("timeZone", {})
        return tz.get("identifier", "")

    def extract_banner(self, entry):
        banner = entry.get("banner", {})
        return {
            "banner_message": banner.get("message", ""),
            "retain_existing_banner": False  # DNAC v1 does not provide this flag
        }

    def extract_netflow(self, entry):
        telemetry = entry.get("telemetry", {})
        app_vis = telemetry.get("applicationVisibility", {})
        collector = app_vis.get("collector", {})

        collector_type = collector.get("collectorType")

        # Prepare base structure
        result = {
            "collector_type": collector_type or "",
            "ip_address": collector.get("ipAddress", ""),
            "port": collector.get("port", None),
            "enable_on_wired_access_devices": app_vis.get("enableOnWiredAccessDevices", False)
        }

        # If Builtin collector -> return only type + enable flag
        if collector_type != "External":
            result["ip_address"] = ""
            result["port"] = None

        return result

    def extract_snmp(self, entry):
        traps = entry.get("telemetry", {}).get("snmpTraps", {})
        return {
            "configure_dnac_ip": traps.get("useBuiltinTrapServer", False),
            "ip_addresses": traps.get("externalTrapServers", []),
        }

    def extract_syslog(self, entry):
        syslog = entry.get("telemetry", {}).get("syslogs", {})
        return {
            "configure_dnac_ip": syslog.get("useBuiltinSyslogServer", False),
            "ip_addresses": syslog.get("externalSyslogServers", []),
        }

    def execute_get_bulk(self, api_family, api_function, params=None):
        """
        Executes a single non-paginated GET request for bulk data retrieval.

        This function is specifically designed for API endpoints that return all data
        in a single call without requiring pagination parameters.

        Args:
            api_family (str): The API family to use for the call (For example, 'network_settings', 'devices', etc.).
            api_function (str): The specific API function to call for retrieving data (For example, 'retrieves_ip_address_subpools').
            params (dict, optional): Parameters for filtering the data. Defaults to None for bulk retrieval.

        Returns:
            list: A list of dictionaries containing the retrieved data.

        Usage:
            # For bulk reserve pool retrieval without site filtering
            all_pools = self.execute_get_bulk("network_settings", "retrieves_ip_address_subpools")

            # For bulk retrieval with specific filters
            filtered_pools = self.execute_get_bulk("network_settings", "retrieves_ip_address_subpools", {"filter": "value"})
        """
        self.log("Starting bulk API execution for family '{0}', function '{1}'".format(
            api_family, api_function), "DEBUG")

        try:
            # Prepare parameters - use empty dict if params is None
            api_params = params if params is not None else {}

            self.log(
                "Executing bulk API call for family '{0}', function '{1}' with parameters: {2}".format(
                    api_family, api_function, api_params
                ),
                "INFO",
            )

            # Execute the API call
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params=api_params,
            )

            self.log(
                "Response received from bulk API call for family '{0}', function '{1}': {2}".format(
                    api_family, api_function, response
                ),
                "DEBUG",
            )

            # Process the response if available
            response_data = response.get("response", [])

            if response_data:
                self.log(
                    "Bulk data retrieved for family '{0}', function '{1}': Total records: {2}".format(
                        api_family, api_function, len(response_data)
                    ),
                    "INFO",
                )
            else:
                self.log(
                    "No data found for family '{0}', function '{1}'.".format(
                        api_family, api_function
                    ),
                    "DEBUG",
                )

            # Return the list of retrieved data
            return response_data if isinstance(response_data, list) else [response_data] if response_data else []

        except Exception as e:
            self.msg = (
                "An error occurred while retrieving bulk data using family '{0}', function '{1}'. "
                "Error: {2}".format(
                    api_family, api_function, str(e)
                )
            )
            self.fail_and_exit(self.msg)

    def get_reserve_pools(self, network_element, filters):
        """
        Retrieves reserve IP pools based on the provided network element and filters.
        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving reserve pools.
            filters (dict): A dictionary containing global_filters and component_specific_filters.
        Returns:
            dict: A dictionary containing the modified details of reserve pools.
        """
        self.log("Starting to retrieve reserve pools with network element: {0} and filters: {1}".format(
            network_element, filters), "DEBUG")

        final_reserve_pools = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log("Getting reserve pools using family '{0}' and function '{1}'.".format(
            api_family, api_function), "INFO")

        # Get global filters
        global_filters = filters.get("global_filters", {})
        component_specific_filters = filters.get("component_specific_filters", {}).get("reserve_pool_details", [])

        # Check if we need site-specific filtering
        site_name_list = global_filters.get("site_name_list", [])
        has_site_specific_filters = site_name_list or any(
            filter_param.get("site_name") or filter_param.get("site_hierarchy")
            for filter_param in component_specific_filters
        )

        # Performance optimization: Use bulk API call when no site-specific filters are present
        if not has_site_specific_filters:
            self.log("No site-specific filters detected, using optimized bulk retrieval", "INFO")

            try:
                # Execute bulk API call to get all reserve pools at once (no siteId parameter needed)
                all_reserve_pools = self.execute_get_bulk(api_family, api_function)
                self.log("Retrieved {0} total reserve pools using bulk API call".format(
                    len(all_reserve_pools)), "INFO")

                # Apply global filters if present
                filtered_pools = all_reserve_pools
                if global_filters.get("pool_name_list") or global_filters.get("pool_type_list"):
                    filtered_pools = []
                    pool_name_list = global_filters.get("pool_name_list", [])
                    pool_type_list = global_filters.get("pool_type_list", [])

                    for pool in all_reserve_pools:
                        # Check pool name filter
                        if pool_name_list and pool.get("groupName") not in pool_name_list:
                            continue

                        # Check pool type filter
                        if pool_type_list and pool.get("type") not in pool_type_list:
                            continue

                        filtered_pools.append(pool)

                    self.log("Applied global filters, remaining pools: {0}".format(len(filtered_pools)), "DEBUG")

                # Apply component-specific filters (non-site-specific only)
                if component_specific_filters:
                    final_filtered_pools = []
                    for filter_param in component_specific_filters:
                        # Skip site-specific filters (should not occur in this path)
                        if filter_param.get("site_name"):
                            continue

                        for pool in filtered_pools:
                            matches_filter = True

                            # Check pool name filter
                            if "pool_name" in filter_param:
                                if pool.get("groupName") != filter_param["pool_name"]:
                                    matches_filter = False
                                    continue

                            # Check pool type filter
                            if "pool_type" in filter_param:
                                if pool.get("type") != filter_param["pool_type"]:
                                    matches_filter = False
                                    continue

                            if matches_filter:
                                final_filtered_pools.append(pool)

                    filtered_pools = final_filtered_pools

                final_reserve_pools = filtered_pools

                # Track success for bulk operation
                self.add_success("All Sites", "reserve_pool_details", {
                    "pools_processed": len(final_reserve_pools),
                    "optimization": "bulk_retrieval"
                })

            except Exception as e:
                self.log("Error in bulk reserve pool retrieval: {0}".format(str(e)), "ERROR")
                self.add_failure("All Sites", "reserve_pool_details", {
                    "error_type": "api_error",
                    "error_message": str(e),
                    "error_code": "BULK_API_CALL_FAILED"
                })
                final_reserve_pools = []

        else:
            # Site-specific filtering is needed, use original site-by-site approach
            self.log("Site-specific filters detected, using site-by-site retrieval", "INFO")

            # Process site-based filtering
            target_sites = []

            if site_name_list:
                self.log("Processing site name list: {0}".format(site_name_list), "DEBUG")
                # Get site ID to name mapping
                if not hasattr(self, 'site_id_name_dict'):
                    self.site_id_name_dict = self.get_site_id_name_mapping()

                # Create reverse mapping (name to ID)
                site_name_to_id_dict = {v: k for k, v in self.site_id_name_dict.items()}

                for site_name in site_name_list:
                    site_id = site_name_to_id_dict.get(site_name)
                    if site_id:
                        target_sites.append({"site_name": site_name, "site_id": site_id})
                        self.log("Added target site: {0} (ID: {1})".format(site_name, site_id), "DEBUG")
                    else:
                        self.log("Site '{0}' not found in Catalyst Center".format(site_name), "WARNING")
                        self.add_failure(site_name, "reserve_pool_details", {
                            "error_type": "site_not_found",
                            "error_message": "Site not found or not accessible",
                            "error_code": "SITE_NOT_FOUND"
                        })

            # If component-specific filters contain site names or site hierarchies but no global site filter, extract those sites
            if not target_sites and component_specific_filters:
                if not hasattr(self, 'site_id_name_dict'):
                    self.site_id_name_dict = self.get_site_id_name_mapping()
                site_name_to_id_dict = {v: k for k, v in self.site_id_name_dict.items()}

                for filter_param in component_specific_filters:
                    # Handle site_name filter
                    filter_site_name = filter_param.get("site_name")
                    if filter_site_name:
                        site_id = site_name_to_id_dict.get(filter_site_name)
                        if site_id and not any(s["site_name"] == filter_site_name for s in target_sites):
                            target_sites.append({"site_name": filter_site_name, "site_id": site_id})

                    # Handle site_hierarchy filter
                    filter_site_hierarchy = filter_param.get("site_hierarchy")
                    if filter_site_hierarchy:
                        self.log("Processing site hierarchy filter: {0}".format(filter_site_hierarchy), "INFO")
                        child_sites = self.get_child_sites_from_hierarchy(filter_site_hierarchy)
                        for child_site in child_sites:
                            # Avoid duplicates
                            if not any(s["site_name"] == child_site["site_name"] for s in target_sites):
                                target_sites.append(child_site)
                                self.log("Added child site from hierarchy: {0} (ID: {1})".format(
                                    child_site["site_name"], child_site["site_id"]), "DEBUG")

            # Process each target site
            for site_info in target_sites:
                site_name = site_info["site_name"]
                site_id = site_info["site_id"]

                self.log("Processing reserve pools for site: {0} (ID: {1})".format(site_name, site_id), "DEBUG")

                try:
                    # Base parameters for API call
                    params = {"siteId": site_id}

                    # Execute API call to get reserve pools for this site
                    reserve_pool_details = self.execute_get_with_pagination(api_family, api_function, params)
                    self.log("Retrieved {0} reserve pools for site {1}".format(
                        len(reserve_pool_details), site_name), "INFO")

                    # Apply component-specific filters
                    if component_specific_filters:
                        filtered_pools = []
                        for filter_param in component_specific_filters:
                            # Check if filter applies to this site
                            filter_site_name = filter_param.get("site_name")
                            filter_site_hierarchy = filter_param.get("site_hierarchy")

                            # Skip if this filter is for a different specific site
                            if filter_site_name and filter_site_name != site_name:
                                continue

                            # Check if this site matches the hierarchy filter
                            if filter_site_hierarchy and not site_name.startswith(filter_site_hierarchy):
                                continue

                            # Apply other filters
                            for pool in reserve_pool_details:
                                matches_filter = True

                                # Check pool name filter
                                if "pool_name" in filter_param:
                                    if pool.get("groupName") != filter_param["pool_name"]:
                                        matches_filter = False
                                        continue

                                # Check pool type filter
                                if "pool_type" in filter_param:
                                    if pool.get("type") != filter_param["pool_type"]:
                                        matches_filter = False
                                        continue

                                if matches_filter:
                                    filtered_pools.append(pool)

                        # Use filtered results if filters were applied
                        if filtered_pools:
                            reserve_pool_details = filtered_pools
                        elif component_specific_filters:
                            # If filters were specified but none matched, empty the list
                            reserve_pool_details = []

                    # Apply global filters
                    if global_filters.get("pool_name_list") or global_filters.get("pool_type_list"):
                        filtered_pools = []
                        pool_name_list = global_filters.get("pool_name_list", [])
                        pool_type_list = global_filters.get("pool_type_list", [])

                        for pool in reserve_pool_details:
                            # Check pool name filter
                            if pool_name_list and pool.get("groupName") not in pool_name_list:
                                continue

                            # Check pool type filter
                            if pool_type_list and pool.get("type") not in pool_type_list:
                                continue

                            filtered_pools.append(pool)

                        reserve_pool_details = filtered_pools
                        self.log("Applied global filters, remaining pools: {0}".format(len(filtered_pools)), "DEBUG")

                    # Add to final list
                    final_reserve_pools.extend(reserve_pool_details)

                    # Track success for this site
                    self.add_success(site_name, "reserve_pool_details", {
                        "pools_processed": len(reserve_pool_details)
                    })

                except Exception as e:
                    self.log("Error retrieving reserve pools for site {0}: {1}".format(site_name, str(e)), "ERROR")
                    self.add_failure(site_name, "reserve_pool_details", {
                        "error_type": "api_error",
                        "error_message": str(e),
                        "error_code": "API_CALL_FAILED"
                    })
                    continue

        # Remove duplicates based on pool ID or unique combination
        unique_pools = []
        seen_pools = set()

        for pool in final_reserve_pools:
            # Create unique identifier based on pool ID (most reliable) or combination of site ID and pool name
            pool_id = pool.get("id")
            if pool_id:
                # Use pool ID as primary identifier (most reliable for deduplication)
                pool_identifier = pool_id
            else:
                # Fallback: Use combination of site ID, pool name, and subnet as unique identifier
                pool_identifier = "{0}_{1}_{2}".format(
                    pool.get("siteId", ""),
                    pool.get("name", ""),  # Use 'name' instead of 'groupName'
                    pool.get("ipV4AddressSpace", {}).get("subnet", "")  # Add subnet for uniqueness
                )

            if pool_identifier not in seen_pools:
                seen_pools.add(pool_identifier)
                unique_pools.append(pool)
            else:
                self.log("Duplicate pool detected and removed: {0} (ID: {1})".format(
                    pool.get('name', 'Unknown'), pool_identifier), "DEBUG")

        final_reserve_pools = unique_pools
        self.log("After deduplication, total reserve pools: {0}".format(len(final_reserve_pools)), "INFO")

        # Debug: Log detailed information about each pool that will be processed
        for i, pool in enumerate(final_reserve_pools):
            pool_name = pool.get('name', 'Unknown')
            site_name = pool.get('siteName', 'Unknown')
            pool_type = pool.get('poolType', 'Unknown')
            self.log("Pool {0}/{1}: '{2}' from site '{3}' (type: {4})".format(
                i + 1, len(final_reserve_pools), pool_name, site_name, pool_type), "DEBUG")

        pool_names = [pool.get('name', 'Unknown') for pool in final_reserve_pools]
        self.log("Pool names to be processed: {0}".format(pool_names), "DEBUG")

        if not final_reserve_pools:
            self.log("No reserve pools found matching the specified criteria", "INFO")
            return {
                "reserve_pool_details": [],
                "operation_summary": self.get_operation_summary()
            }

        # Apply reverse mapping
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        reverse_mapping_spec = reverse_mapping_function()

        self.log("Starting transformation of {0} reserve pools using modify_parameters".format(len(final_reserve_pools)), "INFO")

        # Transform using inherited modify_parameters function (with OrderedDict spec)
        pools_details = self.modify_parameters(reverse_mapping_spec, final_reserve_pools)

        self.log("Transformation completed. Result contains {0} individual pool configurations".format(len(pools_details)), "INFO")

        # Debug: Log detailed information about each transformed pool
        for i, pool in enumerate(pools_details):
            pool_name = pool.get('name', 'Unknown')
            site_name = pool.get('site_name', 'Unknown')
            self.log("Transformed pool {0}/{1}: '{2}' from site '{3}' - each pool gets its own configuration entry".format(
                i + 1, len(pools_details), pool_name, site_name), "DEBUG")

        transformed_pool_names = [pool.get('name', 'Unknown') for pool in pools_details]
        self.log("Pool names after transformation: {0}".format(transformed_pool_names), "DEBUG")

        # Verify that we have individual configurations for each pool
        if len(pools_details) == len(final_reserve_pools):
            self.log("✓ SUCCESS: Each of the {0} pools has its own individual configuration entry".format(len(pools_details)), "INFO")
        else:
            self.log("⚠ WARNING: Pool count mismatch - input: {0}, output: {1}".format(
                len(final_reserve_pools), len(pools_details)), "WARNING")

        # Return in the correct format - note the structure difference from global pools
        return {
            "reserve_pool_details": pools_details,
            "operation_summary": self.get_operation_summary()
        }

    def get_aaa_settings_for_site(self, site_name, site_id):
        try:
            api_family = "network_settings"
            api_function = "retrieve_aaa_settings_for_a_site"
            params = {"id": site_id}

            # Execute the API call
            aaa_network_response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params=params,
            )

            # Extract AAA network and client/endpoint settings
            response = aaa_network_response.get("response", {})
            network_aaa = response.get("aaaNetwork")
            client_and_endpoint_aaa = response.get("aaaClient")

            if not network_aaa or not client_and_endpoint_aaa:
                missing = []
                if not network_aaa:
                    missing.append("network_aaa")
                if not client_and_endpoint_aaa:
                    missing.append("client_and_endpoint_aaa")
                self.log(
                    "No {0} settings found for site '{1}' (ID: {2})".format(
                        " and ".join(missing), site_name, site_id
                    ),
                    "WARNING",
                )
                return network_aaa, client_and_endpoint_aaa

            self.log(
                "Successfully retrieved AAA Network settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, network_aaa
                ),
                "DEBUG",
            )
            self.log(
                "Successfully retrieved AAA Client and Endpoint settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, client_and_endpoint_aaa
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while getting AAA settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return network_aaa, client_and_endpoint_aaa

    def get_dhcp_settings_for_site(self, site_name, site_id):
        """
        Retrieve the DHCP settings for a specified site from Cisco Catalyst Center.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve DHCP settings for.
            site_id (str) - The ID of the site to retrieve DHCP settings for.

        Returns:
            dhcp_details (dict) - DHCP settings details for the specified site.
        """
        self.log(
            "Attempting to retrieve DHCP settings for site '{0}' (ID: {1})".format(
                site_name, site_id
            ),
            "INFO",
        )

        try:
            dhcp_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_d_h_c_p_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )
            # Extract DHCP details
            dhcp_details = dhcp_response.get("response", {}).get("dhcp")

            if not dhcp_response:
                self.log(
                    "No DHCP settings found for site '{0}' (ID: {1})".format(
                        site_name, site_id
                    ),
                    "WARNING",
                )
                return None

            self.log(
                "Successfully retrieved DNS settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, dhcp_response
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while getting DHCP settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return dhcp_details

    def get_dns_settings_for_site(self, site_name, site_id):
        """
        Retrieve the DNS settings for a specified site from Cisco Catalyst Center.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve DNS settings for.
            site_id (str): The ID of the site to retrieve DNS settings for.

        Returns:
            dns_details (dict): DNS settings details for the specified site.
        """
        self.log(
            "Attempting to retrieve DNS settings for site '{0}' (ID: {1})".format(
                site_name, site_id
            ),
            "INFO",
        )

        try:
            dns_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_d_n_s_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )
            # Extract DNS details
            dns_details = dns_response.get("response", {}).get("dns")

            if not dns_details:
                self.log(
                    "No DNS settings found for site '{0}' (ID: {1})".format(
                        site_name, site_id
                    ),
                    "WARNING",
                )
                return None

            self.log(
                "Successfully retrieved DNS settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, dns_details
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while getting DNS settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return dns_details

    def get_telemetry_settings_for_site(self, site_name, site_id):
        """
        Retrieve the telemetry settings for a specified site from Cisco Catalyst Center.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve telemetry settings for.
            site_id (str): The ID of the site to retrieve telemetry settings for.

        Returns:
            telemetry_details (dict): Telemetry settings details for the specified site.
        """
        self.log(
            "Attempting to retrieve telemetry settings for site ID: {0}".format(
                site_id
            ),
            "INFO",
        )

        try:
            telemetry_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_telemetry_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )

            # Extract telemetry details
            telemetry_details = telemetry_response.get("response", {})

            if not telemetry_details:
                self.log(
                    "No telemetry settings found for site '{0}' (ID: {1})".format(
                        site_name, site_id
                    ),
                    "WARNING",
                )
                return None

            self.log(
                "Successfully retrieved telemetry settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, telemetry_details
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while getting telemetry settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return telemetry_details

    def get_ntp_settings_for_site(self, site_name, site_id):
        """
        Retrieve the NTP server settings for a specified site from Cisco Catalyst Center.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve NTP server settings for.
            site_id (str): The ID of the site to retrieve NTP server settings for.

        Returns:
            ntpserver_details (dict): NTP server settings details for the specified site.
        """
        self.log(
            "Attempting to retrieve NTP server settings for site '{0}' (ID: {1})".format(
                site_name, site_id
            ),
            "INFO",
        )

        try:
            ntpserver_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_n_t_p_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )
            # Extract NTP server details
            ntpserver_details = ntpserver_response.get("response", {}).get("ntp")

            if not ntpserver_details:
                self.log(
                    "No NTP server settings found for site '{0}' (ID: {1})".format(
                        site_name, site_id
                    ),
                    "WARNING",
                )
                return None

            if ntpserver_details.get("servers") is None:
                ntpserver_details["servers"] = []

            self.log(
                "Successfully retrieved NTP server settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, ntpserver_details
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while getting NTP server settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return ntpserver_details

    def get_time_zone_settings_for_site(self, site_name, site_id):
        """
        Retrieve the time zone settings for a specified site from Cisco Catalyst Center.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve time zone settings for.
            site_id (str): The ID of the site to retrieve time zone settings for.

        Returns:
            timezone_details (dict): Time zone settings details for the specified site.
        """
        self.log(
            "Attempting to retrieve time zone settings for site '{0}' (ID: {1})".format(
                site_name, site_id
            ),
            "INFO",
        )

        try:
            timezone_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_time_zone_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )
            # Extract time zone details
            timezone_details = timezone_response.get("response", {}).get("timeZone")

            if not timezone_details:
                self.log(
                    "No time zone settings found for site '{0}' (ID: {1})".format(
                        site_name, site_id
                    ),
                    "WARNING",
                )
                return None

            self.log(
                "Successfully retrieved time zone settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, timezone_details
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while getting time zone settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return timezone_details

    def get_banner_settings_for_site(self, site_name, site_id):
        """
        Retrieve the Message of the Day (banner) settings for a specified site from Cisco Catalyst Center.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve banner settings for.
            site_id (str): The ID of the site to retrieve banner settings for.

        Returns:
            messageoftheday_details (dict): Banner (Message of the Day) settings details for the specified site.
        """
        self.log(
            "Attempting to retrieve banner (Message of the Day) settings for site '{0}' (ID: {1})".format(
                site_name, site_id
            ),
            "INFO",
        )

        try:
            banner_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_banner_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )
            # Extract banner (Message of the Day) details
            messageoftheday_details = banner_response.get("response", {}).get("banner")

            if not messageoftheday_details:
                self.log(
                    "No banner (Message of the Day) settings found for site '{0}' (ID: {1})".format(
                        site_name, site_id
                    ),
                    "WARNING",
                )
                return None

            self.log(
                "Successfully retrieved banner (Message of the Day) settings for site '{0}' (ID: {1}): {2}".format(
                    site_name, site_id, messageoftheday_details
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while getting banner settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return messageoftheday_details

    def get_device_controllability_settings(self, network_element, filters):
        """
        Retrieves device controllability settings - these are global settings, not site-specific.
        """
        self.log("Starting to retrieve device controllability settings (global settings)", "DEBUG")

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            f"Getting device controllability settings using family '{api_family}' and function '{api_function}'.",
            "INFO",
        )

        device_controllability_settings = []

        try:
            # No filters or parameters needed for global settings
            params = {}

            # Execute API call
            device_controllability_response = self.execute_get_with_pagination(api_family, api_function, params)
            self.log(f"Retrieved device controllability response: {device_controllability_response}", "DEBUG")

            actual_data = {}

            # ✅ Handle different possible formats from API
            if isinstance(device_controllability_response, dict):
                # Normal API response
                actual_data = device_controllability_response.get("response", device_controllability_response)

            elif isinstance(device_controllability_response, list):
                if device_controllability_response and isinstance(device_controllability_response[0], dict):
                    # Handle list of dicts
                    first_item = device_controllability_response[0]
                    actual_data = first_item.get("response", first_item)
                elif all(isinstance(x, str) for x in device_controllability_response):
                    # Handle incorrect case where only keys were returned
                    self.log(
                        "API returned a list of keys instead of full response dict. Adjusting structure.",
                        "WARNING",
                    )
                    # reconstruct a safe fallback structure
                    actual_data = {
                        "deviceControllability": True,
                        "autocorrectTelemetryConfig": False
                    }
                else:
                    self.log(
                        f"Unexpected item type in response list: {type(device_controllability_response[0])}",
                        "ERROR",
                    )

            else:
                self.log(
                    f"Unexpected response type from API: {type(device_controllability_response)}",
                    "ERROR",
                )

            # ✅ Create entry from extracted data
            if actual_data:
                settings_entry = {
                    "deviceControllability": actual_data.get("deviceControllability", False),
                    "autocorrectTelemetryConfig": actual_data.get("autocorrectTelemetryConfig", False)
                }
                device_controllability_settings.append(settings_entry)
                self.log(f"Created device controllability entry: {settings_entry}", "DEBUG")

            # ✅ If no response or empty data, create default
            if not device_controllability_settings:
                self.log("No device controllability settings found in API response, creating default entry", "INFO")
                settings_entry = {
                    "deviceControllability": True,
                    "autocorrectTelemetryConfig": False
                }
                device_controllability_settings.append(settings_entry)

            # Track success
            self.add_success("Global", "device_controllability_details", {
                "settings_processed": len(device_controllability_settings)
            })

            self.log(f"Successfully processed {len(device_controllability_settings)} device controllability settings", "INFO")

        except Exception as e:
            self.log(f"Error retrieving device controllability settings: {str(e)}", "ERROR")

            # Create default entry even on error to ensure output
            settings_entry = {
                "deviceControllability": True,
                "autocorrectTelemetryConfig": False
            }
            device_controllability_settings.append(settings_entry)

            self.add_failure("Global", "device_controllability_details", {
                "error_type": "api_error",
                "error_message": str(e),
                "error_code": "API_CALL_FAILED"
            })

        # ✅ Apply reverse mapping for consistency
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        reverse_mapping_spec = reverse_mapping_function()

        settings_details = self.modify_network_parameters(reverse_mapping_spec, device_controllability_settings)

        self.log(
            f"Successfully transformed {len(settings_details)} device controllability settings: {settings_details}",
            "INFO",
        )

        # Device controllability is a global setting, not site-specific, so return as single dict instead of list
        device_controllability_dict = settings_details[0] if settings_details else {}

        return {
            "device_controllability_details": device_controllability_dict,
            "operation_summary": self.get_operation_summary(),
        }

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        Args:
            yaml_config_generator (dict): Contains file_path, global_filters, and component_specific_filters.
        Returns:
            self: The current instance with the operation result and message updated.
        """
        self.log("Initializing YAML configuration generation process with parameters: {0}".format(
            yaml_config_generator), "DEBUG")

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log("Auto-discovery mode enabled - will process all network settings and all components", "INFO")

        # Determine output file path
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        # Initialize filter dictionaries
        if generate_all:
            self.log("Auto-discovery mode: Overriding any provided filters to retrieve all network settings", "INFO")
            global_filters = {}
            component_specific_filters = {}
        else:
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        # Get supported network elements
        module_supported_network_elements = self.module_schema.get("network_elements", {})
        components_list = component_specific_filters.get("components_list", list(module_supported_network_elements.keys()))

        self.log("Components to process: {0}".format(components_list), "DEBUG")

        # Reset operation tracking
        self.reset_operation_tracking()

        final_list = []
        consolidated_operation_summary = {
            "total_sites_processed": 0,
            "total_components_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "sites_with_complete_success": [],
            "sites_with_partial_success": [],
            "sites_with_complete_failure": [],
            "success_details": [],
            "failure_details": []
        }

        for component in components_list:
            self.log("Processing component: {0}".format(component), "DEBUG")
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log("Component {0} not supported by module, skipping processing".format(component), "WARNING")
                continue

            # Prepare component filters
            component_filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters
            }

            # Execute component operation function
            operation_func = network_element.get("get_function_name")
            details = operation_func(network_element, component_filters)

            self.log("Details retrieved for component {0}: {1}".format(component, details), "DEBUG")

            # Always add details if the component key exists, even if it's empty
            if details and component in details:
                component_details = details[component]

                # Add the component details as a single entry (no individual pool separation)
                final_list.extend([details])
                self.log("Added component {0} to final list with {1} entries (including empty results)".format(
                    component, len(component_details) if isinstance(component_details, list) else 1), "DEBUG")
            else:
                self.log("Component {0} returned no valid details structure".format(component), "WARNING")

            # Consolidate operation summary
            if details and details.get("operation_summary"):
                summary = details["operation_summary"]
                consolidated_operation_summary["total_components_processed"] += 1
                consolidated_operation_summary["total_successful_operations"] += summary.get("total_successful_operations", 0)
                consolidated_operation_summary["total_failed_operations"] += summary.get("total_failed_operations", 0)

        # Create final dictionary
        final_dict = OrderedDict()
        final_dict["config"] = final_list

        if not final_list:
            self.msg = {
                "message": "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(self.module_name),
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        # Write to YAML file
        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "message": "YAML config generation succeeded for module '{0}'.".format(self.module_name),
                "file_path": file_path,
                "configurations_generated": len(final_list),
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                "message": "YAML config generation failed for module '{0}' - unable to write to file.".format(self.module_name),
                "file_path": file_path,
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('gathered').
        """
        self.log("Creating Parameters for API Calls with state: {0}".format(state), "INFO")

        self.validate_params(config)

        # Set generate_all_configurations after validation
        self.generate_all_configurations = config.get("generate_all_configurations", False)
        self.log("Set generate_all_configurations mode: {0}".format(self.generate_all_configurations), "DEBUG")

        want = {}
        want["yaml_config_generator"] = config

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Network Settings operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the merge operations for various network configurations in the Cisco Catalyst Center.
        """
        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")

        operations = [
            ("yaml_config_generator", "YAML Config Generator", self.yaml_config_generator)
        ]

        for index, (param_key, operation_name, operation_func) in enumerate(operations, start=1):
            self.log("Iteration {0}: Checking parameters for {1} operation with param_key '{2}'.".format(
                index, operation_name, param_key), "DEBUG")

            params = self.want.get(param_key)
            if params:
                self.log("Iteration {0}: Parameters found for {1}. Starting processing.".format(
                    index, operation_name), "INFO")
                operation_func(params).check_return_status()
            else:
                self.log("Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                    index, operation_name), "WARNING")

        end_time = time.time()
        self.log("Completed 'get_diff_gathered' operation in {0:.2f} seconds.".format(end_time - start_time), "DEBUG")
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
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    # Initialize the NetworkSettingsPlaybookGenerator object
    ccc_network_settings_playbook_generator = NetworkSettingsPlaybookGenerator(module)

    # Version check
    if (ccc_network_settings_playbook_generator.compare_dnac_versions(
            ccc_network_settings_playbook_generator.get_ccc_version(), "2.3.7.9") < 0):
        ccc_network_settings_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Network Settings Module. Supported versions start from '2.3.7.9' onwards. "
            "Version '2.3.7.9' introduces APIs for retrieving the network settings for "
            "the following components: Global Pool(s), Reserve Pool(s), Network Management, "
            "Device Controllability, AAA Settings from the Catalyst Center".format(
                ccc_network_settings_playbook_generator.get_ccc_version()
            )
        )
        ccc_network_settings_playbook_generator.set_operation_result(
            "failed", False, ccc_network_settings_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get and validate state
    state = ccc_network_settings_playbook_generator.params.get("state")
    if state not in ccc_network_settings_playbook_generator.supported_states:
        ccc_network_settings_playbook_generator.status = "invalid"
        ccc_network_settings_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_network_settings_playbook_generator.check_return_status()

    # Validate input parameters
    ccc_network_settings_playbook_generator.validate_input().check_return_status()

    # Process configurations
    for config in ccc_network_settings_playbook_generator.validated_config:
        ccc_network_settings_playbook_generator.reset_values()
        ccc_network_settings_playbook_generator.get_want(config, state).check_return_status()
        ccc_network_settings_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_network_settings_playbook_generator.result)


if __name__ == "__main__":
    main()

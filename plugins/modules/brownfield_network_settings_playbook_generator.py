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
        Analyzes pool structure using multiple detection methods in priority order
        to determine whether the pool is configured for IPv4 or IPv6 address space.
        Detection examines explicit flags, IP address formats, and server configurations.

        Args:
            pool_details (dict or None): Complete pool configuration object

        Returns:
            str or None: Address space identifier:
                - "IPv4": For IPv4 address pools
                - "IPv6": For IPv6 address pools
                - None: When address space cannot be determined

        Detection Priority (stops at first match):
            1. Explicit "ipv6" boolean field (most reliable)
            2. Gateway IP address format validation
            3. Subnet IP address format validation
            4. Pool type name contains "ipv6" or "v6"
            5. DHCP/DNS server IP address formats
            6. Fallback to IPv4 if addressSpace exists
        """
        self.log("Determining IP address space (IPv4/IPv6) from pool configuration using "
                 "multiple detection methods in priority order",
                 "DEBUG")
        if pool_details is None or not isinstance(pool_details, dict):
            self.log("Pool configuration validation failed - received {0} instead of dict, "
                     "cannot determine address space".format(type(pool_details).__name__),
                     "DEBUG")
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
            result = self._determine_address_space_from_ip(gateway, "gateway")
            if result:
                return result

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
            if subnet:
                result = self._determine_address_space_from_ip(subnet, "subnet")
            if result:
                return result

        # Method 4: Check for poolType containing IPv6 indicators
        pool_type = pool_details.get("poolType", "")
        if pool_type:
            pool_type_lower = pool_type.lower()
            if "v6" in pool_type_lower or "ipv6" in pool_type_lower:
                self.log(
                    "Detected IPv6 address space from pool type name: {0}".format(
                        pool_type
                    ),
                    "DEBUG"
                )
                return "IPv6"

        # Ensure server lists are actually lists
        if not isinstance(dhcp_servers, list):
            dhcp_servers = [dhcp_servers] if dhcp_servers else []
        if not isinstance(dns_servers, list):
            dns_servers = [dns_servers] if dns_servers else []

        for server in dhcp_servers + dns_servers:
            if server:
                result = self._determine_address_space_from_ip(server, "server")
            if result:
                return result

        # Fallback: Default to IPv4 if address space exists but type unclear
        if address_space or gateway or subnet:
            self.log(
                "Unable to definitively determine address space from pool data, "
                "defaulting to IPv4 based on presence of address space configuration",
                "DEBUG"
            )
            return "IPv4"

        self.log("Unable to determine address space - no valid IP configuration found "
                 "in pool details",
                 "WARNING")
        return None

    def _determine_address_space_from_ip(self, ip_address, source):
        """
        Determines address space (IPv4/IPv6) from IP address format.

        Analyzes IP address string to determine whether it represents an IPv4
        or IPv6 address based on character patterns (presence of colons vs dots).

        Args:
            ip_address (str): IP address string to analyze
            source (str): Source field name for logging context
                        (e.g., 'gateway', 'subnet', 'server')

        Returns:
            str or None: Address space identifier:
                - "IPv4": If address contains dots (IPv4 format)
                - "IPv6": If address contains colons (IPv6 format)
                - None: If address is empty, invalid, or ambiguous

        Notes:
            - Uses simple character detection (not full IP validation)
            - Colon detection may have false positives (e.g., port numbers)
            - Logs warnings for invalid or ambiguous formats
            - Returns None for empty or whitespace-only strings

        Examples:
            _determine_address_space_from_ip("192.168.1.1", "gateway") -> "IPv4"
            _determine_address_space_from_ip("2001:db8::1", "subnet") -> "IPv6"
            _determine_address_space_from_ip("", "server") -> None
            _determine_address_space_from_ip("invalid", "gateway") -> None
        """
        if not ip_address or not str(ip_address).strip():
            return None

        ip_str = str(ip_address).strip()

        # IPv6 detection (contains colons)
        if ":" in ip_str:
            # Basic validation: IPv6 should have multiple colons
            if ip_str.count(":") >= 2:
                self.log(
                    "Detected IPv6 address space from {0}: {1}".format(
                        source, ip_address
                    ),
                    "DEBUG"
                )
                return "IPv6"
            else:
                # Might be IPv4 with port (e.g., "192.168.1.1:8080")
                self.log(
                    "Ambiguous IP format in {0} (single colon detected): {1}, "
                    "treating as invalid".format(source, ip_address),
                    "WARNING"
                )
                return None

        # IPv4 detection (contains dots)
        elif "." in ip_str:
            self.log(
                "Detected IPv4 address space from {0}: {1}".format(
                    source, ip_address
                ),
                "DEBUG"
            )
            return "IPv4"

        # Invalid format (no colons or dots)
        else:
            self.log(
                "Invalid IP address format in {0}: {1} (no colons or dots)".format(
                    source, ip_address
                ),
                "WARNING"
            )
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

        Detection Priority (stops at first match):
        1. addressSpace.subnet + addressSpace.prefixLength (primary)
        2. Direct subnet + prefixLength fields
        3. Alternative fields (ipSubnet, network) + (prefixLen, maskLength)
        4. Subnet mask conversion (255.255.255.0 -> /24)
        5. Existing CIDR field (cidr, ipRange, range)

        Examples:
            IPv4: {"addressSpace": {"subnet": "192.168.1.0", "prefixLength": 24}} -> "192.168.1.0/24"
            IPv6: {"addressSpace": {"subnet": "2001:db8::", "prefixLength": 64}} -> "2001:db8::/64"
            Invalid: None -> None
            Missing data: {"addressSpace": {}} -> None
        """
        self.log("Starting CIDR transformation with pool_details: {0}".format(pool_details), "DEBUG")
        if pool_details is None:
            self.log("Pool details validation failed - expected dict, got {0}".format(
                     type(pool_details).__name__), "WARNING")
            return None

        if not isinstance(pool_details, dict):
            self.log(
                "Pool details validation failed - expected dict, got {0}".format(
                    type(pool_details).__name__
                ),
                "WARNING"
            )
            return None

        self.log(
            "Processing pool configuration with keys: {0}".format(
                list(pool_details.keys())
            ),
            "DEBUG"
        )

        # Method 1: Check addressSpace structure (primary method)
        address_space = pool_details.get("addressSpace") or {}
        subnet = address_space.get("subnet")
        prefix_length = address_space.get("prefixLength")

        cidr = self._build_cidr_notation(subnet, prefix_length, "direct fields")
        if cidr:
            return cidr

        # Method 2: Check direct subnet and prefixLength fields
        subnet = pool_details.get("subnet")
        prefix_length = pool_details.get("prefixLength")

        cidr = self._build_cidr_notation(subnet, prefix_length, "direct fields")
        if cidr:
            return cidr

        # Method 3: Check for alternative field names
        subnet = pool_details.get("ipSubnet") or pool_details.get("network")
        prefix_length = (
            pool_details.get("prefixLen") or
            pool_details.get("maskLength") or
            pool_details.get("subnetMask")
        )

        # Convert subnet mask to prefix length if needed
        if prefix_length and isinstance(prefix_length, str) and "." in prefix_length:
            # Convert subnet mask (e.g., "255.255.255.0") to prefix length (e.g., 24)
            self.log(
                "Detected subnet mask format, attempting conversion: {0}".format(
                    prefix_length
                ),
                "DEBUG"
            )
            prefix_length = self._convert_subnet_mask_to_prefix(prefix_length)
            try:
                import ipaddress
                prefix_length = ipaddress.IPv4Network('0.0.0.0/' + prefix_length).prefixlen
            except Exception:
                pass

        if subnet and prefix_length:
            cidr = self._build_cidr_notation(subnet, prefix_length, "alternative fields")
            if cidr:
                return cidr

        # Method 4: Look for existing CIDR format
        existing_cidr = pool_details.get("cidr") or pool_details.get("ipRange") or pool_details.get("range")
        existing_cidr = (
            pool_details.get("cidr") or
            pool_details.get("ipRange") or
            pool_details.get("range")
        )
        if existing_cidr:
            if self._validate_cidr_format(existing_cidr):
                self.log(
                    "Found valid existing CIDR notation: {0}".format(existing_cidr),
                    "DEBUG"
                )
                return existing_cidr
            else:
                self.log(
                    "Found CIDR field but format is invalid: {0}".format(existing_cidr),
                    "WARNING"
                )

        self.log("transform_cidr: no valid CIDR components found", "DEBUG")
        self.log("Unable to extract CIDR notation - no valid subnet/prefix combination "
                 "found in pool configuration",
                 "WARNING"
                 )

        return None

    def _build_cidr_notation(self, subnet, prefix_length, source):
        """
        Build CIDR notation from subnet and prefix length with validation.

        Args:
            subnet (str or None): Network subnet address
            prefix_length (int, str, or None): Network prefix length
            source (str): Source field name for logging context

        Returns:
            str or None: Valid CIDR notation or None if invalid
        """
        if not subnet or prefix_length is None:
            return None

        # Validate prefix length is numeric and in valid range
        try:
            prefix_int = int(prefix_length)

            # Determine IP version from subnet format
            is_ipv6 = ":" in str(subnet)
            max_prefix = 128 if is_ipv6 else 32

            if not (0 <= prefix_int <= max_prefix):
                self.log(
                    "Invalid prefix length {0} from {1} (must be 0-{2} for {3})".format(
                        prefix_int, source, max_prefix, "IPv6" if is_ipv6 else "IPv4"
                    ),
                    "WARNING"
                )
                return None

            cidr = "{0}/{1}".format(subnet, prefix_int)
            self.log(
                "Built CIDR notation from {0}: {1}".format(source, cidr),
                "DEBUG"
            )
            return cidr

        except (ValueError, TypeError) as e:
            self.log(
                "Failed to build CIDR from {0} (subnet: {1}, prefix: {2}): {3}".format(
                    source, subnet, prefix_length, str(e)
                ),
                "WARNING"
            )
            return None

    def _convert_subnet_mask_to_prefix(self, subnet_mask):
        """
        Convert IPv4 subnet mask to prefix length.

        Args:
            subnet_mask (str): Subnet mask in dotted decimal format (e.g., "255.255.255.0")

        Returns:
            int or None: Prefix length (e.g., 24) or None if conversion fails
        """
        try:
            import ipaddress
            network = ipaddress.IPv4Network('0.0.0.0/' + subnet_mask, strict=False)
            prefix_length = network.prefixlen

            self.log(
                "Converted subnet mask {0} to prefix length {1}".format(
                    subnet_mask, prefix_length
                ),
                "DEBUG"
            )
            return prefix_length

        except (ValueError, ipaddress.AddressValueError, ipaddress.NetmaskValueError) as e:
            self.log(
                "Failed to convert subnet mask to prefix length: {0}, error: {1}".format(
                    subnet_mask, str(e)
                ),
                "WARNING"
            )
            return None

    def _validate_cidr_format(self, cidr):
        """
        Validate CIDR notation format using ipaddress module.

        Args:
            cidr (str): CIDR string to validate (e.g., "192.168.1.0/24")

        Returns:
            bool: True if valid CIDR format, False otherwise
        """
        if not cidr or "/" not in str(cidr):
            return False

        try:
            import ipaddress
            ipaddress.ip_network(cidr, strict=False)
            return True
        except (ValueError, ipaddress.AddressValueError, ipaddress.NetmaskValueError):
            return False

    def transform_preserve_empty_list(self, data, field_path):
        """
        Extract nested field value while preserving empty lists for network configuration.

        This transformation function specifically handles DHCP/DNS server configurations
        where empty lists have semantic meaning (e.g., "no DHCP servers configured")
        and must be preserved in the output, unlike the default helper behavior that
        filters out empty collections.

        Args:
            data (dict or None): Source data dictionary containing nested configuration.
                                Can be None or empty dict.
            field_path (str): Dot-separated path to target field in nested structure.
                            Examples: "ipV4AddressSpace.dhcpServers",
                                    "ipV6AddressSpace.dnsServers"

        Returns:
            list: The list value at the specified field path, or empty list if:
                - data is None
                - field_path not found in data
                - field value is None
                - field exists but is not a list (returns empty list)
                Empty lists are explicitly preserved to maintain semantic meaning.
        """
        self.log(
            "Extracting field '{0}' from data while preserving empty lists".format(
                field_path
            ),
            "DEBUG"
        )
        if data is None:
            # Validate field_path parameter
            if not field_path or not isinstance(field_path, str):
                self.log(
                    "Invalid field_path parameter: {0} (type: {1}), "
                    "must be non-empty string".format(
                        field_path, type(field_path).__name__
                    ),
                    "WARNING"
                )
                return []

            # Validate data parameter
            if data is None:
                self.log(
                    "Input data is None, returning empty list for field '{0}'".format(
                        field_path
                    ),
                    "DEBUG"
                )
                return []

        if not isinstance(data, dict):
            self.log(
                "Input data is not a dict (type: {0}), cannot navigate "
                "field path '{1}'".format(
                    type(data).__name__, field_path
                ),
                "WARNING"
            )
            return []

        # Navigate the field path (e.g., "ipV4AddressSpace.dhcpServers")
        field_value = data
        field_segments = field_path.split('.')

        self.log(
            "Navigating through {0} field segment(s): {1}".format(
                len(field_segments), field_segments
            ),
            "DEBUG"
        )

        for field_name in field_segments:
            # Strip whitespace from field name
            field_name = field_name.strip()

            # Skip empty segments (in case of ".." or trailing dots)
            if not field_name:
                self.log(
                    "Skipping empty field segment in path '{0}'".format(field_path),
                    "DEBUG"
                )
                continue

            # Navigate to next level
            if not isinstance(field_value, dict):
                self.log(
                    "Cannot navigate further - current value is not a dict "
                    "(type: {0}) at field '{1}' in path '{2}'".format(
                        type(field_value).__name__, field_name, field_path
                    ),
                    "DEBUG"
                )
                return []

            field_value = field_value.get(field_name)

            if field_value is None:
                self.log(
                    "Field '{0}' not found in path '{1}', returning empty list".format(
                        field_name, field_path
                    ),
                    "DEBUG"
                )
                return []

        # Check if we successfully navigated to a list
        if isinstance(field_value, list):
            self.log(
                "Successfully extracted list from '{0}': {1} item(s) "
                "(empty list preserved)".format(
                    field_path, len(field_value)
                ),
                "DEBUG"
            )
            return field_value

        # If field exists but is not a list, log warning and return empty list
        self.log(
            "Field '{0}' exists but is not a list (type: {1}, value: {2}). "
            "Returning empty list for safety.".format(
                field_path, type(field_value).__name__, field_value
            ),
            "WARNING"
        )
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
        self.log(
            "Extracting IPv4 DHCP servers from pool/network data while "
            "preserving empty lists",
            "DEBUG"
        )

        result = self.transform_preserve_empty_list(data, "ipV4AddressSpace.dhcpServers")

        self.log(
            "Extracted IPv4 DHCP servers: {0} server(s) (empty list preserved)".format(
                len(result) if result else 0
            ),
            "DEBUG"
        )

        return result

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
        self.log(
            "Extracting IPv4 DNS servers from pool/network data while "
            "preserving empty lists",
            "DEBUG"
        )

        result = self.transform_preserve_empty_list(data, "ipV4AddressSpace.dnsServers")

        self.log(
            "Extracted IPv4 DNS servers: {0} server(s) (empty list preserved)".format(
                len(result) if result else 0
            ),
            "DEBUG"
        )

        return result

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
        self.log(
            "Extracting IPv6 DHCP servers from pool/network data while "
            "preserving empty lists",
            "DEBUG"
        )

        result = self.transform_preserve_empty_list(data, "ipV6AddressSpace.dhcpServers")

        self.log(
            "Extracted IPv6 DHCP servers: {0} server(s) (empty list preserved)".format(
                len(result) if result else 0
            ),
            "DEBUG"
        )

        return result

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
        self.log(
            "Extracting IPv6 DNS servers from pool/network data while "
            "preserving empty lists",
            "DEBUG"
        )

        result = self.transform_preserve_empty_list(data, "ipV6AddressSpace.dnsServers")

        self.log(
            "Extracted IPv6 DNS servers: {0} server(s) (empty list preserved)".format(
                len(result) if result else 0
            ),
            "DEBUG"
        )

        return result

    def get_global_pool_lookup(self):
        """
        Build and cache a lookup mapping of global pool IDs to their properties.

        Creates an in-memory lookup table that maps global pool UUIDs to their
        CIDR notation, names, and IP address space version (IPv4/IPv6). This lookup
        is cached to optimize performance during reserve pool processing, where
        reserve pools reference parent global pools by ID.

        Performance Optimization:
            - Results are cached in self._global_pool_lookup attribute
            - Subsequent calls return cached data without API calls
            - Cache persists for the lifetime of the module instance
            - Significantly reduces API calls during bulk reserve pool operations

        Returns:
            dict: Mapping of global pool IDs to their details:
                {
                    "uuid-pool-1": {
                        "cidr": "10.0.0.0/8",
                        "name": "Global_Pool_Corporate",
                        "ip_address_space": "IPv4"
                    },
                    "uuid-pool-2": {
                        "cidr": "2001:db8::/32",
                        "name": "Global_Pool_IPv6",
                        "ip_address_space": "IPv6"
                    }
                }
                Returns empty dict {} if:
                - No global pools exist in Catalyst Center
                - API call fails
                - Unable to process pool data
        """
        if hasattr(self, '_global_pool_lookup'):
            self.log(
                "Returning cached global pool lookup with {0} pools (cache hit - "
                "avoiding API call)".format(len(self._global_pool_lookup)),
                "DEBUG"
            )
            return self._global_pool_lookup

        self.log("Building cached lookup table mapping global pool IDs to CIDR/name/IP "
                 "version for efficient reserve pool processing", "DEBUG")

        try:
            # Get global pools using the API
            global_pools_response = self.execute_get_with_pagination(
                "network_settings",
                "retrieves_global_ip_address_pools",
                {}
            )

            if not global_pools_response:
                self.log(
                    "API returned empty global pools list - creating empty lookup table",
                    "WARNING"
                )
                self._global_pool_lookup = {}
                return self._global_pool_lookup

            self.log(
                "Processing {0} global pools to build lookup table".format(
                    len(global_pools_response)
                ),
                "INFO"
            )

            self._global_pool_lookup = {}

            # Process each global pool
            for pool in global_pools_response:
                pool_id = pool.get('id')
                pool_name = pool.get('name', 'Unknown')

                # Skip pools without IDs (invalid data)
                if not pool_id:
                    self.log(
                        "Skipping pool without ID: name='{0}', type='{1}'".format(
                            pool_name, pool.get('poolType', 'Unknown')
                        ),
                        "WARNING"
                    )
                    continue

                # Extract CIDR using existing transform method for consistency
                cidr = self.transform_cidr(pool)
                if not cidr:
                    self.log(
                        "Failed to extract CIDR for pool '{0}' (ID: {1}) - "
                        "pool may have incomplete address space data".format(
                            pool_name, pool_id
                        ),
                        "WARNING"
                    )

                # Determine IP address space using existing method
                ip_address_space = self.transform_pool_to_address_space(pool)
                if not ip_address_space:
                    # Fallback: Use simple colon detection
                    subnet = pool.get('addressSpace', {}).get('subnet', '')
                    ip_address_space = "IPv6" if ":" in str(subnet) else "IPv4"
                    self.log(
                        "Used fallback IP space detection for pool '{0}': {1}".format(
                            pool_name, ip_address_space
                        ),
                        "DEBUG"
                    )

                # Add to lookup table
                self._global_pool_lookup[pool_id] = {
                    "cidr": cidr,
                    "name": pool_name,
                    "ip_address_space": ip_address_space
                }

                self.log(
                    "Added pool '{0}' to lookup: ID={1}, CIDR={2}, IP_Space={3}".format(
                        pool_name, pool_id, cidr or "None", ip_address_space
                    ),
                    "DEBUG"
                )

            self.log("Successfully created global pool lookup with {0} pools (cache "
                     "created for future use)".format(len(self._global_pool_lookup)), "DEBUG")
            return self._global_pool_lookup

        except (KeyError, TypeError, AttributeError) as e:
            self.log(
                "Error processing global pool data during lookup creation: {0}. "
                "Returning empty lookup to prevent workflow failure.".format(str(e)),
                "ERROR"
            )
            self._global_pool_lookup = {}
            return self._global_pool_lookup

        except Exception as e:
            self.log(
                "Unexpected error creating global pool lookup: {0}. "
                "Returning empty lookup to prevent workflow failure.".format(str(e)),
                "CRITICAL"
            )
            self._global_pool_lookup = {}
            return self._global_pool_lookup

    def transform_global_pool_id_to_cidr(self, pool_data):
        """Transform IPv4 global pool ID to CIDR notation."""
        return self._transform_global_pool_id_to_field(pool_data, 'cidr', 'IPv4')

    def transform_global_pool_id_to_name(self, pool_data):
        """Transform IPv4 global pool ID to pool name."""
        return self._transform_global_pool_id_to_field(pool_data, 'name', 'IPv4')

    def transform_ipv6_global_pool_id_to_cidr(self, pool_data):
        """Transform IPv6 global pool ID to CIDR notation."""
        return self._transform_global_pool_id_to_field(pool_data, 'cidr', 'IPv6')

    def transform_ipv6_global_pool_id_to_name(self, pool_data):
        """Transform IPv6 global pool ID to pool name."""
        return self._transform_global_pool_id_to_field(pool_data, 'name', 'IPv6')

    def _transform_global_pool_id_to_field(self, pool_data, field_name, ip_version="IPv4"):
        """
        Transform global pool ID to a specific field value for reserve pool configuration.

        Extracts global pool properties (CIDR or name) from reserve pool data using
        cached global pool lookup table. Supports both IPv4 and IPv6 address spaces.

        Args:
            pool_data (dict or None): Reserve pool data containing global pool ID references
            field_name (str): Field to extract ('cidr' or 'name')
            ip_version (str): IP version ('IPv4' or 'IPv6')

        Returns:
            str or None: Field value or None if not found
        """
        self.log(
            "Extracting {0} global pool {1} from reserve pool data using "
            "cached global pool lookup table".format(ip_version, field_name),
            "DEBUG"
        )

        try:
            # Validate pool_data
            if not pool_data or not isinstance(pool_data, dict):
                self.log(
                    "Pool data validation failed - expected dict, got {0}".format(
                        type(pool_data).__name__ if pool_data else "None"
                    ),
                    "DEBUG"
                )
                return None
            # Determine address space key based on IP version
            address_space_key = "ipV{0}AddressSpace".format("4" if ip_version == "IPv4" else "6")

            # Extract address space
            ipv_address_space = pool_data.get(address_space_key) or {}
            if not isinstance(ipv_address_space, dict):
                self.log(
                    "{0} address space is not a dict (type: {1})".format(
                        ip_version, type(ipv_address_space).__name__
                    ),
                    "DEBUG"
                )
                return None

            # Extract global pool ID
            global_pool_id = ipv_address_space.get('globalPoolId')
            if not global_pool_id:
                self.log(
                    "No {0} global pool ID found in reserve pool data".format(ip_version),
                    "DEBUG"
                )
                return None

            # Get cached lookup table
            lookup = self.get_global_pool_lookup()
            if not lookup:
                self.log(
                    "Global pool lookup table is empty - cannot map pool ID '{0}'".format(
                        global_pool_id
                    ),
                    "WARNING"
                )
                return None

            # Lookup pool information
            pool_info = lookup.get(global_pool_id)
            if not pool_info:
                self.log(
                    "{0} global pool ID '{1}' not found in lookup table".format(
                        ip_version, global_pool_id
                    ),
                    "WARNING"
                )
                return None

            # Extract field
            field_value = pool_info.get(field_name)
            if not field_value:
                self.log(
                    "{0} global pool ID '{1}' has no {2} configured".format(
                        ip_version, global_pool_id, field_name
                    ),
                    "WARNING"
                )
                return None

            self.log(
                "{0} global pool ID '{1}' mapped to {2}: {3}".format(
                    ip_version, global_pool_id, field_name, field_value
                ),
                "DEBUG"
            )
            return field_value

        except (KeyError, TypeError, AttributeError) as e:
            self.log(
                "Error extracting {0} global pool {1}: {2}".format(
                    ip_version, field_name, str(e)
                ),
                "WARNING"
            )
            return None

        except Exception as e:
            self.log(
                "Unexpected error transforming {0} global pool ID to {1}: {2}".format(
                    ip_version, field_name, str(e)
                ),
                "ERROR"
            )
            return None

    def reserve_pool_reverse_mapping_function(self, requested_components=None):
        """
        Generate reverse mapping specification for Reserve Pool Details transformation.

        This function creates a comprehensive mapping specification that converts
        Catalyst Center API response fields for reserve pools into Ansible-friendly
        configuration keys compatible with the network_settings_workflow_manager module.

        The mapping includes field transformations, type conversions, and special handling
        for complex data structures like IPv4/IPv6 address spaces, server configurations,
        and pool relationships.
        API Response Structure Expected:
            {
                "id": "pool-uuid",
                "name": "Reserve_Pool_1",
                "siteName": "Global/USA/NYC",
                "poolType": "LAN",
                "ipV4AddressSpace": {
                    "subnet": "192.168.1.0",
                    "prefixLength": 24,
                    "gatewayIpAddress": "192.168.1.1",
                    "dhcpServers": ["10.0.0.1"],
                    "dnsServers": ["8.8.8.8"],
                    "globalPoolId": "global-pool-uuid"
                }
            }

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
        self.log("Building reverse mapping specification to transform Catalyst Center reserve pool "
                 "API response into Ansible playbook format for network_settings_workflow_manager module",
                 "DEBUG")

        reverse_mapping_spec = OrderedDict({
            # -------------------------------
            # Basic Pool Information
            # -------------------------------
            "site_name": {
                "type": "str",
                "source_key": "siteName",
                "special_handling": True,
                "transform": self.transform_site_location,
            },
            "name": {"type": "str", "source_key": "name"},
            "prev_name": {"type": "str", "source_key": "previousName", "optional": True},
            "pool_type": {"type": "str", "source_key": "poolType"},

            # -------------------------------
            # IPv6 Address Space Flag
            # -------------------------------
            "ipv6_address_space": {
                "type": "bool",
                "source_key": "ipV6AddressSpace",
                "transform": self.transform_to_boolean,
            },

            # -------------------------------
            # IPv4 Address Space Configuration
            # -------------------------------
            # Global pool references (transformed from UUID to CIDR/name)
            "ipv4_global_pool": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_global_pool_id_to_cidr,
                "optional": True  # Not all reserve pools have parent global pool
            },
            "ipv4_global_pool_name": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_global_pool_id_to_name,
                "optional": True
            },
            # Prefix configuration
            # Boolean flag indicating if IPv4 prefix is configured (for conditional logic)
            "ipv4_prefix": {
                "type": "bool",
                "source_key": "ipV4AddressSpace.prefixLength",
                "transform": self.transform_to_boolean,
            },
            # Actual IPv4 prefix length value (e.g., 24 for /24 network)
            "ipv4_prefix_length": {"type": "int", "source_key": "ipV4AddressSpace.prefixLength"},
            # Network configuration
            "ipv4_subnet": {"type": "str", "source_key": "ipV4AddressSpace.subnet"},
            "ipv4_gateway": {"type": "str", "source_key": "ipV4AddressSpace.gatewayIpAddress"},
            # Server configurations (preserve empty lists for semantic meaning)
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
            # Pool statistics
            "ipv4_total_host": {"type": "int", "source_key": "ipV4AddressSpace.totalAddresses"},

            # Statistics fields commented out to reduce YAML output clutter
            # These are runtime statistics, not configuration parameters
            # Uncomment if detailed pool usage statistics are needed in playbook
            # "ipv4_unassignable_addresses": {"type": "int", "source_key": "ipV4AddressSpace.unassignableAddresses"},
            # "ipv4_assigned_addresses": {"type": "int", "source_key": "ipV4AddressSpace.assignedAddresses"},
            # "ipv4_default_assigned_addresses": {"type": "int", "source_key": "ipV4AddressSpace.defaultAssignedAddresses"},

            # -------------------------------
            # IPv6 Address Space Configuration
            # -------------------------------
            # Global pool references (transformed from UUID to CIDR/name)
            "ipv6_global_pool": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_ipv6_global_pool_id_to_cidr,
                "optional": True  # Not all reserve pools have parent global pool
            },
            "ipv6_global_pool_name": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_ipv6_global_pool_id_to_name,
                "optional": True
            },
            # Prefix configuration
            # Boolean flag indicating if IPv6 prefix is configured
            "ipv6_prefix": {
                "type": "bool",
                "source_key": "ipV6AddressSpace.prefixLength",
                "transform": self.transform_to_boolean,
            },
            # Actual IPv6 prefix length value (e.g., 64 for /64 network)
            "ipv6_prefix_length": {"type": "int", "source_key": "ipV6AddressSpace.prefixLength"},
            # Network configuration
            "ipv6_subnet": {"type": "str", "source_key": "ipV6AddressSpace.subnet"},
            "ipv6_gateway": {"type": "str", "source_key": "ipV6AddressSpace.gatewayIpAddress"},
            "ipv6_dhcp_servers": {
                "type": "list",
                "special_handling": True,
                "transform": self.transform_ipv6_dhcp_servers
            },
            # Server configurations (preserve empty lists for semantic meaning)
            "ipv6_dns_servers": {
                "type": "list",
                "special_handling": True,
                "transform": self.transform_ipv6_dns_servers
            },
            # Pool statistics
            "ipv6_total_host": {"type": "int", "source_key": "ipV6AddressSpace.totalAddresses"},
            # Statistics fields commented out to reduce YAML output clutter
            # Uncomment if detailed pool usage statistics are needed in playbook
            # "ipv6_unassignable_addresses": {"type": "int", "source_key": "ipV6AddressSpace.unassignableAddresses"},
            # "ipv6_assigned_addresses": {"type": "int", "source_key": "ipV6AddressSpace.assignedAddresses"},
            # "ipv6_default_assigned_addresses": {"type": "int", "source_key": "ipV6AddressSpace.defaultAssignedAddresses"},

            # IPv6-specific features
            "slaac_support": {"type": "bool", "source_key": "ipV6AddressSpace.slaacSupport"},

        })

        self.log(
            "Successfully created reverse mapping specification with {0} field mappings for "
            "reserve pool transformation".format(len(reverse_mapping_spec)),
            "DEBUG"
        )

        return reverse_mapping_spec

    def network_management_reverse_mapping_function(self, requested_components=None):
        """
        Generate reverse mapping specification for Network Management Details transformation.

        This function creates a comprehensive mapping specification that converts
        Catalyst Center Network Management API v1 response fields into Ansible-friendly
        configuration keys compatible with the network_settings_workflow_manager module.

        Purpose:
            Transforms raw Catalyst Center network management API v1 responses into clean,
            Ansible-compatible YAML configuration format by mapping API fields to playbook
            parameters, applying type conversions, and handling nested structures.

        API Response Structure Expected (v1 format):
            {
                "siteName": "Global/USA/NYC",
                "settings": {
                    "dhcp": {"servers": ["10.0.0.1"]},
                    "dns": {
                        "domainName": "example.com",
                        "dnsServers": ["8.8.8.8", "8.8.4.4"]
                    },
                    "ntp": {"servers": ["pool.ntp.org"]},
                    "timeZone": {"identifier": "America/New_York"},
                    "banner": {"message": "Authorized Access Only"},
                    "aaaNetwork": {...},
                    "telemetry": {...}
                }
            }

        Args:
            requested_components (list, optional): Specific components to include.
                                                Reserved for future use.

        Returns:
            OrderedDict: Field mapping specification with type info and source paths.
        """
        self.log("Building reverse mapping specification to transform Catalyst Center network management "
                 "API v1 response into Ansible playbook format for network_settings_workflow_manager module",
                 "DEBUG")

        reverse_mapping_spec = OrderedDict({

            # -------------------------------
            # Site Information
            # -------------------------------
            "site_name": {
                "type": "str",
                "source_key": "siteName",
                "special_handling": True,
                "transform": self.transform_site_location
            },

            # -------------------------------
            # DHCP Server Configuration
            # -------------------------------
            # List of DHCP server IP addresses for the site
            "dhcp_server": {
                "type": "list",
                "source_key": "settings.dhcp.servers"
            },

            # -------------------------------
            # DNS Server Configuration
            # -------------------------------
            # DNS domain name for the site
            "dns_server.domain_name": {
                "type": "str",
                "source_key": "settings.dns.domainName"
            },
            # List of DNS server IP addresses
            "dns_server.dns_servers": {
                "type": "list",
                "source_key": "settings.dns.dnsServers"
            },

            # -------------------------------
            # NTP Server Configuration
            # -------------------------------
            # List of NTP server addresses for time synchronization
            "ntp_server": {
                "type": "list",
                "source_key": "settings.ntp.servers"
            },

            # -------------------------------
            # Timezone Settings
            # -------------------------------
            # Timezone identifier (e.g., "America/New_York", "UTC")
            "timezone": {
                "type": "str",
                "source_key": "settings.timeZone.identifier"
            },

            # -------------------------------
            # Message of the Day (Banner)
            # -------------------------------
            # Banner message displayed on device login
            "message_of_the_day.banner_message": {
                "type": "str",
                "source_key": "settings.banner.message"
            },
            # Whether to retain existing banner when updating
            "message_of_the_day.retain_existing_banner": {
                "type": "bool",
                "source_key": "settings.banner.retainExistingBanner"
            },

            # -------------------------------
            # Network AAA Configuration
            # -------------------------------
            # Primary AAA server IP address for network device authentication
            "network_aaa.primary_server_address": {
                "type": "str",
                "source_key": "settings.aaaNetwork.primaryServerIp"
            },
            # Secondary AAA server IP address (optional failover)
            "network_aaa.secondary_server_address": {
                "type": "str",
                "source_key": "settings.aaaNetwork.secondaryServerIp",
                "optional": True
            },
            # AAA protocol (RADIUS or TACACS)
            "network_aaa.protocol": {
                "type": "str",
                "source_key": "settings.aaaNetwork.protocol"
            },
            # Server type (AAA, ISE)
            "network_aaa.server_type": {
                "type": "str",
                "source_key": "settings.aaaNetwork.serverType"
            },
            # ISE PAN address (required when serverType is ISE)
            "network_aaa.pan_address": {
                "type": "str",
                "source_key": "settings.aaaNetwork.pan",
                "optional": True
            },
            # Shared secret for AAA server authentication
            "network_aaa.shared_secret": {
                "type": "str",
                "source_key": "settings.aaaNetwork.sharedSecret",
                "optional": True
            },

            # -----------------------------------------------
            # Client & Endpoint AAA Configuration
            # -----------------------------------------------
            # Primary AAA server IP for client/endpoint authentication
            "client_and_endpoint_aaa.primary_server_address": {
                "type": "str",
                "source_key": "settings.aaaClient.primaryServerIp"
            },
            # Secondary AAA server IP (optional failover)
            "client_and_endpoint_aaa.secondary_server_address": {
                "type": "str",
                "source_key": "settings.aaaClient.secondaryServerIp",
                "optional": True
            },
            # AAA protocol for client authentication
            "client_and_endpoint_aaa.protocol": {
                "type": "str",
                "source_key": "settings.aaaClient.protocol"
            },
            # Server type for client authentication
            "client_and_endpoint_aaa.server_type": {
                "type": "str",
                "source_key": "settings.aaaClient.serverType"
            },
            # ISE PAN address for client authentication
            "client_and_endpoint_aaa.pan_address": {
                "type": "str",
                "source_key": "settings.aaaClient.pan",
                "optional": True
            },
            # Shared secret for client AAA
            "client_and_endpoint_aaa.shared_secret": {
                "type": "str",
                "source_key": "settings.aaaClient.sharedSecret",
                "optional": True
            },

            # -------------------------------
            # NetFlow Collector (Telemetry)
            # -------------------------------
            # NetFlow collector IP address for application visibility
            "netflow_collector.ip_address": {
                "type": "str",
                "source_key": "settings.telemetry.applicationVisibility.collector.address"
            },
            # NetFlow collector port number
            "netflow_collector.port": {
                "type": "int",
                "source_key": "settings.telemetry.applicationVisibility.collector.port"
            },

            # -------------------------------
            # SNMP Server (Telemetry)
            # -------------------------------
            # Use Catalyst Center built-in SNMP trap server
            "snmp_server.configure_dnac_ip": {
                "type": "bool",
                "source_key": "settings.telemetry.snmpTraps.useBuiltinTrapServer"
            },
            # External SNMP trap server IP addresses (optional)
            "snmp_server.ip_addresses": {
                "type": "list",
                "source_key": "settings.telemetry.snmpTraps.externalTrapServers",
                "optional": True
            },

            # -------------------------------
            # Syslog Server (Telemetry)
            # -------------------------------
            # Use Catalyst Center built-in syslog server
            "syslog_server.configure_dnac_ip": {
                "type": "bool",
                "source_key": "settings.telemetry.syslogs.useBuiltinSyslogServer"
            },
            # External syslog server IP addresses (optional)
            "syslog_server.ip_addresses": {
                "type": "list",
                "source_key": "settings.telemetry.syslogs.externalSyslogServers",
                "optional": True
            },

            # -------------------------------
            # Wired Data Collection (Telemetry)
            # -------------------------------
            # Enable wired network data collection for analytics
            "wired_data_collection.enable_wired_data_collection": {
                "type": "bool",
                "source_key": "settings.telemetry.wiredDataCollection.enableWiredDataCollection"
            },
            # -------------------------------
            # Wireless Telemetry
            # -------------------------------
            # Enable wireless network telemetry collection
            "wireless_telemetry.enable_wireless_telemetry": {
                "type": "bool",
                "source_key": "settings.telemetry.wirelessTelemetry.enableWirelessTelemetry"
            }
        })

        self.log(
            "Successfully created network management reverse mapping specification with {0} field mappings".format(
                len(reverse_mapping_spec)
            ),
            "DEBUG"
        )

        return reverse_mapping_spec

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
        Retrieve all child sites under a specified site hierarchy path for reserve pool filtering.

        This method discovers all sites that exist within a hierarchical site structure,
        enabling bulk extraction of reserve pools from multiple sites using a single
        hierarchy filter. Supports both exact site matches and hierarchical traversal.

        Purpose:
            Facilitates brownfield network settings discovery by allowing users to specify
            a parent site hierarchy (e.g., "Global/USA") and automatically discovering all
            child sites underneath (e.g., "Global/USA/California", "Global/USA/New York").
            This eliminates the need to manually list every site when extracting reserve
            pool configurations from multiple related sites.

        Args:
            site_hierarchy (str): Hierarchical site path to search for child sites.
            Format: Forward-slash delimited path from Global root
            Examples:
                - "Global" (returns all sites)
                - "Global/USA" (returns USA and all child sites)
                - "Global/USA/California" (returns California and child sites)
                - "Global/EMEA/UK/London" (returns London and child sites)

        Returns:
            list: List of dictionaries containing child site information:
                [
                    {
                        "site_name": "Global/USA/California/San-Francisco",
                        "site_id": "uuid-of-sf-site"
                    },
                    {
                        "site_name": "Global/USA/California/Los-Angeles",
                        "site_id": "uuid-of-la-site"
                    }
                ]
                Returns empty list [] if:
                    - site_hierarchy is None or empty string
                    - No sites exist under the specified hierarchy
                    - Site hierarchy path is invalid/not found
                    - Site mapping retrieval fails
        """
        self.log(
            "Discovering all child sites under hierarchical path for reserve pool "
            "bulk extraction using site hierarchy filtering",
            "DEBUG"
        )
        self.log(
            "Hierarchy path to search: '{0}'".format(
                site_hierarchy if site_hierarchy else "None"
            ),
            "DEBUG"
        )

        if not site_hierarchy:
            self.log(
                "Site hierarchy path is empty or None, cannot discover child sites. "
                "Returning empty list.",
                "WARNING"
            )
            return []

        if not isinstance(site_hierarchy, str):
            self.log(
                "Invalid site_hierarchy parameter type - expected str, got {0}. "
                "Returning empty list.".format(type(site_hierarchy).__name__),
                "ERROR"
            )
            return []

        # Strip whitespace and validate non-empty after stripping
        site_hierarchy = site_hierarchy.strip()
        if not site_hierarchy:
            self.log(
                "Site hierarchy path is empty after stripping whitespace. "
                "Returning empty list.",
                "WARNING"
            )
            return []

        self.log(
            "Validated site hierarchy path: '{0}' (length: {1} characters)".format(
                site_hierarchy, len(site_hierarchy)
            ),
            "DEBUG"
        )

        child_sites = []

        # Get or create site ID to name mapping (cached for performance)
        if not hasattr(self, 'site_id_name_dict'):
            self.log(
                "Site ID-name mapping not cached, retrieving from Catalyst Center API",
                "DEBUG"
            )
            try:
                self.site_id_name_dict = self.get_site_id_name_mapping()
                self.log(
                    "Successfully retrieved site mapping with {0} total sites".format(
                        len(self.site_id_name_dict)
                    ),
                    "INFO"
                )
            except Exception as e:
                self.log(
                    "Failed to retrieve site ID-name mapping: {0}. "
                    "Cannot discover child sites, returning empty list.".format(str(e)),
                    "ERROR"
                )
                return []
        else:
            self.log(
                "Using cached site ID-name mapping with {0} sites (cache hit)".format(
                    len(self.site_id_name_dict)
                ),
                "DEBUG"
            )

        # Validate site mapping is not empty
        if not self.site_id_name_dict:
            self.log(
                "Site ID-name mapping is empty, no sites available in Catalyst Center. "
                "Returning empty list.",
                "WARNING"
            )
            return []

        # Create reverse mapping (name to ID)
        site_name_to_id = {v: k for k, v in self.site_id_name_dict.items()}

        # Validate that the hierarchy path exists in the site mapping
        if site_hierarchy not in site_name_to_id:
            self.log(
                "Site hierarchy path '{0}' not found in Catalyst Center site mapping. "
                "This may be an invalid path or the site does not exist. Available top-level "
                "sites: {1}".format(
                    site_hierarchy,
                    [name for name in site_name_to_id.keys() if name.count('/') <= 1][:5]
                ),
                "WARNING"
            )
            # Don't return empty - continue to check for child sites that might match

        self.log(
            "Searching through {0} total sites for matches under hierarchy '{1}'".format(
                len(self.site_id_name_dict), site_hierarchy
            ),
            "DEBUG"
        )

        # Track matching statistics
        exact_match_found = False
        child_matches_found = 0

        # Iterate through all sites to find matches
        for site_id, site_name in self.site_id_name_dict.items():
            # Check if this site is under the specified hierarchy
            # Two cases to match:
            # 1. Exact match: site_name == site_hierarchy (include the parent itself)
            # 2. Child match: site_name starts with site_hierarchy + "/"

            is_exact_match = (site_name == site_hierarchy)
            is_child_match = site_name.startswith(site_hierarchy + "/")

            if is_exact_match:
                exact_match_found = True
                child_sites.append({
                    "site_name": site_name,
                    "site_id": site_id
                })
                self.log(
                    "Found exact match for hierarchy path: '{0}' (ID: {1})".format(
                        site_name, site_id
                    ),
                    "DEBUG"
                )
            elif is_child_match:
                child_matches_found += 1
                child_sites.append({
                    "site_name": site_name,
                    "site_id": site_id
                })
                self.log(
                    "Found child site {0}: '{1}' (ID: {2})".format(
                        child_matches_found, site_name, site_id
                    ),
                    "DEBUG"
                )

        if not child_sites:
            self.log(
                "No child sites found under hierarchy: '{0}'. This hierarchy path may not "
                "exist or may not have any child sites configured.".format(site_hierarchy),
                "WARNING"
            )
        else:
            self.log(
                "Successfully discovered {0} total site(s) under hierarchy '{1}': "
                "exact_match={2}, child_matches={3}".format(
                    len(child_sites),
                    site_hierarchy,
                    "yes" if exact_match_found else "no",
                    child_matches_found
                ),
                "INFO"
            )

        self.log(
            "Completed child site discovery for hierarchy '{0}': found {1} site(s) "
            "(including parent and all descendants)".format(
                site_hierarchy, len(child_sites)
            ),
            "DEBUG"
        )

        return child_sites

    def transform_site_location(self, site_name_or_pool_details):
        """
        Transform site location information to hierarchical site name format for brownfield configurations.

        Purpose:
            Normalizes diverse site identifier formats from Catalyst Center API responses
            into standardized hierarchical site names suitable for Ansible YAML configuration.
            Supports brownfield network settings discovery by providing reliable site
            location mapping across different API response structures.

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

        # =====================================
        # String Input (Already Site Name)
        # =====================================
        if isinstance(site_name_or_pool_details, str):
            # Validate string is not empty or whitespace-only
            site_name = site_name_or_pool_details.strip()

            if not site_name:
                self.log(
                    "Site location string is empty or whitespace-only after stripping. "
                    "Returning None.",
                    "WARNING"
                )
                return None

            # Validate hierarchical format (should contain '/' for proper hierarchy)
            if "/" not in site_name:
                self.log(
                    "Site name '{0}' does not contain hierarchy delimiter '/'. "
                    "This may be a short name without full hierarchy. "
                    "Consider using site ID lookup for complete path.".format(site_name),
                    "WARNING"
                )

            self.log(
                "Input is string type (hierarchical site name), returning as-is: '{0}'".format(
                    site_name
                ),
                "DEBUG"
            )
            return site_name

        # =====================================
        # Case 3: Dictionary Input (Pool/Config Details)
        # =====================================
        if isinstance(site_name_or_pool_details, dict):
            self.log(
                "Input is dict type (pool/configuration details), extracting site information "
                "using priority: 1) siteId lookup, 2) siteName field",
                "DEBUG"
            )

            # Extract both site ID and site name from dict
            site_id = site_name_or_pool_details.get("siteId")
            site_name = site_name_or_pool_details.get("siteName")

            self.log(
                "Extracted from dict - siteId: {0}, siteName: {1}".format(
                    site_id if site_id else "None",
                    site_name if site_name else "None"
                ),
                "DEBUG"
            )

            # Priority 1: Site ID Lookup (Most Reliable for Full Hierarchy)
            if site_id:
                self.log(
                    "Site ID found: {0}, performing lookup to resolve full hierarchical path".format(
                        site_id
                    ),
                    "DEBUG"
                )

                # Ensure site mapping is available
                if not hasattr(self, 'site_id_name_dict'):
                    self.log(
                        "Site ID-to-name mapping not cached, creating mapping via API call",
                        "DEBUG"
                    )

                    try:
                        self.site_id_name_dict = self.get_site_id_name_mapping()
                        self.log(
                            "Successfully created site mapping with {0} total sites".format(
                                len(self.site_id_name_dict)
                            ),
                            "INFO"
                        )
                    except Exception as e:
                        self.log(
                            "Failed to create site ID-to-name mapping: {0}. "
                            "Cannot perform site ID lookup, falling back to siteName.".format(
                                str(e)
                            ),
                            "ERROR"
                        )
                        # Fall through to siteName handling below
                        self.site_id_name_dict = {}
                else:
                    self.log(
                        "Using cached site ID-to-name mapping with {0} sites (cache hit)".format(
                            len(self.site_id_name_dict)
                        ),
                        "DEBUG"
                    )

                # Perform site ID lookup
                site_name_hierarchy = self.site_id_name_dict.get(site_id)

                if site_name_hierarchy:
                    self.log(
                        "Successfully mapped site ID {0} to full hierarchical path: '{1}'".format(
                            site_id, site_name_hierarchy
                        ),
                        "INFO"
                    )
                    return site_name_hierarchy
                else:
                    self.log(
                        "Site ID {0} not found in mapping (total sites: {1}). "
                        "This may indicate an invalid site ID or mapping synchronization issue. "
                        "Falling back to siteName field: '{2}'".format(
                            site_id,
                            len(self.site_id_name_dict) if self.site_id_name_dict else 0,
                            site_name if site_name else "None"
                        ),
                        "WARNING"
                    )
                    # Fall through to siteName handling below

            # Priority 2: Site Name Fallback (When ID Lookup Fails or Unavailable)
            if site_name:
                # Validate site name is not empty after stripping
                site_name_stripped = site_name.strip()

                if not site_name_stripped:
                    self.log(
                        "siteName field is empty or whitespace-only after stripping. "
                        "Cannot determine site location. Returning None.",
                        "WARNING"
                    )
                    return None

                # Warn if siteName doesn't contain full hierarchy
                if "/" not in site_name_stripped:
                    self.log(
                        "siteName '{0}' appears to be a short name without full hierarchy "
                        "(no '/' delimiter). Using as-is but this may result in incomplete "
                        "site path in YAML output.".format(site_name_stripped),
                        "WARNING"
                    )

                self.log(
                    "Using siteName from dict as fallback (siteId lookup unavailable or failed): '{0}'".format(
                        site_name_stripped
                    ),
                    "DEBUG"
                )
                return site_name_stripped

            # Neither siteId nor siteName available
            self.log(
                "Dict input contains neither valid siteId nor siteName field. "
                "Available keys in dict: {0}. Cannot determine site location.".format(
                    list(site_name_or_pool_details.keys())
                ),
                "WARNING"
            )
            return None

        # =====================================
        # Case 4: Invalid Input Type
        # =====================================
        self.log(
            "Invalid input type for site location transformation - expected str, dict, or None, "
            "but received {0}. Cannot process site location. Returning None.".format(
                site_name_or_pool_details
            ),
            "ERROR"
        )

        # Exit log with failure status
        self.log(
            "Site location transformation failed - unable to extract hierarchical site name "
            "from input of type {0}".format(site_name_or_pool_details),
            "WARNING"
        )

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
        self.log(
            "Resetting operation tracking variables to prepare clean state for new "
            "brownfield network settings discovery operation",
            "DEBUG"
        )

        self.log(
            "Current state before reset - Successes: {0}, Failures: {1}, "
            "Sites processed: {2}, Components processed: {3}".format(
                len(self.operation_successes) if hasattr(self, 'operation_successes') else 0,
                len(self.operation_failures) if hasattr(self, 'operation_failures') else 0,
                self.total_sites_processed if hasattr(self, 'total_sites_processed') else 0,
                self.total_components_processed if hasattr(self, 'total_components_processed') else 0
            ),
            "DEBUG"
        )

        # Reset success tracking
        if hasattr(self, 'operation_successes'):
            previous_success_count = len(self.operation_successes)
            self.operation_successes = []
            self.log(
                "Cleared operation_successes list: removed {0} previous success entries".format(
                    previous_success_count
                ),
                "DEBUG"
            )
        else:
            self.operation_successes = []
            self.log(
                "Initialized operation_successes list (first-time initialization)",
                "DEBUG"
            )

        # Reset failure tracking
        if hasattr(self, 'operation_failures'):
            previous_failure_count = len(self.operation_failures)
            self.operation_failures = []
            self.log(
                "Cleared operation_failures list: removed {0} previous failure entries".format(
                    previous_failure_count
                ),
                "DEBUG"
            )
        else:
            self.operation_failures = []
            self.log(
                "Initialized operation_failures list (first-time initialization)",
                "DEBUG"
            )

        # Reset site counter
        if hasattr(self, 'total_sites_processed'):
            previous_site_count = self.total_sites_processed
            self.total_sites_processed = 0
            self.log(
                "Reset total_sites_processed counter from {0} to 0".format(
                    previous_site_count
                ),
                "DEBUG"
            )
        else:
            self.total_sites_processed = 0
            self.log(
                "Initialized total_sites_processed counter to 0 (first-time initialization)",
                "DEBUG"
            )

        # Reset component counter
        if hasattr(self, 'total_components_processed'):
            previous_component_count = self.total_components_processed
            self.total_components_processed = 0
            self.log(
                "Reset total_components_processed counter from {0} to 0".format(
                    previous_component_count
                ),
                "DEBUG"
            )
        else:
            self.total_components_processed = 0
            self.log(
                "Initialized total_components_processed counter to 0 (first-time initialization)",
                "DEBUG"
            )

        # Verify reset was successful
        verification_passed = (
            len(self.operation_successes) == 0 and
            len(self.operation_failures) == 0 and
            self.total_sites_processed == 0 and
            self.total_components_processed == 0
        )

        if verification_passed:
            self.log(
                "Operation tracking reset verification PASSED: All counters and lists "
                "successfully cleared and ready for new operation",
                "INFO"
            )
        else:
            # Log warning if verification failed (should never happen)
            self.log(
                "Operation tracking reset verification FAILED: Some variables may not have "
                "reset properly. Current state - Successes: {0}, Failures: {1}, "
                "Sites: {2}, Components: {3}".format(
                    len(self.operation_successes),
                    len(self.operation_failures),
                    self.total_sites_processed,
                    self.total_components_processed
                ),
                "WARNING"
            )

        self.log(
            "Successfully reset all operation tracking variables - module is ready to track "
            "new brownfield discovery operation with clean state",
            "DEBUG"
        )

    def add_success(self, site_name, component, additional_info=None):
        """
        Record a successful operation for site/component processing in operation tracking.

        This method adds a successful operation entry to the tracking system, recording
        which site and component were successfully processed during brownfield network
        settings extraction. Used for generating comprehensive operation summaries.

        Args:
            site_name (str): Full hierarchical site name that was successfully processed.
            Examples:
                - "Global" (root site for global pool operations)
                - "Global/USA/California/SanFrancisco" (full hierarchy path)
                - "Global/EMEA/UK/London/Building1" (building-level site)
            Must be non-empty string with valid site hierarchy format.

        component (str): Network settings component that was successfully processed.
            Valid component names (from network_elements schema):
                - "global_pool_details": Global IP pool configurations
                - "reserve_pool_details": Reserve IP pool configurations
                - "network_management_details": Network management settings
                - "device_controllability_details": Device controllability settings
            Must match supported component names from module schema.

        additional_info (dict, optional): Supplementary information about the success.
            Common fields:
                - pools_processed (int): Number of pools successfully extracted
                - settings_extracted (list): List of settings types retrieved
                - processing_time (float): Seconds taken for processing
                - optimization (str): Optimization technique used (e.g., "bulk_retrieval")
                - record_count (int): Total records processed
                - api_calls_made (int): Number of API calls executed
            Can include any custom metrics relevant to the operation.
            None is acceptable when no additional context is needed.
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
            Examples:
            - "Global" (root site for global operations)
                - "Global/USA/California/SanFrancisco" (full hierarchy path)
                - "Global/EMEA/UK/London/Building1" (building-level site)
            Must be non-empty string with valid site hierarchy format.

        component (str): Network settings component that failed processing.
            Valid component names (from network_elements schema):
                - "global_pool_details": Global IP pool configurations
                - "reserve_pool_details": Reserve IP pool configurations
                - "network_management_details": Network management settings
                - "device_controllability_details": Device controllability settings
            Must match supported component names from module schema.

        error_info (dict): Detailed error information for troubleshooting containing:
            Required fields:
                - error_message (str): Human-readable error description
            Optional fields (for enhanced diagnostics):
                - error_type (str): Error category (api_error, validation_error, etc.)
                - error_code (str): Specific error code (SITE_NOT_FOUND, API_TIMEOUT, etc.)
                - api_response (dict): Raw API error response for debugging
                - status_code (int): HTTP status code if applicable
                - stack_trace (str): Exception stack trace for critical errors
                - retry_attempted (bool): Whether operation retry was attempted
                - retry_count (int): Number of retry attempts made
                - timestamp (str): ISO timestamp when error occurred
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
            dict: Comprehensive operation summary containing:
                - total_sites_processed (int): Total unique sites processed in operation
                - total_components_processed (int): Total network components processed
                - total_successful_operations (int): Count of successful site/component operations
                - total_failed_operations (int): Count of failed site/component operations
                - sites_with_complete_success (list): Sites with 100% success rate (all components succeeded)
                - sites_with_partial_success (list): Sites with mixed results (some successes, some failures)
                - sites_with_complete_failure (list): Sites with 0% success rate (all components failed)
                - success_details (list): Complete list of successful operation entries with metadata
                - failure_details (list): Complete list of failed operation entries with error information
        """
        self.log(
            "Generating comprehensive operation summary by analyzing tracked successes "
            "and failures to categorize sites and calculate statistics",
            "DEBUG"
        )

        success_count = len(self.operation_successes) if hasattr(self, 'operation_successes') else 0
        failure_count = len(self.operation_failures) if hasattr(self, 'operation_failures') else 0

        self.log(
            "Operation tracking state - Total successes: {0}, Total failures: {1}".format(
                success_count, failure_count
            ),
            "DEBUG"
        )

        unique_successful_sites = set()
        unique_failed_sites = set()

        if not hasattr(self, 'operation_successes'):
            self.log(
                "operation_successes list not initialized, creating empty list. "
                "This indicates no successful operations were recorded.",
                "WARNING"
            )
            self.operation_successes = []

        if not hasattr(self, 'operation_failures'):
            self.log(
                "operation_failures list not initialized, creating empty list. "
                "This indicates no failed operations were recorded.",
                "WARNING"
            )
            self.operation_failures = []

        self.log(
            "Processing {0} successful operation entries to extract unique site identifiers".format(
                len(self.operation_successes)
            ),
            "DEBUG"
        )

        self.log("Processing successful operations to extract unique site information", "DEBUG")
        for index, success in enumerate(self.operation_successes, start=1):
            # Validate success entry structure
            if not isinstance(success, dict):
                self.log(
                    "Success entry {0} is not a dict (type: {1}), skipping site extraction".format(
                        index, type(success).__name__
                    ),
                    "WARNING"
                )
                continue

            # Extract site name with fallback to "Global"
            site_name = success.get("site_name")

            if not site_name:
                self.log(
                    "Success entry {0} missing site_name field, using 'Global' as fallback".format(
                        index
                    ),
                    "DEBUG"
                )
                site_name = "Global"

            # Validate site_name is a string
            if not isinstance(site_name, str):
                self.log(
                    "Success entry {0} has non-string site_name (type: {1}), "
                    "converting to string".format(index, type(site_name).__name__),
                    "WARNING"
                )
                site_name = str(site_name)

            # Add to successful sites set
            unique_successful_sites.add(site_name)

            self.log(
                "Processed success entry {0}/{1}: site='{2}', component='{3}'".format(
                    index, len(self.operation_successes), site_name,
                    success.get("component", "Unknown")
                ),
                "DEBUG"
            )

        self.log(
            "Extracted {0} unique sites from successful operations: {1}".format(
                len(unique_successful_sites), list(unique_successful_sites)
            ),
            "DEBUG"
        )

        # Process failed operations to extract unique sites
        self.log(
            "Processing {0} failed operation entries to extract unique site identifiers".format(
                len(self.operation_failures)
            ),
            "DEBUG"
        )

        for index, failure in enumerate(self.operation_failures, start=1):
            # Validate failure entry structure
            if not isinstance(failure, dict):
                self.log(
                    "Failure entry {0} is not a dict (type: {1}), skipping site extraction".format(
                        index, type(failure).__name__
                    ),
                    "WARNING"
                )
                continue

            # Extract site name with fallback to "Global"
            site_name = failure.get("site_name")

            if not site_name:
                self.log(
                    "Failure entry {0} missing site_name field, using 'Global' as fallback".format(
                        index
                    ),
                    "DEBUG"
                )
                site_name = "Global"

            # Validate site_name is a string
            if not isinstance(site_name, str):
                self.log(
                    "Failure entry {0} has non-string site_name (type: {1}), "
                    "converting to string".format(index, type(site_name).__name__),
                    "WARNING"
                )
                site_name = str(site_name)

            # Add to failed sites set
            unique_failed_sites.add(site_name)

            # Log failure details for troubleshooting
            error_info = failure.get("error_info", {})
            error_message = error_info.get("error_message", "Unknown error") if isinstance(error_info, dict) else str(error_info)

            self.log(
                "Processed failure entry {0}/{1}: site='{2}', component='{3}', error='{4}'".format(
                    index, len(self.operation_failures), site_name,
                    failure.get("component", "Unknown"), error_message[:50]
                ),
                "DEBUG"
            )

        self.log(
            "Extracted {0} unique sites from failed operations: {1}".format(
                len(unique_failed_sites), list(unique_failed_sites)
            ),
            "DEBUG"
        )

        self.log("Calculating site categorization based on success and failure patterns "
                 "using set intersection and difference operations",
                 "DEBUG")
        partial_success_sites = unique_successful_sites.intersection(unique_failed_sites)
        self.log("Sites with partial success (both successes and failures): {0} site(s) - {1}".format(
                 len(partial_success_sites), list(partial_success_sites)), "DEBUG")

        complete_success_sites = unique_successful_sites - unique_failed_sites
        self.log("Sites with complete success (only successes, no failures): {0} site(s) - {1}".format(
            len(complete_success_sites), list(complete_success_sites)), "DEBUG")

        complete_failure_sites = unique_failed_sites - unique_successful_sites
        self.log("Sites with complete failure (only failures, no successes): {0} site(s) - {1}".format(
            len(complete_failure_sites), list(complete_failure_sites)), "DEBUG")

        # Calculate total unique sites processed
        total_sites = len(unique_successful_sites.union(unique_failed_sites))

        self.log(
            "Total unique sites processed across all operations: {0}".format(total_sites),
            "INFO"
        )

        # Validate total_components_processed tracking variable
        if not hasattr(self, 'total_components_processed'):
            self.log(
                "total_components_processed not initialized, defaulting to 0. "
                "This may indicate tracking was not properly initialized.",
                "WARNING"
            )
            self.total_components_processed = 0

        summary = {
            "total_sites_processed": total_sites,
            "total_components_processed": self.total_components_processed,
            "total_successful_operations": len(self.operation_successes),
            "total_failed_operations": len(self.operation_failures),
            "sites_with_complete_success": sorted(list(complete_success_sites)),
            "sites_with_partial_success": sorted(list(partial_success_sites)),
            "sites_with_complete_failure": sorted(list(complete_failure_sites)),
            "success_details": self.operation_successes,
            "failure_details": self.operation_failures
        }

        # Calculate and log success rate
        total_operations = summary["total_successful_operations"] + summary["total_failed_operations"]
        success_rate = (summary["total_successful_operations"] / total_operations * 100) if total_operations > 0 else 0.0

        self.log(
            "Overall operation success rate: {0:.1f}% ({1}/{2} operations succeeded)".format(
                success_rate, summary["total_successful_operations"], total_operations
            ),
            "INFO"
        )

        # Log summary statistics
        self.log(
            "Operation summary statistics - Sites: {0} total ({1} complete success, "
            "{2} partial success, {3} complete failure), Components: {4}, "
            "Success rate: {5:.1f}%".format(
                summary["total_sites_processed"],
                len(summary["sites_with_complete_success"]),
                len(summary["sites_with_partial_success"]),
                len(summary["sites_with_complete_failure"]),
                summary["total_components_processed"],
                success_rate
            ),
            "INFO"
        )

        # Log warnings for sites requiring attention
        if summary["sites_with_complete_failure"]:
            self.log(
                "ATTENTION REQUIRED: {0} site(s) with complete failure need investigation: {1}".format(
                    len(summary["sites_with_complete_failure"]),
                    summary["sites_with_complete_failure"]
                ),
                "WARNING"
            )

        if summary["sites_with_partial_success"]:
            self.log(
                "REVIEW RECOMMENDED: {0} site(s) with partial success may need manual review: {1}".format(
                    len(summary["sites_with_partial_success"]),
                    summary["sites_with_partial_success"]
                ),
                "INFO"
            )

        self.log(
            "Successfully generated operation summary with {0} total sites processed, "
            "{1} successful operations, {2} failed operations".format(
                summary["total_sites_processed"],
                summary["total_successful_operations"],
                summary["total_failed_operations"]
            ),
            "DEBUG"
        )

        return summary

    def get_global_pools(self, network_element, filters):
        """
        Retrieve global IP pools from Catalyst Center with comprehensive filtering support.

        This method orchestrates the complete workflow for extracting global IP pool configurations
        from Catalyst Center, applying multi-level filters (global and component-specific), and
        transforming the results into Ansible-compatible YAML format.
        Args:
            network_element (dict): Network element specification containing:
                - api_family (str): API family name (e.g., 'network_settings')
                - api_function (str): API function name (e.g., 'retrieves_global_ip_address_pools')
                - reverse_mapping_function (callable): Function to generate reverse mapping spec

            filters (dict): Multi-level filtering configuration:
                - global_filters (dict): Top-level filters applied across all components:
                    * pool_name_list (list[str]): Filter by specific pool names
                    * pool_type_list (list[str]): Filter by pool types (Generic, LAN, WAN)
                - component_specific_filters (dict): Component-level filters:
                    * global_pool_details (list[dict]): List of filter criteria:
                        - pool_name (str): Exact pool name match
                        - pool_type (str): Pool type match (Generic, LAN, WAN)
        Returns:
            dict: A dictionary containing the modified details of global pools.
        """
        self.log(
            "Input parameters - API family: '{0}', API function: '{1}', "
            "Global filters: {2}, Component filters: {3}".format(
                network_element.get("api_family"),
                network_element.get("api_function"),
                filters.get("global_filters", {}),
                filters.get("component_specific_filters", {})
            ),
            "DEBUG"
        )

        final_global_pools = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            error_msg = (
                "Invalid network_element configuration - missing required fields. "
                "Expected 'api_family' and 'api_function', got: {0}".format(
                    list(network_element.keys())
                )
            )
            self.log(error_msg, "ERROR")
            self.add_failure("Global", "global_pool_details", {
                "error_type": "configuration_error",
                "error_message": error_msg,
                "error_code": "INVALID_NETWORK_ELEMENT"
            })
            return {
                "global_pool_details": {},
                "operation_summary": self.get_operation_summary()
            }

        self.log("Getting global pools using family '{0}' and function '{1}'.".format(
            api_family, api_function), "INFO")

        # Get global filters
        global_filters = filters.get("global_filters", {})
        component_specific_filters = filters.get("component_specific_filters", {}).get("global_pool_details", [])
        self.log(
            "Filter configuration - Global filters: {0}, Component-specific filters: {1}".format(
                global_filters, component_specific_filters
            ),
            "DEBUG"
        )

        try:
            # Execute bulk API call to get all global pools at once
            # Note: Global pool APIs don't support filter parameters, so we retrieve all and filter locally
            self.log(
                "Executing bulk API call to retrieve all global IP pools from Catalyst Center "
                "(no site-specific filtering at API level)",
                "INFO"
            )
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

            pool_name_list = global_filters.get("pool_name_list", [])
            pool_type_list = global_filters.get("pool_type_list", [])

            if pool_name_list or pool_type_list:
                self.log(
                    "Applying global filters - pool_name_list: {0}, pool_type_list: {1}".format(
                        pool_name_list, pool_type_list
                    ),
                    "INFO"
                )

                filtered_pools = []
                pools_filtered_by_name = 0
                pools_filtered_by_type = 0

                for pool in all_global_pools:
                    pool_name = pool.get("name")
                    pool_type = pool.get("poolType")

                    # Check pool name filter (OR logic within list)
                    if pool_name_list and pool_name not in pool_name_list:
                        pools_filtered_by_name += 1
                        self.log(
                            "Pool '{0}' filtered out - name not in filter list: {1}".format(
                                pool_name, pool_name_list
                            ),
                            "DEBUG"
                        )
                        continue

                    # Check pool type filter (OR logic within list)
                    if pool_type_list and pool_type not in pool_type_list:
                        pools_filtered_by_type += 1
                        self.log(
                            "Pool '{0}' (type: '{1}') filtered out - type not in filter list: {2}".format(
                                pool_name, pool_type, pool_type_list
                            ),
                            "DEBUG"
                        )
                        continue

                    # Pool passed all global filters
                    filtered_pools.append(pool)
                    self.log(
                        "Pool '{0}' (type: '{1}') passed global filters".format(
                            pool_name, pool_type
                        ),
                        "DEBUG"
                    )

                self.log(
                    "Global filter results - Started: {0} pools, Filtered by name: {1}, "
                    "Filtered by type: {2}, Remaining: {3}".format(
                        len(all_global_pools),
                        pools_filtered_by_name,
                        pools_filtered_by_type,
                        len(filtered_pools)
                    ),
                    "INFO"
                )

            # Apply component-specific filters
            if component_specific_filters:
                self.log("Applying component-specific filters with AND logic across {0} filter "
                         "criteria".format(len(component_specific_filters)),
                         "INFO")

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

                final_filtered_pools = []
                pools_filtered_by_component = 0

                for pool in filtered_pools:
                    pool_name = pool.get("name")
                    pool_type = pool.get("poolType")
                    matches_all_criteria = True

                    # Check name criteria (pool must match at least one name if specified)
                    if all_pool_name_filters:
                        if pool_name not in all_pool_name_filters:
                            matches_all_criteria = False
                            pools_filtered_by_component += 1
                            self.log(
                                "Pool '{0}' does not match component name filter: {1}".format(
                                    pool_name, all_pool_name_filters
                                ),
                                "DEBUG"
                            )

                    # Check type criteria (pool must match at least one type if specified)
                    if all_pool_type_filters and matches_all_criteria:
                        if pool_type not in all_pool_type_filters:
                            matches_all_criteria = False
                            pools_filtered_by_component += 1
                            self.log(
                                "Pool '{0}' (type: '{1}') does not match component type "
                                "filter: {2}".format(
                                    pool_name, pool_type, all_pool_type_filters
                                ),
                                "DEBUG"
                            )

                    # Additional AND logic: if both name and type filters exist,
                    # pool must satisfy both criteria
                    if matches_all_criteria and all_pool_name_filters and all_pool_type_filters:
                        name_match = pool_name in all_pool_name_filters
                        type_match = pool_type in all_pool_type_filters

                        if not (name_match and type_match):
                            matches_all_criteria = False
                            pools_filtered_by_component += 1
                            self.log(
                                "Pool '{0}' (type: '{1}') does not satisfy both name AND "
                                "type criteria".format(pool_name, pool_type),
                                "DEBUG"
                            )

                    if matches_all_criteria:
                        final_filtered_pools.append(pool)
                        self.log(
                            "Pool '{0}' (type: '{1}') matched ALL component-specific filter "
                            "criteria".format(pool_name, pool_type),
                            "INFO"
                        )

                final_global_pools = final_filtered_pools

                self.log(
                    "Component filter results - Started: {0} pools, Filtered out: {1}, "
                    "Final remaining: {2}".format(
                        len(filtered_pools),
                        pools_filtered_by_component,
                        len(final_global_pools)
                    ),
                    "INFO"
                )

                final_global_pools = final_filtered_pools
                self.log("Applied component-specific filters with AND logic, final pools: {0}".format(len(final_global_pools)), "DEBUG")
            else:
                self.log(
                    "No component-specific filters specified - using {0} pools from "
                    "global filter stage".format(len(filtered_pools)),
                    "DEBUG"
                )
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
        self.log(
            "Applying reverse mapping transformation to convert {0} global pools "
            "from Catalyst Center format to Ansible playbook format".format(
                len(final_global_pools)
            ),
            "INFO"
        )
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        if not reverse_mapping_function or not callable(reverse_mapping_function):
            error_msg = (
                "Invalid reverse_mapping_function - expected callable, got {0}".format(
                    type(reverse_mapping_function).__name__
                )
            )
            self.log(error_msg, "ERROR")
            self.add_failure("Global", "global_pool_details", {
                "error_type": "configuration_error",
                "error_message": error_msg,
                "error_code": "INVALID_REVERSE_MAPPING_FUNCTION"
            })
            return {
                "global_pool_details": {},
                "operation_summary": self.get_operation_summary()
            }
        reverse_mapping_spec = reverse_mapping_function()

        # Transform using inherited modify_parameters function (with OrderedDict spec)
        pools_details = self.modify_parameters(reverse_mapping_spec, final_global_pools)
        self.log(
            "Reverse mapping transformation completed successfully - generated {0} "
            "Ansible-compatible pool configurations".format(len(pools_details)),
            "INFO"
        )

        self.log(
            "Global pool retrieval completed - Retrieved: {0} total pools, "
            "Filtered: {1} pools remaining, Transformed: {2} configurations generated".format(
                len(all_global_pools) if 'all_global_pools' in locals() else 0,
                len(final_global_pools),
                len(pools_details)
            ),
            "DEBUG"
        )

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
        Retrieve comprehensive network management settings for targeted sites.

        This method orchestrates the collection of all network management configuration
        components (DHCP, DNS, NTP, AAA, telemetry, etc.) from Catalyst Center for
        specified sites, applies unified reverse mapping transformation, and returns
        Ansible-compatible configuration format.

        Purpose:
            Provides centralized network management settings retrieval with site-based
            filtering, component aggregation, and transformation for brownfield network
            discovery workflows.

        Workflow:
            1. Determine target sites from global and component-specific filters
            2. Build site ID-to-name mapping for lookups
            3. For each target site:
            a. Retrieve AAA settings (network + client)
            b. Retrieve DHCP server configuration
            c. Retrieve DNS server settings
            d. Retrieve telemetry settings (NetFlow, SNMP, Syslog)
            e. Retrieve NTP server configuration
            f. Retrieve timezone settings
            g. Retrieve banner (message of the day) settings
            4. Apply unified reverse mapping to normalize data structure
            5. Track success/failure for each site
            6. Return consolidated results with operation summary

        Args:
            network_element (dict): Network element specification containing:
                - api_family (str): API family name (e.g., 'network_settings')
                - api_function (str): API function name (e.g., 'get_network_v2')
                - reverse_mapping_function (callable): Reverse mapping spec generator

            filters (dict): Multi-level filtering configuration:
                - global_filters (dict): Top-level filters:
                    * site_name_list (list[str]): Specific sites to target
                - component_specific_filters (dict): Component-level filters:
                    * network_management_details (list[dict]): Filter criteria:
                        - site_name_list (list[str]): Site names
                        - site_name (str): Individual site name
        Returns:
            dict: Structured response containing:
                {
                    "network_management_details": [
                        {
                            "site_name": "Global/USA/NYC",
                            "settings": {
                                "network_aaa": {...},
                                "client_and_endpoint_aaa": {...},
                                "dhcp_server": [...],
                                "dns_server": {...},
                                "ntp_server": [...],
                                "timezone": "America/New_York",
                                "message_of_the_day": {...},
                                "netflow_collector": {...},
                                "snmp_server": {...},
                                "syslog_server": {...}
                            }
                        }
                    ],
                    "operation_summary": {
                        "total_sites_processed": 2,
                        "total_successful_operations": 2,
                        ...
                    }
                }
        """

        self.log(
            "Starting network management settings retrieval for brownfield discovery "
            "with site-based filtering and component aggregation",
            "DEBUG"
        )

        self.log(
            "Input parameters - API family: '{0}', API function: '{1}', "
            "Global filters: {2}, Component filters: {3}".format(
                network_element.get("api_family"),
                network_element.get("api_function"),
                filters.get("global_filters", {}),
                filters.get("component_specific_filters", {})
            ),
            "DEBUG"
        )

        # =====================================
        # Step 1: Determine Target Sites
        # =====================================
        self.log(
            "Determining target sites using filter priority: "
            "1) Component-specific filters, 2) Global filters, 3) Default to Global site",
            "DEBUG"
        )

        global_filters = filters.get("global_filters", {})
        component_specific_filters = filters.get("component_specific_filters", {}).get(
            "network_management_details", []
        )

        if not isinstance(global_filters, dict):
            self.log(
                "Invalid global_filters type - expected dict, got {0}. "
                "Ignoring global filters.".format(type(global_filters).__name__),
                "WARNING"
            )
            global_filters = {}

        if not isinstance(component_specific_filters, list):
            self.log(
                "Invalid component_specific_filters type - expected list, got {0}. "
                "Ignoring component filters.".format(type(component_specific_filters).__name__),
                "WARNING"
            )
            component_specific_filters = []

        # Extract site_name_list from component specific filters
        site_name_list = []
        if component_specific_filters:
            self.log(
                "Processing {0} component-specific filter criteria".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
            for filter_param in component_specific_filters:
                if "site_name_list" in filter_param:
                    extracted_sites = filter_param["site_name_list"]
                    if isinstance(extracted_sites, list):
                        site_name_list.extend(extracted_sites)
                        self.log(
                            "Extracted {0} sites from site_name_list filter".format(
                                len(extracted_sites)
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "Invalid site_name_list type in component filter - expected list, got {0}".format(
                                type(extracted_sites).__name__
                            ),
                            "WARNING"
                        )
                elif "site_name" in filter_param:
                    site_name = filter_param["site_name"]
                    if isinstance(site_name, str):
                        site_name_list.append(site_name)
                        self.log(
                            "Extracted individual site_name: '{0}'".format(site_name),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "Invalid site_name type in component filter - expected str, got {0}".format(
                                type(site_name).__name__
                            ),
                            "WARNING"
                        )

        # If no component specific filters, check global filters
        if not site_name_list:
            global_site_list = global_filters.get("site_name_list", [])
            if isinstance(global_site_list, list):
                site_name_list = global_site_list
                self.log(
                    "Using global site_name_list filter with {0} sites".format(
                        len(site_name_list)
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "Invalid global site_name_list type - expected list, got {0}".format(
                        type(global_site_list).__name__
                    ),
                    "WARNING"
                )

        self.log(
            "Total sites specified in filters: {0}".format(len(site_name_list)),
            "INFO"
        )
        target_sites = []

        # =====================================
        # Step 2: Build Site Mapping
        # =====================================
        self.log(
            "Building or retrieving site ID-to-name mapping for site lookups",
            "DEBUG"
        )

        # Build site mapping only once (cached)
        if not hasattr(self, "site_id_name_dict"):
            self.log(
                "Site mapping not cached, retrieving from Catalyst Center API",
                "DEBUG"
            )
            try:
                self.site_id_name_dict = self.get_site_id_name_mapping()
                self.log(
                    "Successfully retrieved site mapping with {0} total sites".format(
                        len(self.site_id_name_dict)
                    ),
                    "INFO"
                )
            except Exception as e:
                self.log(
                    "Failed to retrieve site mapping: {0}. Cannot process sites.".format(
                        str(e)
                    ),
                    "ERROR"
                )
                self.add_failure("All Sites", "network_management_details", {
                    "error_type": "site_mapping_error",
                    "error_message": "Failed to retrieve site mapping",
                    "error_code": "SITE_MAPPING_FAILED"
                })
                return {
                    "network_management_details": [],
                    "operation_summary": self.get_operation_summary()
                }
        else:
            self.log(
                "Using cached site mapping with {0} sites (cache hit)".format(
                    len(self.site_id_name_dict)
                ),
                "DEBUG"
            )

        # Reverse-map: name → ID
        site_name_to_id = {v: k for k, v in self.site_id_name_dict.items()}

        # =====================================
        # Step 3: Determine Target Sites List
        # =====================================
        target_sites = []

        if site_name_list:
            # Specific sites requested
            self.log(
                "Processing {0} specific site names from filters".format(
                    len(site_name_list)
                ),
                "INFO"
            )
            for site_name in site_name_list:
                # Validate site name format
                if not site_name or not isinstance(site_name, str):
                    self.log(
                        "Invalid site name format: {0} (type: {1}), skipping".format(
                            site_name, type(site_name).__name__
                        ),
                        "WARNING"
                    )
                    continue

                site_id = site_name_to_id.get(site_name)
                if site_id:
                    target_sites.append({"site_name": site_name, "site_id": site_id})
                    self.log(
                        "Target site added: '{0}' (ID: {1})".format(site_name, site_id),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Site '{0}' not found in Catalyst Center site mapping. "
                        "Available sites: {1}".format(
                            site_name,
                            list(site_name_to_id.keys())[:5]  # Show first 5 for debugging
                        ),
                        "WARNING"
                    )
                    self.add_failure(site_name, "network_management_details", {
                        "error_type": "site_not_found",
                        "error_message": "Site not found or not accessible in Catalyst Center",
                        "error_code": "SITE_NOT_FOUND"
                    })
        else:
            # No specific sites requested - default to Global site only
            self.log(
                "No site filters provided - defaulting to Global site for network "
                "management details retrieval",
                "INFO"
            )

            global_site_id = site_name_to_id.get("Global")
            if global_site_id:
                target_sites.append({"site_name": "Global", "site_id": global_site_id})
                self.log(
                    "Added Global site as default target (ID: {0})".format(global_site_id),
                    "DEBUG"
                )
            else:
                self.log(
                    "Global site not found in mapping - processing all sites as fallback",
                    "WARNING"
                )
                for site_id, site_name in self.site_id_name_dict.items():
                    target_sites.append({"site_name": site_name, "site_id": site_id})
                    if not target_sites:
                        self.log(
                            "No valid target sites identified after filter processing. "
                            "Check filter configuration.",
                            "WARNING"
                        )
                        return {
                            "network_management_details": [],
                            "operation_summary": self.get_operation_summary()
                        }

                    self.log(
                        "Final target sites for processing: {0} sites - {1}".format(
                            len(target_sites),
                            [s["site_name"] for s in target_sites]
                        ),
                        "INFO"
                    )

                self.log(
                    "Fallback to all sites: {0} sites added".format(len(target_sites)),
                    "WARNING"
                )

        # =====================================
        # Step 4: Process Each Site
        # =====================================
        final_nm_details = []
        sites_processed = 0
        sites_succeeded = 0
        sites_failed = 0

        # === Process each site ===
        for site in target_sites:
            site_name = site["site_name"]
            site_id = site["site_id"]

            self.log(
                "Processing site {0}: '{1}' (ID: {2})".format(
                    len(target_sites), site_name, site_id
                ),
                "INFO"
            )

            nm_details = {
                "site_name": site_name,
                "site_id": site_id
            }

            components_retrieved = 0
            components_failed = 0

            # ---------- AAA ----------
            try:
                self.log(
                    "Retrieving AAA settings (network + client) for site '{0}'".format(
                        site_name
                    ),
                    "DEBUG"
                )

                if hasattr(self, "get_aaa_settings_for_site"):
                    aaa_network, aaa_client = self.get_aaa_settings_for_site(site_name, site_id)
                    nm_details["aaaNetwork"] = aaa_network or {}
                    nm_details["aaaClient"] = aaa_client or {}

                    if aaa_network or aaa_client:
                        components_retrieved += 1
                        self.log(
                            "Successfully retrieved AAA settings for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "No AAA settings configured for site '{0}'".format(site_name),
                            "DEBUG"
                        )
                else:
                    nm_details["aaaNetwork"] = {}
                    nm_details["aaaClient"] = {}
                    self.log(
                        "AAA retrieval method not available, using empty configuration",
                        "WARNING"
                    )
            except Exception as e:
                components_failed += 1
                self.log(
                    "AAA retrieval failed for site '{0}': {1}".format(site_name, str(e)),
                    "WARNING"
                )
                nm_details["aaaNetwork"] = {}
                nm_details["aaaClient"] = {}

            # ========== DHCP Settings ==========
            try:
                self.log(
                    "Retrieving DHCP server configuration for site '{0}'".format(site_name),
                    "DEBUG"
                )

                if hasattr(self, "get_dhcp_settings_for_site"):
                    dhcp_settings = self.get_dhcp_settings_for_site(site_name, site_id)
                    nm_details["dhcp"] = dhcp_settings or {}

                    if dhcp_settings:
                        components_retrieved += 1
                        self.log(
                            "Successfully retrieved DHCP settings for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "No DHCP settings configured for site '{0}'".format(site_name),
                            "DEBUG"
                        )
                else:
                    nm_details["dhcp"] = {}
                    self.log(
                        "DHCP retrieval method not available, using empty configuration",
                        "WARNING"
                    )
            except Exception as e:
                components_failed += 1
                self.log(
                    "DHCP retrieval failed for site '{0}': {1}".format(site_name, str(e)),
                    "WARNING"
                )
                nm_details["dhcp"] = {}

            # ========== DNS Settings ==========
            try:
                self.log(
                    "Retrieving DNS server configuration for site '{0}'".format(site_name),
                    "DEBUG"
                )

                if hasattr(self, "get_dns_settings_for_site"):
                    dns_settings = self.get_dns_settings_for_site(site_name, site_id)
                    nm_details["dns"] = dns_settings or {}

                    if dns_settings:
                        components_retrieved += 1
                        self.log(
                            "Successfully retrieved DNS settings for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "No DNS settings configured for site '{0}'".format(site_name),
                            "DEBUG"
                        )
                else:
                    nm_details["dns"] = {}
                    self.log(
                        "DNS retrieval method not available, using empty configuration",
                        "WARNING"
                    )
            except Exception as e:
                components_failed += 1
                self.log(
                    "DNS retrieval failed for site '{0}': {1}".format(site_name, str(e)),
                    "WARNING"
                )
                nm_details["dns"] = {}

            # ========== Telemetry Settings ==========
            try:
                self.log(
                    "Retrieving telemetry settings (NetFlow/SNMP/Syslog) for site '{0}'".format(
                        site_name
                    ),
                    "DEBUG"
                )

                if hasattr(self, "get_telemetry_settings_for_site"):
                    telemetry_settings = self.get_telemetry_settings_for_site(site_name, site_id)
                    nm_details["telemetry"] = telemetry_settings or {}

                    if telemetry_settings:
                        components_retrieved += 1
                        self.log(
                            "Successfully retrieved telemetry settings for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "No telemetry settings configured for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                else:
                    nm_details["telemetry"] = {}
                    self.log(
                        "Telemetry retrieval method not available, using empty configuration",
                        "WARNING"
                    )
            except Exception as e:
                components_failed += 1
                self.log(
                    "Telemetry retrieval failed for site '{0}': {1}".format(
                        site_name, str(e)
                    ),
                    "WARNING"
                )
                nm_details["telemetry"] = {}

            # ========== NTP Settings ==========
            try:
                self.log(
                    "Retrieving NTP server configuration for site '{0}'".format(site_name),
                    "DEBUG"
                )

                if hasattr(self, "get_ntp_settings_for_site"):
                    ntp_settings = self.get_ntp_settings_for_site(site_name, site_id)
                    nm_details["ntp"] = ntp_settings or {}

                    if ntp_settings:
                        components_retrieved += 1
                        self.log(
                            "Successfully retrieved NTP settings for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "No NTP settings configured for site '{0}'".format(site_name),
                            "DEBUG"
                        )
                else:
                    nm_details["ntp"] = {}
                    self.log(
                        "NTP retrieval method not available, using empty configuration",
                        "WARNING"
                    )
            except Exception as e:
                components_failed += 1
                self.log(
                    "NTP retrieval failed for site '{0}': {1}".format(site_name, str(e)),
                    "WARNING"
                )
                nm_details["ntp"] = {}

            # ========== Timezone Settings ==========
            try:
                self.log(
                    "Retrieving timezone configuration for site '{0}'".format(site_name),
                    "DEBUG"
                )

                if hasattr(self, "get_time_zone_settings_for_site"):
                    timezone_settings = self.get_time_zone_settings_for_site(site_name, site_id)
                    nm_details["timeZone"] = timezone_settings or {}

                    if timezone_settings:
                        components_retrieved += 1
                        self.log(
                            "Successfully retrieved timezone settings for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "No timezone settings configured for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                else:
                    nm_details["timeZone"] = {}
                    self.log(
                        "Timezone retrieval method not available, using empty configuration",
                        "WARNING"
                    )
            except Exception as e:
                components_failed += 1
                self.log(
                    "Timezone retrieval failed for site '{0}': {1}".format(
                        site_name, str(e)
                    ),
                    "WARNING"
                )
                nm_details["timeZone"] = {}

            # ========== Banner Settings ==========
            try:
                self.log(
                    "Retrieving banner (message of the day) for site '{0}'".format(
                        site_name
                    ),
                    "DEBUG"
                )

                if hasattr(self, "get_banner_settings_for_site"):
                    banner_settings = self.get_banner_settings_for_site(site_name, site_id)
                    nm_details["banner"] = banner_settings or {}

                    if banner_settings:
                        components_retrieved += 1
                        self.log(
                            "Successfully retrieved banner settings for site '{0}'".format(
                                site_name
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "No banner configured for site '{0}'".format(site_name),
                            "DEBUG"
                        )
                else:
                    nm_details["banner"] = {}
                    self.log(
                        "Banner retrieval method not available, using empty configuration",
                        "WARNING"
                    )
            except Exception as e:
                components_failed += 1
                self.log(
                    "Banner retrieval failed for site '{0}': {1}".format(
                        site_name, str(e)
                    ),
                    "WARNING"
                )
                nm_details["banner"] = {}

            # Store result for this site
            final_nm_details.append(nm_details)
            sites_processed += 1

            # Log site processing summary
            total_components = components_retrieved + components_failed
            self.log(
                "Site '{0}' processing complete - Components retrieved: {1}/{2}, "
                "Failed: {3}".format(
                    site_name, components_retrieved, total_components, components_failed
                ),
                "INFO"
            )

            # Track success/failure for this site
            if components_failed == 0:
                sites_succeeded += 1
                self.add_success(site_name, "network_management_details", {
                    "nm_components_processed": total_components
                })
            else:
                sites_failed += 1
                self.add_failure(site_name, "network_management_details", {
                    "error_type": "partial_failure",
                    "error_message": "{0}/{1} components failed to retrieve".format(
                        components_failed, total_components
                    ),
                    "error_code": "COMPONENT_RETRIEVAL_PARTIAL_FAILURE"
                })

        self.log(
            "Completed network management retrieval for all sites - "
            "Sites processed: {0}, Succeeded: {1}, Failed: {2}".format(
                sites_processed, sites_succeeded, sites_failed
            ),
            "INFO"
        )

        # =====================================
        # Step 5: Apply Unified Reverse Mapping
        # =====================================
        self.log(
            "Applying unified reverse mapping transformation to convert {0} site "
            "configurations to Ansible playbook format".format(len(final_nm_details)),
            "INFO"
        )

        transformed_nm = []
        try:
            self.log("Applying NM unified reverse mapping...", "INFO")

            for index, entry in enumerate(final_nm_details, start=1):
                site_name = entry.get("site_name")

                self.log(
                    "Transforming entry {0}/{1} for site: '{2}'".format(
                        index, len(final_nm_details), site_name
                    ),
                    "DEBUG"
                )

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
                self.log(
                    "Successfully transformed entry {0} for site '{1}'".format(
                        len(final_nm_details), site_name
                    ),
                    "DEBUG"
                )

                self.log(
                    "Unified reverse mapping completed successfully - transformed {0} "
                    "site configurations".format(len(transformed_nm)),
                    "INFO"
                )

            self.log("NM unified reverse mapping completed successfully", "INFO")
            self.log(self.pprint(transformed_nm), "DEBUG")

        except Exception as e:
            self.log(
                "Unified reverse mapping failed for network management: {0}. "
                "Falling back to raw data.".format(str(e)),
                "ERROR"
            )
            transformed_nm = []
            self.log(
                "Network management settings retrieval completed - Retrieved: {0} sites, "
                "Succeeded: {1}, Failed: {2}, Transformed: {3} configurations".format(
                    sites_processed, sites_succeeded, sites_failed, len(transformed_nm)
                ),
                "DEBUG"
            )

        # Return result in consistent format
        return {
            "network_management_details": transformed_nm,
            "operation_summary": self.get_operation_summary()
        }

    def clean_nm_entry(self, entry, depth=0, max_depth=50):
        """
        Recursively convert Catalyst Center MyDict objects to standard Python dictionaries.

        This method ensures that all data structures from Catalyst Center API responses
        are normalized to standard Python types (dict, list, primitives) before being
        processed by unified reverse mapping functions. This prevents type-related errors
        and ensures consistent data handling across all network management components.

        Purpose:
            Transforms proprietary DNAC SDK MyDict objects and nested structures into
            standard Python dictionaries, enabling reliable reverse mapping and YAML
            serialization for network management settings (AAA, DHCP, DNS, NTP, etc.).

        Args:
            entry: Input data to clean/normalize. Supported types:
                - MyDict (DNAC SDK object): Converted to standard dict
                - dict: Recursively cleaned with all values normalized
                - list: Each element recursively cleaned
                - Primitives (str, int, bool, None): Returned as-is

            depth (int, optional): Current recursion depth for infinite loop protection.
                                Default: 0 (root level)
                                Used internally for recursion tracking.

            max_depth (int, optional): Maximum allowed recursion depth.
                                    Default: 50 (prevents stack overflow)
                                    Raises warning if exceeded.

        Returns:
            Cleaned data in standard Python types:
            - dict: Standard Python dictionary with all nested values cleaned
            - list: List with all elements cleaned
            - Primitives: Original value (str, int, bool, None, float)
            - None values are filtered out from dicts
        """
        self.log(
            "Starting recursive data structure normalization to convert DNAC MyDict "
            "objects to standard Python types (depth: {0}/{1})".format(
                depth, max_depth
            ),
            "DEBUG"
        )

        # Recursion depth protection
        if depth > max_depth:
            self.log(
                "Maximum recursion depth ({0}) exceeded during data structure cleaning. "
                "Possible circular reference or extremely deep nesting detected. "
                "Returning empty dict to prevent stack overflow.".format(max_depth),
                "WARNING"
            )
            return {}

        input_type = type(entry).__name__
        self.log(
            "Processing entry at depth {0} - type: {1}".format(depth, input_type),
            "DEBUG"
        )

        # =====================================
        # Case 1: Catalyst Center MyDict Object Detection
        # =====================================
        if hasattr(entry, "to_dict"):
            self.log(
                "Detected Catalyst Center  MyDict object at depth {0}, attempting conversion "
                "to standard Python dict using to_dict() method".format(depth),
                "DEBUG"
            )

            try:
                entry = entry.to_dict()
                self.log(
                    "Successfully converted MyDict to standard dict at depth {0}".format(
                        depth
                    ),
                    "DEBUG"
                )
            except Exception as e:
                self.log(
                    "Failed to convert MyDict using to_dict() method: {0}. "
                    "Attempting fallback conversion using dict()".format(str(e)),
                    "WARNING"
                )
                try:
                    entry = dict(entry)
                    self.log(
                        "Successfully converted MyDict using fallback dict() method "
                        "at depth {0}".format(depth),
                        "DEBUG"
                    )
                except Exception as fallback_error:
                    self.log(
                        "Both to_dict() and dict() conversion failed: {0}. "
                        "Returning empty dict.".format(str(fallback_error)),
                        "ERROR"
                    )
                    return {}

        # =====================================
        # Case 2: Standard Dictionary Processing
        # =====================================
        if isinstance(entry, dict):
            self.log(
                "Processing dictionary at depth {0} with {1} keys: {2}".format(
                    depth, len(entry), list(entry.keys())
                ),
                "DEBUG"
            )

            cleaned = {}
            none_count = 0
            processed_count = 0

            for key, value in entry.items():
                processed_count += 1

                # Skip None values (configuration pruning)
                if value is None:
                    none_count += 1
                    self.log(
                        "Filtering out None value for key '{0}' at depth {1}".format(
                            key, depth
                        ),
                        "DEBUG"
                    )
                    continue

                # Recursively clean nested value
                cleaned_value = self.clean_nm_entry(value, depth + 1, max_depth)

                # Only add non-None results
                if cleaned_value is not None:
                    cleaned[key] = cleaned_value
                else:
                    none_count += 1
                    self.log(
                        "Nested cleaning returned None for key '{0}', filtering out".format(
                            key
                        ),
                        "DEBUG"
                    )

            self.log(
                "Dictionary cleaning completed at depth {0} - Processed: {1} keys, "
                "Filtered: {2} None values, Remaining: {3} keys".format(
                    depth, processed_count, none_count, len(cleaned)
                ),
                "DEBUG"
            )

            return cleaned

        # =====================================
        # Case 3: List Processing
        # =====================================
        if isinstance(entry, list):
            self.log(
                "Processing list at depth {0} with {1} elements".format(
                    depth, len(entry)
                ),
                "DEBUG"
            )

            cleaned_list = []

            for index, item in enumerate(entry):
                self.log(
                    "Cleaning list element {0}/{1} at depth {2}".format(
                        index + 1, len(entry), depth
                    ),
                    "DEBUG"
                )

                cleaned_item = self.clean_nm_entry(item, depth + 1, max_depth)
                cleaned_list.append(cleaned_item)

            self.log(
                "List cleaning completed at depth {0} - Processed {1} elements".format(
                    depth, len(cleaned_list)
                ),
                "DEBUG"
            )

            return cleaned_list

        # =====================================
        # Case 4: Primitive Types (str, int, bool, None, float)
        # =====================================
        if isinstance(entry, (str, int, bool, float)):
            self.log(
                "Primitive type '{0}' detected at depth {1}, returning as-is: {2}".format(
                    input_type, depth, entry
                ),
                "DEBUG"
            )
            return entry

        # =====================================
        # Case 5: Unexpected Type Warning
        # =====================================
        self.log(
            "Unexpected data type '{0}' encountered at depth {1} during cleaning. "
            "Expected MyDict, dict, list, or primitive. Returning as-is: {2}".format(
                input_type, depth, entry
            ),
            "WARNING"
        )

        return entry

    def prune_empty(self, data, depth=0, max_depth=50):
        """
        Recursively remove empty values from nested data structures for clean YAML output.

        This method performs comprehensive pruning of empty values from dictionaries and
        lists to ensure YAML configuration files contain only meaningful data. It removes
        None values, empty strings, empty lists, and empty dictionaries while preserving
        valid data structures and semantic meaning.

        Purpose:
            Generates clean, compact YAML playbook configurations by removing extraneous
            empty values that add no semantic value, improving readability and reducing
            configuration file size for network_settings_workflow_manager playbooks.

        Args:
            data: Input data structure to prune. Supported types:
                - dict: Recursively prune all values, remove empty key-value pairs
                - list: Recursively prune all elements, remove empty items
                - Primitives (str, int, bool, None): Evaluated for emptiness

            depth (int, optional): Current recursion depth for infinite loop protection.
                                Default: 0 (root level)
                                Used internally for recursion tracking.

            max_depth (int, optional): Maximum allowed recursion depth.
                                    Default: 50 (prevents stack overflow)
                                    Logs warning if exceeded.

        Returns:
            Pruned data structure with empty values removed:
            - dict: Dictionary with empty key-value pairs removed
            - list: List with empty elements removed
            - Primitives: Original value if non-empty, removed by caller if empty
            - None: Indicates value should be removed by caller
        """
        self.log(
            "Starting recursive empty value pruning to clean data structure for YAML "
            "output (depth: {0}/{1})".format(depth, max_depth),
            "DEBUG"
        )

        # Recursion depth protection
        if depth > max_depth:
            self.log(
                "Maximum recursion depth ({0}) exceeded during empty value pruning. "
                "Possible circular reference or extremely deep nesting detected. "
                "Returning empty dict to prevent stack overflow.".format(max_depth),
                "WARNING"
            )
            return {}

        # Log input type for debugging
        input_type = type(data).__name__
        self.log(
            "Processing data structure at depth {0} - type: {1}".format(
                depth, input_type
            ),
            "DEBUG"
        )

        # =====================================
        # Case 1: Dictionary Processing
        # =====================================
        if isinstance(data, dict):
            self.log(
                "Processing dictionary at depth {0} with {1} keys: {2}".format(
                    depth, len(data), list(data.keys())
                ),
                "DEBUG"
            )

            cleaned = {}
            keys_processed = 0
            keys_pruned = 0

            for key, value in data.items():
                keys_processed += 1

                # Recursively prune nested value
                pruned_value = self.prune_empty(value, depth + 1, max_depth)

                # Check if pruned value is empty
                if self._is_empty_value(pruned_value):
                    keys_pruned += 1
                    self.log(
                        "Pruning empty value for key '{0}' at depth {1} - value type: {2}, "
                        "value: {3}".format(
                            key, depth, type(pruned_value).__name__, pruned_value
                        ),
                        "DEBUG"
                    )
                    continue

                # Keep non-empty value
                cleaned[key] = pruned_value
                self.log(
                    "Keeping non-empty value for key '{0}' at depth {1}".format(
                        key, depth
                    ),
                    "DEBUG"
                )

            self.log(
                "Dictionary pruning completed at depth {0} - Processed: {1} keys, "
                "Pruned: {2} keys, Remaining: {3} keys".format(
                    depth, keys_processed, keys_pruned, len(cleaned)
                ),
                "DEBUG"
            )

            return cleaned

        # =====================================
        # Case 2: List Processing
        # =====================================
        if isinstance(data, list):
            self.log(
                "Processing list at depth {0} with {1} elements".format(
                    depth, len(data)
                ),
                "DEBUG"
            )

            cleaned_list = []
            elements_processed = 0
            elements_pruned = 0

            for index, item in enumerate(data):
                elements_processed += 1

                self.log(
                    "Cleaning list element {0}/{1} at depth {2}".format(
                        index + 1, len(data), depth
                    ),
                    "DEBUG"
                )

                # Recursively prune list element
                pruned_item = self.prune_empty(item, depth + 1, max_depth)

                # Check if pruned item is empty
                if self._is_empty_value(pruned_item):
                    elements_pruned += 1
                    self.log(
                        "Pruning empty list element at index {0}, depth {1} - type: {2}, "
                        "value: {3}".format(
                            index, depth, type(pruned_item).__name__, pruned_item
                        ),
                        "DEBUG"
                    )
                    continue

                # Keep non-empty element
                cleaned_list.append(pruned_item)
                self.log(
                    "Keeping non-empty list element at index {0}, depth {1}".format(
                        index, depth
                    ),
                    "DEBUG"
                )

            self.log(
                "List pruning completed at depth {0} - Processed: {1} elements, "
                "Pruned: {2} elements, Remaining: {3} elements".format(
                    depth, elements_processed, elements_pruned, len(cleaned_list)
                ),
                "DEBUG"
            )

            return cleaned_list

        # =====================================
        # Case 3: Primitive Values (str, int, bool, None, float)
        # =====================================
        self.log(
            "Primitive type '{0}' detected at depth {1}, evaluating for emptiness: {2}".format(
                input_type, depth, data
            ),
            "DEBUG"
        )

        # Return primitive as-is (caller will check if empty)
        return data

    def _is_empty_value(self, value):
        """
        Check if a value is considered empty for pruning purposes.

        This helper method provides centralized empty value detection logic used
        by the prune_empty function to determine which values should be removed
        from YAML configuration output.

        Args:
            value: Value to check for emptiness. Any type.

        Returns:
            bool: True if value is empty, False otherwise.
                Empty definitions:
                - None: Python None type
                - "": Empty string (zero length or whitespace-only)
                - []: Empty list (zero elements)
                - {}: Empty dictionary (zero key-value pairs)
        """
        # Check for None
        if value is None:
            return True

        # Check for empty string (including whitespace-only)
        if isinstance(value, str):
            is_empty = len(value.strip()) == 0
            if is_empty:
                self.log(
                    "String value is empty or whitespace-only: '{0}'".format(value),
                    "DEBUG"
                )
            return is_empty

        # Check for empty list
        if isinstance(value, list):
            is_empty = len(value) == 0
            if is_empty:
                self.log("List is empty", "DEBUG")
            return is_empty

        # Check for empty dictionary
        if isinstance(value, dict):
            is_empty = len(value) == 0
            if is_empty:
                self.log("Dictionary is empty", "DEBUG")
            return is_empty

        # All other values (int, bool, float, etc.) are considered non-empty
        # Important: 0, False, 0.0 are valid values and should NOT be pruned
        return False

    def extract_network_aaa(self, entry):
        """
        Extract and transform Network AAA configuration from network management API response.

        This method extracts network device AAA (Authentication, Authorization, Accounting)
        settings from Catalyst Center network management API responses and transforms them
        into Ansible playbook-compatible format for the network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center AAA network configuration data into clean, structured
            format suitable for YAML playbook generation, handling optional fields appropriately
            and ensuring compatibility with network_settings_workflow_manager module expectations.

        Args:
            entry (dict or None): Network management entry containing AAA configuration.
                Expected structure:
                {
                    "aaaNetwork": {
                        "primaryServerIp": "10.0.0.1",
                        "secondaryServerIp": "10.0.0.2",
                        "protocol": "RADIUS",
                        "serverType": "ISE",
                        "pan": "ise-pan.example.com"  # Optional - ISE PAN address
                    }
                }

        Returns:
            dict: Transformed AAA network configuration or empty dict:
                {
                    "primary_server_address": "10.0.0.1",
                    "secondary_server_address": "10.0.0.2",
                    "protocol": "RADIUS",
                    "server_type": "ISE",
                    "pan_address": "ise-pan.example.com"  # Only if present
                }
                Returns {} if:
                - entry is None
                - entry is not a dict
                - aaaNetwork key is missing
                - aaaNetwork is empty

        Field Mapping:
            API Field             -> Ansible Field
            primaryServerIp       -> primary_server_address
            secondaryServerIp     -> secondary_server_address
            protocol              -> protocol (RADIUS/TACACS)
            serverType            -> server_type (AAA/ISE)
            pan                   -> pan_address (conditional - only for ISE)

        ISE-Specific Handling:
            - pan_address field is only included when present in API response
            - Required when serverType is "ISE" for ISE PAN (Policy Admin Node)
            - Omitted for serverType "AAA" to keep YAML clean

        Error Handling:
            - Returns empty dict for None/invalid input
            - Handles missing nested keys gracefully
            - Validates data structure before extraction
            - Logs warnings for unexpected data

        Examples:
            # RADIUS AAA configuration
            extract_network_aaa({
                "aaaNetwork": {
                    "primaryServerIp": "10.0.0.1",
                    "protocol": "RADIUS",
                    "serverType": "AAA"
                }
            })
            -> {
                "primary_server_address": "10.0.0.1",
                "secondary_server_address": "",
                "protocol": "RADIUS",
                "server_type": "AAA"
            }

            # ISE configuration with PAN
            extract_network_aaa({
                "aaaNetwork": {
                    "primaryServerIp": "10.0.0.1",
                    "protocol": "RADIUS",
                    "serverType": "ISE",
                    "pan": "ise-pan.example.com"
                }
            })
            -> {
                "primary_server_address": "10.0.0.1",
                "secondary_server_address": "",
                "protocol": "RADIUS",
                "server_type": "ISE",
                "pan_address": "ise-pan.example.com"
            }
        """
        self.log(
            "Extracting Network AAA configuration from network management entry to "
            "transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty AAA configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for Network AAA extraction - expected dict, got {0}. "
                "Returning empty configuration.".format(type(entry).__name__),
                "WARNING"
            )
            return {}

        # Extract aaaNetwork data
        data = entry.get("aaaNetwork")

        if not data:
            self.log(
                "No 'aaaNetwork' configuration found in entry, returning empty AAA "
                "configuration (site may not have network AAA configured)",
                "DEBUG"
            )
            return {}

        if not isinstance(data, dict):
            self.log(
                "Invalid aaaNetwork type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(data).__name__),
                "WARNING"
            )
            return {}

        self.log(
            "Found Network AAA configuration with {0} field(s): {1}".format(
                len(data), list(data.keys())
            ),
            "DEBUG"
        )

        # Extract base AAA configuration fields
        primary_server = data.get("primaryServerIp", "")
        secondary_server = data.get("secondaryServerIp", "")
        protocol = data.get("protocol", "")
        server_type = data.get("serverType", "")

        self.log(
            "Extracted Network AAA base fields - Primary: '{0}', Secondary: '{1}', "
            "Protocol: '{2}', ServerType: '{3}'".format(
                primary_server if primary_server else "Not configured",
                secondary_server if secondary_server else "Not configured",
                protocol if protocol else "Not configured",
                server_type if server_type else "Not configured"
            ),
            "DEBUG"
        )

        # Build base result structure
        result = {
            "primary_server_address": primary_server,
            "secondary_server_address": secondary_server,
            "protocol": protocol,
            "server_type": server_type,
        }

        # Conditional ISE PAN address extraction
        pan_address = data.get("pan")

        if pan_address:
            result["pan_address"] = pan_address
            self.log(
                "ISE PAN address found and included in configuration: '{0}' "
                "(required for serverType=ISE)".format(pan_address),
                "DEBUG"
            )
        else:
            self.log(
                "No ISE PAN address configured (field 'pan' not present or empty). "
                "This is expected for serverType='AAA'.",
                "DEBUG"
            )

        # Validation: Check if ISE server type has PAN address
        if server_type == "ISE" and not pan_address:
            self.log(
                "WARNING: serverType is 'ISE' but pan_address is missing. "
                "ISE configurations typically require PAN (Policy Admin Node) address.",
                "WARNING"
            )

        self.log(
            "Successfully extracted Network AAA configuration with {0} field(s). "
            "PAN address included: {1}".format(
                len(result),
                "Yes" if "pan_address" in result else "No"
            ),
            "DEBUG"
        )

        return result

    def extract_client_aaa(self, entry):
        """
        Extract and transform Client & Endpoint AAA configuration from network management API response.

        This method extracts client and endpoint AAA (Authentication, Authorization, Accounting)
        settings from Catalyst Center network management API responses and transforms them
        into Ansible playbook-compatible format for the network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center AAA client/endpoint configuration data into clean,
            structured format suitable for YAML playbook generation, handling optional fields
            appropriately and ensuring compatibility with network_settings_workflow_manager
            module expectations.

        Args:
            entry (dict or None): Network management entry containing AAA client configuration.
                Expected structure:
                {
                    "aaaClient": {
                        "primaryServerIp": "10.0.0.1",
                        "secondaryServerIp": "10.0.0.2",
                        "protocol": "RADIUS",
                        "serverType": "ISE",
                        "pan": "ise-pan.example.com"  # Optional - ISE PAN address
                    }
                }

        Returns:
            dict: Transformed AAA client & endpoint configuration or empty dict:
                {
                    "primary_server_address": "10.0.0.1",
                    "secondary_server_address": "10.0.0.2",
                    "protocol": "RADIUS",
                    "server_type": "ISE",
                    "pan_address": "ise-pan.example.com"  # Only if present
                }
                Returns {} if:
                - entry is None
                - entry is not a dict
                - aaaClient key is missing
                - aaaClient is empty

        Field Mapping:
            API Field             -> Ansible Field
            primaryServerIp       -> primary_server_address
            secondaryServerIp     -> secondary_server_address
            protocol              -> protocol (RADIUS/TACACS)
            serverType            -> server_type (AAA/ISE)
            pan                   -> pan_address (conditional - only for ISE)

        ISE-Specific Handling:
            - pan_address field is only included when present in API response
            - Required when serverType is "ISE" for ISE PAN (Policy Admin Node)
            - Omitted for serverType "AAA" to keep YAML clean

        Difference from Network AAA:
            - Network AAA: Device authentication (network infrastructure)
            - Client AAA: User/endpoint authentication (clients connecting to network)
            - Both share identical structure but serve different authentication contexts

        Error Handling:
            - Returns empty dict for None/invalid input
            - Handles missing nested keys gracefully
            - Validates data structure before extraction
            - Logs warnings for unexpected data

        Examples:
            # RADIUS AAA configuration for clients
            extract_client_aaa({
                "aaaClient": {
                    "primaryServerIp": "10.0.0.1",
                    "protocol": "RADIUS",
                    "serverType": "AAA"
                }
            })
            -> {
                "primary_server_address": "10.0.0.1",
                "secondary_server_address": "",
                "protocol": "RADIUS",
                "server_type": "AAA"
            }

            # ISE configuration with PAN for client authentication
            extract_client_aaa({
                "aaaClient": {
                    "primaryServerIp": "10.0.0.1",
                    "protocol": "RADIUS",
                    "serverType": "ISE",
                    "pan": "ise-pan.example.com"
                }
            })
            -> {
                "primary_server_address": "10.0.0.1",
                "secondary_server_address": "",
                "protocol": "RADIUS",
                "server_type": "ISE",
                "pan_address": "ise-pan.example.com"
            }
        """
        self.log(
            "Extracting Client & Endpoint AAA configuration from network management entry "
            "to transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty Client AAA configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for Client AAA extraction - expected dict, got {0}. "
                "Returning empty configuration.".format(type(entry).__name__),
                "WARNING"
            )
            return {}

        # Extract aaaClient data
        data = entry.get("aaaClient")

        if not data:
            self.log(
                "No 'aaaClient' configuration found in entry, returning empty Client AAA "
                "configuration (site may not have client/endpoint AAA configured)",
                "DEBUG"
            )
            return {}

        if not isinstance(data, dict):
            self.log(
                "Invalid aaaClient type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(data).__name__),
                "WARNING"
            )
            return {}

        self.log(
            "Found Client & Endpoint AAA configuration with {0} field(s): {1}".format(
                len(data), list(data.keys())
            ),
            "DEBUG"
        )

        # Extract base AAA configuration fields
        primary_server = data.get("primaryServerIp", "")
        secondary_server = data.get("secondaryServerIp", "")
        protocol = data.get("protocol", "")
        server_type = data.get("serverType", "")

        self.log(
            "Extracted Client AAA base fields - Primary: '{0}', Secondary: '{1}', "
            "Protocol: '{2}', ServerType: '{3}'".format(
                primary_server if primary_server else "Not configured",
                secondary_server if secondary_server else "Not configured",
                protocol if protocol else "Not configured",
                server_type if server_type else "Not configured"
            ),
            "DEBUG"
        )

        # Build base result structure
        result = {
            "primary_server_address": primary_server,
            "secondary_server_address": secondary_server,
            "protocol": protocol,
            "server_type": server_type,
        }

        # Conditional ISE PAN address extraction
        pan_address = data.get("pan")

        if pan_address:
            result["pan_address"] = pan_address
            self.log(
                "ISE PAN address found and included in Client AAA configuration: '{0}' "
                "(required for serverType=ISE)".format(pan_address),
                "DEBUG"
            )
        else:
            self.log(
                "No ISE PAN address configured for Client AAA (field 'pan' not present or empty). "
                "This is expected for serverType='AAA'.",
                "DEBUG"
            )

        # Validation: Check if ISE server type has PAN address
        if server_type == "ISE" and not pan_address:
            self.log(
                "WARNING: Client AAA serverType is 'ISE' but pan_address is missing. "
                "ISE configurations typically require PAN (Policy Admin Node) address.",
                "WARNING"
            )

        self.log(
            "Successfully extracted Client & Endpoint AAA configuration with {0} field(s). "
            "PAN address included: {1}".format(
                len(result),
                "Yes" if "pan_address" in result else "No"
            ),
            "DEBUG"
        )

        return result

    def extract_dhcp(self, entry):
        """
        Extract DHCP server settings from network management API response.
        This method extracts DHCP server IP addresses from Catalyst Center network management
        API responses and transforms them into Ansible playbook-compatible format for the
        network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center DHCP configuration data into clean, structured
            format suitable for YAML playbook generation, preserving empty server lists
            to maintain semantic meaning (no DHCP servers configured vs missing data).

        Args:
            entry (dict or None): Network management entry containing DHCP configuration.
                Expected structure:
                {
                    "dhcp": {
                        "servers": ["10.0.0.1", "10.0.0.2"]
                    }
                }

        Returns:
            list: DHCP server IP addresses or empty list:
                - ["10.0.0.1", "10.0.0.2"]: List of configured DHCP servers
                - []: Empty list indicates no DHCP servers configured (preserved for semantics)
                Returns [] if:
                - entry is None
                - entry is not a dict
                - dhcp key is missing
                - dhcp.servers is missing or None

        Field Mapping:
            API Field              -> Ansible Field
            dhcp.servers (list)    -> dhcp_server (list)

        Empty List Handling:
            Empty DHCP server lists are explicitly preserved to maintain semantic meaning:
            - [] means "no DHCP servers configured" (valid configuration state)
            - Different from missing dhcp section (no configuration at all)
            - Important for network management settings where empty = "use inherited settings"

        Error Handling:
            - Returns empty list for None/invalid input
            - Handles missing nested keys gracefully
            - Validates data structure before extraction
            - Logs warnings for unexpected data

        Examples:
            # DHCP servers configured
            extract_dhcp({
                "dhcp": {
                    "servers": ["10.0.0.1", "10.0.0.2"]
                }
            })
            -> ["10.0.0.1", "10.0.0.2"]

            # No DHCP servers configured (empty list)
            extract_dhcp({
                "dhcp": {
                    "servers": []
                }
            })
            -> []

            # DHCP section missing
            extract_dhcp({"siteName": "Global/USA/NYC"})
            -> []
        """
        self.log(
            "Extracting DHCP server configuration from network management entry to "
            "transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty DHCP server list",
                "DEBUG"
            )
            return []

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for DHCP extraction - expected dict, got {0}. "
                "Returning empty server list.".format(type(entry).__name__),
                "WARNING"
            )
            return []

        # Extract dhcp data
        dhcp_data = entry.get("dhcp")

        if not dhcp_data:
            self.log(
                "No 'dhcp' configuration found in entry, returning empty server list "
                "(site may not have DHCP configured or inherits from parent)",
                "DEBUG"
            )
            return []

        if not isinstance(dhcp_data, dict):
            self.log(
                "Invalid dhcp type - expected dict, got {0}. "
                "Returning empty server list.".format(type(dhcp_data).__name__),
                "WARNING"
            )
            return []

        self.log(
            "Found DHCP configuration with {0} field(s): {1}".format(
                len(dhcp_data), list(dhcp_data.keys())
            ),
            "DEBUG"
        )

        # Extract servers list
        servers = dhcp_data.get("servers")

        # Validate servers field
        if servers is None:
            self.log(
                "No 'servers' field found in DHCP configuration, returning empty list",
                "DEBUG"
            )
            return []

        if not isinstance(servers, list):
            self.log(
                "Invalid servers type - expected list, got {0}. "
                "Converting to list.".format(type(servers).__name__),
                "WARNING"
            )
            # Attempt conversion to list
            if isinstance(servers, str):
                servers = [servers] if servers else []
                self.log(
                    "Converted string server '{0}' to list".format(servers[0] if servers else ""),
                    "DEBUG"
                )
            else:
                return []

        server_count = len(servers)
        if server_count > 0:
            self.log(
                "Extracted {0} DHCP server(s): {1}".format(
                    server_count,
                    servers
                ),
                "INFO"
            )
        else:
            self.log(
                "Extracted empty DHCP server list (explicitly preserving empty list "
                "to indicate no DHCP servers configured)",
                "DEBUG"
            )

        self.log(
            "Successfully extracted DHCP server configuration with {0} server(s)".format(
                len(servers)
            ),
            "DEBUG"
        )

        return servers

    def extract_dns(self, entry):
        """
        Extract and transform DNS server configuration from network management API response.

        This method extracts DNS domain name and server IP addresses from Catalyst Center
        network management API responses and transforms them into Ansible playbook-compatible
        format for the network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center DNS configuration data into clean, structured
            format suitable for YAML playbook generation, handling primary/secondary server
            extraction safely and ensuring compatibility with network_settings_workflow_manager
            module expectations.

        Args:
            entry (dict or None): Network management entry containing DNS configuration.
                Expected structure:
                {
                    "dns": {
                        "domainName": "example.com",
                        "dnsServers": ["8.8.8.8", "8.8.4.4"]
                    }
                }

        Returns:
            dict: Transformed DNS configuration or empty dict:
                {
                    "domain_name": "example.com",
                    "primary_ip_address": "8.8.8.8",
                    "secondary_ip_address": "8.8.4.4"
                }
                Returns {} if:
                - entry is None
                - entry is not a dict
                - dns key is missing
                - dns is empty

                Empty strings are used for missing server addresses:
                - primary_ip_address: "" if no servers configured
                - secondary_ip_address: "" if only one server configured

        Field Mapping:
            API Field              -> Ansible Field
            domainName             -> domain_name
            dnsServers[0]          -> primary_ip_address
            dnsServers[1]          -> secondary_ip_address (optional)

        DNS Server Extraction Logic:
            - dnsServers list expected to contain 0-2 IP addresses
            - First server (index 0): Primary DNS server
            - Second server (index 1): Secondary DNS server (optional)
            - Empty string used when server not configured
            - Safe list access prevents IndexError crashes

        Error Handling:
            - Returns empty dict for None/invalid input
            - Handles missing nested keys gracefully
            - Validates data structure before extraction
            - Logs warnings for unexpected data
            - Safe list indexing with bounds checking

        Examples:
            # Both primary and secondary DNS servers
            extract_dns({
                "dns": {
                    "domainName": "example.com",
                    "dnsServers": ["8.8.8.8", "8.8.4.4"]
                }
            })
            -> {
                "domain_name": "example.com",
                "primary_ip_address": "8.8.8.8",
                "secondary_ip_address": "8.8.4.4"
            }

            # Only primary DNS server
            extract_dns({
                "dns": {
                    "domainName": "corp.local",
                    "dnsServers": ["10.0.0.1"]
                }
            })
            -> {
                "domain_name": "corp.local",
                "primary_ip_address": "10.0.0.1",
                "secondary_ip_address": ""
            }

            # No DNS servers configured
            extract_dns({
                "dns": {
                    "domainName": "example.com",
                    "dnsServers": []
                }
            })
            -> {
                "domain_name": "example.com",
                "primary_ip_address": "",
                "secondary_ip_address": ""
            }
        """
        self.log(
            "Extracting DNS server configuration from network management entry to "
            "transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty DNS configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for DNS extraction - expected dict, got {0}. "
                "Returning empty configuration.".format(type(entry).__name__),
                "WARNING"
            )
            return {}

        # Extract dns data
        dns_data = entry.get("dns")

        if not dns_data:
            self.log(
                "No 'dns' configuration found in entry, returning empty DNS "
                "configuration (site may not have DNS configured)",
                "DEBUG"
            )
            return {}

        if not isinstance(dns_data, dict):
            self.log(
                "Invalid dns type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(dns_data).__name__),
                "WARNING"
            )
            return {}

        self.log(
            "Found DNS configuration with {0} field(s): {1}".format(
                len(dns_data), list(dns_data.keys())
            ),
            "DEBUG"
        )

        # Extract domain name
        domain_name = dns_data.get("domainName", "")

        # Extract DNS servers list
        dns_servers = dns_data.get("dnsServers")

        # Validate dns_servers field
        if dns_servers is None:
            self.log(
                "No 'dnsServers' field found in DNS configuration, using empty list",
                "DEBUG"
            )
            dns_servers = []

        if not isinstance(dns_servers, list):
            self.log(
                "Invalid dnsServers type - expected list, got {0}. "
                "Converting to list.".format(type(dns_servers).__name__),
                "WARNING"
            )
            # Attempt conversion to list
            if isinstance(dns_servers, str):
                dns_servers = [dns_servers] if dns_servers else []
                self.log(
                    "Converted string DNS server '{0}' to list".format(
                        dns_servers[0] if dns_servers else ""
                    ),
                    "DEBUG"
                )
            else:
                dns_servers = []

        # Safe extraction of primary and secondary DNS servers with bounds checking
        primary_ip = ""
        secondary_ip = ""

        if len(dns_servers) >= 1:
            primary_ip = dns_servers[0] if dns_servers[0] else ""
            self.log(
                "Extracted primary DNS server: '{0}'".format(
                    primary_ip if primary_ip else "Not configured"
                ),
                "DEBUG"
            )
        else:
            self.log(
                "No primary DNS server configured (empty dnsServers list)",
                "DEBUG"
            )

        if len(dns_servers) >= 2:
            secondary_ip = dns_servers[1] if dns_servers[1] else ""
            self.log(
                "Extracted secondary DNS server: '{0}'".format(
                    secondary_ip if secondary_ip else "Not configured"
                ),
                "DEBUG"
            )
        else:
            self.log(
                "No secondary DNS server configured (only {0} server(s) in list)".format(
                    len(dns_servers)
                ),
                "DEBUG"
            )

        # Log if more than 2 servers present (unusual configuration)
        if len(dns_servers) > 2:
            extra_servers = dns_servers[2:]
            self.log(
                "DNS configuration contains {0} additional server(s) beyond primary/secondary: {1}. "
                "Only primary and secondary will be extracted.".format(
                    len(extra_servers), extra_servers
                ),
                "WARNING"
            )

        self.log(
            "Extracted DNS configuration - Domain: '{0}', Primary: '{1}', Secondary: '{2}'".format(
                domain_name if domain_name else "Not configured",
                primary_ip if primary_ip else "Not configured",
                secondary_ip if secondary_ip else "Not configured"
            ),
            "DEBUG"
        )

        # Build result structure
        result = {
            "domain_name": domain_name,
            "primary_ip_address": primary_ip,
            "secondary_ip_address": secondary_ip,
        }

        self.log(
            "Successfully extracted DNS configuration with domain '{0}' and {1} server(s)".format(
                domain_name if domain_name else "None",
                len([s for s in [primary_ip, secondary_ip] if s])
            ),
            "DEBUG"
        )

        return result

    def extract_ntp(self, entry):
        """
        Extract and transform NTP server configuration from network management API response.

        This method extracts NTP (Network Time Protocol) server addresses from Catalyst Center
        network management API responses and transforms them into Ansible playbook-compatible
        format for the network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center NTP configuration data into clean, structured
            format suitable for YAML playbook generation, preserving empty server lists
            to maintain semantic meaning (no NTP servers configured vs missing data).

        Args:
            entry (dict or None): Network management entry containing NTP configuration.
                Expected structure:
                {
                    "ntp": {
                        "servers": ["pool.ntp.org", "time.nist.gov"]
                    }
                }

        Returns:
            list: NTP server addresses or empty list:
                - ["pool.ntp.org", "time.nist.gov"]: List of configured NTP servers
                - []: Empty list indicates no NTP servers configured (preserved for semantics)
                Returns [] if:
                - entry is None
                - entry is not a dict
                - ntp key is missing
                - ntp.servers is missing or None

        Field Mapping:
            API Field              -> Ansible Field
            ntp.servers (list)     -> ntp_server (list)

        Empty List Handling:
            Empty NTP server lists are explicitly preserved to maintain semantic meaning:
            - [] means "no NTP servers configured" (valid configuration state)
            - Different from missing ntp section (no configuration at all)
            - Important for network management settings where empty = "use default/inherited settings"

        NTP Server Format:
            Supports both hostname and IP address formats:
            - Hostnames: "pool.ntp.org", "time.nist.gov", "ntp.example.com"
            - IPv4: "129.6.15.28", "132.163.96.1"
            - IPv6: "2610:20:6f15:15::27", "2001:67c:1560:8003::c8"

        Error Handling:
            - Returns empty list for None/invalid input
            - Handles missing nested keys gracefully
            - Validates data structure before extraction
            - Logs warnings for unexpected data

        Examples:
            # Multiple NTP servers configured
            extract_ntp({
                "ntp": {
                    "servers": ["pool.ntp.org", "time.nist.gov"]
                }
            })
            -> ["pool.ntp.org", "time.nist.gov"]

            # Single NTP server
            extract_ntp({
                "ntp": {
                    "servers": ["pool.ntp.org"]
                }
            })
            -> ["pool.ntp.org"]

            # No NTP servers configured (empty list)
            extract_ntp({
                "ntp": {
                    "servers": []
                }
            })
            -> []

            # NTP section missing
            extract_ntp({"siteName": "Global/USA/NYC"})
            -> []
        """
        self.log(
            "Extracting NTP server configuration from network management entry to "
            "transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty NTP server list",
                "DEBUG"
            )
            return []

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for NTP extraction - expected dict, got {0}. "
                "Returning empty server list.".format(type(entry).__name__),
                "WARNING"
            )
            return []

        # Extract ntp data
        ntp_data = entry.get("ntp")

        if not ntp_data:
            self.log(
                "No 'ntp' configuration found in entry, returning empty server list "
                "(site may not have NTP configured or inherits from parent)",
                "DEBUG"
            )
            return []

        if not isinstance(ntp_data, dict):
            self.log(
                "Invalid ntp type - expected dict, got {0}. "
                "Returning empty server list.".format(type(ntp_data).__name__),
                "WARNING"
            )
            return []

        self.log(
            "Found NTP configuration with {0} field(s): {1}".format(
                len(ntp_data), list(ntp_data.keys())
            ),
            "DEBUG"
        )

        # Extract servers list
        servers = ntp_data.get("servers")

        # Validate servers field
        if servers is None:
            self.log(
                "No 'servers' field found in NTP configuration, returning empty list",
                "DEBUG"
            )
            return []

        if not isinstance(servers, list):
            self.log(
                "Invalid servers type - expected list, got {0}. "
                "Converting to list.".format(type(servers).__name__),
                "WARNING"
            )
            # Attempt conversion to list
            if isinstance(servers, str):
                servers = [servers] if servers else []
                self.log(
                    "Converted string server '{0}' to list".format(servers[0] if servers else ""),
                    "DEBUG"
                )
            else:
                return []

        # Log extracted values
        server_count = len(servers)
        if server_count > 0:
            self.log(
                "Extracted {0} NTP server(s): {1}".format(
                    server_count,
                    servers
                ),
                "INFO"
            )
        else:
            self.log(
                "Extracted empty NTP server list (explicitly preserving empty list "
                "to indicate no NTP servers configured)",
                "DEBUG"
            )

        # Validate server formats (optional quality check)
        for idx, server in enumerate(servers, start=1):
            if not server or not isinstance(server, str):
                self.log(
                    "NTP server {0}/{1} has invalid format: {2} (type: {3})".format(
                        idx, server_count, server, type(server).__name__
                    ),
                    "WARNING"
                )
            else:
                # Log server type for debugging (hostname vs IP)
                if ":" in server:
                    server_type = "IPv6 address"
                elif "." in server and all(part.isdigit() for part in server.split(".")):
                    server_type = "IPv4 address"
                else:
                    server_type = "hostname"

                self.log(
                    "NTP server {0}/{1}: '{2}' ({3})".format(
                        idx, server_count, server, server_type
                    ),
                    "DEBUG"
                )

        self.log(
            "Successfully extracted NTP server configuration with {0} server(s)".format(
                len(servers)
            ),
            "DEBUG"
        )

        return servers

    def extract_timezone(self, entry):
        """
        Extract and transform timezone configuration from network management API response.

        This method extracts timezone identifier from Catalyst Center network management
        API responses and transforms it into Ansible playbook-compatible format for the
        network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center timezone configuration data into clean string
            format suitable for YAML playbook generation, ensuring compatibility with
            network_settings_workflow_manager module timezone expectations.

        Args:
            entry (dict or None): Network management entry containing timezone configuration.
                Expected structure:
                {
                    "timeZone": {
                        "identifier": "America/New_York"
                    }
                }

        Returns:
            str: Timezone identifier string or empty string:
                - "America/New_York": Valid timezone identifier (IANA format)
                - "UTC": Universal Coordinated Time
                - "": Empty string when no timezone configured
                Returns "" if:
                - entry is None
                - entry is not a dict
                - timeZone key is missing
                - timeZone.identifier is missing or None

        Field Mapping:
            API Field                    -> Ansible Field
            timeZone.identifier (str)    -> timezone (str)

        Timezone Format:
            IANA timezone database format (Olson database):
            - Continental format: "Continent/City" (e.g., "America/New_York")
            - UTC variations: "UTC", "GMT"
            - Regional offsets: "Etc/GMT+5", "Etc/GMT-8"


        Examples:
            # US Eastern timezone
            extract_timezone({
                "timeZone": {
                    "identifier": "America/New_York"
                }
            })
            -> "America/New_York"

            # UTC timezone
            extract_timezone({
                "timeZone": {
                    "identifier": "UTC"
                }
            })
            -> "UTC"

            # No timezone configured
            extract_timezone({
                "timeZone": {
                    "identifier": ""
                }
            })
            -> ""

            # Timezone section missing
            extract_timezone({"siteName": "Global/USA/NYC"})
            -> ""

        """
        self.log(
            "Extracting timezone configuration from network management entry to "
            "transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty timezone string",
                "DEBUG"
            )
            return ""

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for timezone extraction - expected dict, got {0}. "
                "Returning empty string.".format(type(entry).__name__),
                "WARNING"
            )
            return ""

        # Extract timeZone data
        timezone_data = entry.get("timeZone")

        if not timezone_data:
            self.log(
                "No 'timeZone' configuration found in entry, returning empty string "
                "(site may not have timezone configured or inherits from parent)",
                "DEBUG"
            )
            return ""

        if not isinstance(timezone_data, dict):
            self.log(
                "Invalid timeZone type - expected dict, got {0}. "
                "Returning empty string.".format(type(timezone_data).__name__),
                "WARNING"
            )
            return ""

        self.log(
            "Found timezone configuration with {0} field(s): {1}".format(
                len(timezone_data), list(timezone_data.keys())
            ),
            "DEBUG"
        )

        # Extract timezone identifier
        timezone_identifier = timezone_data.get("identifier")

        # Validate timezone identifier field
        if timezone_identifier is None:
            self.log(
                "No 'identifier' field found in timezone configuration, returning empty string",
                "DEBUG"
            )
            return ""

        if not isinstance(timezone_identifier, str):
            self.log(
                "Invalid identifier type - expected str, got {0}. "
                "Converting to string.".format(type(timezone_identifier).__name__),
                "WARNING"
            )
            timezone_identifier = str(timezone_identifier) if timezone_identifier else ""

        # Clean whitespace
        timezone_identifier = timezone_identifier.strip()

        if timezone_identifier:
            self.log(
                "Extracted valid timezone identifier: '{0}'".format(timezone_identifier),
                "INFO"
            )
        else:
            self.log(
                "Extracted empty timezone identifier (explicitly preserving empty string "
                "to indicate no timezone configured)",
                "DEBUG"
            )

        self.log(
            "Successfully extracted timezone configuration: '{0}'".format(
                timezone_identifier if timezone_identifier else "Not configured"
            ),
            "DEBUG"
        )

        return timezone_identifier

    def extract_banner(self, entry):
        """
        Extract and transform Message of the Day (banner) configuration from network management API response.

        This method extracts device banner/MOTD settings from Catalyst Center network management
        API responses and transforms them into Ansible playbook-compatible format for the
        network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center banner configuration data into clean, structured
            format suitable for YAML playbook generation, handling banner message content
            and retention flags appropriately.

        Args:
            entry (dict or None): Network management entry containing banner configuration.
                Expected structure:
                {
                    "banner": {
                        "message": "Authorized Access Only\nUnauthorized access prohibited",
                        "retainExistingBanner": false
                    }
                }

        Returns:
            dict: Transformed banner configuration or empty dict:
                {
                    "banner_message": "Authorized Access Only\nUnauthorized access prohibited",
                    "retain_existing_banner": false
                }
                Returns {} if:
                - entry is None
                - entry is not a dict
                - banner key is missing
                - banner is empty

        Field Mapping:
            API Field              -> Ansible Field
            message                -> banner_message
            retainExistingBanner   -> retain_existing_banner

        Examples:
            # Standard banner with message
            extract_banner({
                "banner": {
                    "message": "Authorized Access Only",
                    "retainExistingBanner": false
                }
            })
            -> {
                "banner_message": "Authorized Access Only",
                "retain_existing_banner": false
            }

            # Multi-line banner
            extract_banner({
                "banner": {
                    "message": "Line 1\nLine 2\nLine 3",
                    "retainExistingBanner": true
                }
            })
            -> {
                "banner_message": "Line 1\nLine 2\nLine 3",
                "retain_existing_banner": true
            }

            # Empty banner (clear banner)
            extract_banner({
                "banner": {
                    "message": "",
                    "retainExistingBanner": false
                }
            })
            -> {
                "banner_message": "",
                "retain_existing_banner": false
            }
        """
        self.log(
            "Extracting Message of the Day (banner) configuration from network management "
            "entry to transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty banner configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for banner extraction - expected dict, got {0}. "
                "Returning empty configuration.".format(type(entry).__name__),
                "WARNING"
            )
            return {}

        # Extract banner data
        banner_data = entry.get("banner")

        if not banner_data:
            self.log(
                "No 'banner' configuration found in entry, returning empty banner "
                "configuration (site may not have MOTD configured)",
                "DEBUG"
            )
            return {}

        if not isinstance(banner_data, dict):
            self.log(
                "Invalid banner type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(banner_data).__name__),
                "WARNING"
            )
            return {}

        self.log(
            "Found banner configuration with {0} field(s): {1}".format(
                len(banner_data), list(banner_data.keys())
            ),
            "DEBUG"
        )

        # Extract banner fields
        banner_message = banner_data.get("message")
        retain_existing = banner_data.get("retainExistingBanner")

        # Validate banner message field
        if banner_message is None:
            self.log(
                "No 'message' field found in banner configuration, using empty string",
                "DEBUG"
            )
            banner_message = ""

        if not isinstance(banner_message, str):
            self.log(
                "Invalid message type - expected str, got {0}. Converting to string.".format(
                    type(banner_message).__name__
                ),
                "WARNING"
            )
            banner_message = str(banner_message)

        # Validate retain_existing_banner field
        if retain_existing is None:
            self.log(
                "No 'retainExistingBanner' field found, defaulting to false (Catalyst "
                "Center v1 API default behavior)",
                "DEBUG"
            )
            retain_existing = False

        if not isinstance(retain_existing, bool):
            self.log(
                "Invalid retainExistingBanner type - expected bool, got {0}. "
                "Converting to boolean.".format(type(retain_existing).__name__),
                "WARNING"
            )
            retain_existing = bool(retain_existing)

        message_preview = banner_message[:50] + "..." if len(banner_message) > 50 else banner_message
        if banner_message:
            # Check for multi-line messages
            line_count = banner_message.count('\n') + 1
            self.log(
                "Extracted banner message ({0} line(s), {1} chars): '{2}', "
                "retain_existing: {3}".format(
                    line_count,
                    len(banner_message),
                    message_preview,
                    retain_existing
                ),
                "INFO"
            )

            # Warn about whitespace-only messages
            if banner_message.strip() == "":
                self.log(
                    "Banner message contains only whitespace ({0} chars) - "
                    "this may be unintentional".format(len(banner_message)),
                    "WARNING"
                )
        else:
            self.log(
                "Extracted empty banner message (clear banner mode), "
                "retain_existing: {0}".format(retain_existing),
                "DEBUG"
            )

        # Build result structure
        result = {
            "banner_message": banner_message,
            "retain_existing_banner": retain_existing
        }

        self.log(
            "Successfully extracted banner configuration - Message length: {0} chars, "
            "Retain existing: {1}".format(
                len(banner_message),
                retain_existing
            ),
            "DEBUG"
        )

        return result

    def extract_netflow(self, entry):
        """
        Extract and transform NetFlow collector configuration from network management API response.

        This method extracts NetFlow collector (Application Visibility) settings from Catalyst
        Center network management API responses and transforms them into Ansible playbook-compatible
        format for the network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center NetFlow collector configuration data into clean,
            structured format suitable for YAML playbook generation, handling both built-in
            and external collector configurations appropriately.

        Args:
            entry (dict or None): Network management entry containing NetFlow configuration.
                Expected structure:
                {
                    "telemetry": {
                        "applicationVisibility": {
                            "collector": {
                                "collectorType": "External",
                                "address": "10.0.0.100",
                                "port": 2055
                            },
                            "enableOnWiredAccessDevices": true
                        }
                    }
                }

        Returns:
            dict: Transformed NetFlow collector configuration or empty dict:
                {
                    "collector_type": "External",
                    "ip_address": "10.0.0.100",
                    "port": 2055,
                    "enable_on_wired_access_devices": true
                }
                Returns {} if:
                - entry is None
                - entry is not a dict
                - telemetry key is missing
                - applicationVisibility is empty

        Field Mapping:
            API Field                                  -> Ansible Field
            collector.collectorType                    -> collector_type
            collector.address                          -> ip_address
            collector.port                             -> port
            enableOnWiredAccessDevices                 -> enable_on_wired_access_devices

        Examples:
            # External NetFlow collector
            extract_netflow({
                "telemetry": {
                    "applicationVisibility": {
                        "collector": {
                            "collectorType": "External",
                            "address": "10.0.0.100",
                            "port": 2055
                        },
                        "enableOnWiredAccessDevices": true
                    }
                }
            })
            -> {
                "collector_type": "External",
                "ip_address": "10.0.0.100",
                "port": 2055,
                "enable_on_wired_access_devices": true
            }

            # Built-in collector (clears IP/port)
            extract_netflow({
                "telemetry": {
                    "applicationVisibility": {
                        "collector": {
                            "collectorType": "Builtin"
                        },
                        "enableOnWiredAccessDevices": false
                    }
                }
            })
            -> {
                "collector_type": "Builtin",
                "ip_address": "",
                "port": None,
                "enable_on_wired_access_devices": false
            }
        """
        self.log(
            "Extracting NetFlow collector (Application Visibility) configuration from "
            "network management entry to transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty NetFlow configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for NetFlow extraction - expected dict, got {0}. "
                "Returning empty configuration.".format(type(entry).__name__),
                "WARNING"
            )
            return {}

        # Navigate nested structure: entry -> telemetry -> applicationVisibility
        telemetry_data = entry.get("telemetry")

        if not telemetry_data:
            self.log(
                "No 'telemetry' configuration found in entry, returning empty NetFlow "
                "configuration (site may not have telemetry configured)",
                "DEBUG"
            )
            return {}

        if not isinstance(telemetry_data, dict):
            self.log(
                "Invalid telemetry type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(telemetry_data).__name__),
                "WARNING"
            )
            return {}

        app_visibility = telemetry_data.get("applicationVisibility")

        if not app_visibility:
            self.log(
                "No 'applicationVisibility' configuration found in telemetry, "
                "returning empty NetFlow configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(app_visibility, dict):
            self.log(
                "Invalid applicationVisibility type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(app_visibility).__name__),
                "WARNING"
            )
            return {}

        self.log(
            "Found Application Visibility configuration with {0} field(s): {1}".format(
                len(app_visibility), list(app_visibility.keys())
            ),
            "DEBUG"
        )

        # Extract collector configuration
        collector = app_visibility.get("collector", {})

        if not isinstance(collector, dict):
            self.log(
                "Invalid collector type - expected dict, got {0}. Using empty dict.".format(
                    type(collector).__name__
                ),
                "WARNING"
            )
            collector = {}

        # Extract collector fields
        collector_type = collector.get("collectorType", "")
        ip_address = collector.get("address", "")
        port = collector.get("port")
        enable_wired = app_visibility.get("enableOnWiredAccessDevices", False)

        # Validate and log collector type
        if collector_type:
            self.log(
                "Extracted NetFlow collector type: '{0}'".format(collector_type),
                "DEBUG"
            )
        else:
            self.log(
                "No collector type configured (empty or missing collectorType field)",
                "DEBUG"
            )

        # Build base result structure
        result = {
            "collector_type": collector_type,
            "ip_address": ip_address,
            "port": port,
            "enable_on_wired_access_devices": enable_wired
        }

        # Special handling for Built-in collector
        if collector_type and collector_type != "External":
            self.log(
                "Built-in collector detected (type: '{0}'), clearing ip_address and "
                "port fields to prevent external collector misconfiguration".format(
                    collector_type
                ),
                "INFO"
            )
            result["ip_address"] = ""
            result["port"] = None
        else:
            # External collector - validate IP and port
            if collector_type == "External":
                if ip_address:
                    self.log(
                        "External NetFlow collector configured - IP: '{0}', Port: {1}".format(
                            ip_address, port if port else "Not configured"
                        ),
                        "INFO"
                    )
                else:
                    self.log(
                        "External collector type specified but no IP address configured",
                        "WARNING"
                    )

                if port is None or port == "":
                    self.log(
                        "External collector missing port number (will use protocol default)",
                        "WARNING"
                    )

        self.log(
            "Wired access devices NetFlow collection: {0}".format(
                "Enabled" if enable_wired else "Disabled"
            ),
            "DEBUG"
        )

        self.log(
            "Successfully extracted NetFlow collector configuration - Type: '{0}', "
            "IP: '{1}', Port: {2}, Wired: {3}".format(
                collector_type if collector_type else "Not configured",
                ip_address if ip_address and collector_type == "External" else "N/A",
                port if port and collector_type == "External" else "N/A",
                enable_wired
            ),
            "DEBUG"
        )

        return result

    def extract_snmp(self, entry):
        """
        Extract and transform SNMP trap server configuration from network management API response.

        This method extracts SNMP trap server settings from Catalyst Center network management
        API responses and transforms them into Ansible playbook-compatible format for the
        network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center SNMP trap configuration data into clean, structured
            format suitable for YAML playbook generation, handling both built-in and external
            trap server configurations appropriately.

        Args:
            entry (dict or None): Network management entry containing SNMP trap configuration.
                Expected structure:
                {
                    "telemetry": {
                        "snmpTraps": {
                            "useBuiltinTrapServer": true,
                            "externalTrapServers": ["10.0.0.50", "10.0.0.51"]
                        }
                    }
                }

        Returns:
            dict: Transformed SNMP trap server configuration or empty dict:
                {
                    "configure_dnac_ip": true,
                    "ip_addresses": ["10.0.0.50", "10.0.0.51"]
                }
                Returns {} if:
                - entry is None
                - entry is not a dict
                - telemetry key is missing
                - snmpTraps is empty

        Field Mapping:
            API Field                    -> Ansible Field
            useBuiltinTrapServer         -> configure_dnac_ip
            externalTrapServers          -> ip_addresses

        Built-in vs External Servers:
            - configure_dnac_ip (true): Use Catalyst Center built-in SNMP trap receiver
            - ip_addresses: Additional external SNMP trap servers (optional)
            - Both can be configured simultaneously (hybrid mode)

        Examples:
            # Built-in + External servers
            extract_snmp({
                "telemetry": {
                    "snmpTraps": {
                        "useBuiltinTrapServer": true,
                        "externalTrapServers": ["10.0.0.50", "10.0.0.51"]
                    }
                }
            })
            -> {
                "configure_dnac_ip": true,
                "ip_addresses": ["10.0.0.50", "10.0.0.51"]
            }

            # Only built-in server
            extract_snmp({
                "telemetry": {
                    "snmpTraps": {
                        "useBuiltinTrapServer": true,
                        "externalTrapServers": []
                    }
                }
            })
            -> {
                "configure_dnac_ip": true,
                "ip_addresses": []
            }

            # Only external servers
            extract_snmp({
                "telemetry": {
                    "snmpTraps": {
                        "useBuiltinTrapServer": false,
                        "externalTrapServers": ["10.0.0.50"]
                    }
                }
            })
            -> {
                "configure_dnac_ip": false,
                "ip_addresses": ["10.0.0.50"]
            }
        """
        self.log(
            "Extracting SNMP trap server configuration from network management entry to "
            "transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty SNMP configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for SNMP extraction - expected dict, got {0}. "
                "Returning empty configuration.".format(type(entry).__name__),
                "WARNING"
            )
            return {}

        # Navigate nested structure: entry -> telemetry -> snmpTraps
        telemetry_data = entry.get("telemetry")

        if not telemetry_data:
            self.log(
                "No 'telemetry' configuration found in entry, returning empty SNMP "
                "configuration (site may not have telemetry configured)",
                "DEBUG"
            )
            return {}

        if not isinstance(telemetry_data, dict):
            self.log(
                "Invalid telemetry type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(telemetry_data).__name__),
                "WARNING"
            )
            return {}

        snmp_traps = telemetry_data.get("snmpTraps")

        if not snmp_traps:
            self.log(
                "No 'snmpTraps' configuration found in telemetry, returning empty SNMP "
                "configuration (SNMP traps may not be configured)",
                "DEBUG"
            )
            return {}

        if not isinstance(snmp_traps, dict):
            self.log(
                "Invalid snmpTraps type - expected dict, got {0}. "
                "Returning empty configuration.".format(type(snmp_traps).__name__),
                "WARNING"
            )
            return {}

        self.log(
            "Found SNMP trap configuration with {0} field(s): {1}".format(
                len(snmp_traps), list(snmp_traps.keys())
            ),
            "DEBUG"
        )

        # Extract SNMP fields
        use_builtin = snmp_traps.get("useBuiltinTrapServer")
        external_servers = snmp_traps.get("externalTrapServers")

        # Validate use_builtin field
        if use_builtin is None:
            self.log(
                "No 'useBuiltinTrapServer' field found, defaulting to false",
                "DEBUG"
            )
            use_builtin = False

        if not isinstance(use_builtin, bool):
            self.log(
                "Invalid useBuiltinTrapServer type - expected bool, got {0}. "
                "Converting to boolean.".format(type(use_builtin).__name__),
                "WARNING"
            )
            use_builtin = bool(use_builtin)

        # Validate external_servers field
        if external_servers is None:
            self.log(
                "No 'externalTrapServers' field found, using empty list",
                "DEBUG"
            )
            external_servers = []

        if not isinstance(external_servers, list):
            self.log(
                "Invalid externalTrapServers type - expected list, got {0}. "
                "Converting to list.".format(type(external_servers).__name__),
                "WARNING"
            )
            # Attempt conversion to list
            if isinstance(external_servers, str):
                external_servers = [external_servers] if external_servers else []
            else:
                external_servers = []

        # Log extracted values
        server_count = len(external_servers)

        if use_builtin:
            self.log(
                "Built-in Catalyst Center SNMP trap server is ENABLED",
                "INFO"
            )
        else:
            self.log(
                "Built-in Catalyst Center SNMP trap server is DISABLED",
                "DEBUG"
            )

        if server_count > 0:
            self.log(
                "Extracted {0} external SNMP trap server(s): {1}".format(
                    server_count, external_servers
                ),
                "INFO"
            )
        else:
            self.log(
                "No external SNMP trap servers configured (empty list preserved for "
                "semantic meaning)",
                "DEBUG"
            )

        # Log configuration mode
        if use_builtin and server_count > 0:
            self.log(
                "Hybrid SNMP trap configuration: Built-in server + {0} external "
                "server(s)".format(server_count),
                "INFO"
            )
        elif use_builtin:
            self.log(
                "Built-in-only SNMP trap configuration (no external servers)",
                "DEBUG"
            )
        elif server_count > 0:
            self.log(
                "External-only SNMP trap configuration ({0} server(s), built-in "
                "disabled)".format(server_count),
                "DEBUG"
            )
        else:
            self.log(
                "No SNMP trap servers configured (built-in disabled, no external servers)",
                "WARNING"
            )

        # Build result structure
        result = {
            "configure_dnac_ip": use_builtin,
            "ip_addresses": external_servers
        }

        self.log(
            "Successfully extracted SNMP trap configuration - Built-in: {0}, "
            "External servers: {1}".format(
                use_builtin,
                server_count
            ),
            "DEBUG"
        )

        return result

    def extract_syslog(self, entry):
        """
        Extract and transform Syslog server configuration from network management API response.

        This method extracts Syslog server settings from Catalyst Center network management
        API responses and transforms them into Ansible playbook-compatible format for the
        network_settings_workflow_manager module.

        Purpose:
            Converts raw Catalyst Center Syslog configuration data into clean, structured
            format suitable for YAML playbook generation, handling both built-in and external
            Syslog server configurations appropriately.

        Args:
            entry (dict or None): Network management entry containing Syslog configuration.
                Expected structure:
                {
                    "telemetry": {
                        "syslogs": {
                            "useBuiltinSyslogServer": false,
                            "externalSyslogServers": ["10.10.10.10"]
                        }
                    }
                }

        Returns:
            dict: Transformed Syslog server configuration or empty dict:
                {
                    "configure_dnac_ip": false,
                    "ip_addresses": ["10.10.10.10"]
                }
                Returns {} if:
                - entry is None
                - entry is not a dict
                - telemetry key is missing
                - syslogs is empty

        Field Mapping:
            API Field                     -> Ansible Field
            useBuiltinSyslogServer        -> configure_dnac_ip
            externalSyslogServers         -> ip_addresses

        Built-in vs External Servers:
            - configure_dnac_ip (true): Use Catalyst Center built-in Syslog server
            - ip_addresses: External Syslog servers
            - Both can be configured simultaneously (hybrid mode)
        """
        self.log(
            "Extracting Syslog server configuration from network management entry to "
            "transform into Ansible playbook format",
            "DEBUG"
        )

        if entry is None:
            self.log(
                "Network management entry is None, returning empty Syslog configuration",
                "DEBUG"
            )
            return {}

        if not isinstance(entry, dict):
            self.log(
                "Invalid entry type for Syslog extraction - expected dict, got {0}. "
                "Returning empty configuration.".format(type(entry).__name__),
                "WARNING"
            )
            return {}

        # Navigate nested structure: entry -> telemetry -> syslogs
        telemetry_data = entry.get("telemetry")

        if not telemetry_data or not isinstance(telemetry_data, dict):
            self.log(
                "No valid 'telemetry' configuration found, returning empty Syslog configuration",
                "DEBUG"
            )
            return {}

        syslogs = telemetry_data.get("syslogs")

        if not syslogs or not isinstance(syslogs, dict):
            self.log(
                "No valid 'syslogs' configuration found in telemetry, returning empty Syslog "
                "configuration",
                "DEBUG"
            )
            return {}

        self.log(
            "Found Syslog configuration with {0} field(s): {1}".format(
                len(syslogs), list(syslogs.keys())
            ),
            "DEBUG"
        )

        # Extract Syslog fields
        use_builtin = syslogs.get("useBuiltinSyslogServer", False)
        external_servers = syslogs.get("externalSyslogServers", [])

        # Validate use_builtin
        if not isinstance(use_builtin, bool):
            self.log(
                "Invalid useBuiltinSyslogServer type - expected bool, got {0}. "
                "Converting to boolean.".format(type(use_builtin).__name__),
                "WARNING"
            )
            use_builtin = bool(use_builtin)

        # Validate external_servers
        if not isinstance(external_servers, list):
            self.log(
                "Invalid externalSyslogServers type - expected list, got {0}. "
                "Converting to list.".format(type(external_servers).__name__),
                "WARNING"
            )
            if isinstance(external_servers, str):
                external_servers = [external_servers] if external_servers else []
            else:
                external_servers = []

        server_count = len(external_servers)

        # Log configuration mode
        if use_builtin and server_count > 0:
            self.log(
                "Hybrid Syslog configuration: Built-in server + {0} external server(s)".format(
                    server_count
                ),
                "INFO"
            )
        elif use_builtin:
            self.log(
                "Built-in-only Syslog configuration (no external servers)",
                "DEBUG"
            )
        elif server_count > 0:
            self.log(
                "External-only Syslog configuration ({0} server(s))".format(server_count),
                "DEBUG"
            )
        else:
            self.log(
                "No Syslog servers configured (built-in disabled, no external servers)",
                "WARNING"
            )

        result = {
            "configure_dnac_ip": use_builtin,
            "ip_addresses": external_servers
        }

        self.log(
            "Successfully extracted Syslog configuration - Built-in: {0}, External servers: {1}".format(
                use_builtin, server_count
            ),
            "DEBUG"
        )

        return result

    def execute_get_bulk(self, api_family, api_function, params=None):
        """
        Executes a single non-paginated GET request for bulk data retrieval.

        This function is specifically designed for API endpoints that return all data
        in a single call without requiring pagination parameters.

        Args:
            api_family (str): Catalyst Center SDK API family identifier for routing:
                - 'network_settings': Network configuration APIs
                - 'devices': Device management APIs
                - 'sites': Site hierarchy APIs
                - 'topology': Network topology APIs

            api_function (str): Specific SDK function name within the API family:
                - 'retrieves_global_ip_address_pools': Global pool bulk retrieval
                - 'get_device_list': All devices without filters
                - 'get_site': Complete site hierarchy

    params (dict, optional): Query parameters for filtering bulk data.
        - None or {}: Retrieves all available records (default)
        - {'filter': 'value'}: API-specific filtering if supported
        - Note: Most bulk APIs ignore filter parameters
        Returns:
            list: Retrieved data records in list format:
            - [dict, dict, ...]: Multiple records from API response
            - [dict]: Single record wrapped in list for consistency
            - []: Empty list when no data found or API returns null
        Usage:
            # For bulk reserve pool retrieval without site filtering
            all_pools = self.execute_get_bulk("network_settings", "retrieves_ip_address_subpools")

            # For bulk retrieval with specific filters
            filtered_pools = self.execute_get_bulk("network_settings", "retrieves_ip_address_subpools", {"filter": "value"})
        """
        self.log("Starting bulk API execution for family '{0}', function '{1}'".format(
            api_family, api_function), "DEBUG")

        if not api_family or not isinstance(api_family, str):
            self.msg = (
                "Invalid api_family parameter for bulk retrieval - expected non-empty "
                "string, got {0}. Valid families: 'network_settings', 'devices', 'sites', "
                "'topology'. Cannot execute API call.".format(
                    type(api_family).__name__ if api_family else "None"
                )
            )
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        if not api_function or not isinstance(api_function, str):
            self.msg = (
                "Invalid api_function parameter for bulk retrieval - expected non-empty "
                "string, got {0}. Provide valid SDK function name (e.g., "
                "'retrieves_global_ip_address_pools'). Cannot execute API call.".format(
                    type(api_function).__name__ if api_function else "None"
                )
            )
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

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
        Retrieve and filter reserve IP pools from Catalyst Center with intelligent optimization.

        This method implements an optimized retrieval strategy for reserve pools that
        automatically chooses between bulk API calls (single request) and site-specific
        queries based on filter requirements, significantly improving performance for
        brownfield network settings discovery.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving reserve pools.
            filters (dict): A dictionary containing global_filters and component_specific_filters.
        Returns:
            dict: A dictionary containing the modified details of reserve pools.
        """
        self.log(
            "Starting reserve IP pool retrieval with intelligent optimization strategy "
            "that automatically selects bulk (single API call) or site-specific (multiple "
            "API calls) approach based on filter requirements",
            "DEBUG"
        )

        self.log(
            "Network element configuration: family='{0}', function='{1}'".format(
                network_element.get("api_family"), network_element.get("api_function")
            ),
            "DEBUG"
        )

        global_filters = filters.get("global_filters", {})
        component_specific_filters = filters.get("component_specific_filters", {}).get(
            "reserve_pool_details", []
        )

        self.log(
            "Global filters configuration: {0}".format(global_filters),
            "DEBUG"
        )
        self.log(
            "Component-specific filters ({0} filter object(s)): {1}".format(
                len(component_specific_filters), component_specific_filters
            ),
            "DEBUG"
        )

        final_reserve_pools = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        # === STEP 1: Determine Retrieval Strategy ===
        self.log(
            "STEP 1: Analyzing filters to determine optimal retrieval strategy "
            "(bulk vs. site-specific)",
            "INFO"
        )

        site_name_list = global_filters.get("site_name_list", [])
        has_site_specific_filters = site_name_list or any(
            filter_param.get("site_name") or filter_param.get("site_hierarchy")
            for filter_param in component_specific_filters
        )

        self.log(
            "Filter analysis result: site_name_list={0}, has_site_specific_filters={1}".format(
                len(site_name_list), has_site_specific_filters
            ),
            "DEBUG"
        )

        # === OPTIMIZATION PATH 1: Bulk Retrieval (No Site Filters) ===
        if not has_site_specific_filters:
            self.log(
                "OPTIMIZATION: No site-specific filters detected, using bulk retrieval "
                "strategy (single API call for all pools, ~90% faster)",
                "INFO"
            )

            try:
                # Execute single bulk API call to retrieve all reserve pools
                self.log(
                    "Executing bulk API call: family='{0}', function='{1}' (no siteId parameter)".format(
                        api_family, api_function
                    ),
                    "INFO"
                )

                all_reserve_pools = self.execute_get_bulk(api_family, api_function)

                self.log(
                    "Bulk API call successful: Retrieved {0} total reserve pools in single request".format(
                        len(all_reserve_pools)
                    ),
                    "INFO"
                )

                # Log sample pool details for debugging (first 3 pools)
                for i, pool in enumerate(all_reserve_pools[:3], start=1):
                    self.log(
                        "Sample pool {0}/{1}: name='{2}', site='{3}', type='{4}', id='{5}'".format(
                            i,
                            len(all_reserve_pools),
                            pool.get("groupName", "N/A"),
                            pool.get("siteName", "N/A"),
                            pool.get("type", "N/A"),
                            pool.get("id", "N/A")
                        ),
                        "DEBUG"
                    )

                # === STEP 2: Apply Global Filters (if present) ===
                filtered_pools = all_reserve_pools
                pool_name_list = global_filters.get("pool_name_list", [])
                pool_type_list = global_filters.get("pool_type_list", [])

                if pool_name_list or pool_type_list:
                    self.log(
                        "STEP 2: Applying global filters to {0} pools: pool_names={1}, pool_types={2}".format(
                            len(all_reserve_pools),
                            pool_name_list or "None",
                            pool_type_list or "None"
                        ),
                        "INFO"
                    )

                    filtered_pools = []
                    filtered_count_by_name = 0
                    filtered_count_by_type = 0

                    for pool in all_reserve_pools:
                        pool_name = pool.get("groupName")
                        pool_type = pool.get("type")

                        # Check pool name filter (if specified)
                        if pool_name_list and pool_name not in pool_name_list:
                            self.log(
                                "Pool '{0}' filtered out by pool_name_list (not in {1})".format(
                                    pool_name, pool_name_list
                                ),
                                "DEBUG"
                            )
                            filtered_count_by_name += 1
                            continue

                        # Check pool type filter (if specified)
                        if pool_type_list and pool_type not in pool_type_list:
                            self.log(
                                "Pool '{0}' (type='{1}') filtered out by pool_type_list (not in {2})".format(
                                    pool_name, pool_type, pool_type_list
                                ),
                                "DEBUG"
                            )
                            filtered_count_by_type += 1
                            continue

                        # Pool passed all global filters
                        filtered_pools.append(pool)

                    self.log(
                        "Global filter results: {0} pools passed, {1} filtered by name, "
                        "{2} filtered by type (original: {3})".format(
                            len(filtered_pools),
                            filtered_count_by_name,
                            filtered_count_by_type,
                            len(all_reserve_pools)
                        ),
                        "INFO"
                    )
                else:
                    self.log(
                        "STEP 2: No global filters specified, skipping global filter application",
                        "DEBUG"
                    )

            # === STEP 3: Apply Component-Specific Filters ===
                if component_specific_filters:
                    self.log(
                        "STEP 3: Applying component-specific filters to {0} pools".format(
                            len(filtered_pools)
                        ),
                        "INFO"
                    )

                    final_filtered_pools = []
                    filtered_count = 0

                    for filter_param in component_specific_filters:
                        # Skip site-specific filters (shouldn't occur in bulk path)
                        if filter_param.get("site_name"):
                            self.log(
                                "Unexpected site_name filter in bulk retrieval path, skipping: {0}".format(
                                    filter_param.get("site_name")
                                ),
                                "WARNING"
                            )
                            continue

                        filter_pool_name = filter_param.get("pool_name")
                        filter_pool_type = filter_param.get("pool_type")

                        self.log(
                            "Processing component filter: pool_name={0}, pool_type={1}".format(
                                filter_pool_name or "None", filter_pool_type or "None"
                            ),
                            "DEBUG"
                        )

                        for pool in filtered_pools:
                            matches_filter = True
                            pool_name = pool.get("groupName")
                            pool_type = pool.get("type")

                            # Check pool name filter
                            if filter_pool_name:
                                if pool_name != filter_pool_name:
                                    matches_filter = False
                                    self.log(
                                        "Pool '{0}' does not match component filter pool_name='{1}'".format(
                                            pool_name, filter_pool_name
                                        ),
                                        "DEBUG"
                                    )
                                    continue

                            # Check pool type filter
                            if filter_pool_type:
                                if pool_type != filter_pool_type:
                                    matches_filter = False
                                    self.log(
                                        "Pool '{0}' (type='{1}') does not match component filter pool_type='{2}'".format(
                                            pool_name, pool_type, filter_pool_type
                                        ),
                                        "DEBUG"
                                    )
                                    continue

                            # Pool matched all criteria
                            if matches_filter:
                                final_filtered_pools.append(pool)
                                self.log(
                                    "Pool '{0}' matched component filter criteria".format(pool_name),
                                    "DEBUG"
                                )

                    filtered_count = len(filtered_pools) - len(final_filtered_pools)
                    filtered_pools = final_filtered_pools

                    self.log(
                        "Component filter results: {0} pools passed, {1} filtered out".format(
                            len(filtered_pools), filtered_count
                        ),
                        "INFO"
                    )
                else:
                    self.log(
                        "STEP 3: No component-specific filters specified, skipping",
                        "DEBUG"
                    )

                final_reserve_pools = filtered_pools

                # Track success for bulk operation
                self.add_success("All Sites", "reserve_pool_details", {
                    "pools_processed": len(final_reserve_pools),
                    "optimization": "bulk_retrieval",
                    "api_calls": 1
                })

            except Exception as e:
                self.log(
                    "Bulk reserve pool retrieval failed: {0}".format(str(e)),
                    "ERROR"
                )
                self.add_failure("All Sites", "reserve_pool_details", {
                    "error_type": "api_error",
                    "error_message": str(e),
                    "error_code": "BULK_API_CALL_FAILED"
                })
                final_reserve_pools = []

        # === STANDARD PATH 2: Site-Specific Retrieval ===
        else:
            self.log(
                "STANDARD: Site-specific filters detected, using site-by-site retrieval "
                "strategy (multiple API calls, one per site)",
                "INFO"
            )

            # === STEP 1: Build Target Site List ===
            self.log(
                "STEP 1: Building target site list from global and component-specific filters",
                "INFO"
            )
            # Process site-based filtering
            target_sites = []

            # Build site ID to name mapping (cached)
            if not hasattr(self, 'site_id_name_dict'):
                self.log("Building site ID to name mapping cache (first-time operation)", "DEBUG")
                self.site_id_name_dict = self.get_site_id_name_mapping()
                self.log(
                    "Site mapping cache created with {0} sites".format(len(self.site_id_name_dict)),
                    "DEBUG"
                )

            # Create reverse mapping (name -> ID)
            site_name_to_id_dict = {v: k for k, v in self.site_id_name_dict.items()}

            # Process global site_name_list
            if site_name_list:
                self.log(
                    "Processing global site_name_list with {0} site(s): {1}".format(
                        len(site_name_list), site_name_list
                    ),
                    "INFO"
                )

                for site_name in site_name_list:
                    site_id = site_name_to_id_dict.get(site_name)

                    if site_id:
                        target_sites.append({"site_name": site_name, "site_id": site_id})
                        self.log(
                            "Added target site from global filter: '{0}' (ID: {1})".format(
                                site_name, site_id
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "Site '{0}' not found in Catalyst Center (may have been deleted or "
                            "user lacks permissions)".format(site_name),
                            "WARNING"
                        )
                        self.add_failure(site_name, "reserve_pool_details", {
                            "error_type": "site_not_found",
                            "error_message": "Site not found or not accessible in Catalyst Center",
                            "error_code": "SITE_NOT_FOUND"
                        })

            # Process component-specific site filters
            if not target_sites and component_specific_filters:
                self.log(
                    "No global site filters, extracting sites from component-specific filters",
                    "INFO"
                )

                for filter_param in component_specific_filters:
                    # Handle site_name filter
                    filter_site_name = filter_param.get("site_name")
                    if filter_site_name:
                        site_id = site_name_to_id_dict.get(filter_site_name)

                        if site_id:
                            # Avoid duplicates
                            if not any(s["site_name"] == filter_site_name for s in target_sites):
                                target_sites.append({"site_name": filter_site_name, "site_id": site_id})
                                self.log(
                                    "Added target site from component filter: '{0}' (ID: {1})".format(
                                        filter_site_name, site_id
                                    ),
                                    "DEBUG"
                                )
                        else:
                            self.log(
                                "Site '{0}' from component filter not found in Catalyst Center".format(
                                    filter_site_name
                                ),
                                "WARNING"
                            )

                    # Handle site_hierarchy filter (expands to all child sites)
                    filter_site_hierarchy = filter_param.get("site_hierarchy")
                    if filter_site_hierarchy:
                        self.log(
                            "Processing site_hierarchy filter: '{0}' (will expand to all child sites)".format(
                                filter_site_hierarchy
                            ),
                            "INFO"
                        )

                        child_sites = self.get_child_sites_from_hierarchy(filter_site_hierarchy)

                        self.log(
                            "Site hierarchy '{0}' expanded to {1} child site(s)".format(
                                filter_site_hierarchy, len(child_sites)
                            ),
                            "INFO"
                        )

                        for child_site in child_sites:
                            # Avoid duplicates
                            if not any(s["site_name"] == child_site["site_name"] for s in target_sites):
                                target_sites.append(child_site)
                                self.log(
                                    "Added child site from hierarchy: '{0}' (ID: {1})".format(
                                        child_site["site_name"], child_site["site_id"]
                                    ),
                                    "DEBUG"
                                )

            self.log(
                "Target site list finalized: {0} site(s) to process".format(len(target_sites)),
                "INFO"
            )

            # === STEP 2: Process Each Target Site ===
            for site_idx, site_info in enumerate(target_sites, start=1):
                site_name = site_info["site_name"]
                site_id = site_info["site_id"]

                self.log(
                    "STEP 2: Processing site {0}/{1}: '{2}' (ID: {3})".format(
                        site_idx, len(target_sites), site_name, site_id
                    ),
                    "INFO"
                )
                try:
                    # Base parameters for API call
                    params = {"siteId": site_id}
                    self.log(
                        "Executing API call for site '{0}': family='{1}', function='{2}', params={3}".format(
                            site_name, api_family, api_function, params
                        ),
                        "DEBUG"
                    )

                    # Execute API call to get reserve pools for this site
                    reserve_pool_details = self.execute_get_with_pagination(api_family, api_function, params)
                    self.log("Retrieved {0} reserve pools for site {1}".format(
                        len(reserve_pool_details), site_name), "INFO")

                    for i, pool in enumerate(reserve_pool_details[:3], start=1):
                        self.log(
                            "  Sample pool {0}/{1} for site '{2}': name='{3}', type='{4}'".format(
                                i, len(reserve_pool_details), site_name,
                                pool.get("groupName", "N/A"), pool.get("type", "N/A")
                            ),
                            "DEBUG"
                        )

                    # === STEP 3: Apply Component-Specific Filters for This Site ===
                    if component_specific_filters:
                        self.log(
                            "STEP 3: Applying component-specific filters to {0} pools from site '{1}'".format(
                                len(reserve_pool_details), site_name
                            ),
                            "DEBUG"
                        )

                        filtered_pools = []
                    if component_specific_filters:
                        filtered_pools = []
                        for filter_param in component_specific_filters:
                            # Check if filter applies to this site
                            filter_site_name = filter_param.get("site_name")
                            filter_site_hierarchy = filter_param.get("site_hierarchy")

                            # Skip if this filter is for a different specific site
                            if filter_site_name and filter_site_name != site_name:
                                self.log(
                                    "Skipping component filter (site_name='{0}') - does not match "
                                    "current site '{1}'".format(filter_site_name, site_name),
                                    "DEBUG"
                                )
                                continue

                            # Check if this site matches the hierarchy filter
                            if filter_site_hierarchy and not site_name.startswith(filter_site_hierarchy):
                                self.log(
                                    "Skipping component filter (site_hierarchy='{0}') - site '{1}' "
                                    "not under hierarchy".format(filter_site_hierarchy, site_name),
                                    "DEBUG"
                                )
                                continue

                            # Apply pool-level filters
                            filter_pool_name = filter_param.get("pool_name")
                            filter_pool_type = filter_param.get("pool_type")

                            # Apply other filters
                            for pool in reserve_pool_details:
                                matches_filter = True
                                pool_name = pool.get("groupName")
                                pool_type = pool.get("type")

                                # Check pool name filter
                                if filter_pool_name:
                                    if pool_name != filter_pool_name:
                                        matches_filter = False
                                        continue

                                # Check pool type filter
                                if filter_pool_type:
                                    if pool_type != filter_pool_type:
                                        matches_filter = False
                                        continue

                                # Pool matched all criteria
                                if matches_filter:
                                    filtered_pools.append(pool)

                        # Use filtered results if filters were applied
                        if filtered_pools:
                            self.log(
                                "Component filters applied: {0} pools passed (from {1} original)".format(
                                    len(filtered_pools), len(reserve_pool_details)
                                ),
                                "DEBUG"
                            )
                            reserve_pool_details = filtered_pools
                        elif component_specific_filters:
                            # If filters were specified but none matched, empty the list
                            self.log(
                                "Component filters applied: 0 pools matched criteria (all {0} filtered out)".format(
                                    len(reserve_pool_details)
                                ),
                                "DEBUG"
                            )
                            reserve_pool_details = []

                    # === STEP 4: Apply Global Filters ===
                    if global_filters.get("pool_name_list") or global_filters.get("pool_type_list"):
                        self.log(
                            "STEP 4: Applying global filters to {0} pools from site '{1}'".format(
                                len(reserve_pool_details), site_name
                            ),
                            "DEBUG"
                        )

                        filtered_pools = []
                        pool_name_list = global_filters.get("pool_name_list", [])
                        pool_type_list = global_filters.get("pool_type_list", [])

                        for pool in reserve_pool_details:
                            pool_name = pool.get("groupName")
                            pool_type = pool.get("type")

                            # Check pool name filter
                            if pool_name_list and pool_name not in pool_name_list:
                                continue

                            # Check pool type filter
                            if pool_type_list and pool_type not in pool_type_list:
                                continue

                            filtered_pools.append(pool)

                        self.log(
                            "Global filters applied: {0} pools passed (from {1} original)".format(
                                len(filtered_pools), len(reserve_pool_details)
                            ),
                            "DEBUG"
                        )
                        reserve_pool_details = filtered_pools
                        self.log("Applied global filters, remaining pools: {0}".format(len(filtered_pools)), "DEBUG")

                    # Add to final list
                    final_reserve_pools.extend(reserve_pool_details)

                    # Track success for this site
                    self.add_success(site_name, "reserve_pool_details", {
                        "pools_processed": len(reserve_pool_details)
                    })
                    self.log(
                        "Site '{0}' processing complete: {1} pools added to final list (total: {2})".format(
                            site_name, len(reserve_pool_details), len(final_reserve_pools)
                        ),
                        "INFO"
                    )

                except Exception as e:
                    self.log("Error retrieving reserve pools for site {0}: {1}".format(site_name, str(e)), "ERROR")
                    self.add_failure(site_name, "reserve_pool_details", {
                        "error_type": "api_error",
                        "error_message": str(e),
                        "error_code": "API_CALL_FAILED"
                    })
                    continue

        # === STEP 5: Deduplication ===
        self.log(
            "STEP 5: Performing deduplication on {0} pools to remove duplicates".format(
                len(final_reserve_pools)
            ),
            "INFO"
        )
        unique_pools = []
        seen_pools = set()
        duplicate_count = 0

        for pool in final_reserve_pools:
            # Create unique identifier
            pool_id = pool.get("id")
            pool_name = pool.get("name")

            if pool_id:
                # Use pool ID as primary identifier (most reliable)
                pool_identifier = pool_id
            else:
                # Fallback: Use combination of site ID, pool name, and subnet
                pool_identifier = "{0}_{1}_{2}".format(
                    pool.get("siteId", ""),
                    pool_name or pool.get("groupName", ""),
                    pool.get("ipV4AddressSpace", {}).get("subnet", "")
                )

            if pool_identifier not in seen_pools:
                seen_pools.add(pool_identifier)
                unique_pools.append(pool)
            else:
                duplicate_count += 1
                self.log(
                    "Duplicate pool detected and removed: name='{0}', identifier='{1}'".format(
                        pool_name or pool.get("groupName", "Unknown"), pool_identifier
                    ),
                    "DEBUG"
                )

        self.log(
            "Deduplication complete: {0} unique pools retained, {1} duplicates removed".format(
                len(unique_pools), duplicate_count
            ),
            "INFO"
        )

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
            self.log(
                "No reserve pools found matching the specified filter criteria. This may indicate: "
                "(1) No pools configured in Catalyst Center, (2) Filters too restrictive, "
                "(3) User lacks permissions to view pools",
                "WARNING"
            )
            return {
                "reserve_pool_details": [],
                "operation_summary": self.get_operation_summary()
            }

        # === STEP 6: Apply Reverse Mapping Transformation ===
        self.log(
            "STEP 6: Applying reverse mapping transformation to {0} pools for YAML output".format(
                len(final_reserve_pools)
            ),
            "INFO"
        )
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
            self.log(
                "✓ Transformation integrity verified: Each of the {0} pools has its own "
                "individual YAML configuration entry".format(len(pools_details)),
                "INFO"
            )
        else:
            self.log(
                "⚠ Transformation count mismatch: input={0}, output={1} (investigate mapping logic)".format(
                    len(final_reserve_pools), len(pools_details)
                ),
                "WARNING"
            )
            self.log("✓ SUCCESS: Each of the {0} pools has its own individual configuration entry".format(len(pools_details)), "INFO")

        # Return in the correct format - note the structure difference from global pools
        if pools_details:
            sample_pool = pools_details[0]
            self.log(
                "Sample transformed pool: name='{0}', site='{1}', has {2} field(s)".format(
                    sample_pool.get('name', 'Unknown'),
                    sample_pool.get('site_name', 'Unknown'),
                    len(sample_pool)
                ),
                "DEBUG"
            )

        self.log(
            "Reserve pool retrieval complete: {0} pools processed, {1} configurations generated, "
            "operation_summary available".format(
                len(final_reserve_pools), len(pools_details)
            ),
            "INFO"
        )

        return {
            "reserve_pool_details": pools_details,
            "operation_summary": self.get_operation_summary()
        }

    def get_aaa_settings_for_site(self, site_name, site_id):
        """Retrieve AAA (Authentication, Authorization, and Accounting) settings for a specific site.

        This method retrieves both Network AAA and Client/Endpoint AAA configurations from
        Catalyst Center for a specified site. AAA settings control device authentication
        (network AAA) and user/endpoint authentication (client AAA) using RADIUS or TACACS+.

        Purpose:
            Extracts dual AAA configurations from Catalyst Center to enable brownfield
            network settings discovery for network_settings_workflow_manager module.
            Supports both ISE-integrated and standalone AAA server deployments.

        Args:
            site_name (str): Full hierarchical site name for logging and error context.
                Example: "Global/USA/SAN-FRANCISCO/SF_BLD1"
                Used for human-readable logging and error messages.

            site_id (str): Unique site identifier (UUID) for API calls.
                Example: "3e1f7e42-9c4c-4d3f-8a2e-1b5c6d7e8f9a"
                Required parameter for retrieve_aaa_settings_for_a_site API call.

        Returns:
            tuple: (network_aaa, client_and_endpoint_aaa) containing:
                - network_aaa (dict or None): Network device AAA configuration:
                    {
                        "primaryServerIp": "10.0.0.50",
                        "secondaryServerIp": "10.0.0.51",
                        "protocol": "RADIUS",
                        "serverType": "ISE",
                        "pan": "ise-pan.example.com",
                        "sharedSecret": "***"
                    }
                - client_and_endpoint_aaa (dict or None): Client/endpoint AAA configuration:
                    {
                        "primaryServerIp": "10.0.0.50",
                        "secondaryServerIp": "10.0.0.51",
                        "protocol": "RADIUS",
                        "serverType": "ISE",
                        "pan": "ise-pan.example.com",
                        "sharedSecret": "***"
                    }

                Returns (None, None) if:
                - Site not found or inaccessible
                - No AAA settings configured for site
                - API call fails
                - Authentication/authorization errors
        """
        self.log(
            "Starting AAA settings retrieval for site '{0}' (ID: {1}) to extract "
            "both network AAA and client/endpoint AAA configurations".format(
                site_name, site_id
            ),
            "DEBUG"
        )

        if not site_name or not isinstance(site_name, str):
            self.log(
                "Invalid site_name parameter for AAA retrieval - expected non-empty "
                "string, got {0}. Cannot proceed with API call.".format(
                    type(site_name).__name__ if site_name else "None"
                ),
                "ERROR"
            )
            return None, None

        if not site_id or not isinstance(site_id, str):
            self.log(
                "Invalid site_id parameter for AAA retrieval - expected non-empty "
                "string (UUID), got {0}. Cannot proceed with API call.".format(
                    type(site_id).__name__ if site_id else "None"
                ),
                "ERROR"
            )
            return None, None

        self.log(
            "Executing API call to retrieve AAA settings using network_settings family, "
            "retrieve_aaa_settings_for_a_site function with site ID: {0}".format(site_id),
            "INFO"
        )

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

            self.log(
                "Received API response successfully for site '{0}', processing response data".format(
                    site_name
                ),
                "DEBUG"
            )

            if not isinstance(aaa_network_response, dict):
                self.log(
                    "Unexpected response type from AAA API - expected dict, got {0}. "
                    "Returning empty AAA configuration.".format(
                        type(aaa_network_response).__name__
                    ),
                    "WARNING"
                )
                return None, None

            # Extract AAA network and client/endpoint settings
            response = aaa_network_response.get("response", {})
            if response is None:
                self.log(
                    "No 'response' key found in API result for site '{0}'. This may indicate: "
                    "(1) Site has no AAA settings configured, (2) Site inherits AAA from parent, "
                    "(3) API response format changed. Returning empty AAA configuration.".format(
                        site_name
                    ),
                    "WARNING"
                )
                return None, None

            if not isinstance(response, dict):
                self.log(
                    "Unexpected 'response' type in API result - expected dict, got {0}. "
                    "Returning empty AAA configuration.".format(type(response).__name__),
                    "WARNING"
                )
                return None, None

            self.log(
                "Response data validated successfully, contains {0} top-level field(s): {1}".format(
                    len(response), list(response.keys())
                ),
                "DEBUG"
            )
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

            found_components = []
            if network_aaa is not None:
                found_components.append("network_aaa")
            if client_and_endpoint_aaa is not None:
                found_components.append("client_and_endpoint_aaa")

            self.log(
                "AAA settings extraction successful for site '{0}': Found {1} component(s): {2}".format(
                    site_name, len(found_components), found_components
                ),
                "INFO"
            )
        except Exception as e:
            error_str = str(e).lower()

            # Provide specific error context based on error type
            if "unauthorized" in error_str or "401" in error_str:
                self.msg = (
                    "Authentication failed while retrieving AAA settings for site '{0}' "
                    "(ID: {1}). Verify Catalyst Center credentials (username/password) "
                    "are correct and user has network-admin privileges. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "forbidden" in error_str or "403" in error_str:
                self.msg = (
                    "Authorization failed while retrieving AAA settings for site '{0}' "
                    "(ID: {1}). User lacks permissions to view AAA settings. Required role: "
                    "NETWORK-ADMIN-ROLE or SUPER-ADMIN-ROLE. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "not found" in error_str or "404" in error_str:
                self.msg = (
                    "Site '{0}' (ID: {1}) not found in Catalyst Center. Site may have been "
                    "deleted or ID is invalid. Verify site exists and ID is correct. "
                    "Error: {2}".format(site_name, site_id, str(e))
                )
            elif "timeout" in error_str or "timed out" in error_str:
                self.msg = (
                    "API call timeout while retrieving AAA settings for site '{0}' "
                    "(ID: {1}). Catalyst Center may be overloaded or network latency is high. "
                    "Retry operation or increase timeout value. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "connection" in error_str:
                self.msg = (
                    "Network connection error while retrieving AAA settings for site '{0}' "
                    "(ID: {1}). Verify network connectivity to Catalyst Center ({2}) and "
                    "DNS resolution. Error: {3}".format(
                        site_name, site_id, self.dnac_host, str(e)
                    )
                )
            else:
                # Generic error message for unknown errors
                self.msg = (
                    "Exception occurred while retrieving AAA settings for site '{0}' "
                    "(ID: {1}). This may indicate: (1) API response format changed, "
                    "(2) Catalyst Center version incompatibility, (3) Temporary API error. "
                    "Error: {2}".format(site_name, site_id, str(e))
                )

            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return network_aaa, client_and_endpoint_aaa

    def get_dhcp_settings_for_site(self, site_name, site_id):
        """
        Retrieve DHCP (Dynamic Host Configuration Protocol) server settings for a specific site.

        This method retrieves DHCP server configuration from Catalyst Center for a specified
        site, enabling brownfield network settings discovery for the network_settings_workflow_manager
        module. DHCP settings control automatic IP address assignment for network devices.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve DHCP settings for.
            site_id (str) - The ID of the site to retrieve DHCP settings for.

        Returns:
            dhcp_details (dict) - DHCP settings details for the specified site.
        """
        self.log(
            "Starting DHCP server settings retrieval for site '{0}' (ID: {1}) to extract "
            "DHCP configuration for brownfield network settings discovery".format(
                site_name, site_id
            ),
            "DEBUG"
        )

        if not site_name or not isinstance(site_name, str):
            self.log(
                "Invalid site_name parameter for DHCP retrieval - expected non-empty "
                "string, got {0}. Cannot proceed with API call.".format(
                    type(site_name).__name__ if site_name else "None"
                ),
                "ERROR"
            )
            return None

        if not site_id or not isinstance(site_id, str):
            self.log(
                "Invalid site_id parameter for DHCP retrieval - expected non-empty "
                "string (UUID), got {0}. Cannot proceed with API call.".format(
                    type(site_id).__name__ if site_id else "None"
                ),
                "ERROR"
            )
            return None

        self.log(
            "Executing API call to retrieve DHCP settings using network_settings family, "
            "retrieve_d_h_c_p_settings_for_a_site function with site ID: {0}".format(site_id),
            "INFO"
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

            if not isinstance(dhcp_response, dict):
                self.log(
                    "Unexpected response type from DHCP API - expected dict, got {0}. "
                    "Returning empty DHCP configuration.".format(
                        type(dhcp_response).__name__
                    ),
                    "WARNING"
                )
                return None

            # Extract response data
            response = dhcp_response.get("response")

            if response is None:
                self.log(
                    "No 'response' key found in API result for site '{0}'. This may indicate: "
                    "(1) Site has no DHCP settings configured, (2) Site inherits DHCP from parent, "
                    "(3) API response format changed. Returning empty DHCP configuration.".format(
                        site_name
                    ),
                    "WARNING"
                )
                return None

            if not isinstance(response, dict):
                self.log(
                    "Unexpected 'response' type in API result - expected dict, got {0}. "
                    "Returning empty DHCP configuration.".format(type(response).__name__),
                    "WARNING"
                )
                return None

            self.log(
                "Response data validated successfully, contains {0} top-level field(s): {1}".format(
                    len(response), list(response.keys())
                ),
                "DEBUG"
            )

            # Extract DHCP details
            dhcp_details = response.get("dhcp")

            # Validate and log DHCP details
            if dhcp_details is None:
                self.log(
                    "No DHCP settings (dhcp field) found for site '{0}' (ID: {1}). "
                    "This may indicate: (1) No DHCP configured for this site, "
                    "(2) Site inherits DHCP from parent site, (3) User lacks permissions.".format(
                        site_name, site_id
                    ),
                    "WARNING"
                )
                return None

            if not isinstance(dhcp_details, dict):
                self.log(
                    "Invalid dhcp_details type - expected dict, got {0}. "
                    "Returning None.".format(type(dhcp_details).__name__),
                    "WARNING"
                )
                return None

            self.log(
                "DHCP configuration found with {0} field(s): {1}".format(
                    len(dhcp_details), list(dhcp_details.keys())
                ),
                "DEBUG"
            )

            # Extract and validate DHCP servers
            dhcp_servers = dhcp_details.get("servers")

            if dhcp_servers is None:
                self.log(
                    "No DHCP servers field found in DHCP configuration for site '{0}'. "
                    "Initializing empty server list.".format(site_name),
                    "DEBUG"
                )
                dhcp_details["servers"] = []
            elif not isinstance(dhcp_servers, list):
                self.log(
                    "Invalid DHCP servers type - expected list, got {0}. "
                    "Converting to list.".format(type(dhcp_servers).__name__),
                    "WARNING"
                )
                # Attempt conversion to list
                if isinstance(dhcp_servers, str):
                    dhcp_details["servers"] = [dhcp_servers] if dhcp_servers else []
                    self.log(
                        "Converted string DHCP server '{0}' to list".format(dhcp_servers),
                        "DEBUG"
                    )
                else:
                    dhcp_details["servers"] = []
                    self.log(
                        "Could not convert DHCP servers to list, using empty list",
                        "WARNING"
                    )
            else:
                # Validate server count and format
                server_count = len(dhcp_servers)
                if server_count > 0:
                    self.log(
                        "Found {0} DHCP server(s) for site '{1}': {2}".format(
                            server_count, site_name, dhcp_servers
                        ),
                        "INFO"
                    )

                    # Log individual server details
                    for idx, server in enumerate(dhcp_servers, start=1):
                        if not server or not isinstance(server, str):
                            self.log(
                                "DHCP server {0}/{1} has invalid format: {2} (type: {3})".format(
                                    idx, server_count, server, type(server).__name__
                                ),
                                "WARNING"
                            )
                        else:
                            # Detect IP version for logging
                            if ":" in server:
                                server_type = "IPv6 address"
                            elif "." in server:
                                server_type = "IPv4 address"
                            else:
                                server_type = "unknown format"

                            self.log(
                                "DHCP server {0}/{1}: '{2}' ({3})".format(
                                    idx, server_count, server, server_type
                                ),
                                "DEBUG"
                            )
                else:
                    self.log(
                        "Empty DHCP server list for site '{0}' - no DHCP servers configured "
                        "(site may inherit from parent or use defaults)".format(site_name),
                        "DEBUG"
                    )
            self.log(
                "Successfully retrieved DHCP settings for site '{0}' (ID: {1}): {2} server(s) configured".format(
                    site_name,
                    site_id,
                    len(dhcp_details.get("servers", []))
                ),
                "INFO"
            )

            return dhcp_details
        except AttributeError as e:
            self.msg = (
                "Invalid API family or function name for DHCP retrieval - SDK does not "
                "recognize family '{0}' or function '{1}'. Verify SDK version compatibility. "
                "Error: {2}".format("network_settings", "retrieve_d_h_c_p_settings_for_a_site", str(e))
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        except Exception as e:
            error_str = str(e).lower()

            # Provide specific error context based on error type
            if "unauthorized" in error_str or "401" in error_str:
                self.msg = (
                    "Authentication failed while retrieving DHCP settings for site '{0}' "
                    "(ID: {1}). Verify Catalyst Center credentials (username/password) "
                    "are correct and user has network-admin privileges. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "forbidden" in error_str or "403" in error_str:
                self.msg = (
                    "Authorization failed while retrieving DHCP settings for site '{0}' "
                    "(ID: {1}). User lacks permissions to view DHCP settings. Required role: "
                    "NETWORK-ADMIN-ROLE or SUPER-ADMIN-ROLE. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "not found" in error_str or "404" in error_str:
                self.msg = (
                    "Site '{0}' (ID: {1}) not found in Catalyst Center. Site may have been "
                    "deleted or ID is invalid. Verify site exists and ID is correct. "
                    "Error: {2}".format(site_name, site_id, str(e))
                )
            elif "timeout" in error_str or "timed out" in error_str:
                self.msg = (
                    "API call timeout while retrieving DHCP settings for site '{0}' "
                    "(ID: {1}). Catalyst Center may be overloaded or network latency is high. "
                    "Retry operation or increase timeout value. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "connection" in error_str:
                self.msg = (
                    "Network connection error while retrieving DHCP settings for site '{0}' "
                    "(ID: {1}). Verify network connectivity to Catalyst Center and "
                    "DNS resolution. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            else:
                # Generic error message for unknown errors
                self.msg = (
                    "Exception occurred while retrieving DHCP settings for site '{0}' "
                    "(ID: {1}). This may indicate: (1) API response format changed, "
                    "(2) Catalyst Center version incompatibility, (3) Temporary API error. "
                    "Error: {2}".format(site_name, site_id, str(e))
                )

            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

    def get_dns_settings_for_site(self, site_name, site_id):
        """
        Retrieve DNS (Domain Name System) server settings for a specific site.

        Extracts DNS server configuration from Catalyst Center for a specified
        site, enabling brownfield network settings discovery for the
        network_settings_workflow_manager module. DNS settings control domain
        name resolution and server addressing for network operations.
        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve DNS settings for.
            site_id (str): The ID of the site to retrieve DNS settings for.

        Returns:
            dns_details (dict): DNS settings details for the specified site.
        """
        self.log(
            "Starting DNS server settings retrieval for site '{0}' (ID: {1}) to "
            "extract DNS configuration for brownfield network settings discovery"
            .format(site_name, site_id),
            "DEBUG"
        )

        if not site_name or not isinstance(site_name, str):
            self.log(
                "Invalid site_name parameter for DNS retrieval - expected "
                "non-empty string, got {0}. Cannot proceed with API call.".format(
                    type(site_name).__name__ if site_name else "None"
                ),
                "ERROR"
            )
            return None

        if not site_id or not isinstance(site_id, str):
            self.log(
                "Invalid site_id parameter for DNS retrieval - expected non-empty "
                "string (UUID), got {0}. Cannot proceed with API call.".format(
                    type(site_id).__name__ if site_id else "None"
                ),
                "ERROR"
            )
            return None

        self.log(
            "Executing API call to retrieve DNS settings using network_settings "
            "family, retrieve_d_n_s_settings_for_a_site function with site ID: {0}"
            .format(site_id),
            "INFO"
        )

        try:
            dns_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_d_n_s_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )
            # Extract DNS details
            self.log(
                "API call completed successfully for site '{0}', processing "
                "response data".format(site_name),
                "DEBUG"
            )

            # Validate response structure
            if not isinstance(dns_response, dict):
                self.log(
                    "Unexpected response type from DNS API - expected dict, got "
                    "{0}. Returning empty DNS configuration.".format(
                        type(dns_response).__name__
                    ),
                    "WARNING"
                )
                return None

            # Extract response data
            response = dns_response.get("response")

            if response is None:
                self.log(
                    "No 'response' key found in API result for site '{0}'. This "
                    "may indicate: (1) Site has no DNS settings configured, "
                    "(2) Site inherits DNS from parent, (3) API response format "
                    "changed. Returning empty DNS configuration.".format(
                        site_name
                    ),
                    "WARNING"
                )
                return None

            if not isinstance(response, dict):
                self.log(
                    "Unexpected 'response' type in API result - expected dict, "
                    "got {0}. Returning empty DNS configuration.".format(
                        type(response).__name__
                    ),
                    "WARNING"
                )
                return None

            self.log(
                "Response data validated successfully, contains {0} top-level "
                "field(s): {1}".format(len(response), list(response.keys())),
                "DEBUG"
            )

            # Extract DNS details
            dns_details = response.get("dns")

            # Validate and log DNS details
            if dns_details is None:
                self.log(
                    "No DNS settings (dns field) found for site '{0}' (ID: {1}). "
                    "This may indicate: (1) No DNS configured for this site, "
                    "(2) Site inherits DNS from parent site, (3) User lacks "
                    "permissions.".format(site_name, site_id),
                    "WARNING"
                )
                return None

            if not isinstance(dns_details, dict):
                self.log(
                    "Invalid dns_details type - expected dict, got {0}. Returning "
                    "None.".format(type(dns_details).__name__),
                    "WARNING"
                )
                return None

            self.log(
                "DNS configuration found with {0} field(s): {1}".format(
                    len(dns_details), list(dns_details.keys())
                ),
                "DEBUG"
            )

            # Extract and validate domain name
            domain_name = dns_details.get("domainName")
            if domain_name is None:
                self.log(
                    "No domain name field found in DNS configuration for site "
                    "'{0}'. Initializing empty domain name.".format(site_name),
                    "DEBUG"
                )
                dns_details["domainName"] = ""
            elif not isinstance(domain_name, str):
                self.log(
                    "Invalid domain name type - expected str, got {0}. Converting "
                    "to string.".format(type(domain_name).__name__),
                    "WARNING"
                )
                dns_details["domainName"] = str(domain_name) if domain_name else ""
            else:
                # Validate domain name format (basic check)
                domain_name = domain_name.strip()
                if domain_name:
                    self.log(
                        "Found domain name for site '{0}': '{1}'".format(
                            site_name, domain_name
                        ),
                        "INFO"
                    )
                else:
                    self.log(
                        "Empty domain name configured for site '{0}'".format(
                            site_name
                        ),
                        "DEBUG"
                    )
                dns_details["domainName"] = domain_name

            # Extract and validate DNS servers
            dns_servers = dns_details.get("dnsServers")

            if dns_servers is None:
                self.log(
                    "No DNS servers field found in DNS configuration for site "
                    "'{0}'. Initializing empty server list.".format(site_name),
                    "DEBUG"
                )
                dns_details["dnsServers"] = []
            elif not isinstance(dns_servers, list):
                self.log(
                    "Invalid DNS servers type - expected list, got {0}. "
                    "Converting to list.".format(type(dns_servers).__name__),
                    "WARNING"
                )
                # Attempt conversion to list
                if isinstance(dns_servers, str):
                    dns_details["dnsServers"] = [dns_servers] if dns_servers else []
                    self.log(
                        "Converted string DNS server '{0}' to list".format(
                            dns_servers
                        ),
                        "DEBUG"
                    )
                else:
                    dns_details["dnsServers"] = []
                    self.log(
                        "Could not convert DNS servers to list, using empty list",
                        "WARNING"
                    )
            else:
                # Validate server count and format
                server_count = len(dns_servers)
                if server_count > 0:
                    self.log(
                        "Found {0} DNS server(s) for site '{1}': {2}".format(
                            server_count, site_name, dns_servers
                        ),
                        "INFO"
                    )
                    # Log individual server details with format validation
                    for idx, server in enumerate(dns_servers, start=1):
                        if not server or not isinstance(server, str):
                            self.log(
                                "DNS server {0}/{1} has invalid format: {2} "
                                "(type: {3})".format(
                                    idx, server_count, server,
                                    type(server).__name__
                                ),
                                "WARNING"
                            )
                        else:
                            # Detect IP version for logging
                            if ":" in server:
                                server_type = "IPv6 address"
                            elif "." in server:
                                server_type = "IPv4 address"
                            else:
                                server_type = "hostname/FQDN"

                            self.log(
                                "DNS server {0}/{1}: '{2}' ({3})".format(
                                    idx, server_count, server, server_type
                                ),
                                "DEBUG"
                            )
                else:
                    self.log(
                        "Empty DNS server list for site '{0}' - no DNS servers "
                        "configured (site may inherit from parent or use defaults)"
                        .format(site_name),
                        "DEBUG"
                    )

            # Exit log with summary
            self.log(
                "Successfully retrieved DNS settings for site '{0}' (ID: {1}): "
                "Domain='{2}', {3} server(s) configured".format(
                    site_name,
                    site_id,
                    dns_details.get("domainName", "Not configured"),
                    len(dns_details.get("dnsServers", []))
                ),
                "INFO"
            )

            return dns_details

        except Exception as e:
            self.msg = "Exception occurred while getting DNS settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

    def get_telemetry_settings_for_site(self, site_name, site_id):
        """
        Extracts comprehensive telemetry configuration from Catalyst Center for a
        specified site, enabling brownfield network settings discovery for the
        network_settings_workflow_manager module. Telemetry settings control network
        monitoring, application visibility, and data collection capabilities.

        Parameters:
            self - The current object details.
            site_name (str): The name of the site to retrieve telemetry settings for.
            site_id (str): The ID of the site to retrieve telemetry settings for.

        Returns:
            telemetry_details (dict): Telemetry settings details for the specified site.
        """
        self.log(
            "Starting telemetry settings retrieval for site '{0}' (ID: {1}) to "
            "extract NetFlow, SNMP, syslog, and data collection configuration for "
            "brownfield network settings discovery".format(site_name, site_id),
            "DEBUG"
        )

        if not site_name or not isinstance(site_name, str):
            self.log(
                "Invalid site_name parameter for telemetry retrieval - expected "
                "non-empty string, got {0}. Cannot proceed with API call.".format(
                    type(site_name).__name__ if site_name else "None"
                ),
                "ERROR"
            )
            return None

        if not site_id or not isinstance(site_id, str):
            self.log(
                "Invalid site_id parameter for telemetry retrieval - expected "
                "non-empty string (UUID), got {0}. Cannot proceed with API call."
                .format(
                    type(site_id).__name__ if site_id else "None"
                ),
                "ERROR"
            )
            return None

        self.log(
            "Executing API call to retrieve telemetry settings using "
            "network_settings family, retrieve_telemetry_settings_for_a_site "
            "function with site ID: {0}".format(site_id),
            "INFO"
        )

        try:
            telemetry_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_telemetry_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )

            self.log(
                "API call completed successfully for site '{0}', processing "
                "response data".format(site_name),
                "DEBUG"
            )

            # Validate response structure
            if not isinstance(telemetry_response, dict):
                self.log(
                    "Unexpected response type from telemetry API - expected dict, "
                    "got {0}. Returning empty telemetry configuration.".format(
                        type(telemetry_response).__name__
                    ),
                    "WARNING"
                )
                return None

            # Extract response data
            response = telemetry_response.get("response")

            if response is None:
                self.log(
                    "No 'response' key found in API result for site '{0}'. This "
                    "may indicate: (1) Site has no telemetry settings configured, "
                    "(2) Site inherits telemetry from parent, (3) API response "
                    "format changed. Returning empty telemetry configuration."
                    .format(site_name),
                    "WARNING"
                )
                return None

            if not isinstance(response, dict):
                self.log(
                    "Unexpected 'response' type in API result - expected dict, "
                    "got {0}. Returning empty telemetry configuration.".format(
                        type(response).__name__
                    ),
                    "WARNING"
                )
                return None

            self.log(
                "Response data validated successfully, contains {0} top-level "
                "field(s): {1}".format(len(response), list(response.keys())),
                "DEBUG"
            )

            # Validate and log telemetry components
            telemetry_details = response

            if not telemetry_details:
                self.log(
                    "Empty telemetry settings for site '{0}' (ID: {1}). Site may "
                    "inherit telemetry from parent site or have no configuration."
                    .format(site_name, site_id),
                    "WARNING"
                )
                return None

            # Track which telemetry components are configured
            configured_components = []

            # Validate Application Visibility (NetFlow) configuration
            app_visibility = telemetry_details.get("applicationVisibility")
            if app_visibility and isinstance(app_visibility, dict):
                collector = app_visibility.get("collector", {})
                collector_address = collector.get("address", "")
                collector_port = collector.get("port", "")
                collector_type = collector.get("collectorType", "")
                enabled_wired = app_visibility.get("enableOnWiredAccessDevices",
                                                   False)

                if collector_address or collector_type:
                    configured_components.append("applicationVisibility")
                    self.log(
                        "Application Visibility (NetFlow) configured - Collector: "
                        "{0}:{1}, Type: {2}, Wired Devices: {3}".format(
                            collector_address or "Not configured",
                            collector_port or "Not configured",
                            collector_type or "Not configured",
                            enabled_wired
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Application Visibility present but no collector configured "
                        "for site '{0}'".format(site_name),
                        "DEBUG"
                    )
            else:
                self.log(
                    "No Application Visibility (NetFlow) configuration found for "
                    "site '{0}'".format(site_name),
                    "DEBUG"
                )

            # Validate SNMP Traps configuration
            snmp_traps = telemetry_details.get("snmpTraps")
            if snmp_traps and isinstance(snmp_traps, dict):
                use_builtin = snmp_traps.get("useBuiltinTrapServer", False)
                external_servers = snmp_traps.get("externalTrapServers", [])

                # Validate external servers is a list
                if not isinstance(external_servers, list):
                    self.log(
                        "Invalid SNMP external trap servers type - expected list, "
                        "got {0}. Converting to list.".format(
                            type(external_servers).__name__
                        ),
                        "WARNING"
                    )
                    external_servers = [external_servers] if external_servers \
                        else []
                    snmp_traps["externalTrapServers"] = external_servers

                configured_components.append("snmpTraps")
                self.log(
                    "SNMP Traps configured - Use Builtin: {0}, External Servers "
                    "({1}): {2}".format(
                        use_builtin,
                        len(external_servers),
                        external_servers if external_servers else "None"
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "No SNMP Traps configuration found for site '{0}'".format(
                        site_name
                    ),
                    "DEBUG"
                )

            # Validate Syslog configuration
            syslogs = telemetry_details.get("syslogs")
            if syslogs and isinstance(syslogs, dict):
                use_builtin = syslogs.get("useBuiltinSyslogServer", False)
                external_servers = syslogs.get("externalSyslogServers", [])

                # Validate external servers is a list
                if not isinstance(external_servers, list):
                    self.log(
                        "Invalid syslog external servers type - expected list, got "
                        "{0}. Converting to list.".format(
                            type(external_servers).__name__
                        ),
                        "WARNING"
                    )
                    external_servers = [external_servers] if external_servers \
                        else []
                    syslogs["externalSyslogServers"] = external_servers

                configured_components.append("syslogs")
                self.log(
                    "Syslog configured - Use Builtin: {0}, External Servers ({1}): "
                    "{2}".format(
                        use_builtin,
                        len(external_servers),
                        external_servers if external_servers else "None"
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "No Syslog configuration found for site '{0}'".format(
                        site_name
                    ),
                    "DEBUG"
                )

            # Validate Wired Data Collection configuration
            wired_data = telemetry_details.get("wiredDataCollection")
            if wired_data and isinstance(wired_data, dict):
                enabled = wired_data.get("enableWiredDataCollection", False)
                configured_components.append("wiredDataCollection")
                self.log(
                    "Wired Data Collection configured - Enabled: {0}".format(
                        enabled
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "No Wired Data Collection configuration found for site '{0}'"
                    .format(site_name),
                    "DEBUG"
                )

            # Validate Wireless Telemetry configuration
            wireless_telemetry = telemetry_details.get("wirelessTelemetry")
            if wireless_telemetry and isinstance(wireless_telemetry, dict):
                enabled = wireless_telemetry.get("enableWirelessTelemetry", False)
                configured_components.append("wirelessTelemetry")
                self.log(
                    "Wireless Telemetry configured - Enabled: {0}".format(enabled),
                    "DEBUG"
                )
            else:
                self.log(
                    "No Wireless Telemetry configuration found for site '{0}'"
                    .format(site_name),
                    "DEBUG"
                )

            # Exit log with summary of configured components
            self.log(
                "Successfully retrieved telemetry settings for site '{0}' "
                "(ID: {1}): {2} component(s) configured: {3}".format(
                    site_name,
                    site_id,
                    len(configured_components),
                    configured_components if configured_components
                    else "No components configured"
                ),
                "INFO"
            )

            return telemetry_details
        except Exception as e:
            self.msg = "Exception occurred while getting telemetry settings for site '{0}' (ID: {1}): {2}".format(
                site_name, site_id, str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

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
        Retrieve timezone settings for a specific site from Catalyst Center.

        Extracts timezone configuration to enable brownfield network settings
        discovery for the network_settings_workflow_manager module. Timezone
        settings control time synchronization and scheduling for network
        operations.

        Purpose:
            Extracts timezone configuration from Catalyst Center to enable
            brownfield network settings discovery and YAML playbook generation
            for network management operations.

        Args:
            site_name (str): Full hierarchical site name for logging and error
                            context.
                Example: "Global/USA/SAN-FRANCISCO/SF_BLD1"
                Used for human-readable logging and error messages.

            site_id (str): Unique site identifier (UUID) for API calls.
                Example: "3e1f7e42-9c4c-4d3f-8a2e-1b5c6d7e8f9a"
                Required parameter for retrieve_time_zone_settings_for_a_site
                API call.

        Returns:
            dict or None: Timezone configuration or None:
                {
                    "identifier": "America/New_York"
                }
                Returns None if:
                - Site not found or inaccessible
                - No timezone settings configured for site
                - API call fails
                - Authentication/authorization errors
        """
        self.log(
            "Starting timezone settings retrieval for site '{0}' (ID: {1}) to "
            "extract timezone configuration for brownfield network settings "
            "discovery".format(site_name, site_id),
            "DEBUG"
        )

        if not site_name or not isinstance(site_name, str):
            self.log(
                "Invalid site_name parameter for timezone retrieval - expected "
                "non-empty string, got {0}. Cannot proceed with API call.".format(
                    type(site_name).__name__ if site_name else "None"
                ),
                "ERROR"
            )
            return None

        if not site_id or not isinstance(site_id, str):
            self.log(
                "Invalid site_id parameter for timezone retrieval - expected "
                "non-empty string (UUID), got {0}. Cannot proceed with API call."
                .format(
                    type(site_id).__name__ if site_id else "None"
                ),
                "ERROR"
            )
            return None

        self.log(
            "Executing API call to retrieve timezone settings using "
            "network_settings family, retrieve_time_zone_settings_for_a_site "
            "function with site ID: {0}".format(site_id),
            "INFO"
        )

        try:
            timezone_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_time_zone_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )

            # Extract time zone details
            if not isinstance(timezone_response, dict):
                self.log(
                    "Unexpected response type from timezone API - expected dict, "
                    "got {0}. Returning empty timezone configuration.".format(
                        type(timezone_response).__name__
                    ),
                    "WARNING"
                )
                return None

            # Extract response data
            response = timezone_response.get("response")

            if response is None:
                self.log(
                    "No 'response' key found in API result for site '{0}'. This "
                    "may indicate: (1) Site has no timezone settings configured, "
                    "(2) Site inherits timezone from parent, (3) API response "
                    "format changed. Returning empty timezone configuration."
                    .format(site_name),
                    "WARNING"
                )
                return None

            if not isinstance(response, dict):
                self.log(
                    "Unexpected 'response' type in API result - expected dict, "
                    "got {0}. Returning empty timezone configuration.".format(
                        type(response).__name__
                    ),
                    "WARNING"
                )
                return None

            self.log(
                "Response data validated successfully, contains {0} top-level "
                "field(s): {1}".format(len(response), list(response.keys())),
                "DEBUG"
            )

            # Extract timezone details
            timezone_details = response.get("timeZone")

            # Validate and log timezone details
            if timezone_details is None:
                self.log(
                    "No timezone settings (timeZone field) found for site '{0}' "
                    "(ID: {1}). This may indicate: (1) No timezone configured for "
                    "this site, (2) Site inherits timezone from parent site, "
                    "(3) User lacks permissions.".format(site_name, site_id),
                    "WARNING"
                )
                return None

            if not isinstance(timezone_details, dict):
                self.log(
                    "Invalid timezone_details type - expected dict, got {0}. "
                    "Returning None.".format(type(timezone_details).__name__),
                    "WARNING"
                )
                return None

            self.log(
                "Timezone configuration found with {0} field(s): {1}".format(
                    len(timezone_details), list(timezone_details.keys())
                ),
                "DEBUG"
            )

            # Extract and validate timezone identifier
            timezone_identifier = timezone_details.get("identifier")

            if timezone_identifier is None:
                self.log(
                    "No timezone identifier field found in timezone configuration "
                    "for site '{0}'. Initializing empty identifier.".format(
                        site_name
                    ),
                    "DEBUG"
                )
                timezone_details["identifier"] = ""
            elif not isinstance(timezone_identifier, str):
                self.log(
                    "Invalid timezone identifier type - expected str, got {0}. "
                    "Converting to string.".format(
                        type(timezone_identifier).__name__
                    ),
                    "WARNING"
                )
                timezone_details["identifier"] = str(timezone_identifier) if \
                    timezone_identifier else ""
            else:
                # Validate timezone identifier format (basic check)
                timezone_identifier = timezone_identifier.strip()

                if timezone_identifier:
                    # Log timezone with validation hints
                    if "/" in timezone_identifier:
                        # Standard IANA format (Continent/City)
                        parts = timezone_identifier.split("/")
                        self.log(
                            "Found standard IANA timezone identifier for site "
                            "'{0}': '{1}' (Region: {2}, Location: {3})".format(
                                site_name, timezone_identifier, parts[0],
                                parts[1] if len(parts) > 1 else "N/A"
                            ),
                            "INFO"
                        )
                    elif timezone_identifier.upper() in ["UTC", "GMT"]:
                        # UTC/GMT special case
                        self.log(
                            "Found UTC/GMT timezone identifier for site '{0}': "
                            "'{1}'".format(site_name, timezone_identifier),
                            "INFO"
                        )
                    else:
                        # Non-standard format (may be valid but unusual)
                        self.log(
                            "Found non-standard timezone identifier for site "
                            "'{0}': '{1}' (does not follow IANA Continent/City "
                            "format)".format(site_name, timezone_identifier),
                            "WARNING"
                        )
                else:
                    self.log(
                        "Empty timezone identifier configured for site '{0}'"
                        .format(site_name),
                        "DEBUG"
                    )

                timezone_details["identifier"] = timezone_identifier

            # Exit log with summary
            self.log(
                "Successfully retrieved timezone settings for site '{0}' "
                "(ID: {1}): Timezone='{2}'".format(
                    site_name,
                    site_id,
                    timezone_details.get("identifier", "Not configured")
                ),
                "INFO"
            )

            return timezone_details
        except AttributeError as e:
            self.msg = (
                "Invalid API family or function name for timezone retrieval - "
                "SDK does not recognize family '{0}' or function '{1}'. Verify "
                "SDK version compatibility. Error: {2}".format(
                    "network_settings", "retrieve_time_zone_settings_for_a_site", str(e)
                )
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        except Exception as e:
            error_str = str(e).lower()

            # Provide specific error context based on error type
            if "unauthorized" in error_str or "401" in error_str:
                self.msg = (
                    "Authentication failed while retrieving timezone settings for "
                    "site '{0}' (ID: {1}). Verify Catalyst Center credentials "
                    "(username/password) are correct and user has network-admin "
                    "privileges. Error: {2}".format(site_name, site_id, str(e))
                )
            elif "forbidden" in error_str or "403" in error_str:
                self.msg = (
                    "Authorization failed while retrieving timezone settings for "
                    "site '{0}' (ID: {1}). User lacks permissions to view "
                    "timezone settings. Required role: NETWORK-ADMIN-ROLE or "
                    "SUPER-ADMIN-ROLE. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "not found" in error_str or "404" in error_str:
                self.msg = (
                    "Site '{0}' (ID: {1}) not found in Catalyst Center. Site may "
                    "have been deleted or ID is invalid. Verify site exists and "
                    "ID is correct. Error: {2}".format(site_name, site_id, str(e))
                )
            elif "timeout" in error_str or "timed out" in error_str:
                self.msg = (
                    "API call timeout while retrieving timezone settings for site "
                    "'{0}' (ID: {1}). Catalyst Center may be overloaded or "
                    "network latency is high. Retry operation or increase timeout "
                    "value. Error: {2}".format(site_name, site_id, str(e))
                )
            elif "connection" in error_str:
                self.msg = (
                    "Network connection error while retrieving timezone settings "
                    "for site '{0}' (ID: {1}). Verify network connectivity to "
                    "Catalyst Center and DNS resolution. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            else:
                # Generic error message for unknown errors
                self.msg = (
                    "Exception occurred while retrieving timezone settings for "
                    "site '{0}' (ID: {1}). This may indicate: (1) API response "
                    "format changed, (2) Catalyst Center version incompatibility, "
                    "(3) Temporary API error. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )

            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

    def get_banner_settings_for_site(self, site_name, site_id):
        """
        Retrieve Message of the Day (MOTD) banner settings for a specific site from
        Catalyst Center.

        Extracts banner configuration to enable brownfield network settings discovery
        for the network_settings_workflow_manager module. Banner settings control the
        message displayed to users when logging into network devices.

        Purpose:
            Extracts banner/MOTD configuration from Catalyst Center to enable
            brownfield network settings discovery and YAML playbook generation for
            network management operations.

        Args:
            site_name (str): Full hierarchical site name for logging and error context.
                Example: "Global/USA/SAN-FRANCISCO/SF_BLD1"
                Used for human-readable logging and error messages.

            site_id (str): Unique site identifier (UUID) for API calls.
                Example: "3e1f7e42-9c4c-4d3f-8a2e-1b5c6d7e8f9a"
                Required parameter for retrieve_banner_settings_for_a_site API call.

        Returns:
            dict or None: Banner configuration or None:
                {
                    "message": "Authorized Access Only\\nUnauthorized access prohibited",
                    "retainExistingBanner": False
                }
                Returns None if:
                - Site not found or inaccessible
                - No banner settings configured for site
                - API call fails
                - Authentication/authorization errors
        """
        self.log(
            "Starting Message of the Day (banner) settings retrieval for site "
            "'{0}' (ID: {1}) to extract banner configuration for brownfield "
            "network settings discovery".format(site_name, site_id),
            "DEBUG"
        )

        if not site_name or not isinstance(site_name, str):
            self.log(
                "Invalid site_name parameter for banner retrieval - expected "
                "non-empty string, got {0}. Cannot proceed with API call.".format(
                    type(site_name).__name__ if site_name else "None"
                ),
                "ERROR"
            )
            return None

        if not site_id or not isinstance(site_id, str):
            self.log(
                "Invalid site_id parameter for banner retrieval - expected "
                "non-empty string (UUID), got {0}. Cannot proceed with API call."
                .format(
                    type(site_id).__name__ if site_id else "None"
                ),
                "ERROR"
            )
            return None

        self.log(
            "Executing API call to retrieve banner settings using "
            "network_settings family, retrieve_banner_settings_for_a_site "
            "function with site ID: {0}".format(site_id),
            "INFO"
        )

        try:
            banner_response = self.dnac._exec(
                family="network_settings",
                function="retrieve_banner_settings_for_a_site",
                op_modifies=False,
                params={"id": site_id},
            )
            # Validate response structure
            if not isinstance(banner_response, dict):
                self.log(
                    "Unexpected response type from banner API - expected dict, "
                    "got {0}. Returning empty banner configuration.".format(
                        type(banner_response).__name__
                    ),
                    "WARNING"
                )
                return None

            # Extract response data
            response = banner_response.get("response")

            if response is None:
                self.log(
                    "No 'response' key found in API result for site '{0}'. This "
                    "may indicate: (1) Site has no banner settings configured, "
                    "(2) Site inherits banner from parent, (3) API response "
                    "format changed. Returning empty banner configuration."
                    .format(site_name),
                    "WARNING"
                )
                return None

            if not isinstance(response, dict):
                self.log(
                    "Unexpected 'response' type in API result - expected dict, "
                    "got {0}. Returning empty banner configuration.".format(
                        type(response).__name__
                    ),
                    "WARNING"
                )
                return None

            self.log(
                "Response data validated successfully, contains {0} top-level "
                "field(s): {1}".format(len(response), list(response.keys())),
                "DEBUG"
            )

            # Extract banner details
            messageoftheday_details = response.get("banner")

            # Validate and log banner details
            if messageoftheday_details is None:
                self.log(
                    "No banner settings (banner field) found for site '{0}' "
                    "(ID: {1}). This may indicate: (1) No banner configured for "
                    "this site, (2) Site inherits banner from parent site, "
                    "(3) User lacks permissions.".format(site_name, site_id),
                    "WARNING"
                )
                return None

            if not isinstance(messageoftheday_details, dict):
                self.log(
                    "Invalid messageoftheday_details type - expected dict, got "
                    "{0}. Returning None.".format(
                        type(messageoftheday_details).__name__
                    ),
                    "WARNING"
                )
                return None

            self.log(
                "Banner configuration found with {0} field(s): {1}".format(
                    len(messageoftheday_details),
                    list(messageoftheday_details.keys())
                ),
                "DEBUG"
            )

            # Extract and validate banner message
            banner_message = messageoftheday_details.get("message")

            if banner_message is None:
                self.log(
                    "No banner message field found in banner configuration for "
                    "site '{0}'. Initializing empty message.".format(site_name),
                    "DEBUG"
                )
                messageoftheday_details["message"] = ""
            elif not isinstance(banner_message, str):
                self.log(
                    "Invalid banner message type - expected str, got {0}. "
                    "Converting to string.".format(type(banner_message).__name__),
                    "WARNING"
                )
                messageoftheday_details["message"] = str(banner_message) if \
                    banner_message else ""
            else:
                # Validate and log banner message details
                banner_message = banner_message.strip()

                if banner_message:
                    # Count lines in banner message
                    line_count = banner_message.count("\\n") + 1
                    char_count = len(banner_message)

                    # Log banner summary (truncate for readability)
                    display_message = banner_message[:100] + "..." if \
                        len(banner_message) > 100 else banner_message

                    self.log(
                        "Found banner message for site '{0}': {1} line(s), "
                        "{2} character(s). Preview: '{3}'".format(
                            site_name, line_count, char_count, display_message
                        ),
                        "INFO"
                    )

                    # Check for common banner patterns
                    if "unauthorized" in banner_message.lower():
                        self.log(
                            "Banner contains 'unauthorized access' warning",
                            "DEBUG"
                        )
                    if "authorized" in banner_message.lower():
                        self.log(
                            "Banner contains 'authorized access' notice",
                            "DEBUG"
                        )
                    if "@" in banner_message or "contact" in banner_message.lower():
                        self.log(
                            "Banner appears to contain contact information",
                            "DEBUG"
                        )
                else:
                    self.log(
                        "Empty banner message configured for site '{0}'".format(
                            site_name
                        ),
                        "DEBUG"
                    )

                messageoftheday_details["message"] = banner_message

            # Extract and validate retainExistingBanner flag
            retain_banner = messageoftheday_details.get("retainExistingBanner")

            if retain_banner is None:
                self.log(
                    "No retainExistingBanner field found in banner configuration "
                    "for site '{0}'. Defaulting to False.".format(site_name),
                    "DEBUG"
                )
                messageoftheday_details["retainExistingBanner"] = False
            elif not isinstance(retain_banner, bool):
                self.log(
                    "Invalid retainExistingBanner type - expected bool, got {0}. "
                    "Converting to boolean.".format(type(retain_banner).__name__),
                    "WARNING"
                )
                # Convert to boolean using truthiness
                messageoftheday_details["retainExistingBanner"] = bool(
                    retain_banner
                )
            else:
                self.log(
                    "Retain existing banner flag for site '{0}': {1}".format(
                        site_name, retain_banner
                    ),
                    "DEBUG"
                )

            # Exit log with summary
            message_status = "configured" if \
                messageoftheday_details.get("message") else "not configured"
            retain_status = messageoftheday_details.get(
                "retainExistingBanner", False
            )

            self.log(
                "Successfully retrieved banner settings for site '{0}' "
                "(ID: {1}): Message={2}, RetainExisting={3}".format(
                    site_name,
                    site_id,
                    message_status,
                    retain_status
                ),
                "INFO"
            )

            return messageoftheday_details
        except AttributeError as e:
            self.msg = (
                "Invalid API family or function name for banner retrieval - SDK "
                "does not recognize family '{0}' or function '{1}'. Verify SDK "
                "version compatibility. Error: {2}".format(
                    "network_settings", "retrieve_banner_settings_for_a_site", str(e)
                )
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        except Exception as e:
            error_str = str(e).lower()

            # Provide specific error context based on error type
            if "unauthorized" in error_str or "401" in error_str:
                self.msg = (
                    "Authentication failed while retrieving banner settings for "
                    "site '{0}' (ID: {1}). Verify Catalyst Center credentials "
                    "(username/password) are correct and user has network-admin "
                    "privileges. Error: {2}".format(site_name, site_id, str(e))
                )
            elif "forbidden" in error_str or "403" in error_str:
                self.msg = (
                    "Authorization failed while retrieving banner settings for "
                    "site '{0}' (ID: {1}). User lacks permissions to view banner "
                    "settings. Required role: NETWORK-ADMIN-ROLE or "
                    "SUPER-ADMIN-ROLE. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            elif "not found" in error_str or "404" in error_str:
                self.msg = (
                    "Site '{0}' (ID: {1}) not found in Catalyst Center. Site may "
                    "have been deleted or ID is invalid. Verify site exists and "
                    "ID is correct. Error: {2}".format(site_name, site_id, str(e))
                )
            elif "timeout" in error_str or "timed out" in error_str:
                self.msg = (
                    "API call timeout while retrieving banner settings for site "
                    "'{0}' (ID: {1}). Catalyst Center may be overloaded or "
                    "network latency is high. Retry operation or increase timeout "
                    "value. Error: {2}".format(site_name, site_id, str(e))
                )
            elif "connection" in error_str:
                self.msg = (
                    "Network connection error while retrieving banner settings "
                    "for site '{0}' (ID: {1}). Verify network connectivity to "
                    "Catalyst Center and DNS resolution. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )
            else:
                # Generic error message for unknown errors
                self.msg = (
                    "Exception occurred while retrieving banner settings for site "
                    "'{0}' (ID: {1}). This may indicate: (1) API response format "
                    "changed, (2) Catalyst Center version incompatibility, "
                    "(3) Temporary API error. Error: {2}".format(
                        site_name, site_id, str(e)
                    )
                )

            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

    def get_device_controllability_settings(self, network_element, filters):
        """
        Retrieve device controllability settings from Catalyst Center.

        Extracts global device controllability configuration to enable brownfield
        network settings discovery for the network_settings_workflow_manager module.
        Device controllability settings control network device management and
        telemetry autocorrection capabilities.

        Purpose:
            Extracts device controllability configuration from Catalyst Center to
            enable brownfield network settings discovery and YAML playbook generation
            for network management operations.

        Important Notes:
            - Device controllability settings are GLOBAL, not site-specific
            - Applies to all network devices managed by Catalyst Center
            - No site filtering parameters are needed or supported
            - Returns single configuration dict (not a list)

        Args:
            network_element (dict): Network element configuration containing:
                - api_family (str): API family name ("site_design")
                - api_function (str): API function name
                                    ("get_device_controllability_settings")
                - reverse_mapping_function (callable): Function for response
                                                    transformation

            filters (dict): Filter parameters (IGNORED for this global setting):
                - global_filters (dict, optional): Not applicable for global settings
                - component_specific_filters (dict, optional): Not applicable

        Returns:
            dict: Device controllability configuration result:
                {
                    "device_controllability_details": {
                        "device_controllability": True,
                        "autocorrect_telemetry_config": False
                    },
                    "operation_summary": {
                        "total_sites_processed": 1,
                        "total_components_processed": 1,
                        "total_successful_operations": 1,
                        "total_failed_operations": 0,
                        "sites_with_complete_success": ["Global"],
                        "sites_with_partial_success": [],
                        "sites_with_complete_failure": [],
                        "success_details": [...],
                        "failure_details": []
                    }
                }
        """
        self.log(
            "Starting device controllability settings retrieval from Catalyst Center "
            "to extract global device management configuration for brownfield network "
            "settings discovery",
            "DEBUG"
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not isinstance(api_family, str):
            self.log(
                "Invalid api_family parameter - expected non-empty string, got {0}. "
                "Cannot proceed with API call.".format(
                    type(api_family).__name__ if api_family else "None"
                ),
                "ERROR"
            )
            return self._create_default_controllability_result(
                "Invalid API family parameter"
            )

        if not api_function or not isinstance(api_function, str):
            self.log(
                "Invalid api_function parameter - expected non-empty string, got {0}. "
                "Cannot proceed with API call.".format(
                    type(api_function).__name__ if api_function else "None"
                ),
                "ERROR"
            )
            return self._create_default_controllability_result(
                "Invalid API function parameter"
            )

        self.log(
            "Executing API call to retrieve device controllability settings using "
            "family '{0}', function '{1}' (global settings - no site filtering)"
            .format(api_family, api_function),
            "INFO"
        )

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

        # Apply reverse mapping for consistency
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        if not reverse_mapping_function or not callable(reverse_mapping_function):
            self.log(
                "Invalid reverse_mapping_function - expected callable, got {0}. "
                "Using raw settings without transformation.".format(
                    type(reverse_mapping_function).__name__
                ),
                "WARNING"
            )
            settings_details = device_controllability_settings
        else:
            reverse_mapping_spec = reverse_mapping_function()

            self.log(
                "Applying reverse mapping specification with {0} field mappings"
                .format(len(reverse_mapping_spec) if reverse_mapping_spec else 0),
                "DEBUG"
            )

            settings_details = self.modify_network_parameters(
                reverse_mapping_spec,
                device_controllability_settings
            )

            self.log(
                "Successfully transformed {0} device controllability settings: {1}"
                .format(len(settings_details), settings_details),
                "INFO"
            )

        settings_details = self.modify_network_parameters(reverse_mapping_spec, device_controllability_settings)

        self.log(
            f"Successfully transformed {len(settings_details)} device controllability settings: {settings_details}",
            "INFO",
        )

        # Device controllability is a global setting, not site-specific, so return as single dict instead of list
        device_controllability_dict = settings_details[0] if settings_details else {}
        self.log(
            "Successfully retrieved device controllability settings: "
            "device_controllability={0}, autocorrect_telemetry_config={1}"
            .format(
                device_controllability_dict.get("device_controllability", "Not set"),
                device_controllability_dict.get("autocorrect_telemetry_config", "Not set")
            ),
            "INFO"
        )

        return {
            "device_controllability_details": device_controllability_dict,
            "operation_summary": self.get_operation_summary(),
        }

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generate YAML playbook configuration file for network_settings_workflow_manager module.

        Orchestrates the complete brownfield network settings extraction workflow by:
        1. Processing configuration parameters and filters
        2. Iterating through requested network components
        3. Executing component-specific retrieval functions
        4. Consolidating results and operation summaries
        5. Writing final YAML configuration to file

        Purpose:
            Creates Ansible-compatible YAML playbook files containing network settings
            configurations discovered from Cisco Catalyst Center, enabling brownfield
            network settings documentation and programmatic modifications.

        Args:
            yaml_config_generator (dict): Configuration parameters containing:
                - file_path (str, optional): Output YAML file path
                    Default: Auto-generated with timestamp
                - generate_all_configurations (bool, optional): Enable auto-discovery mode
                    Default: False
                - global_filters (dict, optional): Site/pool name filters
                - component_specific_filters (dict, optional): Component-level filters
                    - components_list (list): Network components to extract
                        Valid: ["global_pool_details", "reserve_pool_details",
                            "network_management_details", "device_controllability_details"]

        Returns:
            self: Current instance with operation result:
                - self.status: "success", "ok", or "failed"
                - self.msg: Operation result message with summary
                - self.result: Ansible module result dictionary

        Auto-Discovery Mode:
            When generate_all_configurations=True:
            - Ignores all filter parameters
            - Retrieves ALL network settings from Catalyst Center
            - Processes ALL supported components
            - Generates comprehensive brownfield documentation

        Component Processing Flow:
            For each requested component:
            1. Validate component is supported by module schema
            2. Prepare component-specific filters
            3. Execute component retrieval function
            4. Extract component details from response
            5. Add to final configuration list
            6. Consolidate operation summary statistics

        Operation Summary Consolidation:
            Aggregates metrics from all component operations:
            - total_sites_processed: Unique sites across all components
            - total_components_processed: Number of components successfully processed
            - total_successful_operations: Sum of successful component operations
            - total_failed_operations: Sum of failed component operations
            - success_details: Per-component success information
            - failure_details: Per-component error information

        YAML Output Structure:
            config:
            - global_pool_details:
                settings:
                    ip_pool: [...]
            - reserve_pool_details: [...]
            - network_management_details: [...]
            - device_controllability_details: {...}
        """
        self.log(
            "Starting YAML playbook configuration generation workflow for module "
            "'{0}' to extract network settings from Catalyst Center and create "
            "Ansible-compatible playbook file".format(self.module_name),
            "DEBUG"
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if not isinstance(generate_all, bool):
            self.log(
                "Invalid generate_all_configurations parameter - expected bool, got {0}. "
                "Defaulting to False (manual component selection mode).".format(
                    type(generate_all).__name__
                ),
                "WARNING"
            )
            generate_all = False

        if generate_all:
            self.log(
                "Auto-discovery mode enabled - workflow will retrieve ALL network settings "
                "from ALL supported components, ignoring any provided filters",
                "INFO"
            )
        else:
            self.log(
                "Manual component selection mode - workflow will process only requested "
                "components based on provided filters and components_list",
                "DEBUG"
            )

        # Determine output file path
        file_path = yaml_config_generator.get("file_path")

        if not file_path:
            self.log(
                "No file_path parameter provided by user, generating default filename "
                "with timestamp for uniqueness",
                "DEBUG"
            )
            file_path = self.generate_filename()
            self.log(
                "Auto-generated file path: {0}".format(file_path),
                "INFO"
            )
        else:
            # Validate file_path is a string
            if not isinstance(file_path, str):
                error_msg = (
                    "Invalid file_path parameter - expected str, got {0}. "
                    "Cannot proceed with YAML generation.".format(
                        type(file_path).__name__
                    )
                )
                self.log(error_msg, "ERROR")
                self.msg = {
                    "message": "YAML config generation failed for module '{0}' - invalid file_path parameter.".format(
                        self.module_name
                    ),
                    "error": error_msg
                }
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                "Using user-provided file path for YAML output: {0}".format(file_path),
                "INFO"
            )

            # Validate file path is writable
            import os
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                self.log(
                    "Output directory does not exist: {0}. Attempting to create it.".format(
                        directory
                    ),
                    "WARNING"
                )
                try:
                    os.makedirs(directory, exist_ok=True)
                    self.log(
                        "Successfully created output directory: {0}".format(directory),
                        "INFO"
                    )
                except Exception as e:
                    error_msg = "Failed to create output directory: {0}. Error: {1}".format(
                        directory, str(e)
                    )
                    self.log(error_msg, "ERROR")
                    self.msg = {
                        "message": "YAML config generation failed for module '{0}' - cannot create output directory.".format(
                            self.module_name
                        ),
                        "error": error_msg
                    }
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

        # Initialize filter dictionaries based on mode
        if generate_all:
            self.log(
                "Auto-discovery mode: Overriding any user-provided filters to retrieve "
                "all network settings without filtering",
                "INFO"
            )
            global_filters = {}
            component_specific_filters = {}
        else:
            global_filters = yaml_config_generator.get("global_filters")
            component_specific_filters = yaml_config_generator.get("component_specific_filters")

            # Validate and normalize filter parameters
            if global_filters is None:
                global_filters = {}
                self.log(
                    "No global_filters provided, using empty filter set (no global filtering)",
                    "DEBUG"
                )
            elif not isinstance(global_filters, dict):
                self.log(
                    "Invalid global_filters type - expected dict, got {0}. Using empty filter set.".format(
                        type(global_filters).__name__
                    ),
                    "WARNING"
                )
                global_filters = {}
            else:
                self.log(
                    "Using provided global_filters: {0}".format(global_filters),
                    "DEBUG"
                )

            if component_specific_filters is None:
                component_specific_filters = {}
                self.log(
                    "No component_specific_filters provided, will process all supported components",
                    "DEBUG"
                )
            elif not isinstance(component_specific_filters, dict):
                self.log(
                    "Invalid component_specific_filters type - expected dict, got {0}. "
                    "Using empty filter set.".format(
                        type(component_specific_filters).__name__
                    ),
                    "WARNING"
                )
                component_specific_filters = {}
            else:
                self.log(
                    "Using provided component_specific_filters: {0}".format(
                        component_specific_filters
                    ),
                    "DEBUG"
                )

        # Get supported network elements
        module_supported_network_elements = self.module_schema.get("network_elements", {})
        if not module_supported_network_elements:
            error_msg = "No network elements defined in module schema, cannot process any components"
            self.log(error_msg, "CRITICAL")
            self.msg = {
                "message": "YAML config generation failed for module '{0}' - module schema is invalid.".format(
                    self.module_name
                ),
                "error": error_msg
            }
            self.set_operation_result("failed", False, self.msg, "CRITICAL")
            return self

        self.log(
            "Module supports {0} network element type(s): {1}".format(
                len(module_supported_network_elements),
                list(module_supported_network_elements.keys())
            ),
            "DEBUG"
        )
        # Determine which components to process
        components_list = component_specific_filters.get(
            "components_list",
            list(module_supported_network_elements.keys())
        )

        # Validate components_list
        if not isinstance(components_list, list):
            self.log(
                "Invalid components_list type - expected list, got {0}. "
                "Defaulting to all supported components.".format(
                    type(components_list).__name__
                ),
                "WARNING"
            )
            components_list = list(module_supported_network_elements.keys())

        # Remove duplicate components
        components_list = list(dict.fromkeys(components_list))

        self.log(
            "Will process {0} component(s) in this workflow: {1}".format(
                len(components_list), components_list
            ),
            "INFO"
        )

        # Validate each component is supported
        unsupported_components = [
            comp for comp in components_list
            if comp not in module_supported_network_elements
        ]

        if unsupported_components:
            self.log(
                "Detected {0} unsupported component(s) that will be skipped: {1}. "
                "Supported components: {2}".format(
                    len(unsupported_components),
                    unsupported_components,
                    list(module_supported_network_elements.keys())
                ),
                "WARNING"
            )
            # Remove unsupported components
            components_list = [
                comp for comp in components_list
                if comp in module_supported_network_elements
            ]
            self.log(
                "After removing unsupported components, will process {0} component(s): {1}".format(
                    len(components_list), components_list
                ),
                "INFO"
            )

        if not components_list:
            error_msg = "No valid components to process after filtering"
            self.log(error_msg, "ERROR")
            self.msg = {
                "message": "No configurations or components to process for module '{0}'. "
                "Verify input filters or configuration.".format(self.module_name),
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
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        # Reset operation tracking for clean state
        self.log(
            "Resetting operation tracking variables for new YAML generation workflow",
            "DEBUG"
        )
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
        self.log(
            "Beginning component processing loop - will iterate through {0} component(s)".format(
                len(components_list)
            ),
            "INFO"
        )

        for component_index, component in enumerate(components_list, start=1):
            self.log(
                "Processing component {0}/{1}: '{2}'".format(
                    component_index, len(components_list), component
                ),
                "INFO"
            )

            # Get component configuration from module schema
            network_element = module_supported_network_elements.get(component)

            if not network_element:
                self.log(
                    "Component '{0}' not found in module schema (should not happen after "
                    "validation). Skipping this component.".format(component),
                    "ERROR"
                )
                consolidated_operation_summary["total_failed_operations"] += 1
                consolidated_operation_summary["failure_details"].append({
                    "component": component,
                    "error": "Component not found in module schema"
                })
                continue

            # Validate network element has required fields
            if not isinstance(network_element, dict):
                self.log(
                    "Invalid network element configuration for component '{0}' - expected "
                    "dict, got {1}. Skipping this component.".format(
                        component, type(network_element).__name__
                    ),
                    "ERROR"
                )
                consolidated_operation_summary["total_failed_operations"] += 1
                consolidated_operation_summary["failure_details"].append({
                    "component": component,
                    "error": "Invalid network element configuration"
                })
                continue

            # Get component operation function
            operation_func = network_element.get("get_function_name")

            if not operation_func or not callable(operation_func):
                self.log(
                    "Component '{0}' has invalid or missing get_function_name (expected "
                    "callable, got {1}). Skipping this component.".format(
                        component, type(operation_func).__name__ if operation_func else "None"
                    ),
                    "ERROR"
                )
                consolidated_operation_summary["total_failed_operations"] += 1
                consolidated_operation_summary["failure_details"].append({
                    "component": component,
                    "error": "Missing or invalid retrieval function"
                })
                continue

            # Prepare component filters
            component_filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters
            }

            self.log(
                "Executing retrieval function for component '{0}' with filters: {1}".format(
                    component, component_filters
                ),
                "DEBUG"
            )

            # Execute component operation function
            try:
                details = operation_func(network_element, component_filters)

                self.log(
                    "Component '{0}' retrieval function completed, processing results".format(
                        component
                    ),
                    "DEBUG"
                )
            except Exception as e:
                error_msg = "Exception during component '{0}' retrieval: {1}".format(
                    component, str(e)
                )
                self.log(error_msg, "ERROR")
                consolidated_operation_summary["total_failed_operations"] += 1
                consolidated_operation_summary["failure_details"].append({
                    "component": component,
                    "error": error_msg
                })
                continue

            # Validate details structure
            if not details or not isinstance(details, dict):
                self.log(
                    "Component '{0}' returned invalid details structure (expected dict, "
                    "got {1}). Skipping this component.".format(
                        component, type(details).__name__ if details else "None"
                    ),
                    "WARNING"
                )
                consolidated_operation_summary["total_failed_operations"] += 1
                consolidated_operation_summary["failure_details"].append({
                    "component": component,
                    "error": "Invalid details structure returned"
                })
                continue

            # Check if component key exists in details
            if component not in details:
                self.log(
                    "Component '{0}' key not found in returned details. Available keys: {1}. "
                    "Skipping this component.".format(component, list(details.keys())),
                    "WARNING"
                )
                consolidated_operation_summary["total_failed_operations"] += 1
                consolidated_operation_summary["failure_details"].append({
                    "component": component,
                    "error": "Component key not found in response"
                })
                continue

            component_details = details[component]

            if isinstance(component_details, list):
                self.log(
                    "Component '{0}' returned list with {1} item(s)".format(
                        component, len(component_details)
                    ),
                    "INFO"
                )
            elif isinstance(component_details, dict):
                self.log(
                    "Component '{0}' returned dict with {1} key(s): {2}".format(
                        component, len(component_details), list(component_details.keys())
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "Component '{0}' returned unexpected type: {1}".format(
                        component, type(component_details).__name__
                    ),
                    "WARNING"
                )

            # Add component details to final list (preserve structure)
            final_list.append(details)

            self.log(
                "Successfully added component '{0}' to final configuration list "
                "(total entries now: {1})".format(component, len(final_list)),
                "INFO"
            )

            # Consolidate operation summary from component
            if details.get("operation_summary"):
                summary = details["operation_summary"]

                self.log(
                    "Consolidating operation summary from component '{0}': "
                    "successful={1}, failed={2}".format(
                        component,
                        summary.get("total_successful_operations", 0),
                        summary.get("total_failed_operations", 0)
                    ),
                    "DEBUG"
                )

                # Increment component processed counter
                consolidated_operation_summary["total_components_processed"] += 1

                # Aggregate success/failure counts
                consolidated_operation_summary["total_successful_operations"] += summary.get(
                    "total_successful_operations", 0
                )
                consolidated_operation_summary["total_failed_operations"] += summary.get(
                    "total_failed_operations", 0
                )

                # Merge success/failure details lists
                if summary.get("success_details"):
                    consolidated_operation_summary["success_details"].extend(
                        summary["success_details"]
                    )

                if summary.get("failure_details"):
                    consolidated_operation_summary["failure_details"].extend(
                        summary["failure_details"]
                    )

                # Track unique sites (avoid duplicates across components)
                for site in summary.get("sites_with_complete_success", []):
                    if site not in consolidated_operation_summary["sites_with_complete_success"]:
                        consolidated_operation_summary["sites_with_complete_success"].append(site)

                for site in summary.get("sites_with_partial_success", []):
                    if site not in consolidated_operation_summary["sites_with_partial_success"]:
                        consolidated_operation_summary["sites_with_partial_success"].append(site)

                for site in summary.get("sites_with_complete_failure", []):
                    if site not in consolidated_operation_summary["sites_with_complete_failure"]:
                        consolidated_operation_summary["sites_with_complete_failure"].append(site)
            else:
                self.log(
                    "Component '{0}' did not provide operation_summary in response".format(
                        component
                    ),
                    "WARNING"
                )

        # Calculate total unique sites processed
        all_sites = set(
            consolidated_operation_summary["sites_with_complete_success"] +
            consolidated_operation_summary["sites_with_partial_success"] +
            consolidated_operation_summary["sites_with_complete_failure"]
        )
        consolidated_operation_summary["total_sites_processed"] = len(all_sites)

        self.log(
            "Component processing loop completed. Processed {0} component(s), "
            "generated {1} configuration entry/entries, tracked {2} unique site(s)".format(
                consolidated_operation_summary["total_components_processed"],
                len(final_list),
                consolidated_operation_summary["total_sites_processed"]
            ),
            "INFO"
        )

        # Check if any configurations were generated
        if not final_list:
            self.log(
                "No configurations generated after processing all components. This may indicate: "
                "(1) All components returned empty results, (2) All component retrievals failed, "
                "(3) Filters excluded all available configurations",
                "WARNING"
            )

            self.msg = {
                "message": "No configurations or components to process for module '{0}'. "
                "Verify input filters or configuration.".format(self.module_name),
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        # Create final YAML structure
        self.log(
            "Creating final YAML structure with {0} configuration entry/entries".format(
                len(final_list)
            ),
            "DEBUG"
        )
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
        self.log(
            "Attempting to write final YAML configuration to file: {0}".format(file_path),
            "INFO"
        )

        write_success = self.write_dict_to_yaml(final_dict, file_path)

        if write_success:
            self.log(
                "Successfully wrote YAML configuration to file: {0} "
                "({1} configuration entries, {2} bytes)".format(
                    file_path,
                    len(final_list),
                    "size unknown"  # Could add file size check here
                ),
                "INFO"
            )

            # Exit log with success summary
            self.log(
                "YAML playbook configuration generation workflow completed successfully "
                "for module '{0}'. Generated {1} configuration entry/entries across "
                "{2} component(s) covering {3} site(s). Output file: {4}".format(
                    self.module_name,
                    len(final_list),
                    consolidated_operation_summary["total_components_processed"],
                    consolidated_operation_summary["total_sites_processed"],
                    file_path
                ),
                "INFO"
            )

            self.msg = {
                "message": "YAML config generation succeeded for module '{0}'.".format(
                    self.module_name
                ),
                "file_path": file_path,
                "configurations_generated": len(final_list),
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            error_msg = "Failed to write YAML configuration to file: {0}".format(file_path)
            self.log(error_msg, "ERROR")

            # Exit log with failure summary
            self.log(
                "YAML playbook configuration generation workflow failed for module '{0}'. "
                "Processed {1} component(s) successfully but unable to write output file: {2}".format(
                    self.module_name,
                    consolidated_operation_summary["total_components_processed"],
                    file_path
                ),
                "ERROR"
            )

            self.msg = {
                "message": "YAML config generation failed for module '{0}' - unable to write to file.".format(
                    self.module_name
                ),
                "file_path": file_path,
                "error": error_msg,
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_diff_gathered(self):
        """
        Execute the network settings gathering workflow to collect brownfield configurations.

        This method orchestrates the complete brownfield network settings extraction workflow
        by coordinating YAML configuration generation operations based on user-provided
        parameters and filters. It serves as the main execution entry point for the 'gathered'
        state operation.

        Purpose:
            Coordinates the execution of network settings extraction operations to generate
            Ansible-compatible YAML playbook configurations from existing Cisco Catalyst
            Center deployments (brownfield environments).

        Workflow Steps:
            1. Log workflow initiation with timestamp
            2. Validate operation registry and parameters
            3. Iterate through registered operations
            4. Check parameter availability for each operation
            5. Execute operation functions with error handling
            6. Track execution time per operation and total
            7. Aggregate results and operation summaries
            8. Log completion with performance metrics
        """
        self.log(
            "Starting brownfield network settings gathering workflow for state 'gathered' "
            "to extract existing configurations from Cisco Catalyst Center and generate "
            "Ansible-compatible YAML playbooks",
            "DEBUG"
        )

        # Record workflow start time for performance tracking
        workflow_start_time = time.time()

        self.log(
            "Workflow execution started at timestamp: {0}".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(workflow_start_time))
            ),
            "INFO"
        )

        # Define operations registry for this workflow state
        # Each tuple contains: (param_key, operation_name, operation_func)
        operations = [
            ("yaml_config_generator", "YAML Configuration Generator", self.yaml_config_generator)
        ]

        self.log(
            "Registered {0} operation(s) for execution in 'gathered' workflow: {1}".format(
                len(operations),
                [op[1] for op in operations]
            ),
            "DEBUG"
        )

        # Validate operations registry
        if not operations:
            error_msg = (
                "Operations registry is empty for state 'gathered' - no operations to execute"
            )
            self.log(error_msg, "ERROR")
            self.msg = error_msg
            self.status = "failed"
            return self

        # Track operation execution statistics
        operations_attempted = 0
        operations_executed = 0
        operations_skipped = 0
        operations_failed = 0

        # Execute each operation in sequence
        for operation_index, (param_key, operation_name, operation_func) in enumerate(operations, start=1):
            operations_attempted += 1

            self.log(
                "Processing operation {0}/{1}: '{2}' (checking for parameter key '{3}' "
                "in workflow state)".format(
                    operation_index, len(operations), operation_name, param_key
                ),
                "INFO"
            )

            # Validate operation function is callable
            if not operation_func or not callable(operation_func):
                error_msg = (
                    "Operation {0}/{1} '{2}' has invalid function reference (expected "
                    "callable, got {3}). Skipping operation.".format(
                        operation_index, len(operations), operation_name,
                        type(operation_func).__name__ if operation_func else "None"
                    )
                )
                self.log(error_msg, "ERROR")
                operations_skipped += 1
                continue

            # Check if parameters are available for this operation
            operation_params = self.want.get(param_key)

            if not operation_params:
                self.log(
                    "Operation {0}/{1} '{2}' has no parameters in workflow state "
                    "(parameter key '{3}' not found or empty). Skipping operation.".format(
                        operation_index, len(operations), operation_name, param_key
                    ),
                    "WARNING"
                )
                operations_skipped += 1
                continue

            # Validate operation parameters structure
            if not isinstance(operation_params, dict):
                self.log(
                    "Operation {0}/{1} '{2}' has invalid parameters structure - "
                    "expected dict, got {3}. Skipping operation.".format(
                        operation_index, len(operations), operation_name,
                        type(operation_params).__name__
                    ),
                    "WARNING"
                )
                operations_skipped += 1
                continue

            self.log(
                "Operation {0}/{1} '{2}' parameters found in workflow state with "
                "{3} configuration key(s): {4}. Starting operation execution.".format(
                    operation_index, len(operations), operation_name,
                    len(operation_params), list(operation_params.keys())
                ),
                "INFO"
            )

            # Record operation start time
            operation_start_time = time.time()

            self.log(
                "Executing operation '{0}' with parameters: {1}".format(
                    operation_name, operation_params
                ),
                "DEBUG"
            )

            try:
                # Execute the operation function with parameters
                operation_result = operation_func(operation_params)

                # Validate operation result
                if not operation_result:
                    self.log(
                        "Operation '{0}' completed but returned None result".format(
                            operation_name
                        ),
                        "WARNING"
                    )

                # Check operation status via check_return_status()
                # This will exit module if status is 'failed'
                operation_result.check_return_status()

                # Calculate operation execution time
                operation_end_time = time.time()
                operation_duration = operation_end_time - operation_start_time

                self.log(
                    "Operation {0}/{1} '{2}' completed successfully in {3:.2f} seconds".format(
                        operation_index, len(operations), operation_name, operation_duration
                    ),
                    "INFO"
                )

                operations_executed += 1

            except Exception as e:
                # Calculate operation execution time even on failure
                operation_end_time = time.time()
                operation_duration = operation_end_time - operation_start_time

                error_msg = (
                    "Operation {0}/{1} '{2}' failed after {3:.2f} seconds with error: {4}".format(
                        operation_index, len(operations), operation_name,
                        operation_duration, str(e)
                    )
                )
                self.log(error_msg, "ERROR")

                operations_failed += 1

                # Set failure status and message
                self.msg = (
                    "Workflow execution failed during operation '{0}': {1}".format(
                        operation_name, str(e)
                    )
                )
                self.status = "failed"

                # Exit immediately on operation failure
                # Note: check_return_status() will handle module exit
                return self

        # Calculate total workflow execution time
        workflow_end_time = time.time()
        workflow_duration = workflow_end_time - workflow_start_time

        # Log workflow completion summary
        self.log(
            "Brownfield network settings gathering workflow completed. "
            "Execution summary: attempted={0}, executed={1}, skipped={2}, failed={3}, "
            "total_duration={4:.2f} seconds".format(
                operations_attempted, operations_executed, operations_skipped,
                operations_failed, workflow_duration
            ),
            "INFO"
        )

        # Determine overall workflow success
        if operations_executed == 0:
            self.log(
                "No operations were executed - all operations were skipped or had invalid "
                "configurations. Workflow completed with warnings.",
                "WARNING"
            )
            self.msg = (
                "Workflow completed but no operations were executed. "
                "Verify configuration parameters."
            )
            self.status = "ok"
        elif operations_failed > 0:
            self.log(
                "Workflow completed with {0} operation failure(s)".format(operations_failed),
                "ERROR"
            )
            self.status = "failed"
        else:
            self.log(
                "All {0} operation(s) executed successfully without errors".format(
                    operations_executed
                ),
                "INFO"
            )
            # Note: Individual operation may have already set status to "success"
            # We preserve that status if it was set
            if self.status != "success":
                self.status = "ok"

        self.log(
            "Brownfield network settings gathering workflow execution finished at "
            "timestamp {0}. Total execution time: {1:.2f} seconds. Final status: {2}".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(workflow_end_time)),
                workflow_duration,
                self.status
            ),
            "INFO"
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center brownfield network settings playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield network settings extraction.

    Purpose:
        Initializes and executes the brownfield network settings playbook generator
        workflow to extract existing network configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create NetworkSettingsPlaybookGenerator instance
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
        - Introduced APIs for network settings retrieval:
            * Global IP Pools (retrieves_global_ip_address_pools)
            * Reserve IP Pools (retrieves_ip_address_subpools)
            * Network Management (get_network_v2)
            * Device Controllability (get_device_controllability_settings)
            * AAA Settings (retrieve_aaa_settings_for_a_site)

    Supported States:
        - gathered: Extract existing network settings and generate YAML playbook
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

    # Initialize the NetworkSettingsPlaybookGenerator object
    # This creates the main orchestrator for brownfield network settings extraction
    ccc_network_settings_playbook_generator = NetworkSettingsPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_network_settings_playbook_generator.log(
        "Starting Ansible module execution for brownfield network settings playbook "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_network_settings_playbook_generator.log(
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
    ccc_network_settings_playbook_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.7.9 for network settings APIs".format(
            ccc_network_settings_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    if (ccc_network_settings_playbook_generator.compare_dnac_versions(
            ccc_network_settings_playbook_generator.get_ccc_version(), "2.3.7.9") < 0):

        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for Network Settings module. Supported versions start "
            "from '2.3.7.9' onwards. Version '2.3.7.9' introduces APIs for retrieving "
            "network settings for the following components: Global Pool(s), Reserve "
            "Pool(s), Network Management, Device Controllability, and AAA Settings from "
            "the Catalyst Center.".format(
                ccc_network_settings_playbook_generator.get_ccc_version()
            )
        )

        ccc_network_settings_playbook_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_network_settings_playbook_generator.msg = error_msg
        ccc_network_settings_playbook_generator.set_operation_result(
            "failed", False, ccc_network_settings_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_network_settings_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required network settings APIs".format(
            ccc_network_settings_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_network_settings_playbook_generator.params.get("state")

    ccc_network_settings_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_network_settings_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_network_settings_playbook_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_network_settings_playbook_generator.supported_states
            )
        )

        ccc_network_settings_playbook_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_network_settings_playbook_generator.status = "invalid"
        ccc_network_settings_playbook_generator.msg = error_msg
        ccc_network_settings_playbook_generator.check_return_status()

    ccc_network_settings_playbook_generator.log(
        "State validation passed - using state '{0}' for workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_network_settings_playbook_generator.log(
        "Starting comprehensive input parameter validation for playbook configuration",
        "INFO"
    )

    ccc_network_settings_playbook_generator.validate_input().check_return_status()

    ccc_network_settings_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = ccc_network_settings_playbook_generator.validated_config

    ccc_network_settings_playbook_generator.log(
        "Starting configuration processing loop - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        ccc_network_settings_playbook_generator.log(
            "Processing configuration item {0}/{1} for state '{2}'".format(
                config_index, len(config_list), state
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_network_settings_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_network_settings_playbook_generator.reset_values()

        # Collect desired state (want) from configuration
        ccc_network_settings_playbook_generator.log(
            "Collecting desired state parameters from configuration item {0}".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_network_settings_playbook_generator.get_want(
            config, state
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_network_settings_playbook_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1}".format(state, config_index),
            "INFO"
        )
        ccc_network_settings_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_network_settings_playbook_generator.log(
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

    ccc_network_settings_playbook_generator.log(
        "Module execution completed successfully at timestamp {0}. Total execution "
        "time: {1:.2f} seconds. Processed {2} configuration item(s) with final "
        "status: {3}".format(
            completion_timestamp,
            module_duration,
            len(config_list),
            ccc_network_settings_playbook_generator.status
        ),
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_network_settings_playbook_generator.log(
        "Exiting Ansible module with result: {0}".format(
            ccc_network_settings_playbook_generator.result
        ),
        "DEBUG"
    )

    module.exit_json(**ccc_network_settings_playbook_generator.result)


if __name__ == "__main__":
    main()

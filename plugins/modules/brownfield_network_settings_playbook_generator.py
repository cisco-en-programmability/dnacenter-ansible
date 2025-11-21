#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
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
version_added: 6.17.0
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
    choices: [merged]
    default: merged
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
          a default file name "network_settings_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "network_settings_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
        required: false
      global_filters:
        description:
        - Global filters to apply when generating the YAML configuration file.
        - These filters identify which network settings to extract configurations from.
        - At least one filter type must be specified to identify target settings.
        type: dict
        required: false
        suboptions:
          site_name_list:
            description:
            - List of site names to extract network settings from.
            - HIGHEST PRIORITY - If provided, other site-based filters will be applied within these sites.
            - Each site name must follow the hierarchical format (e.g., "Global/India/Mumbai").
            - Sites must exist in Cisco Catalyst Center.
            - Example ["Global/India/Mumbai", "Global/USA/NewYork", "Global/Headquarters"]
            type: list
            elements: str
            required: false
          pool_name_list:
            description:
            - List of IP pool names to extract configurations from.
            - Can be applied to both global pools and reserve pools.
            - Pool names must match those configured in Catalyst Center.
            - Example ["Global_Pool_1", "Production_Pool", "Corporate_Pool"]
            type: list
            elements: str
            required: false
          pool_type_list:
            description:
            - List of pool types to extract configurations from.
            - Valid values are ["Generic", "LAN", "WAN", "Management"].
            - Can be applied to both global pools and reserve pools.
            - Example ["LAN", "Management"]
            type: list
            elements: str
            required: false
            choices: ["Generic", "LAN", "WAN", "Management"]
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
              "device_controllability_details", "aaa_settings"]
            - If not specified, all supported components are included.
            - Example ["global_pool_details", "reserve_pool_details", "network_management_details"]
            type: list
            elements: str
            required: false
            choices: ["global_pool_details", "reserve_pool_details", "network_management_details", 
                     "device_controllability_details", "aaa_settings"]
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
            - Reserve IP Pools to filter by pool name, site, or pool type.
            type: list
            elements: dict
            required: false
            suboptions:
              pool_name:
                description:
                - Reserve pool name to filter by name.
                type: str
                required: false
              site_name:
                description:
                - Site name to filter reserve pools by site.
                type: str
                required: false
              pool_type:
                description:
                - Pool type to filter reserve pools by type (LAN, WAN, Management).
                type: str
                required: false
                choices: ["LAN", "WAN", "Management"]
          network_management_details:
            description:
            - Network management settings to filter by site or NTP server.
            type: list
            elements: dict
            required: false
            suboptions:
              site_name:
                description:
                - Site name to filter network management settings by site.
                type: str
                required: false
              ntp_server:
                description:
                - NTP server to filter by NTP configuration.
                type: str
                required: false
          device_controllability_details:
            description:
            - Device controllability settings to filter by site.
            type: list
            elements: dict
            required: false
            suboptions:
              site_name:
                description:
                - Site name to filter device controllability settings by site.
                type: str
                required: false
          aaa_settings:
            description:
            - AAA settings to filter by network or server type.
            type: list
            elements: dict
            required: false
            suboptions:
              network:
                description:
                - Network to filter AAA settings by network.
                type: str
                required: false
              server_type:
                description:
                - Server type to filter AAA settings (ISE, AAA).
                type: str
                required: false
                choices: ["ISE", "AAA"]
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - network_settings.NetworkSettings.retrieves_global_ip_address_pools
    - network_settings.NetworkSettings.retrieves_ip_address_subpools  
    - network_settings.NetworkSettings.get_network_v2
    - network_settings.NetworkSettings.get_device_credential_details
    - network_settings.NetworkSettings.get_network_v2_aaa
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
    state: merged
    config:
      - global_filters:
          site_name_list: ["Global/India/Mumbai"]

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
    state: merged
    config:
      - file_path: "/tmp/network_settings_config.yml"
        global_filters:
          site_name_list: ["Global/India/Mumbai", "Global/India/Delhi", "Global/USA/NewYork"]

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
    state: merged
    config:
      - file_path: "/tmp/network_settings_config.yml"
        global_filters:
          site_name_list: ["Global/India/Mumbai", "Global/India/Delhi"]
        component_specific_filters:
          components_list: ["global_pool_details", "reserve_pool_details", "network_management_details"]

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
    state: merged
    config:
      - file_path: "/tmp/network_settings_config.yml"
        component_specific_filters:
          components_list: ["global_pool_details"]
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
        self.supported_states = ["merged"]
        super().__init__(module)
        self.module_schema = self.get_workflow_elements_schema()
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
            "merged": self.get_diff_merged,
        }

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
        Validates the configuration parameters.
        Args:
            config (dict): Configuration parameters to validate
        Returns:
            self: Returns self with validation status
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
            supported_components = list(self.module_schema.get("network_elements", {}).keys())
            
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
            "ip_address_space": {"type": "str", "source_key": "ipv6", "transform": self.transform_ipv6_to_address_space},
            "cidr": {"type": "str", "source_key": "addressSpace.subnet", "transform": self.transform_cidr},
            "gateway": {"type": "str", "source_key": "addressSpace.gatewayIpAddress"},
            "dhcp_server_ips": {"type": "list", "source_key": "addressSpace.dhcpServers"},
            "dns_server_ips": {"type": "list", "source_key": "addressSpace.dnsServers"},
        })

    def transform_ipv6_to_address_space(self, ipv6_value):
        """
        Transforms ipv6 boolean to address space string.
        """
        if ipv6_value is True:
            return "IPv6"
        elif ipv6_value is False:
            return "IPv4"
        return None

    def transform_cidr(self, pool_details):
        """
        Transforms subnet and prefix to CIDR format.
        """
        if isinstance(pool_details, dict):
            address_space = pool_details.get("addressSpace", {})
            subnet = address_space.get("subnet")
            prefix_length = address_space.get("prefixLength")
            if subnet and prefix_length:
                return "{0}/{1}".format(subnet, prefix_length)
        return None

    def reserve_pool_reverse_mapping_function(self, requested_components=None):
        """
        Reverse mapping for Reserve Pool Details — converts API response fields
        into Ansible-friendly config keys as per reserve_pool_details schema.
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
                "transform": lambda x: bool(x),
            },

            # IPv4 address space
            "ipv4_global_pool": {"type": "str", "source_key": "ipV4AddressSpace.globalPoolId"},
            "ipv4_prefix": {
                "type": "bool",
                "source_key": "ipV4AddressSpace.prefixLength",
                "transform": lambda x: True if x else False,
            },
            "ipv4_prefix_length": {"type": "int", "source_key": "ipV4AddressSpace.prefixLength"},
            "ipv4_subnet": {"type": "str", "source_key": "ipV4AddressSpace.subnet"},
            "ipv4_gateway": {"type": "str", "source_key": "ipV4AddressSpace.gatewayIpAddress"},
            "ipv4_dhcp_servers": {"type": "list", "source_key": "ipV4AddressSpace.dhcpServers"},
            "ipv4_dns_servers": {"type": "list", "source_key": "ipV4AddressSpace.dnsServers"},
            "ipv4_total_host": {"type": "int", "source_key": "ipV4AddressSpace.totalAddresses"},
            "ipv4_unassignable_addresses": {"type": "int", "source_key": "ipV4AddressSpace.unassignableAddresses"},
            "ipv4_assigned_addresses": {"type": "int", "source_key": "ipV4AddressSpace.assignedAddresses"},
            "ipv4_default_assigned_addresses": {"type": "int", "source_key": "ipV4AddressSpace.defaultAssignedAddresses"},

            # IPv6 address space
            "ipv6_global_pool": {"type": "str", "source_key": "ipV6AddressSpace.globalPoolId"},
            "ipv6_prefix": {
                "type": "bool",
                "source_key": "ipV6AddressSpace.prefixLength",
                "transform": lambda x: True if x else False,
            },
            "ipv6_prefix_length": {"type": "int", "source_key": "ipV6AddressSpace.prefixLength"},
            "ipv6_subnet": {"type": "str", "source_key": "ipV6AddressSpace.subnet"},
            "ipv6_gateway": {"type": "str", "source_key": "ipV6AddressSpace.gatewayIpAddress"},
            "ipv6_dhcp_servers": {"type": "list", "source_key": "ipV6AddressSpace.dhcpServers"},
            "ipv6_dns_servers": {"type": "list", "source_key": "ipV6AddressSpace.dnsServers"},
            "ipv6_total_host": {"type": "int", "source_key": "ipV6AddressSpace.totalAddresses"},
            "ipv6_unassignable_addresses": {"type": "int", "source_key": "ipV6AddressSpace.unassignableAddresses"},
            "ipv6_assigned_addresses": {"type": "int", "source_key": "ipV6AddressSpace.assignedAddresses"},
            "ipv6_default_assigned_addresses": {"type": "int", "source_key": "ipV6AddressSpace.defaultAssignedAddresses"},
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

    def modify_network_parameters(self, params):
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
                normalized[key] = self.modify_network_parameters(value)
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
            # "site_name": {
            #     "type": "str",
            #     "special_handling": True,
            #     "transform": self.transform_site_location,
            # },
            "device_controllability": {"type": "bool", "source_key": "deviceControllability"},
            "autocorrect_telemetry_config": {"type": "bool", "source_key": "autocorrectTelemetryConfig"},
        })

    def aaa_settings_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for AAA settings configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for AAA settings details
        """
        self.log("Generating reverse mapping specification for AAA settings.", "DEBUG")
        
        return OrderedDict({
            "network": {"type": "str", "source_key": "network"},
            "protocol": {"type": "str", "source_key": "protocol"},
            "servers": {"type": "str", "source_key": "servers"},
            "server_type": {"type": "str", "source_key": "serverType"},
            "shared_secret": {"type": "str", "source_key": "sharedSecret"},
        })

    def transform_site_location(self, pool_details):
        """
        Transforms site location information for a given pool by extracting and mapping
        the site hierarchy based on the site ID.
        Args:
            pool_details (dict): A dictionary containing pool-specific information, including the 'siteId' key.
        Returns:
            str: The hierarchical name of the site (e.g., "Global/Site/Building").
        """
        self.log("Transforming site location for pool details: {0}".format(pool_details), "DEBUG")
        site_id = pool_details.get("siteId")
        if not site_id:
            return None
            
        # Create site ID to name mapping if not exists
        if not hasattr(self, 'site_id_name_dict'):
            self.site_id_name_dict = self.get_site_id_name_mapping()
            
        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        return site_name_hierarchy

    def reset_operation_tracking(self):
        """
        Resets the operation tracking variables for a new operation.
        """
        self.log("Resetting operation tracking variables for new operation", "DEBUG")
        self.operation_successes = []
        self.operation_failures = []
        self.total_sites_processed = 0
        self.total_components_processed = 0
        self.log("Operation tracking variables reset successfully", "DEBUG")

    def add_success(self, site_name, component, additional_info=None):
        """
        Adds a successful operation to the tracking list.
        Args:
            site_name (str): Site name that succeeded.
            component (str): Component name that succeeded.
            additional_info (dict): Additional information about the success.
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
        Adds a failed operation to the tracking list.
        Args:
            site_name (str): Site name that failed.
            component (str): Component name that failed.
            error_info (dict): Error information containing error details.
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

        params = {}
        component_specific_filters = filters.get("component_specific_filters", {}).get("global_pool_details", [])
        
        if component_specific_filters:
            for filter_param in component_specific_filters:
                for key, value in filter_param.items():
                    if key == "pool_name":
                        params["ipPoolName"] = value
                    elif key == "pool_type":
                        params["ipPoolType"] = value
                    else:
                        self.log("Ignoring unsupported filter parameter: {0}".format(key), "DEBUG")
                        
                global_pool_details = self.execute_get_with_pagination(api_family, api_function, params)
                self.log("Retrieved global pool details: {0}".format(len(global_pool_details)), "INFO")
                final_global_pools.extend(global_pool_details)
        else:
            # Execute API call to retrieve global pool details
            global_pool_details = self.execute_get_with_pagination(api_family, api_function, params)
            self.log("Retrieved global pool details: {0}".format(len(global_pool_details)), "INFO")
            final_global_pools.extend(global_pool_details)

        # Track success
        self.add_success("Global", "global_pool_details", {
            "pools_processed": len(final_global_pools)
        })

        # Apply reverse mapping
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        reverse_mapping_spec = reverse_mapping_function()
        
        # Transform using modify_network_parameters
        pools_details = self.modify_network_parameters(reverse_mapping_spec, final_global_pools)
        
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
            # All sites
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

        self.log("Completed NM retrieval for all targeted sites. Total sites processed: {0}".format(self.pprint(final_nm_details)), "INFO")
        self.log(self.pprint(nm_details), "DEBUG")

        # === APPLY UNIFIED NM REVERSE MAPPING BEFORE RETURN ===
        try:
            self.log("Applying NM unified reverse mapping...", "INFO")

            transformed_nm = []

            for entry in final_nm_details:
                self.log("Processing NM entry for site: {0}".format(entry.get("site_name")), "DEBUG")
                site_name = entry.get("site_name")

                # ---- Clean / normalize DNAC response ----
                # entry = self.modify_parameters(entry)
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

        return {
            "primary_server_address": data.get("primaryServerIp", ""),
            "secondary_server_address": data.get("secondaryServerIp", ""),
            "protocol": data.get("protocol", ""),
            "server_type": data.get("serverType", ""),
        }

    def extract_client_aaa(self, entry):
        data = entry.get("aaaClient", {})
        if not data:
            return {}

        return {
            "primary_server_address": data.get("primaryServerIp", ""),
            "secondary_server_address": data.get("secondaryServerIp", ""),
            "protocol": data.get("protocol", ""),
            "server_type": data.get("serverType", ""),
        }

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
        
        # Process site-based filtering first
        target_sites = []
        site_name_list = global_filters.get("site_name_list", [])
        
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

        # If no target sites specified, get all sites
        if not target_sites:
            self.log("No specific sites targeted, processing all sites", "DEBUG")
            if not hasattr(self, 'site_id_name_dict'):
                self.site_id_name_dict = self.get_site_id_name_mapping()
            
            for site_id, site_name in self.site_id_name_dict.items():
                target_sites.append({"site_name": site_name, "site_id": site_id})

        # Process each site
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
                        if filter_site_name and filter_site_name != site_name:
                            continue  # Skip this filter as it's for a different site
                        
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
                        
                        # Check pool type filter (note: pool_type_list might contain Management, but API uses different values)
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
            # Create unique identifier based on site ID, group name, and type
            pool_identifier = "{0}_{1}_{2}".format(
                pool.get("siteId", ""), 
                pool.get("groupName", ""), 
                pool.get("type", "")
            )
            
            if pool_identifier not in seen_pools:
                seen_pools.add(pool_identifier)
                unique_pools.append(pool)

        final_reserve_pools = unique_pools
        self.log("After deduplication, total reserve pools: {0}".format(len(final_reserve_pools)), "INFO")

        if not final_reserve_pools:
            self.log("No reserve pools found matching the specified criteria", "INFO")
            return {
                "reserve_pool_details": [],
                "operation_summary": self.get_operation_summary()
            }

        # Apply reverse mapping
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        reverse_mapping_spec = reverse_mapping_function()
        
        # Transform using modify_network_parameters
        pools_details = self.modify_network_parameters(reverse_mapping_spec, final_reserve_pools)
        
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

        return {
            "device_controllability_details": settings_details,
            "operation_summary": self.get_operation_summary(),
        }

    def get_aaa_settings(self, network_element, filters):
        """Placeholder for AAA settings implementation"""
        self.log("AAA settings retrieval not yet implemented", "WARNING")
        return {"aaa_settings": [], "operation_summary": self.get_operation_summary()}

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
                final_list.extend([details])
                self.log("Added component {0} to final list (including empty results)".format(component), "DEBUG")
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
            state (str): The desired state of the network elements ('merged').
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

    def get_diff_merged(self):
        """
        Executes the merge operations for various network configurations in the Cisco Catalyst Center.
        """
        start_time = time.time()
        self.log("Starting 'get_diff_merged' operation.", "DEBUG")
        
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
        self.log("Completed 'get_diff_merged' operation in {0:.2f} seconds.".format(end_time - start_time), "DEBUG")
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
        "state": {"default": "merged", "choices": ["merged"]},
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

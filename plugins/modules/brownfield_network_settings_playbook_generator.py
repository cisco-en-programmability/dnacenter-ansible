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
          components_list: ["global_pool_details", "reserve_pool_details"]

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
                        "ntp_server": {
                            "type": "str",
                            "required": False
                        }
                    },
                    "reverse_mapping_function": self.network_management_reverse_mapping_function,
                    "api_function": "get_network_v2",
                    "api_family": "network_settings",
                    "get_function_name": self.get_network_management_settings,
                },
                "device_controllability_details": {
                    "filters": {
                        "site_name": {
                            "type": "str",
                            "required": False
                        }
                    },
                    "reverse_mapping_function": self.device_controllability_reverse_mapping_function,
                    "api_function": "get_device_credential_details",
                    "api_family": "network_settings",
                    "get_function_name": self.get_device_controllability_settings,
                },
                "aaa_settings": {
                    "filters": {
                        "network": {
                            "type": "str",
                            "required": False
                        },
                        "server_type": {
                            "type": "str",
                            "required": False,
                            "choices": ["ISE", "AAA"]
                        }
                    },
                    "reverse_mapping_function": self.aaa_settings_reverse_mapping_function,
                    "api_function": "get_network_v2_aaa",
                    "api_family": "network_settings",
                    "get_function_name": self.get_aaa_settings,
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
        Returns the reverse mapping specification for reserve pool configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for reserve pool details
        """
        self.log("Generating reverse mapping specification for reserve pools.", "DEBUG")
        
        return OrderedDict({
            "name": {"type": "str", "source_key": "groupName"},
            "site_name": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_site_location,
            },
            "pool_type": {"type": "str", "source_key": "type"},
            "ipv6_address_space": {"type": "bool", "source_key": "ipv6"},
            "ipv4_global_pool_name": {"type": "str", "source_key": "ipv4GlobalPool"},
            "ipv4_prefix": {"type": "bool", "source_key": "ipv4Prefix"},
            "ipv4_prefix_length": {"type": "int", "source_key": "ipv4PrefixLength"},
            "ipv4_subnet": {"type": "str", "source_key": "ipv4Subnet"},
            "ipv4_gateway": {"type": "str", "source_key": "ipv4Gateway"},
            "ipv4_dns_servers": {"type": "list", "source_key": "ipv4DnsServers"},
            "ipv6_prefix": {"type": "bool", "source_key": "ipv6Prefix"},
            "ipv6_prefix_length": {"type": "int", "source_key": "ipv6PrefixLength"},
            "ipv6_global_pool": {"type": "str", "source_key": "ipv6GlobalPool"},
            "ipv6_subnet": {"type": "str", "source_key": "ipv6Subnet"},
            "slaac_support": {"type": "bool", "source_key": "slaacSupport"},
        })

    def network_management_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for network management configurations.
        Args:
            requested_components (list, optional): List of specific components to include
        Returns:
            dict: Reverse mapping specification for network management details
        """
        self.log("Generating reverse mapping specification for network management settings.", "DEBUG")
        
        return OrderedDict({
            "site_name": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_site_location,
            },
            "ntp_server": {"type": "list", "source_key": "ntpServer"},
            "dhcp_server": {"type": "list", "source_key": "dhcpServer"},
            "dns_server": {"type": "dict", "source_key": "dnsServer"},
            "timezone": {"type": "str", "source_key": "timezone"},
            "message_of_the_day": {"type": "dict", "source_key": "messageOfTheday"},
            "netflow_collector": {"type": "dict", "source_key": "netflowcollector"},
            "snmp_server": {"type": "dict", "source_key": "snmpServer"},
            "syslog_server": {"type": "dict", "source_key": "syslogServer"},
        })

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
            "site_name": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_site_location,
            },
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
        
        # Transform using modify_parameters
        pools_details = self.modify_parameters(reverse_mapping_spec, final_global_pools)
        
        return {
            "global_pool_details": {
                "settings": {
                    "ip_pool": pools_details
                }
            },
            "operation_summary": self.get_operation_summary()
        }

    # Placeholder methods for other components
    def get_reserve_pools(self, network_element, filters):
        """Placeholder for reserve pools implementation"""
        self.log("Reserve pools retrieval not yet implemented", "WARNING")
        return {"reserve_pool_details": [], "operation_summary": self.get_operation_summary()}

    def get_network_management_settings(self, network_element, filters):
        """Placeholder for network management implementation"""
        self.log("Network management retrieval not yet implemented", "WARNING")
        return {"network_management_details": [], "operation_summary": self.get_operation_summary()}

    def get_device_controllability_settings(self, network_element, filters):
        """Placeholder for device controllability implementation"""
        self.log("Device controllability retrieval not yet implemented", "WARNING")
        return {"device_controllability_details": [], "operation_summary": self.get_operation_summary()}

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

            if details and details.get(component):
                final_list.extend([details])

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

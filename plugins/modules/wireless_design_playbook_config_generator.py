#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wireless Design Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Rugvedi Kapse, Sunil Shatagopa, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: wireless_design_playbook_config_generator
short_description: Generate YAML playbook for C(wireless_design_workflow_manager) module.
description:
- Generates YAML configurations compatible with the C(wireless_design_workflow_manager)
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the wireless settings configured on
  the Cisco Catalyst Center.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Rugvedi Kapse (@rukapse)
- Sunil Shatagopa (@shatagopasunil)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A dictionary of filters for generating YAML playbook compatible with the `wireless_design_workflow_manager` module.
    - Filters specify which components to include in the YAML configuration file.
    - If C(components_list) is specified, only those components are included, regardless of the filters.
    type: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - When set to C(true), the module generates configurations for all wireless settings
          in the Cisco Catalyst Center, ignoring any provided filters.
        - When enabled, the config parameter becomes optional and will use default values if not provided.
        - A default filename will be generated automatically if file_path is not specified.
        - This is useful for complete playbook configuration infrastructure discovery and documentation.
        - When set to false, the module uses provided filters to generate a targeted YAML configuration.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  C(wireless_design_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(wireless_design_playbook_config_2026-02-20_13-34-58.yml).
        type: str
      file_mode:
        description:
        - Controls how config is written to the YAML file.
        - C(overwrite) replaces existing file content.
        - C(append) appends generated YAML content to the existing file.
        type: str
        choices: ["overwrite", "append"]
        default: "overwrite"
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration file.
        - If C(components_list) is specified, only those components are included, regardless of other filters.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are
              - Wireless SSIDs "ssids"
              - Interfaces "interfaces"
              - Power Profiles "power_profiles"
              - Access Point Profiles "access_point_profiles"
              - Radio Frequency Profiles "radio_frequency_profiles"
              - Anchor Groups "anchor_groups"
              - Feature Template Config "feature_template_config"
              - 802.11be Profiles "802_11_be_profiles"
              - Flex Connect Configuration "flex_connect_configuration"
            - If not specified, all components are included.
            type: list
            elements: str
            choices: ["ssids", "interfaces", "power_profiles", "access_point_profiles", "radio_frequency_profiles",
                      "anchor_groups", "feature_template_config", "802_11_be_profiles", "flex_connect_configuration"]
          ssids:
            description:
            - Filters for SSID retrieval.
            type: list
            elements: dict
            suboptions:
              site_name_hierarchy:
                description:
                - Filter SSIDs by site name hierarchy.
                type: str
              ssid_name:
                description:
                - Filter SSIDs by SSID name.
                type: str
              ssid_type:
                description:
                - Filter SSIDs by SSID type.
                type: str
                choices: ["Enterprise", "Guest"]
          interfaces:
            description:
            - Filters for wireless interface retrieval.
            type: list
            elements: dict
            suboptions:
              interface_name:
                description:
                - Filter interfaces by interface name.
                type: str
              vlan_id:
                description:
                - Filter interfaces by VLAN ID.
                type: int
          power_profiles:
            description:
            - Filters for wireless power profile retrieval.
            type: list
            elements: dict
            suboptions:
              power_profile_name:
                description:
                - Filter power profiles by power profile name.
                type: str
          access_point_profiles:
            description:
            - Filters for access point profile retrieval.
            type: list
            elements: dict
            suboptions:
              ap_profile_name:
                description:
                - Filter AP profiles by AP profile name.
                type: str
          radio_frequency_profiles:
            description:
            - Filters for radio frequency profile retrieval.
            type: list
            elements: dict
            suboptions:
              rf_profile_name:
                description:
                - Filter radio frequency profiles by RF profile name.
                type: str
          anchor_groups:
            description:
            - Filters for anchor group retrieval.
            type: list
            elements: dict
            suboptions:
              anchor_group_name:
                description:
                - Filter anchor groups by anchor group name.
                type: str
          feature_template_config:
            description:
            - Filters for wireless feature template configuration retrieval.
            type: list
            elements: dict
            suboptions:
              feature_template_type:
                description:
                - Filter by feature template type.
                type: str
                choices: ["aaa_radius_attribute", "advanced_ssid", "clean_air_configuration", "dot11ax_configuration",
                          "dot11be_configuration", "event_driven_rrm_configuration", "flexconnect_configuration",
                          "multicast_configuration", "rrm_fra_configuration", "rrm_general_configuration"]
              design_name:
                description:
                - Filter by feature template design name.
                type: str
          802_11_be_profiles:
            description:
            - Filters for 802.11be profile retrieval.
            type: list
            elements: dict
            suboptions:
              profile_name:
                description:
                - Filter 802.11be profiles by profile name.
                type: str
          flex_connect_configuration:
            description:
            - Filters for flex connect configuration retrieval.
            type: list
            elements: dict
            suboptions:
              site_name_hierarchy:
                description:
                - Filter flex connect configuration by site name hierarchy.
                type: str

requirements:
- dnacentersdk >= 2.3.7.9
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - site_design.SiteDesigns.get_sites
    - wirelesss.Wireless.get_ssid_by_site
    - wirelesss.Wireless.get_interfaces
    - wirelesss.Wireless.get_power_profiles
    - wirelesss.Wireless.get_ap_profiles
    - wirelesss.Wireless.get_rf_profiles
    - wirelesss.Wireless.get_anchor_groups
- Paths used are
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/sites/${siteId}/wirelessSettings/ssids
    - GET /dna/intent/api/v1/wirelessSettings/interfaces
    - GET /dna/intent/api/v1/wirelessSettings/powerProfiles
    - GET /dna/intent/api/v1/wirelessSettings/apProfiles
    - GET /dna/intent/api/v1/wirelessSettings/rfProfiles
    - GET /dna/intent/api/v1/wirelessSettings/anchorGroups
seealso:
- module: cisco.dnac.wireless_design_workflow_manager
  description: Module for managing wireless design and feature template config.
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with File Path specified
  cisco.dnac.wireless_design_playbook_config_generator:
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
      generate_all_configurations: true
      file_path: "tmp/catc_wireless_config.yml"
      file_mode: "overwrite"

- name: Generate YAML Configuration with specific wireless network components only
  cisco.dnac.wireless_design_playbook_config_generator:
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
      file_path: "tmp/catc_wireless_components_config.yml"
      file_mode: "overwrite"
      component_specific_filters:
        components_list: ["interfaces", "anchor_groups"]

- name: Generate YAML Configuration for wireless SSIDs with site filter
  cisco.dnac.wireless_design_playbook_config_generator:
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
      file_path: "tmp/catc_wireless_components_config.yml"
      file_mode: "overwrite"
      component_specific_filters:
        components_list: ["ssids"]
        ssids:
          - site_name_hierarchy: "Global/USA/San Jose"

- name: Generate YAML Configuration with multiple filters
  cisco.dnac.wireless_design_playbook_config_generator:
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
      file_path: "/tmp/catc_wireless_components_config.yaml"
      file_mode: "append"
      component_specific_filters:
        components_list: ["ssids", "feature_template_config"]
        ssids:
          - ssid_name: sample_ssid
            ssid_type: Guest
        feature_template_config:
          - feature_template_type: advanced_ssid
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": {
            "components_processed": 9,
            "components_skipped": 0,
            "configurations_count": 9,
            "file_path": "tmp/all_configurations.yml",
            "message": "YAML configuration file generated successfully for module 'wireless_design_workflow_manager'",
            "status": "success"
        },
        "response": {
            "components_processed": 9,
            "components_skipped": 0,
            "configurations_count": 9,
            "file_path": "tmp/all_configurations.yml",
            "message": "YAML configuration file generated successfully for module 'wireless_design_workflow_manager'",
            "status": "success"
        },
        "status": "success"
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg":
            "Validation Error: 'component_specific_filters' must be provided with 'components_list' key
             when 'generate_all_configurations' is set to False.",
        "response":
            "Validation Error: 'component_specific_filters' must be provided with 'components_list' key
             when 'generate_all_configurations' is set to False."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase
)
import time
import re
from collections import OrderedDict


class WirelessDesignPlaybookConfigGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook config for wireless design deployed within the Cisco Catalyst Center using the GET APIs.
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
        self.module_name = "wireless_design_workflow_manager"
        self.country_code_map = None

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
            "generate_all_configurations": {
                "type": "bool",
                "required": False,
                "default": False
            },
            "file_path": {
                "type": "str",
                "required": False
            },
            "file_mode": {
                "type": "str",
                "required": False,
                "default": "overwrite",
                "choices": ["overwrite", "append"]
            },
            "component_specific_filters": {
                "type": "dict",
                "required": False
            }
        }

        # Validate params
        self.log("Validating configuration against schema", "DEBUG")
        valid_temp = self.validate_config_dict(self.config, temp_spec)

        self.log("Validating invalid parameters against provided config", "DEBUG")
        self.validate_invalid_params(self.config, temp_spec.keys())

        self.log("Validating minimum requirements against provided config: {0}".format(self.config), "DEBUG")
        self.validate_minimum_requirements(self.config)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_elements_schema(self):
        """
        Constructs and returns a structured mapping for managing wireless settings information
        such as ssids, interfaces, power_profiles, ap_profiles, rf_profiles and anchor_groups.
        This mapping includes associated filters, temporary specification functions, API details,
        and fetch function references used in the wireless design workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods like
                `wireless_ssid_temp_spec`, `wireless_interfaces_temp_spec`, etc.

        Return:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a network component
                (e.g., 'ssids', 'interfaces', 'power_profiles', 'access_point_profiles',
                'radio_frequency_profiles', 'anchor_groups') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'wireless').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
        """

        self.log("Building workflow filters schema for wireless design module.", "DEBUG")

        schema = {
            "network_elements": {
                "ssids": {
                    "filters": {
                        "site_name_hierarchy": {"type": "str"},
                        "ssid_name": {"type": "str"},
                        "ssid_type": {
                            "type": "str",
                            "choices": ["Enterprise", "Guest"]
                        },
                    },
                    "reverse_mapping_function": self.wireless_ssid_temp_spec,
                    "api_function": "get_ssid_by_site",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_ssids,
                },
                "interfaces": {
                    "filters": {
                        "interface_name": {"type": "str"},
                        "vlan_id": {"type": "int"}
                    },
                    "reverse_mapping_function": self.wireless_interfaces_temp_spec,
                    "api_function": "get_interfaces",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_interfaces,
                },
                "power_profiles": {
                    "filters": {
                        "power_profile_name": {"type": "str"}
                    },
                    "reverse_mapping_function": self.wireless_power_profiles_temp_spec,
                    "api_function": "get_power_profiles",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_power_profiles,
                },
                "access_point_profiles": {
                    "filters": {
                        "ap_profile_name": {"type": "str"}
                    },
                    "reverse_mapping_function": self.wireless_access_point_profiles_temp_spec,
                    "api_function": "get_ap_profiles",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_access_point_profiles,
                },
                "radio_frequency_profiles": {
                    "filters": {
                        "rf_profile_name": {"type": "str"}
                    },
                    "reverse_mapping_function": self.wireless_radio_frequency_profiles_temp_spec,
                    "api_function": "get_rf_profiles",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_radio_frequency_profiles,
                },
                "anchor_groups": {
                    "filters": {
                        "anchor_group_name": {"type": "str"}
                    },
                    "reverse_mapping_function": self.wireless_anchor_groups_temp_spec,
                    "api_function": "get_anchor_groups",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_anchor_groups,
                },
                "feature_template_config": {
                    "filters": {
                        "feature_template_type": {
                            "type": "str",
                            "choices": [
                                "aaa_radius_attribute",
                                "advanced_ssid",
                                "clean_air_configuration",
                                "dot11ax_configuration",
                                "dot11be_configuration",
                                "event_driven_rrm_configuration",
                                "flexconnect_configuration",
                                "multicast_configuration",
                                "rrm_fra_configuration",
                                "rrm_general_configuration"
                            ]
                        },
                        "design_name": {"type": "str"}
                    },
                    "api_function": "get_feature_template_summary",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_feature_template_config,
                },
                "802_11_be_profiles": {
                    "filters": {
                        "profile_name": {"type": "str"}
                    },
                    "reverse_mapping_function": self.wireless_802_11_be_profiles_temp_spec,
                    "api_function": "get80211be_profiles",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_802_11_be_profiles
                },
                "flex_connect_configuration": {
                    "filters": {
                        "site_name_hierarchy": {"type": "str"}
                    },
                    "reverse_mapping_function": self.wireless_flex_connect_config_temp_spec,
                    "api_function": "get_native_vlan_settings_by_site",
                    "api_family": "wireless",
                    "get_function_name": self.get_wireless_flex_connect_configurations
                },
            }
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network element(s): {network_elements}",
            "INFO",
        )

        return schema

    def wireless_ssid_temp_spec(self):
        """
        Constructs a temporary specification for wireless ssid config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as ssid name,
        wlan_profile_name, ssid_type etc.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless ssid attributes.
        """

        self.log("Generating temporary specification for Wireless SSID config", "DEBUG")

        wireless_ssid_temp_spec = OrderedDict(
            {
                "ssid_name": {"type": "str", "source_key": "ssid"},
                "ssid_type": {"type": "str", "source_key": "wlanType"},
                "wlan_profile_name": {"type": "str", "source_key": "profileName"},
                "radio_policy": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "radio_bands": {
                                "type": "list",
                                "source_key": "ssidRadioType",
                                "transform": self.transform_radio_bands,
                            },
                            "2_dot_4_ghz_band_policy": {
                                "type": "str",
                                "source_key": "ghz24Policy",
                                "transform": self.transform_2_dot_4_ghz_band_policy,
                            },
                            "band_select": {"type": "bool", "source_key": "wlanBandSelectEnable"},
                            "6_ghz_client_steering": {"type": "bool", "source_key": "ghz6PolicyClientSteering"}
                        }
                    )
                },
                "fast_lane": {"type": "bool", "source_key": "isFastLaneEnabled"},
                "quality_of_service": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "egress": {"type": "str", "source_key": "egressQos"},
                            "ingress": {"type": "str", "source_key": "ingressQos"}
                        }
                    )
                },
                "ssid_state": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "admin_status": {"type": "bool", "source_key": "isEnabled"},
                            "broadcast_ssid": {"type": "bool", "source_key": "isBroadcastSSID"}
                        }
                    )
                },
                "l2_security": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "l2_auth_type": {"type": "str", "source_key": "authType"},
                            "ap_beacon_protection": {"type": "bool", "source_key": "isApBeaconProtectionEnabled"},
                            "open_ssid": {"type": "str", "source_key": "openSsid"},
                            "passphrase_type": {
                                "type": "str",
                                "source_key": "isHex",
                                "transform": lambda isHex: "HEX" if isHex else "ASCII"
                            },
                            "passphrase": {
                                "type": "str",
                                "source_key": "passphrase",
                                "special_handling": True,
                                "transform": lambda ssid_details: self.generate_placeholder_using_component_details(
                                    ssid_details, "ssid", "ssid", "passphrase"
                                ),
                            }
                        }
                    )
                },
                "fast_transition": {"type": "str", "source_key": "fastTransition"},
                "fast_transition_over_the_ds": {"type": "bool", "source_key": "fastTransitionOverTheDistributedSystemEnable"},
                "wpa_encryption": {
                    "type": "list",
                    "special_handling": True,
                    "transform": self.transform_ssid_wpa_encryption
                },
                "auth_key_management": {
                    "type": "list",
                    "special_handling": True,
                    "transform": self.transform_auth_key_management
                },
                "cckm_timestamp_tolerance": {"type": "int", "source_key": "cckmTsfTolerance"},
                "l3_security": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "l3_auth_type": {
                                "type": "str",
                                "source_key": "l3AuthType",
                                "transform": lambda x: x.upper() if x is not None else x
                            },
                            "auth_server": {
                                "type": "str",
                                "special_handling": True,
                                "transform": self.transform_l3_security_auth_server,
                            },
                            "web_auth_url": {"type": "str", "source_key": "externalAuthIpAddress"},
                            "enable_sleeping_client": {"type": "bool", "source_key": "sleepingClientEnable"},
                            "sleeping_client_timeout": {"type": "int", "source_key": "sleepingClientTimeout"},
                        }
                    )
                },
                "aaa": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "auth_servers_ip_address_list": {"type": "list", "source_key": "authServers"},
                            "accounting_servers_ip_address_list": {"type": "list", "source_key": "acctServers"},
                            "aaa_override": {"type": "bool", "source_key": "aaaOverride"},
                            "mac_filtering": {"type": "bool", "source_key": "isMacFilteringEnabled"},
                            "deny_rcm_clients": {"type": "bool", "source_key": "isRandomMacFilterEnabled"},
                            "enable_posture": {"type": "bool", "source_key": "isPosturingEnabled"},
                            "pre_auth_acl_name": {"type": "str", "source_key": "aclName"},
                        }
                    ),
                },
                "mfp_client_protection": {"type": "str", "source_key": "managementFrameProtectionClientprotection"},
                "protected_management_frame": {"type": "str", "source_key": "protectedManagementFrame"},
                "11k_neighbor_list": {"type": "bool", "source_key": "neighborListEnable"},
                "coverage_hole_detection": {"type": "bool", "source_key": "coverageHoleDetectionEnable"},
                "wlan_timeouts": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "enable_session_timeout": {"type": "bool", "source_key": "sessionTimeOutEnable"},
                            "session_timeout": {"type": "int", "source_key": "sessionTimeOut"},
                            "enable_client_execlusion_timeout": {"type": "bool", "source_key": "clientExclusionEnable"},
                            "client_execlusion_timeout": {"type": "int", "source_key": "clientExclusionTimeout"},
                        }
                    ),
                },
                "bss_transition_support": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "bss_max_idle_service": {"type": "bool", "source_key": "basicServiceSetMaxIdleEnable"},
                            "bss_idle_client_timeout": {"type": "int", "source_key": "basicServiceSetClientIdleTimeout"},
                            "directed_multicast_service": {"type": "bool", "source_key": "directedMulticastServiceEnable"},
                        }
                    ),
                },
                "nas_id": {"type": "list", "source_key": "nasOptions"},
                "client_rate_limit": {"type": "int", "source_key": "clientRateLimit"}
            }
        )
        return wireless_ssid_temp_spec

    def wireless_interfaces_temp_spec(self):
        """
        Constructs a temporary specification for wireless interfaces config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as interface name, vlan id.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless interfaces attributes.
        """

        self.log("Generating temporary specification for Wireless Interfaces config", "DEBUG")

        wireless_interfaces_temp_spec = OrderedDict(
            {
                "interface_name": {"type": "str", "source_key": "interfaceName"},
                "vlan_id": {"type": "int", "source_key": "vlanId"},
            }
        )
        return wireless_interfaces_temp_spec

    def wireless_power_profiles_temp_spec(self):
        """
        Constructs a temporary specification for wireless power profiles config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as power profile name, description, and rules.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless power profiles attributes.
        """

        self.log("Generating temporary specification for Wireless Power Profiles config", "DEBUG")
        wireless_power_profiles_temp_spec = OrderedDict(
            {
                "power_profile_name": {"type": "str", "source_key": "profileName"},
                "power_profile_description": {"type": "str", "source_key": "description"},
                "rules": {
                    "type": "list",
                    "elements": "dict",
                    "options": OrderedDict(
                        {
                            "interface_type": {"type": "str", "source_key": "interfaceType"},
                            "interface_id": {"type": "str", "source_key": "interfaceId"},
                            "parameter_type": {"type": "str", "source_key": "parameterType"},
                            "parameter_value": {"type": "str", "source_key": "parameterValue"},
                        }
                    ),
                },
            }
        )
        return wireless_power_profiles_temp_spec

    def wireless_access_point_profiles_temp_spec(self):
        """
        Constructs a temporary specification for wireless access point profiles config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as access point profile name, description etc.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless access point profiles attributes.
        """

        self.log("Generating temporary specification for Wireless Access Point Profiles config", "DEBUG")

        wireless_access_point_profiles_temp_spec = OrderedDict(
            {
                "access_point_profile_name": {"type": "str", "source_key": "apProfileName"},
                "access_point_profile_description": {"type": "str", "source_key": "description"},
                "remote_teleworker": {"type": "bool", "source_key": "remoteWorkerEnabled"},
                "management_settings": {
                    "type": "dict",
                    "special_handling": True,
                    "transform": self.transform_ap_management_settings
                },
                "security_settings": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "awips": {"type": "bool", "source_key": "awipsEnabled"},
                            "awips_forensic": {"type": "bool", "source_key": "awipsForensicEnabled"},
                            "rogue_detection_enabled": {"type": "bool", "source_key": "rogueDetectionSetting.rogueDetection"},
                            "minimum_rssi": {"type": "int", "source_key": "rogueDetectionSetting.rogueDetectionMinRssi"},
                            "transient_interval": {"type": "int", "source_key": "rogueDetectionSetting.rogueDetectionTransientInterval"},
                            "report_interval": {"type": "int", "source_key": "rogueDetectionSetting.rogueDetectionReportInterval"},
                            "pmf_denial": {"type": "bool", "source_key": "pmfDenialEnabled"},
                        }
                    ),
                },
                "mesh_enabled": {"type": "bool", "source_key": "meshEnabled"},
                "mesh_settings": {
                    "type": "dict",
                    "source_key": "meshSetting",
                    "options": OrderedDict(
                        {
                            "range": {"type": "int", "source_key": "range"},
                            "backhaul_client_access": {"type": "bool", "source_key": "backhaulClientAccess"},
                            "rap_downlink_backhaul": {"type": "str", "source_key": "rapDownlinkBackhaul"},
                            "ghz_5_backhaul_data_rates": {"type": "str", "source_key": "ghz5BackhaulDataRates"},
                            "ghz_2_4_backhaul_data_rates": {"type": "str", "source_key": "ghz24BackhaulDataRates"},
                            "bridge_group_name": {"type": "str", "source_key": "bridgeGroupName"}
                        }
                    ),
                },
                "power_settings": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "ap_power_profile_name": {"type": "str", "source_key": "apPowerProfileName"},
                            "calendar_power_profiles": {
                                "type": "list",
                                "elements": "dict",
                                "source_key": "calendarPowerProfiles",
                                "options": OrderedDict(
                                    {
                                        "ap_power_profile_name": {"type": "str", "source_key": "powerProfileName"},
                                        "scheduler_type": {"type": "str", "source_key": "schedulerType"},
                                        "scheduler_start_time": {"type": "str", "source_key": "duration.schedulerStartTime"},
                                        "scheduler_end_time": {"type": "str", "source_key": "duration.schedulerEndTime"},
                                        "scheduler_days_list": {"type": "list", "source_key": "duration.schedulerDay"},
                                        "scheduler_dates_list": {"type": "list", "source_key": "duration.schedulerDate"},
                                    }
                                ),
                            },
                        }
                    ),
                },
                "country_code": {
                    "type": "str",
                    "source_key": "countryCode",
                    "transform": self.transform_ap_country_code
                },
                "time_zone": {"type": "str", "source_key": "timeZone"},
                "time_zone_offset_hour": {"type": "int", "source_key": "timeZoneOffsetHour"},
                "time_zone_offset_minutes": {"type": "int", "source_key": "timeZoneOffsetMinutes"},
                "maximum_client_limit": {"type": "int", "source_key": "clientLimit"}
            }
        )
        return wireless_access_point_profiles_temp_spec

    def ap_management_settings_temp_spec(self, access_point_profile_name):
        """
        Constructs a temporary specification for AP management settings.

        Args:
            access_point_profile_name (str): Access point profile name used for
                generating placeholder variable names for sensitive attributes.

        Returns:
            OrderedDict: An ordered dictionary defining AP management settings attributes.
        """

        self.log(
            "Generating temporary specification for AP management settings for profile: {0}".format(
                access_point_profile_name
            ),
            "DEBUG",
        )

        ap_management_settings_temp_spec = OrderedDict(
            {
                "access_point_authentication": {"type": "str", "source_key": "authType"},
                "dot1x_username": {"type": "str", "source_key": "dot1xUsername"},
                "dot1x_password": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda value: self.generate_place_holder_using_name_value(
                        value.get("dot1xPassword"),
                        "ap_profile",
                        access_point_profile_name,
                        "dot1x_password"
                    )
                },
                "ssh_enabled": {"type": "bool", "source_key": "sshEnabled"},
                "telnet_enabled": {"type": "bool", "source_key": "telnetEnabled"},
                "management_username": {"type": "str", "source_key": "managementUserName"},
                "management_password": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda value: self.generate_place_holder_using_name_value(
                        value.get("managementPassword"),
                        "ap_profile",
                        access_point_profile_name,
                        "management_password",
                    ),
                },
                "management_enable_password": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda value: self.generate_place_holder_using_name_value(
                        value.get("managementEnablePassword"),
                        "ap_profile",
                        access_point_profile_name,
                        "management_enable_password",
                    ),
                },
                "cdp_state": {"type": "bool", "source_key": "cdpState"}
            }
        )

        self.log(
            "Completed temporary specification generation for AP management settings for profile: {0}".format(
                access_point_profile_name
            ),
            "DEBUG",
        )
        return ap_management_settings_temp_spec

    def wireless_radio_frequency_profiles_temp_spec(self):
        """
        Constructs a temporary specification for wireless radio frequency profiles config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as radio frequency profile name, description etc.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless radio frequency profiles attributes.
        """

        self.log("Generating temporary specification for Wireless Radio Frequency Profiles config", "DEBUG")

        radio_frequency_profiles_temp_spec = OrderedDict(
            {
                "radio_frequency_profile_name": {"type": "str", "source_key": "rfProfileName"},
                "default_rf_profile": {"type": "bool", "source_key": "defaultRfProfile"},
                "radio_bands": {
                    "type": "list",
                    "special_handling": True,
                    "transform": self.transform_rf_radio_bands
                },
                "radio_bands_2_4ghz_settings": {
                    "type": "dict",
                    "source_key": "radioTypeBProperties",
                    "options": OrderedDict(
                        {
                            "parent_profile": {"type": "str", "source_key": "parentProfile"},
                            "dca_channels_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("radioChannels"))
                            },
                            "supported_data_rates_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("dataRates"))
                            },
                            "mandatory_data_rates_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("mandatoryDataRates"))
                            },
                            "minimum_power_level": {"type": "int", "source_key": "minPowerLevel"},
                            "maximum_power_level": {"type": "int", "source_key": "maxPowerLevel"},
                            "rx_sop_threshold": {"type": "str", "source_key": "rxSopThreshold"},
                            "custom_rx_sop_threshold": {"type": "int", "source_key": "customRxSopThreshold"},
                            "tpc_power_threshold": {"type": "int", "source_key": "powerThresholdV1"},
                            "coverage_hole_detection": {
                                "type": "dict",
                                "source_key": "coverageHoleDetectionProperties",
                                "options": OrderedDict(
                                    {
                                        "minimum_client_level": {"type": "int", "source_key": "chdClientLevel"},
                                        "data_rssi_threshold": {"type": "int", "source_key": "chdDataRssiThreshold"},
                                        "voice_rssi_threshold": {"type": "int", "source_key": "chdVoiceRssiThreshold"},
                                        "exception_level": {"type": "int", "source_key": "chdExceptionLevel"},
                                    }
                                ),
                            },
                            "client_limit": {"type": "int", "source_key": "maxRadioClients"},
                            "spatial_reuse": {
                                "type": "dict",
                                "source_key": "spatialReuseProperties",
                                "options": OrderedDict(
                                    {
                                        "non_srg_obss_pd": {"type": "bool", "source_key": "dot11axNonSrgObssPacketDetect"},
                                        "non_srg_obss_pd_max_threshold": {"type": "int", "source_key": "dot11axNonSrgObssPacketDetectMaxThreshold"},
                                        "srg_obss_pd": {"type": "bool", "source_key": "dot11axSrgObssPacketDetect"},
                                        "srg_obss_pd_min_threshold": {"type": "int", "source_key": "dot11axSrgObssPacketDetectMinThreshold"},
                                        "srg_obss_pd_max_threshold": {"type": "int", "source_key": "dot11axSrgObssPacketDetectMaxThreshold"},
                                    }
                                ),
                            },
                        }
                    ),
                },
                "radio_bands_5ghz_settings": {
                    "type": "dict",
                    "source_key": "radioTypeAProperties",
                    "options": OrderedDict(
                        {
                            "parent_profile": {"type": "str", "source_key": "parentProfile"},
                            "channel_width": {"type": "str", "source_key": "channelWidth"},
                            "preamble_puncturing": {"type": "bool", "source_key": "preamblePuncture"},
                            "zero_wait_dfs": {"type": "bool", "source_key": "zeroWaitDfsEnable"},
                            "dca_channels_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("radioChannels"))
                            },
                            "supported_data_rates_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("dataRates"))
                            },
                            "mandatory_data_rates_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("mandatoryDataRates"))
                            },
                            "minimum_power_level": {"type": "int", "source_key": "minPowerLevel"},
                            "maximum_power_level": {"type": "int", "source_key": "maxPowerLevel"},
                            "rx_sop_threshold": {"type": "str", "source_key": "rxSopThreshold"},
                            "custom_rx_sop_threshold": {"type": "int", "source_key": "customRxSopThreshold"},
                            "tpc_power_threshold": {"type": "int", "source_key": "powerThresholdV1"},
                            "coverage_hole_detection": {
                                "type": "dict",
                                "source_key": "coverageHoleDetectionProperties",
                                "options": OrderedDict(
                                    {
                                        "minimum_client_level": {"type": "int", "source_key": "chdClientLevel"},
                                        "data_rssi_threshold": {"type": "int", "source_key": "chdDataRssiThreshold"},
                                        "voice_rssi_threshold": {"type": "int", "source_key": "chdVoiceRssiThreshold"},
                                        "exception_level": {"type": "int", "source_key": "chdExceptionLevel"},
                                    }
                                ),
                            },
                            "client_limit": {"type": "int", "source_key": "maxRadioClients"},
                            "flexible_radio_assigment": {
                                "type": "dict",
                                "source_key": "fraPropertiesA",
                                "options": OrderedDict(
                                    {
                                        "client_aware": {"type": "bool", "source_key": "clientAware"},
                                        "client_select": {"type": "int", "source_key": "clientSelect"},
                                        "client_reset": {"type": "int", "source_key": "clientReset"},
                                    }
                                ),
                            },
                            "spatial_reuse": {
                                "type": "dict",
                                "source_key": "spatialReuseProperties",
                                "options": OrderedDict(
                                    {
                                        "non_srg_obss_pd": {"type": "bool", "source_key": "dot11axNonSrgObssPacketDetect"},
                                        "non_srg_obss_pd_max_threshold": {"type": "int", "source_key": "dot11axNonSrgObssPacketDetectMaxThreshold"},
                                        "srg_obss_pd": {"type": "bool", "source_key": "dot11axSrgObssPacketDetect"},
                                        "srg_obss_pd_min_threshold": {"type": "int", "source_key": "dot11axSrgObssPacketDetectMinThreshold"},
                                        "srg_obss_pd_max_threshold": {"type": "int", "source_key": "dot11axSrgObssPacketDetectMaxThreshold"},
                                    }
                                ),
                            },
                        }
                    ),
                },
                "radio_bands_6ghz_settings": {
                    "type": "dict",
                    "source_key": "radioType6GHzProperties",
                    "options": OrderedDict(
                        {
                            "parent_profile": {"type": "str", "source_key": "parentProfile"},
                            "minimum_dbs_channel_width": {"type": "int", "source_key": "minDbsWidth"},
                            "maximum_dbs_channel_width": {"type": "int", "source_key": "maxDbsWidth"},
                            "preamble_puncturing": {"type": "bool", "source_key": "preamblePuncture"},
                            "psc_enforcing_enabled": {"type": "bool", "source_key": "pscEnforcingEnabled"},
                            "dca_channels_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("radioChannels"))
                            },
                            "supported_data_rates_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("dataRates"))
                            },
                            "mandatory_data_rates_list": {
                                "type": "list",
                                "special_handling": True,
                                "transform": lambda properties:
                                    self.str_numbers_to_numeric_list(properties.get("mandatoryDataRates"))
                            },
                            "standard_power_service": {"type": "bool", "source_key": "enableStandardPowerService"},
                            "minimum_power_level": {"type": "int", "source_key": "minPowerLevel"},
                            "maximum_power_level": {"type": "int", "source_key": "maxPowerLevel"},
                            "rx_sop_threshold": {"type": "str", "source_key": "rxSopThreshold"},
                            "custom_rx_sop_threshold": {"type": "int", "source_key": "customRxSopThreshold"},
                            "tpc_power_threshold": {"type": "int", "source_key": "powerThresholdV1"},
                            "coverage_hole_detection": {
                                "type": "dict",
                                "source_key": "coverageHoleDetectionProperties",
                                "options": OrderedDict(
                                    {
                                        "minimum_client_level": {"type": "int", "source_key": "chdClientLevel"},
                                        "data_rssi_threshold": {"type": "int", "source_key": "chdDataRssiThreshold"},
                                        "voice_rssi_threshold": {"type": "int", "source_key": "chdVoiceRssiThreshold"},
                                        "exception_level": {"type": "int", "source_key": "chdExceptionLevel"},
                                    }
                                ),
                            },
                            "client_limit": {"type": "int", "source_key": "maxRadioClients"},
                            "flexible_radio_assigment": {
                                "type": "dict",
                                "source_key": "fraPropertiesC",
                                "options": OrderedDict(
                                    {
                                        "client_reset_count": {"type": "int", "source_key": "clientResetCount"},
                                        "client_utilization_threshold": {"type": "int", "source_key": "clientUtilizationThreshold"},
                                    }
                                ),
                            },
                            "discovery_frames_6ghz": {"type": "str", "source_key": "discoveryFrames6GHz"},
                            "broadcast_probe_response_interval": {"type": "int", "source_key": "broadcastProbeResponseInterval"},
                            "multi_bssid": {
                                "type": "dict",
                                "source_key": "multiBssidProperties",
                                "options": OrderedDict(
                                    {
                                        "dot_11ax_parameters": {
                                            "type": "dict",
                                            "source_key": "dot11axParameters",
                                            "options": OrderedDict(
                                                {
                                                    "ofdma_downlink": {"type": "bool", "source_key": "ofdmaDownLink"},
                                                    "ofdma_uplink": {"type": "bool", "source_key": "ofdmaUpLink"},
                                                    "mu_mimo_downlink": {"type": "bool", "source_key": "muMimoDownLink"},
                                                    "mu_mimo_uplink": {"type": "bool", "source_key": "muMimoUpLink"},
                                                }
                                            ),
                                        },
                                        "dot_11be_parameters": {
                                            "type": "dict",
                                            "source_key": "dot11beParameters",
                                            "options": OrderedDict(
                                                {
                                                    "ofdma_downlink": {"type": "bool", "source_key": "ofdmaDownLink"},
                                                    "ofdma_uplink": {"type": "bool", "source_key": "ofdmaUpLink"},
                                                    "mu_mimo_downlink": {"type": "bool", "source_key": "muMimoDownLink"},
                                                    "mu_mimo_uplink": {"type": "bool", "source_key": "muMimoUpLink"},
                                                    "ofdma_multi_ru": {"type": "bool", "source_key": "ofdmaMultiRu"},
                                                }
                                            ),
                                        },
                                        "target_waketime": {"type": "bool", "source_key": "targetWakeTime"},
                                        "twt_broadcast_support": {"type": "bool", "source_key": "twtBroadcastSupport"},
                                    }
                                ),
                            },
                            "spatial_reuse": {
                                "type": "dict",
                                "source_key": "spatialReuseProperties",
                                "options": OrderedDict(
                                    {
                                        "non_srg_obss_pd": {"type": "bool", "source_key": "dot11axNonSrgObssPacketDetect"},
                                        "non_srg_obss_pd_max_threshold": {"type": "int", "source_key": "dot11axNonSrgObssPacketDetectMaxThreshold"},
                                        "srg_obss_pd": {"type": "bool", "source_key": "dot11axSrgObssPacketDetect"},
                                        "srg_obss_pd_min_threshold": {"type": "int", "source_key": "dot11axSrgObssPacketDetectMinThreshold"},
                                        "srg_obss_pd_max_threshold": {"type": "int", "source_key": "dot11axSrgObssPacketDetectMaxThreshold"},
                                    }
                                ),
                            },
                        }
                    ),
                },
            }
        )
        return radio_frequency_profiles_temp_spec

    def wireless_anchor_groups_temp_spec(self):
        """
        Constructs a temporary specification for wireless anchor groups config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as anchor group name.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless anchor groups attributes.
        """

        self.log("Generating temporary specification for Wireless Anchor Groups config", "DEBUG")

        anchor_groups_temp_spec = OrderedDict(
            {
                "anchor_group_name": {"type": "str", "source_key": "anchorGroupName"},
                "mobility_anchors": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "mobilityAnchors",
                    "options": OrderedDict(
                        {
                            "device_name": {"type": "str", "source_key": "deviceName"},
                            "device_ip_address": {"type": "str", "source_key": "ipAddress"},
                            "device_mac_address": {"type": "str", "source_key": "macAddress"},
                            "device_type": {"type": "str", "source_key": "peerDeviceType"},
                            "device_priority": {
                                "type": "str",
                                "source_key": "anchorPriority",
                                "transform": lambda priority:
                                    {"PRIMARY": 1, "SECONDARY": 2, "TERTIARY": 3}.get(priority, None),
                            },
                            "device_nat_ip_address": {"type": "str", "source_key": "privateIp"},
                            "mobility_group_name": {"type": "str", "source_key": "mobilityGroupName"},
                            "managed_device": {"type": "bool", "source_key": "managedAnchorWlc"},
                        }
                    ),
                }
            }
        )

        return anchor_groups_temp_spec

    def wireless_aaa_radius_attribute_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless aaa radius config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as design name.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless aaa radius attributes config.
        """

        self.log("Generating temporary specification for Wireless AAA Radius Attributes config", "DEBUG")

        aaa_radius_attribute_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "called_station_id": {
                    "type": "str",
                    "source_key": "featureAttributes",
                    "transform": lambda x: x.get("calledStationId")
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes"
                }
            }
        )
        return aaa_radius_attribute_config_temp_spec

    def wireless_advanced_ssid_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless advanced ssid config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as design name.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless advanced ssid config.
        """

        self.log("Generating temporary specification for Wireless Advanced SSID config", "DEBUG")

        advanced_ssid_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "peer2peer_blocking": {"type": "str", "source_key": "peer2peerblocking"},
                            "passive_client": {"type": "bool", "source_key": "passiveClient"},
                            "prediction_optimization": {"type": "bool", "source_key": "predictionOptimization"},
                            "dual_band_neighbor_list": {"type": "bool", "source_key": "dualBandNeighborList"},
                            "radius_nac_state": {"type": "bool", "source_key": "radiusNacState"},
                            "dhcp_required": {"type": "bool", "source_key": "dhcpRequired"},
                            "dhcp_server": {"type": "str", "source_key": "dhcpServer"},
                            "flex_local_auth": {"type": "bool", "source_key": "flexLocalAuth"},
                            "target_wakeup_time": {"type": "bool", "source_key": "targetWakeupTime"},
                            "downlink_ofdma": {"type": "bool", "source_key": "downlinkOfdma"},
                            "uplink_ofdma": {"type": "bool", "source_key": "uplinkOfdma"},
                            "downlink_mu_mimo": {"type": "bool", "source_key": "downlinkMuMimo"},
                            "uplink_mu_mimo": {"type": "bool", "source_key": "uplinkMuMimo"},
                            "dot11ax": {"type": "bool", "source_key": "dot11ax"},
                            "aironet_ie_support": {"type": "bool", "source_key": "aironetIESupport"},
                            "load_balancing": {"type": "bool", "source_key": "loadBalancing"},
                            "dtim_period_5ghz": {"type": "int", "source_key": "dtimPeriod5GHz"},
                            "dtim_period_24ghz": {"type": "int", "source_key": "dtimPeriod24GHz"},
                            "scan_defer_time": {"type": "int", "source_key": "scanDeferTime"},
                            "max_clients": {"type": "int", "source_key": "maxClients"},
                            "max_clients_per_radio": {"type": "int", "source_key": "maxClientsPerRadio"},
                            "max_clients_per_ap": {"type": "int", "source_key": "maxClientsPerAp"},
                            "wmm_policy": {"type": "str", "source_key": "wmmPolicy"},
                            "multicast_buffer": {"type": "bool", "source_key": "multicastBuffer"},
                            "multicast_buffer_value": {"type": "int", "source_key": "multicastBufferValue"},
                            "media_stream_multicast_direct": {"type": "bool", "source_key": "mediaStreamMulticastDirect"},
                            "mu_mimo_11ac": {"type": "bool", "source_key": "muMimo11ac"},
                            "wifi_to_cellular_steering": {"type": "bool", "source_key": "wifiToCellularSteering"},
                            "wifi_alliance_agile_multiband": {"type": "bool", "source_key": "wifiAllianceAgileMultiband"},
                            "fastlane_asr": {"type": "bool", "source_key": "fastlaneASR"},
                            "dot11v_bss_max_idle_protected": {"type": "bool", "source_key": "dot11vBSSMaxIdleProtected"},
                            "universal_ap_admin": {"type": "bool", "source_key": "universalAPAdmin"},
                            "opportunistic_key_caching": {"type": "bool", "source_key": "opportunisticKeyCaching"},
                            "ip_source_guard": {"type": "bool", "source_key": "ipSourceGuard"},
                            "dhcp_opt82_remote_id_sub_option": {"type": "bool", "source_key": "dhcpOpt82RemoteIDSubOption"},
                            "vlan_central_switching": {"type": "bool", "source_key": "vlanCentralSwitching"},
                            "call_snooping": {"type": "bool", "source_key": "callSnooping"},
                            "send_disassociate": {"type": "bool", "source_key": "sendDisassociate"},
                            "sent_486_busy": {"type": "bool", "source_key": "sent486Busy"},
                            "ip_mac_binding": {"type": "bool", "source_key": "ipMacBinding"},
                            "idle_threshold": {"type": "int", "source_key": "idleThreshold"},
                            "defer_priority_0": {"type": "bool", "source_key": "deferPriority0"},
                            "defer_priority_1": {"type": "bool", "source_key": "deferPriority1"},
                            "defer_priority_2": {"type": "bool", "source_key": "deferPriority2"},
                            "defer_priority_3": {"type": "bool", "source_key": "deferPriority3"},
                            "defer_priority_4": {"type": "bool", "source_key": "deferPriority4"},
                            "defer_priority_5": {"type": "bool", "source_key": "deferPriority5"},
                            "defer_priority_6": {"type": "bool", "source_key": "deferPriority6"},
                            "defer_priority_7": {"type": "bool", "source_key": "deferPriority7"},
                            "share_data_with_client": {"type": "bool", "source_key": "shareDataWithClient"},
                            "advertise_support": {"type": "bool", "source_key": "advertiseSupport"},
                            "advertise_pc_analytics_support": {"type": "bool", "source_key": "advertisePCAnalyticsSupport"},
                            "send_beacon_on_association": {"type": "bool", "source_key": "sendBeaconOnAssociation"},
                            "send_beacon_on_roam": {"type": "bool", "source_key": "sendBeaconOnRoam"},
                            "fast_transition_reassociation_timeout": {"type": "int", "source_key": "fastTransitionReassociationTimeout"},
                            "mdns_mode": {"type": "str", "source_key": "mDNSMode"},
                        }
                    )
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes"
                }
            }
        )
        return advanced_ssid_config_temp_spec

    def wireless_clean_air_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless clean air configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining clean air configuration attributes.
        """

        self.log("Generating temporary specification for Wireless Clean Air configuration", "DEBUG")

        clean_air_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "radio_band": {"type": "str", "source_key": "radioBand"},
                            "clean_air": {"type": "bool", "source_key": "cleanAir"},
                            "clean_air_device_reporting": {"type": "bool", "source_key": "cleanAirDeviceReporting"},
                            "persistent_device_propagation": {"type": "bool", "source_key": "persistentDevicePropagation"},
                            "description": {"type": "str", "source_key": "description"},
                            "interferers_features": {
                                "type": "dict",
                                "source_key": "interferersFeatures",
                                "options": OrderedDict(
                                    {
                                        "ble_beacon": {"type": "bool", "source_key": "bleBeacon"},
                                        "bluetooth_paging_inquiry": {"type": "bool", "source_key": "bluetoothPagingInquiry"},
                                        "bluetooth_sco_acl": {"type": "bool", "source_key": "bluetoothScoAcl"},
                                        "continuous_transmitter": {"type": "bool", "source_key": "continuousTransmitter"},
                                        "generic_dect": {"type": "bool", "source_key": "genericDect"},
                                        "generic_tdd": {"type": "bool", "source_key": "genericTdd"},
                                        "jammer": {"type": "bool", "source_key": "jammer"},
                                        "microwave_oven": {"type": "bool", "source_key": "microwaveOven"},
                                        "motorola_canopy": {"type": "bool", "source_key": "motorolaCanopy"},
                                        "si_fhss": {"type": "bool", "source_key": "siFhss"},
                                        "spectrum80211_fh": {"type": "bool", "source_key": "spectrum80211Fh"},
                                        "spectrum80211_non_standard_channel": {
                                            "type": "bool",
                                            "source_key": "spectrum80211NonStandardChannel",
                                        },
                                        "spectrum802154": {"type": "bool", "source_key": "spectrum802154"},
                                        "spectrum_inverted": {"type": "bool", "source_key": "spectrumInverted"},
                                        "super_ag": {"type": "bool", "source_key": "superAg"},
                                        "video_camera": {"type": "bool", "source_key": "videoCamera"},
                                        "wimax_fixed": {"type": "bool", "source_key": "wimaxFixed"},
                                        "wimax_mobile": {"type": "bool", "source_key": "wimaxMobile"},
                                        "xbox": {"type": "bool", "source_key": "xbox"},
                                    }
                                ),
                            },
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return clean_air_config_temp_spec

    def wireless_dot11ax_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless 802.11ax configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining 802.11ax configuration attributes.
        """

        self.log("Generating temporary specification for Wireless 802.11ax configuration", "DEBUG")

        dot11ax_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "radio_band": {"type": "str", "source_key": "radioBand"},
                            "bss_color": {"type": "bool", "source_key": "bssColor"},
                            "target_waketime_broadcast": {"type": "bool", "source_key": "targetWaketimeBroadcast"},
                            "non_srg_obss_pd_max_threshold": {"type": "int", "source_key": "nonSRGObssPdMaxThreshold"},
                            "target_wakeup_time_11ax": {"type": "bool", "source_key": "targetWakeUpTime11ax"},
                            "obss_pd": {"type": "bool", "source_key": "obssPd"},
                            "multiple_bssid": {"type": "bool", "source_key": "multipleBssid"},
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return dot11ax_config_temp_spec

    def wireless_dot11be_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless 802.11be configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining 802.11be configuration attributes.
        """

        self.log("Generating temporary specification for Wireless 802.11be configuration", "DEBUG")

        dot11be_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "dot11be_status": {"type": "bool", "source_key": "dot11beStatus"},
                            "radio_band": {"type": "str", "source_key": "radioBand"},
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return dot11be_config_temp_spec

    def wireless_event_driven_rrm_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless event-driven RRM configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining event-driven RRM configuration attributes.
        """

        self.log("Generating temporary specification for Wireless Event-Driven RRM configuration", "DEBUG")

        event_driven_rrm_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "radio_band": {"type": "str", "source_key": "radioBand"},
                            "event_driven_rrm_enable": {"type": "bool", "source_key": "eventDrivenRrmEnable"},
                            "event_driven_rrm_threshold_level": {
                                "type": "str",
                                "source_key": "eventDrivenRrmThresholdLevel",
                            },
                            "event_driven_rrm_custom_threshold_val": {
                                "type": "int",
                                "source_key": "eventDrivenRrmCustomThresholdVal",
                            },
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return event_driven_rrm_config_temp_spec

    def wireless_feature_template_flexconnect_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless feature template flexconnect configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining feature template flexconnect configuration attributes.
        """

        self.log("Generating temporary specification for Wireless FlexConnect configuration", "DEBUG")

        flexconnect_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "overlap_ip_enable": {"type": "bool", "source_key": "overlapIpEnable"},
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return flexconnect_config_temp_spec

    def wireless_multicast_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless multicast configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining multicast configuration attributes.
        """

        self.log("Generating temporary specification for Wireless Multicast configuration", "DEBUG")

        multicast_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "global_multicast_enabled": {"type": "bool", "source_key": "globalMulticastEnabled"},
                            "multicast_ipv4_mode": {"type": "str", "source_key": "multicastIpv4Mode"},
                            "multicast_ipv4_address": {"type": "str", "source_key": "multicastIpv4Address"},
                            "multicast_ipv6_mode": {"type": "str", "source_key": "multicastIpv6Mode"},
                            "multicast_ipv6_address": {"type": "str", "source_key": "multicastIpv6Address"},
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return multicast_config_temp_spec

    def wireless_rrm_fra_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless RRM FRA configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining RRM FRA configuration attributes.
        """

        self.log("Generating temporary specification for Wireless RRM FRA configuration", "DEBUG")

        rrm_fra_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "radio_band": {"type": "str", "source_key": "radioBand"},
                            "fra_freeze": {"type": "bool", "source_key": "fraFreeze"},
                            "fra_status": {"type": "bool", "source_key": "fraStatus"},
                            "fra_interval": {"type": "int", "source_key": "fraInterval"},
                            "fra_sensitivity": {
                                "type": "str",
                                "source_key": "fraSensitivity",
                                "transform": lambda x: x.upper() if x is not None else x
                            },
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return rrm_fra_config_temp_spec

    def wireless_rrm_rrm_general_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless RRM general configuration,
        defining the structure and types of attributes used in the YAML file.

        Returns:
            OrderedDict: An ordered dictionary defining RRM general configuration attributes.
        """

        self.log("Generating temporary specification for Wireless RRM General configuration", "DEBUG")

        rrm_general_config_temp_spec = OrderedDict(
            {
                "design_name": {"type": "str", "source_key": "designName"},
                "feature_attributes": {
                    "type": "dict",
                    "source_key": "featureAttributes",
                    "options": OrderedDict(
                        {
                            "radio_band": {"type": "str", "source_key": "radioBand"},
                            "monitoring_channels": {"type": "str", "source_key": "monitoringChannels"},
                            "neighbor_discover_type": {"type": "str", "source_key": "neighborDiscoverType"},
                            "throughput_threshold": {"type": "int", "source_key": "throughputThreshold"},
                            "coverage_hole_detection": {"type": "bool", "source_key": "coverageHoleDetection"},
                        }
                    ),
                },
                "unlocked_attributes": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "unlockedAttributes",
                },
            }
        )
        return rrm_general_config_temp_spec

    def wireless_802_11_be_profiles_temp_spec(self):
        """
        Constructs a temporary specification for wireless 802.11be profiles, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as profile_name.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless 802.11be profile attributes.
        """

        self.log("Generating temporary specification for Wireless 802.11be profiles config", "DEBUG")

        wireless_802_11be_profiles_temp_spec = OrderedDict(
            {
                "profile_name": {"type": "str", "source_key": "profileName"},
                "ofdma_up_link": {"type": "bool", "source_key": "ofdmaUpLink"},
                "ofdma_down_link": {"type": "bool", "source_key": "ofdmaDownLink"},
                "mu_mimo_up_link": {"type": "bool", "source_key": "muMimoUpLink"},
                "mu_mimo_down_link": {"type": "bool", "source_key": "muMimoDownLink"},
                "ofdma_multi_ru": {"type": "bool", "source_key": "ofdmaMultiRu"},
            }
        )
        return wireless_802_11be_profiles_temp_spec

    def wireless_flex_connect_config_temp_spec(self):
        """
        Constructs a temporary specification for wireless flex connect config, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as site name hierarchy, vlan id.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless flex connect configuration attributes.
        """

        self.log("Generating temporary specification for Wireless Flex Connect config", "DEBUG")

        wireless_flex_connect_config_temp_spec = OrderedDict(
            {
                "site_name_hierarchy": {"type": "str", "source_key": "siteNameHierarchy"},
                "vlan_id": {"type": "int", "source_key": "nativeVlanId"}
            }
        )
        return wireless_flex_connect_config_temp_spec

    def generate_placeholder_using_component_details(self, component_details, component, component_name_parameter, parameter):
        """
        Generates a custom variable name for a given component, component name, and parameter.
        Args:
            component (str): The type of network component (e.g., "ssid", "mpsk").
            component_details (dict): The details of the component.
            component_name_parameter (str): The name of the component parameter (e.g., ssidName).
            parameter (str): The parameter for which the variable is being generated (e.g., "passphrase").
        Returns:
            str: The generated custom variable name.
        """
        # Generate the custom variable name
        self.log(
            f"Generating custom variable name for component: {component}, component details: {component_details}, "
            f"parameter: {parameter}, component name parameter: {component_name_parameter}", "DEBUG",
        )

        # Replacing consecutive non-alphanumeric characters with a single underscore
        value = re.sub(r'[^A-Za-z0-9]+', '_', component_details[component_name_parameter])
        self.log("Transformed component name parameter: {0}".format(value), "DEBUG")

        variable_name = f"{{ {component}_{value}_{parameter} }}"

        custom_variable_name = "{" + variable_name + "}"
        self.log(f"Generated custom variable name: {custom_variable_name}", "DEBUG")

        return custom_variable_name

    def generate_place_holder_using_name_value(self, value, component, name, parameter):
        """
        Generates a custom variable name for a given component, name, and parameter.
        Args:
            value (str): The value of the component parameter (e.g., passphrase value).
            component (str): The type of network component (e.g., "ssid", "mpsk").
            name (str): The name to be included in the variable.
            parameter (str): The parameter for which the variable is being generated (e.g., "passphrase").
        Returns:
            str: The generated custom variable name.
        """
        # Generate the custom variable name
        self.log(
            f"Generating custom variable name for value: {value}, component: {component}, name: {name}, parameter: {parameter}", "DEBUG",
        )

        if not value:
            self.log("No value provided for generating variable name, returning None", "DEBUG")
            return None

        # Replacing consecutive non-alphanumeric characters with a single underscore
        value = re.sub(r'[^A-Za-z0-9]+', '_', name)
        self.log("Transformed name: {0}".format(value), "DEBUG")

        variable_name = f"{{ {component}_{value}_{parameter} }}"

        custom_variable_name = "{" + variable_name + "}"
        self.log(f"Generated custom variable name: {custom_variable_name}", "DEBUG")

        return custom_variable_name

    def transform_radio_bands(self, radio_type):
        """
        Transforms SSID radio type string into corresponding radio bands list.

        Args:
            radio_type (str): SSID radio type string from Catalyst Center API response.

        Returns:
            list: A list of radio bands represented as float/int values.
                Returns:
                - [2.4, 5, 6] for triple band operation
                - [5], [2.4], or [6] for single-band operation
                - [2.4, 5], [2.4, 6], or [5, 6] for dual-band operation
                - [] when input is empty or unmatched
        """

        self.log(
            "Starting radio bands transformation for given radio type: {0}"
            .format(radio_type if radio_type is not None else "Unknown"),
            "DEBUG"
        )

        if not radio_type:
            self.log("No radio type provided for transformation", "DEBUG")
            return []

        transformed_radio_bands = {
            "Triple band operation(2.4GHz, 5GHz and 6GHz)": [2.4, 5, 6],
            "5GHz only": [5],
            "2.4GHz only": [2.4],
            "6GHz only": [6],
            "2.4 and 5 GHz": [2.4, 5],
            "2.4 and 6 GHz": [2.4, 6],
            "5 and 6 GHz": [5, 6],
        }.get(radio_type, [])

        if not transformed_radio_bands:
            self.log(
                "No radio bands mapping found for radio type: {0}. Returning empty list."
                .format(radio_type),
                "DEBUG"
            )
            return transformed_radio_bands

        self.log(
            "Completed radio bands transformation. Input radio type: {0}, transformed radio bands: {1}"
            .format(radio_type, transformed_radio_bands),
            "DEBUG"
        )

        return transformed_radio_bands

    def transform_2_dot_4_ghz_band_policy(self, band_value):
        """
        Transforms 2.4 GHz band policy value into workflow-supported format.

        Args:
            band_value (str): 2.4 GHz policy value from Catalyst Center API response.

        Returns:
            str: Transformed 2.4 GHz band policy value.
                Returns:
                - "802.11-bg" when value is "dot11-bg-only"
                - "802.11-g" when value is "dot11-g-only"
                - None for any other value
        """

        self.log(
            "Starting 2.4 GHz band policy transformation for value: {0}"
            .format(band_value if band_value is not None else "Unknown"),
            "DEBUG"
        )

        transformed_value = {
            "dot11-bg-only": "802.11-bg",
            "dot11-g-only": "802.11-g",
        }.get(band_value, None)

        self.log(
            "Completed 2.4 GHz band policy transformation. Input value: {0}, transformed value: {1}"
            .format(band_value, transformed_value),
            "DEBUG"
        )

        return transformed_value

    def transform_ssid_wpa_encryption(self, ssid_details):
        """
        Transforms SSID WPA encryption flags into workflow-supported encryption list.

        Args:
            ssid_details (dict): SSID details containing RSN cipher suite boolean flags.

        Returns:
            list: List of WPA encryption values based on enabled boolean flags.
        """

        self.log(
            "Starting SSID WPA encryption transformation for ssid details: {0}"
            .format(ssid_details),
            "DEBUG"
        )

        mapping = {
            "GCMP256": "rsnCipherSuiteGcmp256",
            "CCMP256": "rsnCipherSuiteCcmp256",
            "GCMP128": "rsnCipherSuiteGcmp128",
            "CCMP128": "rsnCipherSuiteCcmp128",
        }

        result = []
        for list_value, boolean_key in mapping.items():
            boolean_value = ssid_details.get(boolean_key, False)
            self.log(
                "Checking key '{0}': {1}".format(boolean_key, boolean_value), "DEBUG"
            )
            if boolean_value:
                result.append(list_value)

        self.log(
            "Completed SSID WPA encryption transformation. Transformed value: {0}"
            .format(result),
            "DEBUG"
        )

        return result

    def transform_auth_key_management(self, ssid_details):
        """
        Transforms SSID authentication key management flags into workflow-supported list.

        Args:
            ssid_details (dict): SSID details containing authentication key management boolean flags.

        Returns:
            list: List of authentication key management values based on enabled boolean flags.
        """

        self.log(
            "Starting authentication key management transformation for ssid details: {0}"
            .format(ssid_details),
            "DEBUG"
        )

        mapping = {
            "SAE": "isAuthKeySae",
            "SAE-EXT-KEY": "isAuthKeySaeExt",
            "FT+SAE": "isAuthKeySaePlusFT",
            "FT+SAE-EXT-KEY": "isAuthKeySaeExtPlusFT",
            "OWE": "isAuthKeyOWE",
            "PSK": "isAuthKeyPSK",
            "FT+PSK": "isAuthKeyPSKPlusFT",
            "Easy-PSK": "isAuthKeyEasyPSK",
            "PSK-SHA2": "isAuthKeyPSKSHA256",
            "802.1X-SHA1": "isAuthKey8021x",
            "802.1X-SHA2": "isAuthKey8021x_SHA256",
            "FT+802.1x": "isAuthKey8021xPlusFT",
            "SUITE-B-1X": "isAuthKeySuiteB1x",
            "SUITE-B-192X": "isAuthKeySuiteB1921x",
            "CCKM": "isCckmEnabled",
        }

        result = []
        for list_value, boolean_key in mapping.items():
            boolean_value = ssid_details.get(boolean_key, False)
            self.log(
                "Checking key '{0}': {1}".format(boolean_key, boolean_value), "DEBUG"
            )
            if boolean_value:
                result.append(list_value)

        self.log(
            "Completed authentication key management transformation. Transformed value: {0}"
            .format(result), "DEBUG"
        )
        return result

    def transform_l3_security_auth_server(self, ssid_details):
        """
        Transforms L3 security auth server value to workflow-supported format.

        Args:
            auth_server (str): Auth server value from Catalyst Center API response.

        Returns:
            str: Transformed auth server value.
        """

        self.log(
            "Starting L3 security auth server transformation for value: {0}"
            .format(ssid_details.get("authServer", "Unknown")),
            "DEBUG"
        )

        auth_server = ssid_details.get("authServer")
        if not auth_server:
            self.log("No auth server provided for transformation", "DEBUG")
            return None

        web_passthrough_enabled = ssid_details.get("webPassthrough", False)
        self.log("Web passthrough enabled: {0}".format(web_passthrough_enabled), "DEBUG")

        transformed_value = {
            "auth_ise": "central_web_authentication",
            "auth_internal": "web_passthrough_internal" if web_passthrough_enabled else "web_authentication_internal",
            "auth_external": "web_passthrough_external" if web_passthrough_enabled else "web_authentication_external",
        }.get(auth_server, auth_server)

        self.log(
            "Completed L3 security auth server transformation. Input value: {0}, transformed value: {1}"
            .format(auth_server, transformed_value),
            "DEBUG"
        )

        return transformed_value

    def transform_ap_country_code(self, country_code):
        """
        Transforms access point country code value to workflow-supported format.

        Args:
            country_code (str): Country code value from Catalyst Center API response.

        Returns:
            str: Transformed country code value.
        """

        self.log(
            "Starting access point country code transformation for value: {0}"
            .format(country_code if country_code is not None else "Unknown"),
            "DEBUG"
        )

        if self.country_code_map is None:
            self.log(
                "Country code mapping is not initialized. Building country code map for access point country code transformation.",
                "DEBUG"
            )
            self.country_code_map = {
                "AF": "Afghanistan",
                "AL": "Albania",
                "DZ": "Algeria",
                "AO": "Angola",
                "AR": "Argentina",
                "AU": "Australia",
                "AT": "Austria",
                "BS": "Bahamas",
                "BH": "Bahrain",
                "BD": "Bangladesh",
                "BB": "Barbados",
                "BY": "Belarus",
                "BE": "Belgium",
                "BT": "Bhutan",
                "BO": "Bolivia",
                "BA": "Bosnia",
                "BW": "Botswana",
                "BR": "Brazil",
                "BN": "Brunei",
                "BG": "Bulgaria",
                "BI": "Burundi",
                "KH": "Cambodia",
                "CM": "Cameroon",
                "CA": "Canada",
                "CL": "Chile",
                "CN": "China",
                "CO": "Colombia",
                "CR": "Costa Rica",
                "HR": "Croatia",
                "CU": "Cuba",
                "CY": "Cyprus",
                "CZ": "Czech Republic",
                "CD": "Democratic Republic of the Congo",
                "DK": "Denmark",
                "DO": "Dominican Republic",
                "EC": "Ecuador",
                "EG": "Egypt",
                "SV": "El Salvador",
                "EE": "Estonia",
                "ET": "Ethiopia",
                "FJ": "Fiji",
                "FI": "Finland",
                "FR": "France",
                "GA": "Gabon",
                "GE": "Georgia",
                "DE": "Germany",
                "GH": "Ghana",
                "GI": "Gibraltar",
                "GR": "Greece",
                "GT": "Guatemala",
                "HN": "Honduras",
                "HK": "Hong Kong",
                "HU": "Hungary",
                "IS": "Iceland",
                "IN": "India",
                "ID": "Indonesia",
                "IQ": "Iraq",
                "IE": "Ireland",
                "IM": "Isle of Man",
                "IL": "Israel",
                "IT": "Italy",
                "CI": "Ivory Coast (Cote dIvoire)",
                "JM": "Jamaica",
                "J2": "Japan 2(P)",
                "J4": "Japan 4(Q)",
                "JE": "Jersey",
                "JO": "Jordan",
                "KZ": "Kazakhstan",
                "KE": "Kenya",
                "KR": "Korea Extended (CK)",
                "XK": "Kosovo",
                "KW": "Kuwait",
                "LA": "Laos",
                "LV": "Latvia",
                "LB": "Lebanon",
                "LY": "Libya",
                "LI": "Liechtenstein",
                "LT": "Lithuania",
                "LU": "Luxembourg",
                "MO": "Macao",
                "MK": "Macedonia",
                "MY": "Malaysia",
                "MT": "Malta",
                "MU": "Mauritius",
                "MX": "Mexico",
                "MD": "Moldova",
                "MC": "Monaco",
                "MN": "Mongolia",
                "ME": "Montenegro",
                "MA": "Morocco",
                "MM": "Myanmar",
                "NA": "Namibia",
                "NP": "Nepal",
                "NL": "Netherlands",
                "NZ": "New Zealand",
                "NI": "Nicaragua",
                "NG": "Nigeria",
                "NO": "Norway",
                "OM": "Oman",
                "PK": "Pakistan",
                "PA": "Panama",
                "PY": "Paraguay",
                "PE": "Peru",
                "PH": "Philippines",
                "PL": "Poland",
                "PT": "Portugal",
                "PR": "Puerto Rico",
                "QA": "Qatar",
                "RO": "Romania",
                "RU": "Russian Federation",
                "SM": "San Marino",
                "SA": "Saudi Arabia",
                "RS": "Serbia",
                "SG": "Singapore",
                "SK": "Slovak Republic",
                "SI": "Slovenia",
                "ZA": "South Africa",
                "ES": "Spain",
                "LK": "Sri Lanka",
                "SD": "Sudan",
                "SE": "Sweden",
                "CH": "Switzerland",
                "TW": "Taiwan",
                "TH": "Thailand",
                "TT": "Trinidad",
                "TN": "Tunisia",
                "TR": "Turkey",
                "UG": "Uganda",
                "UA": "Ukraine",
                "AE": "United Arab Emirates",
                "GB": "United Kingdom",
                "TZ": "United Republic of Tanzania",
                "US": "United States",
                "UY": "Uruguay",
                "UZ": "Uzbekistan",
                "VA": "Vatican City State",
                "VE": "Venezuela",
                "VN": "Vietnam",
                "YE": "Yemen",
                "ZM": "Zambia",
                "ZW": "Zimbabwe",
            }

        transformed_value = self.country_code_map.get(country_code)

        self.log(
            "Completed access point country code transformation. Input value: {0}, transformed value: {1}"
            .format(country_code, transformed_value),
            "DEBUG"
        )

        return transformed_value

    def transform_rf_radio_bands(self, rf_details):
        """
        Transforms radio frequencey radio band details into a list of enabled radio bands.

        Args:
            rf_details (dict): RF details containing radio band boolean flags.

        Returns:
            list: List of enabled radio bands.
        """

        self.log(
            "Starting RF radio bands transformation for rf details: {0}"
            .format(rf_details),
            "DEBUG"
        )

        mapping = {
            2.4: "enableRadioTypeB",
            5: "enableRadioTypeA",
            6: "enableRadioType6GHz",
        }

        result = []
        for list_value, boolean_key in mapping.items():
            boolean_value = rf_details.get(boolean_key, False)
            self.log(
                "Checking key '{0}': {1}".format(boolean_key, boolean_value), "DEBUG"
            )
            if boolean_value:
                result.append(list_value)

        self.log(
            "Completed RF radio bands transformation. Transformed value: {0}"
            .format(result),
            "DEBUG"
        )

        return result

    def transform_ap_management_settings(self, ap_details):
        """
        Transforms access point management settings details.

        Args:
            ap_details (dict): Access point details containing management settings.


        Returns:
            dict: Dictionary containing transformed access point management settings.
        """

        self.log(
            "Starting AP management settings transformation for ap details: {0}"
            .format(ap_details.get("managementSetting", "Unknown")),
            "DEBUG"
        )

        management_settings = ap_details.get("managementSetting")

        if not management_settings:
            self.log("No management setting provided for transformation", "DEBUG")
            return management_settings

        management_settings_temp_spec = self.ap_management_settings_temp_spec(ap_details.get("apProfileName", ""))
        modified_details = self.modify_parameters(management_settings_temp_spec, [management_settings])[0]

        self.log(
            "Completed AP management settings transformation. Transformed value: {0}"
            .format(modified_details),
            "DEBUG"
        )

        return modified_details

    def str_numbers_to_numeric_list(self, values):
        """
        Converts comma-separated numeric string into list with `int`/`float` values.

        Args:
            values (str): Comma-separated numeric string.
                Example: "1,2.5,3,4,5"

        Returns:
            list: Numeric list where integer tokens are converted to `int` and
                decimal tokens are converted to `float`.
        """
        self.log(
            "Starting numeric-list transformation for input: {0}".format(values),
            "DEBUG"
        )

        if values is None or not str(values).strip():
            self.log("Input is empty. Returning None", "DEBUG")
            return None

        result = []
        for token in str(values).split(","):
            token = token.strip()
            if not token:
                continue
            if "." in token:
                result.append(float(token))
            else:
                result.append(int(token))

        self.log(
            "Completed numeric-list transformation. Output: {0}".format(result),
            "DEBUG"
        )
        return result

    def feature_template_attributes_mapping(self, attribute):
        """
        Maps feature-template attribute name to Catalyst Center feature template type.

        Args:
            attribute (str): Feature-template attribute name from playbook/config
                (for example: aaa_radius_attribute, advanced_ssid).

        Returns:
            str: Feature template type corresponding to the provided attribute.
                Returns None if attribute is unsupported.
        """

        self.log(
            "Resolving feature template type for attribute: {0}".format(
                attribute if attribute is not None else "Unknown"
            ),
            "DEBUG",
        )

        attribute_to_template_type = {
            "aaa_radius_attribute": "AAA_RADIUS_ATTRIBUTES_CONFIGURATION",
            "advanced_ssid": "ADVANCED_SSID_CONFIGURATION",
            "clean_air_configuration": "CLEANAIR_CONFIGURATION",
            "dot11ax_configuration": "DOT11AX_CONFIGURATION",
            "dot11be_configuration": "DOT11BE_STATUS_CONFIGURATION",
            "event_driven_rrm_configuration": "EVENT_DRIVEN_RRM_CONFIGURATION",
            "flexconnect_configuration": "FLEX_CONFIGURATION",
            "multicast_configuration": "MULTICAST_CONFIGURATION",
            "rrm_fra_configuration": "RRM_FRA_CONFIGURATION",
            "rrm_general_configuration": "RRM_GENERAL_CONFIGURATION",
        }

        feature_template_type = attribute_to_template_type.get(attribute)
        if not feature_template_type:
            self.log(
                "No feature template type mapping found for attribute: {0}".format(attribute),
                "WARNING",
            )
            return None

        self.log(
            "Resolved feature template type for attribute '{0}': {1}".format(
                attribute, feature_template_type
            ),
            "DEBUG",
        )
        return feature_template_type

    def get_site_id(self, site_name):
        """
        Retrieve the site ID and check if the site exists in Cisco Catalyst Center based on the provided site name.

        Args:
            site_name (str): The name or hierarchy of the site to be retrieved.

        Returns:
            The site ID (str) if the site exists, or None if the site does not exist.
        """
        try:
            self.log("Retrieving site details from site: {0}".format(site_name), "DEBUG")

            response = self.get_site(site_name)

            # Check if the response is empty
            if response is None:
                self.log(
                    "No response from get_site with site_name: {0}".format(site_name),
                    "DEBUG"
                )
                return response

            site_response = response.get("response")
            if not site_response:
                self.log(
                    "No site response found in the response: {0}".format(site_response),
                    "WARNING"
                )
                return site_response

            site_id = site_response[0].get("id")
            self.log(
                "Site details retrieved for site '{0}'': {1}. Retrieved site id: {2}."
                .format(site_name, str(response), site_id),
                "DEBUG"
            )
            return site_id

        except Exception as e:
            self.log(
                "An exception occurred while retrieving site details for site '{0}'. Error: {1}"
                .format(site_name, e),
                "ERROR"
            )
            return None

    def get_global_site_id(self):
        """
        Retrieves the site ID for the Global site.

        Returns:
            str: Global site ID.

        Raises:
            Exits module execution when Global site ID cannot be retrieved.
        """

        self.log("Starting retrieval of Global site id.", "DEBUG")
        global_site_id = self.get_site_id("Global")

        if not global_site_id:
            self.msg = "Unable to fetch 'Global' site id. Failing and exiting workflow."
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        self.log(
            "Successfully retrieved Global site id: {0}".format(global_site_id),
            "DEBUG",
        )
        return global_site_id

    def get_feature_template_attributes_with_type(self, feature_template_type):
        """
        Retrieves feature-template metadata for a given feature template type.

        Args:
            feature_template_type (str): Feature template type from Catalyst Center API.

        Returns:
            dict: Dictionary containing temp spec, attribute name, and API function
                for the provided feature template type. Returns None when type is unsupported.
        """

        self.log(
            "Resolving feature template attributes for type: {0}".format(
                feature_template_type if feature_template_type is not None else "Unknown"
            ),
            "DEBUG",
        )

        feature_template_attributes_map = {
            "AAA_RADIUS_ATTRIBUTES_CONFIGURATION": {
                "temp_spec": self.wireless_aaa_radius_attribute_config_temp_spec(),
                "attribute_name": "aaa_radius_attribute",
                "api_function": "get_aaa_radius_attributes_configuration_feature_template"
            },
            "ADVANCED_SSID_CONFIGURATION": {
                "temp_spec": self.wireless_advanced_ssid_config_temp_spec(),
                "attribute_name": "advanced_ssid",
                "api_function": "get_advanced_ssid_configuration_feature_template"
            },
            "CLEANAIR_CONFIGURATION": {
                "temp_spec": self.wireless_clean_air_config_temp_spec(),
                "attribute_name": "clean_air_configuration",
                "api_function": "get_clean_air_configuration_feature_template",
            },
            "DOT11AX_CONFIGURATION": {
                "temp_spec": self.wireless_dot11ax_config_temp_spec(),
                "attribute_name": "dot11ax_configuration",
                "api_function": "get_dot11ax_configuration_feature_template",
            },
            "DOT11BE_STATUS_CONFIGURATION": {
                "temp_spec": self.wireless_dot11be_config_temp_spec(),
                "attribute_name": "dot11be_configuration",
                "api_function": "get_dot11be_status_configuration_feature_template",
            },
            "EVENT_DRIVEN_RRM_CONFIGURATION": {
                "temp_spec": self.wireless_event_driven_rrm_config_temp_spec(),
                "attribute_name": "event_driven_rrm_configuration",
                "api_function": "get_event_driven_r_r_m_configuration_feature_template",
            },
            "FLEX_CONFIGURATION": {
                "temp_spec": self.wireless_feature_template_flexconnect_config_temp_spec(),
                "attribute_name": "flexconnect_configuration",
                "api_function": "get_flex_connect_configuration_feature_template",
            },
            "MULTICAST_CONFIGURATION": {
                "temp_spec": self.wireless_multicast_config_temp_spec(),
                "attribute_name": "multicast_configuration",
                "api_function": "get_multicast_configuration_feature_template",
            },
            "RRM_FRA_CONFIGURATION": {
                "temp_spec": self.wireless_rrm_fra_config_temp_spec(),
                "attribute_name": "rrm_fra_configuration",
                "api_function": "get_r_r_m_f_r_a_configuration_feature_template",
            },
            "RRM_GENERAL_CONFIGURATION": {
                "temp_spec": self.wireless_rrm_rrm_general_config_temp_spec(),
                "attribute_name": "rrm_general_configuration",
                "api_function": "get_r_r_m_general_configuration_feature_template",
            },
        }

        feature_template_attributes = feature_template_attributes_map.get(feature_template_type)
        if not feature_template_attributes:
            self.log(
                "No feature template mapping found for type: {0}".format(feature_template_type),
                "WARNING",
            )
            return None

        self.log(
            "Resolved feature template mapping for type '{0}': attribute_name='{1}', api_function='{2}'".format(
                feature_template_type,
                feature_template_attributes.get("attribute_name"),
                feature_template_attributes.get("api_function"),
            ),
            "DEBUG",
        )
        return feature_template_attributes

    def get_feature_template_details_with_type(self, feature_template_type, feature_template_instances):
        """
        Retrieves and transforms feature template details for a specific feature template type.

        Args:
            feature_template_type (str): Feature template type from Catalyst Center API.
            feature_template_instances (dict): Dictionary mapping instance design name to instance id.

        Returns:
            list: A list containing one dictionary with transformed feature template details.
                Returns an empty list when no details are retrieved.
        """

        self.log(
            "Starting retrieval of feature template details for type '{0}' with instances: {1}".format(
                feature_template_type, feature_template_instances
            ),
            "DEBUG",
        )

        feature_template_attributes = self.get_feature_template_attributes_with_type(
            feature_template_type
        )
        if not feature_template_attributes:
            self.log(
                "Feature template attributes not found for type '{0}'. Returning empty result.".format(
                    feature_template_type
                ),
                "WARNING",
            )
            return []

        api_function = feature_template_attributes.get("api_function")
        temp_spec = feature_template_attributes.get("temp_spec")
        attribute_name = feature_template_attributes.get("attribute_name")

        if api_function is None or temp_spec is None or attribute_name is None:
            self.log(
                "Incomplete feature template attributes for type '{0}'. api_function={1}, temp_spec={2}, "
                "attribute_name={3}. Returning empty result.".format(
                    feature_template_type, api_function, bool(temp_spec), attribute_name
                ),
                "WARNING",
            )
            return []

        if not isinstance(feature_template_instances, dict) or not feature_template_instances:
            self.log(
                "No valid feature template instances provided for type '{0}'. Returning empty result.".format(
                    feature_template_type
                ),
                "DEBUG",
            )
            return []

        final_feature_template_details = []
        for feature_template_instance, feature_template_instance_id in feature_template_instances.items():
            if feature_template_instance_id is None:
                self.log(
                    "Skipping feature template instance '{0}' for type '{1}' due to missing id.".format(
                        feature_template_instance, feature_template_type
                    ),
                    "DEBUG",
                )
                continue

            params = {"type": feature_template_type, "id": feature_template_instance_id}
            self.log(
                "Fetching feature template details for instance '{0}' with params: {1}".format(
                    feature_template_instance, params
                ),
                "DEBUG",
            )

            feature_template_details = self.execute_get_with_pagination(
                "wireless", api_function, params, limit=25
            )

            if not feature_template_details:
                self.log(
                    "No feature template details found for instance '{0}' (id: {1}).".format(
                        feature_template_instance, feature_template_instance_id
                    ),
                    "DEBUG",
                )
                continue

            transformed_feature_template_details = self.modify_parameters(
                temp_spec, feature_template_details
            )
            final_feature_template_details.extend(transformed_feature_template_details)
            self.log(
                "Transformed {0} feature template detail record(s) for instance '{1}'.".format(
                    len(transformed_feature_template_details), feature_template_instance
                ),
                "DEBUG",
            )

        if not final_feature_template_details:
            return []

        modified_feature_template_details = [
            {attribute_name: final_feature_template_details}
        ]

        self.log(
            "Completed retrieval of feature template details for type '{0}'. Result: {1}".format(
                feature_template_type, modified_feature_template_details
            ),
            "DEBUG"
        )
        return modified_feature_template_details

    def fetch_instances_from_feature_template_config(self, feature_template_config):
        """
        Extracts feature template instances grouped by feature template type.

        Args:
            feature_template_config (list): List of feature template configuration entries.
                Each entry is expected to contain:
                - type (str): Feature template type
                - instances (list): List of instance objects with designName and id

        Returns:
            dict: Dictionary in the format:
                {
                    "<feature_template_type>": {
                        "<designName>": "<id>"
                    }
                }
        """

        self.log(
            "Starting extraction of feature template instances from configuration payload.",
            "DEBUG",
        )

        feature_template_config_instances = {}
        if not feature_template_config:
            self.log(
                "No feature template configuration provided. Returning empty mapping.",
                "DEBUG",
            )
            return feature_template_config_instances

        self.log(
            "Processing {0} feature template configuration entries.".format(
                len(feature_template_config)
            ),
            "DEBUG",
        )

        for index, feature_template_config_entry in enumerate(feature_template_config, start=1):
            feature_template_type = feature_template_config_entry.get("type")
            feature_template_instances = feature_template_config_entry.get("instances")
            if not feature_template_type or not feature_template_instances:
                self.log(
                    "Skipping feature template configuration entry at index {0} due to missing "
                    "'type' or 'instances'.".format(index),
                    "DEBUG",
                )
                continue

            feature_template_config_instances[feature_template_type] = {
                item.get("designName"): item.get("id")
                for item in feature_template_instances
                if isinstance(item, dict)
                and item.get("designName") is not None
                and item.get("id") is not None
            }

            self.log(
                "Mapped {0} instance(s) for feature template type '{1}'.".format(
                    len(feature_template_config_instances[feature_template_type]),
                    feature_template_type,
                ),
                "DEBUG",
            )

        self.log(
            "Completed feature template instance extraction. Final mapping: {0}".format(
                feature_template_config_instances
            ),
            "DEBUG",
        )
        return feature_template_config_instances

    def get_wireless_ssids(self, network_element, filters):
        """
        Retrieves wireless ssids based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless ssids.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless ssids.

        Returns:
            dict: A dictionary containing the modified details of wireless ssids.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless ssids with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_wireless_ssids = []
        self.log(
            "Getting wireless ssids using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless ssids retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                site_id = None
                supported_keys = {"site_name_hierarchy", "ssid_name", "ssid_type"}
                if "site_name_hierarchy" in filter_param:
                    value = filter_param.get("site_name_hierarchy")
                    site_id = self.get_site_id(value)
                    if not site_id:
                        self.log(
                            "The site '{0}' does not exist in the Catalyst Center, skipping processing."
                            .format(value),
                            "WARNING"
                        )
                        continue

                    self.log(
                        "Mapped site name hierarchy '{0}' to site ID '{1}'.".format(
                            value, site_id
                        ),
                        "DEBUG"
                    )
                else:
                    site_id = self.get_global_site_id()

                params['site_id'] = site_id

                if "ssid_name" in filter_param:
                    params['ssid'] = filter_param.get("ssid_name")
                if "ssid_type" in filter_param:
                    params['wlanType'] = filter_param.get("ssid_type")

                unsupported_keys = set(filter_param.keys()) - supported_keys
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless ssids: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless ssids with parameters: {0}".format(params),
                    "DEBUG"
                )
                wireless_ssid_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if wireless_ssid_details:
                    final_wireless_ssids.extend(wireless_ssid_details)
                    self.log(
                        "Retrieved {0} wireless ssid(s): {1}".format(
                            len(wireless_ssid_details), wireless_ssid_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No wireless ssids found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless ssids retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless ssids from Catalyst Center using Global Site ID", "DEBUG")

            params['site_id'] = self.get_global_site_id()

            wireless_ssid_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if wireless_ssid_details:
                final_wireless_ssids.extend(wireless_ssid_details)
                self.log(
                    "Retrieved {0} wireless ssid(s) from Catalyst Center".format(
                        len(wireless_ssid_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless ssids found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} wireless ssid(s) using wireless_ssid temp spec".format(
                len(final_wireless_ssids)
            ),
            "DEBUG"
        )
        wireless_ssid_temp_spec = self.wireless_ssid_temp_spec()
        ssid_details = self.modify_parameters(
            wireless_ssid_temp_spec, final_wireless_ssids
        )
        modified_ssid_details = {}

        if ssid_details:
            modified_ssid_details['ssids'] = ssid_details

        self.log(
            "Completed retrieving wireless ssid(s): {0}".format(
                modified_ssid_details
            ),
            "INFO",
        )

        return modified_ssid_details

    def get_wireless_interfaces(self, network_element, filters):
        """
        Retrieves wireless interfaces based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless interfaces.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless interfaces.

        Returns:
            dict: A dictionary containing the modified details of wireless interfaces.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless interfaces with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_wireless_interfaces = []
        self.log(
            "Getting wireless interfaces using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless interfaces retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                supported_keys = {"interface_name", "vlan_id"}

                if "interface_name" in filter_param:
                    params['interfaceName'] = filter_param.get("interface_name")
                if "vlan_id" in filter_param:
                    params['vlanId'] = filter_param.get("vlan_id")

                unsupported_keys = set(filter_param.keys()) - supported_keys
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless interfaces: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless interfaces with parameters: {0}".format(params),
                    "DEBUG"
                )
                wireless_interface_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if wireless_interface_details:
                    final_wireless_interfaces.extend(wireless_interface_details)
                    self.log(
                        "Retrieved {0} wireless interface(s): {1}".format(
                            len(wireless_interface_details), wireless_interface_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No wireless interfaces found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless interfaces retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless interfaces from Catalyst Center", "DEBUG")

            wireless_interface_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if wireless_interface_details:
                final_wireless_interfaces.extend(wireless_interface_details)
                self.log(
                    "Retrieved {0} wireless interface(s) from Catalyst Center".format(
                        len(wireless_interface_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless interfaces found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} wireless interface(s) using wireless_interface temp spec".format(
                len(final_wireless_interfaces)
            ),
            "DEBUG"
        )
        wireless_interface_temp_spec = self.wireless_interfaces_temp_spec()
        interface_details = self.modify_parameters(
            wireless_interface_temp_spec, final_wireless_interfaces
        )
        modified_interface_details = {}

        if interface_details:
            modified_interface_details['interfaces'] = interface_details

        self.log(
            "Completed retrieving wireless interfaces: {0}".format(
                modified_interface_details
            ),
            "INFO",
        )

        return modified_interface_details

    def get_wireless_power_profiles(self, network_element, filters):
        """
        Retrieves wireless power profiles based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless power profiles.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless power profiles.

        Returns:
            dict: A dictionary containing the modified details of wireless power profiles.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless power profiles with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_wireless_power_profiles = []
        self.log(
            "Getting wireless power profiles using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless power profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:

                if "power_profile_name" in filter_param:
                    params['profileName'] = filter_param.get("power_profile_name")

                unsupported_keys = set(filter_param.keys()) - {"power_profile_name"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless power profiles: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless power profiles with parameters: {0}".format(params),
                    "DEBUG"
                )
                wireless_power_profile_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if wireless_power_profile_details:
                    final_wireless_power_profiles.extend(wireless_power_profile_details)
                    self.log(
                        "Retrieved {0} wireless power profile(s): {1}".format(
                            len(wireless_power_profile_details), wireless_power_profile_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No wireless power profiles found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless power profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless power profiles from Catalyst Center", "DEBUG")

            wireless_power_profile_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if wireless_power_profile_details:
                final_wireless_power_profiles.extend(wireless_power_profile_details)
                self.log(
                    "Retrieved {0} wireless power profile(s) from Catalyst Center".format(
                        len(wireless_power_profile_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless power profiles found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} wireless power profile(s) using wireless_power_profile temp spec".format(
                len(final_wireless_power_profiles)
            ),
            "DEBUG"
        )
        wireless_power_profile_temp_spec = self.wireless_power_profiles_temp_spec()
        power_profiles_details = self.modify_parameters(
            wireless_power_profile_temp_spec, final_wireless_power_profiles
        )
        modified_power_profiles_details = {}

        if power_profiles_details:
            modified_power_profiles_details['power_profiles'] = power_profiles_details

        self.log(
            "Completed retrieving wireless power profiles: {0}".format(
                modified_power_profiles_details
            ),
            "INFO",
        )

        return modified_power_profiles_details

    def get_wireless_access_point_profiles(self, network_element, filters):
        """
        Retrieves wireless access point profiles based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless access point profiles.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless access point profiles.

        Returns:
            dict: A dictionary containing the modified details of wireless access point profiles.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless access point profiles with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_wireless_access_point_profiles = []
        self.log(
            "Getting wireless access point profiles using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless access point profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:

                if "ap_profile_name" in filter_param:
                    params['apProfileName'] = filter_param.get("ap_profile_name")

                unsupported_keys = set(filter_param.keys()) - {"ap_profile_name"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless access point profiles: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless access point profiles with parameters: {0}".format(params),
                    "DEBUG"
                )
                wireless_access_point_profile_details = self.execute_get_with_pagination(
                    api_family, api_function, params, use_strings=True
                )

                if wireless_access_point_profile_details:
                    final_wireless_access_point_profiles.extend(wireless_access_point_profile_details)
                    self.log(
                        "Retrieved {0} wireless access point profile(s): {1}".format(
                            len(wireless_access_point_profile_details), wireless_access_point_profile_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No wireless access point profiles found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless access point profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless access point profiles from Catalyst Center", "DEBUG")

            wireless_access_point_profile_details = self.execute_get_with_pagination(
                api_family, api_function, params, use_strings=True
            )

            if wireless_access_point_profile_details:
                final_wireless_access_point_profiles.extend(wireless_access_point_profile_details)
                self.log(
                    "Retrieved {0} wireless access point profile(s) from Catalyst Center".format(
                        len(wireless_access_point_profile_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless access point profiles found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} wireless access point profile(s) using wireless_access_point_profile temp spec".format(
                len(final_wireless_access_point_profiles)
            ),
            "DEBUG"
        )
        wireless_access_point_profile_temp_spec = self.wireless_access_point_profiles_temp_spec()
        access_point_profiles_details = self.modify_parameters(
            wireless_access_point_profile_temp_spec, final_wireless_access_point_profiles
        )
        modified_access_point_profiles_details = {}

        if access_point_profiles_details:
            modified_access_point_profiles_details['access_point_profiles'] = access_point_profiles_details

        self.log(
            "Completed retrieving wireless access point profiles: {0}".format(
                modified_access_point_profiles_details
            ),
            "INFO",
        )

        return modified_access_point_profiles_details

    def get_wireless_radio_frequency_profiles(self, network_element, filters):
        """
        Retrieves wireless radio frequency profiles based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless radio frequency profiles.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless radio frequency profiles.

        Returns:
            dict: A dictionary containing the modified details of wireless radio frequency profiles.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless radio frequency profiles with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_wireless_radio_frequency_profiles = []
        self.log(
            "Getting wireless radio frequency profiles using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless radio frequency profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:

                if "rf_profile_name" in filter_param:
                    params['rfProfileName'] = filter_param.get("rf_profile_name")

                unsupported_keys = set(filter_param.keys()) - {"rf_profile_name"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless radio frequency profiles: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless radio frequency profiles with parameters: {0}".format(params),
                    "DEBUG"
                )
                wireless_radio_frequency_profile_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if wireless_radio_frequency_profile_details:
                    final_wireless_radio_frequency_profiles.extend(wireless_radio_frequency_profile_details)
                    self.log(
                        "Retrieved {0} wireless radio frequency profile(s): {1}".format(
                            len(wireless_radio_frequency_profile_details), wireless_radio_frequency_profile_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No wireless radio frequency profiles found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless radio frequency profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless radio frequency profiles from Catalyst Center", "DEBUG")

            wireless_radio_frequency_profile_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if wireless_radio_frequency_profile_details:
                final_wireless_radio_frequency_profiles.extend(wireless_radio_frequency_profile_details)
                self.log(
                    "Retrieved {0} wireless radio frequency profile(s) from Catalyst Center".format(
                        len(wireless_radio_frequency_profile_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless radio frequency profiles found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} wireless radio frequency profile(s) using wireless_radio_frequency_profile temp spec".format(
                len(final_wireless_radio_frequency_profiles)
            ),
            "DEBUG"
        )
        wireless_radio_frequency_profile_temp_spec = self.wireless_radio_frequency_profiles_temp_spec()
        radio_frequency_profiles_details = self.modify_parameters(
            wireless_radio_frequency_profile_temp_spec, final_wireless_radio_frequency_profiles
        )
        modified_radio_frequency_profiles_details = {}

        if radio_frequency_profiles_details:
            modified_radio_frequency_profiles_details['radio_frequency_profiles'] = radio_frequency_profiles_details

        self.log(
            "Completed retrieving wireless radio frequency profiles: {0}".format(
                modified_radio_frequency_profiles_details
            ),
            "INFO",
        )

        return modified_radio_frequency_profiles_details

    def get_wireless_anchor_groups(self, network_element, filters):
        """
        Retrieves wireless anchor groups based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless anchor groups.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless anchor groups.

        Returns:
            dict: A dictionary containing the modified details of wireless anchor groups.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless anchor groups with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_wireless_anchor_groups = []
        self.log(
            "Getting wireless anchor groups using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless anchor groups retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:

                unsupported_keys = set(filter_param.keys()) - {"anchor_group_name"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless anchor groups: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless anchor groups with parameters: {0}".format(params),
                    "DEBUG"
                )
                wireless_anchor_group_details = self.execute_get_with_pagination(
                    api_family, api_function, params, use_strings=True
                )

                if "anchor_group_name" in filter_param:
                    anchor_group_name = filter_param.get("anchor_group_name")
                    wireless_anchor_group_details = [item for item in wireless_anchor_group_details if item.get("anchorGroupName") == anchor_group_name]

                if wireless_anchor_group_details:
                    final_wireless_anchor_groups.extend(wireless_anchor_group_details)
                    self.log(
                        "Retrieved {0} wireless anchor group(s): {1}".format(
                            len(wireless_anchor_group_details), wireless_anchor_group_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log("No wireless anchor groups found with filter params: {0}".format(filter_param), "DEBUG")
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless anchor groups retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless anchor groups from Catalyst Center", "DEBUG")

            wireless_anchor_group_details = self.execute_get_with_pagination(
                api_family, api_function, params, use_strings=True
            )

            if wireless_anchor_group_details:
                final_wireless_anchor_groups.extend(wireless_anchor_group_details)
                self.log(
                    "Retrieved {0} wireless anchor group(s) from Catalyst Center".format(
                        len(wireless_anchor_group_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless anchor groups found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} wireless anchor group(s) using wireless_anchor_group temp spec".format(
                len(final_wireless_anchor_groups)
            ),
            "DEBUG"
        )
        wireless_anchor_group_temp_spec = self.wireless_anchor_groups_temp_spec()
        anchor_group_details = self.modify_parameters(
            wireless_anchor_group_temp_spec, final_wireless_anchor_groups
        )
        modified_anchor_group_details = {}

        if anchor_group_details:
            modified_anchor_group_details['anchor_groups'] = anchor_group_details

        self.log(
            "Completed retrieving wireless anchor groups: {0}".format(
                modified_anchor_group_details
            ),
            "INFO",
        )

        return modified_anchor_group_details

    def get_wireless_feature_template_config(self, network_element, filters):
        """
        Retrieves wireless feature template config based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless feature template config.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless feature template config.

        Returns:
            dict: A dictionary containing the modified details of wireless feature template config.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless feature template config with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        self.log(
            "Getting wireless feature template config using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        feature_template_config = self.execute_get_with_pagination(
            api_family, api_function, {}, limit=25
        )

        self.log(
            "Retrieved wireless feature template config: {0}".format(
                feature_template_config
            ),
            "DEBUG",
        )

        feature_template_instances = self.fetch_instances_from_feature_template_config(feature_template_config)
        if not feature_template_instances:
            self.log("No Feature Template Instances found. Skipping Processing", "DEBUG")
            return {}

        self.log(
            "Fetched wireless feature template instances: {0}".format(
                feature_template_instances
            ),
            "DEBUG",
        )

        final_feature_templates = []

        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless feature template config retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            supported_keys = {"feature_template_type", "design_name"}

            for filter_param in component_specific_filters:
                unsupported_keys = set(filter_param.keys()) - supported_keys
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless feature template config: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                final_feature_template_instances = {}

                has_design_name_filter_param = False

                if "design_name" in filter_param:
                    has_design_name_filter_param = True
                    design_name = filter_param.get("design_name")
                    for feature_template_type, feature_template_instance in feature_template_instances.items():
                        if feature_template_instance and feature_template_instance.get(design_name):
                            final_feature_template_instances[feature_template_type] = {
                                design_name: feature_template_instance.get(design_name)
                            }

                    self.log(
                        "Retrieved feature template instances : {0} using design name filter: {1}"
                        .format(final_feature_template_instances, design_name),
                        "DEBUG"
                    )

                if "feature_template_type" in filter_param:
                    feature_template_type = filter_param.get("feature_template_type")
                    if not feature_template_type:
                        self.log(
                            "Unsupported feature template type: {0}. Skipping Processing...".format(feature_template_type),
                            "WARNING"
                        )
                        continue
                    feature_template_type = self.feature_template_attributes_mapping(feature_template_type)

                    self.log(
                        "Mapped feature-template attribute name to Catalyst Center feature template type: {0}"
                        .format(feature_template_type),
                        "DEBUG"
                    )
                    if feature_template_type:
                        if has_design_name_filter_param:
                            final_feature_template_instances[feature_template_type] = final_feature_template_instances.get(feature_template_type)
                        else:
                            final_feature_template_instances[feature_template_type] = feature_template_instances.get(feature_template_type)

                self.log(
                    "Retrieved final feature template instances : {0} with params: {1}"
                    .format(final_feature_template_instances, filter_param),
                    "DEBUG"
                )

                if final_feature_template_instances:
                    for feature_template_type, feature_template_instance in final_feature_template_instances.items():
                        feature_template_details = self.get_feature_template_details_with_type(
                            feature_template_type,
                            feature_template_instance
                        )
                        final_feature_templates.extend(feature_template_details)
                        self.log(
                            "Retrieved {0} feature template config: {1}".format(
                                len(feature_template_details), feature_template_details
                            ),
                            "DEBUG"
                        )
                else:
                    self.log(
                        "No wireless feature template config found with filter params: {0}".format(filter_param),
                        "DEBUG"
                    )

            self.log(
                "Completed Processing {0} filter(s) for wireless feature template config retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless feature template config from Catalyst Center", "DEBUG")

            for feature_template_type, feature_template_instance in feature_template_instances.items():
                feature_template_details = self.get_feature_template_details_with_type(
                    feature_template_type,
                    feature_template_instance
                )

                if feature_template_details:
                    final_feature_templates.extend(feature_template_details)
                    self.log(
                        "Retrieved {0} wireless feature template config for template type: {1} from Catalyst Center".format(
                            len(feature_template_details), feature_template_type
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No wireless feature template config for template type: {0} found in Catalyst Center"
                        .format(feature_template_type),
                        "DEBUG"
                    )

        modified_feature_templates = {}
        if final_feature_templates:
            modified_feature_templates['feature_template_config'] = final_feature_templates

        self.log(
            "Completed retrieving wireless feature template config: {0}".format(
                modified_feature_templates
            ),
            "INFO",
        )
        return modified_feature_templates

    def get_wireless_802_11_be_profiles(self, network_element, filters):
        """
        Retrieves wireless 802.11be profiles based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless 802.11be profiles.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless 802.11be profiles.

        Returns:
            dict: A dictionary containing the modified details of wireless 802.11be profiles.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless 802.11be profiles with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_wireless_802_11be_profiles = []
        self.log(
            "Getting wireless 802.11be profiles using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless 802.11be profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:

                if "profile_name" in filter_param:
                    params["profileName"] = filter_param.get("profile_name")

                unsupported_keys = set(filter_param.keys()) - {"profile_name"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless 802.11be profiles: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless 802.11be profiles with parameters: {0}".format(params),
                    "DEBUG"
                )

                wireless_802_11be_profiles_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if wireless_802_11be_profiles_details:
                    final_wireless_802_11be_profiles.extend(wireless_802_11be_profiles_details)
                    self.log(
                        "Retrieved {0} wireless 802.11be profile(s): {1}".format(
                            len(wireless_802_11be_profiles_details), wireless_802_11be_profiles_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log("No wireless 802.11be profiles found with params: {0}".format(params), "DEBUG")
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless 802.11be profiles retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all wireless 802.11be profiles from Catalyst Center", "DEBUG")

            wireless_802_11be_profiles_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if wireless_802_11be_profiles_details:
                final_wireless_802_11be_profiles.extend(wireless_802_11be_profiles_details)
                self.log(
                    "Retrieved {0} wireless 802.11be profile(s) from Catalyst Center".format(
                        len(wireless_802_11be_profiles_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless 802.11be profiles found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} wireless 802.11be profile(s) using wireless_802_11be_profiles temp spec".format(
                len(final_wireless_802_11be_profiles)
            ),
            "DEBUG"
        )
        wireless_802_11be_profiles_temp_spec = self.wireless_802_11_be_profiles_temp_spec()
        wireless_802_11be_profiles_details = self.modify_parameters(
            wireless_802_11be_profiles_temp_spec, final_wireless_802_11be_profiles
        )
        modified_802_11be_profiles_details = {}

        if wireless_802_11be_profiles_details:
            modified_802_11be_profiles_details['802_11_be_profiles'] = wireless_802_11be_profiles_details

        self.log(
            "Completed retrieving wireless 802.11be profiles: {0}".format(
                modified_802_11be_profiles_details
            ),
            "INFO",
        )

        return modified_802_11be_profiles_details

    def get_wireless_flex_connect_configurations(self, network_element, filters):
        """
        Retrieves wireless flex connect configurations based on the provided network element and filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving wireless flex connect configurations.
            filters (dict): Dictionary containing global filters and component_specific_filters for wireless flex connect configurations.

        Returns:
            dict: A dictionary containing the modified details of wireless flex connect configurations.
        """

        component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve wireless flex connect configurations with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {}

        final_flex_connect_configs = []
        self.log(
            "Getting wireless flex connect configurations using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for wireless flex connect configurations retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                site_id = None

                if "site_name_hierarchy" in filter_param:
                    site_name = filter_param.get("site_name_hierarchy")
                    site_id = self.get_site_id(site_name)
                    if not site_id:
                        self.log(
                            "The site '{0}' does not exist in the Catalyst Center, skipping processing."
                            .format(site_name),
                            "WARNING"
                        )
                        continue

                    self.log(
                        "Mapped site name hierarchy '{0}' to site ID '{1}'.".format(
                            site_name, site_id
                        ),
                        "DEBUG"
                    )
                else:
                    site_id = self.get_global_site_id()

                params["site_id"] = site_id

                unsupported_keys = set(filter_param.keys()) - {"site_name_hierarchy"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for wireless flex connect configurations: {0}".format(
                            unsupported_keys
                        ),
                        "WARNING"
                    )

                self.log(
                    "Fetching wireless flex connect configurations with parameters: {0}".format(params),
                    "DEBUG"
                )

                flex_connect_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if flex_connect_details:
                    flex_connect_details = [
                        {**item, "siteNameHierarchy": site_name} for item in flex_connect_details
                    ]
                    final_flex_connect_configs.extend(flex_connect_details)
                    self.log(
                        "Retrieved {0} wireless flex connect configuration(s): {1}".format(
                            len(flex_connect_details), flex_connect_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No wireless flex connect configurations found for parameters: {0}".format(params),
                        "DEBUG"
                    )

                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for wireless flex connect configurations retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log(
                "Fetching all wireless flex connect configurations from Catalyst Center using Global Site ID",
                "DEBUG"
            )

            params["site_id"] = self.get_global_site_id()

            flex_connect_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if flex_connect_details:
                flex_connect_details = [
                    {**item, "siteNameHierarchy": "Global"} for item in flex_connect_details
                ]
                final_flex_connect_configs.extend(flex_connect_details)
                self.log(
                    "Retrieved {0} wireless flex connect configuration(s) from Catalyst Center".format(
                        len(flex_connect_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No wireless flex connect configurations found in Catalyst Center", "DEBUG")

        self.log(
            "Transforming {0} wireless flex connect configuration(s) using wireless_flex_connect_config temp spec".format(
                len(final_flex_connect_configs)
            ),
            "DEBUG"
        )

        wireless_flex_connect_temp_spec = self.wireless_flex_connect_config_temp_spec()
        flex_connect_config_details = self.modify_parameters(
            wireless_flex_connect_temp_spec, final_flex_connect_configs
        )

        modified_flex_connect_config_details = {}
        if flex_connect_config_details:
            modified_flex_connect_config_details["flex_connect_configuration"] = flex_connect_config_details

        self.log(
            "Completed retrieving wireless flex connect configuration(s): {0}".format(
                modified_flex_connect_config_details
            ),
            "INFO",
        )

        return modified_flex_connect_config_details

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for wireless design workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.
        """

        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
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
        self.log("Beginning iteration over defined workflow operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
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

                try:
                    operation_func(params).check_return_status()
                    operations_executed += 1
                    self.log(
                        "{0} operation completed successfully".format(operation_name),
                        "DEBUG"
                    )
                except Exception as e:
                    self.log(
                        "{0} operation failed with error: {1}".format(operation_name, str(e)),
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
                    "Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                        index, operation_name
                    ),
                    "WARNING",
                )

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
    # Define the specification for the module"s arguments
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
        "config": {"required": True, "type": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)

    # Initialize the NetworkCompliance object with the module
    config_generator = WirelessDesignPlaybookConfigGenerator(module)
    if (
        config_generator.compare_dnac_versions(
            config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for WIRELESS DESIGN Module. Supported versions start from '2.3.7.9' onwards. ".format(
                config_generator.get_ccc_version()
            )
        )
        config_generator.set_operation_result(
            "failed", False, config_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = config_generator.params.get("state")

    # Check if the state is valid
    if state not in config_generator.supported_states:
        config_generator.status = "invalid"
        config_generator.msg = "State {0} is invalid".format(state)
        config_generator.check_return_status()

    # Validate the input parameters and check the return status
    config_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    config = config_generator.validated_config
    config_generator.reset_values()
    config_generator.get_want(config, state).check_return_status()
    config_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**config_generator.result)


if __name__ == "__main__":
    main()

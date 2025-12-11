#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wired Campus Automation Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Rugvedi Kapse, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_wired_campus_automation_playbook_generator
short_description: Generate YAML configurations playbook for 'wired_campus_automation_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'wired_campus_automation_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the layer 2 configurations deployed
  on network devices within the Cisco Catalyst Center.
- Supports extraction of VLANs, CDP, LLDP, STP, VTP, DHCP Snooping, IGMP Snooping,
  MLD Snooping, Authentication, Logical Ports, and Port Configuration settings.
version_added: 6.40.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Rugvedi Kapse (@rukapse)
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
      - A list of filters for generating YAML playbook compatible with the 'wired_campus_automation_workflow_manager'
        module.
      - Filters specify which components and devices to include in the YAML configuration file.
      - Global filters identify target devices by IP address, hostname, or serial number.
      - Component-specific filters allow selection of specific layer2 features and detailed filtering.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all devices and all supported layer2 features.
          - This mode discovers all managed devices in Cisco Catalyst Center and extracts all supported configurations.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete brownfield infrastructure discovery and documentation.
          - IMPORTANT NOTE - Currently, this module only supports layer2 configurations.
            When generate_all_configurations is enabled, it will attempt to retrieve layer2 configurations
            from ALL managed devices without filtering for layer2 capability.
            This may result in API errors for devices that do not support layer2 configuration features
            (such as older switch models, routers, wireless controllers, etc.).
            It is recommended to use specific device filters (ip_address_list, hostname_list,
            or serial_number_list) to target only layer2-capable devices when not using generate_all_configurations mode.
          - Supported layer2 devices include Catalyst 9000 series switches (9200/9300/9350/9400/9500/9600)
            and IE series switches (IE3400/IE3400H/IE3500/IE9300) running IOS-XE 17.3 or higher.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name  "wired_campus_automation_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
          - For example, "wired_campus_automation_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
        required: false
      global_filters:
        description:
          - Global filters to apply when generating the YAML configuration file.
          - These filters identify which network devices to extract configurations from.
          - At least one filter type must be specified to identify target devices.
        type: dict
        required: false
        suboptions:
          ip_address_list:
            description:
              - List of device IP addresses to extract configurations from.
              - HIGHEST PRIORITY - If provided, serial numbers and hostnames will be ignored.
              - Each IP address must be a valid IPv4 address format.
              - Devices must be managed by Cisco Catalyst Center.
              - Example ["192.168.1.10", "192.168.1.11", "10.1.1.5"]
            type: list
            elements: str
            required: false
          serial_number_list:
            description:
              - List of device serial numbers to extract configurations from.
              - MEDIUM PRIORITY - Only used if ip_address_list is not provided.
              - Serial numbers must match those registered in Catalyst Center.
              - Useful when IP addresses may change but serial numbers remain constant.
              - If both serial_number_list and hostname_list are provided, serial_number_list takes priority.
              - Example ["FCW2140L05Y", "FCW2140L06Z", "9080V0I41J3"]
            type: list
            elements: str
            required: false
          hostname_list:
            description:
              - List of device hostnames to extract configurations from.
              - LOWEST PRIORITY - Only used if neither ip_address_list nor serial_number_list are provided.
              - Hostnames must match those registered in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Example ["switch01.lab.com", "core-switch-01", "access-sw-floor2"]
            type: list
            elements: str
            required: false
      component_specific_filters:
        description:
          - Filters to specify which layer2 components and features to include in the YAML configuration file.
          - Allows granular selection of specific features and their parameters.
          - If not specified, all supported layer2 features will be extracted.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
              - List of components to include in the YAML configuration file.
              - Valid values are ["layer2_configurations"]
              - If not specified, all supported components are included.
              - Future versions may support additional component types.
            type: list
            elements: str
            required: false
          layer2_features:
            description:
              - List of specific layer2 features to extract from devices.
              - Valid values are ["vlans", "cdp", "lldp", "stp", "vtp", "dhcp_snooping",
                "igmp_snooping", "mld_snooping", "authentication", "logical_ports", "port_configuration"]
              - If not specified, all supported layer2 features will be extracted.
              - Example ["vlans", "stp", "cdp"] to extract only VLAN, STP, and CDP configurations.
            type: list
            elements: str
            required: false
            choices: ["vlans", "cdp", "lldp", "stp", "vtp", "dhcp_snooping",
                     "igmp_snooping", "mld_snooping", "authentication",
                     "logical_ports", "port_configuration"]
          vlans:
            description:
              - Specific VLAN filtering options.
              - Allows extraction of only specific VLANs based on VLAN IDs.
              - If not specified, all VLANs configured on the device will be extracted.
            type: dict
            required: false
            suboptions:
              vlan_ids_list:
                description:
                  - List of specific VLAN IDs to extract from devices.
                  - Each VLAN ID must be between 1 and 4094.
                  - Only VLANs in this list will be included in the generated configuration.
                  - Example ["10", "20", "100", "200"] to extract only these specific VLANs.
                type: list
                elements: str
                required: false
          port_configuration:
            description:
              - Specific port configuration filtering options.
              - Allows extraction of configurations for only specific interfaces.
              - If not specified, all configured interfaces will be extracted.
            type: dict
            required: false
            suboptions:
              interface_names_list:
                description:
                  - List of specific interface names to extract configurations from.
                  - Interface names must match the format used by the device.
                  - Example ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "TenGigabitEthernet1/0/1"]
                  - Only interfaces in this list will have their configurations extracted.
                type: list
                elements: str
                required: false
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
  - devices.Devices.get_device_list
  - wired.Wired.get_configurations_for_a_deployed_layer2_feature_on_a_wired_device
- Paths used are
  - GET /dna/intent/api/v1/network-device
  - GET /dna/intent/api/v1/networkDevices/${id}/configFeatures/deployed/layer2/${feature}
"""

EXAMPLES = r"""

# NOT Recommended for actual use cases due to potential API errors on non-layer2 devices.
# - name: Auto-generate YAML Configuration for all devices and features
#   cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
#     dnac_host: "{{dnac_host}}"
#     dnac_username: "{{dnac_username}}"
#     dnac_password: "{{dnac_password}}"
#     dnac_verify: "{{dnac_verify}}"
#     dnac_port: "{{dnac_port}}"
#     dnac_version: "{{dnac_version}}"
#     dnac_debug: "{{dnac_debug}}"
#     dnac_log: true
#     dnac_log_level: "{{dnac_log_level}}"
#     state: gathered
#     config:
#       - generate_all_configurations: true

# NOT Recommended for actual use cases due to potential API errors on non-layer2 devices.
# - name: Auto-generate YAML Configuration with custom file path
#   cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
#     dnac_host: "{{dnac_host}}"
#     dnac_username: "{{dnac_username}}"
#     dnac_password: "{{dnac_password}}"
#     dnac_verify: "{{dnac_verify}}"
#     dnac_port: "{{dnac_port}}"
#     dnac_version: "{{dnac_version}}"
#     dnac_debug: "{{dnac_debug}}"
#     dnac_log: true
#     dnac_log_level: "{{dnac_log_level}}"
#     state: gathered
#     config:
#       - file_path: "/tmp/complete_infrastructure_config.yml"

- name: Generate YAML Configuration with default file path
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - global_filters:
          ip_address_list: ["192.168.1.10"]

- name: Generate YAML Configuration with specific devices by IP address
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

- name: Generate YAML Configuration with specific devices by hostname
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          hostname_list: ["switch01.lab.com", "switch02.lab.com", "core-switch-01"]

- name: Generate YAML Configuration with specific devices by serial number
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          serial_number_list: ["FCW2140L05Y", "FCW2140L06Z", "9080V0I41J3"]

- name: Generate YAML Configuration with specific devices by hostname
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          hostname_list: ["switch01.lab.com", "switch02.lab.com", "core-switch-01"]

- name: Generate YAML Configuration with specific devices by serial number
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          serial_number_list: ["FCW2140L05Y", "FCW2140L06Z", "9080V0I41J3"]

- name: Generate YAML Configuration using explicit components list
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10", "192.168.1.11"]
        component_specific_filters:
          components_list: ["layer2_configurations"]

- name: Generate YAML Configuration with components list and specific features
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10"]
        component_specific_filters:
          components_list: ["layer2_configurations"]
          layer2_configurations:
            layer2_features: ["vlans", "stp", "cdp"]

- name: Generate YAML Configuration for specific VLANs
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10"]
        component_specific_filters:
          components_list: ["layer2_configurations"]
          layer2_configurations:
            layer2_features: ["vlans"]
            vlans:
              vlan_ids_list: ["10", "20", "100", "200"]

- name: Generate YAML Configuration for specific interfaces
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10"]
        component_specific_filters:
          components_list: ["layer2_configurations"]
          layer2_configurations:
            layer2_features: ["port_configuration"]
            port_configuration:
              interface_names_list:
                - "GigabitEthernet1/0/1"
                - "GigabitEthernet1/0/2"
                - "TenGigabitEthernet1/0/1"

- name: Generate YAML Configuration with comprehensive filtering
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10", "192.168.1.11"]
        component_specific_filters:
          components_list: ["layer2_configurations"]
          layer2_configurations:
            layer2_features: ["vlans", "stp", "port_configuration"]
            vlans:
              vlan_ids_list: ["10", "20", "100"]
            port_configuration:
              interface_names_list:
                - "GigabitEthernet1/0/1"
                - "GigabitEthernet1/0/24"

- name: Generate YAML Configuration for specific interfaces
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10"]
        component_specific_filters:
          layer2_features: ["port_configuration"]
          port_configuration:
            interface_names_list:
              - "GigabitEthernet1/0/1"
              - "GigabitEthernet1/0/2"
              - "TenGigabitEthernet1/0/1"

- name: Generate YAML Configuration with comprehensive filtering
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10", "192.168.1.11"]
        component_specific_filters:
          layer2_features: ["vlans", "stp", "port_configuration"]
          vlans:
            vlan_ids_list: ["10", "20", "100"]
          port_configuration:
            interface_names_list:
              - "GigabitEthernet1/0/1"
              - "GigabitEthernet1/0/24"

- name: Generate YAML Configuration for all features (no component filters)
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/wired_campus_automation_config.yml"
        global_filters:
          ip_address_list: ["192.168.1.10"]

- name: Generate YAML Configuration with default file path
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - global_filters:
          ip_address_list: ["192.168.1.10"]

- name: Generate YAML Configuration for protocol features
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/protocol_features_config.yml"
        global_filters:
          hostname_list: ["switch01.lab.com", "switch02.lab.com"]
        component_specific_filters:
          layer2_features: ["cdp", "lldp", "stp", "vtp"]

- name: Generate YAML Configuration for security features
  cisco.dnac.brownfield_wired_campus_automation_playbook_generator:
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
      - file_path: "/tmp/security_features_config.yml"
        global_filters:
          serial_number_list: ["FCW2140L05Y", "FCW2140L06Z"]
        component_specific_filters:
          layer2_features: ["dhcp_snooping", "igmp_snooping", "authentication"]
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
          "message": "YAML config generation succeeded for module 'wired_campus_automation_workflow_manager'.",
          "file_path": "/tmp/wired_campus_automation_config.yml",
          "configurations_generated": 25,
          "operation_summary": {
            "total_devices_processed": 3,
            "total_features_processed": 33,
            "total_successful_operations": 30,
            "total_failed_operations": 3,
            "devices_with_complete_success": ["192.168.1.10", "192.168.1.11"],
            "devices_with_partial_success": ["192.168.1.12"],
            "devices_with_complete_failure": [],
            "success_details": [
              {
                "device_ip": "192.168.1.10",
                "device_id": "12345678-1234-1234-1234-123456789abc",
                "feature": "vlans",
                "status": "success",
                "api_features_processed": ["vlanConfig"]
              }
            ],
            "failure_details": [
              {
                "device_ip": "192.168.1.12",
                "device_id": "12345678-1234-1234-1234-123456789def",
                "feature": "stp",
                "status": "failed",
                "error_info": {
                  "error_type": "api_error",
                  "error_message": "Feature not supported on this device",
                  "error_code": "FEATURE_NOT_SUPPORTED"
                }
              }
            ]
          }
        },
      "msg": "YAML config generation succeeded for module 'wired_campus_automation_workflow_manager'."
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
          "message": "No configurations or components to process for module 'wired_campus_automation_workflow_manager'. Verify input filters or configuration.",
          "operation_summary": {
            "total_devices_processed": 0,
            "total_features_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "devices_with_complete_success": [],
            "devices_with_partial_success": [],
            "devices_with_complete_failure": [],
            "success_details": [],
            "failure_details": []
          }
        },
      "msg": "No configurations or components to process for module 'wired_campus_automation_workflow_manager'. Verify input filters or configuration."
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
          "message": "YAML config generation failed for module 'wired_campus_automation_workflow_manager'.",
          "file_path": "/tmp/wired_campus_automation_config.yml",
          "operation_summary": {
            "total_devices_processed": 2,
            "total_features_processed": 20,
            "total_successful_operations": 10,
            "total_failed_operations": 10,
            "devices_with_complete_success": [],
            "devices_with_partial_success": ["192.168.1.10"],
            "devices_with_complete_failure": ["192.168.1.11"],
            "success_details": [],
            "failure_details": [
              {
                "device_ip": "192.168.1.11",
                "device_id": "12345678-1234-1234-1234-123456789ghi",
                "feature": "vlans",
                "status": "failed",
                "error_info": {
                  "error_type": "device_unreachable",
                  "error_message": "Device is not reachable or not managed",
                  "error_code": "DEVICE_UNREACHABLE"
                }
              }
            ]
          }
        },
      "msg": "YAML config generation failed for module 'wired_campus_automation_workflow_manager'."
    }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
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


class WiredCampusAutomationPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center using the GET APIs.
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
        self.module_name = "wired_campus_automation_workflow_manager"

        # Initialize class-level variables to track successes and failures
        self.operation_successes = []
        self.operation_failures = []
        self.total_devices_processed = 0
        self.total_features_processed = 0

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
            "generate_all_configurations": {
                "type": "bool",
                "required": False,
                "default": False,
            },
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        # Import validate_list_of_dicts function here to avoid circular imports
        from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
            validate_list_of_dicts,
        )

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
        Returns the mapping configuration for wired campus automation workflow manager.
        Returns:
            dict: A dictionary containing network elements and global filters configuration with validation rules.
        """
        return {
            "network_elements": {
                "layer2_configurations": {
                    "filters": {
                        "layer2_features": {
                            "type": "list",
                            "required": False,
                            "elements": "str",
                            "choices": [
                                "vlans",
                                "cdp",
                                "lldp",
                                "stp",
                                "vtp",
                                "dhcp_snooping",
                                "igmp_snooping",
                                "mld_snooping",
                                "authentication",
                                "logical_ports",
                                "port_configuration",
                            ],
                        },
                        "vlans": {
                            "type": "dict",
                            "required": False,
                            "options": {
                                "vlan_ids_list": {
                                    "type": "list",
                                    "required": False,
                                    "elements": "int",
                                    "range": [1, 4094],
                                }
                            },
                        },
                        "port_configuration": {
                            "type": "dict",
                            "required": False,
                            "options": {
                                "interface_names_list": {
                                    "type": "list",
                                    "required": False,
                                    "elements": "str",
                                }
                            },
                        },
                    },
                    "reverse_mapping_function": self.layer2_configurations_reverse_mapping_function,
                    "api_function": "get_configurations_for_a_deployed_layer2_feature_on_a_wired_device",
                    "api_family": "wired",
                    "get_function_name": self.get_layer2_configurations,
                },
                # "layer3_configurations": {
                # },
                # "security_configurations": {
                # },
            },
            "global_filters": {
                "ip_address_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                    "validate_ip": True,
                },
                "hostname_list": {"type": "list", "required": False, "elements": "str"},
                "serial_number_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                },
            },
        }

    def get_feature_reverse_mapping_spec(self, feature_name):
        """
        Returns reverse mapping specification for a specific feature or all features.
        This function is dynamic and works with filters to return only requested features.
        Args:
            feature_name (str or list): Name of specific feature(s) to get mapping for, or None for all
        Returns:
            dict: Reverse mapping specification for requested feature(s)
        """
        self.log(
            "Starting reverse mapping specification retrieval for feature_name: {0} (type: {1})".format(
                feature_name, type(feature_name).__name__
            ),
            "DEBUG",
        )

        self.log(
            "Creating comprehensive mapping dictionary with all supported layer2 features",
            "DEBUG",
        )
        all_mappings = {
            "vlans": self.vlans_reverse_mapping_spec(),
            "cdp": self.cdp_reverse_mapping_spec(),
            "lldp": self.lldp_reverse_mapping_spec(),
            "stp": self.stp_reverse_mapping_spec(),
            "vtp": self.vtp_reverse_mapping_spec(),
            "dhcp_snooping": self.dhcp_snooping_reverse_mapping_spec(),
            "igmp_snooping": self.igmp_snooping_reverse_mapping_spec(),
            "mld_snooping": self.mld_snooping_reverse_mapping_spec(),
            "authentication": self.authentication_reverse_mapping_spec(),
            "logical_ports": self.logical_ports_reverse_mapping_spec(),
            "port_configuration": self.port_configuration_reverse_mapping_spec(),
        }

        self.log(
            "Successfully created all_mappings dictionary with {0} feature types".format(
                len(all_mappings)
            ),
            "DEBUG",
        )

        if feature_name is None:
            self.log(
                "Feature name is None - returning all available mapping specifications",
                "DEBUG",
            )
            self.log(
                "Returning complete mapping specifications for all {0} features".format(
                    len(all_mappings)
                ),
                "INFO",
            )
            return all_mappings
        elif isinstance(feature_name, list):
            self.log(
                "Feature name is list with {0} elements: {1}".format(
                    len(feature_name), feature_name
                ),
                "DEBUG",
            )
            filtered_mappings = {
                feat: all_mappings[feat]
                for feat in feature_name
                if feat in all_mappings
            }
            self.log(
                "Filtered mappings created for {0} valid features out of {1} requested".format(
                    len(filtered_mappings), len(feature_name)
                ),
                "DEBUG",
            )
            return filtered_mappings
        elif isinstance(feature_name, str):
            self.log(
                "Feature name is string: '{0}' - retrieving single feature mapping".format(
                    feature_name
                ),
                "DEBUG",
            )
            single_mapping = {feature_name: all_mappings.get(feature_name, {})}
            if all_mappings.get(feature_name):
                self.log(
                    "Successfully retrieved mapping specification for feature '{0}'".format(
                        feature_name
                    ),
                    "DEBUG",
                )
            else:
                self.log(
                    "Feature '{0}' not found in available mappings - returning empty specification".format(
                        feature_name
                    ),
                    "WARNING",
                )
            return single_mapping
        else:
            self.log(
                "Invalid feature_name type: {0} - returning empty dictionary".format(
                    type(feature_name).__name__
                ),
                "WARNING",
            )
            return {}

    def layer2_configurations_reverse_mapping_function(self, requested_features=None):
        """
        Returns the reverse mapping specification for layer2 configurations.
        Supports dynamic filtering based on requested features.
        Args:
            requested_features (list, optional): List of specific features to include
        Returns:
            dict: A dictionary containing reverse mapping specifications for requested layer2 features
        """
        self.log(
            "Starting reverse mapping specification generation for layer2 configurations",
            "DEBUG",
        )
        self.log(
            "Requested features parameter: {0} (type: {1})".format(
                requested_features, type(requested_features).__name__
            ),
            "DEBUG",
        )

        if requested_features:
            self.log(
                "Specific features requested - delegating to get_feature_reverse_mapping_spec with feature list",
                "DEBUG",
            )
            self.log("Features to process: {0}".format(requested_features), "DEBUG")
            result = self.get_feature_reverse_mapping_spec(requested_features)
            self.log(
                "Successfully retrieved reverse mapping specification for {0} requested features".format(
                    len(requested_features)
                    if isinstance(requested_features, list)
                    else 1
                ),
                "INFO",
            )
            return result

        self.log(
            "No specific features requested - delegating to get_feature_reverse_mapping_spec for all features",
            "DEBUG",
        )
        result = self.get_feature_reverse_mapping_spec(None)
        self.log(
            "Successfully retrieved reverse mapping specification for all available features",
            "INFO",
        )
        return result

    def vlans_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for VLAN configurations.
        Compatible with modify_parameters function from brownfield_helper.
        Returns:
            OrderedDict: Reverse mapping specification for VLANs from API response to user format
        """
        self.log("Generating reverse mapping specification for VLANs.", "DEBUG")

        return OrderedDict(
            {
                "vlans": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "items",
                    "options": OrderedDict(
                        {
                            "vlan_id": {"type": "int", "source_key": "vlanId"},
                            "vlan_name": {"type": "str", "source_key": "name"},
                            "vlan_admin_status": {
                                "type": "bool",
                                "source_key": "isVlanEnabled",
                            },
                        }
                    ),
                }
            }
        )

    def cdp_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for CDP configurations.
        Returns:
            OrderedDict: Reverse mapping specification for CDP from API response to user format
        """
        self.log("Generating reverse mapping specification for CDP.", "DEBUG")

        return OrderedDict(
            {
                "cdp_admin_status": {"type": "bool", "source_key": "isCdpEnabled"},
                "cdp_hold_time": {"type": "int", "source_key": "holdTime"},
                "cdp_timer": {"type": "int", "source_key": "timer"},
                "cdp_advertise_v2": {
                    "type": "bool",
                    "source_key": "isAdvertiseV2Enabled",
                },
                "cdp_log_duplex_mismatch": {
                    "type": "bool",
                    "source_key": "isLogDuplexMismatchEnabled",
                },
            }
        )

    def lldp_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for LLDP configurations.
        Returns:
            OrderedDict: Reverse mapping specification for LLDP from API response to user format
        """
        self.log("Generating reverse mapping specification for LLDP.", "DEBUG")

        return OrderedDict(
            {
                "lldp_admin_status": {"type": "bool", "source_key": "isLldpEnabled"},
                "lldp_hold_time": {"type": "int", "source_key": "holdTime"},
                "lldp_timer": {"type": "int", "source_key": "timer"},
                "lldp_reinitialization_delay": {
                    "type": "int",
                    "source_key": "reinitializationDelay",
                },
            }
        )

    def stp_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for STP configurations.
        Returns:
            OrderedDict: Reverse mapping specification for STP from API response to user format
        """
        self.log("Generating reverse mapping specification for STP.", "DEBUG")

        return OrderedDict(
            {
                "stp_mode": {"type": "str", "source_key": "stpMode"},
                "stp_portfast_mode": {"type": "str", "source_key": "portFastMode"},
                "stp_bpdu_guard": {"type": "bool", "source_key": "isBpduGuardEnabled"},
                "stp_bpdu_filter": {
                    "type": "bool",
                    "source_key": "isBpduFilterEnabled",
                },
                "stp_backbonefast": {
                    "type": "bool",
                    "source_key": "isBackboneFastEnabled",
                },
                "stp_extended_system_id": {
                    "type": "bool",
                    "source_key": "isExtendedSystemIdEnabled",
                },
                "stp_logging": {"type": "bool", "source_key": "isLoggingEnabled"},
                "stp_loopguard": {"type": "bool", "source_key": "isLoopGuardEnabled"},
                "stp_transmit_hold_count": {
                    "type": "int",
                    "source_key": "transmitHoldCount",
                },
                "stp_uplinkfast": {"type": "bool", "source_key": "isUplinkFastEnabled"},
                "stp_uplinkfast_max_update_rate": {
                    "type": "int",
                    "source_key": "uplinkFastMaxUpdateRate",
                },
                "stp_etherchannel_guard": {
                    "type": "bool",
                    "source_key": "isEtherChannelGuardEnabled",
                },
                "stp_instances": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "stpInstances.items",
                    "options": OrderedDict(
                        {
                            "stp_instance_vlan_id": {
                                "type": "int",
                                "source_key": "vlanId",
                            },
                            "stp_instance_priority": {
                                "type": "int",
                                "source_key": "priority",
                            },
                            "enable_stp": {
                                "type": "bool",
                                "source_key": "isStpEnabled",
                            },
                            "stp_instance_max_age_timer": {
                                "type": "int",
                                "source_key": "timers.maxAge",
                            },
                            "stp_instance_hello_interval_timer": {
                                "type": "int",
                                "source_key": "timers.helloInterval",
                            },
                            "stp_instance_forward_delay_timer": {
                                "type": "int",
                                "source_key": "timers.forwardDelay",
                            },
                        }
                    ),
                },
            }
        )

    def vtp_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for VTP configurations.
        Returns:
            OrderedDict: Reverse mapping specification for VTP from API response to user format
        """
        self.log("Generating reverse mapping specification for VTP.", "DEBUG")

        return OrderedDict(
            {
                "vtp_mode": {"type": "str", "source_key": "mode"},
                "vtp_version": {"type": "str", "source_key": "version"},
                "vtp_domain_name": {"type": "str", "source_key": "domainName"},
                "vtp_configuration_file_name": {
                    "type": "str",
                    "source_key": "configurationFileName",
                },
                "vtp_source_interface": {
                    "type": "str",
                    "source_key": "sourceInterface",
                },
                "vtp_pruning": {"type": "bool", "source_key": "isPruningEnabled"},
            }
        )

    def dhcp_snooping_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for DHCP Snooping configurations.
        Returns:
            OrderedDict: Reverse mapping specification for DHCP Snooping from API response to user format
        """
        self.log("Generating reverse mapping specification for DHCP Snooping.", "DEBUG")

        return OrderedDict(
            {
                "dhcp_admin_status": {
                    "type": "bool",
                    "source_key": "isDhcpSnoopingEnabled",
                },
                "dhcp_snooping_vlans": {
                    "type": "list",
                    "elements": "int",
                    "source_key": "dhcpSnoopingVlans",
                    "transform": self.transform_vlan_string_to_list,
                },
                "dhcp_snooping_glean": {
                    "type": "bool",
                    "source_key": "isGleaningEnabled",
                },
                "dhcp_snooping_database_agent_url": {
                    "type": "str",
                    "source_key": "databaseAgent.agentUrl",
                },
                "dhcp_snooping_database_timeout": {
                    "type": "int",
                    "source_key": "databaseAgent.timeout",
                },
                "dhcp_snooping_database_write_delay": {
                    "type": "int",
                    "source_key": "databaseAgent.writeDelay",
                },
                "dhcp_snooping_proxy_bridge_vlans": {
                    "type": "list",
                    "elements": "int",
                    "source_key": "proxyBridgeVlans",
                    "transform": self.transform_vlan_string_to_list,
                },
            }
        )

    def igmp_snooping_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for IGMP Snooping configurations.
        Returns:
            OrderedDict: Reverse mapping specification for IGMP Snooping from API response to user format
        """
        self.log("Generating reverse mapping specification for IGMP Snooping.", "DEBUG")

        return OrderedDict(
            {
                "enable_igmp_snooping": {
                    "type": "bool",
                    "source_key": "isIgmpSnoopingEnabled",
                },
                "igmp_snooping_querier": {
                    "type": "bool",
                    "source_key": "isQuerierEnabled",
                },
                "igmp_snooping_querier_address": {
                    "type": "str",
                    "source_key": "querierAddress",
                },
                "igmp_snooping_querier_version": {
                    "type": "str",
                    "source_key": "querierVersion",
                },
                "igmp_snooping_querier_query_interval": {
                    "type": "int",
                    "source_key": "querierQueryInterval",
                },
                "igmp_snooping_vlans": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "igmpSnoopingVlanSettings.items",
                    "options": OrderedDict(
                        {
                            "igmp_snooping_vlan_id": {
                                "type": "int",
                                "source_key": "vlanId",
                            },
                            "enable_igmp_snooping": {
                                "type": "bool",
                                "source_key": "isIgmpSnoopingEnabled",
                            },
                            "igmp_snooping_immediate_leave": {
                                "type": "bool",
                                "source_key": "isImmediateLeaveEnabled",
                            },
                            "igmp_snooping_querier": {
                                "type": "bool",
                                "source_key": "isQuerierEnabled",
                            },
                            "igmp_snooping_querier_address": {
                                "type": "str",
                                "source_key": "querierAddress",
                            },
                            "igmp_snooping_querier_version": {
                                "type": "str",
                                "source_key": "querierVersion",
                            },
                            "igmp_snooping_querier_query_interval": {
                                "type": "int",
                                "source_key": "querierQueryInterval",
                            },
                            "igmp_snooping_mrouter_port_list": {
                                "type": "list",
                                "elements": "str",
                                "special_handling": True,
                                "source_key": "igmpSnoopingVlanMrouters.items",
                                "transform": lambda vlan_detail: self.extract_interface_names(
                                    vlan_detail.get("igmpSnoopingVlanMrouters", {}).get(
                                        "items", []
                                    )
                                ),
                            },
                        }
                    ),
                },
            }
        )

    def mld_snooping_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for MLD Snooping configurations.
        Returns:
            OrderedDict: Reverse mapping specification for MLD Snooping from API response to user format
        """
        self.log("Generating reverse mapping specification for MLD Snooping.", "DEBUG")

        return OrderedDict(
            {
                "enable_mld_snooping": {
                    "type": "bool",
                    "source_key": "isMldSnoopingEnabled",
                },
                "mld_snooping_querier": {
                    "type": "bool",
                    "source_key": "isQuerierEnabled",
                },
                "mld_snooping_querier_address": {
                    "type": "str",
                    "source_key": "querierAddress",
                },
                "mld_snooping_querier_version": {
                    "type": "str",
                    "source_key": "querierVersion",
                },
                "mld_snooping_listener": {
                    "type": "bool",
                    "source_key": "isSuppressListenerMessagesEnabled",
                },
                "mld_snooping_querier_query_interval": {
                    "type": "int",
                    "source_key": "querierQueryInterval",
                },
                "mld_snooping_vlans": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "mldSnoopingVlanSettings.items",
                    "options": OrderedDict(
                        {
                            "mld_snooping_vlan_id": {
                                "type": "int",
                                "source_key": "vlanId",
                            },
                            "enable_mld_snooping": {
                                "type": "bool",
                                "source_key": "isMldSnoopingEnabled",
                            },
                            "mld_snooping_enable_immediate_leave": {
                                "type": "bool",
                                "source_key": "isImmediateLeaveEnabled",
                            },
                            "mld_snooping_querier": {
                                "type": "bool",
                                "source_key": "isQuerierEnabled",
                            },
                            "mld_snooping_querier_address": {
                                "type": "str",
                                "source_key": "querierAddress",
                            },
                            "mld_snooping_querier_version": {
                                "type": "str",
                                "source_key": "querierVersion",
                            },
                            "mld_snooping_querier_query_interval": {
                                "type": "int",
                                "source_key": "querierQueryInterval",
                            },
                            "mld_snooping_mrouter_port_list": {
                                "type": "list",
                                "elements": "str",
                                "source_key": "mldSnoopingVlanMrouters.items",
                                "special_handling": True,
                                "transform": lambda vlan_detail: self.extract_interface_names(
                                    vlan_detail.get("mldSnoopingVlanMrouters", {}).get(
                                        "items", []
                                    )
                                ),
                            },
                        }
                    ),
                },
            }
        )

    def extract_interface_names(self, mrouter_items):
        """
        Simple function to extract interface names from mrouter items.
        Args:
            mrouter_items (list): List of mrouter items from API response
        Returns:
            list: List of interface names
        """
        self.log("Starting interface name extraction from mrouter items", "DEBUG")
        self.log(
            "Input mrouter_items type: {0}, value: {1}".format(
                type(mrouter_items).__name__, mrouter_items
            ),
            "DEBUG",
        )

        # Early validation - check if input is empty or not a list
        if not mrouter_items or not isinstance(mrouter_items, list):
            self.log(
                "Mrouter items is empty or not a list - returning empty list", "DEBUG"
            )
            return []

        self.log(
            "Processing {0} mrouter items for interface name extraction".format(
                len(mrouter_items)
            ),
            "DEBUG",
        )

        # Initialize list to collect extracted interface names
        interface_names = []

        # Process each mrouter item to extract interface name
        for item_index, item in enumerate(mrouter_items):
            self.log(
                "Processing mrouter item {0} of {1}: {2}".format(
                    item_index + 1, len(mrouter_items), item
                ),
                "DEBUG",
            )

            # Validate item structure and extract interface name if valid
            if isinstance(item, dict) and "interfaceName" in item:
                interface_name = item["interfaceName"]
                interface_names.append(interface_name)
                self.log(
                    "Successfully extracted interface name: '{0}' from item {1}".format(
                        interface_name, item_index + 1
                    ),
                    "DEBUG",
                )
            else:
                self.log(
                    "Skipping invalid mrouter item {0} - not dict or missing interfaceName: {1}".format(
                        item_index + 1, item
                    ),
                    "DEBUG",
                )

        self.log("Interface name extraction completed successfully", "DEBUG")
        self.log(
            "Total interface names extracted: {0}".format(len(interface_names)), "INFO"
        )
        self.log("Extracted interface names list: {0}".format(interface_names), "DEBUG")

        return interface_names

    def authentication_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for Authentication configurations.
        Returns:
            OrderedDict: Reverse mapping specification for Authentication from API response to user format
        """
        self.log(
            "Generating reverse mapping specification for Authentication.", "DEBUG"
        )

        return OrderedDict(
            {
                "enable_dot1x_authentication": {
                    "type": "bool",
                    "source_key": "isDot1xEnabled",
                },
                "authentication_config_mode": {
                    "type": "str",
                    "source_key": "authenticationConfigMode",
                },
            }
        )

    def logical_ports_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for Logical Ports (Port Channel) configurations.
        Returns:
            OrderedDict: Reverse mapping specification for Logical Ports from API response to user format
        """
        self.log("Generating reverse mapping specification for Logical Ports.", "DEBUG")

        return OrderedDict(
            {
                "port_channel_auto": {"type": "bool", "source_key": "isAutoEnabled"},
                "port_channel_lacp_system_priority": {
                    "type": "int",
                    "source_key": "lacpSystemPriority",
                },
                "port_channel_load_balancing_method": {
                    "type": "str",
                    "source_key": "loadBalancingMethod",
                },
                "port_channels": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "portchannels.items",
                    "options": OrderedDict(
                        {
                            "port_channel_protocol": {
                                "type": "str",
                                "source_key": "configType",
                                "transform": self.transform_port_channel_protocol,
                            },
                            "port_channel_name": {"type": "str", "source_key": "name"},
                            "port_channel_min_links": {
                                "type": "int",
                                "source_key": "minLinks",
                            },
                            "port_channel_members": {
                                "type": "list",
                                "elements": "dict",
                                "source_key": "memberPorts.items",
                                "special_handling": True,
                                "transform": self.transform_port_channel_members,
                            },
                        }
                    ),
                },
            }
        )

    def transform_port_channel_protocol(self, config_type):
        """
        Transforms the configType to the expected protocol format.
        Args:
            config_type (str): The configType from API response
        Returns:
            str: The transformed protocol name
        """
        self.log(
            "Starting port channel protocol transformation for config_type: '{0}' (type: {1})".format(
                config_type, type(config_type).__name__
            ),
            "DEBUG",
        )

        # Define mapping dictionary for config type to protocol transformation
        protocol_mapping = {
            "ETHERCHANNEL_CONFIG": "NONE",
            "LACP_PORTCHANNEL_CONFIG": "LACP",
            "PAGP_PORTCHANNEL_CONFIG": "PAGP",
        }

        self.log(
            "Protocol mapping dictionary configured with {0} transformation rules".format(
                len(protocol_mapping)
            ),
            "DEBUG",
        )
        self.log(
            "Available config_type mappings: {0}".format(list(protocol_mapping.keys())),
            "DEBUG",
        )

        # Perform the transformation using mapping dictionary with fallback
        if config_type in protocol_mapping:
            transformed_protocol = protocol_mapping[config_type]
            self.log(
                "Successfully transformed config_type '{0}' to protocol '{1}'".format(
                    config_type, transformed_protocol
                ),
                "DEBUG",
            )
        else:
            self.log(
                "Config_type '{0}' not found in mapping dictionary - using original value as fallback".format(
                    config_type
                ),
                "DEBUG",
            )
            transformed_protocol = config_type

        self.log(
            "Port channel protocol transformation completed - returning: '{0}'".format(
                transformed_protocol
            ),
            "DEBUG",
        )

        return transformed_protocol

    def transform_port_channel_members(self, port_channel_detail):
        """
        Transforms port channel member configurations based on the protocol type.
        Args:
            port_channel_detail (dict): The full port channel configuration
        Returns:
            list: List of transformed member port configurations
        """
        self.log("Starting port channel member transformation process", "DEBUG")
        self.log("Input port_channel_detail: {0}".format(port_channel_detail), "DEBUG")

        members = port_channel_detail.get("memberPorts", {}).get("items", [])
        config_type = port_channel_detail.get("configType")

        self.log(
            "Extracted {0} member ports with config type: {1}".format(
                len(members), config_type
            ),
            "DEBUG",
        )

        if not members:
            self.log("No member ports found - returning empty list", "DEBUG")
            return []

        transformed_members = []

        for member in members:
            self.log(
                "Processing member: {0}".format(member.get("interfaceName")), "DEBUG"
            )

            base_config = {
                "port_channel_interface_name": member.get("interfaceName"),
                "port_channel_port_priority": member.get("portPriority"),
            }

            # Add protocol-specific fields
            if config_type == "LACP_PORTCHANNEL_CONFIG":
                self.log(
                    "Adding LACP-specific fields for interface {0}".format(
                        member.get("interfaceName")
                    ),
                    "DEBUG",
                )
                base_config.update(
                    {
                        "port_channel_mode": member.get("mode"),
                        "port_channel_rate": member.get("rate"),
                    }
                )
            elif config_type == "PAGP_PORTCHANNEL_CONFIG":
                self.log(
                    "Adding PAGP-specific fields for interface {0}".format(
                        member.get("interfaceName")
                    ),
                    "DEBUG",
                )
                base_config.update(
                    {
                        "port_channel_mode": member.get("mode"),
                        "port_channel_learn_method": member.get("learnMethod"),
                    }
                )
            # ETHERCHANNEL_CONFIG (STATIC) doesn't have additional protocol-specific fields

            # Remove None values
            cleaned_config = {k: v for k, v in base_config.items() if v is not None}
            transformed_members.append(cleaned_config)

            self.log(
                "Transformed member {0} - removed {1} None values".format(
                    member.get("interfaceName"), len(base_config) - len(cleaned_config)
                ),
                "DEBUG",
            )

        self.log(
            "Port channel member transformation completed - processed {0} members".format(
                len(transformed_members)
            ),
            "INFO",
        )

        return transformed_members

    def port_configuration_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for Port Configuration from API response to user format.
        Returns:
            OrderedDict: Reverse mapping specification for Port Configuration containing all interface feature mappings
        """
        self.log(
            "Starting generation of reverse mapping specification for Port Configuration",
            "DEBUG",
        )

        # Build mapping spec using individual spec functions for better modularity
        mapping_spec = OrderedDict(
            {
                "switchport_interface_config": self._get_switchport_interface_spec(),
                "vlan_trunking_interface_config": self._get_vlan_trunking_interface_spec(),
                "cdp_interface_config": self._get_cdp_interface_spec(),
                "lldp_interface_config": self._get_lldp_interface_spec(),
                "stp_interface_config": self._get_stp_interface_spec(),
                "dhcp_snooping_interface_config": self._get_dhcp_snooping_interface_spec(),
                "dot1x_interface_config": self._get_dot1x_interface_spec(),
                "mab_interface_config": self._get_mab_interface_spec(),
                "vtp_interface_config": self._get_vtp_interface_spec(),
            }
        )

        self.log(
            "Port Configuration mapping specification created with {0} interface types".format(
                len(mapping_spec)
            ),
            "INFO",
        )

        return mapping_spec

    def _get_switchport_interface_spec(self):
        """
        Returns the reverse mapping specification for switchport interface configuration.
        Returns:
            dict: Switchport interface configuration mapping specification
        """
        self.log("Generating switchport interface configuration specification", "DEBUG")

        return {
            "type": "dict",
            "options": OrderedDict(
                {
                    "switchport_description": {
                        "type": "str",
                        "source_key": "description",
                    },
                    "switchport_mode": {"type": "str", "source_key": "mode"},
                    "access_vlan": {"type": "int", "source_key": "accessVlan"},
                    "voice_vlan": {"type": "int", "source_key": "voiceVlan"},
                    "admin_status": {"type": "str", "source_key": "adminStatus"},
                    "allowed_vlans": {
                        "type": "list",
                        "elements": "int",
                        "source_key": "trunkAllowedVlans",
                        "transform": self.transform_vlan_string_to_list,
                    },
                    "native_vlan_id": {"type": "int", "source_key": "nativeVlan"},
                }
            ),
        }

    def _get_vlan_trunking_interface_spec(self):
        """
        Returns the reverse mapping specification for VLAN trunking interface configuration.
        Returns:
            dict: VLAN trunking interface configuration mapping specification
        """
        self.log(
            "Generating VLAN trunking interface configuration specification", "DEBUG"
        )

        return {
            "type": "dict",
            "options": OrderedDict(
                {
                    "is_protected": {"type": "bool", "source_key": "isProtected"},
                    "is_dtp_negotiation_enabled": {
                        "type": "bool",
                        "source_key": "isDtpNegotiationEnabled",
                    },
                    "prune_eligible_vlans": {
                        "type": "list",
                        "elements": "int",
                        "source_key": "pruneEligibleVlans",
                        "transform": self.transform_vlan_string_to_list,
                    },
                }
            ),
        }

    def _get_cdp_interface_spec(self):
        """
        Returns the reverse mapping specification for CDP interface configuration.
        Returns:
            dict: CDP interface configuration mapping specification
        """
        self.log("Generating CDP interface configuration specification", "DEBUG")

        return {
            "type": "dict",
            "options": OrderedDict(
                {
                    "is_cdp_enabled": {"type": "bool", "source_key": "isCdpEnabled"},
                    "is_log_duplex_mismatch_enabled": {
                        "type": "bool",
                        "source_key": "isLogDuplexMismatchEnabled",
                    },
                }
            ),
        }

    def _get_lldp_interface_spec(self):
        """
        Returns the reverse mapping specification for LLDP interface configuration.
        Returns:
            dict: LLDP interface configuration mapping specification
        """
        self.log("Generating LLDP interface configuration specification", "DEBUG")

        return {
            "type": "dict",
            "options": OrderedDict(
                {"admin_status": {"type": "str", "source_key": "adminStatus"}}
            ),
        }

    def _get_stp_interface_spec(self):
        """
        Returns the reverse mapping specification for STP interface configuration.
        Returns:
            dict: STP interface configuration mapping specification
        """
        self.log("Generating STP interface configuration specification", "DEBUG")

        return {
            "type": "dict",
            "options": OrderedDict(
                {
                    "guard_mode": {"type": "str", "source_key": "guardMode"},
                    "bpdu_filter": {"type": "str", "source_key": "bpduFilter"},
                    "bpdu_guard": {"type": "str", "source_key": "bpduGuard"},
                    "path_cost": {"type": "int", "source_key": "pathCost"},
                    "portfast_mode": {"type": "str", "source_key": "portFastMode"},
                    "priority": {"type": "int", "source_key": "priority"},
                    "port_vlan_cost_settings": {
                        "type": "list",
                        "elements": "dict",
                        "source_key": "portVlanCostSettings.items",
                        "options": OrderedDict(
                            {
                                "cost": {"type": "int", "source_key": "cost"},
                                "vlans": {
                                    "type": "list",
                                    "elements": "int",
                                    "source_key": "vlans",
                                },
                            }
                        ),
                    },
                    "port_vlan_priority_settings": {
                        "type": "list",
                        "elements": "dict",
                        "source_key": "portVlanPrioritySettings.items",
                        "options": OrderedDict(
                            {
                                "priority": {"type": "int", "source_key": "priority"},
                                "vlans": {
                                    "type": "list",
                                    "elements": "int",
                                    "source_key": "vlans",
                                },
                            }
                        ),
                    },
                }
            ),
        }

    def _get_dhcp_snooping_interface_spec(self):
        """
        Returns the reverse mapping specification for DHCP snooping interface configuration.
        Returns:
            dict: DHCP snooping interface configuration mapping specification
        """
        self.log(
            "Generating DHCP snooping interface configuration specification", "DEBUG"
        )

        return {
            "type": "dict",
            "options": OrderedDict(
                {
                    "is_trusted_interface": {
                        "type": "bool",
                        "source_key": "isTrustedInterface",
                    },
                    "message_rate_limit": {
                        "type": "int",
                        "source_key": "messageRateLimit",
                    },
                }
            ),
        }

    def _get_dot1x_interface_spec(self):
        """
        Returns the reverse mapping specification for 802.1X interface configuration.
        Returns:
            dict: 802.1X interface configuration mapping specification
        """
        self.log("Generating 802.1X interface configuration specification", "DEBUG")

        return {
            "type": "dict",
            "options": OrderedDict(
                {
                    "authentication_order": {
                        "type": "list",
                        "elements": "str",
                        "source_key": "authenticationOrder.items",
                    },
                    "priority": {
                        "type": "list",
                        "elements": "str",
                        "source_key": "priority.items",
                    },
                    "control_direction": {
                        "type": "str",
                        "source_key": "controlDirection",
                    },
                    "host_mode": {"type": "str", "source_key": "hostMode"},
                    "inactivity_timer": {
                        "type": "int",
                        "source_key": "inactivityTimer",
                    },
                    "authentication_mode": {
                        "type": "str",
                        "source_key": "authenticationMode",
                    },
                    "is_reauth_enabled": {
                        "type": "bool",
                        "source_key": "isReauthEnabled",
                    },
                    "max_reauth_requests": {
                        "type": "int",
                        "source_key": "maxReauthRequests",
                    },
                    "is_inactivity_timer_from_server_enabled": {
                        "type": "bool",
                        "source_key": "isInactivityTimerFromServerEnabled",
                    },
                    "is_reauth_timer_from_server_enabled": {
                        "type": "bool",
                        "source_key": "isReauthTimerFromServerEnabled",
                    },
                    "pae_type": {"type": "str", "source_key": "paeType"},
                    "port_control": {"type": "str", "source_key": "portControl"},
                    "reauth_timer": {"type": "int", "source_key": "reauthTimer"},
                    "tx_period": {"type": "int", "source_key": "txPeriod"},
                }
            ),
        }

    def _get_mab_interface_spec(self):
        """
        Returns the reverse mapping specification for MAB interface configuration.
        Returns:
            dict: MAB interface configuration mapping specification
        """
        self.log("Generating MAB interface configuration specification", "DEBUG")

        return {
            "type": "dict",
            "options": OrderedDict(
                {"is_mab_enabled": {"type": "bool", "source_key": "isMabEnabled"}}
            ),
        }

    def _get_vtp_interface_spec(self):
        """
        Returns the reverse mapping specification for VTP interface configuration.
        Returns:
            dict: VTP interface configuration mapping specification
        """
        self.log("Generating VTP interface configuration specification", "DEBUG")

        return {
            "type": "dict",
            "options": OrderedDict(
                {"is_vtp_enabled": {"type": "bool", "source_key": "isVtpEnabled"}}
            ),
        }

    def transform_vlan_string_to_list(self, vlan_string):
        """
        Transforms a VLAN string representation into a list of integer VLAN IDs.
        Handles various formats including ranges, comma-separated values, and special cases like 'ALL'.
        """
        self.log(
            "Transforming VLAN string: '{0}' (type: {1})".format(
                vlan_string, type(vlan_string).__name__
            ),
            "DEBUG",
        )

        # Handle None, empty, or not configured values
        if not vlan_string or str(vlan_string).upper() in ["NOT CONFIGURED", "NONE"]:
            self.log(
                "VLAN string empty or not configured - returning empty list", "DEBUG"
            )
            return []

        # Handle the special case "ALL" - return as string to preserve semantic meaning
        vlan_string_upper = str(vlan_string).upper()
        if vlan_string_upper == "ALL":
            self.log("VLAN string is 'ALL' - preserving special meaning", "DEBUG")
            return "ALL"

        # Handle unexpected dictionary input
        if isinstance(vlan_string, dict):
            self.log(
                "Received dictionary for VLAN transformation - returning empty list",
                "WARNING",
            )
            return []

        # Parse VLAN string into individual VLAN IDs
        self.log("Parsing VLAN string for individual IDs", "DEBUG")
        parsed_vlans = self._parse_vlan_string(str(vlan_string).strip())

        # Process and return final result
        if parsed_vlans:
            unique_vlans = sorted(list(set(parsed_vlans)))
            self.log(
                "VLAN transformation completed - {0} unique VLANs parsed".format(
                    len(unique_vlans)
                ),
                "INFO",
            )
            return unique_vlans
        else:
            self.log("VLAN transformation resulted in empty list", "DEBUG")
            return []

    def _parse_vlan_string(self, vlan_string_clean):
        """
        Parses a clean VLAN string into individual VLAN IDs.
        Args:
            vlan_string_clean (str): Cleaned VLAN string to parse.
        Returns:
            list: List of parsed VLAN IDs as integers.
        """
        self.log("Parsing VLAN string: '{0}'".format(vlan_string_clean), "DEBUG")

        vlans = []

        try:
            # Split by comma to handle comma-separated values
            vlan_parts = vlan_string_clean.split(",")
            self.log(
                "Split VLAN string into {0} parts".format(len(vlan_parts)), "DEBUG"
            )

            for part_index, part in enumerate(vlan_parts):
                part = part.strip()

                if not part:
                    self.log("Skipping empty part {0}".format(part_index), "DEBUG")
                    continue

                # Handle range notation (e.g., "3-5")
                if "-" in part:
                    self.log("Processing VLAN range: '{0}'".format(part), "DEBUG")
                    range_vlans = self._parse_vlan_range(part)
                    if range_vlans:
                        vlans.extend(range_vlans)
                else:
                    # Handle single VLAN ID
                    single_vlan = self._parse_single_vlan(part)
                    if single_vlan is not None:
                        vlans.append(single_vlan)

        except Exception as e:
            self.log(
                "Error during VLAN string parsing '{0}': {1}".format(
                    vlan_string_clean, str(e)
                ),
                "ERROR",
            )
            return []

        self.log(
            "VLAN parsing completed - parsed {0} VLANs".format(len(vlans)), "DEBUG"
        )
        return vlans

    def _parse_vlan_range(self, range_part):
        """
        Parses a VLAN range string (e.g., "3-5") into a list of VLAN IDs.
        Args:
            range_part (str): VLAN range string to parse.
        Returns:
            list: List of VLAN IDs in the range, or empty list if invalid.
        """
        self.log("Parsing VLAN range: '{0}'".format(range_part), "DEBUG")

        try:
            range_parts = range_part.split("-")
            if len(range_parts) == 2:
                start, end = map(int, range_parts)

                if start <= end:
                    range_vlans = list(range(start, end + 1))
                    self.log(
                        "Generated VLAN range {0}-{1}: {2} VLANs".format(
                            start, end, len(range_vlans)
                        ),
                        "DEBUG",
                    )
                    return range_vlans
                else:
                    self.log(
                        "Invalid range '{0}' - start > end".format(range_part),
                        "WARNING",
                    )
            else:
                self.log(
                    "Invalid range format '{0}' - expected one hyphen".format(
                        range_part
                    ),
                    "WARNING",
                )

        except ValueError as e:
            self.log(
                "Error parsing range '{0}': {1}".format(range_part, str(e)), "WARNING"
            )

        return []

    def _parse_single_vlan(self, vlan_part):
        """
        Parses a single VLAN ID string into an integer.
        Args:
            vlan_part (str): Single VLAN ID string to parse.
        Returns:
            int: Parsed VLAN ID, or None if invalid.
        """
        self.log("Parsing single VLAN: '{0}'".format(vlan_part), "DEBUG")
        try:
            single_vlan = int(vlan_part)
            self.log("Successfully parsed VLAN: {0}".format(single_vlan), "DEBUG")
            return single_vlan
        except ValueError as e:
            self.log(
                "Error parsing single VLAN '{0}': {1}".format(vlan_part, str(e)),
                "WARNING",
            )
            return None

    def reset_operation_tracking(self):
        """
        Resets the operation tracking variables for a new operation.
        """
        self.log("Resetting operation tracking variables for new operation", "DEBUG")
        self.operation_successes = []
        self.operation_failures = []
        self.total_devices_processed = 0
        self.total_features_processed = 0
        self.log("Operation tracking variables reset successfully", "DEBUG")

    def add_success(self, device_ip, device_id, feature, additional_info=None):
        """
        Adds a successful operation to the tracking list.
        Args:
            device_ip (str): Device IP address.
            device_id (str): Device ID.
            feature (str): Feature name that succeeded.
            additional_info (dict): Additional information about the success.
        """
        self.log(
            "Creating success entry for device {0}, feature {1}".format(
                device_ip, feature
            ),
            "DEBUG",
        )
        success_entry = {
            "device_ip": device_ip,
            "device_id": device_id,
            "feature": feature,
            "status": "success",
        }

        if additional_info:
            self.log(
                "Adding additional information to success entry: {0}".format(
                    additional_info
                ),
                "DEBUG",
            )
            success_entry.update(additional_info)

        self.operation_successes.append(success_entry)
        self.log(
            "Successfully added success entry for device {0}, feature {1}. Total successes: {2}".format(
                device_ip, feature, len(self.operation_successes)
            ),
            "DEBUG",
        )

    def add_failure(self, device_ip, device_id, feature, error_info, api_feature=None):
        """
        Adds a failed operation to the tracking list.
        Args:
            device_ip (str): Device IP address.
            device_id (str): Device ID.
            feature (str): Feature name that failed.
            error_info (dict): Error information containing error details.
            api_feature (str): Specific API feature that failed.
        """
        self.log(
            "Creating failure entry for device {0}, feature {1}".format(
                device_ip, feature
            ),
            "DEBUG",
        )
        failure_entry = {
            "device_ip": device_ip,
            "device_id": device_id,
            "feature": feature,
            "status": "failed",
            "error_info": error_info,
        }

        if api_feature:
            self.log(
                "Adding API feature information to failure entry: {0}".format(
                    api_feature
                ),
                "DEBUG",
            )
            failure_entry["api_feature"] = api_feature

        self.operation_failures.append(failure_entry)
        self.log(
            "Successfully added failure entry for device {0}, feature {1}: {2}. Total failures: {3}".format(
                device_ip,
                feature,
                error_info.get("error_message", "Unknown error"),
                len(self.operation_failures),
            ),
            "ERROR",
        )

    def get_operation_summary(self):
        """
        Returns a summary of all operations performed.
        Returns:
            dict: Summary containing successes, failures, and statistics.
        """
        self.log(
            "Generating operation summary from {0} successes and {1} failures".format(
                len(self.operation_successes), len(self.operation_failures)
            ),
            "DEBUG",
        )

        unique_successful_devices = set()
        unique_failed_devices = set()

        self.log(
            "Processing successful operations to extract unique device information",
            "DEBUG",
        )
        for success in self.operation_successes:
            unique_successful_devices.add(success["device_ip"])

        self.log(
            "Processing failed operations to extract unique device information", "DEBUG"
        )
        for failure in self.operation_failures:
            unique_failed_devices.add(failure["device_ip"])

        self.log(
            "Calculating device categorization based on success and failure patterns",
            "DEBUG",
        )
        partial_success_devices = unique_successful_devices.intersection(
            unique_failed_devices
        )
        self.log(
            "Devices with partial success (both successes and failures): {0}".format(
                len(partial_success_devices)
            ),
            "DEBUG",
        )

        complete_success_devices = unique_successful_devices - unique_failed_devices
        self.log(
            "Devices with complete success (only successes): {0}".format(
                len(complete_success_devices)
            ),
            "DEBUG",
        )

        complete_failure_devices = unique_failed_devices - unique_successful_devices
        self.log(
            "Devices with complete failure (only failures): {0}".format(
                len(complete_failure_devices)
            ),
            "DEBUG",
        )

        summary = {
            "total_devices_processed": len(
                unique_successful_devices.union(unique_failed_devices)
            ),
            "total_features_processed": self.total_features_processed,
            "total_successful_operations": len(self.operation_successes),
            "total_failed_operations": len(self.operation_failures),
            "devices_with_complete_success": list(complete_success_devices),
            "devices_with_partial_success": list(partial_success_devices),
            "devices_with_complete_failure": list(complete_failure_devices),
            "success_details": self.operation_successes,
            "failure_details": self.operation_failures,
        }

        self.log(
            "Operation summary generated successfully with {0} total devices processed".format(
                summary["total_devices_processed"]
            ),
            "INFO",
        )

        return summary

    def get_layer2_configurations(self, network_element, filters):
        """
        Retrieves layer2 configurations from Cisco Catalyst Center based on network element and filters.
        Args:
            network_element (dict): Network element configuration containing API details and reverse mapping function.
            filters (dict): Filters containing global_filters and component_specific_filters.
        Returns:
            dict: A dictionary containing layer2 configurations organized by feature type.
        """
        self.log(
            "Starting comprehensive layer2 configurations retrieval process", "INFO"
        )
        self.log("Network element configuration: {0}".format(network_element), "DEBUG")
        self.log("Applied filters: {0}".format(filters), "DEBUG")

        self.log("Resetting operation tracking for new retrieval session", "DEBUG")
        self.reset_operation_tracking()

        self.log("Processing global filters to obtain device IP to ID mapping", "DEBUG")

        # Check if this is generate_all_configurations mode using class parameter
        global_filters = filters.get("global_filters", {})

        if self.generate_all_configurations:
            self.log(
                "Generate all configurations mode detected - retrieving all managed devices",
                "INFO",
            )
            # Get all devices without any parameters to retrieve everything
            device_ip_to_id_mapping = self.get_network_device_details()
            selected_filter_type = (
                "ip_addresses"  # Default to IP addresses for output format
            )

            processed_global_filters = {
                "device_ip_to_id_mapping": device_ip_to_id_mapping,
                "applied_filters": {"selected_filter_type": selected_filter_type},
            }
        else:
            processed_global_filters = self.process_global_filters(global_filters)
            device_ip_to_id_mapping = processed_global_filters.get(
                "device_ip_to_id_mapping", {}
            )
            selected_filter_type = processed_global_filters.get(
                "applied_filters", {}
            ).get("selected_filter_type")

            # NEW: If no device filters provided, get all devices
            if not device_ip_to_id_mapping and not any(
                [
                    global_filters.get("ip_address_list"),
                    global_filters.get("hostname_list"),
                    global_filters.get("serial_number_list"),
                ]
            ):
                self.log(
                    "No device filters provided - retrieving all managed devices",
                    "INFO",
                )
                device_ip_to_id_mapping = self.get_network_device_details()
                selected_filter_type = (
                    "ip_addresses"  # Default to IP addresses for output format
                )

                # Update processed_global_filters
                processed_global_filters = {
                    "device_ip_to_id_mapping": device_ip_to_id_mapping,
                    "applied_filters": {"selected_filter_type": selected_filter_type},
                }

        if not device_ip_to_id_mapping:
            self.log(
                "No devices found from global filters. Terminating configuration retrieval.",
                "WARNING",
            )
            return {
                "layer2_configurations": [],
                "operation_summary": self.get_operation_summary(),
            }

        self.log(
            "Found {0} devices to process from global filters".format(
                len(device_ip_to_id_mapping)
            ),
            "INFO",
        )
        self.total_devices_processed = len(device_ip_to_id_mapping)

        self.log("Extracting component-specific filters for layer2 features", "DEBUG")
        component_specific_filters = filters.get("component_specific_filters", {})
        self.log(
            "Component specific filters: {0}".format(component_specific_filters),
            "DEBUG",
        )
        layer2_config_filters = component_specific_filters.get(
            "layer2_configurations", {}
        )
        self.log(
            "Layer2 configuration filters: {0}".format(layer2_config_filters), "DEBUG"
        )
        layer2_features = layer2_config_filters.get("layer2_features", [])
        self.log("Requested layer2 features: {0}".format(layer2_features), "DEBUG")

        self.log("Checking if specific layer2 features were requested", "DEBUG")
        if not layer2_features:
            self.log(
                "No specific features requested, retrieving all supported features from module schema",
                "DEBUG",
            )
            layer2_config_filters = (
                self.module_schema.get("network_elements", {})
                .get("layer2_configurations", {})
                .get("filters", {})
            )
            layer2_features = layer2_config_filters["layer2_features"].get(
                "choices", []
            )

        self.log("Processing layer2 features: {0}".format(layer2_features), "DEBUG")

        self.log("Initializing feature to API mapping configuration", "DEBUG")
        feature_to_api_mapping = {
            "vlans": "vlanConfig",
            "cdp": "cdpGlobalConfig",
            "lldp": "lldpGlobalConfig",
            "stp": "stpGlobalConfig",
            "vtp": "vtpGlobalConfig",
            "dhcp_snooping": "dhcpSnoopingGlobalConfig",
            "igmp_snooping": "igmpSnoopingGlobalConfig",
            "mld_snooping": "mldSnoopingGlobalConfig",
            "authentication": "dot1xGlobalConfig",
            "logical_ports": "portchannelConfig",
            "port_configuration": [
                "switchportInterfaceConfig",
                "trunkInterfaceConfig",
                "cdpInterfaceConfig",
                "lldpInterfaceConfig",
                "stpInterfaceConfig",
                "dhcpSnoopingInterfaceConfig",
                "dot1xInterfaceConfig",
                "mabInterfaceConfig",
                "vtpInterfaceConfig",
            ],
        }
        self.log(
            "Feature to API mapping configured with {0} feature mappings".format(
                len(feature_to_api_mapping)
            ),
            "DEBUG",
        )

        self.log("Initializing configuration collection for all devices", "DEBUG")
        device_configurations = {}

        for device_ip, device_info in device_ip_to_id_mapping.items():
            self.log(
                "Processing device {0} (ID: {1})".format(
                    device_ip, device_info.get("device_id")
                ),
                "DEBUG",
            )

            device_id = device_info.get("device_id")

            device_layer2_configs = self.get_device_layer2_configurations(
                device_id,
                device_ip,
                layer2_features,
                feature_to_api_mapping,
                component_specific_filters,
                network_element,
            )
            self.log(
                "Retrieved {0} layer2 configurations from device {1}. Configs: {2}".format(
                    len(device_layer2_configs), device_ip, device_layer2_configs
                ),
                "DEBUG",
            )

            if device_layer2_configs:
                if device_ip not in device_configurations:
                    device_configurations[device_ip] = {
                        "device_info": device_info,  # Store full device info for identifier selection
                        "configs": [],
                    }

                device_configurations[device_ip]["configs"].extend(
                    device_layer2_configs
                )
                self.log(
                    "Adding {0} configurations from device {1} to collection".format(
                        len(device_layer2_configs), device_ip
                    ),
                    "DEBUG",
                )

        self.log(
            "Completed configuration retrieval from all devices 'device_configurations': {0}".format(
                device_configurations
            ),
            "DEBUG",
        )

        self.log(
            "Applying reverse mapping to transform API data to user format", "DEBUG"
        )
        reverse_mapping_function = network_element.get("reverse_mapping_function")
        reverse_mapping_spec = reverse_mapping_function(layer2_features)

        # Transform configurations per device
        transformed_configurations = []

        for device_ip, device_data in device_configurations.items():
            self.log(
                "Processing configurations for device: {0}".format(device_ip), "DEBUG"
            )

            device_info = device_data["device_info"]
            configs = device_data["configs"]

            # Get the appropriate identifier based on filter type
            identifier_key, identifier_value = (
                self.get_device_identifier_from_filter_type(
                    device_info, selected_filter_type
                )
            )

            # For IP addresses, use the device_ip from the mapping key
            if identifier_key == "ip_address":
                identifier_value = device_ip

            self.log(
                "Using device identifier: {0} = {1}".format(
                    identifier_key, identifier_value
                ),
                "DEBUG",
            )

            # Initialize device-specific layer2_configuration as OrderedDict
            device_layer2_config = OrderedDict()

            for config in configs:
                for feature_type, feature_data in config.items():
                    if feature_type in reverse_mapping_spec and feature_data:
                        self.log(
                            "Applying transformation for feature type: {0}".format(
                                feature_type
                            ),
                            "DEBUG",
                        )

                        # Apply transformations based on feature type
                        if feature_type in [
                            "cdp",
                            "lldp",
                            "vtp",
                            "stp",
                            "dhcp_snooping",
                            "igmp_snooping",
                            "mld_snooping",
                            "authentication",
                            "logical_ports",
                        ]:
                            api_feature_name = {
                                "cdp": "cdpGlobalConfig",
                                "lldp": "lldpGlobalConfig",
                                "vtp": "vtpGlobalConfig",
                                "stp": "stpGlobalConfig",
                                "dhcp_snooping": "dhcpSnoopingGlobalConfig",
                                "igmp_snooping": "igmpSnoopingGlobalConfig",
                                "mld_snooping": "mldSnoopingGlobalConfig",
                                "authentication": "dot1xGlobalConfig",
                                "logical_ports": "portchannelConfig",
                            }[feature_type]

                            items = feature_data.get(api_feature_name, {}).get(
                                "items", []
                            )
                            if items:
                                transformed_data = self.modify_parameters(
                                    reverse_mapping_spec[feature_type], [items[0]]
                                )
                                if transformed_data:
                                    if feature_type not in device_layer2_config:
                                        device_layer2_config[feature_type] = (
                                            transformed_data[0]
                                        )
                                    else:
                                        device_layer2_config[feature_type].update(
                                            transformed_data[0]
                                        )
                        elif feature_type == "port_configuration":
                            # Port configuration is already fully processed and reverse-mapped
                            # Just extend the data directly without additional transformation
                            self.log(
                                "Port configuration data is already reverse-mapped, adding directly",
                                "DEBUG",
                            )
                            if feature_type not in device_layer2_config:
                                device_layer2_config[feature_type] = []
                            device_layer2_config[feature_type].extend(feature_data)
                        else:
                            # For vlans and other list-based features
                            self.log(
                                "Transforming list-based feature type: {0}".format(
                                    feature_type
                                ),
                                "DEBUG",
                            )
                            self.log(
                                "Feature data before transformation: {0}".format(
                                    feature_data
                                ),
                                "DEBUG",
                            )

                            # Special handling for VLANs - flatten the structure
                            if feature_type == "vlans":
                                vlan_items = feature_data.get("vlanConfig", {}).get(
                                    "items", []
                                )
                                if vlan_items:
                                    flattened_data = {"items": vlan_items}
                                    transformed_data = self.modify_parameters(
                                        reverse_mapping_spec[feature_type],
                                        [flattened_data],
                                    )
                                else:
                                    transformed_data = []
                            else:
                                transformed_data = self.modify_parameters(
                                    reverse_mapping_spec[feature_type],
                                    (
                                        feature_data
                                        if isinstance(feature_data, list)
                                        else [feature_data]
                                    ),
                                )

                            self.log(
                                "Transformed data for feature type {0}: {1}".format(
                                    feature_type, transformed_data
                                ),
                                "DEBUG",
                            )

                            if transformed_data:
                                if feature_type == "vlans":
                                    device_layer2_config[feature_type] = (
                                        transformed_data[0].get("vlans", [])
                                    )
                                else:
                                    if feature_type not in device_layer2_config:
                                        device_layer2_config[feature_type] = []
                                    device_layer2_config[feature_type].extend(
                                        transformed_data
                                    )

            # Add device configuration with identifier first using OrderedDict
            if device_layer2_config:
                device_config = OrderedDict()
                # Add identifier first to ensure it appears at the top
                device_config[identifier_key] = identifier_value
                device_config["layer2_configuration"] = device_layer2_config
                transformed_configurations.append(device_config)
                self.log(
                    "Added configuration for device with {0}: {1}".format(
                        identifier_key, identifier_value
                    ),
                    "DEBUG",
                )

        self.log("Generating comprehensive operation summary", "DEBUG")
        operation_summary = self.get_operation_summary()

        final_result = {
            "layer2_configurations": transformed_configurations,
            "operation_summary": operation_summary,
        }

        self.log(
            "Layer2 configurations retrieval completed successfully for {0} devices".format(
                len(device_ip_to_id_mapping)
            ),
            "INFO",
        )

        return final_result

    def process_global_filters(self, global_filters):
        """
        Processes global filters to get device IP to ID mapping using priority-based selection.
        Priority order: 1. IP addresses (highest), 2. Serial numbers, 3. Hostnames (lowest)
        Only the highest priority filter type provided will be used.
        Args:
            global_filters (dict): Dictionary containing ip_address_list, hostname_list, and serial_number_list
        Returns:
            dict: Dictionary containing processed global filters with device_ip_to_id_mapping
        """
        self.log(
            "Processing global filters with priority-based selection: {0}".format(
                global_filters
            ),
            "DEBUG",
        )

        # Extract filter lists
        ip_addresses = global_filters.get("ip_address_list", [])
        serial_numbers = global_filters.get("serial_number_list", [])
        hostnames = global_filters.get("hostname_list", [])

        self.log(
            "Raw filters - IP addresses: {0}, Serial numbers: {1}, Hostnames: {2}".format(
                ip_addresses, serial_numbers, hostnames
            ),
            "DEBUG",
        )

        # Check if no filters provided at all
        if not ip_addresses and not serial_numbers and not hostnames:
            self.log(
                "No device identification filters provided - will be handled by caller",
                "DEBUG",
            )
            return {
                "device_ip_to_id_mapping": {},
                "total_devices": 0,
                "applied_filters": {
                    "selected_filter_type": None,
                    "selected_values": [],
                    "ignored_filters": [],
                },
            }

        # Priority-based selection logic
        selected_filter_type = None
        selected_values = []

        if ip_addresses:
            selected_filter_type = "ip_addresses"
            selected_values = ip_addresses
            self.log(
                "IP addresses provided (HIGHEST PRIORITY) - using IP address filter: {0}".format(
                    ip_addresses
                ),
                "INFO",
            )
            if serial_numbers:
                self.log(
                    "Serial numbers provided but IGNORED due to lower priority: {0}".format(
                        serial_numbers
                    ),
                    "WARNING",
                )
            if hostnames:
                self.log(
                    "Hostnames provided but IGNORED due to lower priority: {0}".format(
                        hostnames
                    ),
                    "WARNING",
                )
        elif serial_numbers:
            selected_filter_type = "serial_numbers"
            selected_values = serial_numbers
            self.log(
                "Serial numbers provided (MEDIUM PRIORITY) - using serial number filter: {0}".format(
                    serial_numbers
                ),
                "INFO",
            )
            if hostnames:
                self.log(
                    "Hostnames provided but IGNORED due to lower priority: {0}".format(
                        hostnames
                    ),
                    "WARNING",
                )
        elif hostnames:
            selected_filter_type = "hostnames"
            selected_values = hostnames
            self.log(
                "Hostnames provided (LOWEST PRIORITY) - using hostname filter: {0}".format(
                    hostnames
                ),
                "INFO",
            )

        # Prepare parameters for get_network_device_details based on selected filter
        kwargs = {}
        ignored_filters = []

        if selected_filter_type == "ip_addresses":
            kwargs["ip_addresses"] = selected_values
            if serial_numbers:
                ignored_filters.append(
                    {"type": "serial_numbers", "values": serial_numbers}
                )
            if hostnames:
                ignored_filters.append({"type": "hostnames", "values": hostnames})
        elif selected_filter_type == "serial_numbers":
            kwargs["serial_numbers"] = selected_values
            if hostnames:
                ignored_filters.append({"type": "hostnames", "values": hostnames})
        elif selected_filter_type == "hostnames":
            kwargs["hostnames"] = selected_values

        self.log(
            "Calling get_network_device_details with selected filter type: {0}".format(
                selected_filter_type
            ),
            "DEBUG",
        )

        # Get device IDs using the selected filter
        device_ip_to_id_mapping = self.get_network_device_details(**kwargs)

        self.log(
            "Retrieved device mapping using {0}: {1}".format(
                selected_filter_type, device_ip_to_id_mapping
            ),
            "DEBUG",
        )

        processed_filters = {
            "device_ip_to_id_mapping": device_ip_to_id_mapping,
            "total_devices": len(device_ip_to_id_mapping),
            "applied_filters": {
                "selected_filter_type": selected_filter_type,
                "selected_values": selected_values,
                "ignored_filters": ignored_filters,
            },
        }

        self.log(
            "Processed global filters result - Selected: {0} with {1} values, Ignored: {2} filter types".format(
                selected_filter_type, len(selected_values), len(ignored_filters)
            ),
            "INFO",
        )

        return processed_filters

    def get_device_identifier_from_filter_type(self, device_info, filter_type):
        """
        Returns the appropriate device identifier based on the filter type used.
        Args:
            device_info (dict): Device information containing device_id, hostname, serial_number
            filter_type (str): The filter type used (ip_addresses, serial_numbers, hostnames)
        Returns:
            tuple: (identifier_key, identifier_value) for the final configuration
        """
        self.log(
            "Getting device identifier for filter type: {0}".format(filter_type),
            "DEBUG",
        )

        if filter_type == "ip_addresses":
            # For IP addresses, we use the key from device_ip_to_id_mapping (which is the IP)
            self.log(
                "Using IP address identifier for filter type: {0}".format(filter_type),
                "DEBUG",
            )
            return ("ip_address", None)  # IP will be provided by the caller
        elif filter_type == "serial_numbers":
            serial_number = device_info.get("serial_number")
            self.log(
                "Using serial number identifier: {0}".format(serial_number), "DEBUG"
            )
            return ("serial_number", serial_number)
        elif filter_type == "hostnames":
            hostname = device_info.get("hostname")
            self.log("Using hostname identifier: {0}".format(hostname), "DEBUG")
            return ("hostname", hostname)
        else:
            # Default fallback to IP address
            self.log(
                "Unknown filter type {0}, defaulting to ip_address".format(filter_type),
                "WARNING",
            )
            return ("ip_address", None)

    def get_device_layer2_configurations(
        self,
        device_id,
        device_ip,
        layer2_features,
        feature_to_api_mapping,
        component_specific_filters,
        network_element,
    ):
        """
        Retrieves layer2 configurations for a specific device by making API calls for each requested feature.
        Handles special processing for port configurations which require multiple API calls and consolidation.
        Args:
            device_id (str): Unique identifier for the device in DNA Center.
            device_ip (str): IP address of the device for logging and identification purposes.
            layer2_features (list): List of layer2 feature names to retrieve configurations for.
            feature_to_api_mapping (dict): Mapping dictionary from feature names to corresponding API feature identifiers.
            component_specific_filters (dict): Filters to apply to configuration data before processing.
            network_element (dict): Network element configuration containing API family and function details.
        Returns:
            list: List of configuration dictionaries for the device, one per successfully retrieved feature.
        """
        self.log(
            "Initiating layer2 configuration retrieval process for device {0} with IP {1}".format(
                device_id, device_ip
            ),
            "DEBUG",
        )
        self.log(
            "Features requested for retrieval: {0}".format(layer2_features), "DEBUG"
        )
        self.log(
            "Total number of features to process: {0}".format(len(layer2_features)),
            "DEBUG",
        )

        device_configurations = []

        self.log(
            "Extracting API configuration parameters from network element", "DEBUG"
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "Extracted API family: '{0}', API function: '{1}' for device operations".format(
                api_family, api_function
            ),
            "DEBUG",
        )

        if not api_family or not api_function:
            self.log(
                "Missing required API configuration - family: {0}, function: {1}".format(
                    api_family, api_function
                ),
                "ERROR",
            )
            return []

        self.log(
            "Incrementing total features processed counter by {0}".format(
                len(layer2_features)
            ),
            "DEBUG",
        )
        self.total_features_processed += len(layer2_features)

        for feature_index, feature in enumerate(layer2_features):
            self.log(
                "Processing feature {0} of {1}: '{2}' for device {3}".format(
                    feature_index + 1, len(layer2_features), feature, device_ip
                ),
                "DEBUG",
            )

            api_features = feature_to_api_mapping.get(feature)
            if not api_features:
                error_msg = "No API mapping found for feature '{0}' in feature_to_api_mapping dictionary".format(
                    feature
                )
                self.log(error_msg, "WARNING")
                self.log(
                    "Available mappings in feature_to_api_mapping: {0}".format(
                        list(feature_to_api_mapping.keys())
                    ),
                    "DEBUG",
                )
                self.add_failure(
                    device_ip,
                    device_id,
                    feature,
                    {
                        "error_type": "mapping_error",
                        "error_message": error_msg,
                        "error_code": "MAPPING_ERROR",
                        "available_features": list(feature_to_api_mapping.keys()),
                    },
                )
                continue

            self.log(
                "Found API mapping for feature '{0}': {1}".format(
                    feature, api_features
                ),
                "DEBUG",
            )

            # Ensure api_features is always a list for consistent processing
            if isinstance(api_features, str):
                self.log("Converting single API feature string to list format", "DEBUG")
                api_features = [api_features]

            self.log(
                "API features to process for '{0}': {1} (total: {2})".format(
                    feature, api_features, len(api_features)
                ),
                "DEBUG",
            )

            feature_success = False
            feature_errors = []

            # Route to appropriate processing method based on feature type
            if feature == "port_configuration":
                self.log(
                    "Routing to specialized port configuration processing", "DEBUG"
                )
                port_config_result = self._process_port_configuration_feature(
                    device_id,
                    device_ip,
                    api_features,
                    component_specific_filters,
                    api_family,
                    api_function,
                    feature_errors,
                )
                self.log(
                    "Port configuration processing result: {0}".format(
                        port_config_result
                    ),
                    "DEBUG",
                )

                if port_config_result["success"]:
                    feature_success = True
                    if port_config_result["configurations"]:
                        device_configurations.extend(
                            port_config_result["configurations"]
                        )
                        self.log(
                            "Successfully processed port configuration feature", "DEBUG"
                        )

                feature_errors.extend(port_config_result["errors"])
            else:
                self.log(
                    "Processing standard feature '{0}' using normal API call flow".format(
                        feature
                    ),
                    "DEBUG",
                )
                standard_result = self._process_standard_feature(
                    device_id,
                    device_ip,
                    feature,
                    api_features,
                    component_specific_filters,
                    api_family,
                    api_function,
                    feature_errors,
                )

                if standard_result["success"]:
                    feature_success = True
                    if standard_result["configurations"]:
                        device_configurations.extend(standard_result["configurations"])
                        self.log(
                            "Successfully processed standard feature '{0}'".format(
                                feature
                            ),
                            "DEBUG",
                        )

                feature_errors.extend(standard_result["errors"])

            # Evaluate and track feature processing results
            self.log(
                "Evaluating processing results for feature '{0}' on device {1}".format(
                    feature, device_ip
                ),
                "DEBUG",
            )
            if feature_success:
                self.log(
                    "Feature '{0}' processed successfully - adding to success tracking".format(
                        feature
                    ),
                    "DEBUG",
                )
                self.add_success(
                    device_ip,
                    device_id,
                    feature,
                    {
                        "api_features_processed": api_features,
                        "processing_method": (
                            "port_configuration"
                            if feature == "port_configuration"
                            else "standard"
                        ),
                    },
                )
            else:
                self.log(
                    "Feature '{0}' processing failed - consolidating error information for tracking".format(
                        feature
                    ),
                    "DEBUG",
                )
                self.log(
                    "Total errors encountered for feature '{0}': {1}".format(
                        feature, len(feature_errors)
                    ),
                    "DEBUG",
                )

                consolidated_error = {
                    "error_type": "feature_retrieval_failed",
                    "error_message": "Failed to retrieve {0} configuration for device {1}".format(
                        feature, device_ip
                    ),
                    "error_code": "FEATURE_RETRIEVAL_FAILED",
                    "detailed_errors": feature_errors,
                    "api_features_attempted": api_features,
                }
                self.add_failure(device_ip, device_id, feature, consolidated_error)

        self.log(
            "Completed layer2 configuration retrieval for device {0} (IP: {1}). Configurations: {2}".format(
                device_id, device_ip, device_configurations
            ),
            "DEBUG",
        )
        self.log(
            "Total configurations successfully retrieved: {0}".format(
                len(device_configurations)
            ),
            "DEBUG",
        )
        self.log(
            "Configuration features retrieved: {0}".format(
                [list(config.keys())[0] for config in device_configurations]
            ),
            "DEBUG",
        )

        return device_configurations

    def _process_standard_feature(
        self,
        device_id,
        device_ip,
        feature,
        api_features,
        component_specific_filters,
        api_family,
        api_function,
        feature_errors,
    ):
        """
        Processes standard features using normal API call flow with single API endpoint per feature.
        Args:
            device_id (str): Unique identifier for the device in DNA Center.
            device_ip (str): IP address of the device for logging purposes.
            feature (str): Feature name being processed.
            api_features (list): List of API feature names (typically single item for standard features).
            component_specific_filters (dict): Filters to apply to configuration data.
            api_family (str): API family name for making requests.
            api_function (str): API function name for making requests.
            feature_errors (list): List to collect any errors encountered during processing.
        Returns:
            dict: Dictionary containing success status, configurations, and errors.
        """
        self.log(
            "Processing standard feature '{0}' using normal API call flow for device {1}".format(
                feature, device_ip
            ),
            "DEBUG",
        )
        self.log(
            "Standard feature processing involves {0} API call(s)".format(
                len(api_features)
            ),
            "DEBUG",
        )

        processing_result = {"success": False, "configurations": [], "errors": []}

        for api_feature_index, api_feature in enumerate(api_features):
            self.log(
                "Processing API feature {0} of {1}: '{2}' for feature '{3}' on device {4}".format(
                    api_feature_index + 1,
                    len(api_features),
                    api_feature,
                    feature,
                    device_ip,
                ),
                "DEBUG",
            )

            self.log(
                "Preparing API request parameters for {0}".format(api_feature), "DEBUG"
            )
            api_params = {"id": device_id, "feature": api_feature}
            self.log(
                "API request parameters constructed: {0}".format(api_params), "DEBUG"
            )

            try:
                self.log(
                    "Executing GET request for {0} using execute_get_request method".format(
                        api_feature
                    ),
                    "DEBUG",
                )

                response = self.execute_get_request(
                    api_family, api_function, api_params
                )

                if response and response.get("response"):
                    self.log(
                        "API response received successfully for {0}".format(
                            api_feature
                        ),
                        "DEBUG",
                    )

                    # Use dynamic error checking function
                    response_data = response.get("response")
                    if self.is_api_error_response(response_data):
                        # Use dynamic error extraction function
                        error_info = self.extract_api_error_info(
                            response_data, api_feature, device_ip
                        )
                        processing_result["errors"].append(error_info)
                        self.log(
                            "API returned error for {0}: {1}".format(
                                api_feature, error_info["error_message"]
                            ),
                            "ERROR",
                        )
                        continue

                    self.log(
                        "Extracting configuration data from successful API response",
                        "DEBUG",
                    )
                    config_data = response.get("response")

                    self.log(
                        "Applying component-specific filters to {0} configuration data".format(
                            api_feature
                        ),
                        "DEBUG",
                    )
                    filtered_data = self.apply_component_specific_filters(
                        config_data, feature, component_specific_filters
                    )

                    if filtered_data:
                        self.log(
                            "Configuration data successfully filtered for {0}".format(
                                api_feature
                            ),
                            "DEBUG",
                        )
                        structured_data = {feature: filtered_data}
                        processing_result["configurations"].append(structured_data)
                        processing_result["success"] = True

                        self.log(
                            "Successfully retrieved, filtered, and structured {0} for device {1}".format(
                                feature, device_ip
                            ),
                            "DEBUG",
                        )
                    else:
                        warning_msg = "No data remaining after applying filters for {0} on device {1}".format(
                            api_feature, device_ip
                        )
                        self.log(warning_msg, "DEBUG")

                        processing_result["errors"].append(
                            {
                                "api_feature": api_feature,
                                "error_type": "no_data_after_filtering",
                                "error_message": "No data found after applying component-specific filters for {0}".format(
                                    api_feature
                                ),
                                "error_code": "NO_DATA_AFTER_FILTERING",
                            }
                        )
                else:
                    error_message = (
                        "No response data received for {0} on device {1}".format(
                            api_feature, device_ip
                        )
                    )
                    self.log(error_message, "WARNING")
                    self.log(
                        "Response validation failed - missing or empty response data",
                        "DEBUG",
                    )

                    processing_result["errors"].append(
                        {
                            "api_feature": api_feature,
                            "error_type": "no_response_data",
                            "error_message": error_message,
                            "error_code": "NO_RESPONSE_DATA",
                        }
                    )

            except Exception as e:
                error_message = "Exception occurred while retrieving {0} for device {1}: {2}".format(
                    api_feature, device_ip, str(e)
                )
                self.log(error_message, "ERROR")
                self.log(
                    "Exception details - Type: {0}, Message: {1}".format(
                        type(e).__name__, str(e)
                    ),
                    "ERROR",
                )

                processing_result["errors"].append(
                    {
                        "api_feature": api_feature,
                        "error_type": "exception",
                        "error_message": error_message,
                        "error_code": "EXCEPTION_ERROR",
                        "exception_type": type(e).__name__,
                        "exception_details": str(e),
                    }
                )

        self.log(
            "Standard feature '{0}' processing completed with success: {1}".format(
                feature, processing_result["success"]
            ),
            "DEBUG",
        )

        return processing_result

    def _process_port_configuration_feature(
        self,
        device_id,
        device_ip,
        api_features,
        component_specific_filters,
        api_family,
        api_function,
        feature_errors,
    ):
        """
        Processes port configuration feature by retrieving all interface-related API responses and merging them.
        Args:
            device_id (str): Unique identifier for the device in DNA Center.
            device_ip (str): IP address of the device for logging purposes.
            api_features (list): List of API feature names for port configuration.
            component_specific_filters (dict): Filters to apply to configuration data.
            api_family (str): API family name for making requests.
            api_function (str): API function name for making requests.
            feature_errors (list): List to collect any errors encountered during processing.
        Returns:
            dict: Dictionary containing success status, configurations, and errors.
        """
        self.log(
            "Starting port configuration feature processing for device {0} (IP: {1})".format(
                device_id, device_ip
            ),
            "DEBUG",
        )
        self.log(
            "Port configuration requires processing {0} API features: {1}".format(
                len(api_features), api_features
            ),
            "DEBUG",
        )

        processing_result = {"success": False, "configurations": [], "errors": []}

        # Step 1: Get all feature configurations for port configuration
        self.log(
            "Step 1: Retrieving all API feature configurations for port configuration",
            "DEBUG",
        )
        all_feature_configs = self.get_all_port_features(
            device_id, device_ip, api_features, api_family, api_function
        )
        self.log(
            "All port feature configurations retrieved: {0}".format(
                all_feature_configs
            ),
            "DEBUG",
        )

        if not all_feature_configs["success"]:
            self.log(
                "Failed to retrieve port feature configurations for device {0}".format(
                    device_ip
                ),
                "ERROR",
            )
            processing_result["errors"].extend(all_feature_configs["errors"])
            return processing_result

        # Step 2: Merge configurations by interface name
        self.log("Step 2: Merging port configurations by interface name", "DEBUG")
        merged_interface_configs = self.merge_port_configurations(
            all_feature_configs["configurations"]
        )
        self.log(
            "Merged interface configurations: {0}".format(merged_interface_configs),
            "DEBUG",
        )

        if not merged_interface_configs:
            self.log(
                "No port configurations to process for device {0}".format(device_ip),
                "WARNING",
            )
            processing_result["errors"].append(
                {
                    "error_type": "no_merged_configurations",
                    "error_message": "No port configurations available for merging",
                    "error_code": "NO_MERGED_CONFIGS",
                }
            )
            return processing_result

        # Step 3: Apply component-specific filters to merged configurations
        self.log(
            "Step 3: Applying component-specific filters to merged port configurations",
            "DEBUG",
        )
        filtered_interface_configs = self.apply_port_configuration_filters(
            merged_interface_configs, component_specific_filters
        )
        self.log(
            "Filtered interface configurations: {0}".format(filtered_interface_configs),
            "DEBUG",
        )

        if not filtered_interface_configs:
            self.log(
                "No port configurations remain after filtering for device {0}".format(
                    device_ip
                ),
                "WARNING",
            )
            processing_result["errors"].append(
                {
                    "error_type": "no_configurations_after_filtering",
                    "error_message": "No port configurations remain after applying component-specific filters",
                    "error_code": "NO_CONFIGS_AFTER_FILTERING",
                }
            )
            return processing_result

        # Step 4: Reverse map the filtered configurations to final format
        self.log(
            "Step 4: Reverse mapping filtered interface configurations to final format",
            "DEBUG",
        )
        final_port_configurations = self.reverse_map_port_configurations(
            filtered_interface_configs, component_specific_filters
        )
        self.log(
            "Final port configurations after reverse mapping: {0}".format(
                final_port_configurations
            ),
            "DEBUG",
        )

        if final_port_configurations:
            self.log(
                "Successfully reverse mapped port configurations for {0} interfaces on device {1}".format(
                    len(final_port_configurations), device_ip
                ),
                "INFO",
            )
            processing_result["success"] = True
            processing_result["configurations"].append(
                {"port_configuration": final_port_configurations}
            )
        else:
            self.log(
                "No port configurations successfully reverse mapped for device {0}".format(
                    device_ip
                ),
                "WARNING",
            )
            processing_result["errors"].append(
                {
                    "error_type": "no_reverse_mapped_configurations",
                    "error_message": "No port configurations were successfully reverse mapped",
                    "error_code": "NO_REVERSE_MAPPED_CONFIGS",
                }
            )

        self.log(
            "Port configuration processing completed for device {0}".format(device_ip),
            "DEBUG",
        )

        return processing_result

    def get_all_port_features(
        self, device_id, device_ip, api_features, api_family, api_function
    ):
        """
        Retrieves configurations for all port-related API features from a device.
        Args:
            device_id (str): Unique identifier for the device in DNA Center.
            device_ip (str): IP address of the device for logging purposes.
            api_features (list): List of API feature names to retrieve.
            api_family (str): API family name for making requests.
            api_function (str): API function name for making requests.
        Returns:
            dict: Dictionary containing success status, consolidated configurations, and any errors.
        """
        self.log(
            "Starting retrieval of all port feature configurations for device {0}".format(
                device_ip
            ),
            "DEBUG",
        )
        self.log(
            "Will retrieve {0} API features: {1}".format(
                len(api_features), api_features
            ),
            "DEBUG",
        )

        result = {"success": False, "configurations": {}, "errors": []}

        successful_retrievals = 0

        for feature_index, api_feature in enumerate(api_features):
            self.log(
                "Retrieving API feature {0} of {1}: '{2}' for device {3}".format(
                    feature_index + 1, len(api_features), api_feature, device_ip
                ),
                "DEBUG",
            )

            # Get single feature configuration
            feature_result = self.get_single_port_feature(
                device_id, device_ip, api_feature, api_family, api_function
            )

            if feature_result["success"]:
                result["configurations"][api_feature] = feature_result
                successful_retrievals += 1
                self.log(
                    "Successfully retrieved {0} configuration for device {1}".format(
                        api_feature, device_ip
                    ),
                    "DEBUG",
                )
            else:
                result["errors"].extend(feature_result["errors"])
                self.log(
                    "Failed to retrieve {0} configuration for device {1}: {2}".format(
                        api_feature, device_ip, feature_result["errors"]
                    ),
                    "WARNING",
                )

        # Determine overall success based on retrievals
        if successful_retrievals > 0:
            result["success"] = True
            self.log(
                "Successfully retrieved {0} out of {1} port feature configurations for device {2}".format(
                    successful_retrievals, len(api_features), device_ip
                ),
                "INFO",
            )
        else:
            self.log(
                "Failed to retrieve any port feature configurations for device {0}".format(
                    device_ip
                ),
                "ERROR",
            )
            result["errors"].append(
                {
                    "error_type": "no_configurations_retrieved",
                    "error_message": "Failed to retrieve any port feature configurations from device",
                    "error_code": "NO_PORT_CONFIGS_RETRIEVED",
                }
            )

        return result

    def get_single_port_feature(
        self, device_id, device_ip, api_feature, api_family, api_function
    ):
        """
        Retrieves configuration for a single port-related API feature from a device.
        Args:
            device_id (str): Unique identifier for the device in DNA Center.
            device_ip (str): IP address of the device for logging purposes.
            api_feature (str): Specific API feature name to retrieve.
            api_family (str): API family name for making requests.
            api_function (str): API function name for making requests.
        Returns:
            dict: Dictionary containing success status, configuration data, and any errors.
        """
        self.log(
            "Retrieving single port feature configuration: {0} for device {1}".format(
                api_feature, device_ip
            ),
            "DEBUG",
        )

        result = {"success": False, "data": None, "errors": []}

        # Prepare API request parameters
        api_params = {"id": device_id, "feature": api_feature}
        self.log(
            "API request parameters for {0}: {1}".format(api_feature, api_params),
            "DEBUG",
        )

        try:
            self.log(
                "Executing GET request for {0} using {1}.{2}".format(
                    api_feature, api_family, api_function
                ),
                "DEBUG",
            )

            response = self.execute_get_request(api_family, api_function, api_params)

            if response and response.get("response"):
                self.log("API response received for {0}".format(api_feature), "DEBUG")

                # Check for API error in response
                response_data = response.get("response")
                if self.is_api_error_response(response_data):
                    error_info = self.extract_api_error_info(
                        response_data, api_feature, device_ip
                    )
                    result["errors"].append(error_info)
                    self.log(
                        "API returned error for {0}: {1}".format(
                            api_feature, error_info["error_message"]
                        ),
                        "ERROR",
                    )
                    return result

                # Successful response
                result["success"] = True
                result["data"] = response_data
                self.log(
                    "Successfully retrieved {0} configuration data".format(api_feature),
                    "DEBUG",
                )

            else:
                error_msg = "No response data received for {0} on device {1}".format(
                    api_feature, device_ip
                )
                self.log(error_msg, "WARNING")
                result["errors"].append(
                    {
                        "api_feature": api_feature,
                        "error_type": "no_response_data",
                        "error_message": error_msg,
                        "error_code": "NO_RESPONSE_DATA",
                    }
                )

        except Exception as e:
            error_msg = (
                "Exception occurred while retrieving {0} for device {1}: {2}".format(
                    api_feature, device_ip, str(e)
                )
            )
            self.log(error_msg, "ERROR")
            self.log("Exception details - Type: {0}".format(type(e).__name__), "ERROR")

            result["errors"].append(
                {
                    "api_feature": api_feature,
                    "error_type": "exception",
                    "error_message": error_msg,
                    "error_code": "API_EXCEPTION_ERROR",
                    "exception_type": type(e).__name__,
                    "exception_details": str(e),
                }
            )

        return result

    def find_feature_with_most_interfaces(self, all_feature_configs):
        """
        Finds the API feature configuration that contains the highest number of interface items.
        Args:
            all_feature_configs (dict): Dictionary containing all port feature configurations where keys are API feature names
            and values are the actual API response data.
        Returns:
            str: Name of the API feature with the most interfaces, or None if no valid configurations found
        """
        self.log(
            "Analyzing feature configurations to identify feature with highest interface count",
            "DEBUG",
        )
        self.log("all_feature_configs: {0}".format(all_feature_configs), "DEBUG")
        feature_counts = {}

        # Count interfaces in each feature
        for api_feature_name, api_response_data in all_feature_configs.items():
            self.log(
                "Evaluating feature '{0}' with response data: {1}".format(
                    api_feature_name, api_response_data
                ),
                "DEBUG",
            )
            if isinstance(api_response_data, dict):
                self.log(
                    "Extracting 'items' list from feature '{0}' configuration".format(
                        api_feature_name
                    ),
                    "DEBUG",
                )
                feature_config_section = api_response_data.get("data", {}).get(
                    api_feature_name, {}
                )
                self.log(
                    "Feature '{0}' configuration section: {1}".format(
                        api_feature_name, feature_config_section
                    ),
                    "DEBUG",
                )
                if isinstance(feature_config_section, dict):
                    interface_items = feature_config_section.get("items", [])
                    self.log(
                        "Feature '{0}' has {1} interface items".format(
                            api_feature_name, len(interface_items)
                        ),
                        "DEBUG",
                    )
                    if isinstance(interface_items, list):
                        self.log(
                            "Recording interface count for feature '{0}'".format(
                                api_feature_name
                            ),
                            "DEBUG",
                        )
                        feature_counts[api_feature_name] = len(interface_items)
                        self.log(
                            "Feature '{0}' has {1} interfaces".format(
                                api_feature_name, len(interface_items)
                            ),
                            "DEBUG",
                        )

        self.log("Feature interface counts: {0}".format(feature_counts), "DEBUG")

        # Find feature with most interfaces
        if feature_counts:
            feature_with_most = max(feature_counts, key=feature_counts.get)
            self.log(
                "Feature with most interfaces: '{0}' with {1} interfaces".format(
                    feature_with_most, feature_counts[feature_with_most]
                ),
                "INFO",
            )
            return feature_with_most

        self.log("No valid feature configurations found", "WARNING")
        return None

    def merge_port_configurations(self, all_feature_configs):
        """
        Merges port configurations from all features based on interface name.
        Creates a consolidated dictionary where each interface has all its feature configurations.
        Args:
            all_feature_configs (dict): Dictionary containing all port feature configurations
        Returns:
            list: List of merged interface configurations
        """
        self.log("Starting port configuration merge process", "DEBUG")

        # Find the feature with most interfaces to use as reference
        reference_feature = self.find_feature_with_most_interfaces(all_feature_configs)
        if not reference_feature:
            self.log(
                "No reference feature found for merging port configurations", "WARNING"
            )
            return []

        self.log(
            "Using '{0}' as reference feature for interface merging".format(
                reference_feature
            ),
            "INFO",
        )

        # Get reference interfaces list
        reference_data = all_feature_configs.get(reference_feature, {})
        reference_items = (
            reference_data.get("data", {}).get(reference_feature, {}).get("items", [])
        )

        self.log(
            "Reference feature contains {0} interfaces for merging".format(
                len(reference_items)
            ),
            "DEBUG",
        )

        merged_interfaces = []

        # Process each interface from reference feature
        for interface_item in reference_items:
            interface_name = interface_item.get("interfaceName")
            if not interface_name:
                self.log("Skipping interface item without interfaceName", "WARNING")
                continue

            self.log("Processing interface: {0}".format(interface_name), "DEBUG")

            # Initialize merged interface configuration
            merged_interface = {"interface_name": interface_name}

            # Merge configurations from all features for this interface
            for api_feature_name, feature_result in all_feature_configs.items():
                if not feature_result.get("success"):
                    self.log(
                        "Skipping failed feature '{0}' for interface {1}".format(
                            api_feature_name, interface_name
                        ),
                        "DEBUG",
                    )
                    continue

                # Extract feature data
                feature_data = feature_result.get("data", {})
                feature_config = feature_data.get(api_feature_name, {})
                feature_items = feature_config.get("items", [])

                # Find matching interface in this feature
                matching_item = None
                for item in feature_items:
                    if item.get("interfaceName") == interface_name:
                        matching_item = item
                        break

                if matching_item:
                    # Remove interfaceName and configType from the item before merging
                    cleaned_item = {
                        k: v
                        for k, v in matching_item.items()
                        if k not in ["interfaceName", "configType"]
                    }

                    if cleaned_item:  # Only add if there's actual configuration data
                        merged_interface[api_feature_name] = cleaned_item
                        self.log(
                            "Added {0} configuration for interface {1}".format(
                                api_feature_name, interface_name
                            ),
                            "DEBUG",
                        )
                    else:
                        self.log(
                            "No configuration data found in {0} for interface {1}".format(
                                api_feature_name, interface_name
                            ),
                            "DEBUG",
                        )
                else:
                    self.log(
                        "No configuration found in {0} for interface {1}".format(
                            api_feature_name, interface_name
                        ),
                        "DEBUG",
                    )

            # Only add interface if it has configurations beyond just the interface name
            if len(merged_interface) > 1:
                merged_interfaces.append(merged_interface)
                self.log(
                    "Successfully merged configurations for interface {0} with {1} features".format(
                        interface_name, len(merged_interface) - 1
                    ),
                    "DEBUG",
                )
            else:
                self.log(
                    "No feature configurations found for interface {0}, skipping".format(
                        interface_name
                    ),
                    "DEBUG",
                )

        self.log(
            "Port configuration merge completed - processed {0} interfaces, merged {1} interfaces".format(
                len(reference_items), len(merged_interfaces)
            ),
            "INFO",
        )

        return merged_interfaces

    def reverse_map_port_configurations(
        self, filtered_interface_configs, component_specific_filters
    ):
        """
        Reverse maps filtered interface configurations using modify_parameters and reverse mapping functions.
        Only processes interfaces that have switchportInterfaceConfig data.
        Args:
            filtered_interface_configs (list): List of filtered interface configurations.
            component_specific_filters (dict): Component-specific filters for additional processing.
        Returns:
            list: List of reverse-mapped port configuration dictionaries.
        """
        self.log("Starting reverse mapping process for port configurations", "DEBUG")
        self.log(
            "Input interface configurations count: {0}".format(
                len(filtered_interface_configs)
            ),
            "DEBUG",
        )

        if not filtered_interface_configs:
            self.log(
                "No interface configurations provided for reverse mapping", "DEBUG"
            )
            return []

        self.log(
            "Getting reverse mapping specification for port configuration features",
            "DEBUG",
        )
        port_config_reverse_spec = self.port_configuration_reverse_mapping_spec()
        self.log(
            "Retrieved reverse mapping spec with {0} feature mappings".format(
                len(port_config_reverse_spec)
            ),
            "DEBUG",
        )

        final_port_configurations = []
        processed_interfaces_count = 0
        skipped_interfaces_count = 0

        for interface_index, interface_config in enumerate(filtered_interface_configs):
            interface_name = interface_config.get("interface_name")
            self.log(
                "Processing interface {0} of {1}: {2}".format(
                    interface_index + 1, len(filtered_interface_configs), interface_name
                ),
                "DEBUG",
            )

            if not interface_name:
                self.log(
                    "Skipping interface configuration without interface_name at index {0}".format(
                        interface_index
                    ),
                    "WARNING",
                )
                skipped_interfaces_count += 1
                continue

            # Check if switchportInterfaceConfig exists - this is our main criterion
            switchport_config = interface_config.get("switchportInterfaceConfig")
            if not switchport_config:
                self.log(
                    "Interface {0} does not have switchportInterfaceConfig - skipping reverse mapping".format(
                        interface_name
                    ),
                    "DEBUG",
                )
                skipped_interfaces_count += 1
                continue

            self.log(
                "Interface {0} has switchportInterfaceConfig - proceeding with reverse mapping".format(
                    interface_name
                ),
                "DEBUG",
            )

            # Initialize the final interface configuration
            final_interface_config = {"interface_name": interface_name}
            reverse_mapped_features_count = 0

            # Process each feature type for this interface
            for feature_type, feature_spec in port_config_reverse_spec.items():
                self.log(
                    "Processing feature type: {0} for interface {1}".format(
                        feature_type, interface_name
                    ),
                    "DEBUG",
                )

                # Get the raw feature data from interface config
                raw_feature_data = interface_config.get(
                    self._get_api_feature_name(feature_type)
                )

                if not raw_feature_data:
                    self.log(
                        "No {0} data found for interface {1}".format(
                            feature_type, interface_name
                        ),
                        "DEBUG",
                    )
                    continue

                self.log(
                    "Found {0} data for interface {1} - applying reverse mapping".format(
                        feature_type, interface_name
                    ),
                    "DEBUG",
                )

                # Apply reverse mapping using modify_parameters
                try:
                    # Wrap the data in the expected structure for modify_parameters
                    wrapped_data = {
                        "interface_name": interface_name,
                        **raw_feature_data,
                    }

                    # Use modify_parameters to reverse map
                    reverse_mapped_data = self.modify_parameters(
                        {feature_type: feature_spec}, [wrapped_data]
                    )

                    if reverse_mapped_data and reverse_mapped_data[0].get(feature_type):
                        final_interface_config[feature_type] = reverse_mapped_data[0][
                            feature_type
                        ]
                        reverse_mapped_features_count += 1
                        self.log(
                            "Successfully reverse mapped {0} for interface {1}".format(
                                feature_type, interface_name
                            ),
                            "DEBUG",
                        )
                    else:
                        self.log(
                            "Reverse mapping for {0} resulted in empty data for interface {1}".format(
                                feature_type, interface_name
                            ),
                            "DEBUG",
                        )

                except Exception as e:
                    self.log(
                        "Error during reverse mapping of {0} for interface {1}: {2}".format(
                            feature_type, interface_name, str(e)
                        ),
                        "ERROR",
                    )
                    continue

            # Only add interface to final config if we successfully mapped at least one feature
            if reverse_mapped_features_count > 0:
                final_port_configurations.append(final_interface_config)
                processed_interfaces_count += 1
                self.log(
                    "Added interface {0} to final configuration with {1} mapped features".format(
                        interface_name, reverse_mapped_features_count
                    ),
                    "DEBUG",
                )
            else:
                self.log(
                    "Interface {0} has no successfully mapped features - excluding from final config".format(
                        interface_name
                    ),
                    "WARNING",
                )
                skipped_interfaces_count += 1

        self.log("Reverse mapping process completed", "INFO")
        self.log(
            "Successfully processed {0} interfaces out of {1} total".format(
                processed_interfaces_count, len(filtered_interface_configs)
            ),
            "INFO",
        )
        self.log(
            "Skipped {0} interfaces (no switchportInterfaceConfig or mapping failures)".format(
                skipped_interfaces_count
            ),
            "INFO",
        )

        if final_port_configurations:
            interface_names = [
                config.get("interface_name") for config in final_port_configurations
            ]
            self.log(
                "Final port configurations include interfaces: {0}".format(
                    interface_names
                ),
                "DEBUG",
            )
        else:
            self.log("No interfaces were successfully reverse mapped", "WARNING")

        return final_port_configurations

    def _get_api_feature_name(self, feature_type):
        """
        Maps feature type to corresponding API feature name.
        Args:
            feature_type (str): The feature type from reverse mapping spec.
        Returns:
            str: The corresponding API feature name.
        """
        self.log(
            "Mapping feature type '{0}' to API feature name".format(feature_type),
            "DEBUG",
        )

        api_feature_mapping = {
            "switchport_interface_config": "switchportInterfaceConfig",
            "vlan_trunking_interface_config": "trunkInterfaceConfig",
            "cdp_interface_config": "cdpInterfaceConfig",
            "lldp_interface_config": "lldpInterfaceConfig",
            "stp_interface_config": "stpInterfaceConfig",
            "dhcp_snooping_interface_config": "dhcpSnoopingInterfaceConfig",
            "dot1x_interface_config": "dot1xInterfaceConfig",
            "mab_interface_config": "mabInterfaceConfig",
            "vtp_interface_config": "vtpInterfaceConfig",
        }

        result = api_feature_mapping.get(feature_type, feature_type)
        self.log("Mapped '{0}' to '{1}'".format(feature_type, result), "DEBUG")

        return result

    def is_api_error_response(self, response_data):
        """
        Checks if the API response contains error information.
        Args:
            response_data (dict): API response data to check for errors.
        Returns:
            bool: True if response contains error, False otherwise.
        """
        self.log(
            "Checking API response for error indicators: {0}".format(
                type(response_data).__name__
            ),
            "DEBUG",
        )

        if not isinstance(response_data, dict):
            self.log("Response data is not a dictionary - no error detected", "DEBUG")
            return False

        # Check for common error indicators in API responses
        error_indicators = ["errorCode", "error_code", "errorMessage", "error"]

        for indicator in error_indicators:
            if response_data.get(indicator):
                self.log(
                    "API error detected - indicator: {0}, value: {1}".format(
                        indicator, response_data.get(indicator)
                    ),
                    "DEBUG",
                )
                return True

        self.log("No error indicators found in API response", "DEBUG")
        return False

    def extract_api_error_info(self, response_data, api_feature, device_ip):
        """
        Extracts error information from API response data.
        Args:
            response_data (dict): API response containing error information.
            api_feature (str): API feature name that failed.
            device_ip (str): Device IP address for context.
        Returns:
            dict: Structured error information.
        """
        self.log(
            "Extracting API error information for {0} on device {1}".format(
                api_feature, device_ip
            ),
            "DEBUG",
        )

        # Extract error code with fallback options
        error_code = (
            response_data.get("errorCode")
            or response_data.get("error_code")
            or "UNKNOWN_ERROR_CODE"
        )

        # Extract error message with fallback options
        error_message = (
            response_data.get("message")
            or response_data.get("errorMessage")
            or response_data.get("error")
            or "No error message provided by API"
        )

        # Extract additional details if available
        error_detail = response_data.get("detail", "")

        # Construct comprehensive error message
        full_error_message = "API Error {0}: {1}".format(error_code, error_message)
        if error_detail:
            full_error_message += " - Details: {0}".format(error_detail)

        error_info = {
            "api_feature": api_feature,
            "error_code": error_code,
            "error_message": full_error_message,
            "error_detail": error_detail,
            "api_response": response_data,
        }

        self.log(
            "Extracted error - code: {0}, message: {1}".format(
                error_code, error_message
            ),
            "DEBUG",
        )
        return error_info

    def apply_component_specific_filters(
        self, config_data, feature, component_specific_filters
    ):
        """
        Applies component-specific filters to configuration data based on the feature type.
        Routes to appropriate filter functions for different feature types like VLANs and port configurations.
        Args:
            config_data (dict): Raw configuration data received from API response.
            feature (str): Feature name indicating the type of configuration data being filtered.
            component_specific_filters (dict): Dictionary containing filter criteria for various components.
        Returns:
            dict: Filtered configuration data with only matching items included based on filter criteria.
        """
        self.log(
            "Starting component-specific filtering process for feature: {0}".format(
                feature
            ),
            "DEBUG",
        )
        self.log(
            "Input configuration data structure: {0} top-level keys".format(
                len(config_data) if isinstance(config_data, dict) else "non-dict type"
            ),
            "DEBUG",
        )

        if component_specific_filters:
            self.log(
                "Component-specific filters provided: {0}".format(
                    list(component_specific_filters.keys())
                ),
                "DEBUG",
            )
        else:
            self.log(
                "No component-specific filters provided - returning original data unchanged",
                "DEBUG",
            )
            return config_data

        # Route to appropriate filter function based on feature type
        if feature == "vlans":
            self.log("Routing to VLAN-specific filter function", "DEBUG")
            filtered_result = self.apply_vlan_filters(
                config_data, component_specific_filters
            )
        elif feature == "port_configuration":
            self.log("Routing to port configuration-specific filter function", "DEBUG")
            filtered_result = self.apply_port_configuration_filters(
                config_data, component_specific_filters
            )
        else:
            # For features without specific filter implementations, return data unchanged
            self.log(
                "No specific filter implementation for feature '{0}' - returning original data".format(
                    feature
                ),
                "DEBUG",
            )
            filtered_result = config_data

        self.log(
            "Component-specific filtering completed for feature: {0}".format(feature),
            "INFO",
        )
        return filtered_result

    def apply_vlan_filters(self, config_data, component_specific_filters):
        """
        Applies VLAN-specific filters to configuration data.
        Filters out system default VLANs and applies user-specified VLAN ID filters.
        Args:
            config_data (dict): Raw configuration data from API.
            component_specific_filters (dict): Component-specific filters.
        Returns:
            dict: Filtered VLAN configuration data.
        """
        self.log("Starting VLAN filtering process", "DEBUG")

        if not config_data.get("vlanConfig", {}).get("items"):
            self.log("No VLAN configuration items found in API response", "DEBUG")
            return config_data

        # Define system default VLANs that should be excluded
        default_vlans = {
            1: ["default"],
            1002: ["fddi-default"],
            1003: ["token-ring-default", "trcrf-default"],
            1004: ["fddinet-default"],
            1005: ["trnet-default", "trbrf-default"],
        }

        original_vlans = config_data["vlanConfig"]["items"]
        self.log("Original VLANs count: {0}".format(len(original_vlans)), "DEBUG")

        filtered_vlans = []
        excluded_count = 0

        # First pass: Filter out system default VLANs
        for vlan in original_vlans:
            vlan_id = vlan.get("vlanId")
            vlan_name = vlan.get("name")

            # Check if this VLAN should be excluded (system default)
            if vlan_id in default_vlans and vlan_name in default_vlans[vlan_id]:
                excluded_count += 1
                continue

            filtered_vlans.append(vlan)

        self.log(
            "Excluded {0} system default VLANs from {1} total VLANs".format(
                excluded_count, len(original_vlans)
            ),
            "INFO",
        )

        # Second pass: Apply user-specified VLAN ID filters if any
        vlan_filters = component_specific_filters.get("vlans", {})
        vlan_ids_list = vlan_filters.get("vlan_ids_list", [])

        if vlan_ids_list:
            self.log(
                "Applying user-specified VLAN ID filters: {0}".format(vlan_ids_list),
                "DEBUG",
            )
            user_filtered_vlans = []
            for vlan in filtered_vlans:
                vlan_id = vlan.get("vlanId")
                if str(vlan_id) in vlan_ids_list:
                    user_filtered_vlans.append(vlan)

            if user_filtered_vlans:
                filtered_config = config_data.copy()
                filtered_config["vlanConfig"]["items"] = user_filtered_vlans
                self.log(
                    "User filtering: {0} out of {1} VLANs match criteria".format(
                        len(user_filtered_vlans), len(filtered_vlans)
                    ),
                    "DEBUG",
                )
                return filtered_config
            else:
                self.log("No VLANs match the user-specified filter criteria", "DEBUG")
                return {}
        else:
            # No user filters, return with only system defaults removed
            if filtered_vlans:
                filtered_config = config_data.copy()
                filtered_config["vlanConfig"]["items"] = filtered_vlans
                self.log(
                    "Returning {0} VLANs after filtering out system defaults".format(
                        len(filtered_vlans)
                    ),
                    "DEBUG",
                )
                return filtered_config
            else:
                self.log(
                    "All VLANs were system defaults - no VLANs remaining after filtering",
                    "DEBUG",
                )
                return {}

    def apply_port_configuration_filters(
        self, merged_interface_configs, component_specific_filters
    ):
        """
        Applies component-specific filters to merged port configurations based on interface names.
        Args:
            merged_interface_configs (list): List of merged interface configurations.
            component_specific_filters (dict): Dictionary containing filters for port configuration.
        Returns:
            list: Filtered list of interface configurations matching the specified criteria.
        """
        self.log("Starting port configuration filtering process", "DEBUG")
        self.log(
            "Input configurations count: {0}".format(len(merged_interface_configs)),
            "DEBUG",
        )

        if not merged_interface_configs:
            self.log("No interface configurations to filter", "DEBUG")
            return []

        if not component_specific_filters:
            self.log(
                "No component-specific filters provided - returning all configurations",
                "DEBUG",
            )
            return merged_interface_configs

        self.log(
            "Extracting port configuration filters from component-specific filters",
            "DEBUG",
        )

        # Fix: Look for port_configuration filters in the correct nested structure
        layer2_config_filters = component_specific_filters.get(
            "layer2_configurations", {}
        )
        port_config_filters = layer2_config_filters.get("port_configuration", {})

        if not port_config_filters:
            self.log(
                "No port configuration filters found in layer2_configurations - returning all configurations",
                "DEBUG",
            )
            return merged_interface_configs

        interface_names_list = port_config_filters.get("interface_names_list", [])

        if not interface_names_list:
            self.log(
                "No interface names filter provided - returning all configurations",
                "DEBUG",
            )
            return merged_interface_configs

        self.log(
            "Filtering interfaces based on interface names list: {0}".format(
                interface_names_list
            ),
            "INFO",
        )
        self.log(
            "Interface names filter contains {0} entries".format(
                len(interface_names_list)
            ),
            "DEBUG",
        )

        filtered_configs = []

        for config_index, interface_config in enumerate(merged_interface_configs):
            interface_name = interface_config.get("interface_name")
            self.log(
                "Evaluating interface {0} of {1}: '{2}'".format(
                    config_index + 1, len(merged_interface_configs), interface_name
                ),
                "DEBUG",
            )

            if interface_name in interface_names_list:
                self.log(
                    "Interface '{0}' matches filter criteria - including in results".format(
                        interface_name
                    ),
                    "DEBUG",
                )
                filtered_configs.append(interface_config)
            else:
                self.log(
                    "Interface '{0}' does not match filter criteria - excluding from results".format(
                        interface_name
                    ),
                    "DEBUG",
                )

        self.log("Port configuration filtering completed", "INFO")
        self.log(
            "Filtered result: {0} out of {1} interfaces match the criteria".format(
                len(filtered_configs), len(merged_interface_configs)
            ),
            "INFO",
        )

        if filtered_configs:
            filtered_interface_names = [
                config.get("interface_name") for config in filtered_configs
            ]
            self.log(
                "Filtered interfaces: {0}".format(filtered_interface_names), "INFO"
            )
        else:
            self.log("No interfaces matched the filter criteria", "WARNING")

        return filtered_configs

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        Args:
            yaml_config_generator (dict): Contains file_path, global_filters, and component_specific_filters.
        Returns:
            self: The current instance with the operation result and message updated.
        """
        self.log(
            "Initializing YAML configuration generation process with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log(
                "Auto-discovery mode enabled - will process all devices and all features",
                "INFO",
            )

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No file_path provided by user, generating default filename", "DEBUG"
            )
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log(
            "YAML configuration file path determined: {0}".format(file_path), "DEBUG"
        )

        self.log("Initializing filter dictionaries", "DEBUG")
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log(
                "Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features",
                "INFO",
            )
            if yaml_config_generator.get("global_filters"):
                self.log(
                    "Warning: global_filters provided but will be ignored due to generate_all_configurations=True",
                    "WARNING",
                )
            if yaml_config_generator.get("component_specific_filters"):
                self.log(
                    "Warning: component_specific_filters provided but will be ignored due to generate_all_configurations=True",
                    "WARNING",
                )

            # Set empty filters to retrieve everything
            global_filters = {}
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = (
                yaml_config_generator.get("component_specific_filters") or {}
            )

        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        self.log("Determining components list for processing", "DEBUG")
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )
        self.log("Components to process: {0}".format(components_list), "DEBUG")

        self.log(
            "Initializing final configuration list and operation summary tracking",
            "DEBUG",
        )
        final_list = []
        consolidated_operation_summary = {
            "total_devices_processed": 0,
            "total_features_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "devices_with_complete_success": [],
            "devices_with_partial_success": [],
            "devices_with_complete_failure": [],
            "success_details": [],
            "failure_details": [],
        }

        for component in components_list:
            self.log("Processing component: {0}".format(component), "DEBUG")
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Component {0} not supported by module, skipping processing".format(
                        component
                    ),
                    "WARNING",
                )
                continue

            self.log("Preparing component-specific filter configuration", "DEBUG")
            component_filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters,
            }

            self.log(
                "Executing component operation function to retrieve details", "DEBUG"
            )
            operation_func = network_element.get("get_function_name")
            details = operation_func(network_element, component_filters)
            self.log(
                "Details retrieved for component {0}: configurations count = {1}".format(
                    component, len(details.get("layer2_configurations", []))
                ),
                "DEBUG",
            )

            if details and details.get("layer2_configurations"):
                self.log(
                    "Adding {0} configurations from component {1} to final list".format(
                        len(details["layer2_configurations"]), component
                    ),
                    "DEBUG",
                )
                final_list.extend(details["layer2_configurations"])

            self.log("Consolidating operation summary from component results", "DEBUG")
            if details and details.get("operation_summary"):
                summary = details["operation_summary"]
                self.log("Processing operation summary consolidation", "DEBUG")

                consolidated_operation_summary["total_devices_processed"] = max(
                    consolidated_operation_summary["total_devices_processed"],
                    summary.get("total_devices_processed", 0),
                )
                consolidated_operation_summary[
                    "total_features_processed"
                ] += summary.get("total_features_processed", 0)
                consolidated_operation_summary[
                    "total_successful_operations"
                ] += summary.get("total_successful_operations", 0)
                consolidated_operation_summary[
                    "total_failed_operations"
                ] += summary.get("total_failed_operations", 0)

                self.log("Merging device lists while avoiding duplicates", "DEBUG")
                for key in [
                    "devices_with_complete_success",
                    "devices_with_partial_success",
                    "devices_with_complete_failure",
                ]:
                    devices = summary.get(key, [])
                    for device in devices:
                        if device not in consolidated_operation_summary[key]:
                            consolidated_operation_summary[key].append(device)

                self.log("Extending operation detail lists", "DEBUG")
                consolidated_operation_summary["success_details"].extend(
                    summary.get("success_details", [])
                )
                consolidated_operation_summary["failure_details"].extend(
                    summary.get("failure_details", [])
                )

        self.log("Creating final dictionary structure with operation summary", "DEBUG")
        final_dict = OrderedDict()
        final_dict["config"] = final_list

        if not final_list:
            self.log(
                "No configurations found to process, setting appropriate result",
                "WARNING",
            )
            self.msg = {
                "message": "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                    self.module_name
                ),
                "operation_summary": consolidated_operation_summary,
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        self.log(
            "Final dictionary created successfully with {0} configurations".format(
                len(final_list)
            ),
            "DEBUG",
        )
        self.log(
            "Consolidated operation summary: {0} total successful operations, {1} total failed operations".format(
                consolidated_operation_summary["total_successful_operations"],
                consolidated_operation_summary["total_failed_operations"],
            ),
            "INFO",
        )

        # Determine if operation should be considered failed based on partial or complete failures
        has_partial_failures = (
            len(consolidated_operation_summary["devices_with_partial_success"]) > 0
        )
        has_complete_failures = (
            len(consolidated_operation_summary["devices_with_complete_failure"]) > 0
        )
        has_any_failures = consolidated_operation_summary["total_failed_operations"] > 0

        self.log(
            "Evaluating operation status - Partial failures: {0}, Complete failures: {1}, Total failed operations: {2}".format(
                has_partial_failures,
                has_complete_failures,
                consolidated_operation_summary["total_failed_operations"],
            ),
            "DEBUG",
        )

        self.log("Attempting to write final dictionary to YAML file", "DEBUG")
        if self.write_dict_to_yaml(final_dict, file_path):
            self.log("YAML file write operation completed successfully", "INFO")

            # Determine final operation status
            if has_partial_failures or has_complete_failures or has_any_failures:
                self.log(
                    "Operation contains failures - setting final status to failed",
                    "WARNING",
                )
                self.msg = {
                    "message": "YAML config generation completed with failures for module '{0}'. Check operation_summary for details.".format(
                        self.module_name
                    ),
                    "file_path": file_path,
                    "configurations_generated": len(final_list),
                    "operation_summary": consolidated_operation_summary,
                }
                self.set_operation_result("failed", True, self.msg, "ERROR")
            else:
                self.log("Operation completed successfully without failures", "INFO")
                self.msg = {
                    "message": "YAML config generation succeeded for module '{0}'.".format(
                        self.module_name
                    ),
                    "file_path": file_path,
                    "configurations_generated": len(final_list),
                    "operation_summary": consolidated_operation_summary,
                }
                self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.log("YAML file write operation failed", "ERROR")
            self.msg = {
                "message": "YAML config generation failed for module '{0}' - unable to write to file.".format(
                    self.module_name
                ),
                "file_path": file_path,
                "operation_summary": consolidated_operation_summary,
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        self.log("YAML configuration generation process completed", "DEBUG")
        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        This method prepares the parameters required for adding, updating, or deleting
        network configurations such as SSIDs and interfaces in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.
        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('gathered').
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        # Set generate_all_configurations after validation
        self.generate_all_configurations = config.get(
            "generate_all_configurations", False
        )
        self.log(
            "Set generate_all_configurations mode: {0}".format(
                self.generate_all_configurations
            ),
            "DEBUG",
        )

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator added to want: {0}".format(
                want["yaml_config_generator"]
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Wireless Design operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the merge operations for various network configurations in the Cisco Catalyst Center.
        This method processes additions and updates for SSIDs, interfaces, power profiles, access point profiles,
        radio frequency profiles, and anchor groups. It logs detailed information about each operation,
        updates the result status, and returns a consolidated result.
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
                operation_func(params).check_return_status()
            else:
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
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_wired_campus_automation_playbook_generator = (
        WiredCampusAutomationPlaybookGenerator(module)
    )
    if (
        ccc_wired_campus_automation_playbook_generator.compare_dnac_versions(
            ccc_wired_campus_automation_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_wired_campus_automation_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for <module_name_caps> Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_wired_campus_automation_playbook_generator.get_ccc_version()
            )
        )
        ccc_wired_campus_automation_playbook_generator.set_operation_result(
            "failed", False, ccc_wired_campus_automation_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_wired_campus_automation_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_wired_campus_automation_playbook_generator.supported_states:
        ccc_wired_campus_automation_playbook_generator.status = "invalid"
        ccc_wired_campus_automation_playbook_generator.msg = (
            "State {0} is invalid".format(state)
        )
        ccc_wired_campus_automation_playbook_generator.check_recturn_status()

    # Validate the input parameters and check the return statusk
    ccc_wired_campus_automation_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_wired_campus_automation_playbook_generator.validated_config:
        ccc_wired_campus_automation_playbook_generator.reset_values()
        ccc_wired_campus_automation_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_wired_campus_automation_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_wired_campus_automation_playbook_generator.result)


if __name__ == "__main__":
    main()

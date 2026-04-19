#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module for brownfield YAML playbook generation of SDA host port onboarding configurations.

This module automates the extraction of SDA host port onboarding configurations from Cisco
Catalyst Center infrastructure, transforming them into YAML playbooks compatible
with sda_host_port_onboarding_workflow_manager module. It retrieves port assignments,
port channels, and wireless SSID configurations via REST APIs, applies optional fabric
site-based filters for targeted extraction, resolves device IDs to management IP addresses,
and generates formatted YAML files for configuration documentation, port onboarding auditing,
disaster recovery, and multi-fabric deployment standardization workflows.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Vivek Raj, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: sda_host_port_onboarding_playbook_config_generator
short_description: Generate YAML configurations playbook for 'sda_host_port_onboarding_workflow_manager' module.
description:
- Automates brownfield YAML playbook generation for SDA host port onboarding
  configurations deployed in Cisco Catalyst Center infrastructure.
- Extracts port assignments, port channels, and wireless SSID configurations
  via REST APIs for fabric sites managed in SDA environments.
- Generates YAML files compatible with sda_host_port_onboarding_workflow_manager
  module for configuration documentation, port onboarding auditing, disaster
  recovery, and multi-fabric deployment standardization.
- Supports auto-discovery mode for complete fabric infrastructure extraction
  or component-based filtering for targeted extraction (port assignments,
  port channels, wireless SSIDs).
- Transforms camelCase API responses to snake_case YAML format with comprehensive
  header comments and metadata.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Vivek Raj (@vivekraj2000)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - Desired state for YAML playbook generation workflow.
    - Only 'gathered' state supported for brownfield SDA host port onboarding extraction.
    type: str
    choices: [gathered]
    default: gathered
  file_path:
    description:
    - Absolute or relative path for YAML configuration file output.
    - If not provided, generates default filename in current working directory
        with pattern
        'sda_host_port_onboarding_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml'
    - Example default filename
        'sda_host_port_onboarding_playbook_config_2026-02-27_14-31-46.yml'
    - Directory created automatically if path does not exist.
    - Supports YAML file extension (.yml or .yaml).
    type: str
  file_mode:
    description:
    - Controls how config is written to the YAML file.
    - C(overwrite) replaces existing file content.
    - C(append) appends generated YAML content to the existing file.
    type: str
    choices: ["overwrite", "append"]
    default: "overwrite"
  config:
    description:
    - A dictionary of filters for generating YAML playbook compatible with the `sda_host_port_onboarding_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    - If config is not provided or is empty, all configurations for all port assignments, port channels
      and wireless SSIDs will be generated.
    - This is useful for complete brownfield infrastructure discovery and documentation.
    type: dict
    required: false
    suboptions:
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration
          file.
        - If "components_list" is specified, only those components are included,
          regardless of other filters.
        - If filters for specific components (e.g., port_assignments, port_channels, or wireless_ssids)
          are provided without explicitly including them in components_list, those components will be
          automatically added to components_list.
        - At least one of components_list or component filters must be provided.
        type: dict
        suboptions:
          components_list:
            description:
            - List of SDA host port onboarding components to include in YAML configuration.
            - Valid values are 'port_assignments' for interface port assignments,
              'port_channels' for port channel configurations, and 'wireless_ssids'
              for wireless SSID mappings to VLANs within fabric sites.
            - If specified, only the listed components will be included in the generated YAML file.
            - If not specified but component filters (port_assignments, port_channels, or wireless_ssids)
              are provided, those components are automatically added to this list.
            - If neither components_list nor any component filters are provided, an error will be raised.
            type: list
            choices: ["port_assignments", "port_channels", "wireless_ssids"]
            elements: str
          port_assignments:
            description:
            - Filters for port channel configuration
              extraction.
            - Each list entry targets one fabric site with
              optional device-level filtering by management
              IP address, serial number, or hostname.
            - Extracts only port assignments for specified
              fabric site hierarchies and optionally only
              for devices matching the specified device_ips,
              serial_numbers, or hostnames within those
              sites.
            - When multiple device filters (device_ips,
              serial_numbers, hostnames) are specified in
              the same list entry, they are combined using
              AND logic. A device must match ALL specified
              filters to be included.
            - Each filter type is optional and independent.
              Omitting a filter type means no restriction
              on that attribute.
            - Fabric site names must be full hierarchical
              paths (case-sensitive).
            - If not specified when component included in
              components_list, extracts all port assignments
              across all fabric sites and all devices.
            type: list
            elements: dict
            required: false
            suboptions:
              fabric_site_name_hierarchy:
                description:
                - Fabric site hierarchical paths to extract port assignments.
                - Site names must match exact hierarchical paths in Catalyst Center
                  (case-sensitive).
                - Extracts port assignments for all devices within specified fabric sites.
                - For example, "Global/USA/San Jose/Building1"
                type: str
                required: false
              device_ips:
                description:
                - List of device management IP addresses to
                  filter extraction within this fabric site.
                - Each IP is matched against the
                  managementIpAddress field resolved from
                  Catalyst Center for each device in the
                  fabric site.
                - Devices whose management IP does not match
                  any IP in this list are skipped.
                - Combined with serial_numbers and hostnames
                  using AND logic when multiple filter types
                  are specified in the same list entry. A
                  device must satisfy all specified filters
                  to be included.
                - Scoped per list entry. Each fabric site
                  entry can specify its own set of device
                  IPs independently.
                - If omitted, no IP-based filtering is
                  applied and all devices in the fabric
                  site are candidates (subject to other
                  filters).
                - For example, ["1.1.1.1", "1.1.1.2"]
                type: list
                elements: str
                required: false
              serial_numbers:
                description:
                - List of device serial numbers to filter
                  extraction within this fabric site.
                - Each serial number is matched against the
                  serialNumber field resolved from Catalyst
                  Center for each device in the fabric site.
                - Devices whose serial number does not match
                  any value in this list are skipped.
                - Combined with device_ips and hostnames
                  using AND logic when multiple filter types
                  are specified in the same list entry. A
                  device must satisfy all specified filters
                  to be included.
                - Scoped per list entry. Each fabric site
                  entry can specify its own set of serial
                  numbers independently.
                - If omitted, no serial number-based
                  filtering is applied and all devices in
                  the fabric site are candidates (subject
                  to other filters).
                - For example, ["FJC2327U0S2", "FJC2327U0S3"]
                type: list
                elements: str
                required: false
              hostnames:
                description:
                - List of device hostnames to filter
                  extraction within this fabric site.
                - Each hostname is matched against the
                  hostname field resolved from Catalyst
                  Center for each device in the fabric site.
                - Devices whose hostname does not match any
                  value in this list are skipped.
                - Combined with device_ips and serial_numbers
                  using AND logic when multiple filter types
                  are specified in the same list entry. A
                  device must satisfy all specified filters
                  to be included.
                - Scoped per list entry. Each fabric site
                  entry can specify its own set of hostnames
                  independently.
                - If omitted, no hostname-based filtering is
                  applied and all devices in the fabric site
                  are candidates (subject to other filters).
                - For example, ["switch1", "switch2"]
                type: list
                elements: str
                required: false
          port_channels:
            description:
            - Filters for port channel configuration
              extraction.
            - Each list entry targets one fabric site with
              optional device-level filtering by management
              IP address, serial number, or hostname.
            - Extracts only port channels for specified
              fabric site hierarchies and optionally only
              for devices matching the specified device_ips,
              serial_numbers, or hostnames within those
              sites.
            - When multiple device filters (device_ips,
              serial_numbers, hostnames) are specified in
              the same list entry, they are combined using
              AND logic. A device must match ALL specified
              filters to be included.
            - Each filter type is optional and independent.
              Omitting a filter type means no restriction
              on that attribute.
            - Fabric site names must be full hierarchical
              paths (case-sensitive).
            - If not specified when component included in
              components_list, extracts all port channels
              across all fabric sites and all devices.
            type: list
            elements: dict
            required: false
            suboptions:
              fabric_site_name_hierarchy:
                description:
                - Fabric site hierarchical paths to extract port channels.
                - Site names must match exact hierarchical paths in Catalyst Center
                  (case-sensitive).
                - Extracts port channel configurations for all devices within specified fabric sites.
                - For example, "Global/USA/San Jose/Building1"
                type: str
                required: false
              device_ips:
                description:
                - List of device management IP addresses to
                  filter extraction within this fabric site.
                - Each IP is matched against the
                  managementIpAddress field resolved from
                  Catalyst Center for each device in the
                  fabric site.
                - Devices whose management IP does not match
                  any IP in this list are skipped.
                - Combined with serial_numbers and hostnames
                  using AND logic when multiple filter types
                  are specified in the same list entry. A
                  device must satisfy all specified filters
                  to be included.
                - Scoped per list entry. Each fabric site
                  entry can specify its own set of device
                  IPs independently.
                - If omitted, no IP-based filtering is
                  applied and all devices in the fabric
                  site are candidates (subject to other
                  filters).
                - For example, ["1.1.1.1", "1.1.1.2"]
                type: list
                elements: str
                required: false
              serial_numbers:
                description:
                - List of device serial numbers to filter
                  extraction within this fabric site.
                - Each serial number is matched against the
                  serialNumber field resolved from Catalyst
                  Center for each device in the fabric site.
                - Devices whose serial number does not match
                  any value in this list are skipped.
                - Combined with device_ips and hostnames
                  using AND logic when multiple filter types
                  are specified in the same list entry. A
                  device must satisfy all specified filters
                  to be included.
                - Scoped per list entry. Each fabric site
                  entry can specify its own set of serial
                  numbers independently.
                - If omitted, no serial number-based
                  filtering is applied and all devices in
                  the fabric site are candidates (subject
                  to other filters).
                - For example, ["FJC2327U0S2", "FJC2327U0S3"]
                type: list
                elements: str
                required: false
              hostnames:
                description:
                - List of device hostnames to filter
                  extraction within this fabric site.
                - Each hostname is matched against the
                  hostname field resolved from Catalyst
                  Center for each device in the fabric site.
                - Devices whose hostname does not match any
                  value in this list are skipped.
                - Combined with device_ips and serial_numbers
                  using AND logic when multiple filter types
                  are specified in the same list entry. A
                  device must satisfy all specified filters
                  to be included.
                - Scoped per list entry. Each fabric site
                  entry can specify its own set of hostnames
                  independently.
                - If omitted, no hostname-based filtering is
                  applied and all devices in the fabric site
                  are candidates (subject to other filters).
                - For example, ["switch1", "switch2"]
                type: list
                elements: str
                required: false
          wireless_ssids:
            description:
            - Filters for wireless SSID configuration extraction.
            - Extracts only wireless SSID to VLAN mappings for specified fabric site hierarchies.
            - Fabric site names must be full hierarchical paths (case-sensitive).
            - If not specified when component included in components_list, extracts
              all wireless SSID mappings across all fabric sites.
            type: dict
            required: false
            suboptions:
              fabric_site_name_hierarchy:
                description:
                - List of fabric site hierarchical paths to extract wireless SSID mappings.
                - Site names must match exact hierarchical paths in Catalyst Center
                  (case-sensitive).
                - Extracts VLAN to SSID mappings for specified fabric sites.
                - For example, ["Global/USA/San Jose/Building1", "Global/USA/RTP/Building2"]
                type: list
                elements: str
                required: false

requirements:
- dnacentersdk >= 2.3.7.9
- python >= 3.9
- PyYAML >= 5.1
notes:
  - SDK methods utilized - sda.get_port_assignments, sda.get_port_channels,
    fabric_wireless.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site,
    devices.get_device_by_id, sda.get_fabric_sites
  - API paths utilized - GET /dna/intent/api/v1/sda/portAssignments,
    GET /dna/intent/api/v1/sda/portChannels,
    GET /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids
    GET /dna/intent/api/v1/network-device/{id}
    GET /dna/intent/api/v1/sda/fabricSites
  - Module is idempotent; multiple runs generate identical YAML content except
    timestamp in header comments.
  - Check mode supported; validates parameters without file generation.
  - Device management IP addresses are resolved from device IDs for all port
    configurations enabling device-specific port onboarding playbooks.
  - Generated YAML uses OrderedDumper for consistent key ordering enabling version
    control.
  - Fabric site hierarchical paths must match exact Catalyst Center fabric site structure.
  - 'Auto-population of components_list:
    If component-specific filters (such as port_assignments, port_channels, or wireless_ssids) are provided
    without explicitly including them in components_list, those components will be
    automatically added to components_list. This simplifies configuration by eliminating
    the need to redundantly specify components in both places.'
  - 'Example of auto-population behavior:
    If you provide filters for port_assignments without including port_assignments in components_list,
    the module will automatically add port_assignments to components_list before processing.
    This allows you to write more concise playbooks.'
  - 'Validation requirements:
    If component_specific_filters is provided, at least one of the following must be true -
    (1) components_list contains at least one component, OR
    (2) Component-specific filters (e.g., port_assignments, port_channels, wireless_ssids) are provided.
    If neither condition is met, the module will fail with a validation error.'
seealso:
- module: cisco.dnac.sda_host_port_onboarding_workflow_manager
  description: Module for managing SDA host port onboarding workflows in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML playbook for host port onboarding workflow manager
    which includes all fabric sites's host port onboarding details
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_mode: "overwrite"

- name: Generate YAML Configuration with File Path specified
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"

- name: Generate YAML with multiple fabric sites and per-site device IP filtering
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["port_assignments", "port_channels"]
        port_assignments:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            device_ips:
              - 1.1.1.1
          - fabric_site_name_hierarchy: "Global/USA/RTP/Building2"
        port_channels:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            device_ips:
              - 1.1.1.1

- name: Generate YAML Configuration with specific component port assignments filters
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["port_assignments"]
        port_assignments:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            device_ips:
              - 1.1.1.1
              - 1.1.1.2

- name: Generate YAML Configuration with specific component port assignments filters
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["port_assignments"]
        port_assignments:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            serial_numbers:
              - FJC27251Z8B
              - FJC27251Z8C

- name: Generate YAML Configuration with specific component port assignments filters
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["port_assignments"]
        port_assignments:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            hostnames:
              - switch1
              - switch2

- name: Generate YAML Configuration with specific component port channels filters
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["port_channels"]
        port_channels:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            device_ips:
              - 1.1.1.1
              - 1.1.1.2

- name: Generate YAML Configuration with specific component port channels filters
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["port_channels"]
        port_channels:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            serial_numbers:
              - FJC27251Z8B
              - FJC27251Z8C

- name: Generate YAML Configuration with specific component port channels filters
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["port_channels"]
        port_channels:
          - fabric_site_name_hierarchy: "Global/Site_India/Karnataka/Bangalore"
            hostnames:
              - switch1
              - switch2

- name: Generate YAML with AND-combined device filters per site
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list:
          - "port_assignments"
          - "port_channels"
        port_assignments:
          # Site 1: AND filter — device must match IP AND hostname
          - fabric_site_name_hierarchy: "Global/USA/San Jose/Building1"
            device_ips:
              - 1.1.1.1
            hostnames:
              - switch1
          # Site 2: single filter — only serial number filtering
          - fabric_site_name_hierarchy: "Global/USA/RTP/Building2"
            serial_numbers:
              - FJC2327U0S2
              - FJC2327U0S3
          # Site 3: no device filter — extracts all devices
          - fabric_site_name_hierarchy: "Global/India/Bangalore/Building3"
        port_channels:
          - fabric_site_name_hierarchy: "Global/USA/San Jose/Building1"
            device_ips:
              - 1.1.1.1

- name: Generate YAML Configuration with specific component wireless ssids filters
  cisco.dnac.sda_host_port_onboarding_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    file_path: "host_onboarding_playbook.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["wireless_ssids"]
        wireless_ssids:
          fabric_site_name_hierarchy:
            - "Global/Site_India/Karnataka/Bangalore"
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
            "components_processed": 1,
            "components_skipped": 0,
            "configurations_count": 1,
            "file_path": "host_onboarding_playbook.yml",
            "message": "YAML configuration file generated successfully for module 'sda_host_port_onboarding_workflow_manager'",
            "status": "success"
        },
        "response": {
            "components_processed": 1,
            "components_skipped": 0,
            "configurations_count": 1,
            "file_path": "host_onboarding_playbook.yml",
            "message": "YAML configuration file generated successfully for module 'sda_host_port_onboarding_workflow_manager'",
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
            "Validation Error: component_specific_filters is provided but no components are specified.
             Either provide 'components_list' with at least one component, or provide filters for specific components.",
        "response":
            "Validation Error: component_specific_filters is provided but no components are specified.
             Either provide 'components_list' with at least one component, or provide filters for specific components."
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
            """
            Represent an OrderedDict as a YAML mapping while preserving insertion order.

            Args:
                data (OrderedDict): The OrderedDict to represent in YAML format.

            Returns:
                MappingNode: YAML mapping node with preserved key ordering.
            """
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class SdaHostPortOnboardingPlaybookConfigGenerator(DnacBase, BrownFieldHelper):
    """
    Brownfield playbook generator for Cisco Catalyst Center SDA host port onboarding.

    This class orchestrates automated YAML playbook generation for SDA host port
    onboarding configurations by extracting existing settings from Cisco Catalyst
    Center via REST APIs and transforming them into Ansible playbooks compatible with
    the sda_host_port_onboarding_workflow_manager module.

    The generator supports both auto-discovery mode (extracting all fabric site
    configurations for port assignments, port channels, and wireless SSIDs) and targeted
    extraction mode (filtering by fabric site hierarchies) to facilitate brownfield SDA
    infrastructure documentation, configuration backup, migration planning, and
    multi-fabric deployment standardization workflows.

    Key Capabilities:
    - Extracts three configuration types (port assignments, port channels, wireless
      SSIDs) with fabric site hierarchy-based filtering from SDA infrastructure
    - Retrieves device-specific port configurations and resolves device IDs to
      management IP addresses for device-based port onboarding
    - Groups configurations by fabric site and network device for organized playbook
      structure enabling device-specific deployment
    - Generates YAML files with comprehensive header comments including metadata,
      generation timestamp, configuration summary statistics, and usage instructions
    - Transforms camelCase API response keys to snake_case YAML format for improved
      playbook readability and maintainability
    - Supports per-fabric wireless SSID to VLAN mappings for wireless infrastructure
      documentation

    Inheritance:
        DnacBase: Provides Cisco Catalyst Center API connectivity, authentication,
                  request execution, logging infrastructure, and common utility methods
        BrownFieldHelper: Provides parameter transformation utilities, reverse mapping
                         functions, and configuration processing helpers for brownfield
                         operations including modify_parameters() and YAML generation

    Class-Level Attributes:
        supported_states (list): List of supported Ansible states, currently
                                ['gathered'] for configuration extraction workflow
        module_schema (dict): Network elements schema configuration mapping API
                             families, functions, filters, and reverse mapping
                             specifications for SDA host port onboarding components
        fabric_site_id_to_name_mapping (dict): Cached mapping of fabric site UUIDs to
                                        hierarchical site names from Catalyst Center
                                        for fabric site name resolution
        module_name (str): Target workflow manager module name for generated playbooks
                          ('sda_host_port_onboarding_workflow_manager')
        values_to_nullify (list): List of string values to treat as None during
                                 processing (e.g., ['NOT CONFIGURED'])

    Workflow Execution:
        1. validate_input() - Validates playbook configuration parameters and filters
        2. get_want() - Constructs desired state parameters from validated configuration
        3. get_diff_gathered() - Orchestrates YAML generation workflow execution
        4. yaml_config_generator() - Generates YAML file with header and configurations
        5. get_port_assignments_configuration() - Retrieves port assignment configs
        6. get_port_channels_configuration() - Retrieves port channel configs
        7. get_wireless_ssids_configuration() - Retrieves wireless SSID to VLAN mappings
        8. write_dict_to_yaml() - Writes formatted YAML with header comments to file

    Error Handling:
        - Comprehensive parameter validation with detailed error messages
        - API exception handling with error tracking and logging
        - File I/O error handling with fallback messaging and status reporting
        - Component-specific filter validation preventing invalid configurations
        - Device ID resolution validation with warnings for missing devices

    Version Requirements:
        - Cisco Catalyst Center: 2.3.7.9 or higher
        - dnacentersdk: 2.3.7.9 or higher
        - Python: 3.9 or higher
        - PyYAML: 5.1 or higher (for YAML serialization with OrderedDumper)

    Notes:
        - The class is idempotent; multiple runs with same parameters generate
          identical YAML content (except generation timestamp in header comments)
        - Check mode is supported but does not perform actual file generation;
          validates parameters and returns expected operation results
        - Large-scale deployments with many fabric sites and devices may require
          increased dnac_api_task_timeout values for complete data extraction
        - Generated YAML files use OrderedDumper for consistent key ordering across
          multiple generations enabling reliable version control
        - Fabric site hierarchical paths are case-sensitive and must match exact
          fabric site names configured in Catalyst Center
        - Port assignments and port channels are grouped by device for efficient
          device-specific port onboarding workflows

    See Also:
        sda_host_port_onboarding_workflow_manager: Target module for applying generated
                                                  SDA host port onboarding configurations
                                                  to Catalyst Center instances
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
        self.module_schema = self.get_workflow_filters_schema()
        self.fabric_site_name_to_id_mapping, self.fabric_site_id_to_name_mapping = self.get_fabric_site_name_to_id_mapping()
        self.module_name = "sda_host_port_onboarding_workflow_manager"

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
            self.validated_config = {"generate_all_configurations": True}
            self.msg = "Configuration is not provided or empty - treating as generate_all_configurations mode"
            self.log(self.msg, "INFO")
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "component_specific_filters": {
                "type": "dict",
                "required": False
            }
        }

        # Validate params
        self.log("Validating configuration against schema.", "DEBUG")

        valid_temp = self.validate_config_dict(self.config, temp_spec)
        self.log(
            "Schema validation passed successfully. All parameters conform to expected "
            "types and structure. Total valid entries: {0}.".format(len(valid_temp)),
            "DEBUG"
        )

        self.log("Validating invalid parameters against provided config", "DEBUG")
        self.validate_invalid_params(self.config, temp_spec.keys())

        # Auto-populate components_list from component filters and validate
        component_specific_filters = valid_temp.get("component_specific_filters")
        if component_specific_filters:
            self.auto_populate_and_validate_components_list(component_specific_filters)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = f"Successfully validated playbook configuration parameters using 'validated_input': {str(valid_temp)}"
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_filters_schema(self):
        """
        Constructs and returns comprehensive workflow filters schema for SDA host port onboarding.

        This method defines the complete mapping structure between network components
        (port assignments, port channels, wireless SSIDs) and their associated API
        operations, filter parameters, and reverse mapping specifications for YAML
        playbook generation.

        The schema serves as the central configuration mapping that drives brownfield
        extraction workflow by defining component-specific API families, function names,
        supported filters, and reverse mapping functions for transforming API responses
        to YAML format.

        Returns:
            dict: Nested dictionary containing two main sections:
                - network_elements (dict): Component configurations with keys:
                    * port_assignments (dict): Port assignment extraction configuration
                        - filters (list): ['fabric_site_name_hierarchy']
                        - reverse_mapping_function (method): port_assignments_temp_spec
                        - api_function (str): 'get_port_assignments'
                        - api_family (str): 'sda'
                        - get_function_name (method): get_port_assignments_configuration
                    * port_channels (dict): Port channel extraction configuration
                        - filters (list): ['fabric_site_name_hierarchy']
                        - reverse_mapping_function (method): port_channels_temp_spec
                        - api_function (str): 'get_port_channels'
                        - api_family (str): 'sda'
                        - get_function_name (method): get_port_channels_configuration
                    * wireless_ssids (dict): Wireless SSID extraction configuration
                        - filters (list): ['fabric_site_name_hierarchy']
                        - reverse_mapping_function (method): wireless_ssids_temp_spec
                        - api_function (str): 'retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site'
                        - api_family (str): 'fabric_wireless'
                        - get_function_name (method): get_wireless_ssids_configuration

        Component Configuration Details:
            Each network element configuration contains five key mappings:
            1. filters: List of supported filter keys for targeted extraction
            2. reverse_mapping_function: Method reference returning OrderedDict spec
               for transforming camelCase API responses to snake_case YAML format
            3. api_function: SDK function name for retrieving component data
            4. api_family: SDK API family category ('sda' or 'fabric_wireless')
            5. get_function_name: Method reference for component retrieval logic

        Usage Context:
            - Called during __init__() to initialize self.module_schema attribute
            - Used by get_want() to determine which network element retrievers to invoke
            - Referenced by yaml_config_generator() for filter validation and processing
            - Provides metadata for component-specific configuration transformation

        Filter Capabilities:
            - fabric_site_name_hierarchy: Filters configurations by fabric site paths
              (e.g., ['Global/USA/San Jose/Building1', 'Global/USA/RTP/Building2'])
            - All filters are optional; omission results in retrieval of all
              configurations across all fabric sites for that component type

        Workflow Integration:
            The schema enables dynamic workflow execution where:
            1. User specifies components_list in component_specific_filters
            2. get_want() validates components against schema keys
            3. For each component, retrieves api_family, api_function, filters
            4. Invokes get_function_name with network_element config and filters
            5. Applies reverse_mapping_function to transform API responses to YAML

        Notes:
            - Schema is immutable during instance lifetime; modifications require restart
            - All API functions assumed to be accessible via self.dnac._exec()
            - Reverse mapping functions must return OrderedDict for consistent key ordering
            - get_function_name methods must accept (network_element, filters) parameters
        """
        return {
            "network_elements": {
                "port_assignments": {
                    "filters": ["fabric_site_name_hierarchy"],
                    "reverse_mapping_function": self.port_assignments_temp_spec,
                    "api_function": "get_port_assignments",
                    "api_family": "sda",
                    "get_function_name": self.get_port_assignments_configuration,
                },
                "port_channels": {
                    "filters": ["fabric_site_name_hierarchy"],
                    "reverse_mapping_function": self.port_channels_temp_spec,
                    "api_function": "get_port_channels",
                    "api_family": "sda",
                    "get_function_name": self.get_port_channels_configuration,
                },
                "wireless_ssids": {
                    "filters": ["fabric_site_name_hierarchy"],
                    "reverse_mapping_function": self.wireless_ssids_temp_spec,
                    "api_function": "retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site",
                    "api_family": "fabric_wireless",
                    "get_function_name": self.get_wireless_ssids_configuration,
                },
            }
        }

    def get_fabric_site_names_and_device_details_mapping(self, component_specific_filters):
        """
        Extracts fabric site name hierarchies and per-site device detail
        mappings from component-specific filter entries.

        Iterates over each filter entry in the provided
        component_specific_filters list, collecting fabric site hierarchical
        names into an ordered list and building dictionaries that map each
        fabric site name to sets of device management IP addresses, serial
        numbers, and hostnames specified for that site.

        Downstream filtering applies AND logic across filter types: when
        multiple device filter types (device_ips, serial_numbers, hostnames)
        are specified for the same fabric site, a device must match ALL
        specified filter types to be included. Each individual filter type
        uses OR logic within its own set (e.g., management IP must match
        ANY IP in device_ips). Omitting a filter type means no restriction
        on that attribute.

        Filter evaluation order: device_ips → serial_numbers → hostnames.
        A device that fails any filter is skipped immediately via 'continue'
        without evaluating subsequent filters.

        Args:
            component_specific_filters (list[dict]): List of filter dictionaries, each
                containing:
                - fabric_site_name_hierarchy (str): Full hierarchical path of the fabric
                  site in Catalyst Center (e.g., 'Global/USA/San Jose/Building1').
                - device_ips (list[str], optional): List of device management IP addresses
                  to filter extraction within the fabric site. Defaults to an empty list
                  if not provided, indicating no IP-based filtering for that site.
                - serial_numbers (list[str], optional): List of device serial numbers
                  to filter extraction within the fabric site. Defaults to an empty list
                  if not provided, indicating no serial number-based filtering for that site.
                - hostnames (list[str], optional): List of device hostnames to filter
                  extraction within the fabric site. Defaults to an empty list if not
                  provided, indicating no hostname-based filtering for that site.

        Returns:
            tuple: A four-element tuple containing:
                - fabric_site_name_hierarchies (list[str]): Ordered list of fabric site
                  hierarchical names extracted from the filter entries, preserving the
                  input order.
                - fabric_site_name_device_ip_mapping (dict[str, set[str]]): Dictionary
                  mapping each fabric site hierarchical name to a set of device management
                  IP addresses. An empty set indicates no IP-based device filtering for
                  that site.
                - fabric_site_name_serial_number_mapping (dict[str, set[str]]): Dictionary
                  mapping each fabric site hierarchical name to a set of device serial
                  numbers. An empty set indicates no serial number-based device filtering
                  for that site.
                - fabric_site_name_hostname_mapping (dict[str, set[str]]): Dictionary
                  mapping each fabric site hierarchical name to a set of device hostnames.
                  An empty set indicates no hostname-based device filtering for that site.
        """
        self.log(
            "Extracting fabric site name hierarchies and device detail mappings from "
            "component-specific filters for targeted configuration extraction. This process "
            "enables downstream methods to apply precise fabric site and device-based "
            "filtering during API data retrieval and transformation workflows.",
            "DEBUG"
        )
        fabric_site_name_hierarchies = []
        fabric_site_name_device_ip_mapping = {}
        fabric_site_name_serial_number_mapping = {}
        fabric_site_name_hostname_mapping = {}

        for filter_index, filter_item in enumerate(component_specific_filters, start=1):
            fabric_site_name = filter_item.get("fabric_site_name_hierarchy")
            device_ips = filter_item.get("device_ips", [])
            serial_numbers = filter_item.get("serial_numbers", [])
            hostnames = filter_item.get("hostnames", [])
            self.log(
                f"Processing filter {filter_index}/{len(component_specific_filters)} — "
                f"fabric_site_name_hierarchy='{fabric_site_name}', device_ips={device_ips}, "
                f"serial_numbers={serial_numbers}, hostnames={hostnames}.",
                "DEBUG"
            )
            fabric_site_name_hierarchies.append(fabric_site_name)
            fabric_site_name_device_ip_mapping[fabric_site_name] = set(device_ips)
            fabric_site_name_serial_number_mapping[fabric_site_name] = set(serial_numbers)
            fabric_site_name_hostname_mapping[fabric_site_name] = set(hostnames)

        self.log(
            f"Completed extraction of fabric site name hierarchies and device detail mappings. "
            f"Extracted {len(fabric_site_name_hierarchies)} fabric site name hierarchy filter(s). "
            f"Fabric site name to device IP mapping: {fabric_site_name_device_ip_mapping}. "
            f"Fabric site name to serial number mapping: {fabric_site_name_serial_number_mapping}. "
            f"Fabric site name to hostname mapping: {fabric_site_name_hostname_mapping}.",
            "DEBUG"
        )

        return fabric_site_name_hierarchies, fabric_site_name_device_ip_mapping, fabric_site_name_serial_number_mapping, fabric_site_name_hostname_mapping

    def get_port_assignments_configuration(self, network_element, filters):
        """
        Retrieves and transforms port assignment configurations from Catalyst Center.

        This function orchestrates port assignment retrieval by querying all port
        assignments via API, applying optional fabric site filters for targeted
        selection, grouping assignments by fabric and network device, resolving
        device IDs to management IP addresses, and transforming API response format
        to user-friendly YAML structure.

        Args:
            network_element (dict): Network element configuration containing:
                                - api_family (str): SDK API family name (e.g., 'sda')
                                - api_function (str): SDK function name
                                    (e.g., 'get_port_assignments')
            filters (dict): Filter configuration containing:
                        - component_specific_filters (dict, optional): Nested filters
                            for fabric site selection:
                            - fabric_site_name_hierarchy (list): List of fabric site
                                hierarchical names to process

        Returns:
            list: List of dictionaries, one per device with structure:
                - ip_address (str): Device management IP address
                - fabric_site_name_hierarchy (str): Fabric site hierarchical name
                - port_assignments (list): List of port assignment configurations
        """
        self.log(
            "Starting port assignments configuration retrieval and transformation "
            "workflow. Workflow includes API query for all port assignments, optional "
            "fabric site filtering, device grouping, IP address resolution, and YAML "
            "structure transformation.",
            "DEBUG"
        )

        self.log(
            f"Extracting component_specific_filters from filters dictionary: {filters}. "
            "Filters determine which fabric sites to process for port assignment "
            "retrieval.",
            "DEBUG"
        )
        component_specific_filters = filters.get("component_specific_filters")
        if component_specific_filters:
            self.log(
                "Component-specific filters found with fabric site filters. "
                "Will apply fabric_site_name_hierarchy filtering to port assignments.",
                "DEBUG"
            )
        else:
            self.log(
                "No component_specific_filters provided. Will retrieve port assignments "
                "for all fabric sites without filtering.",
                "DEBUG"
            )
        self.log(f"component_specific_filters for port assignments: {component_specific_filters}", "DEBUG")

        self.log(
            "Extracting API family and function from network_element configuration "
            "for port assignments retrieval.",
            "DEBUG"
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            f"API configuration extracted - family: {api_family}, function: {api_function}. "
            f"Executing API call to retrieve all port assignments from Catalyst Center.",
            "DEBUG"
        )

        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
        except Exception as e:
            self.log(f"Failed to retrieve port assignments using {api_family}.{api_function}: {e}", "ERROR")
            raise RuntimeError(
                f"Port assignments API call failed for {api_family}.{api_function}: {e}"
            ) from e

        all_port_assignments = response.get("response", [])
        self.log(
            f"Port assignments API call completed successfully. Retrieved {len(all_port_assignments)} port assignment(s) from Catalyst Center.",
            "INFO"
        )

        self.log(
            "Initializing data structures for port assignment processing. "
            "all_fabric_port_assignments_details will contain final transformed data, "
            "fabric_ids will store target fabric site IDs.",
            "DEBUG"
        )
        all_fabric_port_assignments_details = []
        fabric_ids = []

        self.log(
            "Determining fabric site IDs to process based on filter presence. "
            "Building fabric_ids list from filters or using all cached fabric sites.",
            "DEBUG"
        )

        fabric_site_name_device_ip_mapping = {}
        fabric_site_name_serial_number_mapping = {}
        fabric_site_name_hostname_mapping = {}

        if component_specific_filters:
            self.log(
                "Building fabric name to site ID mapping from cached "
                "fabric_site_id_to_name_mapping for filter-based fabric ID resolution.",
                "DEBUG"
            )
            (
                fabric_site_name_hierarchies,
                fabric_site_name_device_ip_mapping,
                fabric_site_name_serial_number_mapping,
                fabric_site_name_hostname_mapping
            ) = self.get_fabric_site_names_and_device_details_mapping(component_specific_filters)

            self.log(
                f"Extracted {len(fabric_site_name_hierarchies)} fabric site name "
                "hierarchy filter(s) from component_specific_filters: "
                f"{fabric_site_name_hierarchies}. Resolving to fabric site IDs.",
                "DEBUG"
            )

            for hierarchy_index, fabric_site_name_hierarchy in enumerate(fabric_site_name_hierarchies, start=1):
                self.log(
                    f"Resolving fabric site name hierarchy {hierarchy_index}/"
                    f"{len(fabric_site_name_hierarchies)}: "
                    f"'{fabric_site_name_hierarchy}' for port assignments.",
                    "DEBUG"
                )
                fabric_id = self.fabric_site_name_to_id_mapping.get(fabric_site_name_hierarchy)
                if not fabric_id:
                    self.log(
                        f"Warning: Fabric site name '{fabric_site_name_hierarchy}' "
                        f"(hierarchy {hierarchy_index}/"
                        f"{len(fabric_site_name_hierarchies)}) not found in cached "
                        "mapping. Skipping this fabric site for port assignments.",
                        "WARNING"
                    )
                    continue
                fabric_ids.append(fabric_id)
                self.log(
                    f"Resolved fabric site name '{fabric_site_name_hierarchy}' "
                    f"(hierarchy {hierarchy_index}/"
                    f"{len(fabric_site_name_hierarchies)}) to fabric ID "
                    f"'{fabric_id}'. Added to port assignments processing list.",
                    "DEBUG"
                )
        else:
            self.log(
                "No fabric site filters provided. Using all "
                f"{len(self.fabric_site_id_to_name_mapping)} cached fabric site IDs for "
                "complete port assignment retrieval.",
                "DEBUG"
            )
            fabric_ids = list(self.fabric_site_id_to_name_mapping.keys())

        self.log(
            f"Fabric site ID resolution completed. Will process {len(fabric_ids)} fabric site(s): {fabric_ids}.",
            "INFO"
        )

        self.log(
            f"Grouping {len(all_port_assignments)} port assignment(s) by fabric ID for organized processing. Building fabric_port_assignments_dict.",
            "DEBUG"
        )
        # Group port assignments by fabric_id
        # Convert to set for O(1) membership checks
        fabric_ids_set = set(fabric_ids)
        fabric_port_assignments_dict = {}
        for port_assignment_index, port_assignment in enumerate(all_port_assignments, start=1):
            fabric_id = port_assignment.get("fabricId")
            self.log(
                f"Processing port assignment {port_assignment_index}/{len(all_port_assignments)} with fabric ID '{fabric_id}'.",
                "DEBUG"
            )
            if fabric_id in fabric_ids_set:
                self.log(
                    f"Fabric ID '{fabric_id}' matches filter criteria. Adding port "
                    f"assignment {port_assignment_index}/"
                    f"{len(all_port_assignments)} to fabric group.",
                    "DEBUG"
                )
                if fabric_id not in fabric_port_assignments_dict:
                    fabric_port_assignments_dict[fabric_id] = []
                fabric_port_assignments_dict[fabric_id].append(port_assignment)
            else:
                self.log(
                    f"Fabric ID '{fabric_id}' does not match filter criteria. Skipping port assignment {port_assignment_index}/{len(all_port_assignments)}.",
                    "DEBUG"
                )

        # Process each fabric's port assignments
        self.log(
            f"Starting fabric site iteration loop. Processing {len(fabric_port_assignments_dict)} fabric site(s) with port assignments.",
            "DEBUG"
        )

        for fabric_index, (fabric_id, port_assignments) in enumerate(fabric_port_assignments_dict.items(), start=1):
            self.log(
                f"Processing fabric site {fabric_index}/"
                f"{len(fabric_port_assignments_dict)} with ID '{fabric_id}'. "
                f"Contains {len(port_assignments)} port assignment(s).",
                "DEBUG"
            )

            self.log(
                "Retrieving reverse mapping specification for port assignments "
                "transformation. Specification defines field mappings and YAML structure.",
                "DEBUG"
            )
            port_assignments_temp_spec = self.port_assignments_temp_spec()

            self.log(
                "Applying reverse mapping transformation to "
                f"{len(port_assignments)} port assignment(s) using "
                "modify_parameters(). Transformation converts API format to "
                "user-friendly YAML structure.",
                "DEBUG"
            )
            modified_port_assignments = self.modify_parameters(
                port_assignments_temp_spec, port_assignments
            )
            self.log(
                f"Reverse mapping transformation completed for {len(modified_port_assignments)} port assignment(s).",
                "DEBUG"
            )

            # Group port assignments by network device
            self.log(
                f"Grouping {len(port_assignments)} port assignment(s) by network device ID for device-based organization.",
                "DEBUG"
            )
            device_port_assignments = {}
            for idx, port_assignment in enumerate(port_assignments):
                network_device_id = port_assignment.get("networkDeviceId")
                self.log(
                    f"Processing port assignment {idx + 1}/{len(port_assignments)} "
                    f"for network device ID '{network_device_id}' in fabric ID "
                    f"'{fabric_id}'.",
                    "DEBUG"
                )
                if network_device_id not in device_port_assignments:
                    device_port_assignments[network_device_id] = []
                    self.log(
                        f"Initialized new device group for network device ID "
                        f"'{network_device_id}' in port assignments grouping.",
                        "DEBUG"
                    )
                device_port_assignments[network_device_id].append(modified_port_assignments[idx])
                self.log(
                    f"Added port assignment {idx + 1} to device group. Device ID "
                    f"'{network_device_id}' now has "
                    f"{len(device_port_assignments[network_device_id])} port "
                    "assignment(s).",
                    "DEBUG"
                )

            # Build the final structure with device IP addresses
            self.log(
                f"Building final device configuration structures with management IP address resolution for {len(device_port_assignments)} device(s).",
                "DEBUG"
            )
            for device_index, (network_device_id, device_ports) in enumerate(device_port_assignments.items(), start=1):
                self.log(
                    f"Processing device {device_index}/{len(device_port_assignments)} "
                    f"with ID '{network_device_id}'. Fetching device details to "
                    "resolve management IP address.",
                    "DEBUG"
                )
                # Get device details to fetch management IP address
                try:
                    device_response = self.dnac._exec(
                        family="devices",
                        function="get_device_by_id",
                        op_modifies=False,
                        params={"id": network_device_id},
                    )
                except Exception as e:
                    self.log(f"Failed to resolve device details for device ID '{network_device_id}': {e}", "ERROR")
                    raise RuntimeError(
                        f"Device lookup failed for device ID '{network_device_id}': {e}"
                    ) from e
                self.log(f"Device details response for device ID {network_device_id}: {device_response}", "DEBUG")
                device_info = device_response.get("response", {})
                management_ip = device_info.get("managementIpAddress", "")
                serial_number = device_info.get("serialNumber", "")
                hostname = device_info.get("hostname", "")
                fabric_site_name = self.fabric_site_id_to_name_mapping.get(fabric_id)

                # ----------------------------------------------------------
                # Device filter evaluation (AND logic across filter types).
                # The device must pass ALL specified filters to be included.
                # Evaluation order: device_ips → serial_numbers → hostnames.
                # Within each filter type, matching is OR (any value match).
                # Omitted/empty filter type → no restriction on that attribute.
                # ----------------------------------------------------------

                if fabric_site_name_device_ip_mapping:
                    expected_ips = fabric_site_name_device_ip_mapping.get(fabric_site_name, set())
                    if expected_ips and management_ip not in expected_ips:
                        self.log(
                            f"Warning: Resolved management IP '{management_ip}' for "
                            f"device ID '{network_device_id}' does not match expected "
                            f"IPs {expected_ips} from filters for fabric site "
                            f"'{fabric_site_name}'.",
                            "DEBUG"
                        )
                        continue

                if fabric_site_name_serial_number_mapping:
                    expected_serials = fabric_site_name_serial_number_mapping.get(fabric_site_name, set())
                    if expected_serials and serial_number not in expected_serials:
                        self.log(
                            f"Warning: Resolved serial number '{serial_number}' for "
                            f"device ID '{network_device_id}' does not match expected "
                            f"serial numbers {expected_serials} from filters for "
                            f"fabric site '{fabric_site_name}'.",
                            "DEBUG"
                        )
                        continue

                if fabric_site_name_hostname_mapping:
                    expected_hostnames = fabric_site_name_hostname_mapping.get(fabric_site_name, set())
                    if expected_hostnames and hostname not in expected_hostnames:
                        self.log(
                            f"Warning: Resolved hostname '{hostname}' for device ID "
                            f"'{network_device_id}' does not match expected hostnames "
                            f"{expected_hostnames} from filters for fabric site "
                            f"'{fabric_site_name}'.",
                            "DEBUG"
                        )
                        continue

                self.log(
                    f"Resolved device ID '{network_device_id}' to management IP address '{management_ip}'.",
                    "DEBUG"
                )

                device_dict = {
                    'ip_address': management_ip,
                    'fabric_site_name_hierarchy': fabric_site_name,
                    'port_assignments': device_ports
                }
                all_fabric_port_assignments_details.append(device_dict)
                self.log(
                    f"Added device configuration to final list. Device IP: "
                    f"{management_ip}, Fabric: "
                    f"{fabric_site_name}, Port "
                    f"assignments: {len(device_ports)}.",
                    "DEBUG"
                )

        self.log(
            "Port assignments configuration retrieval completed successfully. "
            f"Retrieved {len(all_fabric_port_assignments_details)} device "
            "configuration(s) with port assignments.",
            "INFO"
        )
        return all_fabric_port_assignments_details

    def get_port_channels_configuration(self, network_element, filters):
        """
        Retrieves and transforms port channel configurations from Catalyst Center.

        This function orchestrates port channel retrieval by querying all port
        channels via API, applying optional fabric site filters for targeted
        selection, grouping channels by fabric and network device, resolving
        device IDs to management IP addresses, and transforming API response format
        to user-friendly YAML structure.

        Args:
            network_element (dict): Network element configuration containing:
                                - api_family (str): SDK API family name (e.g., 'sda')
                                - api_function (str): SDK function name
                                    (e.g., 'get_port_channels')
            filters (dict): Filter configuration containing:
                        - component_specific_filters (dict, optional): Nested filters
                            for fabric site selection:
                            - fabric_site_name_hierarchy (list): List of fabric site
                                hierarchical names to process

        Returns:
            list: List of dictionaries, one per device with structure:
                - ip_address (str): Device management IP address
                - fabric_site_name_hierarchy (str): Fabric site hierarchical name
                - port_channels (list): List of port channel configurations
        """
        self.log(
            "Starting port channels configuration retrieval and transformation "
            "workflow. Workflow includes API query for all port channels, optional "
            "fabric site filtering, device grouping, IP address resolution, and YAML "
            "structure transformation.",
            "DEBUG"
        )

        self.log(
            f"Extracting component_specific_filters from filters dictionary: {filters}. "
            "Filters determine which fabric sites to process for port channel retrieval.",
            "DEBUG"
        )
        component_specific_filters = filters.get("component_specific_filters")
        if component_specific_filters:
            self.log(
                "Component-specific filters found with fabric site filters. "
                "Will apply fabric_site_name_hierarchy filtering to port channels.",
                "DEBUG"
            )
        else:
            self.log(
                "No component_specific_filters provided. Will retrieve port channels "
                "for all fabric sites without filtering.",
                "DEBUG"
            )
        self.log(f"component_specific_filters for port channels: {component_specific_filters}", "DEBUG")

        self.log(
            "Extracting API family and function from network_element configuration "
            "for port channels retrieval.",
            "DEBUG"
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            f"API configuration extracted - family: {api_family}, function: "
            f"{api_function}. Executing API call to retrieve all port channels "
            "from Catalyst Center.",
            "DEBUG"
        )

        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
        except Exception as e:
            self.log(f"Failed to retrieve port channels using {api_family}.{api_function}: {e}", "ERROR")
            raise RuntimeError(
                f"Port channels API call failed for {api_family}.{api_function}: {e}"
            ) from e

        all_port_channels = response.get("response", [])
        self.log(
            f"Port channels API call completed successfully. Retrieved {len(all_port_channels)} port channel(s) from Catalyst Center.",
            "INFO"
        )

        self.log(
            "Initializing data structures for port channel processing. "
            "all_fabric_port_channels_details will contain final transformed data, "
            "fabric_ids will store target fabric site IDs.",
            "DEBUG"
        )
        all_fabric_port_channels_details = []
        fabric_ids = []

        self.log(
            "Determining fabric site IDs to process based on filter presence. "
            "Building fabric_ids list from filters or using all cached fabric sites.",
            "DEBUG"
        )

        fabric_site_name_device_ip_mapping = {}
        fabric_site_name_serial_number_mapping = {}
        fabric_site_name_hostname_mapping = {}

        if component_specific_filters:
            self.log(
                "Building fabric name to site ID mapping from cached "
                "fabric_site_id_to_name_mapping for filter-based fabric ID resolution.",
                "DEBUG"
            )
            (
                fabric_site_name_hierarchies,
                fabric_site_name_device_ip_mapping,
                fabric_site_name_serial_number_mapping,
                fabric_site_name_hostname_mapping
            ) = self.get_fabric_site_names_and_device_details_mapping(component_specific_filters)

            self.log(
                f"Extracted {len(fabric_site_name_hierarchies)} fabric site name "
                "hierarchy filter(s) from component_specific_filters: "
                f"{fabric_site_name_hierarchies}. Resolving to fabric site IDs.",
                "DEBUG"
            )

            for hierarchy_index, fabric_site_name_hierarchy in enumerate(fabric_site_name_hierarchies, start=1):
                self.log(
                    f"Resolving fabric site name hierarchy {hierarchy_index}/"
                    f"{len(fabric_site_name_hierarchies)}: "
                    f"'{fabric_site_name_hierarchy}' for port channels.",
                    "DEBUG"
                )
                fabric_id = self.fabric_site_name_to_id_mapping.get(fabric_site_name_hierarchy)
                if not fabric_id:
                    self.log(
                        f"Warning: Fabric site name '{fabric_site_name_hierarchy}' "
                        f"(hierarchy {hierarchy_index}/"
                        f"{len(fabric_site_name_hierarchies)}) not found in cached "
                        "mapping. Skipping this fabric site for port channels.",
                        "WARNING"
                    )
                    continue
                fabric_ids.append(fabric_id)
                self.log(
                    f"Resolved fabric site name '{fabric_site_name_hierarchy}' "
                    f"(hierarchy {hierarchy_index}/"
                    f"{len(fabric_site_name_hierarchies)}) to fabric ID "
                    f"'{fabric_id}'. Added to port channels processing list.",
                    "DEBUG"
                )
        else:
            self.log(
                f"No fabric site filters provided. Using all {len(self.fabric_site_id_to_name_mapping)} "
                f"cached fabric site IDs for complete port channel retrieval.",
                "DEBUG"
            )
            fabric_ids = list(self.fabric_site_id_to_name_mapping.keys())

        self.log(
            f"Fabric site ID resolution completed. Will process {len(fabric_ids)} fabric site(s): {fabric_ids}.",
            "INFO"
        )

        self.log(
            f"Grouping {len(all_port_channels)} port channel(s) by fabric ID for organized processing. Building fabric_port_channels_dict.",
            "DEBUG"
        )
        # Group port channels by fabric_id
        # Convert to set for O(1) membership checks
        fabric_ids_set = set(fabric_ids)
        fabric_port_channels_dict = {}
        for port_channel_index, port_channel in enumerate(all_port_channels, start=1):
            fabric_id = port_channel.get("fabricId")
            self.log(
                f"Processing port channel {port_channel_index}/{len(all_port_channels)} with fabric ID '{fabric_id}'.",
                "DEBUG"
            )
            if fabric_id in fabric_ids_set:
                self.log(
                    f"Fabric ID '{fabric_id}' matches filter criteria. Adding port channel {port_channel_index}/{len(all_port_channels)} to fabric group.",
                    "DEBUG"
                )
                if fabric_id not in fabric_port_channels_dict:
                    fabric_port_channels_dict[fabric_id] = []
                fabric_port_channels_dict[fabric_id].append(port_channel)
            else:
                self.log(
                    f"Fabric ID '{fabric_id}' does not match filter criteria. Skipping port channel {port_channel_index}/{len(all_port_channels)}.",
                    "DEBUG"
                )

        # Process each fabric's port channels
        self.log(
            f"Starting fabric site iteration loop. Processing {len(fabric_port_channels_dict)} fabric site(s) with port channels.",
            "DEBUG"
        )

        for fabric_index, (fabric_id, port_channels) in enumerate(fabric_port_channels_dict.items(), start=1):
            self.log(
                f"Processing fabric site {fabric_index}/"
                f"{len(fabric_port_channels_dict)} with ID '{fabric_id}'. "
                f"Contains {len(port_channels)} port channel(s).",
                "DEBUG"
            )

            self.log(
                "Retrieving reverse mapping specification for port channels "
                "transformation. Specification defines field mappings and YAML structure.",
                "DEBUG"
            )
            port_channels_temp_spec = self.port_channels_temp_spec()

            self.log(
                "Applying reverse mapping transformation to "
                f"{len(port_channels)} port channel(s) using modify_parameters(). "
                "Transformation converts API format to user-friendly YAML structure.",
                "DEBUG"
            )
            modified_port_channels = self.modify_parameters(
                port_channels_temp_spec, port_channels
            )
            self.log(
                f"Reverse mapping transformation completed for {len(modified_port_channels)} port channel(s).",
                "DEBUG"
            )

            # Group port channels by network device
            self.log(
                f"Grouping {len(port_channels)} port channel(s) by network device ID for device-based organization.",
                "DEBUG"
            )
            device_port_channels = {}
            for idx, port_channel in enumerate(port_channels):
                network_device_id = port_channel.get("networkDeviceId")
                self.log(
                    f"Processing port channel {idx + 1}/{len(port_channels)} "
                    f"for network device ID '{network_device_id}' in fabric ID "
                    f"'{fabric_id}'.",
                    "DEBUG"
                )
                if network_device_id not in device_port_channels:
                    device_port_channels[network_device_id] = []
                    self.log(
                        f"Initialized new device group for network device ID "
                        f"'{network_device_id}' in port channels grouping.",
                        "DEBUG"
                    )
                device_port_channels[network_device_id].append(modified_port_channels[idx])
                self.log(
                    f"Added port channel {idx + 1} to device group. Device ID "
                    f"'{network_device_id}' now has "
                    f"{len(device_port_channels[network_device_id])} port "
                    "channel(s).",
                    "DEBUG"
                )

            # Build the final structure with device IP addresses
            self.log(
                f"Building final device configuration structures with management IP address resolution for {len(device_port_channels)} device(s).",
                "DEBUG"
            )
            for device_index, (network_device_id, device_port_channels_list) in enumerate(device_port_channels.items(), start=1):
                self.log(
                    f"Processing device {device_index}/{len(device_port_channels)} "
                    f"with ID '{network_device_id}'. Fetching device details to "
                    "resolve management IP address.",
                    "DEBUG"
                )
                # Get device details to fetch management IP address
                try:
                    device_response = self.dnac._exec(
                        family="devices",
                        function="get_device_by_id",
                        op_modifies=False,
                        params={"id": network_device_id},
                    )
                except Exception as e:
                    self.log(f"Failed to resolve device details for device ID '{network_device_id}': {e}", "ERROR")
                    raise RuntimeError(
                        f"Device lookup failed for device ID '{network_device_id}': {e}"
                    ) from e
                self.log(
                    f"Device API response received for device ID '{network_device_id}'.",
                    "DEBUG"
                )
                device_info = device_response.get("response", {})
                management_ip = device_info.get("managementIpAddress", "")
                serial_number = device_info.get("serialNumber", "")
                hostname = device_info.get("hostname", "")
                fabric_site_name = self.fabric_site_id_to_name_mapping.get(fabric_id)

                # ----------------------------------------------------------
                # Device filter evaluation (AND logic across filter types).
                # The device must pass ALL specified filters to be included.
                # Evaluation order: device_ips → serial_numbers → hostnames.
                # Within each filter type, matching is OR (any value match).
                # Omitted/empty filter type → no restriction on that attribute.
                # ----------------------------------------------------------

                if fabric_site_name_device_ip_mapping:
                    expected_ips = fabric_site_name_device_ip_mapping.get(fabric_site_name, set())
                    if expected_ips and management_ip not in expected_ips:
                        self.log(
                            f"Warning: Resolved management IP '{management_ip}' for "
                            f"device ID '{network_device_id}' does not match expected "
                            f"IPs {expected_ips} from filters for fabric site "
                            f"'{fabric_site_name}'.",
                            "DEBUG"
                        )
                        continue

                if fabric_site_name_serial_number_mapping:
                    expected_serials = fabric_site_name_serial_number_mapping.get(fabric_site_name, set())
                    if expected_serials and serial_number not in expected_serials:
                        self.log(
                            f"Warning: Resolved serial number '{serial_number}' for "
                            f"device ID '{network_device_id}' does not match expected "
                            f"serial numbers {expected_serials} from filters for "
                            f"fabric site '{fabric_site_name}'.",
                            "DEBUG"
                        )
                        continue

                if fabric_site_name_hostname_mapping:
                    expected_hostnames = fabric_site_name_hostname_mapping.get(fabric_site_name, set())
                    if expected_hostnames and hostname not in expected_hostnames:
                        self.log(
                            f"Warning: Resolved hostname '{hostname}' for device ID "
                            f"'{network_device_id}' does not match expected hostnames "
                            f"{expected_hostnames} from filters for fabric site "
                            f"'{fabric_site_name}'.",
                            "DEBUG"
                        )
                        continue

                self.log(
                    f"Resolved device ID '{network_device_id}' to management IP address '{management_ip}'.",
                    "DEBUG"
                )

                device_dict = {
                    'ip_address': management_ip,
                    'fabric_site_name_hierarchy': fabric_site_name,
                    'port_channels': device_port_channels_list
                }
                all_fabric_port_channels_details.append(device_dict)
                self.log(
                    "Added device configuration to final list. Device IP: "
                    f"{management_ip}, Fabric: "
                    f"{fabric_site_name}, Port channels: "
                    f"{len(device_port_channels_list)}.",
                    "DEBUG"
                )

        self.log(
            "Port channels configuration retrieval completed successfully. "
            f"Retrieved {len(all_fabric_port_channels_details)} device "
            "configuration(s) with port channels.",
            "INFO"
        )
        return all_fabric_port_channels_details

    def get_wireless_ssids_configuration(self, network_element, filters):
        """
        Retrieves and transforms wireless SSID configurations from Catalyst Center.

        This function orchestrates wireless SSID retrieval by querying VLAN and SSID
        mappings for each fabric site via API, applying optional fabric site filters
        for targeted selection, transforming API response format to user-friendly YAML
        structure with VLAN and SSID details.

        Args:
            network_element (dict): Network element configuration containing:
                                - api_family (str): SDK API family name
                                    (e.g., 'fabric_wireless')
                                - api_function (str): SDK function name (e.g.,
                                    'retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site')
            filters (dict): Filter configuration containing:
                        - component_specific_filters (dict, optional): Nested filters
                            for fabric site selection:
                            - fabric_site_name_hierarchy (list): List of fabric site
                                hierarchical names to process

        Returns:
            list: List of dictionaries, one per fabric site with structure:
                - fabric_site_name_hierarchy (str): Fabric site hierarchical name
                - wireless_ssids (list): List of VLAN and SSID mapping configurations
        """
        self.log(
            "Starting wireless SSIDs configuration retrieval and transformation "
            "workflow. Workflow includes per-fabric API queries for VLAN/SSID mappings, "
            "optional fabric site filtering, and YAML structure transformation.",
            "DEBUG"
        )

        self.log(
            f"Extracting component_specific_filters from filters dictionary: {filters}. "
            "Filters determine which fabric sites to process for wireless SSID "
            "retrieval.",
            "DEBUG"
        )
        component_specific_filters = filters.get("component_specific_filters")
        if component_specific_filters:
            self.log(
                "Component-specific filters found with fabric site filters. "
                "Will apply fabric_site_name_hierarchy filtering to wireless SSIDs.",
                "DEBUG"
            )
        else:
            self.log(
                "No component_specific_filters provided. Will retrieve wireless SSIDs "
                "for all fabric sites without filtering.",
                "DEBUG"
            )

        self.log(
            "Extracting API family and function from network_element configuration "
            "for wireless SSIDs retrieval.",
            "DEBUG"
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            f"API configuration extracted - family: {api_family}, function: {api_function}. Will execute per-fabric API calls to retrieve VLAN/SSID mappings.",
            "DEBUG"
        )

        self.log(
            "Initializing data structures for wireless SSID processing. "
            "all_fabric_wireless_ssids_details will contain final transformed data, "
            "fabric_ids will store target fabric site IDs.",
            "DEBUG"
        )
        all_fabric_wireless_ssids_details = []
        fabric_ids = []

        self.log(
            "Determining fabric site IDs to process based on filter presence. "
            "Building fabric_ids list from filters or using all cached fabric sites.",
            "DEBUG"
        )
        if component_specific_filters:
            self.log(
                "Building fabric name to site ID mapping from cached "
                "fabric_site_id_to_name_mapping for filter-based fabric ID resolution.",
                "DEBUG"
            )

            fabric_site_name_hierarchies = component_specific_filters.get("fabric_site_name_hierarchy", [])
            self.log(
                f"Extracted {len(fabric_site_name_hierarchies)} fabric site name "
                "hierarchy filter(s) from component_specific_filters: "
                f"{fabric_site_name_hierarchies}. Resolving to fabric site IDs.",
                "DEBUG"
            )

            for hierarchy_index, fabric_site_name_hierarchy in enumerate(fabric_site_name_hierarchies, start=1):
                self.log(
                    f"Resolving fabric site name hierarchy {hierarchy_index}/"
                    f"{len(fabric_site_name_hierarchies)}: "
                    f"'{fabric_site_name_hierarchy}' for wireless SSIDs.",
                    "DEBUG"
                )
                fabric_id = self.fabric_site_name_to_id_mapping.get(fabric_site_name_hierarchy)
                if not fabric_id:
                    self.log(
                        f"Warning: Fabric site name '{fabric_site_name_hierarchy}' "
                        f"(hierarchy {hierarchy_index}/"
                        f"{len(fabric_site_name_hierarchies)}) not found in cached "
                        "mapping. Skipping this fabric site for wireless SSIDs.",
                        "WARNING"
                    )
                    continue
                fabric_ids.append(fabric_id)
                self.log(
                    f"Resolved fabric site name '{fabric_site_name_hierarchy}' "
                    f"(hierarchy {hierarchy_index}/"
                    f"{len(fabric_site_name_hierarchies)}) to fabric ID "
                    f"'{fabric_id}'. Added to wireless SSIDs processing list.",
                    "DEBUG"
                )
        else:
            self.log(
                f"No fabric site filters provided. Using all {len(self.fabric_site_id_to_name_mapping)} "
                f"cached fabric site IDs for complete wireless SSID retrieval.",
                "DEBUG"
            )
            fabric_ids = list(self.fabric_site_id_to_name_mapping.keys())

        self.log(
            f"Fabric site ID resolution completed. Will process {len(fabric_ids)} fabric site(s): {fabric_ids}.",
            "INFO"
        )

        self.log(
            f"Starting fabric site iteration loop for per-fabric wireless SSID retrieval. Processing {len(fabric_ids)} fabric site(s).",
            "DEBUG"
        )
        for fabric_index, fabric_id in enumerate(fabric_ids, start=1):
            self.log(
                f"Processing fabric site {fabric_index}/{len(fabric_ids)} with ID '{fabric_id}'. Executing API call to retrieve VLAN/SSID mappings.",
                "DEBUG"
            )
            try:
                response = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    op_modifies=False,
                    params={"fabric_id": fabric_id},
                )
            except Exception as e:
                self.log(f"Failed to retrieve wireless SSIDs for fabric ID '{fabric_id}' using {api_family}.{api_function}: {e}", "ERROR")
                raise RuntimeError(
                    f"Wireless SSIDs API call failed for fabric ID '{fabric_id}': {e}"
                ) from e

            response = response.get("response", [])
            self.log(
                f"Wireless SSID API call completed for fabric ID '{fabric_id}'. Retrieved {len(response)} VLAN/SSID mapping(s).",
                "DEBUG"
            )

            if not response:
                self.log(
                    f"No wireless SSIDs found for fabric ID '{fabric_id}' (fabric "
                    f"name: '{self.fabric_site_id_to_name_mapping.get(fabric_id)}'). "
                    "Skipping this fabric site.",
                    "WARNING"
                )
                continue

            self.log(
                "Retrieving reverse mapping specification for wireless SSIDs "
                "transformation. Specification defines field mappings and YAML structure.",
                "DEBUG"
            )
            wireless_ssids_temp_spec = self.wireless_ssids_temp_spec()

            self.log(
                "Applying reverse mapping transformation to "
                f"{len(response)} wireless SSID mapping(s) using "
                "modify_parameters(). Transformation converts API format to "
                "user-friendly YAML structure.",
                "DEBUG"
            )
            wireless_ssids = self.modify_parameters(
                wireless_ssids_temp_spec, response
            )
            self.log(
                f"Reverse mapping transformation completed for {len(wireless_ssids)} wireless SSID mapping(s).",
                "DEBUG"
            )

            modified_wireless_ssids_details = {
                'fabric_site_name_hierarchy': self.fabric_site_id_to_name_mapping.get(fabric_id),
                'wireless_ssids': wireless_ssids
            }
            all_fabric_wireless_ssids_details.append(modified_wireless_ssids_details)
            self.log(
                "Added wireless SSID configuration to final list. Fabric: "
                f"{self.fabric_site_id_to_name_mapping.get(fabric_id)}, Wireless SSIDs: "
                f"{len(wireless_ssids)}.",
                "DEBUG"
            )

        self.log(
            "Wireless SSIDs configuration retrieval completed successfully. "
            f"Retrieved {len(all_fabric_wireless_ssids_details)} fabric site "
            "configuration(s) with wireless SSIDs.",
            "INFO"
        )
        return all_fabric_wireless_ssids_details

    def port_assignments_temp_spec(self):
        """
        Defines comprehensive reverse mapping specification for port assignment configurations.

        This method constructs the transformation schema mapping camelCase API response
        keys from Catalyst Center port assignment endpoints to snake_case YAML playbook
        parameter names. The specification is consumed by modify_parameters() to perform
        field-level transformations during brownfield extraction workflow.

        Returns:
            OrderedDict: Ordered mapping specification with preserved key sequence for
                        consistent YAML generation. Contains nine port assignment
                        parameters:
                - interface_name (str): Maps 'interfaceName' from API response
                - connected_device_type (str): Maps 'connectedDeviceType' from API response
                - data_vlan_name (str): Maps 'dataVlanName' from API response
                - voice_vlan_name (str): Maps 'voiceVlanName' from API response
                - security_group_name (str): Maps 'securityGroupName' from API response
                - authentication_template_name (str): Maps 'authenticateTemplateName'
                  from API response
                - interface_description (str): Maps 'interfaceDescription' from API response
                - native_vlan_id (int): Maps 'nativeVlanId' from API response with type
                  conversion to integer
                - allowed_vlan_ranges (str): Maps 'allowedVlanRanges' from API response

        Specification Structure:
            Each key-value pair defines:
            - Outer key: Target YAML parameter name (snake_case convention)
            - Inner dict: Transformation metadata including:
                * type: Target Python/YAML data type ('str', 'int', 'list', 'dict')
                * source_key: Original API response field name (camelCase)
                * elements (optional): List element type for list-type fields
                * options (optional): Nested specification for dict-type fields

        Usage Context:
            - Referenced in get_workflow_filters_schema() as reverse_mapping_function
              for 'port_assignments' component
            - Invoked by modify_parameters() during API response transformation phase
            - Used by yaml_config_generator() to generate properly formatted port
              assignment configurations in YAML output

        Transformation Process:
            1. API returns port assignment with interfaceName='GigabitEthernet1/0/1'
            2. modify_parameters() applies port_assignments_temp_spec mapping
            3. Field transforms to interface_name='GigabitEthernet1/0/1' in YAML
            4. Process repeats for all nine port assignment parameters

        Parameter Details:
            - interface_name: Physical or logical interface identifier (e.g.,
              'GigabitEthernet1/0/1', 'TenGigabitEthernet1/1/1')
            - connected_device_type: Device category connected to port (e.g.,
              'USER_DEVICE', 'TRUNKING_DEVICE', 'ACCESS_POINT')
            - data_vlan_name: VLAN name for data traffic (e.g., 'Data_VLAN_100')
            - voice_vlan_name: VLAN name for voice traffic (e.g., 'Voice_VLAN_200')
            - security_group_name: Trustsec SGT name for access control
            - authentication_template_name: 802.1X authentication template name
            - interface_description: User-friendly interface description
            - native_vlan_id: Native VLAN identifier for trunk ports (integer)
            - allowed_vlan_ranges: Comma-separated VLAN ranges (e.g., '10-20,30,40-50')

        Notes:
            - OrderedDict ensures consistent YAML key ordering across multiple generations
              enabling reliable version control diff operations
            - Type conversions (e.g., native_vlan_id to int) are handled automatically
              by modify_parameters() based on type field
            - Missing fields in API response are omitted from final YAML (not set to None)
            - Specification is immutable; runtime modifications have no effect on
              transformation behavior
        """
        port_assignments = OrderedDict({
            "interface_name": {"type": "str", "source_key": "interfaceName"},
            "connected_device_type": {"type": "str", "source_key": "connectedDeviceType"},
            "data_vlan_name": {"type": "str", "source_key": "dataVlanName"},
            "voice_vlan_name": {"type": "str", "source_key": "voiceVlanName"},
            "security_group_name": {"type": "str", "source_key": "securityGroupName"},
            "authentication_template_name": {"type": "str", "source_key": "authenticateTemplateName"},
            "interface_description": {"type": "str", "source_key": "interfaceDescription"},
            "native_vlan_id": {"type": "int", "source_key": "nativeVlanId"},
            "allowed_vlan_ranges": {"type": "str", "source_key": "allowedVlanRanges"},
        })
        return port_assignments

    def port_channels_temp_spec(self):
        """
        Defines comprehensive reverse mapping specification for port channel configurations.

        This method constructs the transformation schema mapping camelCase API response
        keys from Catalyst Center port channel endpoints to snake_case YAML playbook
        parameter names. The specification is consumed by modify_parameters() to perform
        field-level transformations during brownfield extraction workflow.

        Returns:
            OrderedDict: Ordered mapping specification with preserved key sequence for
                        consistent YAML generation. Contains six port channel parameters:
                - interface_names (list[str]): Maps 'interfaceNames' from API response with
                  list of interface identifiers
                - connected_device_type (str): Maps 'connectedDeviceType' from API response
                - protocol (str): Maps 'protocol' from API response (e.g., 'LACP', 'PAGP')
                - port_channel_description (str): Maps 'description' from API response
                - native_vlan_id (int): Maps 'nativeVlanId' from API response with type
                  conversion to integer
                - allowed_vlan_ranges (str): Maps 'allowedVlanRanges' from API response

        Specification Structure:
            Each key-value pair defines:
            - Outer key: Target YAML parameter name (snake_case convention)
            - Inner dict: Transformation metadata including:
                * type: Target Python/YAML data type ('str', 'int', 'list', 'dict')
                * source_key: Original API response field name (camelCase)
                * elements (optional): List element type for list-type fields
                * options (optional): Nested specification for dict-type fields

        Usage Context:
            - Referenced in get_workflow_filters_schema() as reverse_mapping_function
              for 'port_channels' component
            - Invoked by modify_parameters() during API response transformation phase
            - Used by yaml_config_generator() to generate properly formatted port channel
              configurations in YAML output

        Transformation Process:
            1. API returns port channel with interfaceNames=['Gi1/0/1', 'Gi1/0/2']
            2. modify_parameters() applies port_channels_temp_spec mapping
            3. Field transforms to interface_names=['Gi1/0/1', 'Gi1/0/2'] in YAML
            4. Process repeats for all six port channel parameters

        Parameter Details:
            - interface_names: List of physical interfaces aggregated into port channel
              (e.g., ['GigabitEthernet1/0/1', 'GigabitEthernet1/0/2'])
            - connected_device_type: Device category connected to port channel (e.g.,
              'TRUNKING_DEVICE', 'EXTENDED_NODE')
            - protocol: Link aggregation protocol ('LACP', 'PAGP', 'ON' for static)
            - port_channel_description: User-friendly description of port channel purpose
            - native_vlan_id: Native VLAN identifier for trunk port channels (integer)
            - allowed_vlan_ranges: Comma-separated VLAN ranges (e.g., '10-20,30,40-50')

        Notes:
            - OrderedDict ensures consistent YAML key ordering across multiple generations
              enabling reliable version control diff operations
            - Type conversions (e.g., native_vlan_id to int) are handled automatically
              by modify_parameters() based on type field
            - List type fields (interface_names) with elements='str' ensure proper YAML
              list formatting with string elements
            - Missing fields in API response are omitted from final YAML (not set to None)
            - Specification is immutable; runtime modifications have no effect on
              transformation behavior
        """
        port_channels = OrderedDict({
            "interface_names": {"type": "list", "elements": "str", "source_key": "interfaceNames"},
            "connected_device_type": {"type": "str", "source_key": "connectedDeviceType"},
            "protocol": {"type": "str", "source_key": "protocol"},
            "port_channel_description": {"type": "str", "source_key": "description"},
            "native_vlan_id": {"type": "int", "source_key": "nativeVlanId"},
            "allowed_vlan_ranges": {"type": "str", "source_key": "allowedVlanRanges"},
        })
        return port_channels

    def wireless_ssids_temp_spec(self):
        """
        Defines comprehensive reverse mapping specification for wireless SSID configurations.

        This method constructs the transformation schema mapping camelCase API response
        keys from Catalyst Center fabric wireless endpoints to snake_case YAML playbook
        parameter names for VLAN to SSID mappings. The specification includes nested
        structure for SSID details with security group mappings.

        Returns:
            OrderedDict: Ordered mapping specification with preserved key sequence for
                        consistent YAML generation. Contains two main parameters:
                - vlan_name (str): Maps 'vlanName' from API response indicating VLAN name
                  associated with SSIDs
                - ssid_details (list[dict]): Maps 'ssidDetails' from API response with
                  nested structure containing:
                    * ssid_name (str): Maps nested 'name' field from ssidDetails elements
                    * security_group_name (str): Maps nested 'securityGroupTag' field from
                      ssidDetails elements for Trustsec SGT assignments

        Specification Structure:
            Each key-value pair defines:
            - Outer key: Target YAML parameter name (snake_case convention)
            - Inner dict: Transformation metadata including:
                * type: Target Python/YAML data type ('str', 'int', 'list', 'dict')
                * source_key: Original API response field name (camelCase)
                * elements (optional): List element type for list-type fields
                * options (optional): Nested specification for dict-type fields defining
                  transformation for nested object properties

        Usage Context:
            - Referenced in get_workflow_filters_schema() as reverse_mapping_function
              for 'wireless_ssids' component
            - Invoked by modify_parameters() during API response transformation phase
            - Used by yaml_config_generator() to generate properly formatted wireless SSID
              configurations with VLAN-SSID-SGT mappings in YAML output

        Transformation Process:
            1. API returns vlanName='Data_VLAN', ssidDetails=[{name='Corp_SSID',
               securityGroupTag='Employees'}]
            2. modify_parameters() applies wireless_ssids_temp_spec mapping
            3. Transforms to vlan_name='Data_VLAN', ssid_details=[{ssid_name='Corp_SSID',
               security_group_name='Employees'}] in YAML
            4. Process handles nested list-of-dict structure automatically

        Parameter Details:
            - vlan_name: VLAN name for wireless traffic (e.g., 'Guest_VLAN', 'Data_VLAN')
            - ssid_details: List of SSID configurations mapped to the VLAN with nested fields:
                * ssid_name: Wireless SSID network name (e.g., 'Corp_WiFi', 'Guest_WiFi')
                * security_group_name: Trustsec Security Group Tag (SGT) name for access
                  policy enforcement (e.g., 'Employees', 'Guests', 'Contractors')

        Nested Structure Handling:
            - 'options' key defines nested transformation for list-of-dict elements
            - modify_parameters() recursively applies nested specifications to each
              dictionary element within ssid_details list
            - Preserves list ordering from API response in YAML output
            - Each SSID detail transformed independently with consistent field mapping

        Notes:
            - OrderedDict ensures consistent YAML key ordering across multiple generations
              enabling reliable version control diff operations
            - Nested options structure supports multi-level transformation for complex
              API response objects
            - Missing nested fields in API response are omitted from final YAML elements
            - Specification is immutable; runtime modifications have no effect on
              transformation behavior
            - Multiple SSIDs can map to single VLAN enabling shared VLAN infrastructure
              with differentiated access policies via security_group_name
        """
        wireless_ssids = OrderedDict({
            "vlan_name": {"type": "str", "source_key": "vlanName"},
            "ssid_details": {
                "type": "list",
                "elements": "dict",
                "source_key": "ssidDetails",
                "options": {
                    "ssid_name": {"type": "str", "source_key": "name"},
                    "security_group_name": {"type": "str", "source_key": "securityGroupTag"},
                },
            },
        })
        return wireless_ssids

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for template workflow.

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
                f"Iteration {index}: Checking parameters for {operation_name} operation with param_key '{param_key}'.",
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    f"Iteration {index}: Parameters found for {operation_name}. Starting processing.",
                    "INFO",
                )

                try:
                    operation_func(params).check_return_status()
                    operations_executed += 1
                    self.log(
                        f"{operation_name} operation completed successfully",
                        "DEBUG"
                    )
                except Exception as e:
                    self.log(
                        f"{operation_name} operation failed with error: {str(e)}",
                        "ERROR"
                    )
                    self.set_operation_result(
                        "failed", True,
                        f"{operation_name} operation failed: {str(e)}",
                        "ERROR"
                    ).check_return_status()

            else:
                operations_skipped += 1
                self.log(
                    f"Iteration {index}: No parameters found for {operation_name}. Skipping operation.",
                    "WARNING",
                )

        end_time = time.time()
        self.log(
            f"Completed 'get_diff_gathered' operation in {end_time - start_time:.2f} seconds.",
            "DEBUG",
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center SDA host port onboarding playbook config generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for SDA host port onboarding configuration extraction.

    Purpose:
        Initializes and executes the SDA host port onboarding playbook config generator
        workflow to extract existing port assignments, port channels, and wireless SSID
        configurations from Cisco Catalyst Center and generate Ansible-compatible YAML
        playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create SdaHostPortOnboardingPlaybookConfigGenerator instance
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
            - config (list[dict], required): Configuration parameters list containing:
                * file_path (str): Output YAML file path
                * component_specific_filters (dict): Component-based filters with:
                    - components_list (list): Component types to extract
                    - port_assignments (dict): Port assignment filters
                    - port_channels (dict): Port channel filters
                    - wireless_ssids (dict): Wireless SSID filters
            - state (str, default="gathered", choices=["gathered"]): Workflow state

    Version Requirements:
        - Minimum Catalyst Center version: 2.3.7.9
        - Introduced APIs for SDA host port onboarding retrieval:
            * Port Assignments (get_port_assignments)
            * Port Channels (get_port_channels)
            * Wireless VLAN-SSID Mappings (retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site)
            * Device Information (get_device_by_id)

    API Paths Utilized:
        - GET /dna/intent/api/v1/sda/portAssignments
        - GET /dna/intent/api/v1/sda/portChannels
        - GET /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids
        - GET /dna/intent/api/v1/network-device/{id}

    Supported States:
        - gathered: Extract existing SDA host port onboarding configurations and generate
          YAML playbook compatible with sda_host_port_onboarding_workflow_manager module

    Component Types:
        - port_assignments: Interface port assignment configurations with VLAN mappings,
          security groups, and authentication templates
        - port_channels: Port channel (LAG) configurations with member interfaces and
          trunk settings
        - wireless_ssids: Wireless SSID to VLAN mappings within fabric sites

    Error Handling:
        - Version compatibility failures: Module exits with error
        - Invalid state parameter: Module exits with error
        - Input validation failures: Module exits with error
        - Configuration processing errors: Module exits with error
        - Filter validation errors: Module exits with error
        - All errors are logged and returned via module.fail_json()

    Return Format:
        Success: module.exit_json() with result containing:
            - status (str): "success"
            - msg (dict): Operation result details with:
                * message (str): Success message
                * file_path (str): Generated YAML file path
                * components_processed (int): Number of components processed
                * components_skipped (int): Number of components skipped
                * configurations_count (int): Total configurations retrieved
            - response (dict): Detailed operation results
            - changed (bool): Whether changes were made (False for gathered state)

        Failure: module.fail_json() with error details:
            - failed (bool): True
            - msg (str): Error message
            - response (str): Detailed error information

    Notes:
        - Module is idempotent; multiple runs generate identical YAML content except
          timestamp in header comments
        - Check mode supported; validates parameters without file generation
        - Device management IP addresses are resolved from device IDs for all port
          configurations
        - Generated YAML uses OrderedDumper for consistent key ordering enabling
          version control
        - Fabric site hierarchical paths must match exact Catalyst Center fabric site
          structure (case-sensitive)
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
            "required": False,
            "type": "dict",
        },
        "file_path": {
            "type": "str",
            "required": False,
        },
        "file_mode": {
            "type": "str",
            "default": "overwrite",
            "choices": ["overwrite", "append"]
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

    # Initialize the SdaHostPortOnboardingPlaybookConfigGenerator object
    # This creates the main orchestrator for SDA host port onboarding playbook config generator extraction
    catc_sda_host_port_onboarding_playbook_config_generator = SdaHostPortOnboardingPlaybookConfigGenerator(module)

    # Log module initialization after object creation (now logging is available)
    catc_sda_host_port_onboarding_playbook_config_generator.log(
        f"Starting Ansible module execution for SDA host port onboarding playbook config generator generator at timestamp {initialization_timestamp}",
        "INFO"
    )

    # ============================================
    # Version Compatibility Check
    # ============================================
    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Validating Catalyst Center version compatibility - checking if version "
        f"{catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version()} "
        "meets minimum requirement of 2.3.7.9 for SDA host port onboarding APIs",
        "INFO"
    )

    if (
        catc_sda_host_port_onboarding_playbook_config_generator.compare_dnac_versions(
            catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        error_msg = (
            "The specified Catalyst Center version "
            f"'{catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version()}' "
            "does not support the YAML playbook generation for SDA Host Port "
            "Onboarding module. Supported versions start from '2.3.7.9' onwards. "
            "Version '2.3.7.9' introduces APIs for retrieving SDA host port "
            "onboarding configurations for the following components: Port "
            "Assignments, Port Channels, and Wireless SSIDs from the "
            "Catalyst Center."
        )

        catc_sda_host_port_onboarding_playbook_config_generator.log(
            f"Version compatibility check failed: {error_msg}",
            "ERROR"
        )

        catc_sda_host_port_onboarding_playbook_config_generator.msg = error_msg
        catc_sda_host_port_onboarding_playbook_config_generator.set_operation_result(
            "failed", False, catc_sda_host_port_onboarding_playbook_config_generator.msg, "ERROR"
        ).check_return_status()

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        f"Version compatibility check passed - Catalyst Center version {catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version()}"
        f" supports all required SDA host port onboarding APIs",
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = catc_sda_host_port_onboarding_playbook_config_generator.params.get("state")

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        f"Validating requested state parameter: '{state}' against "
        f"supported states: {catc_sda_host_port_onboarding_playbook_config_generator.supported_states}",
        "DEBUG"
    )

    if state not in catc_sda_host_port_onboarding_playbook_config_generator.supported_states:
        error_msg = (
            f"State '{state}' is invalid for this module. Supported states are: {catc_sda_host_port_onboarding_playbook_config_generator.supported_states}. "
            f"Please update your playbook to use one of the supported states."
        )

        catc_sda_host_port_onboarding_playbook_config_generator.log(
            f"State validation failed: {error_msg}",
            "ERROR"
        )

        catc_sda_host_port_onboarding_playbook_config_generator.status = "invalid"
        catc_sda_host_port_onboarding_playbook_config_generator.msg = error_msg
        catc_sda_host_port_onboarding_playbook_config_generator.check_return_status()

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        f"State validation passed - using state '{state}' for workflow execution",
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Starting comprehensive input parameter validation for playbook configuration",
        "INFO"
    )

    catc_sda_host_port_onboarding_playbook_config_generator.validate_input().check_return_status()

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = catc_sda_host_port_onboarding_playbook_config_generator.validated_config

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        f"Starting configuration processing loop - will process {len(config_list)} configuration item(s) from playbook",
        "INFO"
    )

    config = catc_sda_host_port_onboarding_playbook_config_generator.validated_config
    catc_sda_host_port_onboarding_playbook_config_generator.get_want(
        config, state
    ).check_return_status()
    catc_sda_host_port_onboarding_playbook_config_generator.get_diff_state_apply[
        state
    ]().check_return_status()

    # ============================================
    # Module Completion and Exit
    # ============================================
    module_end_time = time.time()
    module_duration = module_end_time - module_start_time

    completion_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_end_time)
    )

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        f"Module execution completed successfully at timestamp {completion_timestamp}. "
        f"Total execution time: {module_duration:.2f} seconds. Processed "
        f"{len(config_list)} configuration item(s) with final status: "
        f"{catc_sda_host_port_onboarding_playbook_config_generator.status}",
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    catc_sda_host_port_onboarding_playbook_config_generator.log(
        f"Exiting Ansible module with result: {catc_sda_host_port_onboarding_playbook_config_generator.result}",
        "DEBUG"
    )

    module.exit_json(**catc_sda_host_port_onboarding_playbook_config_generator.result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for SD-Access Fabric Virtual Networks Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Abhishek Maheshwari, Sunil Shatagopa, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: sda_fabric_virtual_networks_playbook_config_generator
short_description: Generate YAML playbook for C(sda_fabric_virtual_networks_workflow_manager) module.
description:
- Generates YAML configurations compatible with the C(sda_fabric_virtual_networks_workflow_manager)
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the fabric vlans, virtual networks and anycast
  gateways configured on the Cisco Catalyst Center.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Abhishek Maheshwari (@abmahesh)
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
    - A list of filters for generating YAML playbook compatible with the `sda_fabric_virtual_networks_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If C(components_list) is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to C(true), automatically generates YAML configurations for all the fabric vlans, virtual networks
            and anycast gateways present in the Cisco Catalyst Center, ignoring any provided filters.
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
          a default file name  C(<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(sda_fabric_virtual_networks_workflow_manager_playbook_2026-01-24_12-33-20.yml).
        type: str
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
              - Fabric VLANs C(fabric_vlan)
              - Virtual Networks C(virtual_networks)
              - Anycast Gateways C(anycast_gateways)
            - For example, ["fabric_vlan", "virtual_networks", "anycast_gateways"].
            - If not specified, all components are included.
            type: list
            elements: str
            choices: ["fabric_vlan", "virtual_networks", "anycast_gateways"]
          fabric_vlan:
            description:
            - Fabric VLANs to filter fabric vlans by vlan name or vlan id.
            type: list
            elements: dict
            suboptions:
              vlan_name:
                description:
                - VLAN name to filter fabric vlans by vlan name.
                type: str
              vlan_id:
                description:
                - VLAN ID to filter fabric vlans by vlan id.
                type: int
          virtual_networks:
            description:
            - Virtual Networks to filter virtual networks by VN name.
            type: list
            elements: dict
            suboptions:
              vn_name:
                description:
                - Virtual Network name to filter virtual networks by VN name.
                type: str
          anycast_gateways:
            description:
            - Anycast Gateways to filter anycast gateways by VN name, VLAN name,
              VLAN ID, or IP Pool name.
            type: list
            elements: dict
            suboptions:
              vn_name:
                description:
                - Virtual Network name to filter anycast gateways by VN name.
                type: str
              vlan_name:
                description:
                - VLAN name to filter anycast gateways by VLAN name.
                type: str
              vlan_id:
                description:
                - VLAN ID to filter anycast gateways by VLAN ID.
                type: int
              ip_pool_name:
                description:
                - IP Pool name to filter anycast gateways by IP Pool name.
                type: str

requirements:
- dnacentersdk >= 2.3.7.9
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - site_design.SiteDesigns.get_sites
    - sda.Sda.get_layer2_virtual_networks
    - sda.Sda.get_layer3_virtual_networks
    - sda.Sda.get_anycast_gateways
    - sda.Sda.get_fabric_sites
    - sda.Sda.get_fabric_zones
    - sda.Sda.get_fabric_sites_by_id
    - sda.Sda.get_fabric_zones_by_id
- Paths used are
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/sda/layer2-virtual-networks
    - GET /dna/intent/api/v1/sda/layer3-virtual-networks
    - GET /dna/intent/api/v1/sda/anycast-gateways
    - GET /dna/intent/api/v1/sda/fabric-sites
    - GET /dna/intent/api/v1/sda/fabric-zones
    - GET /dna/intent/api/v1/sda/fabric-sites/{id}
    - GET /dna/intent/api/v1/sda/fabric-zones/{id}
seealso:
- module: cisco.dnac.sda_fabric_virtual_networks_workflow_manager
  description: Module for managing fabric VLANs, Virtual Networks,
               and Anycast Gateways in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Auto-generate YAML Configuration for all components which
     includes fabric vlans, virtual networks and anycast gateways.
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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

- name: Generate YAML Configuration with File Path specified
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
        file_path: "/tmp/all_config.yml"

- name: Generate YAML Configuration with specific fabric vlan components only
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_vlan_components_config.yml"
        component_specific_filters:
          components_list: ["fabric_vlan"]

- name: Generate YAML Configuration with specific virtual networks components only
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_virtual_networks_components_config.yml"
        component_specific_filters:
          components_list: ["virtual_networks"]

- name: Generate YAML Configuration with specific anycast gateways components only
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_anycast_gateways_components_config.yml"
        component_specific_filters:
          components_list: ["anycast_gateways"]

- name: Generate YAML Configuration for fabric vlans with vlan name filter
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_vlans_components_config.yml"
        component_specific_filters:
          components_list: ["fabric_vlan"]
          fabric_vlan:
            - vlan_name: "vlan_1"
            - vlan_name: "vlan_2"

- name: Generate YAML Configuration for fabric vlans and virtual networks with multiple filters
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_multiple_components_config.yml"
        component_specific_filters:
          components_list: ["fabric_vlan", "virtual_networks"]
          fabric_vlan:
            - vlan_name: "vlan_1"
            - vlan_name: "vlan_2"
          virtual_networks:
            - vn_name: "vn_1"
            - vn_name: "vn_2"

- name: Generate YAML Configuration for all components with no filters
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_all_components_config.yml"
        component_specific_filters:
          components_list: ["fabric_vlan", "virtual_networks", "anycast_gateways"]

- name: Generate YAML Configuration for fabric vlans with VLAN IDs filter
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_vlan_components_config.yml"
        component_specific_filters:
          components_list: ["fabric_vlan"]
          fabric_vlan:
            - vlan_id: 1031
            - vlan_id: 1038

- name: Generate YAML Configuration for fabric vlans with both VLAN name and ID filters
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_vlan_components_config.yml"
        component_specific_filters:
          components_list: ["fabric_vlan"]
          fabric_vlan:
            - vlan_name: "Chennai-VN6-Pool1"
              vlan_id: 1031
            - vlan_name: "Chennai-VN9-Pool2"
              vlan_id: 1038

- name: Generate YAML Configuration for virtual networks with specific VN names
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_virtual_networks_components_config.yml"
        component_specific_filters:
          components_list: ["virtual_networks"]
          virtual_networks:
            - vn_name: "VN1"
            - vn_name: "VN3"

- name: Generate YAML Configuration for anycast gateways with VN name filter
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_anycast_gateways_components_config.yml"
        component_specific_filters:
          components_list: ["anycast_gateways"]
          anycast_gateways:
            - vn_name: "Chennai_VN1"
            - vn_name: "Chennai_VN3"

- name: Generate YAML Configuration for anycast gateways with IP pool name filter
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_anycast_gateways_components_config.yml"
        component_specific_filters:
          components_list: ["anycast_gateways"]
          anycast_gateways:
            - ip_pool_name: "Chennai-VN3-Pool1"
            - ip_pool_name: "Chennai-VN1-Pool2"

- name: Generate YAML Configuration for anycast gateways with VLAN ID and IP pool filter
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_anycast_gateways_components_config.yml"
        component_specific_filters:
          components_list: ["anycast_gateways"]
          anycast_gateways:
            - vlan_id: 1032
            - vlan_id: 1033
            - ip_pool_name: "Chennai-VN1-Pool2"

- name: Generate YAML Configuration for anycast gateways with VLAN name filter
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_anycast_gateways_components_config.yml"
        component_specific_filters:
          components_list: ["anycast_gateways"]
          anycast_gateways:
            - vlan_name: "Chennai-VN1-Pool2"
            - vlan_name: "Chennai-VN7-Pool1"

- name: Generate YAML Configuration for anycast gateways with VLAN name and ID combination
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_anycast_gateways_components_config.yml"
        component_specific_filters:
          components_list: ["anycast_gateways"]
          anycast_gateways:
            - vlan_name: "Chennai-VN1-Pool2"
              vlan_id: 1022
            - vlan_name: "Chennai-VN7-Pool1"
              vlan_id: 1033

- name: Generate YAML Configuration for anycast gateways with comprehensive filters
  cisco.dnac.sda_fabric_virtual_networks_playbook_config_generator:
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
      - file_path: "/tmp/catc_anycast_gateways_components_config.yml"
        component_specific_filters:
          components_list: ["anycast_gateways"]
          anycast_gateways:
            - vlan_name: "Chennai-VN1-Pool2"
              vlan_id: 1022
              ip_pool_name: "Chennai-VN1-Pool2"
              vn_name: "Chennai_VN1"
            - vlan_name: "Chennai-VN7-Pool1"
              vlan_id: 1033
              ip_pool_name: "Chennai-VN7-Pool1"
              vn_name: "Chennai_VN7"
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
            "components_processed": 3,
            "components_skipped": 0,
            "configurations_count": 3,
            "file_path": "sda_fabric_virtual_networks_playbook_config_2026-02-18_15-56-19.yml",
            "message": "YAML configuration file generated successfully for module 'sda_fabric_virtual_networks_workflow_manager'",
            "status": "success"
        },
        "response": {
            "components_processed": 3,
            "components_skipped": 0,
            "configurations_count": 3,
            "file_path": "sda_fabric_virtual_networks_playbook_config_2026-02-18_15-56-19.yml",
            "message": "YAML configuration file generated successfully for module 'sda_fabric_virtual_networks_workflow_manager'",
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
            "Validation Error in entry 1: 'component_specific_filters' must be provided with 'components_list' key
             when 'generate_all_configurations' is set to False.",
        "response":
            "Validation Error in entry 1: 'component_specific_filters' must be provided with 'components_list' key
             when 'generate_all_configurations' is set to False."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase
)
from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts
)
import time
from collections import OrderedDict


class VirtualNetworksPlaybookConfigGenerator(DnacBase, BrownFieldHelper):
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
        self.site_id_name_dict = self.get_site_id_name_mapping()
        self.module_name = "sda_fabric_virtual_networks_workflow_manager"

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
            "component_specific_filters": {
                "type": "dict",
                "required": False
            }
        }

        # Validate params
        self.log("Validating configuration against schema", "DEBUG")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

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
        Constructs and returns a structured mapping for managing various virtual network elements
        such as fabric VLANs, virtual networks, and anycast gateways. This mapping includes
        associated filters, temporary specification functions, API details, and fetch function references
        used in the virtual network workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods like
                `fabric_vlan_temp_spec`, `get_fabric_vlans_configuration`, etc.

        Return:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a network component
                (e.g., 'fabric_vlan', 'virtual_networks', 'anycast_gateways') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'sda').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
        """

        self.log("Building workflow filters schema for sda fabric virtual networks module", "DEBUG")

        schema = {
            "network_elements": {
                "fabric_vlan": {
                    "filters": ["vlan_name", "vlan_id"],
                    "reverse_mapping_function": self.fabric_vlan_temp_spec,
                    "api_function": "get_layer2_virtual_networks",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_vlans_configuration,
                },
                "virtual_networks": {
                    "filters": ["vn_name"],
                    "reverse_mapping_function": self.virtual_network_temp_spec,
                    "api_function": "get_layer3_virtual_networks",
                    "api_family": "sda",
                    "get_function_name": self.get_virtual_networks_configuration,
                },
                "anycast_gateways": {
                    "filters": ["vn_name", "vlan_id", "vlan_name", "ip_pool_name"],
                    "reverse_mapping_function": self.anycast_gateway_temp_spec,
                    "api_function": "get_anycast_gateways",
                    "api_family": "sda",
                    "get_function_name": self.get_anycast_gateways_configuration,
                },
            }
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network element(s): {network_elements}",
            "INFO",
        )

        return schema

    def transform_fabric_site_locations(self, vlan_details):
        """
        Transforms fabric site-related information for a given VLAN by extracting and mapping
        the site hierarchy and fabric type based on the fabric ID.

        Args:
            vlan_details (dict): A dictionary containing VLAN-specific information, including the 'fabricId' key.

        Returns:
            list: A list containing a single dictionary with the following keys:
                - "site_name_hierarchy" (str): The hierarchical name of the site (e.g., "Global/Site/Building").
                - "fabric_type" (str): The type of fabric, such as "fabric_site" or "fabric_zone".
        """

        self.log(
            "Starting site name hierarchy and fabric type transformation for given fabric id: {0}"
            .format(vlan_details.get("fabricId", "Unknown")),
            "DEBUG"
        )
        fabric_id = vlan_details.get("fabricId")

        if not fabric_id:
            self.log("No fabric ID found in vlan details: {0}".format(vlan_details), "WARNING")
            return fabric_id

        self.log(
            "Processing site name hierarchy and fabric type for given fabric id: {0}"
            .format(fabric_id),
            "DEBUG"
        )
        site_id, fabric_type = self.analyse_fabric_site_or_zone_details(fabric_id)

        if not site_id:
            self.log("No site ID found for given fabric ID: {0}". format(fabric_id), "WARNING")
            return site_id

        if not fabric_type:
            self.log("Fabric type not found for given fabric ID: {0}".format(fabric_id), "WARNING")
            return fabric_type

        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        if not site_name_hierarchy:
            self.log("Site name hierarchy not found for site ID: {0}".format(site_id), "WARNING")
            return site_name_hierarchy

        self.log(
            "Completed site name hierarchy and fabric type transformation for fabric id: {0}, "
            "Transformed site name hierarchy: {1}, fabric type: {2}"
            .format(fabric_id, site_name_hierarchy, fabric_type),
            "DEBUG"
        )

        return [{
            "site_name_hierarchy": site_name_hierarchy,
            "fabric_type": fabric_type
        }]

    def transform_fabric_vn_site_locations(self, vn_details):
        """
        Transforms virtual network (VN) details by mapping fabric IDs to their corresponding
        site hierarchy names and fabric types.

        Args:
            vn_details (dict): A dictionary containing virtual network information,
                            expected to include a list of fabric IDs under the 'fabricIds' key.

        Returns:
            list: A list of dictionaries, each containing:
                - "site_name_hierarchy" (str): The hierarchical name of the site
                (e.g., "Global/Site/Building/Floor").
                - "fabric_type" (str): The type of fabric, such as "fabric_site" or "fabric_zone".
        """

        self.log(
            "Starting fabric site locations transformation for given fabric id(s): {0}"
            .format(vn_details.get("fabricIds", "Unknown")),
            "DEBUG"
        )
        fabric_ids = vn_details.get("fabricIds")
        fabric_site_list = []
        if not fabric_ids:
            self.log(
                "No fabric IDs found in VN details: {0}".format(vn_details),
                "DEBUG"
            )
            return fabric_site_list

        self.log(
            "Processing {0} fabric site locations for fabric id(s): {1}".format(len(fabric_ids), fabric_ids),
            "DEBUG"
        )

        for fabric_id in fabric_ids:
            site_id, fabric_type = self.analyse_fabric_site_or_zone_details(fabric_id)
            if not site_id:
                self.log("No site ID found for given fabric ID: {0}". format(fabric_id), "WARNING")
                return site_id

            if not fabric_type:
                self.log("Fabric type not found for given fabric ID: {0}".format(fabric_id), "WARNING")
                return fabric_type

            site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
            if not site_name_hierarchy:
                self.log("Site name hierarchy not found for site ID: {0}".format(site_id), "WARNING")
                return site_name_hierarchy

            self.log(
                "Transformed fabric site name {0} for fabric id: {1}".format(
                    site_name_hierarchy, fabric_id
                ),
                "DEBUG"
            )
            site_dict = {
                "site_name_hierarchy": site_name_hierarchy,
                "fabric_type": fabric_type
            }
            fabric_site_list.append(site_dict)

        self.log(
            "Completed fabric site locations transformation. Transformed fabric site(s): {0}"
            .format(fabric_site_list), "DEBUG"
        )

        return fabric_site_list

    def transform_anycast_fabric_site_location(self, anycast_details):
        """
        Transforms anycast gateway details by extracting the site hierarchy and fabric type
        using the provided fabric ID.

        Args:
            anycast_details (dict): A dictionary containing anycast gateway information,
                                    expected to include the key 'fabricId'.

        Returns:
            dict or None: A dictionary containing:
                - "site_name_hierarchy" (str): The hierarchical name of the site
                (e.g., "Global/Site/Building/Floor").
                - "fabric_type" (str): The type of fabric, such as "fabric_site" or "fabric_zone".
        """

        self.log(
            "Starting anycast gateway details transformation for given fabric id: {0}"
            .format(anycast_details.get("fabricId", "Unknown")), "DEBUG"
        )

        fabric_id = anycast_details.get("fabricId")
        if not fabric_id:
            self.log(
                "No fabric ID found in anycast gateway details: {0}".format(anycast_details),
                "DEBUG"
            )
            return fabric_id

        site_id, fabric_type = self.analyse_fabric_site_or_zone_details(fabric_id)
        if not site_id:
            self.log("No site ID found for given fabric ID: {0}". format(fabric_id), "WARNING")
            return site_id

        if not fabric_type:
            self.log("Fabric type not found for given fabric ID: {0}".format(fabric_id), "WARNING")
            return fabric_type

        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        if not site_name_hierarchy:
            self.log("Site name hierarchy not found for site ID: {0}".format(site_id), "WARNING")
            return site_name_hierarchy

        self.log(
            "Completed anycast gateway details transformation for fabric id: {0}. "
            "Transformed site name hierarchy: {1}, fabric type: {2}"
            .format(fabric_id, site_name_hierarchy, fabric_type),
            "DEBUG"
        )
        return {
            "site_name_hierarchy": site_name_hierarchy,
            "fabric_type": fabric_type
        }

    def transform_anchored_site_name(self, vn_details):
        """
        Transforms the anchored site name for a given virtual network (VN) by extracting
        the site hierarchy and fabric type from the VN details.

        Args:
            vn_details (dict): A dictionary containing virtual network information,
                               expected to include the key 'anchoredSiteId'.

        Returns:
            str or None: The hierarchical name of the anchored site if found, otherwise None.
        """

        self.log(
            "Starting anchored site name transformation for given anchored site id: {0}"
            .format(vn_details.get("anchoredSiteId", "Unknown")), "DEBUG"
        )

        fabric_id = vn_details.get("anchoredSiteId")
        if not fabric_id:
            self.log(
                "No anchored site ID found in VN details: {0}".format(vn_details),
                "DEBUG"
            )
            return fabric_id

        site_id, fabric_type = self.analyse_fabric_site_or_zone_details(fabric_id)
        if not site_id:
            self.log("No site ID found for given fabric ID: {0}". format(fabric_id), "WARNING")
            return site_id

        if not fabric_type:
            self.log("Fabric type not found for given fabric ID: {0}".format(fabric_id), "WARNING")
            return fabric_type

        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        if not site_name_hierarchy:
            self.log("Site name hierarchy not found for site ID: {0}".format(site_id), "WARNING")
            return site_name_hierarchy

        self.log(
            "Completed anchored site name transformation for anchored site id: {0}. "
            "Transformed anchored site name: {1}". format(fabric_id, site_name_hierarchy),
            "DEBUG"
        )
        return site_name_hierarchy

    def fabric_vlan_temp_spec(self):
        """
        Constructs a temporary specification for fabric VLANs, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as VLAN name,
        VLAN ID, fabric site locations, traffic type, and various flags related to wireless and resource management.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of fabric VLAN attributes.
        """

        self.log("Generating temporary specification for fabric VLANs.", "DEBUG")
        fabric_vlan = OrderedDict(
            {
                "vlan_name": {"type": "str", "source_key": "vlanName"},
                "vlan_id": {
                    "type": "int",
                    "source_key": "vlanId"
                },
                "fabric_site_locations": {
                    "type": "list",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_fabric_site_locations,
                    "site_name_hierarchy": {"type": "str"},
                    "fabric_type": {"type": "str"},
                },
                "traffic_type": {"type": "str", "source_key": "trafficType"},
                "fabric_enabled_wireless": {"type": "bool", "source_key": "isFabricEnabledWireless"},
                "associated_layer3_virtual_network": {"type": "str", "source_key": "associatedLayer3VirtualNetworkName"},
                "is_wireless_flooding_enable": {"type": "bool", "source_key": "isWirelessFloodingEnabled"},
                "is_resource_guard_enable": {"type": "bool", "source_key": "isResourceGuardEnabled"},
                "flooding_address_assignment": {"type": "str", "source_key": "layer2FloodingAddressAssignment"},
                "flooding_address": {"type": "str", "source_key": "layer2FloodingAddress"},
            }
        )
        return fabric_vlan

    def virtual_network_temp_spec(self):
        """
        Constructs a temporary specification for virtual networks, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as virtual network name,
        anchored site name, fabric site locations, and other relevant attributes.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of virtual network attributes.
        """

        self.log("Generating temporary specification for virtual networks.", "DEBUG")
        virtual_network = OrderedDict(
            {
                "vn_name": {"type": "str", "source_key": "virtualNetworkName"},
                "anchored_site_name": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_anchored_site_name,
                },
                "fabric_site_locations": {
                    "type": "list",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_fabric_vn_site_locations,
                    "site_name_hierarchy": {"type": "str"},
                    "fabric_type": {"type": "str"},
                },
            }
        )
        return virtual_network

    def anycast_gateway_temp_spec(self):
        """
        Constructs a temporary specification for anycast gateways, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as virtual network name,
        IP pool name, TCP MSS adjustment, VLAN name, VLAN ID, traffic type, pool type, security group name,
        and various flags related to wireless and resource management.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of anycast gateway attributes.
        """

        self.log("Generating temporary specification for anycast gateways.", "DEBUG")
        anycast_gateway = OrderedDict(
            {
                "vn_name": {"type": "str", "source_key": "virtualNetworkName"},
                "ip_pool_name": {"type": "str", "source_key": "ipPoolName"},
                "tcp_mss_adjustment": {"type": "int", "source_key": "tcpMssAdjustment"},
                "vlan_name": {"type": "str", "source_key": "vlanName"},
                "vlan_id": {"type": "int", "source_key": "vlanId"},
                "traffic_type": {"type": "str", "source_key": "trafficType"},
                "pool_type": {"type": "str", "source_key": "poolType"},
                "security_group_name": {"type": "str", "source_key": "securityGroupName"},
                "is_critical_pool": {"type": "bool", "source_key": "isCriticalPool"},
                "layer2_flooding_enabled": {"type": "bool", "source_key": "isLayer2FloodingEnabled"},
                "fabric_enabled_wireless": {"type": "bool", "source_key": "isWirelessPool"},
                "is_wireless_flooding_enable": {"type": "bool", "source_key": "isWirelessFloodingEnabled"},
                "is_resource_guard_enable": {"type": "bool", "source_key": "isResourceGuardEnabled"},
                "ip_directed_broadcast": {"type": "bool", "source_key": "isIpDirectedBroadcast"},
                "intra_subnet_routing_enabled": {"type": "bool", "source_key": "isIntraSubnetRoutingEnabled"},
                "multiple_ip_to_mac_addresses": {"type": "bool", "source_key": "isMultipleIpToMacAddresses"},
                "supplicant_based_extended_node_onboarding": {"type": "bool", "source_key": "isSupplicantBasedExtendedNodeOnboarding"},
                "group_policy_enforcement_enabled": {"type": "bool", "source_key": "isGroupBasedPolicyEnforcementEnabled"},
                "flooding_address_assignment": {"type": "str", "source_key": "layer2FloodingAddressAssignment"},
                "flooding_address": {"type": "str", "source_key": "layer2FloodingAddress"},
                "fabric_site_location": {
                    "type": "dict",
                    "special_handling": True,
                    "transform": self.transform_anycast_fabric_site_location,
                    "site_name_hierarchy": {"type": "str"},
                    "fabric_type": {"type": "str"},
                },
            }
        )
        return anycast_gateway

    def validate_fabric_vlan_id(self, vlan_id):
        """
        Validates the fabric VLAN ID to ensure it is within the acceptable range (1-4094).
        Args:
            vlan_id (int): The VLAN ID to be validated.
        Returns:
            None: If the VLAN ID is valid.
        Description:
            Validates the provided VLAN ID to ensure it falls within the acceptable range of 2 to
            4094, excluding reserved VLANs 1002-1005 and 2046. If the VLAN ID is invalid,
            an error message is set, and the operation result is updated to indicate failure.
        """
        if (
            vlan_id
            and vlan_id not in range(2, 4094)
            or vlan_id in [1002, 1003, 1004, 1005, 2046]
        ):
            self.msg = (
                "Invalid vlan_id '{0}' given in the playbook. Allowed VLAN range is (2,4094) except for "
                "reserved VLANs 1002-1005, and 2046."
            ).format(vlan_id)
            self.fail_and_exit(self.msg)

    def get_fabric_vlans_configuration(self, network_element, filters):
        """
        Retrieves fabric VLANs based on the provided network element and component_specific_filters.
        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving fabric VLANs.
            filters (dict): Dictionary containing global filters and component_specific_filters for fabric VLANs.

        Returns:
            dict: A dictionary containing the modified details of fabric VLANs.
        """

        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve fabric VLANs with network element: {0} and component-specific filters: {1}".format(
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
            return {"fabric_vlan": []}

        final_fabric_vlans = []

        self.log(
            "Getting fabric vlans using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for fabric vlans retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                supported_keys = {"vlan_name", "vlan_id"}

                if "vlan_name" in filter_param:
                    params["vlanName"] = filter_param["vlan_name"]
                if "vlan_id" in filter_param:
                    self.validate_fabric_vlan_id(filter_param["vlan_id"])
                    params["vlanId"] = filter_param["vlan_id"]

                unsupported_keys = set(filter_param.keys()) - supported_keys
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for fabric vlans: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching fabric vlans with parameters: {0}".format(params),
                    "DEBUG"
                )
                fabric_vlan_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if fabric_vlan_details:
                    final_fabric_vlans.extend(fabric_vlan_details)
                    self.log(
                        "Retrieved {0} fabric vlan(s): {1}".format(
                            len(fabric_vlan_details), fabric_vlan_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No fabric vlans found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for fabric vlans retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

        else:
            self.log("Fetching all fabric vlans from Catalyst Center", "DEBUG")

            fabric_vlan_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if fabric_vlan_details:
                final_fabric_vlans.extend(fabric_vlan_details)
                self.log(
                    "Retrieved {0} fabric vlan(s) from Catalyst Center".format(
                        len(fabric_vlan_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No fabric vlans found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} fabric vlan(s) using fabric_vlan temp spec".format(
                len(final_fabric_vlans)
            ),
            "DEBUG"
        )
        fabric_vlan_temp_spec = self.fabric_vlan_temp_spec()
        vlans_details = self.modify_parameters(
            fabric_vlan_temp_spec, final_fabric_vlans
        )
        modified_fabric_vlans_details = {}

        if vlans_details:
            modified_fabric_vlans_details['fabric_vlan'] = vlans_details

        self.log(
            "Completed retrieving fabric vlan(s): {0}".format(
                modified_fabric_vlans_details
            ),
            "INFO",
        )

        return modified_fabric_vlans_details

    def get_virtual_networks_configuration(self, network_element, filters):
        """
        Retrieves virtual networks based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving virtual networks.
            filters (dict): Dictionary containing global filters and component_specific_filters for virtual networks.

        Returns:
            dict: A dictionary containing the modified details of virtual networks.
        """

        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve virtual networks with network element: {0} and component-specific filters: {1}".format(
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
            return {"virtual_networks": []}

        final_virtual_networks = []
        self.log(
            "Getting virtual networks using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for virtual networks retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                if "vn_name" in filter_param:
                    params["virtualNetworkName"] = filter_param["vn_name"]

                unsupported_keys = set(filter_param.keys()) - {"vn_name"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for virtual networks: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching virtual networks with parameters: {0}".format(params),
                    "DEBUG"
                )
                virtual_network_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if virtual_network_details:
                    final_virtual_networks.extend(virtual_network_details)
                    self.log(
                        "Retrieved {0} virtual network(s): {1}".format(
                            len(virtual_network_details), virtual_network_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No virtual networks found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for virtual networks retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all virtual networks from Catalyst Center", "DEBUG")

            virtual_network_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if virtual_network_details:
                final_virtual_networks.extend(virtual_network_details)
                self.log(
                    "Retrieved {0} virtual network(s) from Catalyst Center".format(
                        len(virtual_network_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No virtual networks found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} virtual network(s) using virtual_network temp spec".format(
                len(final_virtual_networks)
            ),
            "DEBUG"
        )
        virtual_network_temp_spec = self.virtual_network_temp_spec()
        vn_details = self.modify_parameters(
            virtual_network_temp_spec, final_virtual_networks
        )
        modified_virtual_networks_details = {}

        if vn_details:
            modified_virtual_networks_details['virtual_networks'] = vn_details

        self.log(
            "Completed retrieving virtual network(s): {0}".format(
                modified_virtual_networks_details
            ),
            "INFO",
        )

        return modified_virtual_networks_details

    def get_anycast_gateways_configuration(self, network_element, filters):
        """
        Fetches anycast gateways from the Cisco DNA Center using the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving anycast gateways.
            filters (dict): Dictionary containing global filters and component_specific_filters for anycast gateways.

        Returns:
            dict: A dictionary containing the modified details of anycast gateways.
        """

        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve anycast gateways with network element: {0} and component-specific filters: {1}".format(
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
            return {"anycast_gateways": []}

        final_anycast_gateways = []

        self.log(
            "Getting anycast gateways using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG",
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for anycast gateways retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                supported_keys = {"vn_name", "vlan_name", "ip_pool_name", "vlan_id"}

                if "vn_name" in filter_param:
                    params["virtualNetworkName"] = filter_param["vn_name"]
                if "vlan_name" in filter_param:
                    params["vlanName"] = filter_param["vlan_name"]
                if "ip_pool_name" in filter_param:
                    params["ipPoolName"] = filter_param["ip_pool_name"]
                if "vlan_id" in filter_param:
                    self.validate_fabric_vlan_id(filter_param["vlan_id"])
                    params["vlanId"] = filter_param["vlan_id"]

                unsupported_keys = set(filter_param.keys()) - supported_keys
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for anycast gateways: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching anycast gateways with parameters: {0}".format(params),
                    "DEBUG"
                )
                anycast_gateway_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if anycast_gateway_details:
                    final_anycast_gateways.extend(anycast_gateway_details)
                    self.log(
                        "Retrieved {0} anycast gateway(s): {1}".format(
                            len(anycast_gateway_details), anycast_gateway_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No anycast gateways found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for anycast gateways retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all anycast gateways from Catalyst Center", "DEBUG")

            anycast_gateway_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if anycast_gateway_details:
                final_anycast_gateways.extend(anycast_gateway_details)
                self.log(
                    "Retrieved {0} anycast gateway(s) from Catalyst Center".format(
                        len(anycast_gateway_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No anycast gateways found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} anycast gateway(s) using anycast_gateway temp spec".format(
                len(final_anycast_gateways)
            ),
            "DEBUG"
        )
        anycast_gateway_temp_spec = self.anycast_gateway_temp_spec()
        anycast_gateways_details = self.modify_parameters(
            anycast_gateway_temp_spec, final_anycast_gateways
        )

        modified_anycast_gateways_details = {}

        if anycast_gateways_details:
            modified_anycast_gateways_details["anycast_gateways"] = anycast_gateways_details

        self.log(
            "Completed retrieving anycast gateway(s): {0}".format(
                modified_anycast_gateways_details
            ),
            "INFO",
        )
        return modified_anycast_gateways_details

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for sda fabric virtual networks workflow.

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
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_virtual_networks_playbook_config_generator = VirtualNetworksPlaybookConfigGenerator(module)
    if (
        ccc_virtual_networks_playbook_config_generator.compare_dnac_versions(
            ccc_virtual_networks_playbook_config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_virtual_networks_playbook_config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for SDA FABRIC VIRTUAL NETWORKS Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_virtual_networks_playbook_config_generator.get_ccc_version()
            )
        )
        ccc_virtual_networks_playbook_config_generator.set_operation_result(
            "failed", False, ccc_virtual_networks_playbook_config_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_virtual_networks_playbook_config_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_virtual_networks_playbook_config_generator.supported_states:
        ccc_virtual_networks_playbook_config_generator.status = "invalid"
        ccc_virtual_networks_playbook_config_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_virtual_networks_playbook_config_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_virtual_networks_playbook_config_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_virtual_networks_playbook_config_generator.validated_config:
        ccc_virtual_networks_playbook_config_generator.reset_values()
        ccc_virtual_networks_playbook_config_generator.get_want(
            config, state
        ).check_return_status()
        ccc_virtual_networks_playbook_config_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_virtual_networks_playbook_config_generator.result)


if __name__ == "__main__":
    main()

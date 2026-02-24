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
  config:
    description:
    - Configuration parameters for YAML playbook generation workflow.
    - Defines output file path, auto-discovery mode, and component-specific
      filters for targeted SDA host port onboarding extraction.
    - At least one of generate_all_configurations or component_specific_filters
      with components_list must be specified to identify target configurations.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - Enables auto-discovery mode for complete SDA fabric infrastructure extraction.
        - When True, extracts all port assignments, port channels, and wireless SSIDs
          for all fabric sites without filter restrictions.
        - Ignores component_specific_filters if provided; retrieves complete
          brownfield SDA host port onboarding inventory from Catalyst Center.
        - Automatically generates timestamped filename if file_path not specified.
        - Useful for complete fabric documentation, configuration backup, and
          disaster recovery planning.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Absolute or relative path for YAML configuration file output.
        - If not provided, generates default filename in current working directory
          with pattern
          'sda_host_port_onboarding_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml'
        - Example default filename
          'sda_host_port_onboarding_workflow_manager_playbook_2026-01-24_12-33-20.yml'
        - Directory created automatically if path does not exist.
        - Supports YAML file extension (.yml or .yaml).
        type: str
      global_filters:
        description:
        - Global filters to apply when generating the YAML configuration file.
        - Reserved for future use; currently not implemented for this module.
        - Component-specific filters should be used for fabric site filtering.
        type: dict
        required: false
      component_specific_filters:
        description:
        - Component-based filters for targeted SDA host port onboarding extraction.
        - Requires components_list to specify which components to process.
        - When generate_all_configurations is False, component_specific_filters
          with components_list must be provided.
        - Filters apply independently per component type (port assignments,
          port channels, wireless SSIDs).
        type: dict
        suboptions:
          components_list:
            description:
            - List of SDA host port onboarding components to include in YAML configuration.
            - Valid values are 'port_assignments' for interface port assignments,
              'port_channels' for port channel configurations, and 'wireless_ssids'
              for wireless SSID mappings to VLANs within fabric sites.
            - If not specified when generate_all_configurations is False, validation
              fails requiring explicit component selection.
            - Multiple components can be specified for combined extraction.
            - For example, [port_assignments, port_channels, wireless_ssids]
            type: list
            choices: ["port_assignments", "port_channels", "wireless_ssids"]
            elements: str
          port_assignments:
            description:
            - Filters for port assignment configuration extraction.
            - Extracts only port assignments for specified fabric site hierarchies.
            - Fabric site names must be full hierarchical paths (case-sensitive).
            - If not specified when component included in components_list, extracts
              all port assignments across all fabric sites.
            type: dict
            required: false
            suboptions:
              fabric_site_name_hierarchy:
                description:
                - List of fabric site hierarchical paths to extract port assignments.
                - Site names must match exact hierarchical paths in Catalyst Center
                  (case-sensitive).
                - Extracts port assignments for all devices within specified fabric sites.
                - For example, ["Global/USA/San Jose/Building1", "Global/USA/RTP/Building2"]
                type: list
                elements: str
                required: false
          port_channels:
            description:
            - Filters for port channel configuration extraction.
            - Extracts only port channels for specified fabric site hierarchies.
            - Fabric site names must be full hierarchical paths (case-sensitive).
            - If not specified when component included in components_list, extracts
              all port channels across all fabric sites.
            type: dict
            required: false
            suboptions:
              fabric_site_name_hierarchy:
                description:
                - List of fabric site hierarchical paths to extract port channels.
                - Site names must match exact hierarchical paths in Catalyst Center
                  (case-sensitive).
                - Extracts port channel configurations for all devices within specified fabric sites.
                - For example, ["Global/USA/San Jose/Building1", "Global/USA/RTP/Building2"]
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
    devices.get_device_by_id
  - API paths utilized - GET /dna/intent/api/v1/sda/portAssignments,
    GET /dna/intent/api/v1/sda/portChannels,
    GET /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids
    GET /dna/intent/api/v1/network-device/{id}
  - Module is idempotent; multiple runs generate identical YAML content except
    timestamp in header comments.
  - Check mode supported; validates parameters without file generation.
  - Device management IP addresses are resolved from device IDs for all port
    configurations enabling device-specific port onboarding playbooks.
  - Generated YAML uses OrderedDumper for consistent key ordering enabling version
    control.
  - Fabric site hierarchical paths must match exact Catalyst Center fabric site structure.
seealso:
- module: cisco.dnac.sda_host_port_onboarding_workflow_manager
  description: Module for managing SDA host port onboarding workflows in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML playbook for SDA host port onboarding workflow manager which includes all components
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
    config:
      - generate_all_configurations: true

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
    config:
      - generate_all_configurations: true
        file_path: "sda_host_port_onboarding_config.yml"

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
    config:
      - generate_all_configurations: false
        file_path: "port_assignments_config.yml"
        component_specific_filters:
          components_list: ["port_assignments"]
          port_assignments:
            fabric_site_name_hierarchy:
              - "Global/USA/San Jose/Building1"
              - "Global/USA/RTP/Building2"

- name: Generate YAML Configuration with port channels component
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
    config:
      - file_path: "port_channels_config.yml"
        component_specific_filters:
          components_list: ["port_channels"]
          port_channels:
            fabric_site_name_hierarchy:
              - "Global/USA/San Jose/Building1"

- name: Generate YAML Configuration with wireless SSIDs component
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
    config:
      - file_path: "wireless_ssids_config.yml"
        component_specific_filters:
          components_list: ["wireless_ssids"]
          wireless_ssids:
            fabric_site_name_hierarchy:
              - "Global/USA/San Jose/Building1"
              - "Global/USA/RTP/Building2"

- name: Generate YAML Configuration with multiple components and fabric site filters
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
    config:
      - file_path: "complete_sda_config.yml"
        component_specific_filters:
          components_list: ["port_assignments", "port_channels", "wireless_ssids"]
          port_assignments:
            fabric_site_name_hierarchy:
              - "Global/USA/San Jose/Building1"
          port_channels:
            fabric_site_name_hierarchy:
              - "Global/USA/San Jose/Building1"
          wireless_ssids:
            fabric_site_name_hierarchy:
              - "Global/USA/San Jose/Building1"
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
        fabric_site_id_name_dict (dict): Cached mapping of fabric site UUIDs to
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
        self.fabric_site_id_name_dict = self.get_fabric_site_id_name_mapping()
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
            },
            "global_filters": {
                "type": "dict",
                "required": False},
        }

        # Validate params
        self.log("Validating configuration against schema.", "DEBUG")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log("Validating minimum requirements against provided config: {0}".format(self.config), "DEBUG")
        self.validate_minimum_requirements(self.config)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
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
                - global_filters (list): Empty list (reserved for future use)

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
            },
            "global_filters": [],
        }

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
            "Extracting component_specific_filters from filters dictionary: {0}. "
            "Filters determine which fabric sites to process for port assignment "
            "retrieval.".format(filters),
            "DEBUG"
        )
        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")
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
        self.log("component_specific_filters for port assignments: {0}".format(component_specific_filters), "DEBUG")

        self.log(
            "Extracting API family and function from network_element configuration "
            "for port assignments retrieval.",
            "DEBUG"
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API configuration extracted - family: {0}, function: {1}. Executing "
            "API call to retrieve all port assignments from Catalyst Center.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        response = self.dnac._exec(
            family=api_family,
            function=api_function,
            op_modifies=False,
        )

        all_port_assignments = response.get("response", [])
        self.log(
            "Port assignments API call completed successfully. Retrieved {0} port "
            "assignment(s) from Catalyst Center.".format(len(all_port_assignments)),
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
        if component_specific_filters:
            self.log(
                "Building fabric name to site ID mapping from cached "
                "fabric_site_id_name_dict for filter-based fabric ID resolution.",
                "DEBUG"
            )
            fabric_name_site_id_dict = {v: k for k, v in self.fabric_site_id_name_dict.items()}
            self.log("Fabric name to site ID mapping: {0}".format(fabric_name_site_id_dict), "DEBUG")

            fabric_site_name_hierarchies = component_specific_filters.get("fabric_site_name_hierarchy", [])
            self.log(
                "Extracted {0} fabric site name hierarchy filter(s) from "
                "component_specific_filters: {1}. Resolving to fabric site IDs.".format(
                    len(fabric_site_name_hierarchies), fabric_site_name_hierarchies
                ),
                "DEBUG"
            )

            for fabric_site_name_hierarchy in fabric_site_name_hierarchies:
                fabric_id = fabric_name_site_id_dict.get(fabric_site_name_hierarchy)
                if fabric_id:
                    fabric_ids.append(fabric_id)
                    self.log(
                        "Resolved fabric site name '{0}' to fabric ID '{1}'. Added to "
                        "processing list.".format(fabric_site_name_hierarchy, fabric_id),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Warning: Fabric site name '{0}' not found in cached mapping. "
                        "Skipping this fabric site.".format(fabric_site_name_hierarchy),
                        "WARNING"
                    )
        else:
            self.log(
                "No fabric site filters provided. Using all {0} cached fabric site "
                "IDs for complete port assignment retrieval.".format(
                    len(self.fabric_site_id_name_dict)
                ),
                "DEBUG"
            )
            fabric_ids = list(self.fabric_site_id_name_dict.keys())

        self.log(
            "Fabric site ID resolution completed. Will process {0} fabric site(s): "
            "{1}.".format(len(fabric_ids), fabric_ids),
            "INFO"
        )
        self.log("Fabric IDs to process for port assignments: {0}".format(fabric_ids), "DEBUG")

        self.log(
            "Grouping {0} port assignment(s) by fabric ID for organized processing. "
            "Building fabric_port_assignments_dict.".format(len(all_port_assignments)),
            "DEBUG"
        )
        # Group port assignments by fabric_id
        fabric_port_assignments_dict = {}
        for port_assignment in all_port_assignments:
            fabric_id = port_assignment.get("fabricId")
            if fabric_id in fabric_ids:
                if fabric_id not in fabric_port_assignments_dict:
                    fabric_port_assignments_dict[fabric_id] = []
                fabric_port_assignments_dict[fabric_id].append(port_assignment)

        self.log(
            "Port assignment grouping completed. Grouped into {0} fabric site(s) "
            "with assignments: {1}.".format(
                len(fabric_port_assignments_dict),
                {k: len(v) for k, v in fabric_port_assignments_dict.items()}
            ),
            "DEBUG"
        )

        # Process each fabric's port assignments
        self.log(
            "Starting fabric site iteration loop. Processing {0} fabric site(s) "
            "with port assignments.".format(len(fabric_port_assignments_dict)),
            "DEBUG"
        )

        for fabric_index, (fabric_id, port_assignments) in enumerate(fabric_port_assignments_dict.items(), start=1):
            self.log(
                "Processing fabric site {0}/{1} with ID '{2}'. Contains {3} port "
                "assignment(s).".format(
                    fabric_index, len(fabric_port_assignments_dict), fabric_id,
                    len(port_assignments)
                ),
                "DEBUG"
            )

            self.log(
                "Retrieving reverse mapping specification for port assignments "
                "transformation. Specification defines field mappings and YAML structure.",
                "DEBUG"
            )
            port_assignments_temp_spec = self.port_assignments_temp_spec()

            self.log(
                "Applying reverse mapping transformation to {0} port assignment(s) "
                "using modify_parameters(). Transformation converts API format to "
                "user-friendly YAML structure.".format(len(port_assignments)),
                "DEBUG"
            )
            modified_port_assignments = self.modify_parameters(
                port_assignments_temp_spec, port_assignments
            )
            self.log(
                "Reverse mapping transformation completed for {0} port assignment(s).".format(
                    len(modified_port_assignments)
                ),
                "DEBUG"
            )

            # Group port assignments by network device
            self.log(
                "Grouping {0} port assignment(s) by network device ID for device-based "
                "organization.".format(len(port_assignments)),
                "DEBUG"
            )
            device_port_assignments = {}
            for idx, port_assignment in enumerate(port_assignments):
                network_device_id = port_assignment.get("networkDeviceId")
                if network_device_id not in device_port_assignments:
                    device_port_assignments[network_device_id] = []
                device_port_assignments[network_device_id].append(modified_port_assignments[idx])

            self.log(
                "Port assignment device grouping completed. Grouped into {0} network "
                "device(s) with assignments: {1}.".format(
                    len(device_port_assignments),
                    {k: len(v) for k, v in device_port_assignments.items()}
                ),
                "DEBUG"
            )

            # Build the final structure with device IP addresses
            self.log(
                "Building final device configuration structures with management IP "
                "address resolution for {0} device(s).".format(len(device_port_assignments)),
                "DEBUG"
            )
            for device_index, (network_device_id, device_ports) in enumerate(device_port_assignments.items(), start=1):
                self.log(
                    "Processing device {0}/{1} with ID '{2}'. Fetching device details "
                    "to resolve management IP address.".format(
                        device_index, len(device_port_assignments), network_device_id
                    ),
                    "DEBUG"
                )
                # Get device details to fetch management IP address
                device_response = self.dnac._exec(
                    family="devices",
                    function="get_device_by_id",
                    op_modifies=False,
                    params={"id": network_device_id},
                )
                self.log("Device details response for device ID {0}: {1}".format(network_device_id, device_response), "DEBUG")
                device_info = device_response.get("response", {})
                management_ip = device_info.get("managementIpAddress", "")
                self.log(
                    "Resolved device ID '{0}' to management IP address '{1}'.".format(
                        network_device_id, management_ip
                    ),
                    "DEBUG"
                )

                device_dict = {}
                device_dict['ip_address'] = management_ip
                device_dict['fabric_site_name_hierarchy'] = self.fabric_site_id_name_dict.get(fabric_id)
                device_dict['port_assignments'] = device_ports
                all_fabric_port_assignments_details.append(device_dict)
                self.log(
                    "Added device configuration to final list. Device IP: {0}, "
                    "Fabric: {1}, Port assignments: {2}.".format(
                        management_ip, self.fabric_site_id_name_dict.get(fabric_id),
                        len(device_ports)
                    ),
                    "DEBUG"
                )

        self.log(
            "Port assignments configuration retrieval completed successfully. "
            "Retrieved {0} device configuration(s) with port assignments.".format(
                len(all_fabric_port_assignments_details)
            ),
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
            "Extracting component_specific_filters from filters dictionary: {0}. "
            "Filters determine which fabric sites to process for port channel "
            "retrieval.".format(filters),
            "DEBUG"
        )
        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")
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
        self.log("component_specific_filters for port channels: {0}".format(component_specific_filters), "DEBUG")

        self.log(
            "Extracting API family and function from network_element configuration "
            "for port channels retrieval.",
            "DEBUG"
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API configuration extracted - family: {0}, function: {1}. Executing "
            "API call to retrieve all port channels from Catalyst Center.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        response = self.dnac._exec(
            family=api_family,
            function=api_function,
            op_modifies=False,
        )

        all_port_channels = response.get("response", [])
        self.log(
            "Port channels API call completed successfully. Retrieved {0} port "
            "channel(s) from Catalyst Center.".format(len(all_port_channels)),
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
        if component_specific_filters:
            self.log(
                "Building fabric name to site ID mapping from cached "
                "fabric_site_id_name_dict for filter-based fabric ID resolution.",
                "DEBUG"
            )
            fabric_name_site_id_dict = {v: k for k, v in self.fabric_site_id_name_dict.items()}

            fabric_site_name_hierarchies = component_specific_filters.get("fabric_site_name_hierarchy", [])
            self.log(
                "Extracted {0} fabric site name hierarchy filter(s) from "
                "component_specific_filters: {1}. Resolving to fabric site IDs.".format(
                    len(fabric_site_name_hierarchies), fabric_site_name_hierarchies
                ),
                "DEBUG"
            )

            for fabric_site_name_hierarchy in fabric_site_name_hierarchies:
                fabric_id = fabric_name_site_id_dict.get(fabric_site_name_hierarchy)
                if fabric_id:
                    fabric_ids.append(fabric_id)
                    self.log(
                        "Resolved fabric site name '{0}' to fabric ID '{1}'. Added to "
                        "processing list.".format(fabric_site_name_hierarchy, fabric_id),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Warning: Fabric site name '{0}' not found in cached mapping. "
                        "Skipping this fabric site.".format(fabric_site_name_hierarchy),
                        "WARNING"
                    )
        else:
            self.log(
                "No fabric site filters provided. Using all {0} cached fabric site "
                "IDs for complete port channel retrieval.".format(
                    len(self.fabric_site_id_name_dict)
                ),
                "DEBUG"
            )
            fabric_ids = list(self.fabric_site_id_name_dict.keys())

        self.log(
            "Fabric site ID resolution completed. Will process {0} fabric site(s): "
            "{1}.".format(len(fabric_ids), fabric_ids),
            "INFO"
        )
        self.log("Fabric IDs to process for port channels: {0}".format(fabric_ids), "DEBUG")

        self.log(
            "Grouping {0} port channel(s) by fabric ID for organized processing. "
            "Building fabric_port_channels_dict.".format(len(all_port_channels)),
            "DEBUG"
        )
        # Group port channels by fabric_id
        fabric_port_channels_dict = {}
        for port_channel in all_port_channels:
            fabric_id = port_channel.get("fabricId")
            if fabric_id in fabric_ids:
                if fabric_id not in fabric_port_channels_dict:
                    fabric_port_channels_dict[fabric_id] = []
                fabric_port_channels_dict[fabric_id].append(port_channel)

        self.log(
            "Port channel grouping completed. Grouped into {0} fabric site(s) "
            "with channels: {1}.".format(
                len(fabric_port_channels_dict),
                {k: len(v) for k, v in fabric_port_channels_dict.items()}
            ),
            "DEBUG"
        )

        # Process each fabric's port channels
        self.log(
            "Starting fabric site iteration loop. Processing {0} fabric site(s) "
            "with port channels.".format(len(fabric_port_channels_dict)),
            "DEBUG"
        )

        for fabric_index, (fabric_id, port_channels) in enumerate(fabric_port_channels_dict.items(), start=1):
            self.log(
                "Processing fabric site {0}/{1} with ID '{2}'. Contains {3} port "
                "channel(s).".format(
                    fabric_index, len(fabric_port_channels_dict), fabric_id,
                    len(port_channels)
                ),
                "DEBUG"
            )

            self.log(
                "Retrieving reverse mapping specification for port channels "
                "transformation. Specification defines field mappings and YAML structure.",
                "DEBUG"
            )
            port_channels_temp_spec = self.port_channels_temp_spec()

            self.log(
                "Applying reverse mapping transformation to {0} port channel(s) "
                "using modify_parameters(). Transformation converts API format to "
                "user-friendly YAML structure.".format(len(port_channels)),
                "DEBUG"
            )
            modified_port_channels = self.modify_parameters(
                port_channels_temp_spec, port_channels
            )
            self.log(
                "Reverse mapping transformation completed for {0} port channel(s).".format(
                    len(modified_port_channels)
                ),
                "DEBUG"
            )

            # Group port channels by network device
            self.log(
                "Grouping {0} port channel(s) by network device ID for device-based "
                "organization.".format(len(port_channels)),
                "DEBUG"
            )
            device_port_channels = {}
            for idx, port_channel in enumerate(port_channels):
                network_device_id = port_channel.get("networkDeviceId")
                if network_device_id not in device_port_channels:
                    device_port_channels[network_device_id] = []
                device_port_channels[network_device_id].append(modified_port_channels[idx])

            self.log(
                "Port channel device grouping completed. Grouped into {0} network "
                "device(s) with channels: {1}.".format(
                    len(device_port_channels),
                    {k: len(v) for k, v in device_port_channels.items()}
                ),
                "DEBUG"
            )

            # Build the final structure with device IP addresses
            self.log(
                "Building final device configuration structures with management IP "
                "address resolution for {0} device(s).".format(len(device_port_channels)),
                "DEBUG"
            )
            for device_index, (network_device_id, device_port_channels_list) in enumerate(device_port_channels.items(), start=1):
                self.log(
                    "Processing device {0}/{1} with ID '{2}'. Fetching device details "
                    "to resolve management IP address.".format(
                        device_index, len(device_port_channels), network_device_id
                    ),
                    "DEBUG"
                )
                # Get device details to fetch management IP address
                device_response = self.dnac._exec(
                    family="devices",
                    function="get_device_by_id",
                    op_modifies=False,
                    params={"id": network_device_id},
                )
                self.log(
                    "Device API response received for device ID '{0}'.".format(
                        network_device_id
                    ),
                    "DEBUG"
                )
                device_info = device_response.get("response", {})
                management_ip = device_info.get("managementIpAddress", "")
                self.log(
                    "Resolved device ID '{0}' to management IP address '{1}'.".format(
                        network_device_id, management_ip
                    ),
                    "DEBUG"
                )
                device_dict = {}
                device_dict['ip_address'] = management_ip
                device_dict['fabric_site_name_hierarchy'] = self.fabric_site_id_name_dict.get(fabric_id)
                device_dict['port_channels'] = device_port_channels_list
                all_fabric_port_channels_details.append(device_dict)
                self.log(
                    "Added device configuration to final list. Device IP: {0}, "
                    "Fabric: {1}, Port channels: {2}.".format(
                        management_ip, self.fabric_site_id_name_dict.get(fabric_id),
                        len(device_port_channels_list)
                    ),
                    "DEBUG"
                )

        self.log(
            "Port channels configuration retrieval completed successfully. "
            "Retrieved {0} device configuration(s) with port channels.".format(
                len(all_fabric_port_channels_details)
            ),
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
            "Extracting component_specific_filters from filters dictionary: {0}. "
            "Filters determine which fabric sites to process for wireless SSID "
            "retrieval.".format(filters),
            "DEBUG"
        )
        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")
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
            "API configuration extracted - family: {0}, function: {1}. Will execute "
            "per-fabric API calls to retrieve VLAN/SSID mappings.".format(
                api_family, api_function
            ),
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
                "fabric_site_id_name_dict for filter-based fabric ID resolution.",
                "DEBUG"
            )
            fabric_name_site_id_dict = {v: k for k, v in self.fabric_site_id_name_dict.items()}

            fabric_site_name_hierarchies = component_specific_filters.get("fabric_site_name_hierarchy", [])
            self.log(
                "Extracted {0} fabric site name hierarchy filter(s) from "
                "component_specific_filters: {1}. Resolving to fabric site IDs.".format(
                    len(fabric_site_name_hierarchies), fabric_site_name_hierarchies
                ),
                "DEBUG"
            )

            for fabric_site_name_hierarchy in fabric_site_name_hierarchies:
                fabric_id = fabric_name_site_id_dict.get(fabric_site_name_hierarchy)
                if fabric_id:
                    fabric_ids.append(fabric_id)
                    self.log(
                        "Resolved fabric site name '{0}' to fabric ID '{1}'. Added to "
                        "processing list.".format(fabric_site_name_hierarchy, fabric_id),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Warning: Fabric site name '{0}' not found in cached mapping. "
                        "Skipping this fabric site.".format(fabric_site_name_hierarchy),
                        "WARNING"
                    )
        else:
            self.log(
                "No fabric site filters provided. Using all {0} cached fabric site "
                "IDs for complete wireless SSID retrieval.".format(
                    len(self.fabric_site_id_name_dict)
                ),
                "DEBUG"
            )
            fabric_ids = list(self.fabric_site_id_name_dict.keys())

        self.log(
            "Fabric site ID resolution completed. Will process {0} fabric site(s): "
            "{1}.".format(len(fabric_ids), fabric_ids),
            "INFO"
        )

        self.log(
            "Starting fabric site iteration loop for per-fabric wireless SSID "
            "retrieval. Processing {0} fabric site(s).".format(len(fabric_ids)),
            "DEBUG"
        )
        for fabric_index, fabric_id in enumerate(fabric_ids, start=1):
            self.log(
                "Processing fabric site {0}/{1} with ID '{2}'. Executing API call to "
                "retrieve VLAN/SSID mappings.".format(
                    fabric_index, len(fabric_ids), fabric_id
                ),
                "DEBUG"
            )
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params={"fabric_id": fabric_id},
            )

            response = response.get("response", [])
            self.log(
                "Wireless SSID API call completed for fabric ID '{0}'. Retrieved {1} "
                "VLAN/SSID mapping(s).".format(fabric_id, len(response)),
                "DEBUG"
            )

            if not response:
                self.log(
                    "No wireless SSIDs found for fabric ID '{0}' (fabric name: '{1}'). "
                    "Skipping this fabric site.".format(
                        fabric_id, self.fabric_site_id_name_dict.get(fabric_id)
                    ),
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
                "Applying reverse mapping transformation to {0} wireless SSID "
                "mapping(s) using modify_parameters(). Transformation converts API "
                "format to user-friendly YAML structure.".format(len(response)),
                "DEBUG"
            )
            wireless_ssids = self.modify_parameters(
                wireless_ssids_temp_spec, response
            )
            self.log(
                "Reverse mapping transformation completed for {0} wireless SSID "
                "mapping(s).".format(len(wireless_ssids)),
                "DEBUG"
            )

            modified_wireless_ssids_details = {}
            modified_wireless_ssids_details['fabric_site_name_hierarchy'] = self.fabric_site_id_name_dict.get(fabric_id)
            modified_wireless_ssids_details['wireless_ssids'] = wireless_ssids
            all_fabric_wireless_ssids_details.append(modified_wireless_ssids_details)
            self.log(
                "Added wireless SSID configuration to final list. Fabric: {0}, "
                "Wireless SSIDs: {1}.".format(
                    self.fabric_site_id_name_dict.get(fabric_id), len(wireless_ssids)
                ),
                "DEBUG"
            )

        self.log(
            "Wireless SSIDs configuration retrieval completed successfully. "
            "Retrieved {0} fabric site configuration(s) with wireless SSIDs.".format(
                len(all_fabric_wireless_ssids_details)
            ),
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

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates YAML configuration file for SDA host port onboarding brownfield workflow.

        This function orchestrates complete YAML playbook generation by determining
        output file path (user-provided or auto-generated), processing auto-discovery
        mode flags to override filters for complete fabric infrastructure extraction,
        iterating through requested network components (port_assignments, port_channels,
        wireless_ssids) with component-specific filters, executing retrieval functions
        for each component, aggregating configurations into unified structure, and
        writing formatted YAML file with comprehensive header comments for compatibility
        with sda_host_port_onboarding_workflow_manager module.

        Args:
            yaml_config_generator (dict): Configuration parameters containing:
                                        - generate_all_configurations (bool, optional):
                                        Auto-discovery mode flag enabling complete
                                        fabric infrastructure extraction across all sites
                                        - file_path (str, optional): Output YAML file
                                        path, defaults to auto-generated timestamped
                                        filename if not provided
                                        - global_filters (dict, optional): Reserved for
                                        future use, currently not implemented
                                        - component_specific_filters (dict, optional):
                                        Component filters with components_list and
                                        per-component filter criteria for fabric site
                                        hierarchy filtering

        Returns:
            object: Self instance with updated attributes:
                    - self.msg: Operation result message with status, file path,
                    component counts, and configuration counts
                    - self.status: Operation status ("success", "failed", or "ok")
                    - self.result: Complete operation result for module exit
                    - Operation result set via set_operation_result()

        Workflow Steps:
            1. File Path Determination - Validates user-provided file_path or generates
               default timestamped filename with pattern:
               'sda_host_port_onboarding_workflow_manager_playbook_<timestamp>.yml'
            2. Auto-Discovery Processing - If generate_all_configurations=True, overrides
               all filters to retrieve complete fabric infrastructure without restrictions
            3. Filter Extraction - Retrieves global_filters and component_specific_filters
               from yaml_config_generator parameters for targeted extraction
            4. Component Iteration - Loops through components_list (port_assignments,
               port_channels, wireless_ssids) invoking retrieval functions with filters
            5. Configuration Aggregation - Combines retrieved configurations from all
               components into unified final_config_list structure
            6. YAML Generation - Writes final_config_list to file using write_dict_to_yaml()
               with OrderedDumper for consistent key ordering and comprehensive header
            7. Result Reporting - Sets operation status with component counts, file path,
               and configuration statistics

        Component Processing Logic:
            - For each component in components_list:
                1. Validates component support via module_schema network_elements lookup
                2. Constructs filter dictionary with global and component-specific filters
                3. Retrieves get_function_name method from network_element schema
                4. Executes retrieval function passing network_element and filters
                5. Validates returned data for non-empty content
                6. Extends final_config_list with component data (flattens lists)
                7. Increments processed_count or skipped_count based on outcome

        Status Outcomes:
            - success: YAML file written successfully with at least one configuration
            - ok: No configurations found matching filters or in Catalyst Center
            - failed: File write operation failed or critical error occurred

        Error Handling:
            - Component not in module_schema: Logs warning, increments skipped_count
            - No retrieval function: Logs error, increments skipped_count, continues
            - Empty component_data: Logs debug, continues to next component
            - Empty final_config_list: Returns "ok" status with attempted component list
            - File write failure: Returns "failed" status with file path details

        Usage Examples:
            # Auto-discovery mode (all fabric sites, all components)
            yaml_config_generator({'generate_all_configurations': True})

            # Targeted extraction with fabric site filters
            yaml_config_generator({
                'file_path': 'port_configs.yml',
                'component_specific_filters': {
                    'components_list': ['port_assignments', 'port_channels'],
                    'port_assignments': {
                        'fabric_site_name_hierarchy': ['Global/USA/Building1']
                    },
                    'port_channels': {
                        'fabric_site_name_hierarchy': ['Global/USA/Building1']
                    }
                }
            })

        Notes:
            - Method is idempotent; same parameters produce identical YAML content
              except for generation timestamp in header comments
            - Check mode is honored; file generation skipped if check_mode=True
            - Empty components_list defaults to all supported components from module_schema
            - Component-specific filters are optional; omission retrieves all configurations
              for that component across all fabric sites
            - File path directory is created automatically if it doesn't exist
            - YAML uses OrderedDumper for consistent key ordering enabling version control
        """

        self.log(
            "Starting YAML configuration generation workflow for SDA host port onboarding "
            "brownfield playbook. Workflow includes file path determination, "
            "auto-discovery mode processing, component iteration with filters, and "
            "YAML file writing with header comments.",
            "DEBUG"
        )

        self.log(
            "YAML config generator parameters received: {0}. Extracting "
            "generate_all_configurations flag, file_path, and filter configurations.".format(
                yaml_config_generator
            ),
            "DEBUG"
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log(
                "Auto-discovery mode enabled (generate_all_configurations=True). Will "
                "process all SDA host port onboarding configs and all supported components "
                "without filter restrictions for complete brownfield fabric inventory.",
                "INFO"
            )
        else:
            self.log(
                "Targeted extraction mode (generate_all_configurations=False). Will "
                "apply provided filters for selective component and configuration retrieval.",
                "DEBUG"
            )

        self.log(
            "Determining output file path for YAML configuration. Checking for "
            "user-provided file_path parameter or generating default timestamped "
            "filename.",
            "DEBUG"
        )
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No file_path provided in configuration. Generating default filename "
                "with pattern <module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml in "
                "current working directory.",
                "DEBUG"
            )
            file_path = self.generate_filename()
            self.log(
                "Default filename generated: {0}. File will be created in current "
                "working directory.".format(file_path),
                "DEBUG"
            )
        else:
            self.log(
                "Using user-provided file_path: {0}. File will be created at "
                "specified location with directory creation if needed.".format(file_path),
                "DEBUG"
            )

        self.log(
            "YAML configuration file path determined: {0}. Path will be used for "
            "write_dict_to_yaml() operation.".format(file_path),
            "INFO"
        )

        self.log(
            "Initializing filter extraction from yaml_config_generator parameters. "
            "Filters control component selection (port_assignments, port_channels, "
            "wireless_ssids) and fabric site targeting for SDA configuration retrieval. "
            "Auto-discovery mode override will clear filters if generate_all_configurations=True.",
            "DEBUG"
        )
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log(
                "Auto-discovery mode: Overriding any provided filters to ensure "
                "complete fabric configuration and component extraction without restrictions."
            )

            if yaml_config_generator.get("global_filters"):
                self.log(
                    "Warning: global_filters provided ({0}) but will be ignored due to "
                    "generate_all_configurations=True. Complete infrastructure "
                    "extraction takes precedence.".format(
                        yaml_config_generator.get("global_filters")
                    ),
                    "WARNING"
                )
            if yaml_config_generator.get("component_specific_filters"):
                self.log(
                    "Warning: component_specific_filters provided ({0}) but will be "
                    "ignored because generate_all_configurations=True. All supported "
                    "components and configurations will be extracted.".format(
                        yaml_config_generator.get("component_specific_filters")
                    ),
                    "WARNING"
                )

            # Set empty filters to retrieve everything
            global_filters = {}
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}
            self.log(
                "Targeted extraction mode: Using provided filters. Global filters: {0}, "
                "Component-specific filters: {1}. Filters will be applied during "
                "component retrieval.".format(
                    bool(global_filters), bool(component_specific_filters)
                ),
                "DEBUG"
            )

        self.log(
            "Retrieving supported network elements schema from module_schema. Schema "
            "defines available components (port_assignments, port_channels, "
            "wireless_ssids) with their retrieval functions and filter specifications.",
            "DEBUG"
        )
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        self.log(
            "Module supports {0} network element component(s): {1}. Components define "
            "available SDA host port onboarding configuration types and fabric site "
            "mappings.".format(
                len(module_supported_network_elements),
                list(module_supported_network_elements.keys())
            ),
            "DEBUG"
        )

        self.log(
            "Determining components list for processing. Extracting components_list "
            "from component_specific_filters or defaulting to all supported components "
            "from module schema.",
            "DEBUG"
        )
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )

        # If components_list is empty, default to all supported components
        if not components_list:
            self.log(
                "No components specified in components_list. Defaulting to all "
                "supported components for complete SDA host port onboarding configuration "
                "extraction: {0}".format(
                    list(module_supported_network_elements.keys())
                ),
                "DEBUG"
            )
            components_list = list(module_supported_network_elements.keys())
        else:
            self.log(
                "Components list extracted from filters: {0}. Will process {1} "
                "component(s) for targeted SDA configuration retrieval.".format(
                    components_list, len(components_list)
                ),
                "DEBUG"
            )

        self.log(
            "Components to process: {0}. Starting iteration through components for "
            "SDA configuration retrieval and configuration aggregation.".format(components_list),
            "INFO"
        )

        self.log(
            "Initializing final configuration list for aggregating component data. "
            "List will contain retrieved configurations from all processed components "
            "ready for YAML serialization.",
            "DEBUG"
        )

        final_config_list = []
        processed_count = 0
        skipped_count = 0

        self.log(
            "Starting component iteration loop. Processing {0} component(s) with "
            "retrieval functions, filter application, and data aggregation for each.".format(
                len(components_list)
            ),
            "DEBUG"
        )
        for component_index, component in enumerate(components_list, start=1):
            self.log(
                "Processing component {0}/{1}: '{2}'. Checking module schema for "
                "component support and retrieval function availability.".format(
                    component_index, len(components_list), component
                ),
                "DEBUG"
            )
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Component {0} not supported by module, skipping processing".format(component),
                    "WARNING",
                )
                skipped_count += 1
                continue

            filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters.get(component, [])
            }
            self.log(
                "Filter dictionary constructed for component '{0}': global_filters={1}, "
                "component_specific_filters={2}. Filters will be passed to component "
                "retrieval function.".format(
                    component, bool(filters["global_filters"]),
                    bool(filters["component_specific_filters"])
                ),
                "DEBUG"
            )

            self.log(
                "Extracting retrieval function for component '{0}' from network element "
                "schema. Function will execute API calls and data transformation for "
                "this component.".format(component),
                "DEBUG"
            )
            operation_func = network_element.get("get_function_name")
            if not callable(operation_func):
                self.log(
                    "No retrieval function defined for component: {0}".format(component),
                    "ERROR"
                )
                skipped_count += 1
                continue

            component_data = operation_func(network_element, filters)
            # Validate retrieval success
            if not component_data:
                self.log(
                    "No data retrieved for component: {0}".format(component),
                    "DEBUG"
                )
                continue

            self.log(
                "Details retrieved for {0}: {1}".format(component, component_data), "DEBUG"
            )
            processed_count += 1

            if isinstance(component_data, list):
                final_config_list.extend(component_data)
                self.log(
                    "Component '{0}' returned list with {1} item(s). Extended final "
                    "configuration list. Total configurations: {2}".format(
                        component, len(component_data), len(final_config_list)
                    ),
                    "DEBUG"
                )
            else:
                final_config_list.append(component_data)
                self.log(
                    "Component '{0}' returned single dictionary. Appended to final "
                    "configuration list. Total configurations: {1}".format(
                        component, len(final_config_list)
                    ),
                    "DEBUG"
                )

        self.log(
            "Component iteration completed. Processed {0}/{1} component(s), skipped "
            "{2} component(s). Final configuration list contains {3} item(s) for YAML "
            "generation.".format(
                processed_count, len(components_list), skipped_count,
                len(final_config_list)
            ),
            "INFO"
        )
        if not final_config_list:
            self.log(
                "No configurations retrieved after processing {0} component(s). "
                "Processed: {1}, Skipped: {2}. All filters may have excluded available "
                "configurations or no SDA configurations exist in Catalyst Center for "
                "requested components: {3}".format(
                    len(components_list), processed_count, skipped_count, components_list
                ),
                "WARNING"
            )
            self.msg = {
                "status": "ok",
                "message": (
                    "No configurations found for module '{0}'. Verify filters and component availability. "
                    "Components attempted: {1}".format(self.module_name, components_list)
                ),
                "components_attempted": len(components_list),
                "components_processed": processed_count,
                "components_skipped": skipped_count
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        yaml_config_dict = {"config": final_config_list}
        self.log(
            "Final YAML configuration dictionary created successfully. Dictionary "
            "structure: {0}. Proceeding with write_dict_to_yaml() operation.".format(
                self.pprint(yaml_config_dict)
            ),
            "DEBUG"
        )

        self.log(
            "Writing YAML configuration dictionary to file path: {0}. Using "
            "OrderedDumper for consistent key ordering and formatting.".format(file_path),
            "DEBUG"
        )

        if self.write_dict_to_yaml(yaml_config_dict, file_path, OrderedDumper):
            self.log(
                "YAML file write operation succeeded. File created at: {0}. File "
                "contains {1} configuration(s) with header comments and formatted "
                "structure.".format(file_path, len(final_config_list)),
                "INFO"
            )
            self.msg = {
                "status": "success",
                "message": "YAML configuration file generated successfully for module '{0}'".format(
                    self.module_name
                ),
                "file_path": file_path,
                "components_processed": processed_count,
                "components_skipped": skipped_count,
                "configurations_count": len(final_config_list)
            }
            self.set_operation_result("success", True, self.msg, "INFO")

            self.log(
                "YAML configuration generation completed. File: {0}, Components: {1}/{2}, Configs: {3}".format(
                    file_path, processed_count, len(components_list), len(final_config_list)
                ),
                "INFO"
            )
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

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
                * generate_all_configurations (bool): Enable auto-discovery mode
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
        - Future: merged, deleted, replaced (reserved for future use)

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

    # Initialize the SdaHostPortOnboardingPlaybookConfigGenerator object
    # This creates the main orchestrator for SDA host port onboarding playbook config generator extraction
    catc_sda_host_port_onboarding_playbook_config_generator = SdaHostPortOnboardingPlaybookConfigGenerator(module)

    # Log module initialization after object creation (now logging is available)
    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Starting Ansible module execution for SDA host port onboarding playbook config generator "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    catc_sda_host_port_onboarding_playbook_config_generator.log(
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
    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.7.9 for SDA host port onboarding APIs".format(
            catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version()
        ),
        "INFO"
    )

    if (
        catc_sda_host_port_onboarding_playbook_config_generator.compare_dnac_versions(
            catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for SDA Host Port Onboarding module. Supported versions start "
            "from '2.3.7.9' onwards. Version '2.3.7.9' introduces APIs for retrieving "
            "SDA host port onboarding configurations for the following components: Port Assignments, "
            "Port Channels, and Wireless SSIDs from the Catalyst Center.".format(
                catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version()
            )
        )

        catc_sda_host_port_onboarding_playbook_config_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        catc_sda_host_port_onboarding_playbook_config_generator.msg = error_msg
        catc_sda_host_port_onboarding_playbook_config_generator.set_operation_result(
            "failed", False, catc_sda_host_port_onboarding_playbook_config_generator.msg, "ERROR"
        ).check_return_status()

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required SDA host port onboarding APIs".format(
            catc_sda_host_port_onboarding_playbook_config_generator.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = catc_sda_host_port_onboarding_playbook_config_generator.params.get("state")

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, catc_sda_host_port_onboarding_playbook_config_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in catc_sda_host_port_onboarding_playbook_config_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, catc_sda_host_port_onboarding_playbook_config_generator.supported_states
            )
        )

        catc_sda_host_port_onboarding_playbook_config_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        catc_sda_host_port_onboarding_playbook_config_generator.status = "invalid"
        catc_sda_host_port_onboarding_playbook_config_generator.msg = error_msg
        catc_sda_host_port_onboarding_playbook_config_generator.check_return_status()

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "State validation passed - using state '{0}' for workflow execution".format(
            state
        ),
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
        "Starting configuration processing loop - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        catc_sda_host_port_onboarding_playbook_config_generator.log(
            "Processing configuration item {0}/{1} for state '{2}'".format(
                config_index, len(config_list), state
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        catc_sda_host_port_onboarding_playbook_config_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        catc_sda_host_port_onboarding_playbook_config_generator.reset_values()

        # Collect desired state (want) from configuration
        catc_sda_host_port_onboarding_playbook_config_generator.log(
            "Collecting desired state parameters from configuration item {0}".format(
                config_index
            ),
            "DEBUG"
        )
        catc_sda_host_port_onboarding_playbook_config_generator.get_want(
            config, state
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        catc_sda_host_port_onboarding_playbook_config_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1}".format(state, config_index),
            "INFO"
        )
        catc_sda_host_port_onboarding_playbook_config_generator.get_diff_state_apply[
            state
        ]().check_return_status()

        catc_sda_host_port_onboarding_playbook_config_generator.log(
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

    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Module execution completed successfully at timestamp {0}. Total execution "
        "time: {1:.2f} seconds. Processed {2} configuration item(s) with final "
        "status: {3}".format(
            completion_timestamp,
            module_duration,
            len(config_list),
            catc_sda_host_port_onboarding_playbook_config_generator.status
        ),
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    catc_sda_host_port_onboarding_playbook_config_generator.log(
        "Exiting Ansible module with result: {0}".format(
            catc_sda_host_port_onboarding_playbook_config_generator.result
        ),
        "DEBUG"
    )

    module.exit_json(**catc_sda_host_port_onboarding_playbook_config_generator.result)


if __name__ == "__main__":
    main()

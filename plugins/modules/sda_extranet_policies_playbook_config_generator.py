#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for SDA Extranet Policies Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Apoorv Bansal, Madhan Sankaranarayanan"
DOCUMENTATION = r"""
---
module: sda_extranet_policies_playbook_config_generator
short_description: Generate YAML playbooks for SDA extranet
  policies from existing configurations.
description:
- Generates YAML playbooks compatible with the
  C(sda_extranet_policies_workflow_manager) module by
  extracting existing SDA extranet policy configurations
  from Cisco Catalyst Center.
- Reduces manual effort by programmatically retrieving
  extranet policy details including provider virtual
  networks, subscriber virtual networks, and fabric
  site assignments.
- Supports selective filtering by extranet policy name
  to generate targeted playbooks.
- Enables complete infrastructure discovery with
  auto-generation mode when
  C(generate_all_configurations) is enabled.
- Resolves fabric site UUIDs to human-readable site
  hierarchy paths for generated playbooks.
- Requires Cisco Catalyst Center version 2.3.7.9 or
  higher for SDA extranet policy API support.
version_added: 6.45.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
options:
  state:
    description:
    - The desired state for the module operation.
    - Only C(gathered) state is supported to generate
      YAML playbooks from existing configurations.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of configuration filters for generating
      YAML playbooks compatible with the
      C(sda_extranet_policies_workflow_manager) module.
    - Each configuration entry can include file path
      specification, component filters, and
      auto-discovery settings.
    - Multiple configuration entries can be provided to
      generate separate playbooks with different filter
      criteria.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - Enables automatic discovery and generation of
          YAML configurations for all SDA extranet
          policies.
        - When C(true), retrieves all extranet policies
          from Cisco Catalyst Center without requiring
          specific filters.
        - Overrides any provided
          C(component_specific_filters) to ensure
          complete configuration retrieval.
        - Ideal for complete brownfield infrastructure
          migration and documentation.
        - "Default filename format when file_path not
          provided:
          C(sda_extranet_policies_workflow_manager_playbook_<timestamp>.yml)"
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Absolute or relative path where the generated
          YAML playbook file will be saved.
        - If not provided, the file is saved in the
          current working directory with an
          auto-generated filename.
        - "Default filename format: C(<module_name>playbook<YYYY-MM-DD_HH-MM-SS>.yml)."
        - Ensure the directory path exists and has write
          permissions.
        type: str
      global_filters:
        description:
        - Global-level filters that apply across all
          components.
        - Currently not used by this module but reserved
          for future extensibility.
        type: dict
        required: false
      component_specific_filters:
        description:
        - Absolute or relative path where the generated
          YAML playbook file will be saved.
        - If not provided, the file is saved in the
          current working directory with an
          auto-generated filename.
        - "Default filename format:
          C(sda_extranet_policies_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml)"
        - Ensure the directory path exists and has write
          permissions.
        type: dict
        suboptions:
          components_list:
            description:
            - List of component types to include in the
              generated YAML playbook.
            - Currently supports only
              C(extranet_policies) for SDA extranet
              policy configurations.
            - If omitted, all supported components are
              included by default.
            type: list
            elements: str
            choices:
            - extranet_policies
            required: false
          extranet_policies:
            description:
            - Filters for retrieving specific extranet
              policy configurations from Cisco Catalyst
              Center.
            - Multiple filter entries can be specified
              to target different policies.
            - If no filters are provided, all extranet
              policies are retrieved.
            type: list
            elements: dict
            required: false
            suboptions:
              extranet_policy_name:
                description:
                - Name of the extranet policy to filter.
                - Must match the exact policy name as
                  configured in Cisco Catalyst Center.
                - "Example: C(Test_1)"
                type: str
                required: false
author:
- Apoorv Bansal (@Apoorv74-dot)
- Madhan Sankaranarayanan (@madhansansel)
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
- Cisco Catalyst Center >= 2.3.7.9
- Requires minimum Cisco Catalyst Center version 2.3.7.9
  for SDA extranet policies API support.
- Module will fail with an error if connected to an
  unsupported version.
- Generated playbooks are compatible with the
  C(sda_extranet_policies_workflow_manager) module for
  extranet policy management operations.
- Fabric site UUIDs are automatically resolved to
  human-readable site hierarchy paths in the generated
  playbook.
- The module operates in check mode but does not make
  any changes to Cisco Catalyst Center.
- Use C(dnac_log) and C(dnac_log_level) parameters for
  detailed operation logging and troubleshooting.
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - sda.Sda.get_extranet_policies
    - sda.Sda.get_fabric_sites
    - sda.Sda.get_fabric_zones
    - sda.Sda.get_fabric_sites_by_id
    - sda.Sda.get_fabric_zones_by_id
- Paths used are
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/sda/extranet-policies
    - GET /dna/intent/api/v1/sda/fabric-sites
    - GET /dna/intent/api/v1/sda/fabric-zones
    - GET /dna/intent/api/v1/sda/fabric-sites/{id}
    - GET /dna/intent/api/v1/sda/fabric-zones/{id}
seealso:
- module: cisco.dnac.sda_extranet_policies_workflow_manager
  description: Manage SDA extranet policies in Cisco
    Catalyst Center
"""

EXAMPLES = r"""
- name: Generate YAML playbook for all SDA extranet policies
  cisco.dnac.sda_extranet_policies_playbook_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    config:
      - generate_all_configurations: true

- name: Generate YAML playbook for all SDA extranet policies with custom file path
  cisco.dnac.sda_extranet_policies_playbook_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    config:
      - generate_all_configurations: true
        file_path: "/tmp/all_extranet_policies.yml"

- name: Generate YAML playbook for specific extranet policy by name
  cisco.dnac.sda_extranet_policies_playbook_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    config:
      - component_specific_filters:
          components_list:
            - extranet_policies
          extranet_policies:
            - extranet_policy_name: "Test_1"

- name: Generate YAML playbook for multiple specific extranet policies
  cisco.dnac.sda_extranet_policies_playbook_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: DEBUG
    state: gathered
    config:
      - file_path: "/tmp/selected_extranet_policies.yml"
        component_specific_filters:
          components_list:
            - extranet_policies
          extranet_policies:
            - extranet_policy_name: "Test_1"
            - extranet_policy_name: "Test_2"
            - extranet_policy_name: "Test_3"

- name: Generate multiple playbooks with different filters
  cisco.dnac.sda_extranet_policies_playbook_config_generator:
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
      - file_path: "/tmp/policy_test1.yml"
        component_specific_filters:
          extranet_policies:
            - extranet_policy_name: "Test_1"
      - file_path: "/tmp/all_policies.yml"
        generate_all_configurations: true
"""


RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample:
    msg:
      "YAML config generation Task succeeded for module 'sda_extranet_policies_workflow_manager'":
        file_path: "sda_extranet_policies_workflow_manager_playbook_2026-02-03_15-22-02.yml"
    response:
      "YAML config generation Task succeeded for module 'sda_extranet_policies_workflow_manager'":
        file_path: "sda_extranet_policies_workflow_manager_playbook_2026-02-03_15-22-02.yml"

# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: on failure
  type: dict
  sample:
    response: []
    msg: "YAML config generation Task failed for module 'sda_extranet_policies_workflow_manager': Invalid file path"
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
        """Custom YAML dumper preserving OrderedDict key order."""

        def represent_dict(self, data):
            """Represent OrderedDict as YAML mapping."""
            return self.represent_mapping(
                "tag:yaml.org,2002:map", data.items()
            )

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class SdaExtranetPoliciesPlaybookConfigGenerator(DnacBase, BrownFieldHelper):
    """
    Playbook config generator for SDA extranet policies.
    Attributes:
        supported_states (list): Supported Ansible states
            (only 'gathered').
        module_schema (dict): Workflow filters schema
            defining network elements and API mappings.
        site_id_name_dict (dict): Cached mapping of site
            IDs to hierarchical site names.
        module_name (str): Target module name for generated
            playbooks
            ('sda_extranet_policies_workflow_manager').
        values_to_nullify (list): Values treated as null
            during transformation.

    Description:
        Retrieves existing SDA extranet policy configurations
        from Cisco Catalyst Center and generates YAML
        playbooks compatible with the
        sda_extranet_policies_workflow_manager module.
        Supports filtering by policy name or complete
        auto-discovery mode. Transforms fabric site UUIDs
        to human-readable site hierarchies. Requires Cisco
        Catalyst Center version 2.3.7.9 or higher.
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
        self.site_id_name_dict = self.get_site_id_name_mapping()
        self.module_name = "sda_extranet_policies_workflow_manager"

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
            "file_path": {
                "type": "str",
                "required": False,
            },
            "component_specific_filters": {
                "type": "dict",
                "required": False,
            },
            "global_filters": {
                "type": "dict",
                "required": False,
            },
        }
        allowed_keys = set(temp_spec.keys())
        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(
            self.config, start=1
        ):
            self.log(
                "Validating configuration item "
                "{0}/{1}".format(
                    config_index, len(self.config)
                ),
                "DEBUG",
            )
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

        # Import validate_list_of_dicts function here to avoid circular imports
        from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts
        self.log("Validating configuration parameters against schema", "DEBUG")
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

    def get_workflow_filters_schema(self):
        """
        Description:
            Constructs and returns a structured mapping for managing extranet policy elements.
            This mapping includes associated filters, temporary specification functions,
            API details, and fetch function references used in the extranet policies
            workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods.

        Return:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a network component
                (e.g., 'extranet_policies') and maps to:
                    - "filters": List of filter keys relevant to the component (e.g., ["extranet_policy_name"]).
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component (e.g., "get_extranet_policies").
                    - "api_family": API family name (e.g., 'sda').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
                - "global_filters": An empty list reserved for global filters applicable across all network elements.
        """

        self.log(
            "Building workflow filters schema for SDA "
            "extranet policies",
            "DEBUG",
        )

        schema = {
            "network_elements": {
                "extranet_policies": {
                    "filters": ["extranet_policy_name"],
                    "reverse_mapping_function": (
                        self.extranet_policy_temp_spec
                    ),
                    "api_function": "get_extranet_policies",
                    "api_family": "sda",
                    "get_function_name": (
                        self
                        .get_extranet_policies_configuration
                    ),
                },
            },
            "global_filters": [],
        }

        network_elements = list(
            schema["network_elements"].keys()
        )
        self.log(
            "Built workflow schema with {0} network "
            "element type(s): {1}".format(
                len(network_elements), network_elements
            ),
            "DEBUG",
        )
        return schema

    def transform_fabric_site_ids_to_names(self, extranet_policy_details):
        """
        Transform fabric site IDs into human-readable site name hierarchies for extranet policies.

        Converts fabric site IDs from Cisco Catalyst Center's internal UUID format into
        their corresponding hierarchical site name paths (e.g., "Global/USA/San Jose/Building1"),
        enabling user-friendly YAML playbook generation and configuration management.

        Purpose:
            Provides human-readable site references in generated playbooks by mapping
            internal fabric IDs to site hierarchy paths, supporting infrastructure-as-code
            workflows for SDA extranet policy management.

        Args:
            self: Instance containing site_id_name_dict mapping and helper methods
            extranet_policy_details (dict): Extranet policy configuration containing:
                - fabricIds (list[str]): List of fabric site/zone UUIDs from Catalyst Center
                - Other policy details (not processed by this method)

        Returns:
            list[str]: Fabric site name hierarchies in order:
                - Format: "Global/Region/Site/Building"
                - Only includes successfully resolved site names
                - Returns empty list if no fabricIds or resolution failures

        Processing Flow:
            1. Extract fabricIds list from policy details
            2. For each fabric ID:
                a. Analyze ID to extract site_id and fabric_type
                b. Lookup site_id in site_id_name_dict
                c. Add resolved site name to results
                d. Log warning if resolution fails
            3. Return consolidated site name list

        Site Name Resolution:
            - Uses pre-populated site_id_name_dict from get_sites() API
            - Handles both fabric sites and fabric zones
            - Skips IDs that cannot be resolved (logs warning)

        Example Transformation:
            Input:
                fabricIds: ["550e8400-e29b-41d4-a716-446655440000"]

            Output:
                ["Global/USA/California/San Jose/Building21"]

        Logging:
            - DEBUG: Start/completion with counts
            - DEBUG: Successful site name resolution
            - WARNING: Failed site ID lookups
        """

        self.log("Starting transformation of fabric site IDs to names for extranet policy.", "DEBUG")
        fabric_ids = extranet_policy_details.get("fabricIds", [])
        if not fabric_ids:
            self.log(
                "No fabric IDs found in extranet policy "
                "details, returning empty list",
                "DEBUG",
            )
            return []

        self.log(
            "Processing {0} fabric ID(s) for site name "
            "resolution".format(len(fabric_ids)),
            "DEBUG",
        )

        fabric_site_names = []
        for index, fabric_id in enumerate(fabric_ids, start=1):
            site_id, fabric_type = (
                self.analyse_fabric_site_or_zone_details(
                    fabric_id
                )
            )
            site_name_hierarchy = (
                self.site_id_name_dict.get(site_id)
            )

            if not site_name_hierarchy:
                self.log(
                    "Unable to resolve site name for fabric "
                    "ID {0}/{1}: '{2}' (site_id: '{3}'). "
                    "The site may have been deleted or the "
                    "ID is invalid.".format(
                        index, len(fabric_ids),
                        fabric_id, site_id,
                    ),
                    "WARNING",
                )
                continue

            fabric_site_names.append(site_name_hierarchy)
            self.log(
                "Resolved fabric ID {0}/{1}: '{2}' "
                "(type: {3}) to site name: "
                "'{4}'".format(
                    index, len(fabric_ids),
                    fabric_id, fabric_type,
                    site_name_hierarchy,
                ),
                "DEBUG",
            )
        return fabric_site_names

    def extranet_policy_temp_spec(self):

        """
        Generate temporary specification mapping for transforming SDA extranet policy data structures.

        Creates an OrderedDict schema that defines the mapping between Cisco Catalyst Center
        API response fields (camelCase) and Ansible playbook YAML fields (snake_case),
        including data type definitions and special transformation functions.

        Purpose:
            Provides a structured specification for the modify_parameters() method to
            consistently transform raw API responses into Ansible-compatible YAML configuration
            format, ensuring standardized playbook generation across all extranet policies.

        Returns:
            OrderedDict: Specification mapping with structure:
                {
                    "yaml_field_name": {
                        "type": "str|list|dict|bool|int",
                        "source_key": "apiResponseFieldName",
                        "special_handling": bool (optional),
                        "transform": callable (optional)
                    }
                }

        Specification Fields:
            1. extranet_policy_name (str):
                - Source: extranetPolicyName
                - Policy identifier name
                - Required field for policy operations

            2. provider_virtual_network (str):
                - Source: providerVirtualNetworkName
                - Provider VN name providing services
                - Single VN per extranet policy

            3. subscriber_virtual_networks (list[str]):
                - Source: subscriberVirtualNetworkNames
                - List of subscriber VNs consuming services
                - Multiple subscribers supported

            4. fabric_sites (list[str]):
                - Special handling: True
                - Transform: transform_fabric_site_ids_to_names()
                - Converts fabric UUIDs to site hierarchies
                - Custom transformation function applied

        Transform Function Usage:
            - Standard fields: Direct mapping via source_key
            - Special fields: Transformation function called with policy details
            - fabric_sites: Converts fabricIds→site names via transform method

        Integration with modify_parameters():
            The temp_spec is consumed by modify_parameters() to:
            1. Iterate through extranet policy list
            2. For each field in temp_spec:
                a. Extract value from API response using source_key
                b. Apply transform function if special_handling=True
                c. Set YAML field with transformed value
            3. Return list of transformed policy dictionaries

        Example Output Format:
            OrderedDict([
                ("extranet_policy_name", {"type": "str", "source_key": "extranetPolicyName"}),
                ("provider_virtual_network", {"type": "str", "source_key": "providerVirtualNetworkName"}),
                ("subscriber_virtual_networks", {"type": "list", "source_key": "subscriberVirtualNetworkNames"}),
                ("fabric_sites", {"type": "list", "special_handling": True, "transform": <function>})
            ])

        Usage Pattern:
            temp_spec = self.extranet_policy_temp_spec()
            transformed_policies = self.modify_parameters(temp_spec, raw_api_response)
        """
        self.log(
            "Generating reverse mapping specification for "
            "extranet policy transformation",
            "DEBUG",
        )
        extranet_policy = OrderedDict(
            {
                "extranet_policy_name": {
                    "type": "str",
                    "source_key": "extranetPolicyName"
                },
                "provider_virtual_network": {
                    "type": "str",
                    "source_key": "providerVirtualNetworkName"
                },
                "subscriber_virtual_networks": {
                    "type": "list",
                    "source_key": "subscriberVirtualNetworkNames"
                },
                "fabric_sites": {
                    "type": "list",
                    "special_handling": True,
                    "transform": self.transform_fabric_site_ids_to_names
                },
            }
        )
        return extranet_policy

    def get_extranet_policies_configuration(self, network_element, filters=None):
        """
        Retrieve and transform SDA extranet policies configuration from Cisco Catalyst Center.

        Executes API calls to fetch extranet policy details from Catalyst Center, applies
        filtering based on policy names if specified, transforms raw API responses into
        Ansible-compatible format, and returns structured configuration data suitable for
        YAML playbook generation.

        Purpose:
            Serves as the primary data retrieval function for SDA extranet policies brownfield
            documentation, enabling discovery and export of existing multi-VN connectivity
            configurations across SDA fabric deployments.

        Args:
            self: Instance with API execution methods, transformation utilities, and logging
            network_element (dict): Component metadata from workflow schema containing:
                - api_family (str): "sda" - API family for extranet operations
                - api_function (str): "get_extranet_policies" - API method name
                - filters (list): Supported filter field names
                - reverse_mapping_function (callable): Temp spec generator reference
                - get_function_name (callable): This function reference

            component_specific_filters (list[dict], optional): Filter criteria:
                Format: [{"extranet_policy_name": "Policy_Name"}, ...]
                - extranet_policy_name (str): Specific policy name to retrieve
                - Multiple filters supported for batch retrieval
                - None/empty: Retrieves ALL extranet policies

        Returns:
            dict: Transformed extranet policies configuration:
                {
                    "extranet_policies": [
                        {
                            "extranet_policy_name": str,
                            "provider_virtual_network": str,
                            "subscriber_virtual_networks": list[str],
                            "fabric_sites": list[str]  # Site hierarchies, not UUIDs
                        },
                        ...
                    ]
                }
                Returns {"extranet_policies": []} if no policies found

        Processing Workflow:
            1. Extract API family and function from network_element
            2. Initialize results collection list
            3. Apply filtering logic:
                a. If filters provided: Process each filter individually
                b. If no filters: Retrieve all policies via pagination
            4. For filtered retrieval:
                - Iterate through filter parameters
                - Extract policy name from filter
                - Build filter_params dict {"extranetPolicyName": value}
                - Execute API call with filters
                - Append results to collection
            5. For full retrieval:
                - Execute paginated API call with empty params
                - Collect all policies from Catalyst Center
            6. Transform results:
                - Generate extranet_policy_temp_spec()
                - Apply modify_parameters(temp_spec, policies)
                - Convert API format to YAML format
            7. Return structured result dictionary

        API Integration:
            - Family: sda
            - Function: get_extranet_policies
            - Pagination: Handled by execute_get_with_pagination()
            - Response: List of extranet policy objects

        Data Transformation:
            Raw API Response (camelCase):
                {
                    "extranetPolicyName": "Test_Policy_1",
                    "providerVirtualNetworkName": "Provider_VN",
                    "subscriberVirtualNetworkNames": ["Subscriber_VN1", "Subscriber_VN2"],
                    "fabricIds": ["uuid-1", "uuid-2"]
                }

            Transformed Output (snake_case):
                {
                    "extranet_policy_name": "Test_Policy_1",
                    "provider_virtual_network": "Provider_VN",
                    "subscriber_virtual_networks": ["Subscriber_VN1", "Subscriber_VN2"],
                    "fabric_sites": ["Global/USA/Site1", "Global/USA/Site2"]
                }

        Filter Examples:
            # Retrieve specific policy
            filters = [{"extranet_policy_name": "Production_Extranet"}]

            # Retrieve multiple policies
            filters = [
                {"extranet_policy_name": "Prod_Extranet"},
                {"extranet_policy_name": "Dev_Extranet"}
            ]

            # Retrieve all policies
            filters = None

        Error Handling:
            - API failures: Logged and propagated to calling function
            - Empty results: Returns empty list, not error
            - Invalid filter names: Logged as warning, skipped
            - Failed transformations: Logged and may cause failures

        Logging:
            - DEBUG: Start, filter details, API calls, transformation process
            - INFO: Completion with counts
            - WARNING: Invalid filters, missing data
            - ERROR: API failures, transformation errors
        """
        component_specific_filters = None
        if isinstance(filters, dict):
            component_specific_filters = filters.get("component_specific_filters")
        else:
            component_specific_filters = filters
        self.log("Starting retrieval of extranet policies configuration.", "DEBUG")
        self.log("Network element details: {0}".format(network_element), "DEBUG")
        self.log("Component specific filters: {0}".format(component_specific_filters), "DEBUG")
        final_extranet_policies = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if component_specific_filters:
            # Process filters for specific policies
            self.log(
                "Processing {0} component-specific "
                "filter(s) for extranet policies".format(
                    len(component_specific_filters)
                ),
                "DEBUG",
            )
            for filter_index, filter_param in enumerate(
                component_specific_filters, start=1
            ):
                for key, value in filter_param.items():
                    if key != "extranet_policy_name":
                        self.log(
                            "Skipping unsupported filter "
                            "key '{0}' in filter entry "
                            "{1}/{2}. Only "
                            "'extranet_policy_name' is "
                            "supported.".format(
                                key,
                                filter_index,
                                len(component_specific_filters),
                            ),
                            "WARNING",
                        )
                        continue

                    self.log(
                        "Retrieving extranet policy by "
                        "name: '{0}' (filter {1}/"
                        "{2})".format(
                            value,
                            filter_index,
                            len(component_specific_filters),
                        ),
                        "INFO",
                    )
                    params = {"extranetPolicyName": value}
                    policies = self.execute_get_with_pagination(
                        api_family, api_function, params
                    )
                    final_extranet_policies.extend(policies)
                    self.log(
                        "Retrieved {0} policy(ies) for "
                        "name '{1}' (filter {2}/"
                        "{3})".format(
                            len(policies),
                            value,
                            filter_index,
                            len(component_specific_filters),
                        ),
                        "DEBUG",
                    )
        else:
            # Retrieve all policies
            self.log("No filters provided. Retrieving all extranet policies.", "INFO")
            policies = self.execute_get_with_pagination(api_family, api_function, {})
            final_extranet_policies.extend(policies)
            self.log("Retrieved {0} total extranet policies.".format(len(policies)), "DEBUG")

        # Transform using temp_spec
        if not final_extranet_policies:
            self.log(
                "No extranet policies found matching the "
                "specified filters. Returning empty "
                "result.",
                "WARNING",
            )
            return {"extranet_policies": []}

        self.log(
            "Transforming {0} extranet policy(ies) using "
            "reverse mapping specification".format(
                len(final_extranet_policies)
            ),
            "DEBUG",
        )
        extranet_policy_temp_spec = self.extranet_policy_temp_spec()
        ep_details = self.modify_parameters(extranet_policy_temp_spec, final_extranet_policies)

        result = {'extranet_policies': ep_details}
        self.log("Completed extranet policies configuration retrieval. Returning {0} transformed policies.".format(
            len(ep_details)), "INFO")
        return result

    def get_diff_gathered(self):
        """
        Execute the 'gathered' state workflow for SDA extranet policies playbook generation.

        Orchestrates the complete brownfield extraction workflow by iterating through
        defined operations, executing the YAML config generator with prepared parameters
        from the 'want' state, and consolidating results into the module's result dictionary.

        Purpose:
            Implements the 'gathered' state behavior for the sda_extranet_policies_playbook_config_generator
            module, coordinating the retrieval of existing extranet policy configurations from
            Cisco Catalyst Center and generation of Ansible-compatible YAML playbook files.

        Args:
            self: Instance containing:
                - self.want (dict): Prepared parameters from get_want()
                - self.module_name (str): "sda_extranet_policies_workflow_manager"
                - Operation methods (yaml_config_generator)
                - Result tracking (self.result, self.status, self.msg)

        Returns:
            self: Current instance with updated result:
                - self.result (dict): Ansible module result containing:
                    * changed (bool): Whether YAML file was written
                    * msg (dict/str): Operation result message
                    * response (dict): Detailed operation results
                    * file_path (str): Path to generated YAML file
                - self.status (str): "success" or "failed"
                - self.msg (dict/str): Operation outcome message

        Operations List:
            Processes a sequential list of operations defined as tuples:
            [
                (
                    param_key: "yaml_config_generator",
                    operation_name: "YAML Config Generator",
                    operation_func: self.yaml_config_generator
                )
            ]

            Future operations can be added to this list for additional
            extranet policy processing tasks.

        Workflow Execution:
            1. Record start time for performance tracking
            2. Log workflow initiation
            3. Define operations list with:
                - Parameter key from want dictionary
                - Human-readable operation name
                - Callable operation function
            4. Iterate through operations:
                a. Log iteration details with index
                b. Extract parameters from want using param_key
                c. Check if parameters exist
                d. If parameters present:
                    - Log operation start
                    - Execute operation_func(params)
                    - Call check_return_status() to validate result
                    - Continue to next operation
                e. If parameters absent:
                    - Log warning about missing parameters
                    - Skip operation
            5. Calculate and log execution time
            6. Return self for method chaining

        Operation Execution Flow:
            For yaml_config_generator operation:
            1. Extract params = self.want.get("yaml_config_generator")
            2. Verify params is not None/empty
            3. Execute self.yaml_config_generator(params)
            4. yaml_config_generator workflow:
                - Determine file path
                - Apply filters
                - Retrieve extranet policies
                - Transform to YAML format
                - Write to file
                - Set operation result
            5. check_return_status() validates:
                - Operation completed successfully
                - No critical errors occurred
                - Result properly populated
            6. If check fails: Module exits with error
            7. If check passes: Continue to next operation

        State Application:
            The get_diff_state_apply dictionary maps states to methods:
            {
                "gathered": self.get_diff_gathered  # This method
            }

            Called from main() as:
            get_diff_state_apply[state]().check_return_status()

        Performance Tracking:
            - Logs total execution time at completion
            - Useful for monitoring large deployments
            - Format: "Completed 'get_diff_gathered' operation in X.XX seconds."

        Error Handling:
            - Missing parameters: Logged as WARNING, operation skipped
            - Operation failures: Caught by check_return_status()
            - check_return_status() exits module on failure
            - No exception handling needed (delegated to operations)

        Logging:
            - DEBUG: Workflow start/end, timing, iteration details
            - INFO: Operation execution, parameter validation
            - WARNING: Missing parameters, skipped operations
            - ERROR: Operation failures (via operation functions)

        Method Chaining:
            Returns self to support fluent interface:
            get_diff_gathered().check_return_status()

        Result Structure After Execution:
            Success:
            {
                "changed": True,
                "msg": {
                    "YAML config generation Task succeeded for module 'sda_extranet_policies_workflow_manager'": {
                        "file_path": "/path/to/generated/file.yml"
                    }
                },
                "response": {
                    "YAML config generation Task succeeded for module 'sda_extranet_policies_workflow_manager'": {
                        "file_path": "/path/to/generated/file.yml"
                    }
                }
            }

            Failure:
            {
                "failed": True,
                "msg": "YAML config generation Task failed for module 'sda_extranet_policies_workflow_manager': <error details>",
                "error": "<detailed error information>"
            }

        Future Extensibility:
            Additional operations can be added to the operations list:
            - Policy validation
            - Configuration drift detection
            - Policy compliance checking
            - Multi-site policy aggregation

            Example:
            operations = [
                ("yaml_config_generator", "YAML Config Generator", self.yaml_config_generator),
                ("policy_validator", "Policy Validator", self.validate_policies),
                ("drift_detector", "Drift Detector", self.detect_drift)
            ]

        Check-Mode Behavior:
            - Operations should respect Ansible check mode
            - YAML generation may or may not occur in check mode
            - Depends on implementation of operation functions
        """

        start_time = time.time()
        self.log(
            "Starting YAML playbook generation workflow "
            "for SDA extranet policies",
            "INFO",
        )
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
        elapsed_time = time.time() - start_time
        self.log(
            "Completed gathered state workflow in "
            "{0:.2f} seconds".format(elapsed_time),
            "INFO",
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center SDA extranet policies playbook config generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for SDA extranet policies extraction.

    Purpose:
        Initializes and executes the SDA extranet policies playbook config generator
        workflow to extract existing extranet policy configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files for SDA fabric extranet policies.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create SdaExtranetPoliciesPlaybookConfigGenerator instance
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
        - Introduced APIs for SDA extranet policies:
            * get_extranet_policies (SDA API family)
            * Extranet policy details retrieval
            * Fabric site and virtual network associations

    Supported States:
        - gathered: Extract existing SDA extranet policies and generate YAML playbook
        - Future: merged, deleted, replaced (reserved for future use)

    Configuration Options:
        - generate_all_configurations (bool): Auto-discover and export all extranet policies
        - component_specific_filters (dict): Filter specific policies by name
        - file_path (str): Custom output file path for generated playbook

    Extranet Policy Components:
        - extranet_policy_name: Name identifier for the policy
        - provider_virtual_network: Provider VN associated with the policy
        - subscriber_virtual_networks: List of subscriber VNs
        - fabric_sites: List of fabric site hierarchies where policy is deployed

    Error Handling:
        - Version compatibility failures: Module exits with error
        - Invalid state parameter: Module exits with error
        - Input validation failures: Module exits with error
        - Configuration processing errors: Module exits with error
        - All errors are logged and returned via module.fail_json()

    Return Format:
        Success: module.exit_json() with result containing:
            - changed (bool): Whether changes were made
            - msg (dict/str): Operation result message with file path
            - response (dict): Detailed operation results
            - file_path (str): Path to generated YAML playbook

        Failure: module.fail_json() with error details:
            - failed (bool): True
            - msg (str): Error message
            - error (str): Detailed error information

    Examples:
        See EXAMPLES constant for usage patterns including:
        - Generate all extranet policies
        - Filter specific policies by name
        - Custom file path specification
    """
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
    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_sda_extranet_policies_playbook_config_generator = SdaExtranetPoliciesPlaybookConfigGenerator(module)
    ccc_sda_extranet_policies_playbook_config_generator.log(
        "Starting SDA extranet policies playbook "
        "generator execution",
        "INFO",
    )
    if (
        ccc_sda_extranet_policies_playbook_config_generator.compare_dnac_versions(
            ccc_sda_extranet_policies_playbook_config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_sda_extranet_policies_playbook_config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for SDA Extranet Policies Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_sda_extranet_policies_playbook_config_generator.get_ccc_version()
            )
        )
        ccc_sda_extranet_policies_playbook_config_generator.set_operation_result(
            "failed", False, ccc_sda_extranet_policies_playbook_config_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_extranet_policies_playbook_config_generator.params.get("state")
    ccc_sda_extranet_policies_playbook_config_generator.log(
        "Validating requested state '{0}' against "
        "supported states: {1}".format(
            state, ccc_sda_extranet_policies_playbook_config_generator.supported_states
        ),
        "DEBUG",
    )
    # Check if the state is valid
    if state not in ccc_sda_extranet_policies_playbook_config_generator.supported_states:
        ccc_sda_extranet_policies_playbook_config_generator.status = "invalid"
        ccc_sda_extranet_policies_playbook_config_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_sda_extranet_policies_playbook_config_generator.check_return_status()
    ccc_sda_extranet_policies_playbook_config_generator.log(
        "State '{0}' validated successfully".format(
            state
        ),
        "INFO",
    )

    # Validate the input parameters and check the return statusk
    ccc_sda_extranet_policies_playbook_config_generator.validate_input().check_return_status()
    # Validate input configuration
    ccc_sda_extranet_policies_playbook_config_generator.log(
        "Starting validation of input configuration "
        "parameters from playbook",
        "DEBUG",
    )
    config = ccc_sda_extranet_policies_playbook_config_generator.validated_config
    if len(config) == 1 and config[0].get("component_specific_filters") is None and not config[0].get("generate_all_configurations"):
        ccc_sda_extranet_policies_playbook_config_generator.msg = (
            "No valid configurations found in the provided parameters."
        )
        ccc_sda_extranet_policies_playbook_config_generator.validated_config = [
            {
                'component_specific_filters':
                {
                    'components_list': []
                }
            }
        ]
    ccc_sda_extranet_policies_playbook_config_generator.log(
        "Processing {0} validated configuration(s) "
        "for state '{1}'".format(
            len(ccc_sda_extranet_policies_playbook_config_generator.validated_config), state
        ),
        "INFO",
    )
    # Iterate over the validated configuration parameters
    for config in ccc_sda_extranet_policies_playbook_config_generator.validated_config:
        ccc_sda_extranet_policies_playbook_config_generator.reset_values()
        ccc_sda_extranet_policies_playbook_config_generator.get_want(
            config, state
        ).check_return_status()
        ccc_sda_extranet_policies_playbook_config_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    ccc_sda_extranet_policies_playbook_config_generator.log(
        "All {0} configuration(s) processed "
        "successfully. Exiting module.".format(
            len(ccc_sda_extranet_policies_playbook_config_generator.validated_config)
        ),
        "INFO",
    )

    module.exit_json(**ccc_sda_extranet_policies_playbook_config_generator.result)


if __name__ == "__main__":
    main()

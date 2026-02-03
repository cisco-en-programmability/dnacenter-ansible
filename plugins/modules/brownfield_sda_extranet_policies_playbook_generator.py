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
module: brownfield_sda_extranet_policies_playbook_generator
short_description: Generate YAML configurations playbook for 'sda_extranet_policies_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'sda_extranet_policies_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
version_added: 6.43.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the SDA extranet policies workflow manager
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all devices and all supported features.
          - This mode discovers all managed devices in Cisco Catalyst Center and extracts all supported configurations.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete brownfield infrastructure discovery and documentation.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "sda_extranet_policies_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "sda_extranet_policies_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
      global_filters:
        description:
        - Global filters to apply when generating the YAML configuration file.
        - These filters apply to all components unless overridden by component-specific filters.
        type: dict
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration
          file.
        - If "components_list" is specified, only those components are included,
          regardless of other filters.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are
              - Extranet Policies "extranet_policies"
            - If not specified, all components are included.
            - For example, ["extranet_policies"].
            type: list
            elements: str
          extranet_policies:
            description:
            - Extranet Policies to filter by extranet policy name.
            type: list
            elements: dict
            suboptions:
              extranet_policy_name:
                description:
                - Extranet Policy name to filter extranet policies by policy name.
                type: str
author:
- Apoorv Bansal (@Apoorv74-dot)
- Madhan Sankaranarayanan (@madhansansel)
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
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
"""

EXAMPLES = r"""
- name: Generate YAML playbook for all SDA extranet policies
  cisco.dnac.brownfield_sda_extranet_policies_playbook_generator:
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
  cisco.dnac.brownfield_sda_extranet_policies_playbook_generator:
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
  cisco.dnac.brownfield_sda_extranet_policies_playbook_generator:
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
          components_list: ["extranet_policies"]
          extranet_policies:
            - extranet_policy_name: "Test_1"

- name: Generate YAML playbook for multiple specific extranet policies
  cisco.dnac.brownfield_sda_extranet_policies_playbook_generator:
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
          components_list: ["extranet_policies"]
          extranet_policies:
            - extranet_policy_name: "Test_1"
            - extranet_policy_name: "Test_2"
            - extranet_policy_name: "Test_3"
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
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class SdaExtranetPoliciesPlaybookGenerator(DnacBase, BrownFieldHelper):
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
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }
        allowed_keys = set(temp_spec.keys())

        # Import validate_list_of_dicts function here to avoid circular imports
        from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

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

        return {
            "network_elements": {
                "extranet_policies": {
                    "filters": ["extranet_policy_name"],
                    "reverse_mapping_function": self.extranet_policy_temp_spec,
                    "api_function": "get_extranet_policies",
                    "api_family": "sda",
                    "get_function_name": self.get_extranet_policies_configuration,
                },
            },
            "global_filters": [],
        }

    def transform_fabric_site_ids_to_names(self, extranet_policy_details):
        """
        Transforms fabric site IDs into their corresponding site name hierarchies.
        This method converts fabric IDs from extranet policy details into human-readable
        site name hierarchies by analyzing each fabric ID and mapping it to its corresponding
        site name from the site_id_name_dict.

        Args:
            self: The instance of the class containing site_id_name_dict and helper methods.
            extranet_policy_details (dict): Dictionary containing extranet policy details with fabricIds.
                Expected to have a 'fabricIds' key containing a list of fabric IDs.

        Returns:
            list: A list of fabric site name hierarchies (strings) corresponding to the fabric IDs.
                Only includes site names that were successfully resolved from the site_id_name_dict.
                Returns an empty list if no fabric IDs are provided or none can be resolved.
        """
        self.log("Starting transformation of fabric site IDs to names for extranet policy.", "DEBUG")
        fabric_ids = extranet_policy_details.get("fabricIds", [])
        self.log("Found {0} fabric IDs to process.".format(len(fabric_ids)), "DEBUG")

        fabric_site_names = []
        for fabric_id in fabric_ids:
            site_id, fabric_type = self.analyse_fabric_site_or_zone_details(fabric_id)
            site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
            if site_name_hierarchy:
                fabric_site_names.append(site_name_hierarchy)
                self.log("Resolved fabric ID '{0}' to site name: '{1}'.".format(fabric_id, site_name_hierarchy), "DEBUG")
            else:
                self.log("Unable to resolve site name for fabric ID '{0}' with site ID '{1}'.".format(fabric_id, site_id), "WARNING")

        self.log("Completed transformation. Returning {0} fabric site names: {1}".format(
            len(fabric_site_names), fabric_site_names), "DEBUG")
        return fabric_site_names

    def extranet_policy_temp_spec(self):

        """Generates a temporary specification mapping for transforming extranet policy data."""
        self.log("Generating temporary specification for extranet policies.", "DEBUG")
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

    def get_extranet_policies_configuration(self, network_element, component_specific_filters=None):
        """
        Retrieves extranet policies configuration from Cisco Catalyst Center.
        This method fetches extranet policy details either for all policies or filtered by specific
        policy names, transforms the raw API response data into a structured format suitable for
        YAML playbook generation, and returns the processed configuration.

        Args:
            self: The instance of the class containing API execution methods and configuration.
            network_element (dict): Dictionary containing network element metadata including:
                - api_family (str): The API family name (e.g., 'sda').
                - api_function (str): The API function name (e.g., 'get_extranet_policies').
            component_specific_filters (list, optional): List of filter dictionaries to narrow down
                the extranet policies to retrieve. Each filter dictionary can contain:
                - extranet_policy_name (str): Specific policy name to filter by.
                If None or empty, retrieves all extranet policies.

        Returns:
            dict: A dictionary with the key 'extranet_policies' containing a list of transformed
                extranet policy configurations. Each policy includes:
                - extranet_policy_name: The name of the extranet policy.
                - provider_virtual_network: The provider virtual network name.
                - subscriber_virtual_networks: List of subscriber virtual network names.
                - fabric_sites: List of fabric site name hierarchies (transformed from fabric IDs).
                Returns empty list if no policies are found.
        """
        self.log("Starting retrieval of extranet policies configuration.", "DEBUG")
        self.log("Network element details: {0}".format(network_element), "DEBUG")
        self.log("Component specific filters: {0}".format(component_specific_filters), "DEBUG")

        final_extranet_policies = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        if component_specific_filters:
            # Process filters for specific policies
            self.log("Processing component-specific filters for extranet policies.", "DEBUG")
            for filter_param in component_specific_filters:
                for key, value in filter_param.items():
                    if key == "extranet_policy_name":
                        self.log("Filtering extranet policies by name: '{0}'.".format(value), "INFO")
                        params = {"extranetPolicyName": value}
                        policies = self.execute_get_with_pagination(api_family, api_function, params)
                        final_extranet_policies.extend(policies)
                        self.log("Retrieved {0} policies for filter '{1}'.".format(len(policies), value), "DEBUG")
        else:
            # Retrieve all policies
            self.log("No filters provided. Retrieving all extranet policies.", "INFO")
            policies = self.execute_get_with_pagination(api_family, api_function, {})
            final_extranet_policies.extend(policies)
            self.log("Retrieved {0} total extranet policies.".format(len(policies)), "DEBUG")

        # Transform using temp_spec
        self.log("Transforming {0} extranet policies using temp_spec.".format(len(final_extranet_policies)), "DEBUG")
        extranet_policy_temp_spec = self.extranet_policy_temp_spec()
        ep_details = self.modify_parameters(extranet_policy_temp_spec, final_extranet_policies)

        result = {'extranet_policies': ep_details}
        self.log("Completed extranet policies configuration retrieval. Returning {0} transformed policies.".format(
            len(ep_details)), "INFO")
        return result

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters, processes the data,
        and writes the YAML content to a specified file. It dynamically handles multiple network elements and their respective filters.

        Args:
            yaml_config_generator (dict): Contains file_path, global_filters, and component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """

        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log("Auto-discovery mode enabled - will process all devices and all features", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("Initializing filter dictionaries", "DEBUG")
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log("Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features", "INFO")
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")
            if yaml_config_generator.get("component_specific_filters"):
                self.log("Warning: component_specific_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")

            # Set empty filters to retrieve everything
            global_filters = {}
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        # Get components_list - if generate_all is True, use all available components
        if generate_all:
            components_list = list(module_supported_network_elements.keys())
            self.log("Auto-discovery mode: Processing all components: {0}".format(components_list), "INFO")
        else:
            components_list = component_specific_filters.get(
                "components_list", module_supported_network_elements.keys()
            )

        self.log("Components to process: {0}".format(components_list), "DEBUG")

        final_list = []
        for component in components_list:
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Skipping unsupported network element: {0}".format(component),
                    "WARNING",
                )
                continue

            filters = component_specific_filters.get(component, [])
            operation_func = network_element.get("get_function_name")
            if callable(operation_func):
                details = operation_func(network_element, filters)
                self.log(
                    "Details retrieved for {0}: {1}".format(component, details), "DEBUG"
                )
                final_list.append(details)

        if not final_list:
            self.msg = "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name
            )
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        final_dict = {"config": final_list}
        self.log("Final dictionary created: {0}".format(final_dict), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        This method prepares the parameters required for adding, updating, or deleting
        network configurations such as SSIDs and interfaces in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.

        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('gathered' or 'deleted').
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

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
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_sda_extranet_policies_playbook_generator = SdaExtranetPoliciesPlaybookGenerator(module)
    if (
        ccc_sda_extranet_policies_playbook_generator.compare_dnac_versions(
            ccc_sda_extranet_policies_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_sda_extranet_policies_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for SDA Extranet Policies Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_sda_extranet_policies_playbook_generator.get_ccc_version()
            )
        )
        ccc_sda_extranet_policies_playbook_generator.set_operation_result(
            "failed", False, ccc_sda_extranet_policies_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_extranet_policies_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_sda_extranet_policies_playbook_generator.supported_states:
        ccc_sda_extranet_policies_playbook_generator.status = "invalid"
        ccc_sda_extranet_policies_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_sda_extranet_policies_playbook_generator.check_recturn_status()

    # Validate the input parameters and check the return statusk
    ccc_sda_extranet_policies_playbook_generator.validate_input().check_return_status()
    config = ccc_sda_extranet_policies_playbook_generator.validated_config
    if len(config) == 1 and config[0].get("component_specific_filters") is None and not config[0].get("generate_all_configurations"):
        ccc_sda_extranet_policies_playbook_generator.msg = (
            "No valid configurations found in the provided parameters."
        )
        ccc_sda_extranet_policies_playbook_generator.validated_config = [
            {
                'component_specific_filters':
                {
                    'components_list': []
                }
            }
        ]

    # Iterate over the validated configuration parameters
    for config in ccc_sda_extranet_policies_playbook_generator.validated_config:
        ccc_sda_extranet_policies_playbook_generator.reset_values()
        ccc_sda_extranet_policies_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_sda_extranet_policies_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_sda_extranet_policies_playbook_generator.result)


if __name__ == "__main__":
    main()


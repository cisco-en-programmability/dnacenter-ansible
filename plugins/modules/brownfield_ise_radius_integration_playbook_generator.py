#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wired Campus Automation Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Jeet Ram, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_ise_radius_integration_playbook_generator
short_description: Resource module for Authentication
  and Policy Servers
description:
  - It generates playbook for Authentication and Policy Servers which can be use to manage operations on Authentication and Policy Servers.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
- Jeet Ram (@jeeram)
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
    - A list of filters for generating YAML playbook compatible with the `ise_radius_integration_integration_playbook_generator`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_components:
        description:
        - If true, all authentication and policy server components are included in the YAML
          configuration file.
        - If false, only the components specified in "components_list" are included.
        type: bool
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "ise_radius_integration_integration_playbook_generator_15_Dec_2025_21_43_26_379.yml".
        type: str
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
              - type "server_type"
              - server ip Address "server_ip_address"
            - If not specified, all components are included.
            - For example, ["server_type", "server_ip_address"].
            type: list
            elements: str
          server_type:
            description:
            - Authentication server type to filter by its server type.
            type: str
          server_ip_address:
            description:
            - Authentication servers to filter by its IP address.
            type: str

requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - system_settings.SystemSettings.get_authentication_and_policy_servers
- Paths used are
    get /dna/intent/api/v1/authentication-policy-servers
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with File Path specified
  cisco.dnac.ise_radius_integration_integration_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "/tmp/ise_radius_integration_config.yaml"

- name: Generate YAML Configuration with specific fabric sites components only
  cisco.dnac.ise_radius_integration_integration_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "/tmp/ise_radius_integration_config.yaml"
        component_specific_filters:
          components_list: ["server_type"]

- name: Generate YAML Configuration with specific fabric zones components only
  cisco.dnac.ise_radius_integration_integration_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "/tmp/ise_radius_integration_config.yaml"
        component_specific_filters:
          components_list: ["server_ip_address"]

- name: Generate YAML Configuration for all components
  cisco.dnac.ise_radius_integration_integration_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "/tmp/ise_radius_integration_config.yaml"
        component_specific_filters:
          components_list: ["server_type", "server_ip_address"]

- name: Generate YAML Configuration for all components
  cisco.dnac.ise_radius_integration_integration_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - generate_all_components: true
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "response": {
        },
        "msg": {
        }
    }
# Case_2: Error Scenario
response_2:
  description: A string with the message returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "msg": String
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
            return self.represent_mapping("tag:yaml.org, 2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class BrownfieldIseRadiusIntegrationPlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.log("Inside INIT function.", "DEBUG")
        self.module_schema = self.get_workflow_filters_schema()
        self.module_name = "brownfield_ise_radius_integration_playbook_generator"

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
        self.set_operation_result("success", False, self.msg, "DEBUG")
        return self

    def transform_cisco_ise_dtos(self, ise_radius_integration_details):
        """
            This function transforms the cisco_ise_dtos details from the API response to match the YAML configuration structure.
            Returns:
                list: A list of transformed cisco_ise_dtos details.
        """
        cisco_ise_dtos = ise_radius_integration_details.get("ciscoIseDtos")
        self.log("ciscoIseDtos: {0}".format(cisco_ise_dtos), "DEBUG")
        if not cisco_ise_dtos:
            return []
        cisco_ise_dtos_list = []
        for cisco_ise_dto in cisco_ise_dtos:
            user_name = cisco_ise_dto.get("userName")
            password = cisco_ise_dto.get("password")
            fqdn = cisco_ise_dto.get("fqdn")
            ip_address = cisco_ise_dto.get("ipAddress")
            description = cisco_ise_dto.get("description")
            cisco_ise_dtos_list.append({
                "user_name": user_name,
                "password": self.generate_custom_variable_name(self.transform_server_type(ise_radius_integration_details), "policy_server_password"),
                "fqdn": fqdn,
                "ip_address": ip_address,
                "description": description,
            })
        self.log(
            "Final cisco_ise_dtos_list data :: {0}".format(cisco_ise_dtos_list),
            "DEBUG",
            )
        return cisco_ise_dtos_list

    def transform_server_type(self, ise_radius_integration_details):
        """
            This function transforms the server_type details from the API response to match the YAML configuration structure.
            Returns:
                str: The transformed server_type detail.
        """
        cisco_ise_dtos = ise_radius_integration_details.get("ciscoIseDtos")
        self.log("ciscoIseDtos in transform_server_type(): {0}".format(cisco_ise_dtos), "DEBUG")
        if not cisco_ise_dtos:
            return None
        server_type = None
        for cisco_ise_dto in cisco_ise_dtos:
            server_type = cisco_ise_dto.get("type")
            self.log("server_type in transform_server_type(): {0}".format(server_type), "DEBUG")
            break
        return server_type

    def ise_radius_integration_temp_spec(self):
        """
        Constructs a temporary specification for authentication server, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as server_type, server_ip_address,
        shared_secret, protocol, encryption_scheme, encryption_key, message_authenticator_code_key etc.

        Returns:
            dict: A dictionary containing the temporary specification.
        """
        self.log("Generating temporary specification for ISE Radius Integration.", "DEBUG")
        ise_radius_integration = OrderedDict(
            {
                "server_type": {
                    "type": "str", "source_key": "server_type",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_server_type,
                },
                "server_ip_address": {"type": "str", "source_key": "ipAddress"},
                "shared_secret": {"type": "str", "source_key": "sharedSecret"},
                "protocol": {"type": "str", "source_key": "protocol"},
                "encryption_scheme": {"type": "str", "source_key": "encryptionScheme"},
                "encryption_key": {"type": "str", "source_key": "encryptionKey"},
                "message_authenticator_code_key": {"type": "str", "source_key": "messageKey"},
                "authentication_port": {"type": "int", "source_key": "authenticationPort"},
                "accounting_port": {"type": "int", "source_key": "accountingPort"},
                "retries": {"type": "int", "source_key": "retries"},
                "timeout": {"type": "int", "source_key": "timeoutSeconds"},
                "role": {"type": "int", "source_key": "role"},
                "pxgrid_enabled": {"type": "bool", "source_key": "pxgridEnabled"},
                "use_dnac_cert_for_pxgrid": {"type": "bool", "source_key": "useDnacCertForPxgrid"},
                "cisco_ise_dtos": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "ciscoIseDtos",
                    "special_handling": True,
                    "transform": self.transform_cisco_ise_dtos,
                    "user_name": {"type": "str"},
                    "password": {"type": "str"},
                    "fqdn": {"type": "str"},
                    "ip_address": {"type": "str"},
                    "description": {"type": "str"},
                },
                "trusted_server": {"type": "str", "source_key": "trustedServer"},
                "ise_integration_wait_time": {"type": "str", "source_key": "iseIntegrationWaitTime"},
            }
        )
        return ise_radius_integration

    def filter_ise_radius_integration_details(self, auth_server_details, filters=None):
        """
        Filter ISE RADIUS integration details based on server type and IP address.

        Args:
            auth_server_details (list): List of ISE RADIUS server configurations from API response.
            filters (dict): Filter criteria containing:
                - server_type (str): Type to filter (e.g., "ISE", "AAA")
                - server_ip_address (str): IP address to filter

        Returns:
            list: Filtered list of ISE RADIUS configurations matching the criteria.

        Example:
            filters = {
                "server_type": "ISE",
                "server_ip_address": "10.197.156.78"
            }
            result = filter_ise_radius_integration_details(auth_server_details, filters)
        """
        if not auth_server_details:
            self.log("No API response to filter", "WARNING")
            return []

        if not filters:
            self.log("No filters provided, returning all API response data", "DEBUG")
            return auth_server_details

        filtered_results = []
        server_type = filters.get("server_type")
        server_ip_address = filters.get("server_ip_address")
        self.log("Filtering ISE RADIUS integration details with server_type: {0}, server_ip_address: {1}".format(
                server_type, server_ip_address), "DEBUG")

        for each_server_resp in auth_server_details:
            # Check if the main server IP matches (if specified)
            self.log("Checking server response: {0} ".format(each_server_resp), "DEBUG")
            ip_match = True
            if server_ip_address:
                ip_match = each_server_resp.get("server_ip_address") == server_ip_address

            if not ip_match:
                self.log("Skipping server {0} due to IP address: {1} mismatch".format(each_server_resp, server_ip_address), "DEBUG")
                continue

            if server_type:
                matching_server_type = server_type == each_server_resp.get("server_type")

                # If matching DTOs found, include this server with filtered DTOs
                if matching_server_type:
                    self.log(
                        "Including server {0} with filtered server_type: {1}".format(
                            each_server_resp, matching_server_type
                        ),
                        "DEBUG"
                    )
                    filtered_results.append(each_server_resp)
            else:
                # No server_type filter, include the entire server
                self.log("Including entire server without server_type filter: {0}".format(each_server_resp), "DEBUG")
                filtered_results.append(each_server_resp)
        self.log("Filtering complete. Filtered servers response data {0}".format(
                filtered_results
            ),
            "DEBUG",
        )
        return filtered_results

    def filter_ise_radius_by_criteria(self, auth_server_details, filter_list=None):
        """
        Filter ISE RADIUS integration details based on multiple filter criteria.
        Supports OR logic for multiple filters and AND logic within each filter.

        Args:
            api_response (list): List of ISE RADIUS server configurations from API response.
            filter_list (list): List of filter criteria dicts. Each dict can contain:
                - server_type (str): Type to filter (e.g., "ISE")
                - server_ip_address (str): IP address to filter

                Multiple filters in the list are combined with OR logic.

        Returns:
            list: Filtered list of ISE RADIUS configurations matching any of the criteria.

        Example:
            filters = [
                {"server_type": "ISE", "server_ip_address": "10.197.156.78"},
                {"server_ip_address": "10.197.156.79"}
            ]
            result = filter_ise_radius_by_criteria(api_response, filters)
        """
        if not auth_server_details or not filter_list:
            return auth_server_details if auth_server_details else []

        all_filtered_results = []
        seen_server_ips = set()
        self.log(
            "Value of filter_list:: {0}".format(filter_list),
            "DEBUG",
        )

        for filters in filter_list:
            filtered = self.filter_ise_radius_integration_details(auth_server_details, filters)

            for server in filtered:
                # Use server_ip_address as unique identifier to avoid duplicates
                server_ip = server.get("server_ip_address")
                self.log("Processing server ID: {0}, seen_servers set value: {1}".format(server_ip, seen_server_ips), "DEBUG")
                if server_ip not in seen_server_ips:
                    all_filtered_results.append(server)
                    self.log(
                        "Adding server {0} to final results, all_filtered_results : {1}".format(server_ip, all_filtered_results),
                        "DEBUG",
                    )
                    seen_server_ips.add(server_ip)
        self.log(
            "Final filtered ISE RADIUS integration details: {0}".format(all_filtered_results),
        )
        self.log("Final filtered ISE RADIUS integration details all_filtered_results: {0}".format(all_filtered_results), "DEBUG")
        return all_filtered_results

    def generate_custom_variable_name(self, server_type, parameter_string):
        """
        Generate a custom variable name for a given server_type and parameter.
        Args:
            server_type (str): The type of the server (e.g., "ISE", "AAA").
            parameter_string (str): The parameter for which to generate the variable name (e.g., "password").
        Returns:
            str: The generated custom variable name in the format "{{ server_type_parameter_string }}".
        """
        self.log(
            "Generating custom variable name for server_type: {0}, parameter_string: {1}".format(
                server_type, parameter_string
            )
        ),

        variable_placeholder_name = "{{ {0}_{1} }}".format(
            server_type.lower(),
            parameter_string.lower(),
        )
        custom_variable_placeholder_name = "{" + variable_placeholder_name + "}"
        variable = "{0}_{1}".format(
            server_type.lower(),
            parameter_string.lower(),
        )

        self.log("Variable: {0}".format(variable), "DEBUG")
        # Create YAML file with custom variable name
        try:
            yaml_variable_content = {variable: "REPLACE_WITH_ACTUAL_VALUE"}
            yaml_filename = "{0}_variables.yml".format("{0}".format(parameter_string.lower(),))

            with open(yaml_filename, 'w') as yaml_file:
                yaml.dump(yaml_variable_content, yaml_file, default_flow_style=False)
            self.log(
                "Created YAML file for custom variable: {0}".format(yaml_filename),
                "DEBUG"
            )

        except Exception as e:
            self.log(
                "Failed to create YAML file for custom variable: {0}".format(str(e)),
                "WARNING"
            )

        self.log(
            "Generated custom variable name: {0}".format(custom_variable_placeholder_name), "DEBUG",
        )
        return custom_variable_placeholder_name

    def get_ise_radius_integration_configuration(self, network_element, component_specific_filters=None):
        """
         call catc to get authentication and policy server details.
        """
        self.log(
            "Calling Authentication and Policy Server details:",
            "DEBUG",
        )

        auth_server_details = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        response = self.dnac._exec(
            family=api_family,
            function=api_function,
        )
        if not isinstance(response, dict):
            self.log(
                "Failed to retrieve the Authentication and Policy Server details - "
                "Response is not a dictionary",
                "CRITICAL",
            )
            return None

        auth_server_details = response.get("response")
        if not auth_server_details:
            self.log(
                "Authentication and Policy Server does not exist",
                "DEBUG",
            )
            return None

        self.log(
            "Authentication and Policy Server details: {0}".format(auth_server_details),
            "DEBUG",
        )

        # Modify Authentication server's details using temp_spec
        ise_radius_integration_temp_spec = self.ise_radius_integration_temp_spec()
        ise_radius_integration_details = self.modify_parameters(
            ise_radius_integration_temp_spec, auth_server_details
        )

        self.log(
            "ISE Radius Integration's details ise_radius_integration_details after modify_parameters: {0}".format(
                ise_radius_integration_details
            ),
            "DEBUG",
        )

        filter_ise_radius_integration_response = self.filter_ise_radius_by_criteria(
            ise_radius_integration_details, component_specific_filters
        )

        modified_ise_radius_integration_details = {}
        modified_ise_radius_integration_details['authentication_policy_server'] = filter_ise_radius_integration_response

        self.log(
            "Modified ISE Radius Integration's details: {0}".format(
                modified_ise_radius_integration_details
            ),
            "DEBUG",
        )

        return modified_ise_radius_integration_details

    def get_workflow_filters_schema(self):
        """
        Description: Returns the schema for workflow filters supported by the module.
        Returns:
            dict: A dictionary representing the schema for workflow filters.
        """
        self.log("Inside get_workflow_filters_schema function.", "DEBUG")
        return {
            "network_elements": {
                "authentication_policy_server": {
                    "filters": ["server_type", "server_ip_address"],
                    "api_function": "get_authentication_and_policy_servers",
                    "api_family": "system_settings",
                    "reverse_mapping_function": self.ise_radius_integration_temp_spec,
                    "get_function_name": self.get_ise_radius_integration_configuration,
                }
            },
            "global_filters": [],
        }

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
            self.log("Auto-discovery mode enabled - will process all devices and all features", "DEBUG")

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
            self.log("Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features", "DEBUG")
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
            self.set_operation_result("ok", False, self.msg, "DEBUG")
            return self

        final_dict = {"config": final_list}
        self.log("Final dictionary created: {0}".format(final_dict), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "DEBUG")
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
            state (str): The desired state of the network elements ('merged' or 'deleted').
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "DEBUG"
        )

        self.validate_params(config)

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator added to want: {0}".format(
                want["yaml_config_generator"]
            ),
            "DEBUG",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "DEBUG")
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
                    "DEBUG",
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
            "Completed 'get_diff_merged' operation in {0:.2f} seconds.".format(
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
    ccc_brownfield_ise_radius_integration_playbook_generator = BrownfieldIseRadiusIntegrationPlaybookGenerator(module)
    if (
        ccc_brownfield_ise_radius_integration_playbook_generator.compare_dnac_versions(
            ccc_brownfield_ise_radius_integration_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_brownfield_ise_radius_integration_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for BrownfieldIseRadiusIntegrationPlaybookGenerator Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_brownfield_ise_radius_integration_playbook_generator.get_ccc_version()
            )
        )
        ccc_brownfield_ise_radius_integration_playbook_generator.set_operation_result(
            "failed", False, ccc_brownfield_ise_radius_integration_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_brownfield_ise_radius_integration_playbook_generator.params.get("state")
    # Check if the state is valid
    if state not in ccc_brownfield_ise_radius_integration_playbook_generator.supported_states:
        ccc_brownfield_ise_radius_integration_playbook_generator.status = "invalid"
        ccc_brownfield_ise_radius_integration_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_brownfield_ise_radius_integration_playbook_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_brownfield_ise_radius_integration_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_brownfield_ise_radius_integration_playbook_generator.validated_config:
        ccc_brownfield_ise_radius_integration_playbook_generator.reset_values()

        ccc_brownfield_ise_radius_integration_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_brownfield_ise_radius_integration_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_brownfield_ise_radius_integration_playbook_generator.result)
if __name__ == "__main__":


    main()

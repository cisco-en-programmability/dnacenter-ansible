#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for ISE Radius Integration Workflow Manager Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Jeet Ram, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: ise_radius_integration_playbook_config_generator
short_description: Generate YAML configurations playbook for 'ise_radius_integration_workflow_manager' module.
description:
  - Generates a YAML playbook for Authentication and Policy Servers that can
    be used with the ISE RADIUS integration workflow manager module.
  - Retrieves existing server configurations from Cisco Catalyst Center and
    transforms them into a YAML format compatible with the
    C(ise_radius_integration_workflow_manager) module.
version_added: '6.45.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
- Jeet Ram (@jeeram)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `ise_radius_integration_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - When C(components_list) is provided, only those components are included,
      regardless of other filters or C(generate_all_configurations).
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - When true, include all authentication and policy server components in
          the YAML configuration file.
        - When false, include only the components listed in
          C(component_specific_filters.components_list).
        - Ignored if C(component_specific_filters.components_list) is
          specified.
        type: bool
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  C(<module_name>_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(ise_radius_integration_playbook_config_2026-01-24_12-33-20.yml).
        type: str
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration
          file.
        - When C(components_list) is provided, only those components are included.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid value is C(authentication_policy_server).
            - If omitted, all components are included.
            - 'Example: C(["authentication_policy_server"])'
            type: list
            elements: str
            choices: ["authentication_policy_server"]
          authentication_policy_server:
            description:
            - Authentication and policy server filter with server_type and server_ip_address.
            type: dict
            suboptions:
              server_type:
                description:
                  - Server type to filter authentication and policy servers by server_type.
                  - ISE for Cisco ISE servers.
                  - AAA for Non-Cisco ISE servers.
                type: str
                choices: ["AAA", "ISE"]
              server_ip_address:
                description:
                - Server IP address to filter authentication and policy servers by IP address.
                type: str

requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - system_settings.SystemSettings.get_authentication_and_policy_servers
- Paths used are
    get /dna/intent/api/v1/authentication-policy-servers
seealso:
- module: cisco.dnac.ise_radius_integration_workflow_manager
  description: Module for managing ISE Radius Integration server.
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with File Path specified for all components
  cisco.dnac.ise_radius_integration_playbook_config_generator:
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
      - generate_all_configurations: true

- name: Generate YAML Configuration for all components with File Path specified
  cisco.dnac.ise_radius_integration_playbook_config_generator:
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
      - generate_all_configurations: true
        file_path: "/tmp/ise_radius_integration_config.yaml"

- name: Generate YAML Configuration for mentioned components without File Path specified
  cisco.dnac.ise_radius_integration_playbook_config_generator:
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
      - generate_all_configurations: false
        component_specific_filters:
          components_list: ["authentication_policy_server"]

- name: Generate YAML Configuration for mentioned components with component and specific server_type filter
  cisco.dnac.ise_radius_integration_playbook_config_generator:
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
          components_list: ["authentication_policy_server"]
          authentication_policy_server:
            server_type: "ISE"

- name: Generate YAML Configuration for mentioned components with component and specific server_ip_address filter
  cisco.dnac.ise_radius_integration_playbook_config_generator:
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
          components_list: ["authentication_policy_server"]
          authentication_policy_server:
            server_ip_address: 10.197.156.10

- name: Generate YAML Configuration for mentioned components with component and specific server_type and server_ip_address filter
  cisco.dnac.ise_radius_integration_playbook_config_generator:
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
          components_list: ["authentication_policy_server"]
          authentication_policy_server:
            server_type: "ISE"
            server_ip_address: 10.197.156.10
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
            "file_path": "ise_radius_integration_workflow_manager_playbook_2026-01-28_17-26-35.yml",
            "message": "YAML configuration file generated successfully for module 'ise_radius_integration_workflow_manager'",
            "status": "success"
        },
        "response": {
            "components_processed": 1,
            "components_skipped": 0,
            "configurations_count": 1,
            "file_path": "ise_radius_integration_workflow_manager_playbook_2026-01-28_17-26-35.yml",
            "message": "YAML configuration file generated successfully for module 'ise_radius_integration_workflow_manager'",
            "status": "success"
        },
        "status": "success"
    }
# Case_2: Error Scenario
response_2:
  description: A string with the message returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
        "msg": "Validation Error in entry 1: 'component_specific_filters' must be provided with
            'components_list' key when 'generate_all_configurations' is set to False.",
        "response": "Validation Error in entry 1: 'component_specific_filters' must be provided with
            'components_list' key when 'generate_all_configurations' is set to False."
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


class IseRadiusIntegrationPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    Generates YAML playbook files for ISE RADIUS integration brownfield deployments.

    This class retrieves existing Authentication and Policy Server configurations
    from Cisco Catalyst Center using GET APIs and transforms them into YAML
    playbooks compatible with the ise_radius_integration_workflow_manager module.

    Inherits from:
        DnacBase: Provides base functionality for Catalyst Center operations.
        BrownFieldHelper: Provides helper methods for brownfield configuration
            generation.

    Attributes:
        supported_states (list): List of supported Ansible states, currently
            only 'gathered'.
        module_schema (dict): Schema defining workflow elements, filters, and
            API bindings.
        module_name (str): Target module name for generated playbooks
            ('ise_radius_integration_workflow_manager').
        values_to_nullify (list): List of values to treat as null/empty in
            configurations.

    Methods:
        validate_input(): Validates input configuration parameters.
        transform_cisco_ise_dtos(): Transforms cisco_ise_dtos from API to YAML.
        transform_server_type(): Extracts server type from API response.
        ise_radius_integration_reverse_mapping_temp_spec_function(): Builds
            reverse mapping specification.
        filter_ise_radius_integration_details(): Filters servers by type and IP.
        filter_ise_radius_by_criteria(): Applies multi-criteria filtering.
        generate_custom_variable_name(): Generates variable placeholders.
        get_ise_radius_integration_configuration(): Retrieves and transforms
            server configurations.
        get_workflow_elements_schema(): Returns workflow filter schema.
        get_diff_gathered(): Orchestrates YAML generation workflow.
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
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "ise_radius_integration_workflow_manager"

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
        self.log("Validating configuration against schema.", "DEBUG")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "Validating minimum requirements against provided config: {0}".format(
                self.config
            ),
            "DEBUG",
        )
        self.validate_minimum_requirements(self.config)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "DEBUG")
        return self

    def transform_cisco_ise_dtos(self, ise_radius_integration_details):
        """
        Transforms the cisco_ise_dtos details from the API response to
        match the YAML configuration structure.

        Args:
            ise_radius_integration_details (dict): API response payload containing
                ciscoIseDtos and related metadata.
        """
        self.log(
            "Starting transformation of cisco_ise_dtos from ISE RADIUS integration details.",
            "DEBUG",
        )

        if not isinstance(ise_radius_integration_details, dict):
            self.log(
                "Invalid input for transformation; expected dict but received type={0}".format(
                    type(ise_radius_integration_details).__name__
                ),
                "ERROR",
            )
            return []

        cisco_ise_dtos = ise_radius_integration_details.get("ciscoIseDtos")
        self.log(
            "Retrieved {0} cisco_ise_dto entries from ISE RADIUS integration details.".format(
                len(cisco_ise_dtos) if cisco_ise_dtos else 0
            ),
            "DEBUG",
        )

        if not cisco_ise_dtos:
            self.log("No cisco_ise_dtos found. Returning empty list.", "WARNING")
            return []

        cisco_ise_dtos_list = []
        total_entries = len(cisco_ise_dtos)
        self.log(
            "Processing {0} cisco_ise_dto entry/entries for transformation.".format(
                total_entries
            ),
            "DEBUG",
        )

        for idx, cisco_ise_dto in enumerate(cisco_ise_dtos):
            self.log(
                "Processing cisco_ise_dto entry {0}/{1}".format(
                    idx,
                    total_entries,
                ),
                "DEBUG",
            )
            if not isinstance(cisco_ise_dto, dict):
                self.log(
                    "Skipping entry due to invalid type; index={0}, type={1}".format(
                        idx, type(cisco_ise_dto).__name__
                    ),
                    "WARNING",
                )
                continue

            user_name = cisco_ise_dto.get("userName")
            password = cisco_ise_dto.get("password")
            fqdn = cisco_ise_dto.get("fqdn")
            ip_address = cisco_ise_dto.get("ipAddress")
            description = cisco_ise_dto.get("description")
            ssh_key = cisco_ise_dto.get("sshKey")

            self.log(
                "Mapping entry fields; index={0}, user_name={1}, ip_address={2}".format(
                    idx, user_name, ip_address
                ),
                "DEBUG",
            )

            transformed_entry = {
                "user_name": user_name,
                "password": self.generate_custom_variable_name(
                    self.transform_server_type(ise_radius_integration_details),
                    "policy_server_password",
                ),
                "fqdn": fqdn,
                "ip_address": ip_address,
                "description": description,
                "ssh_key": ssh_key,
            }

            cisco_ise_dtos_list.append(transformed_entry)
            self.log(
                "Successfully transformed entry {0}/{1}: user_name={2}, ip_address={3}".format(
                    idx, total_entries, user_name, ip_address
                ),
                "DEBUG",
            )
            break

        self.log(
            "Completed cisco_ise_dtos transformation. Returning {0} transformed entry/entries.".format(
                len(cisco_ise_dtos_list)
            ),
            "DEBUG",
        )
        return cisco_ise_dtos_list

    def transform_server_type(self, ise_radius_integration_details):
        """
        Transforms server_type from ISE RADIUS integration details to YAML structure.

        Args:
            ise_radius_integration_details (dict): API response containing ciscoIseDtos.

        Returns:
            str: Server type value when present, otherwise None.
        """
        self.log(
            "Starting transformation of server_type from ISE RADIUS integration details.",
            "DEBUG",
        )
        if not isinstance(ise_radius_integration_details, dict):
            self.log(
                "Invalid details payload type; expected dict but received {0}".format(
                    type(ise_radius_integration_details).__name__
                ),
                "ERROR",
            )
            self.log("Returning server type: None due to invalid input.", "DEBUG")
            return None

        cisco_ise_dtos = ise_radius_integration_details.get("ciscoIseDtos")
        self.log(
            "Retrieved cisco_ise_dtos for server_type extraction: {0}".format(
                cisco_ise_dtos
            ),
            "DEBUG",
        )

        if not cisco_ise_dtos:
            self.log(
                "No cisco_ise_dtos found. Returning None for server_type.", "WARNING"
            )
            return None

        server_type = None
        self.log(
            "Extracting server_type from {0} cisco_ise_dto entries.".format(
                len(cisco_ise_dtos)
            ),
            "DEBUG",
        )

        for idx, cisco_ise_dto in enumerate(cisco_ise_dtos, start=1):
            self.log(
                "Inspecting cisco_ise_dto entry; index={0}, value={1}".format(
                    idx, cisco_ise_dto
                ),
                "DEBUG",
            )

            if not isinstance(cisco_ise_dto, dict):
                self.log(
                    "Skipping entry due to invalid type; index={0}, type={1}".format(
                        idx, type(cisco_ise_dto).__name__
                    ),
                    "WARNING",
                )
                continue
            server_type = cisco_ise_dto.get("type")
            if server_type:
                self.log(
                    "Server type identified; index={0}, server_type={1}".format(
                        idx, server_type
                    ),
                    "DEBUG",
                )
                break

            self.log(
                "Server type not present in entry; continuing scan. index={0}".format(
                    idx
                ),
                "DEBUG",
            )
        return server_type

    def ise_radius_integration_reverse_mapping_temp_spec_function(self):
        """
        Constructs a temporary specification for authentication server, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as server_type, server_ip_address,
        shared_secret, protocol, encryption_scheme, encryption_key, message_authenticator_code_key etc.

        Returns:
            dict: A dictionary containing the temporary specification.
        """
        self.log(
            "Generating temporary specification for ISE Radius Integration.", "DEBUG"
        )
        ise_radius_integration = OrderedDict(
            {
                "server_type": {
                    "type": "str",
                    "source_key": "server_type",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_server_type,
                },
                "server_ip_address": {"type": "str", "source_key": "ipAddress"},
                "shared_secret": {"type": "str", "source_key": "sharedSecret"},
                "protocol": {"type": "str", "source_key": "protocol"},
                "encryption_scheme": {"type": "str", "source_key": "encryptionScheme"},
                "encryption_key": {"type": "str", "source_key": "encryptionKey"},
                "message_authenticator_code_key": {
                    "type": "str",
                    "source_key": "messageKey",
                },
                "authentication_port": {
                    "type": "int",
                    "source_key": "authenticationPort",
                },
                "accounting_port": {"type": "int", "source_key": "accountingPort"},
                "retries": {"type": "int", "source_key": "retries"},
                "timeout": {"type": "int", "source_key": "timeoutSeconds"},
                "role": {"type": "int", "source_key": "role"},
                "pxgrid_enabled": {"type": "bool", "source_key": "pxgridEnabled"},
                "use_dnac_cert_for_pxgrid": {
                    "type": "bool",
                    "source_key": "useDnacCertForPxgrid",
                },
                "cisco_ise_dtos": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "ciscoIseDtos",
                    "special_handling": True,
                    "transform": self.transform_cisco_ise_dtos,
                    "suboptions": {
                        "user_name": {"type": "str"},
                        "password": {"type": "str"},
                        "fqdn": {"type": "str"},
                        "ip_address": {"type": "str"},
                        "description": {"type": "str"},
                        "ssh_key": {"type": "str", "source_key": "sshKey"},
                    },
                },
                "trusted_server": {"type": "str", "source_key": "trustedServer"},
                "ise_integration_wait_time": {
                    "type": "str",
                    "source_key": "iseIntegrationWaitTime",
                },
            }
        )
        self.log(
            "Generated temporary specification for ISE Radius Integration: {0}".format(
                ise_radius_integration
            ),
            "DEBUG",
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
        self.log(
            "Starting filtering of ISE RADIUS integration details with filters: {0}".format(
                filters
            ),
            "DEBUG",
        )

        if not auth_server_details:
            self.log(
                "No authentication server details to filter. Returning empty list.",
                "WARNING",
            )
            return []

        if not filters:
            self.log(
                "No filters provided, returning all {0} authentication server(s) without filtering.".format(
                    len(auth_server_details)
                ),
                "DEBUG",
            )
            return auth_server_details

        filtered_results = []
        self.log(
            "Filter criteria - server_type: {0}".format(filters),
            "DEBUG",
        )
        server_type = filters["server_type"] if "server_type" in filters else None

        server_ip_address = (
            filters["server_ip_address"] if "server_ip_address" in filters else None
        )
        self.log(
            "Filter criteria - server_type: {0}, server_ip_address: {1}".format(
                server_type, server_ip_address
            ),
            "DEBUG",
        )
        self.log(
            "Processing {0} authentication server entries for filtering.".format(
                len(auth_server_details)
            ),
            "DEBUG",
        )

        for idx, each_server_resp in enumerate(auth_server_details, start=1):
            self.log(
                "Evaluating server entry {0}/{1}: {2}".format(
                    idx,
                    len(auth_server_details),
                    each_server_resp.get("server_ip_address"),
                ),
                "DEBUG",
            )

            # Check if the main server IP matches (if specified)
            ip_match = True
            if server_ip_address:
                ip_match = (
                    each_server_resp.get("server_ip_address") == server_ip_address
                )
                self.log(
                    "IP address filter check for entry {0}: Expected={1}, Actual={2}, Match={3}".format(
                        idx,
                        server_ip_address,
                        each_server_resp.get("server_ip_address"),
                        ip_match,
                    ),
                    "DEBUG",
                )

            if not ip_match:
                self.log(
                    "Skipping server entry {0} due to IP address mismatch: Expected={1}, Actual={2}".format(
                        idx,
                        server_ip_address,
                        each_server_resp.get("server_ip_address"),
                    ),
                    "DEBUG",
                )
                continue

            if server_type:
                matching_server_type = server_type == each_server_resp.get(
                    "server_type"
                )
                self.log(
                    "Server type filter check for entry {0}: Expected={1}, Actual={2}, Match={3}".format(
                        idx,
                        server_type,
                        each_server_resp.get("server_type"),
                        matching_server_type,
                    ),
                    "DEBUG",
                )

                # If matching DTOs found, include this server with filtered DTOs
                if matching_server_type:
                    self.log(
                        "Including server entry {0} with matching server_type '{1}'.".format(
                            idx, server_type
                        ),
                        "DEBUG",
                    )
                    filtered_results.append(each_server_resp)
                else:
                    self.log(
                        "Skipping server entry {0} due to server_type mismatch.".format(
                            idx
                        ),
                        "DEBUG",
                    )
            else:
                # No server_type filter, include the entire server
                self.log(
                    "Including server entry {0} without server_type filter applied.".format(
                        idx
                    ),
                    "DEBUG",
                )
                filtered_results.append(each_server_resp)

        self.log(
            "Filtering complete. Matched {0} out of {1} servers. Filtered results: {2}".format(
                len(filtered_results), len(auth_server_details), filtered_results
            ),
            "DEBUG",
        )
        return filtered_results

    def filter_ise_radius_by_criteria(self, auth_server_details, filters=None):
        """
        Filter ISE RADIUS integration details based on multiple filter criteria.
        Supports OR logic for multiple filters and AND logic within each filter.

        Args:
            api_response (list): List of ISE RADIUS server configurations from API response.
            filters (dict): filter criteria dicts. Dict can contain:
                server_type (str): Type to filter (e.g., "ISE") and server_ip_address (str): IP address to filter

        Returns:
            list: Filtered list of ISE RADIUS configurations matching any of the criteria.

        Example:
            filters = {
                "server_type": "ISE",
                "server_ip_address": "10.197.156.79"
            }
            result = filter_ise_radius_by_criteria(api_response, filters)
        """
        self.log(
            "Starting filtering with filters: {0}".format(filters),
            "DEBUG",
        )

        if not auth_server_details:
            self.log(
                "No auth_server_details data found for filtering. Returning empty list.",
                "DEBUG",
            )
            return []
        if not filters:
            self.log(
                "No filters provided for filtering. Returning all {0} server(s).".format(
                    len(auth_server_details)
                ),
                "DEBUG",
            )
            return auth_server_details

        all_filtered_results = []
        seen_server_ips = set()
        self.log(
            "Processing filter criteria: {0}".format(filters),
            "DEBUG",
        )

        filtered = self.filter_ise_radius_integration_details(
            auth_server_details, filters
        )

        for server_idx, server in enumerate(filtered):
            # Use server_ip_address as unique identifier to avoid duplicates
            server_ip = server.get("server_ip_address")
            self.log(
                "Processing server {0}/{1}, IP={2}, Already seen={3}".format(
                    server_idx,
                    len(filtered),
                    server_ip,
                    server_ip in seen_server_ips,
                ),
                "DEBUG",
            )

            if server_ip not in seen_server_ips:
                all_filtered_results.append(server)
                seen_server_ips.add(server_ip)
                self.log(
                    "Added server with IP {0} to final results. Total unique servers: {1}".format(
                        server_ip, len(all_filtered_results)
                    ),
                    "DEBUG",
                )
            else:
                self.log(
                    "Skipping duplicate server with IP {0} (already in results).".format(
                        server_ip
                    ),
                    "DEBUG",
                )

        self.log(
            "Multi-criteria filtering complete. Matched {0} unique server(s) out of {1} total. Results: {2}".format(
                len(all_filtered_results),
                len(auth_server_details),
                all_filtered_results,
            ),
            "DEBUG",
        )
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
            "Generating custom variable placeholder for server_type='{0}', parameter_string='{1}'".format(
                server_type, parameter_string
            ),
            "DEBUG",
        )

        variable_placeholder_name = "{{ {0} }}".format(
            parameter_string.lower(),
        )
        custom_variable_placeholder_name = "{" + variable_placeholder_name + "}"

        self.log(
            "Generated custom variable placeholder: {0}".format(
                custom_variable_placeholder_name
            ),
            "DEBUG",
        )
        return custom_variable_placeholder_name

    def get_ise_radius_integration_configuration(self, network_element, filters=None):
        """
        call catalyst center to get authentication and policy server details.
        """

        component_specific_filters = filters.get("component_specific_filters", None)

        auth_server_details = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "Calling Authentication and Policy Server with api: family={0}, function={1}".format(
                api_family, api_function
            ),
            "DEBUG",
        )

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
        ise_radius_integration_reverse_mapping_temp_spec_function = (
            self.ise_radius_integration_reverse_mapping_temp_spec_function()
        )
        ise_radius_integration_details = self.modify_parameters(
            ise_radius_integration_reverse_mapping_temp_spec_function,
            auth_server_details,
        )

        self.log(
            "Applying component-specific filters to transformed details; filters={0}".format(
                component_specific_filters
            ),
            "DEBUG",
        )

        filter_ise_radius_integration_response = self.filter_ise_radius_by_criteria(
            ise_radius_integration_details, component_specific_filters
        )

        modified_ise_radius_integration_details = {
            "authentication_policy_server": filter_ise_radius_integration_response
        }

        self.log(
            "Completed ISE RADIUS integration configuration retrieval. Returning {0} configuration(s).".format(
                len(
                    modified_ise_radius_integration_details.get(
                        "authentication_policy_server", []
                    )
                )
            ),
            "DEBUG",
        )
        return modified_ise_radius_integration_details

    def get_workflow_elements_schema(self):
        """
        Description: Returns the schema for workflow filters supported by the module.
        Returns:
            dict: A dictionary representing the schema for workflow filters.
        """
        self.log("Inside get_workflow_elements_schema function.", "DEBUG")
        schema = {
            "network_elements": {
                "authentication_policy_server": {
                    "filters": {
                        "server_type": {
                            "type": "str",
                            "elements": "str",
                            "required": False,
                            "choices": ["AAA", "ISE"],
                        },
                        "server_ip_address": {"type": "str", "required": False},
                    },
                    "api_function": "get_authentication_and_policy_servers",
                    "api_family": "system_settings",
                    "reverse_mapping_function": self.ise_radius_integration_reverse_mapping_temp_spec_function,
                    "get_function_name": self.get_ise_radius_integration_configuration,
                }
            },
            "global_filters": [],
        }
        self.log(
            "Returning workflow schema with network_elements_count={0}, "
            "global_filters_count={1}.".format(
                len(schema.get("network_elements", {})),
                len(schema.get("global_filters", [])),
            ),
            "DEBUG",
        )
        self.log(
            "Workflow schema payload prepared: {0}".format(schema),
            "DEBUG",
        )
        return schema

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for ISE Radius Integration workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.
        """

        start_time = time.time()
        self.log(
            "Starting YAML configuration generation workflow; want_keys={0}".format(
                list(self.want.keys()) if isinstance(self.want, dict) else self.want
            ),
            "DEBUG",
        )
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
        self.log(
            "Beginning iteration over defined workflow operations for processing.",
            "DEBUG",
        )
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
            self.log(
                "Resolved parameters for operation; index={0}, has_params={1}".format(
                    index, bool(params)
                ),
                "DEBUG",
            )

            if not params:
                operations_skipped += 1
                self.log(
                    "Skipping operation due to missing parameters; index={0}, "
                    "operation={1}".format(index, operation_name),
                    "WARNING",
                )
                continue

            self.log(
                "Executing operation with resolved parameters; index={0}, operation={1}".format(
                    index, operation_name
                ),
                "INFO",
            )

            try:
                operation_func(params).check_return_status()
                operations_executed += 1
                self.log(
                    "Operation completed successfully; index={0}, operation={1}".format(
                        index, operation_name
                    ),
                    "DEBUG",
                )
            except Exception as e:
                self.log(
                    "Operation failed; index={0}, operation={1}, error={2}".format(
                        index, operation_name, str(e)
                    ),
                    "ERROR",
                )
                self.set_operation_result(
                    "failed",
                    True,
                    "{0} operation failed: {1}".format(operation_name, str(e)),
                    "ERROR",
                ).check_return_status()

        end_time = time.time()
        self.log(
            "Completed YAML configuration generation workflow; executed={0}, skipped={1}, "
            "duration_seconds={2:.2f}".format(
                operations_executed, operations_skipped, end_time - start_time
            ),
            "DEBUG",
        )

        return self


def main():
    """
    Main entry point for the ISE RADIUS integration playbook generator module.

    Orchestrates the module execution workflow by:
    1. Defining and validating module argument specifications.
    2. Initializing the playbook generator instance.
    3. Verifying Catalyst Center version compatibility (minimum 2.3.7.9).
    4. Validating the requested state against supported states.
    5. Validating input configuration parameters.
    6. Iterating through validated configurations and executing the appropriate
       state-based workflow.
    7. Returning results to Ansible via module.exit_json().

    Raises:
        AnsibleModule exit: Exits with success or failure status and result dictionary.

    Workflow:
        - For 'gathered' state: Retrieves existing ISE RADIUS integration
          configurations and generates YAML playbook.

    Returns:
        None: Results are returned through AnsibleModule.exit_json().
    """
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
    ccc_ise_radius_integration_playbook_config_generator = (
        IseRadiusIntegrationPlaybookGenerator(module)
    )
    if (
        ccc_ise_radius_integration_playbook_config_generator.compare_dnac_versions(
            ccc_ise_radius_integration_playbook_config_generator.get_ccc_version(),
            "2.3.7.9",
        )
        < 0
    ):
        ccc_ise_radius_integration_playbook_config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for IseRadiusIntegrationPlaybookGenerator Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_ise_radius_integration_playbook_config_generator.get_ccc_version()
            )
        )
        ccc_ise_radius_integration_playbook_config_generator.set_operation_result(
            "failed",
            False,
            ccc_ise_radius_integration_playbook_config_generator.msg,
            "ERROR",
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_ise_radius_integration_playbook_config_generator.params.get("state")
    # Check if the state is valid
    if (
        state
        not in ccc_ise_radius_integration_playbook_config_generator.supported_states
    ):
        ccc_ise_radius_integration_playbook_config_generator.status = "invalid"
        ccc_ise_radius_integration_playbook_config_generator.msg = (
            "State {0} is invalid".format(state)
        )
        ccc_ise_radius_integration_playbook_config_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_ise_radius_integration_playbook_config_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_ise_radius_integration_playbook_config_generator.validated_config:
        ccc_ise_radius_integration_playbook_config_generator.reset_values()

        ccc_ise_radius_integration_playbook_config_generator.get_want(
            config, state
        ).check_return_status()
        ccc_ise_radius_integration_playbook_config_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_ise_radius_integration_playbook_config_generator.result)


if __name__ == "__main__":
    main()

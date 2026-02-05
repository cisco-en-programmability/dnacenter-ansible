#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Device Credential Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Vivek Raj, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_device_credential_playbook_generator
short_description: Generate YAML configurations playbook for 'device_credential_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'device_credential_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Vivek Raj (@vivekraj2000)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `device_credential_workflow_manager`
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
          a default file name  C(<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(device_credential_workflow_manager_playbook_2026-01-24_12-33-20.yml).
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
              - global_credential_details
              - assign_credentials_to_site
            - If not specified, all supported components will be included.
            - For example, [global_credential_details, assign_credentials_to_site]
            type: list
            choices: ["global_credential_details", "assign_credentials_to_site"]
            elements: str
          global_credential_details:
            description: Global credentials to be included in the YAML configuration file.
            type: dict
            suboptions:
              cli_credential:
                description: CLI credentials to be included.
                type: list
                elements: dict
                suboptions:
                  description:
                    description: Description of the CLI credential.
                    type: str
              https_read:
                description: HTTPS Read credentials to be included.
                type: list
                elements: dict
                suboptions:
                  description:
                    description: Description of the HTTPS Read credential.
                    type: str
              https_write:
                description: HTTPS Write credentials to be included.
                type: list
                elements: dict
                suboptions:
                  description:
                    description: Description of the HTTPS Write credential.
                    type: str
              snmp_v2c_read:
                description: SNMPv2c Read credentials to be included.
                type: list
                elements: dict
                suboptions:
                  description:
                    description: Description of the SNMPv2c Read credential.
                    type: str
              snmp_v2c_write:
                description: SNMPv2c Write credentials to be included.
                type: list
                elements: dict
                suboptions:
                  description:
                    description: Description of the SNMPv2c Write credential.
                    type: str
              snmp_v3:
                description: SNMPv3 credentials to be included.
                type: list
                elements: dict
                suboptions:
                  description:
                    description: Description of the SNMPv3 credential.
                    type: str
          assign_credentials_to_site:
            description: Assign credentials to site details to be included in the YAML configuration file.
            type: dict
            suboptions:
              site_name:
                description: List of site names to include.
                type: list
                elements: str
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
  discovery.Discovery.get_all_global_credentials,
  site_design.SiteDesigns.get_sites,
  network_settings.NetworkSettings.get_device_credential_settings_for_a_site
- Paths used are
  GET /dna/intent/api/v2/global-credential,
  GET /dna/intent/api/v1/sites,
  GET /dna/intent/api/v1/sites/${id}/deviceCredentials
seealso:
- module: cisco.dnac.device_credential_workflow_manager
  description: Module for managing device credential workflows in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML playbook for device credential workflow manager which includes all global credentials and site assignments
  cisco.dnac.brownfield_device_credential_playbook_generator:
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
  cisco.dnac.brownfield_device_credential_playbook_generator:
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
        file_path: "device_credential_config.yml"

- name: Generate YAML Configuration with specific component global credential filters
  cisco.dnac.brownfield_device_credential_playbook_generator:
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
        file_path: "device_credential_config.yml"
        component_specific_filters:
          components_list: ["global_credential_details"]
          global_credential_details:
            cli_credential:
              - description: test
            https_read:
              - description: http_read
            https_write:
              - description: http_write

- name: Generate YAML Configuration with specific component assign credentials to site filters
  cisco.dnac.brownfield_device_credential_playbook_generator:
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
      - file_path: "device_credential_config.yml"
        component_specific_filters:
          components_list: ["assign_credentials_to_site"]
          assign_credentials_to_site:
            site_name:
              - "Global/India/Assam"
              - "Global/India/Haryana"

- name: Generate YAML Configuration with both global credential and assign credentials to site filters
  cisco.dnac.brownfield_device_credential_playbook_generator:
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
      - file_path: "device_credential_config.yml"
        component_specific_filters:
          components_list: ["global_credential_details", "assign_credentials_to_site"]
          global_credential_details:
            cli_credential:
              - description: test
            https_read:
              - description: http_read
            https_write:
              - description: http_write
          assign_credentials_to_site:
            site_name:
              - "Global/India/Assam"
              - "Global/India/TamilNadu"
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
            "components_processed": 2,
            "components_skipped": 0,
            "configurations_count": 2,
            "file_path": "device_credential_config.yml",
            "message": "YAML configuration file generated successfully for module 'device_credential_workflow_manager'",
            "status": "success"
        },
        "response": {
            "components_processed": 2,
            "components_skipped": 0,
            "configurations_count": 2,
            "file_path": "device_credential_config.yml",
            "message": "YAML configuration file generated successfully for module 'device_credential_workflow_manager'",
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

import time
from collections import OrderedDict

# Third-party imports
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
from ansible.module_utils.basic import AnsibleModule

# Local application/library-specific imports
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)


if HAS_YAML:
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class DeviceCredentialPlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.log(
            "Site ID to Name mapping: {0}".format(self.site_id_name_dict),
            "DEBUG",
        )
        self.global_credential_details = self.dnac._exec(
            family="discovery", function="get_all_global_credentials", op_modifies=False
        ).get("response", [])
        self.module_name = "device_credential_workflow_manager"

    def validate_input(self):
        """
        This function performs comprehensive validation of input configuration parameters
        by checking parameter presence, validating against expected schema specification,
        verifying minimum requirements for brownfield credential extraction, and setting
        validated configuration for downstream processing workflows.
        Returns:
            object: An instance of the class with updated attributes:
                self.msg: A message describing the validation result.
                self.status: The status of the validation (either "success" or "failed").
                self.validated_config: If successful, a validated version of the "config" parameter.
        """
        self.log(
            "Starting validation of playbook configuration parameters. Checking "
            "configuration availability, schema compliance, and minimum requirements "
            "for device credential extraction workflow.",
            "DEBUG"
        )

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        self.log(
            "Configuration found with {0} entries. Proceeding with schema validation "
            "against expected parameter specification.".format(len(self.config)),
            "DEBUG"
        )

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
        self.log(
            "Validation result - valid: {0}, invalid: {1}".format(
                valid_temp, invalid_params
            ),
            "DEBUG",
        )
        if invalid_params:
            self.log(
                "Schema validation failed. Invalid parameters detected: {0}. These "
                "parameters do not conform to expected types or structure.".format(
                    invalid_params
                ),
                "ERROR"
            )
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self
        self.log(
            "Schema validation passed successfully. All parameters conform to expected "
            "types and structure. Total valid entries: {0}.".format(len(valid_temp)),
            "DEBUG"
        )
        self.log("Validating minimum requirements against provided config: {0}".format(self.config), "DEBUG")
        self.validate_minimum_requirements(self.config)
        self.log(
            "Minimum requirements validation completed successfully. Configuration "
            "meets all prerequisites for brownfield credential extraction workflow.",
            "DEBUG"
        )

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = (
            "Successfully validated playbook configuration parameters using "
            "'validated_input': {0}".format(str(valid_temp))
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        self.log(
            "Validation completed successfully. Returning self instance with status "
            "'success' and validated_config populated for method chaining.",
            "DEBUG"
        )
        return self

    def get_workflow_filters_schema(self):
        """
        Constructs workflow filter schema for device credential network elements.

        This function defines the complete schema specification for device credential
        workflow manager operations including filter specifications for global
        credentials and site assignments, reverse mapping functions for data
        transformation, API configuration for Catalyst Center integration, and
        operation handler functions for configuration retrieval enabling consistent
        parameter validation, API execution, and YAML generation throughout the
        module lifecycle.

        Returns:
                dict: Dictionary containing network_elements schema configuration with:
                    - global_credential_details: Complete configuration including:
                        - filters: Parameter specifications for credential types (CLI,
                        HTTPS, SNMPv2c, SNMPv3) with description filtering
                        - reverse_mapping_function: Function reference for API to YAML
                        format transformation with sensitive field masking
                        - get_function_name: Method reference for retrieving global
                        credential configurations
                    - assign_credentials_to_site: Complete configuration including:
                        - filters: List containing site_name parameter for filtering
                        - reverse_mapping_function: Function reference for site
                        assignment transformation
                        - api_function: API method name for credential settings retrieval
                        - api_family: SDK family name (network_settings) for API execution
                        - get_function_name: Method reference for site assignment retrieval
                    - global_filters: Empty list reserved for future global filtering
        """
        self.log(
            "Constructing workflow filter schema for device credential network "
            "elements. Schema defines filter specifications, reverse mapping functions, "
            "API configuration, and handler functions for global credentials and site "
            "assignments enabling consistent parameter validation and YAML generation.",
            "DEBUG"
        )
        return {
            "network_elements": {
                "global_credential_details": {
                    "filters": {
                        "cli_credential": {
                            "type": "list",
                            "required": False,
                            "elements": "dict",
                            "options": {
                                "description": {"type": "str"},
                            }

                        },
                        "https_read": {
                            "type": "list",
                            "required": False,
                            "elements": "dict",
                            "options": {
                                "description": {"type": "str"},
                            }
                        },
                        "https_write": {
                            "type": "list",
                            "required": False,
                            "elements": "dict",
                            "options": {
                                "description": {"type": "str"},
                            }
                        },
                        "snmp_v2c_read": {
                            "type": "list",
                            "required": False,
                            "elements": "dict",
                            "options": {
                                "description": {"type": "str"},
                            }
                        },
                        "snmp_v2c_write": {
                            "type": "list",
                            "required": False,
                            "elements": "dict",
                            "options": {
                                "description": {"type": "str"},
                            }

                        },
                        "snmp_v3": {
                            "type": "list",
                            "required": False,
                            "elements": "dict",
                            "options": {
                                "description": {"type": "str"},
                            }
                        }
                    },
                    "reverse_mapping_function": self.global_credential_details_temp_spec,
                    "get_function_name": self.get_global_credential_details_configuration,
                },
                "assign_credentials_to_site": {
                    "filters": ["site_name"],
                    "reverse_mapping_function": self.assign_credentials_to_site_temp_spec,
                    "api_function": "get_device_credential_settings_for_a_site",
                    "api_family": "network_settings",
                    "get_function_name": self.get_assign_credentials_to_site_configuration,
                }
            },
            "global_filters": [],
        }

    def global_credential_details_temp_spec(self):
        """
        Constructs reverse mapping specification for global credential details.

        This function generates the complete ordered dictionary structure defining
        transformation rules for converting API response format to user-friendly YAML
        format compatible with device_credential_workflow_manager module. Handles six
        credential types (CLI, HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3) with
        sensitive field masking using custom variable placeholders to prevent raw
        credential exposure in generated YAML files.

        Args:
            None: Uses class methods for credential masking and transformation logic.

        Returns:
            OrderedDict: Reverse mapping specification with credential type mappings:
                        - cli_credential: List transformation with username, masked
                        password/enable_password, description, and id fields
                        - https_read: List transformation with username, masked password,
                        port, description, and id fields
                        - https_write: List transformation with username, masked password,
                        port, description, and id fields
                        - snmp_v2c_read: List transformation with masked read_community,
                        description, and id fields
                        - snmp_v2c_write: List transformation with write_community,
                        description, and id fields
                        - snmp_v3: List transformation with auth_type, snmp_mode,
                        privacy settings, username, masked auth_password,
                        description, and id fields
        """
        self.log(
            "Constructing reverse mapping specification for global credential details. "
            "Specification defines transformation rules for 6 credential types (CLI, "
            "HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3) with sensitive field masking "
            "to prevent raw credential exposure in generated YAML playbooks.",
            "DEBUG"
        )
        # Mask helper builds a placeholder using description to ensure
        # stable variable names (e.g., { { cli_credential_desc_password } }).

        def mask(component_key, item, field):
            """
            Generates masked variable placeholder for sensitive credential fields.

            Creates Jinja-like variable references (e.g., {{ cli_credential_desc_password }})
            to replace sensitive values preventing credential exposure in YAML output.

            Args:
                component_key (str): Credential type identifier (e.g., 'cli_credential')
                item (dict): Credential item containing description for variable naming
                field (str): Sensitive field name to mask (e.g., 'password')

            Returns:
                str: Masked variable placeholder or None if generation fails
            """
            try:
                self.log(
                    "Generating masked variable placeholder for component '{0}', "
                    "field '{1}' using description '{2}' for unique variable naming.".format(
                        component_key, field, item.get("description", "unknown")
                    ),
                    "DEBUG"
                )

                masked_value = self.generate_custom_variable_name(
                    item,
                    component_key,
                    "description",
                    field,
                )

                self.log(
                    "Successfully generated masked placeholder: {0} for field '{1}' "
                    "in component '{2}'.".format(masked_value, field, component_key),
                    "DEBUG"
                )

                return masked_value
            except Exception as e:
                self.log(
                    "Failed to generate masked variable for component '{0}', "
                    "field '{1}': {2}. Returning None.".format(
                        component_key, field, str(e)
                    ),
                    "ERROR"
                )
                return None

        global_credential_details = OrderedDict({
            "cli_credential": {
                "type": "list",
                "elements": "dict",
                "source_key": "cliCredential",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        "description": key.get("description"),
                        "username": key.get("username"),
                        # Sensitive fields masked
                        "password": mask("cli_credential", key, "password"),
                        "enable_password": mask("cli_credential", key, "enable_password"),
                        # Non-sensitive fields passed through
                        "id": key.get("id"),
                    }
                    for key in (detail.get("cliCredential") or [])
                ],
            },
            "https_read": {
                "type": "list",
                "elements": "dict",
                "source_key": "httpsRead",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        "description": key.get("description"),
                        "username": key.get("username"),
                        # Sensitive field masked
                        "password": mask("https_read", key, "password"),
                        # Non-sensitive fields passed through
                        "port": key.get("port"),
                        "id": key.get("id"),
                    }
                    for key in (detail.get("httpsRead") or [])
                ],
            },
            "https_write": {
                "type": "list",
                "elements": "dict",
                "source_key": "httpsWrite",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        "description": key.get("description"),
                        "username": key.get("username"),
                        # Sensitive field masked
                        "password": mask("https_write", key, "password"),
                        # Non-sensitive fields passed through
                        "port": key.get("port"),
                        "id": key.get("id"),
                    }
                    for key in (detail.get("httpsWrite") or [])
                ],
            },
            "snmp_v2c_read": {
                "type": "list",
                "elements": "dict",
                "source_key": "snmpV2cRead",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        # Non-sensitive fields passed through
                        "id": key.get("id"),
                        "description": key.get("description"),
                        # Sensitive field masked
                        "read_community": mask("snmp_v2c_read", key, "read_community"),
                    }
                    for key in (detail.get("snmpV2cRead") or [])
                ],
            },
            "snmp_v2c_write": {
                "type": "list",
                "elements": "dict",
                "source_key": "snmpV2cWrite",
                "options": OrderedDict({
                    "id": {"type": "str", "source_key": "id"},
                    "description": {"type": "str", "source_key": "description"},
                    "write_community": {"type": "str", "source_key": "writeCommunity"},
                }),
            },
            "snmp_v3": {
                "type": "list",
                "elements": "dict",
                "source_key": "snmpV3",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        # Non-sensitive fields passed through
                        "id": key.get("id"),
                        "auth_type": key.get("authType"),
                        "snmp_mode": key.get("snmpMode"),
                        "privacy_password": key.get("privacyPassword"),
                        "privacy_type": key.get("privacyType"),
                        "username": key.get("username"),
                        "description": key.get("description"),
                        # Sensitive field masked
                        "auth_password": mask("snmp_v3", key, "auth_password"),
                    }
                    for key in (detail.get("snmpV3") or [])
                ],
            },
        })
        self.log(
            "Reverse mapping specification constructed successfully with 6 credential "
            "type transformations. Specification includes field mappings for username, "
            "passwords (masked), ports, communities (masked for v2c read), auth settings "
            "(masked for v3), and description/id fields for all credential types.",
            "DEBUG"
        )

        self.log(
            "Returning global credential details reverse mapping specification for use "
            "in modify_parameters() transformation during YAML generation workflow.",
            "DEBUG"
        )
        return global_credential_details

    def assign_credentials_to_site_temp_spec(self):
        """
        Constructs reverse mapping specification for site credential assignments.

        This function generates the complete ordered dictionary structure defining
        transformation rules for converting site credential assignment API responses
        to user-friendly YAML format compatible with device_credential_workflow_manager
        module. Extracts non-sensitive credential metadata (description, username, id)
        for six credential types assigned to sites, preventing sensitive credential
        data exposure while maintaining credential reference integrity through ID
        mapping.

        Args:
            None: Uses helper function for field extraction from API responses.

        Returns:
            OrderedDict: Reverse mapping specification with site assignment mappings:
                        - cli_credential: Dict transformation with description, username,
                        and id fields extracted
                        - https_read: Dict transformation with description, username,
                        and id fields extracted
                        - https_write: Dict transformation with description, username,
                        and id fields extracted
                        - snmp_v2c_read: Dict transformation with description and id
                        fields extracted
                        - snmp_v2c_write: Dict transformation with description and id
                        fields extracted
                        - snmp_v3: Dict transformation with description and id fields
                        extracted
                        - site_name: List of site names where credentials are assigned
        """
        self.log(
            "Constructing reverse mapping specification for site credential "
            "assignments. Specification defines transformation rules for 6 credential "
            "types (CLI, HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3) extracting "
            "non-sensitive metadata (description, username, id) to prevent raw "
            "credential exposure while maintaining reference integrity.",
            "DEBUG"
        )

        def pick_fields(src, fields):
            """
            Extracts specified fields from source dictionary for safe credential metadata.

            Filters credential assignment objects to include only non-sensitive fields
            (description, username, id) while excluding passwords, community strings,
            and other sensitive authentication data from YAML output.

            Args:
                src (dict): Source credential assignment object from API response
                fields (list): List of field names to extract (e.g., ['description',
                            'username', 'id'])

            Returns:
                dict: Dictionary containing only specified fields with non-None values,
                    or None if source is not a dictionary
            """
            if not isinstance(src, dict):
                self.log(
                    "Source is not a dictionary type, returning None. Source type: {0}".format(
                        type(src).__name__
                    ),
                    "DEBUG"
                )
                return None
            self.log(
                "Extracting fields {0} from source credential object. Available source "
                "keys: {1}".format(fields, list(src.keys())),
                "DEBUG"
            )

            result = {k: src.get(k) for k in fields if src.get(k) is not None}

            self.log(
                "Successfully extracted {0} non-None fields from {1} requested fields. "
                "Extracted fields: {2}".format(
                    len(result), len(fields), list(result.keys())
                ),
                "DEBUG"
            )

            return result

        assign_credentials_to_site = OrderedDict({
            "cli_credential": {
                "type": "dict",
                "source_key": "cliCredential",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("cliCredential"), ["description", "username", "id"]),
            },
            "https_read": {
                "type": "dict",
                "source_key": "httpsRead",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("httpsRead"), ["description", "username", "id"]),
            },
            "https_write": {
                "type": "dict",
                "source_key": "httpsWrite",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("httpsWrite"), ["description", "username", "id"]),
            },
            "snmp_v2c_read": {
                "type": "dict",
                "source_key": "snmpV2cRead",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("snmpV2cRead"), ["description", "id"]),
            },
            "snmp_v2c_write": {
                "type": "dict",
                "source_key": "snmpV2cWrite",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("snmpV2cWrite"), ["description", "id"]),
            },
            "snmp_v3": {
                "type": "dict",
                "source_key": "snmpV3",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("snmpV3"), ["description", "id"]),
            },
            "site_name": {
                "type": "list",
                "elements": "str",
                "source_key": "siteName"
            },
        })

        self.log(
            "Reverse mapping specification constructed successfully with 7 field "
            "mappings (6 credential types + site_name). Specification includes "
            "transformations for CLI (description, username, id), HTTPS Read/Write "
            "(description, username, id), SNMPv2c Read/Write (description, id), "
            "SNMPv3 (description, id), and site_name list for location context.",
            "DEBUG"
        )

        self.log(
            "Returning site credential assignment reverse mapping specification for "
            "use in modify_parameters() transformation during YAML generation workflow "
            "with sensitive field protection.",
            "DEBUG"
        )
        return assign_credentials_to_site

    def get_global_credential_details_configuration(self, network_element, filters):
        """
        Retrieves and transforms global credential details from Catalyst Center.

        This function orchestrates global credential retrieval by extracting credentials
        from cached global_credential_details, applying optional component-specific
        filters for targeted credential selection, transforming API response format to
        user-friendly YAML structure using reverse mapping specification, and masking
        sensitive fields (passwords, community strings) with custom variable placeholders
        to prevent raw credential exposure in generated playbooks.

        Args:
            network_element (dict): Network element configuration (reserved for future
                                use, currently unused for consistency with other
                                component functions).
            filters (dict): Filter configuration containing:
                        - component_specific_filters (dict, optional): Nested filters
                            for credential types with description-based filtering:
                            - cli_credential: List of CLI credential filters
                            - https_read: List of HTTPS Read credential filters
                            - https_write: List of HTTPS Write credential filters
                            - snmp_v2c_read: List of SNMPv2c Read credential filters
                            - snmp_v2c_write: List of SNMPv2c Write credential filters
                            - snmp_v3: List of SNMPv3 credential filters

        Returns:
            dict: Dictionary containing transformed global credential details:
                - global_credential_details (dict): Mapped credential structure with:
                    - cli_credential (list): CLI credentials with masked passwords
                    - https_read (list): HTTPS Read credentials with masked passwords
                    - https_write (list): HTTPS Write credentials with masked passwords
                    - snmp_v2c_read (list): SNMPv2c Read with masked community strings
                    - snmp_v2c_write (list): SNMPv2c Write credentials
                    - snmp_v3 (list): SNMPv3 credentials with masked auth passwords
        """
        self.log(
            "Starting global credential details retrieval and transformation workflow. "
            "Workflow includes credential extraction from cache, optional filter "
            "application for targeted selection, reverse mapping transformation to "
            "YAML format, and sensitive field masking to prevent credential exposure.",
            "DEBUG"
        )

        self.log(
            "Extracting component_specific_filters from filters dictionary: {0}. "
            "Filters determine which credential types and descriptions to include in "
            "generated YAML configuration.".format(filters),
            "DEBUG"
        )
        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")
            self.log(
                "Component-specific filters found with {0} credential type filter(s). "
                "Will apply description-based filtering to credential groups.".format(
                    len(component_specific_filters) if component_specific_filters else 0
                ),
                "DEBUG"
            )
        else:
            self.log(
                "No component_specific_filters provided. Will retrieve all global "
                "credentials without filtering for complete credential inventory.",
                "DEBUG"
            )
        self.log(
            "Initializing final credential list for transformation. List will contain "
            "either filtered credentials or complete credential set based on filter "
            "presence.",
            "DEBUG"
        )
        self.log(
            (
                "Starting to retrieve global credential details with "
                "component-specific filters: {0}"
            ).format(component_specific_filters),
            "DEBUG",
        )
        final_global_credentials = []

        self.log(
            "Cached global credential details type: {0}, count: {1}. Credentials "
            "retrieved during initialization from discovery.get_all_global_credentials "
            "API.".format(
                type(self.global_credential_details),
                len(self.global_credential_details) if isinstance(
                    self.global_credential_details, list
                ) else "N/A"
            ),
            "DEBUG"
        )

        self.log(
            "Cached global credential details content: {0}. Contains credential groups "
            "cliCredential, httpsRead, httpsWrite, snmpV2cRead, snmpV2cWrite, snmpV3.".format(
                self.global_credential_details
            ),
            "DEBUG"
        )

        if component_specific_filters:
            self.log(
                "Applying component-specific filters to global credentials. Filtering "
                "by description fields to extract targeted credential subset for YAML "
                "generation.",
                "DEBUG"
            )
            filtered_credentials = self.filter_credentials(self.global_credential_details, component_specific_filters)
            self.log(
                "Filter application completed. Filtered credentials contain {0} "
                "credential group(s). Groups: {1}".format(
                    len(filtered_credentials) if isinstance(
                        filtered_credentials, dict
                    ) else 0,
                    list(filtered_credentials.keys()) if isinstance(
                        filtered_credentials, dict
                    ) else []
                ),
                "DEBUG"
            )

            self.log(
                "Filtered credential details: {0}. Using filtered subset for reverse "
                "mapping transformation.".format(filtered_credentials),
                "DEBUG"
            )
            final_global_credentials = [filtered_credentials]
        else:
            self.log(
                "No filtering applied. Using complete global credential details for "
                "reverse mapping transformation to generate comprehensive credential "
                "YAML configuration.",
                "DEBUG"
            )
            final_global_credentials = [self.global_credential_details]

        self.log(
            "Retrieving reverse mapping specification for global credential details "
            "transformation. Specification defines field mappings, sensitive field "
            "masking rules, and YAML structure for 6 credential types.",
            "DEBUG"
        )
        global_credential_details_temp_spec = self.global_credential_details_temp_spec()

        self.log(
            "Reverse mapping specification retrieved successfully. Specification "
            "includes transformations for cli_credential, https_read, https_write, "
            "snmp_v2c_read, snmp_v2c_write, and snmp_v3 with password/community string "
            "masking.",
            "DEBUG"
        )

        self.log(
            "Applying reverse mapping transformation to {0} credential set(s) using "
            "modify_parameters(). Transformation converts API format to user-friendly "
            "YAML structure with sensitive field placeholders.".format(
                len(final_global_credentials)
            ),
            "DEBUG"
        )

        mapped_list = self.modify_parameters(
            global_credential_details_temp_spec, final_global_credentials
        )

        self.log(
            "Reverse mapping transformation completed. Generated {0} mapped "
            "credential structure(s) with masked sensitive fields for secure YAML "
            "output.".format(len(mapped_list)),
            "DEBUG"
        )
        mapped = mapped_list[0] if mapped_list else {}
        return {"global_credential_details": mapped}

    def filter_credentials(self, source, filters):
        """
        Filters global credential groups by matching description fields.

        This function applies component-specific filters to global credential data by
        matching credential descriptions against requested filter criteria, extracting
        only credentials with matching descriptions from each credential type group
        (CLI, HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3), and constructing a filtered
        credential dictionary containing only matched items for targeted credential
        selection in YAML generation workflow.

        Args:
            source (dict): Global credentials dictionary from Catalyst Center containing
                        credential groups with camelCase keys (e.g., cliCredential,
                        httpsRead, httpsWrite, snmpV2cRead, snmpV2cWrite, snmpV3).
                        Each group contains list of credential objects with description,
                        username, id, and sensitive credential fields.
            filters (dict): Component-specific filter dictionary with snake_case keys
                        (e.g., cli_credential, https_read) containing lists of
                        filter objects. Each filter object specifies description
                        field to match (e.g., [{"description": "WLC"}]).

        Returns:
            dict: Filtered credentials dictionary with camelCase keys containing only
                credential objects matching filter descriptions. Empty dictionary if
                no matches found or source/filters invalid. Preserves original API
                response structure with matched items only.
        """
        self.log("Starting filter_credentials with source: {0} and filters: {1}".format(source, filters), "DEBUG")
        key_map = {
            'cli_credential': 'cliCredential',
            'https_read': 'httpsRead',
            'https_write': 'httpsWrite',
            'snmp_v2c_read': 'snmpV2cRead',
            'snmp_v2c_write': 'snmpV2cWrite',
            'snmp_v3': 'snmpV3',
        }
        result = {}
        self.log(
            "Starting iteration through {0} filter entries to extract matching "
            "credentials from source groups. Each filter specifies description "
            "criteria for credential selection.".format(len(filters)),
            "DEBUG"
        )
        for filter_index, (f_key, wanted_list) in enumerate(filters.items(), start=1):
            self.log(
                "Processing filter {0}/{1} for credential type '{2}' with {3} "
                "description filter(s). Resolving API key and extracting wanted "
                "descriptions for matching.".format(
                    filter_index, len(filters), f_key, len(wanted_list)
                ),
                "DEBUG"
            )
            src_key = key_map.get(f_key)
            if not src_key:
                self.log(
                    "Filter key '{0}' not found in key mapping. Skipping unsupported "
                    "credential type filter. Valid filter keys: {1}".format(
                        f_key, list(key_map.keys())
                    ),
                    "WARNING"
                )
                continue

            if src_key not in source:
                self.log(
                    "Credential group '{0}' (mapped from filter key '{1}') not found "
                    "in source credentials. Skipping filter for this group. Available "
                    "source groups: {2}".format(
                        src_key, f_key, list(source.keys())
                    ),
                    "DEBUG"
                )
                continue

            self.log(
                "Extracting wanted descriptions from {0} filter objects for credential "
                "type '{1}'. Building description set for efficient matching against "
                "source credentials.".format(len(wanted_list), f_key),
                "DEBUG"
            )
            wanted_desc = {item.get('description') for item in wanted_list if 'description' in item}
            self.log(
                "Extracted {0} unique description(s) from filter criteria: {1}. "
                "Matching against {2} credential(s) in source group '{3}'.".format(
                    len(wanted_desc), wanted_desc, len(source[src_key]), src_key
                ),
                "DEBUG"
            )

            self.log(
                "Filtering credential group '{0}' with {1} source credential(s) "
                "against {2} wanted description(s). Extracting credentials with "
                "matching description fields.".format(
                    src_key, len(source[src_key]), len(wanted_desc)
                ),
                "DEBUG"
            )
            matched = [item for item in source[src_key] if item.get('description') in wanted_desc]
            if matched:
                result[src_key] = matched
        return result

    def get_assign_credentials_to_site_configuration(self, network_element, filters):
        """Build assigned credential configuration per requested sites.

        Resolves site names to IDs, queries sync status, matches credential IDs
        against global credentials, and maps the first match per type to a
        dict suitable for YAML output.

        Args:
            network_element (dict): Contains API family and function names.
            filters (dict): Dictionary containing global filters and component_specific_filters.

        Returns:
            list | dict: One item per site `{ "assign_credentials_to_site": <mapped> }`,
            or empty dict if no sites resolved.
        """

        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")

        self.log(
            (
                "Starting to retrieve assign_credentials_to_site with "
                "component-specific filters: {0}"
            ).format(component_specific_filters),
            "DEBUG",
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            (
                "Getting assign_credentials_to_site using API family: {0}, "
                "function: {1}"
            ).format(api_family, api_function),
            "DEBUG",
        )
        # Resolve requested site names (if any) to IDs using the cached mapping from __init__
        final_assignments = []
        name_site_id_dict = {v: k for k, v in self.site_id_name_dict.items() if v is not None}
        self.log(
            "Name to Site ID mapping: {0}".format(name_site_id_dict), "DEBUG"
        )
        site_names = []
        if component_specific_filters:
            site_names = component_specific_filters.get("site_name", []) or []
        else:
            site_names = list(name_site_id_dict.keys())
        site_ids = [name_site_id_dict.get(n) for n in site_names if n in name_site_id_dict]
        self.log(
            "Resolved site IDs from site names {0}: {1}".format(
                site_names, site_ids
            ),
            "DEBUG",
        )
        if not site_ids:
            self.log(
                "No site IDs resolved from site names: {0}".format(site_names),
                "INFO",
            )
            return {"assign_credentials_to_site": {}}

        key_map = {
            "cliCredentialsId": "cliCredential",
            "httpReadCredentialsId": "httpsRead",
            "httpWriteCredentialsId": "httpsWrite",
            "snmpv2cReadCredentialsId": "snmpV2cRead",
            "snmpv2cWriteCredentialsId": "snmpV2cWrite",
            "snmpv3CredentialsId": "snmpV3",
        }

        def find_credential(cred_group_key, cred_id):
            group = []
            if isinstance(self.global_credential_details, dict):
                group = self.global_credential_details.get(cred_group_key, []) or []
            for item in group:
                if item.get("id") == cred_id:
                    return item
            return None

        for site_id in site_ids:
            if not site_id:
                continue
            self.log(
                "Fetching credential sync status for site_id: {0}".format(
                    site_id
                ),
                "DEBUG",
            )
            try:
                resp = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    params={"id": site_id}
                ) or {}
            except Exception as e:
                self.log(
                    (
                        "Failed to fetch credential sync status for site {0}: "
                        "{1}"
                    ).format(site_id, str(e)),
                    "ERROR",
                )
                continue

            sync_resp = resp.get("response", {}) or {}
            self.log(
                "Sync status response for site {0}".format(sync_resp), "DEBUG"
            )

            raw_assign = {
                "cliCredential": None,
                "httpsRead": None,
                "httpsWrite": None,
                "snmpV2cRead": None,
                "snmpV2cWrite": None,
                "snmpV3": None,
                "siteName": None,
            }
            for sync_key, global_key in key_map.items():
                raw_val = sync_resp.get(sync_key)
                cred_id = None
                if isinstance(raw_val, dict):
                    cred_id = raw_val.get("credentialsId")
                if not cred_id:
                    continue

                cred_obj = find_credential(global_key, cred_id)
                if cred_obj and raw_assign.get(global_key) is None:
                    raw_assign[global_key] = cred_obj
                    self.log(
                        (
                            "Matched credential id {0} for sync key {1} "
                            "(group {2})"
                        ).format(cred_id, sync_key, global_key),
                        "DEBUG",
                    )
            raw_assign["siteName"] = [self.site_id_name_dict.get(site_id, "UNKNOWN SITE")]

            for k in list(raw_assign.keys()):
                if raw_assign[k] is None:
                    del raw_assign[k]

            assign_spec = self.assign_credentials_to_site_temp_spec()
            mapped_list = self.modify_parameters(assign_spec, [raw_assign])
            mapped = mapped_list[0] if mapped_list else {}
            final_assignments.append({"assign_credentials_to_site": mapped})
        return final_assignments

    def generate_custom_variable_name(
        self,
        network_component_details,
        network_component,
        network_component_name_parameter,
        parameter,
    ):
        """Generate masked variable placeholder for sensitive fields.

        Constructs a Jinja-like variable name for the given component and parameter
        to prevent emitting raw values.

        Args:
            network_component_details (dict): Source dict containing the component name parameter.
            network_component (str): Component key, e.g., "cli_credential".
            network_component_name_parameter (str): Field name used as component identifier, e.g., "description".
            parameter (str): Field to mask, e.g., "password".

        Returns:
            str: Masked variable placeholder string.
        """
        # Generate the custom variable name
        self.log(
            "Generating custom variable name for network component: {0}".format(
                network_component
            ),
            "DEBUG",
        )
        self.log(
            "Network component details: {0}".format(network_component_details), "DEBUG"
        )
        self.log(
            "Network component name parameter: {0}".format(
                network_component_name_parameter
            ),
            "DEBUG",
        )
        self.log("Parameter: {0}".format(parameter), "DEBUG")
        variable_name = "{{ {0}_{1}_{2} }}".format(
            network_component,
            network_component_details[network_component_name_parameter].replace(" ", "_").replace("-", "_").lower(),
            parameter,
        )
        custom_variable_name = "{" + variable_name + "}"
        self.log(
            "Generated custom variable name: {0}".format(custom_variable_name), "DEBUG"
        )
        return custom_variable_name

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

        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        self.log("Determining components list for processing", "DEBUG")
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )

        # If components_list is empty, default to all supported components
        if not components_list:
            self.log("No components specified; processing all supported components.", "DEBUG")
            components_list = list(module_supported_network_elements.keys())

        self.log("Components to process: {0}".format(components_list), "DEBUG")

        self.log("Initializing final configuration list and operation summary tracking", "DEBUG")
        final_config_list = []
        processed_count = 0
        skipped_count = 0

        for component in components_list:
            self.log("Processing component: {0}".format(component), "DEBUG")
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
            else:
                final_config_list.append(component_data)

        if not final_config_list:
            self.log(
                "No configurations retrieved. Processed: {0}, Skipped: {1}, Components: {2}".format(
                    processed_count, skipped_count, components_list
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
            "Final config dictionary created: {0}".format(self.pprint(yaml_config_dict)),
            "DEBUG"
        )

        if self.write_dict_to_yaml(yaml_config_dict, file_path, OrderedDumper):
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
        Executes YAML configuration file generation for brownfield device credentials.

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
    """Main entry point for module execution.

    Parses Ansible parameters, initializes the module class, validates input,
    runs the requested operations, and returns results via `module.exit_json`.
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
    ccc_device_credential_playbook_generator = DeviceCredentialPlaybookGenerator(module)
    if (
        ccc_device_credential_playbook_generator.compare_dnac_versions(
            ccc_device_credential_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_device_credential_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for <module_name_caps> Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_device_credential_playbook_generator.get_ccc_version()
            )
        )
        ccc_device_credential_playbook_generator.set_operation_result(
            "failed", False, ccc_device_credential_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_device_credential_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_device_credential_playbook_generator.supported_states:
        ccc_device_credential_playbook_generator.status = "invalid"
        ccc_device_credential_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_device_credential_playbook_generator.check_recturn_status()

    # Validate the input parameters and check the return statusk
    ccc_device_credential_playbook_generator.validate_input().check_return_status()
    config = ccc_device_credential_playbook_generator.validated_config
    ccc_device_credential_playbook_generator.log(
        "Validated configuration parameters: {0}".format(str(config)), "DEBUG"
    )

    # Iterate over the validated configuration parameters
    for config in ccc_device_credential_playbook_generator.validated_config:
        ccc_device_credential_playbook_generator.reset_values()
        ccc_device_credential_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_device_credential_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_device_credential_playbook_generator.result)


if __name__ == "__main__":
    main()

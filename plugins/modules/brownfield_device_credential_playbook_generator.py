#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wired Campus Automation Module."""
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
version_added: 6.17.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Vivek Raj (vivekraj2000)
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
          a default file name  "device_credential_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "device_credential_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
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
    - discovery.Discovery.get_all_global_credentials
    - site_design.SiteDesigns.get_sites
    -  network_settings.NetworkSettings.get_device_credential_settings_for_a_site
- Paths used are:
    - GET /dna/intent/api/v2/global-credential
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/sites/${id}/deviceCredentials

"""

EXAMPLES = r"""
    - name: Generate YAML playbook for device credential workflow manager
        which includes all global credentials and site assignments
      cisco.dnac.brownfield_device_credential_playbook_generator:
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

    - name: Generate YAML Configuration with File Path specified
      cisco.dnac.brownfield_device_credential_playbook_generator:
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
            file_path: "device_credential_config.yml"

    - name: Generate YAML Configuration with specific component global credential filters
      cisco.dnac.brownfield_device_credential_playbook_generator:
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
            - generate_all_configurations: false
              file_path: "device_credential_config.yml"
              component_specific_filters:
                components_list: ["global_credential_details"]
                global_credential_details:
                    cli_credential :
                      - description: test
                    https_read :
                      - description: http_read
                    https_write :
                      - description: http_write

    - name: Generate YAML Configuration with specific component assign credentials to site filters
      cisco.dnac.brownfield_device_credential_playbook_generator:
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
            - file_path: "device_credential_config.yml"
              component_specific_filters:
                components_list: ["assign_credentials_to_site"]
                assign_credentials_to_site:
                    site_name:
                        - "Global/India/Assam"
                        - "Global/India/Haryana"

    - name: Generate YAML Configuration with both global credential and assign credentials to site filters
      cisco.dnac.brownfield_device_credential_playbook_generator:
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
            - file_path: "device_credential_config.yml"
              component_specific_filters:
                components_list: ["global_credential_details", "assign_credentials_to_site"]
                global_credential_details:
                    cli_credential :
                        - description: test
                    https_read :
                    - description: http_read
                    https_write :
                    - description: http_write
                assign_credentials_to_site:
                    site_name:
                        - "Global/India/Assam"
                        - "Global/India/TamilNadu"
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
        Validates the input configuration parameters for the playbook.
        Returns:
            object: An instance of the class with updated attributes:
                self.msg: A message describing the validation result.
                self.status: The status of the validation (either "success" or "failed").
                self.validated_config: If successful, a validated version of the "config" parameter.
        """
        self.log(
            "Starting validation of input configuration parameters.", "DEBUG"
        )

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
        self.log(
            "Validation result - valid: {0}, invalid: {1}".format(
                valid_temp, invalid_params
            ),
            "DEBUG",
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = (
            "Successfully validated playbook configuration parameters using "
            "'validated_input': {0}".format(str(valid_temp))
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_filters_schema(self):
        """Return the supported network elements and filter schema.

        The schema describes filters, reverse mapping functions, and handler
        functions used to build the YAML output for each component.

        Returns:
            dict: Module filter and component schema mapping.
        """

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
        """Build temp spec for mapping global credentials to YAML.

        Returns:
            OrderedDict: A spec consumed by `modify_parameters`.
        """
        # Mask helper builds a placeholder using description to ensure
        # stable variable names (e.g., { { cli_credential_desc_password } }).
        def mask(component_key, item, field):
            try:
                return self.generate_custom_variable_name(
                    item,
                    component_key,
                    "description",
                    field,
                )
            except Exception:
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
        return global_credential_details

    def assign_credentials_to_site_temp_spec(self):
        """Build temp spec for assigned credentials per site.

        Returns:
            OrderedDict: Spec for `modify_parameters` to map site assignments.
        """
        def pick_fields(src, fields):
            if not isinstance(src, dict):
                return None
            return {k: src.get(k) for k in fields if src.get(k) is not None}

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
        return assign_credentials_to_site

    def get_global_credential_details_configuration(self, network_element, component_specific_filters=None):
        """Retrieve and map global credential details.

        Applies optional component-specific filters, then maps results using
        `global_credential_details_temp_spec`.

        Args:
            network_element (dict): Unused; reserved for consistency.
            component_specific_filters (dict | None): Filter dict with lists keyed
                by credential groups (e.g., `cli_credential`).

        Returns:
            dict: `{ "global_credential_details": <mapped dict> }`.
        """
        self.log(
            (
                "Starting to retrieve global credential details with "
                "component-specific filters: {0}"
            ).format(component_specific_filters),
            "DEBUG",
        )
        final_global_credentials = []

        self.log(
            "type of global_credential_details: {0}".format(
                type(self.global_credential_details)
            ),
            "DEBUG",
        )
        self.log(
            "Retrieved global credential details: {0}".format(
                self.global_credential_details
            ),
            "DEBUG",
        )

        if component_specific_filters:
            filtered_credentials = self.filter_credentials(self.global_credential_details, component_specific_filters)
            self.log(
                (
                    "Filtered global credential details based on "
                    "component-specific filters: {0}"
                ).format(filtered_credentials),
                "DEBUG",
            )
            final_global_credentials = [filtered_credentials]
        else:
            final_global_credentials = [self.global_credential_details]

        global_credential_details_temp_spec = self.global_credential_details_temp_spec()
        mapped_list = self.modify_parameters(
            global_credential_details_temp_spec, final_global_credentials
        )
        mapped = mapped_list[0] if mapped_list else {}
        return {"global_credential_details": mapped}

    def filter_credentials(self, source, filters):
        """Filter credential groups by description.

        Args:
            source (dict): Global credentials grouped by keys like `cliCredential`.
            filters (dict): Desired descriptions per group (e.g., `{"cli_credential": [{"description": "WLC"}]}`).

        Returns:
            dict: Subset of `source` with only matching items per group.
        """
        key_map = {
            'cli_credential': 'cliCredential',
            'https_read': 'httpsRead',
            'https_write': 'httpsWrite',
            'snmp_v2c_read': 'snmpV2cRead',
            'snmp_v2c_write': 'snmpV2cWrite',
            'snmp_v3': 'snmpV3',
            'netconf_credential': 'netconfCredential',
        }
        result = {}
        for f_key, wanted_list in filters.items():
            src_key = key_map.get(f_key)
            if not src_key or src_key not in source:
                continue
            wanted_desc = {item.get('description') for item in wanted_list if 'description' in item}
            matched = [item for item in source[src_key] if item.get('description') in wanted_desc]
            if matched:
                result[src_key] = matched
        return result

    def get_assign_credentials_to_site_configuration(self, network_element, component_specific_filters=None):
        """Build assigned credential configuration per requested sites.

        Resolves site names to IDs, queries sync status, matches credential IDs
        against global credentials, and maps the first match per type to a
        dict suitable for YAML output.

        Args:
            network_element (dict): Contains API family and function names.
            component_specific_filters (dict | None): Contains `site_name` list.

        Returns:
            list | dict: One item per site `{ "assign_credentials_to_site": <mapped> }`,
            or empty dict if no sites resolved.
        """
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

    def yaml_config_generator(self, yaml_config_generator):
        """Generate the YAML configuration file for the module.

        Retrieves data for selected components using provided filters, maps
        them through temp specs, and writes the resulting structure to YAML.

        Args:
            yaml_config_generator (dict): Includes `file_path`, `global_filters`,
                and `component_specific_filters` plus `generate_all_configurations`.

        Returns:
            DeviceCredentialPlaybookGenerator: self.
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
            self.log(
                (
                    "Auto-discovery mode enabled - will process all devices and "
                    "all features"
                ),
                "INFO",
            )

        self.log(
            "Determining output file path for YAML configuration", "DEBUG"
        )
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No file_path provided by user, generating default filename",
                "DEBUG",
            )
            file_path = self.generate_filename()
        else:
            self.log(
                "Using user-provided file_path: {0}".format(file_path), "DEBUG"
            )

        self.log(
            "YAML configuration file path determined: {0}".format(file_path),
            "DEBUG",
        )

        self.log("Initializing filter dictionaries", "DEBUG")
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log(
                (
                    "Auto-discovery mode: Overriding any provided filters to "
                    "retrieve all devices and all features"
                ),
                "INFO",
            )
            if yaml_config_generator.get("global_filters"):
                self.log(
                    (
                        "Warning: global_filters provided but will be ignored "
                        "due to generate_all_configurations=True"
                    ),
                    "WARNING",
                )
            if yaml_config_generator.get("component_specific_filters"):
                self.log(
                    (
                        "Warning: component_specific_filters provided but will "
                        "be ignored due to generate_all_configurations=True"
                    ),
                    "WARNING",
                )

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
                    "Details retrieved for {0}: {1}".format(component, details),
                    "DEBUG",
                )
                if isinstance(details, list):
                    final_list.extend(details)
                else:
                    final_list.append(details)

        if not final_list:
            self.msg = (
                "No configurations or components to process for module "
                "'{0}'. Verify input filters or configuration."
            ).format(self.module_name)
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        final_dict = {"config": final_list}
        self.log("Final dictionary created: {0}".format(final_dict), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                (
                    "YAML config generation Task succeeded for module '{0}'."
                ).format(self.module_name): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                (
                    "YAML config generation Task failed for module '{0}'."
                ).format(self.module_name): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """Collect and store desired operation parameters.

        Validates input and prepares `self.want` for downstream operations.

        Args:
            config (dict): User-provided configuration.
            state (str): Desired state; supported: "gathered".
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state),
            "INFO",
        )

        self.validate_params(config)

        self.generate_all_configurations = config.get("generate_all_configurations", False)
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

    def get_diff_gathered(self):
        """Execute generation operations for the gathered state.

        Runs the YAML configuration generator and records timings and status.
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
                (
                    "Iteration {0}: Checking parameters for {1} operation with "
                    "param_key '{2}'."
                ).format(index, operation_name, param_key),
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    (
                        "Iteration {0}: Parameters found for {1}. Starting "
                        "processing."
                    ).format(index, operation_name),
                    "INFO",
                )
                operation_func(params).check_return_status()
            else:
                self.log(
                    (
                        "Iteration {0}: No parameters found for {1}. Skipping "
                        "operation."
                    ).format(index, operation_name),
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
        "config_verify": {"type": "bool", "default": False},
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

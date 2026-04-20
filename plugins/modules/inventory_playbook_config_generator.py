#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Inventory Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Mridul Saurabh, Sunil Shatagopa, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: inventory_playbook_config_generator
short_description: Generate YAML playbook for C(inventory_workflow_manager) module.
description:
- Generates YAML configurations compatible with the C(inventory_workflow_manager)
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the inventory configurations
  configured on the Cisco Catalyst Center.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Mridul Saurabh (@msaurabh12)
- Sunil Shatagopa (@shatagopasunil)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  file_path:
    description:
    - Path where the YAML configuration file will be saved.
    - If not provided, the file will be saved in the current working directory with
      a default file name  C(inventory_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
    - For example, C(inventory_playbook_config_2026-02-20_13-34-58.yml).
    type: str
  file_mode:
    description:
    - Controls how config is written to the YAML file.
    - C(overwrite) replaces existing file content.
    - C(append) appends generated YAML content to the existing file.
    - This parameter is only relevant when C(file_path) is specified. Defaults to C(overwrite).
    type: str
    choices: ["overwrite", "append"]
    default: "overwrite"
  config:
    description:
    - A dictionary of filters for generating YAML playbook compatible with the C(inventory_workflow_manager) module.
    - If config is not provided (omitted entirely), all configurations for all inventory devices will be generated.
    - This is useful for complete brownfield infrastructure discovery and documentation.
    - Important - An empty dictionary {} is not valid. Either omit 'config' entirely to generate
      all configurations, or provide specific filters within 'config'.
    type: dict
    required: false
    suboptions:
      global_filters:
        description:
        - Global filters used to filter inventory data.
        - Multiple filters under C(global_filters) are combined using logical AND.
        - At least one supported global filter must be provided when using C(global_filters).
        - Unknown keys fail validation with an error.
        type: dict
        suboptions:
          devices:
            description:
            - List of device identifier values to filter inventory records.
            - You can provide one or more values from C(ip_address), C(hostname), C(serial_number),
              or C(mac_address), and the module matches each value against these identifier fields.
            type: list
            elements: str
          device_roles:
            description:
            - List of inventory device roles to include.
            - Supported values are C(ACCESS), C(DISTRIBUTION), C(CORE), C(BORDER ROUTER), and C(UNKNOWN).
            type: list
            elements: str
            choices:
            - "ACCESS"
            - "DISTRIBUTION"
            - "CORE"
            - "BORDER ROUTER"
            - "UNKNOWN"
          device_types:
            description:
            - List of inventory device types to include.
            type: list
            elements: str
            choices:
            - "COMPUTE_DEVICE"
            - "MERAKI_DASHBOARD"
            - "THIRD_PARTY_DEVICE"
            - "NETWORK_DEVICE"
            - "ACCESS_POINT"
          device_identifier:
            description:
            - Identifier used to build the generated list key in output config.
            - The output key is written as C(<device_identifier>_list).
            type: str
            choices:
            - "ip_address"
            - "hostname"
            - "serial_number"
            - "mac_address"
            default: "ip_address"

requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
- Cisco Catalyst Center >= 2.3.7.9
- |-
  SDK Methods used are
  devices.Devices.get_device_list
- |-
  SDK/REST Paths used are
  GET /dna/intent/api/v1/network-device
  GET /dna/intent/api/v1/device-credential/network-device
- |
  Auto-discovery mode:
  When C(config) is omitted entirely, the module runs in auto-discovery mode and
  generates inventory configuration for all discovered devices without applying filters.
- |
  Filter behavior:
  When C(config.global_filters) is provided, C(devices), C(device_roles), and C(device_types) are
  applied with AND semantics. Unknown global filter keys fail validation with an error.
- |-
  Module result behavior (changed/ok/failed):
  The module result reflects local file state only, not Catalyst Center state.
  In overwrite mode, generated YAML is compared against existing file content after
  excluding generated comment lines. In append mode, only the last YAML
  document is considered for idempotency check.
  - changed=true (status: success): Generated configuration differs (or file does not exist), and file is written.
  - changed=false (status: ok): Generated configuration matches existing content, so write is skipped.
  - failed=true (status: failed): Validation/API/file-write failure occurred.
seealso:
- module: cisco.dnac.inventory_workflow_manager
  description: Module for managing inventory settings and workflows.
"""

EXAMPLES = r"""
- name: Auto-generate YAML Configuration for all inventory devices
  cisco.dnac.inventory_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log_level: "{{ dnac_log_level }}"
    dnac_log: true
    state: gathered
    # No config provided - generates all inventory configurations

- name: Generate YAML Configuration with file path and overwrite mode
  cisco.dnac.inventory_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log_level: "{{ dnac_log_level }}"
    dnac_log: true
    state: gathered
    file_path: "tmp/catc_inventory_config.yml"
    file_mode: "overwrite"

- name: Generate YAML Configuration filtered by device roles and types
  cisco.dnac.inventory_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log_level: "{{ dnac_log_level }}"
    dnac_log: true
    state: gathered
    file_path: "tmp/catc_filtered_inventory_config.yml"
    file_mode: "overwrite"
    config:
      global_filters:
        device_roles: ["ACCESS", "CORE"]
        device_types: ["NETWORK_DEVICE", "ACCESS_POINT"]
        device_identifier: "hostname"

- name: Generate YAML Configuration for selected devices using serial number and IP
  cisco.dnac.inventory_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log_level: "{{ dnac_log_level }}"
    dnac_log: true
    state: gathered
    file_path: "tmp/catc_inventory_config.yml"
    file_mode: "append"
    config:
      global_filters:
        devices:
          - "10.10.20.11"
          - "FDO1234A1BC"
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": {
            "configurations_count": 31,
            "file_mode": "overwrite",
            "file_path": "tmp/inventory_testing.yml",
            "message": "YAML configuration file generated successfully for module 'inventory_workflow_manager'",
            "status": "success"
        },
        "response": {
            "configurations_count": 31,
            "file_mode": "overwrite",
            "file_path": "tmp/inventory_testing.yml",
            "message": "YAML configuration file generated successfully for module 'inventory_workflow_manager'",
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
            "Configuration cannot be an empty dictionary. Either omit 'config' entirely to generate all configurations,
             or provide specific filters within 'config'.",
        "response":
            "Configuration cannot be an empty dictionary. Either omit 'config' entirely to generate all configurations,
             or provide specific filters within 'config'."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase
)
from collections import OrderedDict
import time


class InventoryPlaybookConfigGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for inventory config deployed within the Cisco Catalyst Center using the GET APIs.
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
        self.module_name = "inventory_workflow_manager"

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

        # Check if config is provided but empty - Error scenario
        if isinstance(self.config, dict) and len(self.config) == 0:
            self.msg = (
                "Configuration cannot be an empty dictionary. "
                "Either omit 'config' entirely to generate all configurations, "
                "or provide specific filters within 'config'."
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Check if configuration is not provided (None) - treat as generate_all
        if self.config is None:
            self.validated_config = {"generate_all_configurations": True}
            self.msg = "Configuration is not provided - treating as generate all config mode"
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "global_filters": {
                "type": "dict",
                "required": False
            }
        }

        # Validate params
        self.log("Validating configuration against schema", "DEBUG")
        valid_temp = self.validate_config_dict(self.config, temp_spec)

        self.log("Validating invalid parameters against provided config", "DEBUG")
        self.validate_invalid_params(self.config, temp_spec.keys())

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_elements_schema(self):
        """
        Constructs and returns a structured mapping for inventory global filters
        used by the playbook configuration generator workflow. This mapping defines
        supported filter keys used during input validation and downstream filtering logic.

        Args:
            self: Refers to the instance of the class containing helper methods.

        Return:
            dict: A dictionary containing "global_filters".
        """

        self.log("Building workflow filters schema for inventory module.", "DEBUG")

        schema = {
            "global_filters": {
                "devices": {
                    "type": "list",
                    "elements": "str",
                    "required": False,
                },
                "device_roles": {
                    "type": "list",
                    "elements": "str",
                    "required": False,
                    "choices": [
                        "ACCESS",
                        "DISTRIBUTION",
                        "CORE",
                        "BORDER ROUTER",
                        "UNKNOWN"
                    ]
                },
                "device_types": {
                    "type": "list",
                    "elements": "str",
                    "required": False,
                    "choices": [
                        "COMPUTE_DEVICE",
                        "MERAKI_DASHBOARD",
                        "THIRD_PARTY_DEVICE",
                        "NETWORK_DEVICE",
                        "ACCESS_POINT"
                    ]
                },
                "device_identifier": {
                    "type": "str",
                    "choices": ["ip_address", "hostname", "serial_number", "mac_address"],
                    "default": "ip_address",
                    "required": False
                }
            }
        }

        global_filters = list(schema["global_filters"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(global_filters)} global filter(s): {global_filters}",
            "INFO",
        )

        return schema

    def device_identifiers_temp_spec(self):
        """
        Constructs a temporary specification for device identifiers for inventory devices.
        This specification includes details such as IP address, hostname, serial number, MAC address, and role.
        This is used to transform the device identifiers in the inventory configuration.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of device identifier attributes.
        """

        self.log("Generating temporary specification for device identifiers.", "DEBUG")

        device_identifier_details = OrderedDict(
            {
                "ip_address": {"type": "str", "source_key": "managementIpAddress"},
                "hostname": {"type": "str", "source_key": "hostname"},
                "serial_number": {"type": "str", "source_key": "serialNumber"},
                "mac_address": {"type": "str", "source_key": "macAddress"},
                "role": {"type": "str", "source_key": "role"}
            }
        )

        return device_identifier_details

    def device_credentials_temp_spec(self):
        """
        Constructs a temporary specification for device credentials for inventory devices.
        This specification includes details such as username, password, and enable password.
        This is used to transform the device credentials in the inventory configuration.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of device credential attributes.
        """

        self.log("Generating temporary specification for device credentials.", "DEBUG")

        device_credential_details = OrderedDict(
            {
                "ip_address": {"type": "str", "source_key": "ipAddress"},
                "type": {"type": "str", "source_key": "type"},
                "cli_transport": {
                    "type": "str",
                    "source_key": "cliTransport",
                    "transform": lambda cli_transport: "telnet" if str(cli_transport).lower() == "telnet" else "ssh"
                },
                "netconf_port": {"type": "str", "source_key": "netconfPort"},
                "username": {"type": "str", "source_key": "userName"},
                "password": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda device_details: self.generate_sensitive_placeholder(
                        device_details, "password", "password"
                    ),
                },
                "enable_password": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda device_details: self.generate_sensitive_placeholder(
                        device_details, "enable_password", "enablePassword"
                    ),
                },
                "http_username": {"type": "str", "source_key": "httpUserName"},
                "http_password": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda device_details: self.generate_sensitive_placeholder(
                        device_details, "http_password", "httpPassword"
                    ),
                },
                "http_port": {"type": "str", "source_key": "httpPort"},
                "http_secure": {"type": "bool", "source_key": "httpSecure"},
                "snmp_version": {
                    "type": "str",
                    "source_key": "snmpVersion",
                    "transform": lambda snmp_version: snmp_version.lower() if snmp_version.lower() in ["v2", "v3"] else "v2"
                },
                "snmp_mode": {"type": "str", "source_key": "snmpMode"},
                "snmp_username": {"type": "str", "source_key": "snmpUserName"},
                "snmp_auth_passphrase": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda device_details: self.generate_sensitive_placeholder(
                        device_details, "snmp_auth_passphrase", "snmpAuthPassphrase"
                    ),
                },
                "snmp_auth_protocol": {"type": "str", "source_key": "snmpAuthProtocol"},
                "snmp_priv_passphrase": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda device_details: self.generate_sensitive_placeholder(
                        device_details, "snmp_priv_passphrase", "snmpPrivPassphrase"
                    ),
                },
                "snmp_priv_protocol": {"type": "str", "source_key": "snmpPrivProtocol"},
                "snmp_ro_community": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda device_details: self.generate_sensitive_placeholder(
                        device_details, "snmp_ro_community", "snmpROCommunity"
                    ),
                },
                "snmp_rw_community": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda device_details: self.generate_sensitive_placeholder(
                        device_details, "snmp_rw_community", "snmpRWCommunity"
                    ),
                },
                "snmp_retry": {"type": "int", "source_key": "snmpRetry"},
                "snmp_timeout": {"type": "int", "source_key": "snmpTimeout"},
                "compute_device": {"type": "bool", "source_key": "computeDevice"}
            }
        )

        return device_credential_details

    def apply_global_filters(self, inventory_config_data, global_filters):
        """
        Apply supported global filters to inventory configuration data.

        Supported global_filters keys:
            - devices (list): Match when any one of these record fields equals
              any provided value: ip_address, hostname, serial_number, mac_address.
            - device_roles (list): Match against record key 'role'.
            - device_types (list): Match against record key 'type'.

        Filter groups are combined using AND semantics.

        Args:
            inventory_config_data (list): List of device dictionaries to be filtered.
            global_filters (dict): Dictionary containing supported global filters.

        Returns:
            list: Filtered list of device dictionaries that match the global filter criteria.
        """

        if not global_filters:
            self.log("No global filters provided, skipping filtering step.", "DEBUG")
            return inventory_config_data

        self.log(
            "Applying global filters to inventory configuration data. Filters: {0}".format(
                self.pprint(global_filters)
            ),
            "DEBUG",
        )

        supported_filter_keys = {"devices", "device_roles", "device_types", "device_identifier"}
        unknown_filter_keys = sorted(set(global_filters.keys()) - supported_filter_keys)
        if unknown_filter_keys:
            self.log(
                "Ignoring unsupported global filter key(s): {0}".format(
                    unknown_filter_keys
                ),
                "WARNING",
            )

        devices_filter = global_filters.get("devices") or []
        roles_filter = global_filters.get("device_roles") or []
        types_filter = global_filters.get("device_types") or []

        if not devices_filter and not roles_filter and not types_filter:
            self.log(
                "No valid global filters provided within 'global_filters' for filtering. Skipping filtering step.",
                "DEBUG",
            )
            return inventory_config_data

        devices_values = {
            value for value in devices_filter if value is not None and value.strip()
        }
        roles_values = {
            value for value in roles_filter if value is not None and value.strip()
        }
        types_values = {
            value for value in types_filter if value is not None and value.strip()
        }

        self.log(
            "Resolved global filters - devices({0}): {1}, roles({2}): {3}, types({4}): {5}".format(
                len(devices_values), devices_values,
                len(roles_values), roles_values,
                len(types_values), types_values
            ),
            "DEBUG",
        )

        filtered_data = [
            record for record in inventory_config_data if isinstance(record, dict)
        ]

        if len(filtered_data) != len(inventory_config_data):
            self.log(
                "Skipped {0} non-dictionary record(s) before applying filters.".format(
                    len(inventory_config_data) - len(filtered_data)
                ),
                "DEBUG",
            )

        if devices_values:
            before_count = len(filtered_data)
            device_identifier_fields = [
                "ip_address",
                "hostname",
                "serial_number",
                "mac_address",
            ]
            filtered_data = [
                record
                for record in filtered_data
                if any(record.get(field) in devices_values for field in device_identifier_fields)
            ]
            self.log(
                "Applied 'devices' global filter. Records before: {0}, after: {1}.".format(
                    before_count, len(filtered_data)
                ),
                "DEBUG",
            )

        if roles_values:
            before_count = len(filtered_data)
            filtered_data = [
                record for record in filtered_data if record.get("role") in roles_values
            ]
            self.log(
                "Applied 'roles' global filter. Records before: {0}, after: {1}.".format(
                    before_count, len(filtered_data)
                ),
                "DEBUG",
            )

        if types_values:
            before_count = len(filtered_data)
            filtered_data = [
                record for record in filtered_data if record.get("type") in types_values
            ]
            self.log(
                "Applied 'types' global filter. Records before: {0}, after: {1}.".format(
                    before_count, len(filtered_data)
                ),
                "DEBUG",
            )

        self.log(
            "Completed filtering using global filters. Matched {0} of {1} input record(s). Filtered data: {2}"
            .format(
                len(filtered_data),
                len(inventory_config_data),
                filtered_data,
            ),
            "DEBUG",
        )

        return filtered_data

    def generate_sensitive_placeholder(self, device_details, attribute_name, attribute_source_key):
        """
        Generate an Ansible variable placeholder for sensitive attributes.

        Args:
            device_details (dict): Source device credential dictionary from API.
            attribute_name (str): Target attribute name used in generated variable
                naming (for example, password, snmp_ro_community).
            attribute_source_key (str): Source key to verify whether the sensitive
                value exists in the current record.

        Returns:
            str or None: Jinja placeholder string in the format
                '{{ ip_<normalized_ip>_<attribute_name> }}' when applicable,
                otherwise None.
        """

        self.log(
            "Generating sensitive placeholder for attribute '{0}' using source key '{1}'.".format(
                attribute_name, attribute_source_key
            ),
            "DEBUG",
        )

        if device_details.get(attribute_source_key) is None:
            self.log(
                "Skipping placeholder generation as source key '{0}' is not present in device details.".format(
                    attribute_source_key
                ),
                "DEBUG",
            )
            return None

        ip_address = device_details.get("ipAddress", "").strip()
        attr = (attribute_name or "").strip()

        if not ip_address or not attr:
            self.log(
                "Skipping placeholder generation due to missing ipAddress or attribute_name. ipAddress: '{0}', attribute_name: '{1}'".format(
                    ip_address, attr
                ),
                "DEBUG",
            )
            return None

        # Normalize IP and attribute to safe variable name format
        normalized_ip = ip_address.replace(".", "_")
        normalized_attr = attr.lower().replace(" ", "_")

        self.log(
            "Normalized values for placeholder generation - ip: '{0}', attribute: '{1}'".format(
                normalized_ip, normalized_attr
            ),
            "DEBUG",
        )

        place_holder = f"{{{{ ip_{normalized_ip}_{normalized_attr} }}}}"

        self.log(
            "Generated custom variable placeholder: {0}".format(place_holder),
            "DEBUG",
        )

        return place_holder

    def transform_config_using_device_identifier(self, inventory_config_data, device_identifier):
        """
        Transform inventory records to use selected device identifier list key.

        Args:
            inventory_config_data (list): List of device dictionaries.
            device_identifier (str): Selected identifier key from supported device
                identifiers.

        Returns:
            list: Updated list where only selected identifier is retained as
                '<device_identifier>_list' with a single-item list value.
        """

        if not isinstance(inventory_config_data, list):
            self.log(
                "Expected list for inventory_config_data, got '{0}'. Skipping IP transformation.".format(
                    type(inventory_config_data).__name__
                ),
                "WARNING",
            )
            return inventory_config_data

        supported_device_identifiers = [
            "ip_address",
            "hostname",
            "serial_number",
            "mac_address",
        ]
        if device_identifier not in supported_device_identifiers:
            self.log(
                "Unsupported device_identifier '{0}'. Supported values are: {1}. Returning unmodified config.".format(
                    device_identifier, supported_device_identifiers
                ),
                "WARNING",
            )
            return inventory_config_data

        device_identifier_list_key = "{0}_list".format(device_identifier)

        self.log(
            "Transforming device identifier '{0}' to '{1}' for {2} record(s).".format(
                device_identifier, device_identifier_list_key, len(inventory_config_data)
            ),
            "DEBUG",
        )

        transformed_inventory_config = []

        for device_info in inventory_config_data:
            if not isinstance(device_info, dict):
                self.log(
                    "Skipping non-dictionary record during IP transformation: {0}".format(
                        device_info
                    ),
                    "DEBUG",
                )
                continue

            identifier_value = device_info.get(device_identifier)
            if not identifier_value:
                self.log(
                    "Record does not contain valid '{0}'; skipping: {1}".format(
                        device_identifier, device_info
                    ),
                    "DEBUG",
                )
                continue

            # Keep selected <device_identifier>_list as first key and remove all identifier keys.
            transformed_device_info = {
                device_identifier_list_key: [identifier_value],
                **{
                    k: v
                    for k, v in device_info.items()
                    if k not in supported_device_identifiers
                },
            }
            transformed_inventory_config.append(transformed_device_info)

        return transformed_inventory_config

    def fetch_device_identifier_details(self):
        """
        Fetch and transform device identifier details from Catalyst Center inventory.

        Returns:
            list: Transformed list of device records containing identifier fields
                such as ip_address, hostname, serial_number, mac_address, and role.
        """

        self.log(
            "Fetching device identifier details using 'devices.get_device_list'.",
            "DEBUG",
        )

        final_device_identifier_details = []
        api_function, api_family = "get_device_list", "devices"
        device_identifier_details = self.execute_get_with_pagination(
            api_family, api_function
        )

        if not device_identifier_details:
            self.log(
                "No inventory devices found from 'get_device_list' API.",
                "DEBUG",
            )
            return final_device_identifier_details

        self.log(
            "Retrieved {0} raw device record(s) from inventory API. Data: {1}".format(
                len(device_identifier_details),
                self.pprint(device_identifier_details),
            ),
            "DEBUG",
        )

        final_device_identifier_details = self.modify_parameters(
            self.device_identifiers_temp_spec(), device_identifier_details
        )

        self.log(
            "Transformed inventory data into {0} device identifier record(s). Data: {1}".format(
                len(final_device_identifier_details),
                self.pprint(final_device_identifier_details),
            ),
            "INFO",
        )

        return final_device_identifier_details

    def fetch_device_credentials_by_ip(self, device_details_by_ip):
        """
        Fetch and transform device credential details for given device IP addresses.

        Args:
            device_details_by_ip (dict): Mapping of device IP address to identifier
                details.

        Returns:
            list: Transformed list of device credential records.
        """

        ip_addresses = list(device_details_by_ip.keys())
        self.log(
            "Fetching credentials for {0} device IP(s). IP list: {1}".format(
                len(ip_addresses),
                self.pprint(ip_addresses),
            ),
            "DEBUG",
        )

        raw_device_credential_response = self.dnac.execute_rest_api_call(
            method="GET",
            endpoint="/api/v1/device-credential/network-device",
            params={
                "deviceIps": ip_addresses
            }
        )

        if isinstance(raw_device_credential_response, dict):
            device_credential_details = raw_device_credential_response.get("response", [])
        else:
            device_credential_details = raw_device_credential_response or []

        if not device_credential_details:
            self.log(
                "No device credential records returned for requested device IPs.",
                "DEBUG",
            )
            return []

        self.log(
            "Retrieved {0} raw credential record(s) from API.".format(
                len(device_credential_details)
            ),
            "DEBUG",
        )

        final_device_credential_details = self.modify_parameters(
            self.device_credentials_temp_spec(), device_credential_details
        )

        self.log(
            "Transformed credential data into {0} record(s). Data: {1}".format(
                len(final_device_credential_details),
                self.pprint(final_device_credential_details),
            ),
            "INFO",
        )
        return final_device_credential_details

    def fetch_all_inventory_config(self):
        """
        Build merged inventory configuration by combining identifier and credential data.

        Returns:
            list: Inventory configuration records ready for downstream transformation
                and YAML generation.
        """

        self.log("Starting inventory configuration data aggregation.", "DEBUG")

        inventory_config_data = []

        device_identifier_details = self.fetch_device_identifier_details()
        if not device_identifier_details:
            self.log(
                "No device identifier details available to generate inventory configuration.",
                "DEBUG",
            )
            return inventory_config_data

        self.log(
            "Processing {0} device identifier record(s) for IP-index creation. Data: {1}".format(
                len(device_identifier_details),
                self.pprint(device_identifier_details),
            ),
            "DEBUG",
        )

        # Build an index of device details by management IP for fast lookups
        device_details_by_ip = {}
        for device_item in device_identifier_details:
            ip_address = device_item.get("ip_address")
            if not ip_address:
                self.log(
                    "Device item missing IP address, skipping: {0}".format(device_item),
                    "WARNING"
                )
                continue

            device_details_by_ip[ip_address] = device_item

        self.log(
            "Created device_details_by_ip index with {0} entry/entries. Data: {1}".format(
                len(device_details_by_ip),
                self.pprint(device_details_by_ip),
            ),
            "DEBUG",
        )

        device_credential_details = self.fetch_device_credentials_by_ip(device_details_by_ip)
        self.log(
            "Merging {0} credential record(s) with identifier data.".format(
                len(device_credential_details)
            ),
            "DEBUG",
        )

        for device_credential in device_credential_details:
            ip_address = device_credential.get("ip_address")
            if not ip_address:
                self.log(
                    "Device credential item missing IP address, skipping: {0}".format(device_credential),
                    "WARNING"
                )
                continue

            # Merge device identifier details with credentials based on IP address
            device_info = device_details_by_ip.get(ip_address, {})
            merged_device_info = {**device_info, **device_credential}
            inventory_config_data.append(merged_device_info)

        self.log(
            "Completed inventory data aggregation with {0} merged record(s). Data: {1}".format(
                len(inventory_config_data),
                self.pprint(inventory_config_data),
            ),
            "INFO",
        )

        return inventory_config_data

    def get_final_inventory_config(self, yaml_config_generator):
        """
        Retrieves the final inventory configuration data to be included in the YAML configuration file.

        Args:
            yaml_config_generator (dict): Contains global_filters.

        Returns:
            list: A list of inventory configuration dictionaries that will be included in the YAML file.
        """

        final_inventory_data = self.fetch_all_inventory_config()

        generate_all = yaml_config_generator.get("generate_all_configurations", False)

        if generate_all:
            self.log(
                "Auto-discovery mode enabled - will process all the config.",
                "INFO",
            )
            config_device_identifier = "ip_address"
        else:
            self.log(
                "Auto-discovery mode not enabled - applying global filters to filter inventory data.",
                "INFO",
            )
            global_filters = yaml_config_generator.get("global_filters", {})

            final_inventory_data = self.apply_global_filters(final_inventory_data, global_filters)
            self.log(
                "Inventory data count after applying global filters: {0}".format(
                    len(final_inventory_data)
                ),
                "DEBUG",
            )
            config_device_identifier = global_filters.get("device_identifier", "ip_address")

        self.log(
            "Device identifier selected for YAML configuration: '{0}'".format(config_device_identifier),
            "DEBUG"
        )
        transformed_inventory_config = self.transform_config_using_device_identifier(final_inventory_data, config_device_identifier)

        return transformed_inventory_config

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file for the inventory workflow based on the provided configuration parameters.

        Args:
            yaml_config_generator (dict): Contains global_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """

        final_inventory_config = self.get_final_inventory_config(yaml_config_generator)

        if not final_inventory_config:
            self.log(
                "No configurations retrieved for inventory workflow YAML generation after applying filters.",
                "WARNING",
            )
            self.msg = {
                "status": "ok",
                "message":
                    "No configurations found for module '{0}'. Verify filters applied and inventory data in Catalyst Center."
                    .format(self.module_name)
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        final_config = {"config": final_inventory_config}

        # Get file_path and file_mode from self.params (top-level parameters)
        file_path = self.params.get("file_path")
        if not file_path:
            self.log(
                "No file_path provided by user, generating default filename", "DEBUG"
            )
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        file_mode = self.params.get("file_mode", "overwrite")
        self.log(
            "YAML configuration file path determined: {0}, file_mode: {1}".format(
                file_path, file_mode
            ),
            "DEBUG",
        )

        file_written = self.write_dict_to_yaml(
            final_config,
            file_path,
            file_mode
        )

        if file_written:
            self.msg = {
                "status": "success",
                "message": "YAML configuration file generated successfully for module '{0}'".format(
                    self.module_name
                ),
                "file_path": file_path,
                "file_mode": file_mode,
                "configurations_count": len(final_inventory_config)
            }
            self.set_operation_result("success", True, self.msg, "INFO")

            self.log(
                "YAML configuration generation completed. File: {0}, Configs: {1}".format(
                    file_path,
                    len(final_inventory_config),
                ),
                "INFO",
            )
        else:
            self.msg = {
                "status": "ok",
                "message": "YAML configuration file already up-to-date for module '{0}'. No changes written.".format(
                    self.module_name
                ),
                "file_path": file_path,
                "file_mode": file_mode,
                "configurations_count": len(final_inventory_config)
            }
            self.set_operation_result("ok", False, self.msg, "INFO")

            self.log(
                "YAML configuration unchanged. File: {0}, Configs: {1}".format(
                    file_path,
                    len(final_inventory_config),
                ),
                "INFO",
            )

        return self

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for inventory workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.

        Returns:
            InventoryPlaybookConfigGenerator: Current instance after completing
                gathered-state processing.
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
        "state": {"default": "gathered", "choices": ["gathered"]},
        "file_path": {"required": False, "type": "str"},
        "file_mode": {
            "required": False,
            "type": "str",
            "default": "overwrite",
            "choices": ["overwrite", "append"],
        },
        "config": {"required": False, "type": "dict"},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    config_generator = InventoryPlaybookConfigGenerator(module)
    if (
        config_generator.compare_dnac_versions(
            config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for INVENTORY Module. Supported versions start from '2.3.7.9' onwards. ".format(
                config_generator.get_ccc_version()
            )
        )
        config_generator.set_operation_result(
            "failed", False, config_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = config_generator.params.get("state")

    # Check if the state is valid
    if state not in config_generator.supported_states:
        config_generator.status = "invalid"
        config_generator.msg = "State {0} is invalid".format(
            state
        )
        config_generator.check_return_status()

    # Validate the input parameters and check the return status
    config_generator.validate_input().check_return_status()

    config = config_generator.validated_config
    config_generator.get_want(
        config, state
    ).check_return_status()
    config_generator.get_diff_state_apply[
        state
    ]().check_return_status()

    module.exit_json(**config_generator.result)


if __name__ == "__main__":
    main()

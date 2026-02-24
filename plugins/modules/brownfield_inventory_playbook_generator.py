#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wired Campus Automation Module."""
from __future__ import absolute_import, division, print_function
from operator import index

__metaclass__ = type
__author__ = "Mridul Saurabh, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_inventory_playbook_generator
short_description: Generate YAML playbook input for 'inventory_workflow_manager' module.
description:
- Generates YAML input files for C(cisco.dnac.inventory_workflow_manager).
- Supports independent component generation for device details, SDA provisioning,
  interface details, and user-defined fields.
- Supports global device filters by IP, hostname, serial number, and MAC address.
- In non-auto mode, provide C(component_specific_filters.components_list) to
  control which component sections are generated.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Mridul Saurabh (@msaurabh)
- Madhan Sankaranarayanan (@madsanka)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the 'inventory_workflow_manager'
      module.
    - Filters specify which devices and credentials to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all devices in Cisco Catalyst Center.
          - This mode discovers all managed devices in Cisco Catalyst Center and extracts all device inventory configurations.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete brownfield infrastructure discovery and documentation.
          - Note - Only devices with manageable software versions are included in the output.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  C(inventory_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(inventory_workflow_manager_playbook_2026-01-24_12-33-20.yml).
        type: str
      global_filters:
        description:
        - Global filters to apply when generating the YAML configuration file.
        - These filters apply to all components unless overridden by component-specific filters.
        - Supports filtering devices by IP address, hostname, serial number, or MAC address.
        type: dict
        suboptions:
          ip_address_list:
            description:
            - List of device IP addresses to include in the YAML configuration file.
            - When specified, only devices with matching management IP addresses will be included.
            - For example, ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
            type: list
            elements: str
          hostname_list:
            description:
            - List of device hostnames to include in the YAML configuration file.
            - When specified, only devices with matching hostnames will be included.
            - For example, ["switch-1", "router-1", "firewall-1"]
            type: list
            elements: str
          serial_number_list:
            description:
            - List of device serial numbers to include in the YAML configuration file.
            - When specified, only devices with matching serial numbers will be included.
            - For example, ["ABC123456789", "DEF987654321"]
            type: list
            elements: str
          mac_address_list:
            description:
            - List of device MAC addresses to include in the YAML configuration file.
            - When specified, only devices with matching MAC addresses will be included.
            - For example, ["e4:1f:7b:d7:bd:00", "a1:b2:c3:d4:e5:f6"]
            type: list
            elements: str
      component_specific_filters:
        description:
        - Filters to specify which components and device attributes to include in the YAML configuration file.
        - If "components_list" is specified, only those components are included.
        - Additional filters can be applied to narrow down device selection based on role, type, etc.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are "device_details", "provision_device", and "interface_details".
            - If not specified, all components are included.
            type: list
            elements: str
            choices:
            - device_details
            - provision_device
            - interface_details
            - user_defined_field
          device_details:
            description:
            - Filters for device configuration generation.
            - Accepts a dict or a list of dicts.
            - List behavior: OR between dict entries.
            - Dict behavior: AND between filter keys.
            - Supported keys:
            - C(type): NETWORK_DEVICE, COMPUTE_DEVICE,
              MERAKI_DASHBOARD, THIRD_PARTY_DEVICE,
              FIREPOWER_MANAGEMENT_SYSTEM.
            - C(role): ACCESS, CORE, DISTRIBUTION, BORDER ROUTER,
              UNKNOWN.
            - C(snmp_version): v2, v2c, v3.
            - C(cli_transport): ssh or telnet.
            type: raw
            suboptions:
              role:
                description:
                - Filter devices by network role.
                - Can be a single role string or a list of roles (matches any in the list).
                - Valid values are ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN.
                - 'Example: role="ACCESS" for single role or role=["ACCESS", "CORE"] for multiple roles.'
                type: str
                choices: [ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN]
          provision_device:
            description:
            - Specific filters for provision_device component.
            - Filters the provision_wired_device configuration based on site assignment.
            - No additional API calls are made; filtering is applied to existing provision data.
            type: dict
            suboptions:
              site_name:
                description:
                - Filter provision devices by site name (e.g., Global/India/Telangana/Hyderabad/BLD_1).
                type: str
          interface_details:
            description:
            - Component selector for auto-generated interface_details.
            - Filters interface configurations based on device IP addresses and interface names.
            - Interfaces are automatically discovered from matched devices using Catalyst Center API.
            type: dict
            suboptions:
              interface_name:
                description:
                - Filter interfaces by name (optional).
                - Can be a single interface name string or a list of interface names.
                - When specified, only interfaces with matching names will be included.
                - Matches use 'OR' logic; any interface matching any name in the list is included.
                - Common interface names include Vlan100, Loopback0, GigabitEthernet1/0/1, or FortyGigabitEthernet1/1/1.
                - If not specified, all discovered interfaces for matched devices are included.
                - 'Example: interface_name="Vlan100" for single or interface_name=["Vlan100", "Loopback0"] for multiple.'
                type: str
          user_defined_fields:
            description:
            - Component selector for user-defined fields (UDF).
            - Fetches user-defined field definitions from Catalyst Center.
            - Cannot be used together with global_filters (global filters use IP-based device selection).
            - Optionally filter by user-defined field name.
            type: dict
            suboptions:
              udf_name:
                description:
                - Filter user-defined fields by name (optional).
                - Can be a single UDF name string or a list of UDF names.
                - When specified, only UDFs with matching names will be included.
                - Matches use 'OR' logic; any UDF matching any name in the list is included.
                - If not specified, all user-defined fields are included.
                - 'Example: udf_name="Cisco Switches" for single or udf_name=["Cisco Switches", "Test123"] for multiple.'
                type: str
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - devices.Devices.get_device_list
    - devices.Devices.get_network_device_by_ip
    - devices.Devices.get_device_by_ip
    - licenses.Licenses.device_license_summary
- API Endpoints used are GET /dna/intent/api/v2/devices (list all devices), GET /dna/intent/api/v2/network-device
  (get network device info), GET /dna/intent/api/v1/interface/ip-address/{ipAddress} (get interfaces for device IP),
  and GET /dna/intent/api/v1/licenses/device/summary (get device license and site info).
- 'Device Consolidation: Devices are grouped and consolidated by their configuration hash. All interfaces from devices
  with identical configurations are grouped under a single device entry. This reduces redundancy when multiple physical
  devices share the same configuration.'
- 'Component Independence: Each component (device_details, provision_device, interface_details) is filtered
  independently. Global filters apply to all components unless overridden by component-specific filters. Interface
  details are automatically fetched based on matched device IPs.'
- 'Interface Discovery: Interfaces are discovered using the IP-to-interface API endpoint. Interface names can be
  optionally filtered using the interface_name parameter. When no interfaces match the filter criteria, no
  interface_details output is generated.'
seealso:
- module: cisco.dnac.inventory_workflow_manager
  description: Module for managing inventory configurations in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate inventory playbook for all devices
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - generate_all_configurations: true
        file_path: "./inventory_devices_all.yml"

- name: Generate inventory playbook for specific devices by IP address
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
            - "10.195.225.42"
        file_path: "./inventory_devices_by_ip.yml"

- name: Generate inventory playbook for devices by hostname
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          hostname_list:
            - "cat9k_1"
            - "cat9k_2"
            - "switch_1"
        file_path: "./inventory_devices_by_hostname.yml"

- name: Generate inventory playbook for devices by serial number
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          serial_number_list:
            - "FCW2147L0AR1"
            - "FCW2147L0AR2"
        file_path: "./inventory_devices_by_serial.yml"

- name: Generate inventory playbook for mixed device filtering
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
          hostname_list:
            - "cat9k_1"
        file_path: "./inventory_devices_mixed_filter.yml"

- name: Generate inventory playbook with default file path
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"

- name: Generate inventory playbook for multiple devices
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
            - "10.195.225.41"
            - "10.195.225.42"
            - "10.195.225.43"
        file_path: "./inventory_devices_multiple.yml"

- name: Generate inventory playbook for ACCESS role devices only
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - component_specific_filters:
          components_list: ["device_details"]
          device_details:
            - role: "ACCESS"
        file_path: "./inventory_access_role_devices.yml"

- name: Generate inventory playbook with auto-populated provision_wired_device
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - generate_all_configurations: true
        file_path: "./inventory_with_provisioning.yml"

- name: Generate inventory playbook with interface filtering
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
            - "10.195.225.42"
        component_specific_filters:
          interface_details:
            interface_name:
              - "Vlan100"
              - "GigabitEthernet1/0/1"
        file_path: "./inventory_interface_filtered.yml"

- name: Generate inventory playbook for specific interface on single device
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
        component_specific_filters:
          interface_details:
            interface_name: "Loopback0"
        file_path: "./inventory_loopback_interface.yml"

- name: Generate complete inventory with all components and interface filter
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - component_specific_filters:
          components_list: ["device_details", "provision_device", "interface_details"]
          device_details:
            role: "ACCESS"
          interface_details:
            interface_name:
              - "GigabitEthernet1/0/1"
              - "GigabitEthernet1/0/2"
              - "GigabitEthernet1/0/3"
        file_path: "./inventory_access_with_interfaces.yml"
"""
RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: success
  type: dict
  sample: >
    {
        "msg": {
            "YAML config generation Task succeeded for module 'inventory_workflow_manager'.": {
            "file_path": "inventory_specific_ips.yml"
            }
        },
        "response": {
            "YAML config generation Task succeeded for module 'inventory_workflow_manager'.": {
            "file_path": "inventory_specific_ips.yml"
            }
        },
        "status": "success"
    }

# Case_2: Error Scenario
response_2:
  description: A string with the error message returned by the Cisco Catalyst Center Python SDK
  returned: on failure
  type: dict
  sample: >
    {
      "msg": "Invalid 'global_filters' found for module 'inventory_workflow_manager': [\"Filter 'ip_address_list' must be a list, got NoneType\"]",
      "response": "Invalid 'global_filters' found for module 'inventory_workflow_manager': [\"Filter 'ip_address_list' must be a list, got NoneType\"]"
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


class InventoryPlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.module_name = "inventory_workflow_manager"
        self.generate_all_configurations = False  # Initialize the attribute

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
        self.log("Validating configuration against schema.", "DEBUG")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log("Validating minimum requirements against provided config: {0}".format(self.config), "DEBUG")
        self.validate_minimum_requirements(self.config, require_global_filters=True)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_filters_schema(self):
        """
        Description: Returns the schema for workflow filters supported by the module.
        Returns:
            dict: A dictionary representing the schema for workflow filters.
        """
        self.log("Building workflow filter schema for inventory generation.", "DEBUG")

        schema = {
            "network_elements": {
                "device_details": {
                    "filters": ["ip_address", "hostname", "serial_number", "role"],
                    "api_function": "get_device_list",
                    "api_family": "devices",
                    "reverse_mapping_function": self.inventory_get_device_reverse_mapping,
                    "get_function_name": self.get_device_details_details,
                },
                "provision_device": {
                    "filters": ["site_name"],
                    "is_filter_only": True,
                },
                "interface_details": {
                    "filters": ["interface_name"],
                    "is_filter_only": True,
                },
                "user_defined_fields": {
                    "filters": ["udf_name"],
                    "api_function": "get_all_user_defined_fields",
                    "api_family": "devices",
                    "reverse_mapping_function": self.inventory_get_user_defined_fields_reverse_mapping,
                    "get_function_name": self.get_user_defined_fields_details,
                }
            },
            "global_filters": {
                "ip_address_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                    "validate_ip": True,
                },
                "hostname_list": {"type": "list", "required": False, "elements": "str"},
                "serial_number_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                },
                "mac_address_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                },
            },
            "component_specific_filters": {
                "components_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                    "choices": [
                        "device_details",
                        "provision_device",
                        "interface_details",
                        "user_defined_fields",
                    ],
                },
                "device_details": {
                    "type": {
                        "type": "str",
                        "required": False,
                        "choices": [
                            "NETWORK_DEVICE",
                            "COMPUTE_DEVICE",
                            "MERAKI_DASHBOARD",
                            "THIRD_PARTY_DEVICE",
                            "FIREPOWER_MANAGEMENT_SYSTEM",
                        ],
                    },
                    "role": {
                        "type": "str",
                        "required": False,
                        "choices": [
                            "ACCESS",
                            "CORE",
                            "DISTRIBUTION",
                            "BORDER ROUTER",
                            "UNKNOWN",
                        ],
                    },
                    "snmp_version": {
                        "type": "str",
                        "required": False,
                        "choices": ["v2", "v2c", "v3"],
                    },
                    "cli_transport": {
                        "type": "str",
                        "required": False,
                        "choices": ["ssh", "telnet", "SSH", "TELNET"],
                    },
                },
                "interface_details": {
                    "interface_name": {
                        "type": "list",
                        "required": False,
                        "elements": "str",
                    },
                },
                "user_defined_fields": {
                    "udf_name": {
                        "type": "list",
                        "required": False,
                        "elements": "str",
                    },
                },
            },
        }

        self.log(
            "Workflow filter schema built with components: {0}".format(
                list(schema.get("network_elements", {}).keys())
            ),
            "DEBUG",
        )

        return schema
    
    def fetch_all_devices(self, reason=""):
        """
        Fetch all devices from Cisco Catalyst Center API with pagination support.
        Handles large device inventories (500+ devices) by paginating through results.
        Deduplicates devices by UUID to prevent duplicate entries.

        Args:
            reason (str): Optional reason for fetching all devices (for logging)

        Returns:
            list: List of all device dictionaries from API
        """
        self.log(
            "Starting device inventory retrieval for playbook generation. "
            "Reason: {0}".format(reason if reason else "not provided"),
            "INFO",
        )

        all_devices = []
        seen_device_ids = set()
        offset = 1
        limit = 500
        page_number = 1

        try:
            while True:
                request_params = {"offset": offset, "limit": limit}
                self.log(
                    "Requesting device inventory page {0} with offset={1}, limit={2}".format(
                        page_number, offset, limit
                    ),
                    "DEBUG",
                )

                response = self.dnac._exec(
                    family="devices",
                    function="get_device_list",
                    op_modifies=False,
                    params=request_params,
                )

                if not isinstance(response, dict):
                    self.msg = (
                        "Invalid device inventory response type: expected dict, got {0}".format(
                            type(response).__name__
                        )
                    )
                    self.status = "failed"
                    self.log(self.msg, "ERROR")
                    return []

                page_devices = response.get("response", [])
                if page_devices is None:
                    page_devices = []

                if isinstance(page_devices, dict):
                    page_devices = [page_devices]
                elif not isinstance(page_devices, list):
                    self.msg = (
                        "Invalid device inventory payload type under 'response': "
                        "expected list or dict, got {0}".format(type(page_devices).__name__)
                    )
                    self.status = "failed"
                    self.log(self.msg, "ERROR")
                    return []

                if not page_devices:
                    self.log(
                        "No additional devices returned from API. Pagination complete at page {0}.".format(
                            page_number
                        ),
                        "DEBUG",
                    )
                    break

                added_count = 0
                for device in page_devices:
                    if not isinstance(device, dict):
                        continue

                    device_id = device.get("id") or device.get("instanceUuid")
                    if device_id and device_id in seen_device_ids:
                        continue

                    if device_id:
                        seen_device_ids.add(device_id)

                    all_devices.append(device)
                    added_count += 1

                self.log(
                    "Processed page {0}: received={1}, added={2}, cumulative_total={3}".format(
                        page_number, len(page_devices), added_count, len(all_devices)
                    ),
                    "INFO",
                )

                if len(page_devices) < limit:
                    self.log(
                        "Last page detected because returned records are fewer than the page limit.",
                        "DEBUG",
                    )
                    break

                offset += limit
                page_number += 1

            if all_devices:
                sample_fields = sorted(all_devices[0].keys())
                self.log(
                    "Completed device inventory retrieval. Total devices collected: {0}".format(
                        len(all_devices)
                    ),
                    "INFO",
                )
                self.log(
                    "Sample fields available in retrieved device payload: {0}".format(
                        sample_fields
                    ),
                    "DEBUG",
                )
            else:
                self.log(
                    "Completed device inventory retrieval with no devices returned.",
                    "WARNING",
                )

            return all_devices

        except Exception as e:
            self.msg = "Failed to retrieve device inventory from Catalyst Center: {0}".format(
                str(e)
            )
            self.status = "failed"
            self.log(self.msg, "ERROR")
            return []

    def process_global_filters(self, global_filters):
        """
        Retrieve device details for the provided global filters.

        Args:
            global_filters (dict): Filter dictionary with optional keys:
                ip_address_list, hostname_list, serial_number_list, mac_address_list.

        Returns:
            dict: {"device_ip_to_id_mapping": {<device_ip>: <device_info_dict>}}
        """
        self.log(
            "Collecting device inventory using global filter input: {0}".format(global_filters),
            "DEBUG",
        )

        device_ip_to_id_mapping = {}
        lookup_errors = 0

        def normalize_filter_values(filter_name):
            """Normalize filter values to a unique, non-empty string list."""
            raw_value = (global_filters or {}).get(filter_name)

            if raw_value is None:
                return []

            if isinstance(raw_value, str):
                raw_value = [raw_value]

            if not isinstance(raw_value, list):
                self.log(
                    "Skipping filter '{0}' because the value type is invalid: {1}".format(
                        filter_name, type(raw_value).__name__
                    ),
                    "WARNING",
                )
                return []

            normalized = []
            for item in raw_value:
                if not isinstance(item, str):
                    self.log(
                        "Ignoring non-string value in filter '{0}': {1}".format(
                            filter_name, item
                        ),
                        "WARNING",
                    )
                    continue
                item = item.strip()
                if item:
                    normalized.append(item)

            return list(dict.fromkeys(normalized))

        def add_device_to_mapping(device_info, filter_name, filter_value):
            """Add or refresh a device entry in the IP-to-device mapping."""
            if not isinstance(device_info, dict):
                return

            device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
            if not device_ip:
                self.log(
                    "Skipping device from {0}='{1}' because management IP is missing".format(
                        filter_name, filter_value
                    ),
                    "WARNING",
                )
                return

            existing_device = device_ip_to_id_mapping.get(device_ip)
            if existing_device is None:
                device_ip_to_id_mapping[device_ip] = device_info
                self.log(
                    "Added device '{0}' from {1}='{2}'".format(
                        device_ip, filter_name, filter_value
                    ),
                    "DEBUG",
                )
                return

            existing_keys = len(existing_device.keys()) if isinstance(existing_device, dict) else 0
            current_keys = len(device_info.keys())
            if current_keys > existing_keys:
                device_ip_to_id_mapping[device_ip] = device_info
                self.log(
                    "Refreshed device '{0}' with richer payload from {1}='{2}'".format(
                        device_ip, filter_name, filter_value
                    ),
                    "DEBUG",
                )

        def fetch_devices_by_query(param_key, param_value, filter_name):
            """
            Fetch devices from get_device_list with pagination for one filter value.
            """
            nonlocal lookup_errors
            offset = 1
            limit = 500
            page_number = 1

            while True:
                request_params = {param_key: param_value, "offset": offset, "limit": limit}
                self.log(
                    "Querying devices for {0}='{1}', page={2}, offset={3}, limit={4}".format(
                        filter_name, param_value, page_number, offset, limit
                    ),
                    "DEBUG",
                )

                try:
                    response = self.dnac._exec(
                        family="devices",
                        function="get_device_list",
                        op_modifies=False,
                        params=request_params,
                    )
                except Exception as error:
                    lookup_errors += 1
                    self.log(
                        "Device lookup failed for {0}='{1}': {2}".format(
                            filter_name, param_value, str(error)
                        ),
                        "ERROR",
                    )
                    return

                if not isinstance(response, dict):
                    lookup_errors += 1
                    self.log(
                        "Skipping {0}='{1}' because API response type is invalid: {2}".format(
                            filter_name, param_value, type(response).__name__
                        ),
                        "WARNING",
                    )
                    return

                records = response.get("response", [])
                if records is None:
                    records = []
                elif isinstance(records, dict):
                    records = [records]
                elif not isinstance(records, list):
                    lookup_errors += 1
                    self.log(
                        "Skipping {0}='{1}' because response payload type is invalid: {2}".format(
                            filter_name, param_value, type(records).__name__
                        ),
                        "WARNING",
                    )
                    return

                if not records:
                    self.log(
                        "No additional devices found for {0}='{1}'".format(
                            filter_name, param_value
                        ),
                        "DEBUG",
                    )
                    return

                for device_info in records:
                    add_device_to_mapping(device_info, filter_name, param_value)

                if len(records) < limit:
                    return

                offset += limit
                page_number += 1

        try:
            ip_address_list = normalize_filter_values("ip_address_list")
            hostname_list = normalize_filter_values("hostname_list")
            serial_number_list = normalize_filter_values("serial_number_list")
            mac_address_list = normalize_filter_values("mac_address_list")

            self.log(
                "Prepared filter counts for inventory lookup: ips={0}, hostnames={1}, "
                "serials={2}, macs={3}".format(
                    len(ip_address_list),
                    len(hostname_list),
                    len(serial_number_list),
                    len(mac_address_list),
                ),
                "INFO",
            )

            if (
                not ip_address_list
                and not hostname_list
                and not serial_number_list
                and not mac_address_list
            ):
                self.log(
                    "No valid global filters provided. Returning empty device mapping.",
                    "DEBUG",
                )
                return {"device_ip_to_id_mapping": {}}

            for ip_address in ip_address_list:
                self.log(
                    "Looking up device details for management IP '{0}'".format(ip_address),
                    "DEBUG",
                )
                try:
                    response = self.dnac._exec(
                        family="devices",
                        function="get_network_device_by_ip",
                        op_modifies=False,
                        params={"ip_address": ip_address},
                    )
                except Exception as error:
                    lookup_errors += 1
                    self.log(
                        "Management IP lookup failed for '{0}': {1}".format(
                            ip_address, str(error)
                        ),
                        "ERROR",
                    )
                    continue

                if not isinstance(response, dict):
                    lookup_errors += 1
                    self.log(
                        "Skipping IP '{0}' because API response type is invalid: {1}".format(
                            ip_address, type(response).__name__
                        ),
                        "WARNING",
                    )
                    continue

                device_payload = response.get("response")
                if isinstance(device_payload, list):
                    for device_info in device_payload:
                        add_device_to_mapping(device_info, "ip_address_list", ip_address)
                elif isinstance(device_payload, dict):
                    add_device_to_mapping(device_payload, "ip_address_list", ip_address)
                else:
                    self.log(
                        "No device found for management IP '{0}'".format(ip_address),
                        "WARNING",
                    )

            for hostname in hostname_list:
                fetch_devices_by_query("hostname", hostname, "hostname_list")

            for serial_number in serial_number_list:
                fetch_devices_by_query("serialNumber", serial_number, "serial_number_list")

            for mac_address in mac_address_list:
                fetch_devices_by_query("macAddress", mac_address, "mac_address_list")

            self.log(
                "Completed inventory lookup using global filters. Matched devices={0}, "
                "lookup_errors={1}".format(len(device_ip_to_id_mapping), lookup_errors),
                "INFO",
            )

            return {"device_ip_to_id_mapping": device_ip_to_id_mapping}

        except Exception as error:
            self.log(
                "Global filter processing failed unexpectedly: {0}".format(str(error)),
                "ERROR",
            )
            return {"device_ip_to_id_mapping": {}}

    def _get_device_mapping_spec(self):
        """
        Build and return the device field mapping specification.
        Defines transformation rules for mapping Catalyst Center API device fields
        to inventory_workflow_manager playbook format.

        Returns:
            OrderedDict: Mapping specification with field definitions and transform functions
        """
        # Valid enumeration values
        valid_device_types = {
            "NETWORK_DEVICE",
            "COMPUTE_DEVICE",
            "MERAKI_DASHBOARD",
            "THIRD_PARTY_DEVICE",
            "FIREPOWER_MANAGEMENT_SYSTEM",
        }
        valid_snmp_modes = {"NOAUTHNOPRIV", "AUTHNOPRIV", "AUTHPRIV"}

        # Helper transformation functions
        def parse_int(value, default):
            try:
                return int(value)
            except (TypeError, ValueError):
                return default

        def normalize_device_type(value):
            if isinstance(value, str):
                normalized = value.strip().upper()
                if normalized in valid_device_types:
                    return normalized
            return "NETWORK_DEVICE"

        def normalize_cli_transport(value):
            if not value:
                return "ssh"
            normalized = str(value).strip().lower()
            return normalized if normalized in {"ssh", "telnet"} else "ssh"

        def normalize_snmp_version(value):
            if not value:
                return "v2"
            normalized = str(value).strip().lower()
            if normalized in {"v2", "v2c"}:
                return "v2"
            if normalized == "v3":
                return "v3"
            return "v2"

        def normalize_snmp_mode(value):
            if isinstance(value, str):
                normalized = value.strip().upper()
                if normalized in valid_snmp_modes:
                    return normalized
            return "{{ item.snmp_mode }}"

        def value_or_template(value, template):
            return value if value not in (None, "") else template

        def normalize_bool(value, default=False):
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                lowered = value.strip().lower()
                if lowered in {"true", "yes", "1"}:
                    return True
                if lowered in {"false", "no", "0"}:
                    return False
            return default

        # Device field mapping specification
        mapping_spec = OrderedDict(
            {
                "ip_address_list": {
                    "type": "list",
                    "source_key": "managementIpAddress",
                    "transform": lambda x: [x] if x else [],
                },
                "type": {
                    "type": "str",
                    "source_key": "type",
                    "transform": normalize_device_type,
                },
                "role": {
                    "type": "str",
                    "source_key": "role",
                    "transform": lambda x: x if x else None,
                },
                "cli_transport": {
                    "type": "str",
                    "source_key": "cliTransport",
                    "transform": normalize_cli_transport,
                },
                "netconf_port": {
                    "type": "str",
                    "source_key": "netconfPort",
                    "transform": lambda x: str(x) if x not in (None, "") else "830",
                },
                "snmp_mode": {
                    "type": "str",
                    "source_key": "snmpMode",
                    "transform": normalize_snmp_mode,
                },
                "snmp_ro_community": {
                    "type": "str",
                    "source_key": "snmpRoCommunity",
                    "transform": lambda x: value_or_template(x, "{{ item.snmp_ro_community }}"),
                },
                "snmp_rw_community": {
                    "type": "str",
                    "source_key": "snmpRwCommunity",
                    "transform": lambda x: value_or_template(x, "{{ item.snmp_rw_community }}"),
                },
                "snmp_username": {
                    "type": "str",
                    "source_key": "snmpUsername",
                    "transform": lambda x: value_or_template(x, "{{ item.snmp_username }}"),
                },
                "snmp_auth_protocol": {
                    "type": "str",
                    "source_key": "snmpAuthProtocol",
                    "transform": lambda x: value_or_template(x, "{{ item.snmp_auth_protocol }}"),
                },
                "snmp_priv_protocol": {
                    "type": "str",
                    "source_key": "snmpPrivProtocol",
                    "transform": lambda x: value_or_template(x, "{{ item.snmp_priv_protocol }}"),
                },
                "snmp_retry": {
                    "type": "int",
                    "source_key": "snmpRetry",
                    "transform": lambda x: parse_int(x, 3),
                },
                "snmp_timeout": {
                    "type": "int",
                    "source_key": "snmpTimeout",
                    "transform": lambda x: parse_int(x, 5),
                },
                "snmp_version": {
                    "type": "str",
                    "source_key": "snmpVersion",
                    "transform": normalize_snmp_version,
                },
                "http_username": {
                    "type": "str",
                    "source_key": "httpUserName",
                    "transform": lambda x: value_or_template(x, "{{ item.http_username }}"),
                },
                "http_password": {
                    "type": "str",
                    "source_key": "httpPassword",
                    "transform": lambda x: value_or_template(x, "{{ item.http_password }}"),
                },
                "http_port": {
                    "type": "str",
                    "source_key": "httpPort",
                    "transform": lambda x: str(x) if x not in (None, "") else "{{ item.http_port }}",
                },
                "http_secure": {
                    "type": "bool",
                    "source_key": "httpSecure",
                    "transform": lambda x: normalize_bool(x, default=False),
                },
                "username": {
                    "type": "str",
                    "source_key": None,
                    "transform": lambda x: "{{ item.username }}",
                },
                "password": {
                    "type": "str",
                    "source_key": None,
                    "transform": lambda x: "{{ item.password }}",
                },
                "enable_password": {
                    "type": "str",
                    "source_key": None,
                    "transform": lambda x: "{{ item.enable_password }}",
                },
                "snmp_auth_passphrase": {
                    "type": "str",
                    "source_key": None,
                    "transform": lambda x: "{{ item.snmp_auth_passphrase }}",
                },
                "snmp_priv_passphrase": {
                    "type": "str",
                    "source_key": None,
                    "transform": lambda x: "{{ item.snmp_priv_passphrase }}",
                },
                "credential_update": {
                    "type": "bool",
                    "source_key": None,
                    "transform": lambda x: False,
                },
                "clean_config": {
                    "type": "bool",
                    "source_key": None,
                    "transform": lambda x: False,
                },
                "device_resync": {
                    "type": "bool",
                    "source_key": None,
                    "transform": lambda x: False,
                },
                "reboot_device": {
                    "type": "bool",
                    "source_key": None,
                    "transform": lambda x: False,
                },
                "add_user_defined_field": {
                    "type": "list",
                    "elements": "dict",
                    "name": {"type": "str"},
                    "description": {"type": "str"},
                    "value": {"type": "str"},
                },
                "provision_wired_device": {
                    "type": "list",
                    "elements": "dict",
                    "device_ip": {"type": "str"},
                    "site_name": {"type": "str"},
                    "resync_retry_count": {"default": 200, "type": "int"},
                    "resync_retry_interval": {"default": 2, "type": "int"},
                },
                "update_interface_details": {
                    "type": "dict",
                    "description": {"type": "str"},
                    "vlan_id": {"type": "int"},
                    "voice_vlan_id": {"type": "int"},
                    "interface_name": {"type": "list", "elements": "str"},
                    "deployment_mode": {"default": "Deploy", "type": "str"},
                    "clear_mac_address_table": {"default": False, "type": "bool"},
                    "admin_status": {"type": "str"},
                },
            }
        )

        return mapping_spec

    def inventory_get_device_reverse_mapping(self):
        """
        Returns reverse mapping specification for inventory devices.
        Transforms API response from Catalyst Center to inventory_workflow_manager format.
        Maps device attributes from API response to playbook configuration structure.
        Includes only fields needed for inventory_workflow_manager module.
        """
        self.log(
            "Preparing reverse mapping rules for device inventory transformation.",
            "DEBUG",
        )

        mapping_spec = self._get_device_mapping_spec()

        self.log(
            "Prepared reverse mapping rules for {0} device fields.".format(
                len(mapping_spec)
            ),
            "DEBUG",
        )

        return mapping_spec

    def fetch_device_site_mapping(self, device_id):
        """
        Fetch site assignment for a specific device.

        Args:
            device_id (str): Device UUID

        Returns:
            str: Site name path (e.g., "Global/USA/San Francisco/BGL_18") or empty string if not assigned
        """
        self.log(
            "Starting site assignment lookup for device_id='{0}'".format(device_id),
            "DEBUG",
        )

        if not device_id or not isinstance(device_id, str):
            self.log(
                "Skipping site assignment lookup because device_id is invalid: {0}".format(
                    device_id
                ),
                "WARNING",
            )
            return ""

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_assigned_site_for_device",
                params={"device_id": device_id},
                op_modifies=False,
            )

            self.log("Site assignment response for device {0}: {1}".format(device_id, response), "INFO")

            if not isinstance(response, dict):
                self.log(
                    "Site assignment lookup returned invalid response type for device_id='{0}': {1}".format(
                        device_id, type(response).__name__
                    ),
                    "WARNING",
                )
                return ""

            site_info = response.get("response")
            if not site_info:
                self.log(
                    "No site assignment data found for device_id='{0}'".format(device_id),
                    "DEBUG",
                )
                return ""

            if isinstance(site_info, list):
                site_info = site_info[0] if site_info else {}

            if not isinstance(site_info, dict):
                self.log(
                    "Site assignment payload is not a dictionary for device_id='{0}'".format(
                        device_id
                    ),
                    "WARNING",
                )
                return ""

            site_name_path = (
                site_info.get("groupNameHierarchy")
                or site_info.get("siteNameHierarchy")
                or site_info.get("nameHierarchy")
                or site_info.get("site")
            )

            if site_name_path:
                self.log(
                    "Resolved site assignment for device_id='{0}' to '{1}'".format(
                        device_id, site_name_path
                    ),
                    "DEBUG",
                )
                return site_name_path

            self.log(
                "Site assignment response did not contain hierarchy fields for device_id='{0}'".format(
                    device_id
                ),
                "DEBUG",
            )
            return ""

        except Exception as e:
            self.log("Error fetching site for device {0}: {1}".format(device_id, str(e)), "WARNING")
            return ""

    def fetch_user_defined_fields(self, udf_filter=None):
        """
        Fetch user-defined fields from Cisco Catalyst Center API.
        Validates input, optimizes API calls for single filters, and provides comprehensive error handling.

        Args:
            udf_filter (str or list): Optional filter by UDF name(s)

        Returns:
            list: List of user-defined field dictionaries with name, description, and value fields
        """
        self.log(
            "Starting user-defined field retrieval with filter input: {0}".format(udf_filter),
            "DEBUG",
        )

        # Validate and normalize filter input
        filter_names = []
        if udf_filter is not None:
            if isinstance(udf_filter, str):
                if udf_filter.strip():
                    filter_names = [udf_filter.strip()]
            elif isinstance(udf_filter, list):
                for item in udf_filter:
                    if isinstance(item, str) and item.strip():
                        filter_names.append(item.strip())
                    else:
                        self.log(
                            "Ignoring invalid user-defined field filter value: {0}".format(item),
                            "WARNING",
                        )
            else:
                self.msg = (
                    "Invalid udf_filter type. Expected str or list, got {0}.".format(
                        type(udf_filter).__name__
                    )
                )
                self.status = "failed"
                self.log(self.msg, "ERROR")
                return []

        # Remove duplicates while preserving order
        filter_names = list(dict.fromkeys(filter_names))
        filter_name_set = set(filter_names)

        try:
            # Optimize API call: use name parameter for single filter
            request_params = {}
            if len(filter_names) == 1:
                request_params["name"] = filter_names[0]
                self.log(
                    "Using API name filter for single UDF: '{0}'".format(filter_names[0]),
                    "DEBUG",
                )

            self.log(
                "Requesting user-defined fields with params: {0}".format(request_params),
                "DEBUG",
            )

            response = self.dnac._exec(
                family="devices",
                function="get_all_user_defined_fields",
                op_modifies=False,
                params=request_params,
            )

            # Validate response structure
            if not isinstance(response, dict):
                self.msg = (
                    "Invalid response type while retrieving user-defined fields: expected dict, got {0}".format(
                        type(response).__name__
                    )
                )
                self.status = "failed"
                self.log(self.msg, "ERROR")
                return []

            if "response" not in response:
                self.log(
                    "API response missing 'response' key for user-defined fields",
                    "WARNING",
                )
                return []

            udfs = response.get("response", [])
            
            # Validate response payload type
            if udfs is None:
                udfs = []
            elif isinstance(udfs, dict):
                udfs = [udfs]
            elif not isinstance(udfs, list):
                self.msg = (
                    "Invalid response payload type for user-defined fields: expected list, got {0}".format(
                        type(udfs).__name__
                    )
                )
                self.status = "failed"
                self.log(self.msg, "ERROR")
                return []

            self.log(
                "Retrieved {0} user-defined field(s) from Catalyst Center API".format(len(udfs)),
                "INFO",
            )

            # Transform UDF response: keep only name and description, set value to null
            transformed_udfs = []
            for udf in udfs:
                if not isinstance(udf, dict):
                    continue

                transformed_udf = {
                    "name": udf.get("name", ""),
                    "description": udf.get("description", ""),
                    "value": None,
                }
                transformed_udfs.append(transformed_udf)

            # Apply in-memory filtering for multiple names (API doesn't support multi-name filtering)
            if filter_names:
                filtered_udfs = [
                    udf for udf in transformed_udfs if udf.get("name") in filter_name_set
                ]

                # Warn about missing filter names
                matched_names = {udf.get("name") for udf in filtered_udfs if udf.get("name")}
                missing_names = sorted(filter_name_set - matched_names)
                if missing_names:
                    self.log(
                        "Requested user-defined fields not found: {0}".format(missing_names),
                        "WARNING",
                    )

                self.log(
                    "Filtered to {0} user-defined field(s) matching names: {1}".format(
                        len(filtered_udfs), filter_names
                    ),
                    "INFO",
                )
                return filtered_udfs
            else:
                self.log(
                    "Returning all {0} user-defined field(s) (no filter applied)".format(
                        len(transformed_udfs)
                    ),
                    "DEBUG",
                )
                return transformed_udfs

        except Exception as e:
            self.msg = "Failed to retrieve user-defined fields from Catalyst Center: {0}".format(
                str(e)
            )
            self.status = "failed"
            self.log(self.msg, "ERROR")
            return []

    def inventory_get_user_defined_fields_reverse_mapping(self):
        """
        Returns reverse mapping specification for user-defined fields.
        Transforms API response from Catalyst Center to inventory_workflow_manager format.
        Maps UDF attributes from API response to playbook configuration structure.
        """
        self.log(
            "Preparing mapping rules to transform user-defined field attributes.",
            "DEBUG",
        )

        return OrderedDict({
            "name": {
                "type": "str",
                "source_key": "name",
                "transform": lambda x: x if x else ""
            },
            "description": {
                "type": "str",
                "source_key": "description",
                "transform": lambda x: x if x else ""
            },
            "value": {
                "type": "str",
                "source_key": "value",
                "transform": lambda x: x if x else None
            }
        })

    def get_user_defined_fields_details(self, network_element, filters):
        """
        Retrieves user-defined fields from Cisco Catalyst Center API.
        Processes the response and transforms it to inventory_workflow_manager format.
        UDF component is independent and cannot be used with global_filters.
        """
        self.log("Starting get_user_defined_fields_details", "INFO")

        try:
            self.log(
                "Retrieving user-defined field details with request filters: {0}".format(filters),
                "DEBUG",
            )

            if not isinstance(filters, dict):
                self.log(
                    "Skipping user-defined field retrieval because filter payload type is invalid: {0}".format(
                        type(filters).__name__
                    ),
                    "ERROR",
                )
                return []

            component_specific_filters = filters.get("component_specific_filters") or {}
            if not isinstance(component_specific_filters, dict):
                self.log(
                    "Skipping user-defined field retrieval because component filter type is invalid: {0}".format(
                        type(component_specific_filters).__name__
                    ),
                    "ERROR",
                )
                return []

            udf_name_filter = component_specific_filters.get("udf_name")
            if udf_name_filter is not None and not isinstance(udf_name_filter, (str, list)):
                self.log(
                    "Ignoring unsupported user-defined field name filter type: {0}. "
                    "Proceeding without a name filter.".format(type(udf_name_filter).__name__),
                    "WARNING",
                )
                udf_name_filter = None

            if isinstance(network_element, dict):
                self.log(
                    "Using user-defined field source configuration: family={0}, function={1}".format(
                        network_element.get("api_family", "devices"),
                        network_element.get("api_function", "get_all_user_defined_fields"),
                    ),
                    "DEBUG",
                )

            self.log(
                "Requesting user-defined fields from Catalyst Center with name filter: {0}".format(
                    udf_name_filter
                ),
                "INFO",
            )
            udf_response = self.fetch_user_defined_fields(udf_filter=udf_name_filter)

            if not isinstance(udf_response, list):
                self.log(
                    "Received invalid user-defined field payload type: {0}".format(
                        type(udf_response).__name__
                    ),
                    "ERROR",
                )
                return []

            cleaned_udfs = []
            for udf in udf_response:
                if not isinstance(udf, dict):
                    self.log(
                        "Skipping invalid user-defined field record type: {0}".format(
                            type(udf).__name__
                        ),
                        "WARNING",
                    )
                    continue

                udf_name = udf.get("name")
                udf_description = udf.get("description")
                udf_value = udf.get("value")

                cleaned_udfs.append(
                    {
                        "name": str(udf_name).strip() if udf_name is not None else "",
                        "description": (
                            str(udf_description).strip() if udf_description is not None else ""
                        ),
                        "value": str(udf_value).strip() if udf_value not in (None, "") else None,
                    }
                )

            if not cleaned_udfs:
                self.log(
                    "No user-defined fields matched the requested criteria.",
                    "WARNING",
                )
                return []

            cleaned_udfs.sort(key=lambda item: item.get("name", "").lower())

            self.log(
                "Prepared {0} user-defined field entries for playbook output.".format(
                    len(cleaned_udfs)
                ),
                "INFO",
            )
            return [{"user_defined_fields": cleaned_udfs}]

        except Exception as e:
            self.log(
                "User-defined field retrieval failed while processing Catalyst Center data: {0}".format(
                    str(e)
                ),
                "ERROR",
            )
            import traceback

            self.log(
                "Detailed traceback for user-defined field retrieval failure: {0}".format(
                    traceback.format_exc()
                ),
                "DEBUG",
            )
            return []

    def build_provision_wired_device_config(self, device_list):
        """
        Build provision_wired_device configuration from device list.

        Args:
            device_list (list): List of device dictionaries from API

        Returns:
            list: List of provision_wired_device configuration dictionaries
        """
        if not isinstance(device_list, list):
            self.log(
                "Skipping provisioning entry creation because device input type is invalid: {0}".format(
                    type(device_list).__name__
                ),
                "ERROR",
            )
            return []

        self.log(
            "Preparing provisioning entries from {0} discovered device records.".format(
                len(device_list)
            ),
            "INFO",
        )

        provision_devices = []
        seen_device_ips = set()

        skipped_invalid_records = 0
        skipped_missing_ip = 0
        skipped_duplicates = 0
        placeholder_site_count = 0
        site_lookup_attempts = 0

        for index, device in enumerate(device_list, start=1):
            try:
                if not isinstance(device, dict):
                    skipped_invalid_records += 1
                    self.log(
                        "Skipping record {0} because device data is not a dictionary.".format(index),
                        "WARNING",
                    )
                    continue

                device_ip = device.get("managementIpAddress") or device.get("ipAddress")
                device_id = device.get("id") or device.get("instanceUuid")
                device_hostname = device.get("hostname", "Unknown")

                if isinstance(device_ip, str):
                    device_ip = device_ip.strip()

                if not device_ip:
                    skipped_missing_ip += 1
                    self.log(
                        "Skipping device '{0}' in record {1} because management IP is missing.".format(
                            device_hostname, index
                        ),
                        "DEBUG",
                    )
                    continue

                if device_ip in seen_device_ips:
                    skipped_duplicates += 1
                    self.log(
                        "Skipping duplicate provisioning entry for device IP '{0}'.".format(device_ip),
                        "DEBUG",
                    )
                    continue

                seen_device_ips.add(device_ip)
                site_name = (
                    device.get("siteNameHierarchy")
                    or device.get("groupNameHierarchy")
                    or device.get("nameHierarchy")
                    or device.get("site")
                )

                if isinstance(site_name, str):
                    site_name = site_name.strip()
                else:
                    site_name = ""

                if not site_name:
                    if device_id:
                        site_lookup_attempts += 1
                        site_name = self.fetch_device_site_mapping(device_id)
                        if isinstance(site_name, str):
                            site_name = site_name.strip()
                        else:
                            site_name = ""
                    else:
                        self.log(
                            "Using fallback site placeholder for device IP '{0}' because device ID is missing.".format(
                                device_ip
                            ),
                            "DEBUG",
                        )

                if not site_name:
                    site_name = "Global/{{ site_name }}"
                    placeholder_site_count += 1
                    self.log(
                        "Using fallback site placeholder for device IP '{0}'.".format(device_ip),
                        "DEBUG",
                    )

                provision_entry = {
                    "device_ip": device_ip,
                    "site_name": site_name,
                    "resync_retry_count": 200,
                    "resync_retry_interval": 2,
                }

                provision_devices.append(provision_entry)
                self.log(
                    "Prepared provisioning entry for device IP '{0}' with site '{1}'.".format(
                        device_ip, site_name
                    ),
                    "DEBUG",
                )

            except Exception as e:
                skipped_invalid_records += 1
                self.log(
                    "Skipping record {0} while preparing provisioning entries due to processing error: {1}".format(
                        index, str(e)
                    ),
                    "ERROR",
                )

        self.log(
            "Completed provisioning entry preparation. created={0}, lookups={1}, placeholders={2}, "
            "skipped_invalid={3}, skipped_missing_ip={4}, skipped_duplicates={5}".format(
                len(provision_devices),
                site_lookup_attempts,
                placeholder_site_count,
                skipped_invalid_records,
                skipped_missing_ip,
                skipped_duplicates,
            ),
            "INFO",
        )
        return provision_devices

    def fetch_sda_provision_device(self, device_ip):
        """
        Fetch SDA provision device information for a specific device IP.
        Uses the business SDA provision-device endpoint to check if device is provisioned.

        Args:
            device_ip (str): Device management IP address

        Returns:
            dict: Response containing device provisioning status and site, or None if error/not provisioned
        """
        self.log(
            "Checking SDA provisioning state for management IP '{0}'.".format(device_ip),
            "DEBUG",
        )

        if not isinstance(device_ip, str) or not device_ip.strip():
            self.log(
                "Skipping SDA provisioning lookup because management IP is invalid: {0}".format(
                    device_ip
                ),
                "WARNING",
            )
            return None

        device_ip = device_ip.strip()
        try:
            response = self.dnac._exec(
                family="sda",
                function="get_provisioned_wired_device",
                op_modifies=False,
                params={"device_management_ip_address": device_ip},
            )
        except Exception as e:
            self.log(
                "SDA provisioning lookup failed for management IP '{0}': {1}".format(
                    device_ip, str(e)
                ),
                "ERROR",
            )
            return None

        if not isinstance(response, dict):
            self.log(
                "Ignoring SDA provisioning response for management IP '{0}' because response "
                "type is invalid: {1}".format(device_ip, type(response).__name__),
                "WARNING",
            )
            return None

        self.log(
            "Received SDA provisioning response keys for management IP '{0}': {1}".format(
                device_ip, list(response.keys())
            ),
            "DEBUG",
        )

        response_payload = response.get("response")
        if isinstance(response_payload, dict):
            payload = response_payload
        elif isinstance(response_payload, list):
            payload = response_payload[0] if response_payload else {}
            if payload and not isinstance(payload, dict):
                payload = {}
        else:
            payload = response

        status_raw = payload.get("status", "")
        status = str(status_raw).strip().lower()
        description = payload.get("description", "")
        provisioned_ip = payload.get("deviceManagementIpAddress") or device_ip
        site_name_hierarchy = payload.get("siteNameHierarchy")

        if status != "success":
            self.log(
                "Device '{0}' is not provisioned in SDA. Status='{1}', description='{2}'.".format(
                    device_ip, status_raw, description
                ),
                "INFO",
            )
            return None

        if not site_name_hierarchy:
            self.log(
                "Device '{0}' returned success status but site hierarchy is missing. "
                "Skipping provisioning entry.".format(device_ip),
                "WARNING",
            )
            return None

        normalized_response = {
            "status": "success",
            "description": description,
            "deviceManagementIpAddress": provisioned_ip,
            "siteNameHierarchy": site_name_hierarchy,
        }

        self.log(
            "Device '{0}' is provisioned in SDA at site '{1}'.".format(
                provisioned_ip, site_name_hierarchy
            ),
            "INFO",
        )
        return normalized_response

    def build_provision_wired_device_from_sda_endpoint(self, device_configs):
        """
        Build provision_wired_device configuration from SDA provision-device endpoint.
        Queries each device IP individually to check provisioning status and site assignment.
        Only includes devices that are successfully provisioned to a site.

        Args:
            device_configs (list): List of filtered device configurations with ip_address_list

        Returns:
            dict: Configuration dictionary with provision_wired_device only for provisioned devices
        """
        self.log(
            "Building provision_wired_device configuration from SDA provision-device data.",
            "INFO",
        )

        if not isinstance(device_configs, list):
            self.log(
                "Skipping provisioning build because device_configs type is invalid: {0}".format(
                    type(device_configs).__name__
                ),
                "ERROR",
            )
            return {}

        filtered_device_ips = []
        invalid_config_entries = 0
        invalid_ip_values = 0

        for index, config in enumerate(device_configs, start=1):
            if not isinstance(config, dict):
                invalid_config_entries += 1
                self.log(
                    "Skipping config entry {0} because it is not a dictionary.".format(index),
                    "WARNING",
                )
                continue

            ip_list = config.get("ip_address_list", [])
            if isinstance(ip_list, str):
                ip_list = [ip_list]

            if not isinstance(ip_list, list):
                invalid_config_entries += 1
                self.log(
                    "Skipping config entry {0} because ip_address_list type is invalid: {1}".format(
                        index, type(ip_list).__name__
                    ),
                    "WARNING",
                )
                continue

            for ip_value in ip_list:
                if not isinstance(ip_value, str):
                    invalid_ip_values += 1
                    self.log(
                        "Ignoring non-string device IP value in config entry {0}: {1}".format(
                            index, ip_value
                        ),
                        "WARNING",
                    )
                    continue

                normalized_ip = ip_value.strip()
                if not normalized_ip:
                    invalid_ip_values += 1
                    self.log(
                        "Ignoring empty device IP value in config entry {0}.".format(index),
                        "WARNING",
                    )
                    continue

                filtered_device_ips.append(normalized_ip)

        if not filtered_device_ips:
            self.log(
                "No valid device IPs found for SDA provisioning lookup.",
                "WARNING",
            )
            return {}

        unique_device_ips = []
        seen_input_ips = set()
        duplicate_input_ips = 0

        for device_ip in filtered_device_ips:
            if device_ip in seen_input_ips:
                duplicate_input_ips += 1
                continue
            seen_input_ips.add(device_ip)
            unique_device_ips.append(device_ip)

        self.log(
            "Starting SDA provisioning checks for {0} unique device IPs "
            "(duplicates_removed={1}, invalid_configs={2}, invalid_ip_values={3}).".format(
                len(unique_device_ips),
                duplicate_input_ips,
                invalid_config_entries,
                invalid_ip_values,
            ),
            "INFO",
        )

        provision_devices = []
        seen_output_ips = set()
        not_provisioned_count = 0
        invalid_response_count = 0
        duplicate_output_count = 0

        for device_ip in unique_device_ips:
            try:
                provision_response = self.fetch_sda_provision_device(device_ip)

                if not provision_response:
                    not_provisioned_count += 1
                    self.log(
                        "Device '{0}' is not provisioned in SDA or lookup returned no data.".format(
                            device_ip
                        ),
                        "INFO",
                    )
                    continue

                if not isinstance(provision_response, dict):
                    invalid_response_count += 1
                    self.log(
                        "Skipping device '{0}' due to invalid provisioning response type: {1}".format(
                            device_ip, type(provision_response).__name__
                        ),
                        "WARNING",
                    )
                    continue

                device_mgmt_ip = provision_response.get("deviceManagementIpAddress") or device_ip
                site_name_hierarchy = provision_response.get("siteNameHierarchy")
                status = provision_response.get("status")

                if not site_name_hierarchy:
                    invalid_response_count += 1
                    self.log(
                        "Skipping device '{0}' because siteNameHierarchy is missing in SDA response.".format(
                            device_ip
                        ),
                        "WARNING",
                    )
                    continue

                if device_mgmt_ip in seen_output_ips:
                    duplicate_output_count += 1
                    self.log(
                        "Skipping duplicate provision output entry for device '{0}'.".format(
                            device_mgmt_ip
                        ),
                        "DEBUG",
                    )
                    continue

                seen_output_ips.add(device_mgmt_ip)

                provision_entry = {
                    "device_ip": device_mgmt_ip,
                    "site_name": site_name_hierarchy,
                    "resync_retry_count": 200,
                    "resync_retry_interval": 2,
                }

                provision_devices.append(provision_entry)
                self.log(
                    "Prepared provision entry from SDA response: IP='{0}', site='{1}', status='{2}'.".format(
                        device_mgmt_ip, site_name_hierarchy, status
                    ),
                    "DEBUG",
                )

            except Exception as e:
                invalid_response_count += 1
                self.log(
                    "Error while processing SDA provisioning for device '{0}': {1}".format(
                        device_ip, str(e)
                    ),
                    "ERROR",
                )
                continue

        self.log(
            "Completed SDA provisioning build. provisioned={0}, not_provisioned={1}, "
            "invalid_response={2}, duplicate_output={3}.".format(
                len(provision_devices),
                not_provisioned_count,
                invalid_response_count,
                duplicate_output_count,
            ),
            "INFO",
        )

        if not provision_devices:
            self.log("No provisioned devices found via SDA endpoint.", "WARNING")
            return {}

        return {"provision_wired_device": provision_devices}

    def build_update_interface_details_from_all_devices(self, device_configs, interface_name_filter=None):
        """
        Fetch interface details from all devices in device_configs and consolidate
        into separate update_interface_details configs grouped by interface configuration.
        Uses get_interface_by_ip endpoint to fetch actual interface information.

        Args:
            device_configs (list): List of device configuration dicts with ip_address_list
            interface_name_filter (list): Optional list of interface names to include. If specified, only these interfaces are included.

        Returns:
            list: List of update_interface_details configs with consolidated IP addresses
        """
        self.log(
            "Preparing interface update configurations from discovered devices.",
            "INFO",
        )

        if not isinstance(device_configs, list):
            self.log(
                "Skipping interface details generation because device_configs type is invalid: {0}".format(
                    type(device_configs).__name__
                ),
                "ERROR",
            )
            return []
        
        interface_name_filter_set = None
        if interface_name_filter:
            if isinstance(interface_name_filter, str):
                normalized_filter = interface_name_filter.strip()
                interface_name_filter_set = {normalized_filter} if normalized_filter else set()
            elif isinstance(interface_name_filter, list):
                interface_name_filter_set = {
                    item.strip()
                    for item in interface_name_filter
                    if isinstance(item, str) and item.strip()
                }
            else:
                self.log(
                    "Ignoring interface_name filter because type is invalid: {0}".format(
                        type(interface_name_filter).__name__
                    ),
                    "WARNING",
                )
                interface_name_filter_set = None

        try:
            if not device_configs:
                self.log("No device configs provided", "WARNING")
                return []

            collected_ips = []
            for index, config in enumerate(device_configs, start=1):
                if not isinstance(config, dict):
                    self.log(
                        "Skipping config entry {0} because it is not a dictionary.".format(index),
                        "WARNING",
                    )
                    self.log(
                        "Continuing to next config entry after invalid type at index {0}.".format(index),
                        "DEBUG",
                    )
                    continue

                ip_list = config.get("ip_address_list", [])
                if isinstance(ip_list, str):
                    ip_list = [ip_list]

                if not isinstance(ip_list, list):
                    self.log(
                        "Skipping config entry {0} because ip_address_list type is invalid: {1}".format(
                            index, type(ip_list).__name__
                        ),
                        "WARNING",
                    )
                    self.log(
                        "Continuing to next config entry after invalid ip_address_list at index {0}.".format(
                            index
                        ),
                        "DEBUG",
                    )
                    continue

                for ip in ip_list:
                    if isinstance(ip, str) and ip.strip():
                        collected_ips.append(ip.strip())

            if not collected_ips:
                self.log("No valid device IPs found for interface detail retrieval.", "WARNING")
                return []

            unique_device_ips = []
            seen_ips = set()
            for ip in collected_ips:
                if ip in seen_ips:
                    continue
                seen_ips.add(ip)
                unique_device_ips.append(ip)

            self.log(
                "Fetching interface details for {0} unique device IPs.".format(len(unique_device_ips)),
                "INFO",
            )

            interface_configs_by_hash = {}
            total_interfaces_seen = 0
            total_interfaces_included = 0
            device_errors = 0

            for device_ip in unique_device_ips:
                try:
                    interface_response = self.dnac._exec(
                        family="devices",
                        function="get_interface_by_ip",
                        op_modifies=False,
                        params={"ip_address": device_ip},
                    )
                except Exception as e:
                    device_errors += 1
                    self.log(
                        "Interface retrieval failed for device '{0}': {1}".format(
                            device_ip, str(e)
                        ),
                        "ERROR",
                    )
                    self.log(
                        "Continuing to next device after interface retrieval failure for '{0}'.".format(
                            device_ip
                        ),
                        "DEBUG",
                    )
                    continue

                if not isinstance(interface_response, dict):
                    device_errors += 1
                    self.log(
                        "Skipping device '{0}' because interface response type is invalid: {1}".format(
                            device_ip, type(interface_response).__name__
                        ),
                        "WARNING",
                    )
                    self.log(
                        "Continuing to next device after invalid interface response for '{0}'.".format(
                            device_ip
                        ),
                        "DEBUG",
                    )
                    continue

                interfaces = interface_response.get("response", [])
                if interfaces is None:
                    interfaces = []
                elif isinstance(interfaces, dict):
                    interfaces = [interfaces]
                elif not isinstance(interfaces, list):
                    device_errors += 1
                    self.log(
                        "Skipping device '{0}' because interface payload type is invalid: {1}".format(
                            device_ip, type(interfaces).__name__
                        ),
                        "WARNING",
                    )
                    self.log(
                        "Continuing to next device after invalid interface payload for '{0}'.".format(
                            device_ip
                        ),
                        "DEBUG",
                    )
                    continue

                for interface in interfaces:
                    if not isinstance(interface, dict):
                        self.log(
                            "Skipping interface entry because payload is not a dictionary.",
                            "DEBUG",
                        )
                        continue

                    total_interfaces_seen += 1

                    interface_name = interface.get("name") or interface.get("portName") or ""
                    interface_name = interface_name.strip() if isinstance(interface_name, str) else ""
                    if not interface_name:
                        self.log(
                            "Skipping interface entry on device '{0}' because name is missing.".format(
                                device_ip
                            ),
                            "DEBUG",
                        )
                        continue

                    if interface_name_filter_set is not None and interface_name not in interface_name_filter_set:
                        self.log(
                            "Skipping interface '{0}' on device '{1}' because it is not in the filter list.".format(
                                interface_name, device_ip
                            ),
                            "DEBUG",
                        )
                        continue

                    interface_config = {
                        "description": interface.get("description") or "",
                        "admin_status": interface.get("adminStatus") or "",
                        "vlan_id": interface.get("vlanId") or interface.get("nativeVlanId"),
                        "voice_vlan_id": interface.get("voiceVlan"),
                        "interface_name": [interface_name],
                        "deployment_mode": "Deploy",
                        "clear_mac_address_table": False,
                    }

                    config_hash = (
                        interface_config["description"],
                        interface_config["admin_status"],
                        interface_config["vlan_id"],
                        interface_config["voice_vlan_id"],
                        interface_name,
                        interface_config["deployment_mode"],
                        interface_config["clear_mac_address_table"],
                    )

                    if config_hash not in interface_configs_by_hash:
                        interface_configs_by_hash[config_hash] = {
                            "ip_address_list": [],
                            "update_interface_details": interface_config,
                        }

                    if device_ip not in interface_configs_by_hash[config_hash]["ip_address_list"]:
                        interface_configs_by_hash[config_hash]["ip_address_list"].append(device_ip)

                    total_interfaces_included += 1

            update_interface_configs = list(interface_configs_by_hash.values())

            self.log(
                "Interface detail generation completed. groups={0}, interfaces_seen={1}, "
                "interfaces_included={2}, device_errors={3}".format(
                    len(update_interface_configs),
                    total_interfaces_seen,
                    total_interfaces_included,
                    device_errors,
                ),
                "INFO",
            )
            return update_interface_configs

        except Exception as e:
            self.log("Error building update_interface_details from all devices: {0}".format(str(e)), "ERROR")
            return []

    def transform_ip_address_list(self, api_value):

        """
        Transform API ipAddress to ip_address_list format.
        Ensures it's always returned as a list.
        """
        if not api_value:
            return []
        if isinstance(api_value, list):
            return [ip.strip() for ip in api_value if isinstance(ip, str) and ip.strip()]

        if isinstance(api_value, str):
            api_value = api_value.strip()
            return [api_value] if api_value else []

        return []

    def get_device_details_details(self, network_element, filters):
        """
        Retrieves inventory device credentials from Cisco Catalyst Center API.
        Processes the response and transforms it using the reverse mapping specification.
        Captures FULL device response with all available fields.
        """
        self.log("Retrieving device details for inventory playbook generation.", "INFO")

        if not isinstance(filters, dict):
            self.log(
                "Skipping device details retrieval because filters type is invalid: {0}".format(
                    type(filters).__name__
                ),
                "ERROR",
            )
            return []

        try:
            reverse_mapping_spec = self.inventory_get_device_reverse_mapping()
            global_filters = filters.get("global_filters") or {}
            component_specific_filters = filters.get("component_specific_filters") or {}
            generate_all = bool(filters.get("generate_all_configurations", False))

            if not isinstance(global_filters, dict):
                self.log(
                    "Ignoring invalid global_filters type: {0}".format(type(global_filters).__name__),
                    "WARNING",
                )
                global_filters = {}

            if not isinstance(component_specific_filters, (dict, list)):
                self.log(
                    "Ignoring invalid component-specific filter type: {0}".format(
                        type(component_specific_filters).__name__
                    ),
                    "WARNING",
                )
                component_specific_filters = {}

            has_global_filters = bool(global_filters and any(global_filters.values()))

            self.log("Filters received - Global: {0}, Component: {1}, Generate All: {2}".format(
                global_filters, component_specific_filters, generate_all
            ), "DEBUG")

            device_response = []

            try:
                if generate_all:
                    device_response = self.fetch_all_devices(
                        reason="generate_all_configurations enabled"
                    )
                elif has_global_filters:
                    filter_result = self.process_global_filters(global_filters)
                    mapping = {}
                    if isinstance(filter_result, dict):
                        mapping = filter_result.get("device_ip_to_id_mapping", {})
                    if isinstance(mapping, dict):
                        device_response = list(mapping.values())
                    self.log(
                        "Device lookup with global filters returned {0} record(s).".format(
                            len(device_response)
                        ),
                        "INFO",
                    )
                else:
                    device_response = self.fetch_all_devices(
                        reason="no global filters provided"
                    )
            except Exception as e:
                self.log(
                    "Device retrieval failed: {0}".format(str(e)),
                    "ERROR",
                )
                return []

            if device_response and has_global_filters:
                first_device = device_response[0]
                if isinstance(first_device, dict):
                    self.log(
                        "Sample filtered device fields: {0}".format(list(first_device.keys())),
                        "INFO",
                    )
                    self.log(
                        "Sample filtered device data: {0}".format(first_device),
                        "DEBUG",
                    )

            self.log("Retrieved {0} devices before component filtering".format(len(device_response)), "INFO")

            if not isinstance(device_response, list):
                self.log(
                    "Invalid device response type received: {0}".format(type(device_response).__name__),
                    "ERROR",
                )
                return []

            device_response = [d for d in device_response if isinstance(d, dict)]
            if not device_response:
                self.log("No device data available after retrieval and normalization.", "WARNING")
                return []

            # ✅ Log what fields are actually available in the device_response
            sample_device = device_response[0]
            available_fields = list(sample_device.keys())
            self.log("Available fields in device response: {0}".format(available_fields), "INFO")
            self.log("Total fields available: {0}".format(len(available_fields)), "INFO")

            # Check which fields from reverse_mapping_spec are missing
            missing_fields = []
            for playbook_key, mapping_spec in reverse_mapping_spec.items():
                source_key = mapping_spec.get("source_key")
                if source_key and source_key not in sample_device:
                    missing_fields.append(source_key)

            if missing_fields:
                self.log("WARNING: {0} fields from reverse_mapping_spec are NOT in API response: {1}".format(
                    len(missing_fields), missing_fields
                ), "WARNING")
            else:
                self.log("All fields from reverse_mapping_spec are present in API response", "INFO")

            if component_specific_filters:
                filtered_devices = self.apply_component_specific_filters(
                    device_response, component_specific_filters
                )
                if filtered_devices is None:
                    self.log("Component-specific filter validation failed.", "ERROR")
                    return []
                device_response = filtered_devices

            if not device_response:
                self.log("No devices matched requested component-specific filters.", "WARNING")
                return []

            transformed_devices = self.transform_device_to_playbook_format(
                reverse_mapping_spec, device_response
            )

            if not transformed_devices:
                self.log("No transformed device configurations were generated.", "WARNING")
                return []

            provision_source_devices = []
            try:
                if generate_all or not has_global_filters:
                    provision_source_devices = self.fetch_all_devices(
                        reason="building provision_wired_device section"
                    )
                else:
                    provision_filter_result = self.process_global_filters(global_filters)
                    provision_mapping = {}
                    if isinstance(provision_filter_result, dict):
                        provision_mapping = provision_filter_result.get("device_ip_to_id_mapping", {})
                    if isinstance(provision_mapping, dict):
                        provision_source_devices = list(provision_mapping.values())
            except Exception as e:
                self.log(
                    "Provision source retrieval failed: {0}".format(str(e)),
                    "ERROR",
                )
                provision_source_devices = []

            if provision_source_devices:
                transformed_for_provision = self.transform_device_to_playbook_format(
                    reverse_mapping_spec, provision_source_devices
                )
                provision_config = self.build_provision_wired_device_from_sda_endpoint(
                    transformed_for_provision
                )
                if (
                    isinstance(provision_config, dict)
                    and provision_config.get("provision_wired_device")
                ):
                    transformed_devices.append(provision_config)
                    self.log(
                        "Appended provision_wired_device section with {0} entries.".format(
                            len(provision_config.get("provision_wired_device", []))
                        ),
                        "INFO",
                    )

            return transformed_devices

        except Exception as e:
            self.log("Error in get_device_details_details: {0}".format(str(e)), "ERROR")
            import traceback
            self.log("Traceback: {0}".format(traceback.format_exc()), "ERROR")
            return []

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

        if not isinstance(yaml_config_generator, dict):
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(self.module_name): {
                    "reason": "Invalid input for configuration generation. Expected a dictionary.",
                    "status": "INVALID_INPUT",
                }
            }
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.generate_all_configurations = bool(
            yaml_config_generator.get("generate_all_configurations", False)
        )

        file_path = yaml_config_generator.get("file_path") or self.generate_filename()
        self.log("YAML output file path resolved: {0}".format(file_path), "DEBUG")

        module_supported_network_elements = self.module_schema.get("network_elements", {})

        if self.generate_all_configurations:
            global_filters = {}
            component_specific_filters = {}
        else:
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        if not isinstance(global_filters, dict):
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(self.module_name): {
                    "reason": "global_filters must be a dictionary.",
                    "status": "INVALID_GLOBAL_FILTERS",
                }
            }
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        if not isinstance(component_specific_filters, dict):
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(self.module_name): {
                    "reason": "component_specific_filters must be a dictionary.",
                    "status": "INVALID_COMPONENT_FILTERS",
                }
            }
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Extract and validate components_list from component_specific_filters
        # Supports: None (defaults to all), string (single component), or list/tuple/set (multiple components)
        raw_components_list = component_specific_filters.get("components_list")
        if raw_components_list is None:
            # Default: process all supported network elements
            components_list = list(module_supported_network_elements.keys())
        elif isinstance(raw_components_list, str):
            # Single component provided as string
            components_list = [raw_components_list]
        elif isinstance(raw_components_list, (list, tuple, set)):
            # Multiple components provided as iterable
            components_list = list(raw_components_list)
        else:
            # Invalid type - fail fast
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(self.module_name): {
                    "reason": "components_list must be a string, list, tuple, or set.",
                    "status": "INVALID_COMPONENTS_LIST",
                }
            }
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Normalize components: strip whitespace, remove duplicates, validate types
        normalized_components = []
        for component in components_list:
            if not isinstance(component, str) or not component.strip():
                self.log("Ignoring invalid component value: {0}".format(component), "WARNING")
                continue
            component_name = component.strip()
            # Preserve order, avoid duplicates
            if component_name not in normalized_components:
                normalized_components.append(component_name)

        # Identify unsupported components and log warnings (non-fatal)
        unsupported_components = [
            component
            for component in normalized_components
            if component not in module_supported_network_elements
        ]
        if unsupported_components:
            self.log("Ignoring unsupported component(s): {0}".format(unsupported_components), "WARNING")

        # Filter to only include supported components
        components_list = [
            component
            for component in normalized_components
            if component in module_supported_network_elements
        ]

        # Validate constraint: user_defined_fields is incompatible with global_filters
        # user_defined_fields operates independently (no IP-based filtering)
        # global_filters are IP-based device filters (apply only to device_details)
        has_user_defined_fields = "user_defined_fields" in components_list
        has_global_filters = any(bool(value) for value in global_filters.values())

        if has_user_defined_fields and has_global_filters:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(self.module_name): {
                    "reason": (
                        "user_defined_fields component cannot be used with global_filters "
                        "(global filters are IP-based device filtering)."
                    ),
                    "status": "INVALID_FILTER_COMBINATION",
                }
            }
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log("Retrieving module-supported network elements", "DEBUG")

        self.log(
            "Retrieved {0} supported network elements: {1}".format(
                len(module_supported_network_elements),
                list(module_supported_network_elements.keys()),
            ),
            "DEBUG",
        )

        self.log(
            "Components list determined (independent): {0}".format(components_list), "DEBUG"
        )

        # For filter-only components (provision_device, interface_details), we need device_details data
        # So we fetch device_details internally if any filter-only component is requested
        components_to_fetch = list(components_list)
        has_filter_only_component = any(
            module_supported_network_elements.get(component, {}).get("is_filter_only", False)
            for component in components_list
        )
        if has_filter_only_component and "device_details" not in components_to_fetch:
            components_to_fetch.insert(0, "device_details")

        self.log(
            "Components to fetch internally: {0}".format(components_to_fetch), "DEBUG"
        )

        final_list = []
        for component in components_to_fetch:
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Skipping unsupported network element: {0}".format(component),
                    "WARNING",
                )
                continue

            # Skip provision_device in this loop as it's a filter-only component
            # It will be handled after provision_wired_device is built
            # Also skip user_defined_fields as it's an independent component processed separately
            if network_element.get("is_filter_only") or component == "user_defined_fields":
                self.log("Skipping filter-only or independent component: {0}".format(component), "DEBUG")
                continue

            operation_func = network_element.get("get_function_name")
            if not callable(operation_func):
                self.log(
                    "Skipping component '{0}' due to unavailable operation.".format(component),
                    "WARNING",
                )
                continue

            filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters.get(component, {}),
                "generate_all_configurations": self.generate_all_configurations,
            }

            self.log("Collecting data for component '{0}'.".format(component), "INFO")
            details = operation_func(network_element, filters)

            if self.status == "failed":
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            if isinstance(details, list):
                final_list.extend([item for item in details if item])
            elif isinstance(details, dict):
                final_list.append(details)
            elif details is not None:
                self.log(
                    "Skipping unexpected response type for component '{0}': {1}".format(
                        component, type(details).__name__
                    ),
                    "WARNING",
                )

        self.log(
            "Completed processing all components. Total configurations: {0}".format(
                len(final_list)
            ),
            "INFO",
        )

        # Separate provision_wired_device config from device configs
        device_configs = []
        provision_config = None

        self.log("Separating configs from final_list with {0} total items".format(len(final_list)), "DEBUG")

        for idx, config in enumerate(final_list):
            self.log("Config {0}: keys = {1}".format(idx, list(config.keys()) if isinstance(config, dict) else type(config)), "DEBUG")
            # Check if this is the main provision_wired_device config (not the null field in device configs)
            if isinstance(config, dict) and "provision_wired_device" in config and isinstance(config.get("provision_wired_device"), list):
                provision_config = config
                self.log("Found provision_wired_device config at index {0}".format(idx), "DEBUG")
            else:
                device_configs.append(config)
                self.log("Added device config at index {0}".format(idx), "DEBUG")

        self.log("Separated configs - Device configs: {0}, Provision config: {1}".format(
            len(device_configs), "yes" if provision_config else "no"), "DEBUG")

        # Filter provision_wired_device by site_name if provision_device component is specified
        # Each component filter is INDEPENDENT - provision_device filter only affects provision output
        if provision_config and "provision_device" in components_list:
            provision_device_filters = component_specific_filters.get("provision_device", {})
            site_name_filter = provision_device_filters.get("site_name")

            if site_name_filter:
                self.log("Applying provision_device site_name filter (independent of device_details filter)", "INFO")
                self.log("Filtering provision config by site_name: {0}".format(site_name_filter), "INFO")

                # Filter provision_wired_device - this does NOT affect device_configs
                provision_wired_devices = provision_config.get("provision_wired_device", [])
                filtered_provision_devices = [
                    device for device in provision_wired_devices
                    if device.get("site_name") == site_name_filter
                ]
                self.log("Provision devices before site_name filter: {0}, after filter: {1}".format(
                    len(provision_wired_devices), len(filtered_provision_devices)), "INFO")
                provision_config["provision_wired_device"] = filtered_provision_devices

        # device_configs remains unchanged - it's filtered independently by device_details criteria only
        self.log("Device configs (filtered by device_details only): {0}".format(len(device_configs)), "INFO")

        # Create the list of dictionaries to output (may be one, two, or three configs)
        dicts_to_write = []

        # Determine which components to include based on generate_all_configurations or components_list
        # Each component is independent - only include what user explicitly requested
        include_device_details = self.generate_all_configurations or "device_details" in components_list
        include_provision_device = self.generate_all_configurations or "provision_device" in components_list
        include_interface_details = self.generate_all_configurations or "interface_details" in components_list

        self.log("Component inclusion (independent) - device_details: {0}, provision_device: {1}, interface_details: {2}".format(
            include_device_details, include_provision_device, include_interface_details), "INFO")

        # First document: device details
        if include_device_details and device_configs:
            dicts_to_write.append({
                "_comment": "config for adding network devices:",
                "data": device_configs
            })
            self.log("Added device configs section with {0} configs".format(len(device_configs)), "DEBUG")

        # When device configs are available and interface_details is requested, auto-fetch interface details
        # For independent filtering, fetch from ALL devices respecting global filters
        auto_interface_configs = []
        if include_interface_details:
            self.log("Auto-generating interface details from devices (applying global filters)", "INFO")

            # Fetch devices respecting global filters for interface details
            if global_filters and any(global_filters.values()):
                # Apply same global filters as device_details
                self.log("Applying global filters to interface details fetch", "INFO")
                result = self.process_global_filters(global_filters)
                device_ip_to_id_mapping = result.get("device_ip_to_id_mapping", {})

                if device_ip_to_id_mapping:
                    all_devices_for_interfaces = list(device_ip_to_id_mapping.values())
                else:
                    all_devices_for_interfaces = self.fetch_all_devices(reason="fallback for interface filtering")
            else:
                # No global filters - fetch all devices
                all_devices_for_interfaces = self.fetch_all_devices(reason="no global filters for interface")

            if all_devices_for_interfaces:
                # Transform all devices to get IP addresses
                reverse_mapping_spec = self.inventory_get_device_reverse_mapping()
                all_transformed_for_interfaces = self.transform_device_to_playbook_format(
                    reverse_mapping_spec, all_devices_for_interfaces
                )
                # Extract interface_name filter if specified in component_specific_filters
                interface_name_filter = None
                if component_specific_filters and "interface_details" in component_specific_filters:
                    interface_details_filter = component_specific_filters.get("interface_details", {})
                    if isinstance(interface_details_filter, dict):
                        interface_name_filter = interface_details_filter.get("interface_name")
                        if interface_name_filter and not isinstance(interface_name_filter, list):
                            interface_name_filter = [interface_name_filter]

                auto_interface_configs = self.build_update_interface_details_from_all_devices(
                    all_transformed_for_interfaces,
                    interface_name_filter=interface_name_filter
                )
                if auto_interface_configs:
                    self.log("Generated {0} interface detail configs (with global filters)".format(
                        len(auto_interface_configs)
                    ), "INFO")
            else:
                self.log("No devices found for interface details generation", "WARNING")

        # Second document with provision_wired_device configuration
        second_doc_config = []

        if include_provision_device and provision_config:
            # Only add if there are actual devices in the provision config
            provision_devices = provision_config.get("provision_wired_device", [])
            if provision_devices:
                second_doc_config.append(provision_config)
                self.log("Added provision_wired_device config section with {0} devices".format(len(provision_devices)), "DEBUG")
            else:
                self.log("Skipping empty provision_wired_device config (no devices after filtering)", "DEBUG")

        if second_doc_config:
            dicts_to_write.append({
                "_comment": "config for provisioning wired device:",
                "data": second_doc_config
            })
            self.log("Added second document with {0} config sections".format(len(second_doc_config)), "DEBUG")

        # Third document with auto-generated interface details
        if include_interface_details and auto_interface_configs:
            dicts_to_write.append({
                "_comment": "config for updating interface details:",
                "data": auto_interface_configs
            })
            self.log("Added third document with {0} auto-generated interface configs".format(len(auto_interface_configs)), "DEBUG")

        # Fourth document with user-defined fields (independent component)
        include_user_defined_fields = self.generate_all_configurations or "user_defined_fields" in components_list
        user_defined_fields_config = []

        if include_user_defined_fields:
            self.log("Processing user_defined_fields component (independent of global filters)", "INFO")

            # Get UDF filters
            udf_filters = {
                "global_filters": {},  # UDFs cannot use global_filters (constraint already validated)
                "component_specific_filters": component_specific_filters.get("user_defined_fields", {}),
                "generate_all_configurations": self.generate_all_configurations
            }

            # Call get_user_defined_fields_details to fetch and transform UDFs
            network_element = module_supported_network_elements.get("user_defined_fields")
            if network_element:
                udf_details = self.get_user_defined_fields_details(network_element, udf_filters)
                if udf_details:
                    user_defined_fields_config = udf_details
                    self.log("Retrieved user_defined_fields config with {0} UDF entries".format(
                        len(udf_details[0].get("user_defined_fields", []))
                    ), "INFO")
                else:
                    self.log("No user_defined_fields data retrieved", "DEBUG")
            else:
                self.log("user_defined_fields network element not found in schema", "WARNING")

        if user_defined_fields_config:
            dicts_to_write.append({
                "_comment": "User defined fields:",
                "data": user_defined_fields_config
            })
            self.log("Added fourth document with user-defined fields config", "DEBUG")

        self.log("Final dictionaries created: {0} config sections".format(len(dicts_to_write)), "DEBUG")

        # Check if there's any data to write
        if not dicts_to_write:
            self.log("No data found to generate YAML configuration", "WARNING")
            self.msg = {
                "YAML config generation Task completed for module '{0}' - No data found.".format(
                    self.module_name
                ): {
                    "reason": "No devices matching the provided filters were found in Cisco Catalyst Center",
                    "file_path": file_path,
                    "status": "NO_DATA_TO_GENERATE"
                }
            }
            self.set_operation_result("success", False, self.msg, "WARNING")
            return self

        self.log("Writing final dictionaries to file: {0}".format(file_path), "INFO")
        write_result = self.write_dicts_to_yaml(dicts_to_write, file_path)
        if write_result:
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

    def write_dicts_to_yaml(self, dicts_list, file_path, dumper=None):
        """
        Writes multiple dictionaries as separate YAML documents to a file.
        Each dictionary becomes a separate YAML document separated by ---.
        Adds blank lines before top-level config items for better readability.
        Supports _comment key for adding comments before YAML sections.

        Args:
            dicts_list (list): List of dictionaries to write as separate YAML documents.
            file_path (str): The path where the YAML file will be written.
            dumper: The YAML dumper class to use for serialization (default is OrderedDumper).
        Returns:
            bool: True if the YAML file was successfully written, False otherwise.
        """
        if dumper is None:
            dumper = OrderedDumper

        if not isinstance(dicts_list, list):
            self.log("YAML write skipped: expected list input for document payload.", "ERROR")
            return False

        if not dicts_list:
            self.log("YAML write skipped: no document payload provided.", "WARNING")
            return False

        if not isinstance(file_path, str) or not file_path.strip():
            self.log("YAML write skipped: invalid file path provided.", "ERROR")
            return False

        self.log(
            "Preparing to write {0} YAML document(s) to {1}.".format(len(dicts_list), file_path),
            "INFO",
        )

        try:
            serialized_documents = []

            for index, section in enumerate(dicts_list, start=1):
                if not isinstance(section, dict):
                    self.log(
                        "Skipping non-dictionary YAML section at index {0}.".format(index),
                        "WARNING",
                    )
                    continue

                comment = section.get("_comment")
                if "data" in section:
                    payload = section.get("data")
                else:
                    payload = {k: v for k, v in section.items() if k != "_comment"}

                if payload is None:
                    payload = {}

                yaml_content = yaml.dump(
                    payload,
                    Dumper=dumper,
                    default_flow_style=False,
                    indent=2,
                    allow_unicode=True,
                    sort_keys=False,
                ).rstrip()

                if not yaml_content:
                    yaml_content = "{}"

                lines = yaml_content.split("\n")
                formatted_lines = []
                for line_index, line in enumerate(lines):
                    if (
                        line.startswith("- ")
                        and line_index > 0
                        and formatted_lines
                        and formatted_lines[-1].strip() != ""
                    ):
                        formatted_lines.append("")
                    formatted_lines.append(line)

                yaml_content = "\n".join(formatted_lines)

                if comment:
                    comment_line = str(comment).splitlines()[0].strip()
                    serialized_documents.append("# {0}\n{1}".format(comment_line, yaml_content))
                else:
                    serialized_documents.append(yaml_content)

            if not serialized_documents:
                self.log("YAML write skipped: no valid documents after normalization.", "WARNING")
                return False

            final_yaml = "---\n" + "\n---\n".join(serialized_documents) + "\n"

            self.ensure_directory_exists(file_path)
            with open(file_path, "w", encoding="utf-8") as yaml_file:
                yaml_file.write(final_yaml)

            self.log("YAML documents written successfully to {0}.".format(file_path), "INFO")
            return True

        except Exception as e:
            self.msg = "An error occurred while writing to {0}: {1}".format(
                file_path, str(e)
            )
            self.fail_and_exit(self.msg)

    def write_dict_to_yaml(self, data_dict, file_path, dumper=None):
        """
        Override: Converts a dictionary to YAML format and writes it to a specified file path.
        Adds blank lines before top-level config items (no indentation) for better readability.

        Args:
            data_dict (dict): The dictionary to convert to YAML format.
            file_path (str): The path where the YAML file will be written.
            dumper: The YAML dumper class to use for serialization (default is OrderedDumper).
        Returns:
            bool: True if the YAML file was successfully written, False otherwise.
        """
        if dumper is None:
            dumper = OrderedDumper

        self.log(
            "Starting to write dictionary to YAML file at: {0}".format(file_path),
            "DEBUG",
        )
        try:
            self.log("Starting conversion of dictionary to YAML format.", "INFO")
            yaml_content = yaml.dump(
                data_dict,
                Dumper=dumper,
                default_flow_style=False,
                indent=2,
                allow_unicode=True,
                sort_keys=False,
            )
            yaml_content = "---\n" + yaml_content

            # Post-process to add blank lines only before top-level list items (config items)
            # Top-level items have no indentation (start with - at column 0)
            lines = yaml_content.split('\n')
            result_lines = []

            for i, line in enumerate(lines):
                # Check if this line starts a top-level list item (no leading whitespace before -)
                if line.startswith('- ') and i > 0:
                    # Check if previous line is not blank and not the opening ---
                    if result_lines and result_lines[-1].strip() != '' and result_lines[-1] != '---':
                        # Add a blank line before this top-level list item
                        result_lines.append('')
                result_lines.append(line)

            yaml_content = '\n'.join(result_lines)
            self.log("Dictionary successfully converted to YAML format with blank lines before config items.", "DEBUG")

            # Ensure the directory exists
            self.ensure_directory_exists(file_path)

            self.log(
                "Preparing to write YAML content to file: {0}".format(file_path), "INFO"
            )
            with open(file_path, "w") as yaml_file:
                yaml_file.write(yaml_content)

            self.log(
                "Successfully written YAML content to {0}.".format(file_path), "INFO"
            )
            return True

        except Exception as e:
            self.msg = "An error occurred while writing to {0}: {1}".format(
                file_path, str(e)
            )
            self.fail_and_exit(self.msg)

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for brownfield Inventory workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.
        """

        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
        workflow_operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]
        operations_executed = 0
        operations_skipped = 0

        want_payload = self.want if isinstance(self.want, dict) else {}

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
            if param_key not in want_payload:
                operations_skipped += 1
                self.log(
                    "Skipping {0}: input section '{1}' not provided.".format(
                        operation_name, param_key
                    ),
                    "DEBUG",
                )
                continue

            params = want_payload.get(param_key)
            if params is None:
                operations_skipped += 1
                self.log(
                    "Skipping {0}: input section '{1}' is null.".format(
                        operation_name, param_key
                    ),
                    "WARNING",
                )
                continue

            try:
                self.log("Running {0} operation.".format(operation_name), "INFO")
                operation_result = operation_func(params)
                if hasattr(operation_result, "check_return_status"):
                    operation_result.check_return_status()
                operations_executed += 1
                self.log("{0} operation completed successfully.".format(operation_name), "INFO")
            except Exception as e:
                self.log(
                    "{0} operation failed: {1}".format(operation_name, str(e)),
                    "ERROR",
                )
                self.set_operation_result(
                    "failed",
                    False,
                    "{0} operation failed: {1}".format(operation_name, str(e)),
                    "ERROR",
                ).check_return_status()

        elapsed_time = time.time() - start_time
        self.log(
            "Gathered-state workflow completed in {0:.2f} seconds (executed={1}, skipped={2}).".format(
                elapsed_time, operations_executed, operations_skipped
            ),
            "INFO",
        )

        if operations_executed == 0 and operations_skipped > 0 and self.status != "failed":
            self.set_operation_result(
                "success",
                False,
                "No gathered-state operations were executed for the provided configuration.",
                "WARNING",
            )

        return self

    def transform_device_to_playbook_format(self, reverse_mapping_spec, device_response):
        """
        Transform raw device payload into playbook format and consolidate records
        with identical non-IP attributes.

        Args:
            reverse_mapping_spec (OrderedDict): Mapping specification for transformation
            device_response (list): List of raw device dictionaries from API

        Returns:
            list: List of consolidated device configurations with merged IP addresses
        """
        if not isinstance(reverse_mapping_spec, dict):
            self.log("Invalid reverse mapping specification. Expected dictionary input.", "ERROR")
            return []

        if device_response is None:
            self.log("No device data available for transformation.", "WARNING")
            return []

        if not isinstance(device_response, list):
            self.log("Invalid device response format. Expected list input.", "ERROR")
            return []

        if not device_response:
            self.log("Empty device list received for transformation.", "INFO")
            return []

        self.log(
            "Transforming {0} devices into consolidated playbook configurations.".format(
                len(device_response)
            ),
            "INFO",
        )

        def normalize_for_grouping(value):
            if isinstance(value, dict):
                return tuple(
                    (str(key), normalize_for_grouping(val))
                    for key, val in sorted(value.items(), key=lambda item: str(item[0]))
                )

            if isinstance(value, list):
                return tuple(normalize_for_grouping(item) for item in value)

            if isinstance(value, tuple):
                return tuple(normalize_for_grouping(item) for item in value)

            if isinstance(value, set):
                normalized_values = [normalize_for_grouping(item) for item in value]
                return tuple(sorted(normalized_values, key=lambda item: str(item)))

            return value

        optional_nested_keys = {
            "add_user_defined_field",
            "provision_wired_device",
            "update_interface_details",
        }

        transformed_devices = []
        total_devices = len(device_response)

        for index, device in enumerate(device_response, start=1):
            if not isinstance(device, dict):
                self.log(
                    "Skipping device record {0} because it is not a dictionary.".format(index),
                    "WARNING",
                )
                continue

            device_name = device.get("hostname") or device.get("managementIpAddress") or "Unknown"
            self.log(
                "Preparing playbook fields for device {0}/{1}: {2}".format(
                    index, total_devices, device_name
                ),
                "DEBUG",
            )

            device_config = {}
            for playbook_key, mapping_spec in reverse_mapping_spec.items():
                if not isinstance(mapping_spec, dict):
                    continue

                source_key = mapping_spec.get("source_key")
                transform_func = mapping_spec.get("transform")

                api_value = device.get(source_key) if source_key else None

                try:
                    transformed_value = (
                        transform_func(api_value) if callable(transform_func) else api_value
                    )
                except Exception as e:
                    self.log(
                        "Transformation failed for key '{0}' on device index {1}: {2}".format(
                            playbook_key, index, str(e)
                        ),
                        "ERROR",
                    )
                    transformed_value = None

                if playbook_key in (
                    "add_user_defined_field",
                    "provision_wired_device",
                    "update_interface_details",
                ):
                    if transformed_value in (None, [], {}):
                        continue

                device_config[playbook_key] = transformed_value

            transformed_devices.append(device_config)

        if not transformed_devices:
            self.log("No device records were transformed.", "WARNING")
            return []

        def to_immutable(value):
            if isinstance(value, dict):
                return tuple((k, to_immutable(v)) for k, v in sorted(value.items()))
            if isinstance(value, list):
                return tuple(to_immutable(v) for v in value)
            return value

        consolidated = {}
        for device_config in transformed_devices:
            non_ip_payload = {
                k: v for k, v in device_config.items() if k != "ip_address_list"
            }
            signature = to_immutable(non_ip_payload)

            if signature not in consolidated:
                consolidated[signature] = device_config.copy()
                if "ip_address_list" not in consolidated[signature]:
                    consolidated[signature]["ip_address_list"] = []

            current_ips = consolidated[signature].get("ip_address_list", [])
            incoming_ips = device_config.get("ip_address_list", [])

            if isinstance(incoming_ips, str):
                incoming_ips = [incoming_ips]
            elif not isinstance(incoming_ips, list):
                incoming_ips = []

            for ip in incoming_ips:
                if isinstance(ip, str):
                    ip = ip.strip()
                if ip and ip not in current_ips:
                    current_ips.append(ip)

            consolidated[signature]["ip_address_list"] = current_ips

        consolidated_list = list(consolidated.values())

        self.log(
            "Transformation completed. raw={0}, transformed={1}, consolidated={2}".format(
                len(device_response),
                len(transformed_devices),
                len(consolidated_list),
            ),
            "INFO",
        )
        return consolidated_list

    def apply_component_specific_filters(self, devices, component_filters):
        """
        Apply component-specific filters to device list after API retrieval.
        Handles filters that can be:
        - Single dict: {role: "ACCESS"}
        - List of single dict: [{role: "ACCESS"}]
        - List of multiple dicts: [{role: "ACCESS"}, {role: "CORE"}]

        Multiple filter dicts use OR logic (device matches ANY filter set).

        Args:
            devices (list): List of device dictionaries from API
            component_filters (dict or list): Filters like type, role, snmp_version, cli_transport
                                             Can be nested dict or list of filter dicts

        Returns:
            list: Filtered device list
        """
        if not isinstance(devices, list):
            self.log(
                "Cannot apply component filters because devices type is invalid: {0}".format(
                    type(devices).__name__
                ),
                "ERROR",
            )
            self.status = "failed"
            self.msg = "Device filter input is invalid."
            return None

        if not component_filters:
            return [d for d in devices if isinstance(d, dict)]

        if isinstance(component_filters, dict):
            filter_sets = [component_filters]
        elif isinstance(component_filters, list):
            filter_sets = [f for f in component_filters if isinstance(f, dict)]
        else:
            self.log(
                "Ignoring component filters because type is invalid: {0}".format(
                    type(component_filters).__name__
                ),
                "WARNING",
            )
            return [d for d in devices if isinstance(d, dict)]

        if not filter_sets:
            return [d for d in devices if isinstance(d, dict)]
        valid_types = {
            "NETWORK_DEVICE",
            "COMPUTE_DEVICE",
            "MERAKI_DASHBOARD",
            "THIRD_PARTY_DEVICE",
            "FIREPOWER_MANAGEMENT_SYSTEM",
        }
        valid_roles = {"ACCESS", "CORE", "DISTRIBUTION", "BORDER ROUTER", "UNKNOWN"}
        valid_snmp_versions = {"v2", "v2c", "v3"}
        valid_cli_transports = {"ssh", "telnet"}

        normalized_filters = []

        for index, raw_filter in enumerate(filter_sets, start=1):
            unknown_keys = set(raw_filter.keys()) - {
                "type",
                "role",
                "snmp_version",
                "cli_transport",
            }
            if unknown_keys:
                self.log(
                    "Ignoring unsupported keys in filter set {0}: {1}".format(
                        index, sorted(list(unknown_keys))
                    ),
                    "WARNING",
                )

            device_type = raw_filter.get("type")
            device_role = raw_filter.get("role")
            snmp_version = raw_filter.get("snmp_version")
            cli_transport = raw_filter.get("cli_transport")

            if device_type:
                if not isinstance(device_type, str):
                    self.status = "failed"
                    self.msg = "Filter 'type' must be a string."
                    return None
                device_type = device_type.strip().upper()
                if device_type not in valid_types:
                    self.status = "failed"
                    self.msg = "Invalid type '{0}' in component_specific_filters.".format(
                        raw_filter.get("type")
                    )
                    return None

            role_values = None
            if device_role is not None:
                if isinstance(device_role, str):
                    role_values = [device_role]
                elif isinstance(device_role, list):
                    role_values = device_role
                else:
                    self.status = "failed"
                    self.msg = "Filter 'role' must be a string or list."
                    return None

                normalized_roles = []
                for role in role_values:
                    if not isinstance(role, str):
                        self.status = "failed"
                        self.msg = "Role filter values must be strings."
                        return None
                    role_norm = role.strip().upper()
                    if role_norm not in valid_roles:
                        self.status = "failed"
                        self.msg = "Invalid role '{0}' in component_specific_filters.".format(role)
                        return None
                    normalized_roles.append(role_norm)
                role_values = normalized_roles

            if snmp_version:
                if not isinstance(snmp_version, str):
                    self.status = "failed"
                    self.msg = "Filter 'snmp_version' must be a string."
                    return None
                snmp_version = snmp_version.strip().lower()
                if snmp_version not in valid_snmp_versions:
                    self.status = "failed"
                    self.msg = "Invalid snmp_version '{0}' in component_specific_filters.".format(
                        raw_filter.get("snmp_version")
                    )
                    return None

            if cli_transport:
                if not isinstance(cli_transport, str):
                    self.status = "failed"
                    self.msg = "Filter 'cli_transport' must be a string."
                    return None
                cli_transport = cli_transport.strip().lower()
                if cli_transport not in valid_cli_transports:
                    self.status = "failed"
                    self.msg = "Invalid cli_transport '{0}' in component_specific_filters.".format(
                        raw_filter.get("cli_transport")
                    )
                    return None

            if any([device_type, role_values, snmp_version, cli_transport]):
                normalized_filters.append(
                    {
                        "type": device_type,
                        "role": role_values,
                        "snmp_version": snmp_version,
                        "cli_transport": cli_transport,
                    }
                )

        if not normalized_filters:
            return [d for d in devices if isinstance(d, dict)]

        matched_indexes = set()

        for device_index, device in enumerate(devices):
            if not isinstance(device, dict):
                continue

            device_type_value = (device.get("type") or "").strip().upper()
            device_role_value = (device.get("role") or "").strip().upper()
            device_snmp_value = (device.get("snmpVersion") or "").strip().lower()
            device_cli_value = (device.get("cliTransport") or "").strip().lower()

            normalized_device_snmp = device_snmp_value.replace("v2c", "v2")
            normalized_device_role = device_role_value if device_role_value else "UNKNOWN"

            for criteria in normalized_filters:
                if criteria["type"] and device_type_value != criteria["type"]:
                    continue

                if criteria["role"] and normalized_device_role not in criteria["role"]:
                    continue

                if criteria["snmp_version"]:
                    expected_snmp = criteria["snmp_version"].replace("v2c", "v2")
                    if normalized_device_snmp != expected_snmp:
                        continue

                if criteria["cli_transport"] and device_cli_value != criteria["cli_transport"]:
                    continue

                matched_indexes.add(device_index)
                break

        filtered_devices = [devices[i] for i in sorted(matched_indexes)]

        self.log(
            "Component filtering completed: matched={0}, total={1}, filter_sets={2}".format(
                len(filtered_devices), len(devices), len(normalized_filters)
            ),
            "INFO",
        )
        return filtered_devices


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
    ccc_inventory_playbook_generator = InventoryPlaybookGenerator(module)
    if (
        ccc_inventory_playbook_generator.compare_dnac_versions(
            ccc_inventory_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_inventory_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for INVENTORY Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_inventory_playbook_generator.get_ccc_version()
            )
        )
        ccc_inventory_playbook_generator.set_operation_result(
            "failed", False, ccc_inventory_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_inventory_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_inventory_playbook_generator.supported_states:
        ccc_inventory_playbook_generator.status = "invalid"
        ccc_inventory_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_inventory_playbook_generator.check_recturn_status()

    # Validate the input parameters and check the return statusk
    ccc_inventory_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_inventory_playbook_generator.validated_config:
        ccc_inventory_playbook_generator.reset_values()
        ccc_inventory_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_inventory_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_inventory_playbook_generator.result)


if __name__ == "__main__":
    main()

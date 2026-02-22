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
        try:
            self.log("Fetching site assignment for device: {0}".format(device_id), "DEBUG")
            response = self.dnac._exec(
                family="devices",
                function="get_assigned_site_for_device",
                params={"device_id": device_id},
                op_modifies=False
            )

            self.log("Site assignment response for device {0}: {1}".format(device_id, response), "INFO")

            if response and response.get("response"):
                site_info = response.get("response", {})
                site_name_path = site_info.get("groupNameHierarchy") or site_info.get("site")
                if site_name_path:
                    self.log("Device {0} assigned to site: {1}".format(device_id, site_name_path), "DEBUG")
                    return site_name_path
                else:
                    self.log("Device {0} has no site assignment".format(device_id), "DEBUG")
                    return ""
            else:
                self.log("No site info found for device: {0}".format(device_id), "DEBUG")
                return ""

        except Exception as e:
            self.log("Error fetching site for device {0}: {1}".format(device_id, str(e)), "WARNING")
            return ""

    def fetch_user_defined_fields(self, udf_filter=None):
        """
        Fetch user-defined fields from Cisco Catalyst Center API.

        Args:
            udf_filter (str or list): Optional filter by UDF name(s)

        Returns:
            list: List of user-defined field dictionaries with name, description, and value fields
        """
        self.log("Fetching user-defined fields{0}".format(
            " with filter: {0}".format(udf_filter) if udf_filter else ""
        ), "INFO")

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_all_user_defined_fields",
                op_modifies=False,
                params={}
            )

            if response and "response" in response:
                udfs = response.get("response", [])
                self.log("Retrieved {0} user-defined fields from API".format(len(udfs)), "INFO")

                # Transform UDF response: keep only name and description, add value: null
                transformed_udfs = []
                for udf in udfs:
                    transformed_udf = {
                        "name": udf.get("name", ""),
                        "description": udf.get("description", ""),
                        "value": None
                    }
                    transformed_udfs.append(transformed_udf)

                # Apply filter if provided
                if udf_filter:
                    filter_list = udf_filter if isinstance(udf_filter, list) else [udf_filter]
                    filtered_udfs = [udf for udf in transformed_udfs if udf.get("name") in filter_list]
                    self.log("Filtered to {0} user-defined fields matching names: {1}".format(
                        len(filtered_udfs), filter_list
                    ), "INFO")
                    return filtered_udfs
                else:
                    return transformed_udfs

            else:
                self.log("No user-defined fields returned from API", "WARNING")
                return []

        except Exception as e:
            self.log("Error fetching user-defined fields: {0}".format(str(e)), "ERROR")
            return []

    def inventory_get_user_defined_fields_reverse_mapping(self):
        """
        Returns reverse mapping specification for user-defined fields.
        Transforms API response from Catalyst Center to inventory_workflow_manager format.
        Maps UDF attributes from API response to playbook configuration structure.
        """
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
            component_specific_filters = filters.get("component_specific_filters", {})
            udf_name_filter = component_specific_filters.get("udf_name")

            self.log("UDF component-specific filters: {0}".format(component_specific_filters), "DEBUG")

            # Fetch user-defined fields from API with optional filter
            udf_response = self.fetch_user_defined_fields(udf_filter=udf_name_filter)

            self.log("Retrieved {0} user-defined fields".format(len(udf_response)), "INFO")

            if not udf_response:
                self.log("No user-defined fields found", "WARNING")
                return []

            # Build the UDF configuration dictionary
            udf_config = {
                "user_defined_fields": udf_response
            }

            # Return as a list containing the configuration
            self.log("Built user_defined_fields config with {0} UDFs".format(len(udf_response)), "INFO")
            return [udf_config]

        except Exception as e:
            self.log("Error in get_user_defined_fields_details: {0}".format(str(e)), "ERROR")
            import traceback
            self.log("Traceback: {0}".format(traceback.format_exc()), "DEBUG")
            return []

    def build_provision_wired_device_config(self, device_list):
        """
        Build provision_wired_device configuration from device list.

        Args:
            device_list (list): List of device dictionaries from API

        Returns:
            list: List of provision_wired_device configuration dictionaries
        """
        self.log("Building provision_wired_device config for {0} devices".format(len(device_list)), "INFO")

        provision_devices = []

        for device in device_list:
            try:
                device_ip = device.get("managementIpAddress") or device.get("ipAddress")
                device_id = device.get("id") or device.get("instanceUuid")
                device_hostname = device.get("hostname", "Unknown")

                if not device_ip:
                    self.log("Skipping device {0}: no management IP".format(device_hostname), "DEBUG")
                    continue

                # Fetch site assignment for this device
                site_name = self.fetch_device_site_mapping(device_id)

                # If no site assigned, use placeholder
                if not site_name:
                    site_name = "Global/{{ site_name }}"
                    self.log("Device {0}: using placeholder for site_name".format(device_ip), "DEBUG")

                # Build provision device entry
                provision_entry = {
                    "device_ip": device_ip,
                    "site_name": site_name,
                    "resync_retry_count": 200,
                    "resync_retry_interval": 2
                }

                provision_devices.append(provision_entry)
                self.log("Added provision config for device {0} ({1})".format(device_ip, device_hostname), "DEBUG")

            except Exception as e:
                self.log("Error building provision config for device: {0}".format(str(e)), "ERROR")
                continue

        self.log("Built provision_wired_device configs: {0} devices".format(len(provision_devices)), "INFO")
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
        try:
            self.log("Fetching SDA provision status for device IP: {0}".format(device_ip), "DEBUG")
            response = self.dnac._exec(
                family="sda",
                function="get_provisioned_wired_device",
                params={
                    "device_management_ip_address": device_ip
                }
            )

            self.log("SDA provision response for {0}: {1}".format(device_ip, response), "DEBUG")

            if response and isinstance(response, dict):
                status = response.get("status", "").lower()

                # Check if device is provisioned (success status)
                if status == "success":
                    self.log("Device {0} is provisioned to site".format(device_ip), "INFO")
                    return response
                else:
                    # Device not provisioned
                    description = response.get("description", "")
                    self.log("Device {0} not provisioned: {1}".format(device_ip, description), "INFO")
                    return None
            else:
                self.log("Invalid response for device {0}".format(device_ip), "WARNING")
                return None

        except Exception as e:
            self.log("Error fetching SDA provision status for device {0}: {1}".format(device_ip, str(e)), "DEBUG")
            return None

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
        self.log("Building provision_wired_device config from SDA provision-device endpoint", "INFO")

        # Collect all filtered device IPs from device_configs
        filtered_device_ips = []
        for config in device_configs:
            if isinstance(config, dict) and "ip_address_list" in config:
                ip_list = config.get("ip_address_list", [])
                if isinstance(ip_list, list):
                    filtered_device_ips.extend(ip_list)

        self.log("Checking provisioning status for {0} device IPs".format(len(filtered_device_ips)), "INFO")

        provision_devices = []

        for device_ip in filtered_device_ips:
            try:
                # Query SDA provision-device endpoint for this device
                provision_response = self.fetch_sda_provision_device(device_ip)

                if provision_response:
                    # Device is provisioned - extract information
                    device_mgmt_ip = provision_response.get("deviceManagementIpAddress")
                    site_name_hierarchy = provision_response.get("siteNameHierarchy")
                    status = provision_response.get("status")
                    description = provision_response.get("description")

                    # Build provision device entry from SDA response
                    provision_entry = {
                        "device_ip": device_mgmt_ip,
                        "site_name": site_name_hierarchy,
                        "resync_retry_count": 200,
                        "resync_retry_interval": 2
                    }

                    provision_devices.append(provision_entry)
                    self.log("Added provision config from SDA endpoint - IP: {0}, Site: {1}, Status: {2}".format(
                        device_mgmt_ip, site_name_hierarchy, status
                    ), "DEBUG")
                else:
                    # Device not provisioned - skip it
                    self.log("Skipping device {0}: not provisioned or error occurred".format(device_ip), "INFO")
                    continue

            except Exception as e:
                self.log("Error processing device {0} for provisioning config: {1}".format(device_ip, str(e)), "ERROR")
                continue

        if provision_devices:
            provision_config = {
                "provision_wired_device": provision_devices
            }
            self.log("Built provision config with {0} provisioned devices from SDA endpoint".format(
                len(provision_devices)
            ), "INFO")
            return provision_config
        else:
            self.log("No provisioned devices found via SDA endpoint", "WARNING")
            return {}

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
        self.log("Building update_interface_details configs from all devices", "INFO")

        try:
            if not device_configs:
                self.log("No device configs provided", "WARNING")
                return []

            # Collect all IPs from device configs
            all_device_ips = []
            for config in device_configs:
                if isinstance(config, dict) and "ip_address_list" in config:
                    ip_list = config.get("ip_address_list", [])
                    if isinstance(ip_list, list):
                        all_device_ips.extend(ip_list)

            self.log("Collected {0} device IPs for interface detail fetching".format(len(all_device_ips)), "INFO")

            if not all_device_ips:
                return []

            # Fetch interface details for all devices and group by configuration
            interface_configs_by_hash = {}  # Group configs by their hash for consolidation

            for device_ip in all_device_ips:
                try:
                    self.log("Fetching interface details for device {0} using get_interface_by_ip".format(device_ip), "DEBUG")

                    # Call get_interface_by_ip endpoint - returns all interfaces for the device IP
                    # API: /dna/intent/api/v1/interface/ip-address/{ipAddress}
                    interface_response = self.dnac._exec(
                        family="devices",
                        function="get_interface_by_ip",
                        params={"ip_address": device_ip}
                    )

                    if interface_response and isinstance(interface_response, dict):
                        interfaces = interface_response.get("response", [])
                        if not isinstance(interfaces, list):
                            interfaces = [interfaces]

                        self.log("Found {0} interfaces for device {1}".format(len(interfaces), device_ip), "DEBUG")

                        if interfaces:
                            # Process each interface and create configs
                            for interface in interfaces:
                                if not isinstance(interface, dict):
                                    continue

                                # Map API response fields to our config format
                                # Field mapping from API response schema:
                                # name -> interface_name
                                # description -> description
                                # adminStatus -> admin_status
                                # vlanId -> vlan_id
                                # voiceVlan -> voice_vlan_id
                                interface_name = interface.get("name") or interface.get("portName") or ""
                                interface_description = interface.get("description") or ""
                                admin_status = interface.get("adminStatus") or ""
                                vlan_id = interface.get("vlanId") or interface.get("nativeVlanId")
                                voice_vlan_id = interface.get("voiceVlan")

                                if not interface_name:
                                    continue

                                # Apply interface_name filter if specified
                                if interface_name_filter and interface_name not in interface_name_filter:
                                    self.log("Skipping interface {0} on device {1}: not in filter list {2}".format(
                                        interface_name, device_ip, interface_name_filter
                                    ), "DEBUG")
                                    continue

                                # Build interface config with all required fields
                                interface_config = {
                                    "description": interface_description,
                                    "admin_status": admin_status,
                                    "vlan_id": vlan_id,
                                    "voice_vlan_id": voice_vlan_id,
                                    "interface_name": [interface_name],
                                    "deployment_mode": "Deploy",
                                    "clear_mac_address_table": False
                                }

                                # Keep all fields including null/empty values as requested
                                # Create a hash of the config to group similar configs
                                config_hash = str(sorted(interface_config.items()))

                                if config_hash not in interface_configs_by_hash:
                                    interface_configs_by_hash[config_hash] = {
                                        "ip_address_list": [],
                                        "update_interface_details": interface_config
                                    }

                                # Add device IP to this config group if not already present
                                if device_ip not in interface_configs_by_hash[config_hash]["ip_address_list"]:
                                    interface_configs_by_hash[config_hash]["ip_address_list"].append(device_ip)

                                self.log("Processed interface {0} for device {1}".format(
                                    interface_name, device_ip
                                ), "DEBUG")
                        else:
                            # If no interfaces found, skip this device
                            self.log("No interfaces found for device {0}, skipping".format(device_ip), "DEBUG")

                except Exception as e:
                    self.log("Error fetching interface details for device {0}: {1}".format(device_ip, str(e)), "DEBUG")
                    # Skip device on error
                    self.log("Skipping device {0} due to error".format(device_ip), "WARNING")
                    continue

            # Convert grouped configs to list
            update_interface_configs = list(interface_configs_by_hash.values())

            self.log("Created {0} update_interface_details config sections from all devices".format(
                len(update_interface_configs)
            ), "INFO")

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
            return api_value
        return [api_value]

    def get_device_details_details(self, network_element, filters):
        """
        Retrieves inventory device credentials from Cisco Catalyst Center API.
        Processes the response and transforms it using the reverse mapping specification.
        Captures FULL device response with all available fields.
        """
        self.log("Starting get_device_details_details", "INFO")

        try:
            reverse_mapping_spec = self.inventory_get_device_reverse_mapping()

            global_filters = filters.get("global_filters", {})
            component_specific_filters = filters.get("component_specific_filters", {})
            generate_all = filters.get("generate_all_configurations", False)

            self.log("Filters received - Global: {0}, Component: {1}, Generate All: {2}".format(
                global_filters, component_specific_filters, generate_all
            ), "DEBUG")

            device_response = []

            # Step 1: Get devices from API with FULL details
            if generate_all:
                devices = self.fetch_all_devices(reason="generate_all_configurations enabled")
                device_response.extend(devices)

            else:
                self.log("Processing global filters", "INFO")
                result = self.process_global_filters(global_filters)
                device_ip_to_id_mapping = result.get("device_ip_to_id_mapping", {})

                if device_ip_to_id_mapping:
                    self.log("Retrieved {0} devices from global filters".format(len(device_ip_to_id_mapping)), "INFO")

                    # Log the first device to see what fields are available
                    first_device = list(device_ip_to_id_mapping.values())[0] if device_ip_to_id_mapping else None
                    if first_device:
                        self.log("Sample filtered device fields: {0}".format(list(first_device.keys())), "INFO")
                        self.log("Sample filtered device data: {0}".format(first_device), "DEBUG")

                    for device_ip, device_info in device_ip_to_id_mapping.items():
                        device_response.append(device_info)

                else:
                    # Fallback: fetch all devices when no global filters provided
                    devices = self.fetch_all_devices(reason="no global filters provided")
                    device_response.extend(devices)

            self.log("Retrieved {0} devices before component filtering".format(len(device_response)), "INFO")

            # ✅ Log what fields are actually available in the device_response
            if device_response:
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

                # Step 2: Apply component-specific filters (type, role, snmp_version, cli_transport)
                if component_specific_filters:
                    self.log("Applying component-specific filters: {0}".format(component_specific_filters), "DEBUG")
                    device_response = self.apply_component_specific_filters(device_response, component_specific_filters)

                    # Check if filtering failed (returns None on validation error)
                    if device_response is None:
                        self.log("Component filter validation failed", "ERROR")
                        return []

                    self.log("After component filtering: {0} devices remain".format(len(device_response)), "INFO")
                else:
                    self.log("No component-specific filters to apply", "DEBUG")

                if not device_response:
                    self.log("No devices found matching all filters", "WARNING")
                    return []

                # Step 3: Transform devices to playbook format
                self.log("Transforming {0} devices to playbook format".format(len(device_response)), "INFO")
                transformed_devices = self.transform_device_to_playbook_format(
                    reverse_mapping_spec, device_response
                )

                self.log("Devices transformed successfully: {0} configurations".format(len(transformed_devices)), "INFO")

                # Step 4: Add separate provision_wired_device config from SDA endpoint
                # Build provision config applying global filters (but independent of device_details component filters)
                self.log("Building separate provision_wired_device config from SDA endpoint (applying global filters)", "INFO")

                # Fetch devices respecting global filters for provision config
                if global_filters and any(global_filters.values()):
                    # Apply same global filters as device_details
                    self.log("Applying global filters to provision device fetch", "INFO")
                    result = self.process_global_filters(global_filters)
                    device_ip_to_id_mapping = result.get("device_ip_to_id_mapping", {})

                    if device_ip_to_id_mapping:
                        all_devices_for_provision = list(device_ip_to_id_mapping.values())
                    else:
                        all_devices_for_provision = self.fetch_all_devices(reason="fallback for provision filtering")
                else:
                    # No global filters - fetch all devices
                    all_devices_for_provision = self.fetch_all_devices(reason="no global filters for provision")

                if all_devices_for_provision:
                    # Transform all devices for provision config
                    all_transformed_devices = self.transform_device_to_playbook_format(
                        reverse_mapping_spec, all_devices_for_provision
                    )
                    license_provision_config = self.build_provision_wired_device_from_sda_endpoint(all_transformed_devices)
                else:
                    license_provision_config = None

                if license_provision_config and "provision_wired_device" in license_provision_config:
                    # Add provision config as a separate entry below the device configs
                    transformed_devices.append(license_provision_config)
                    self.log("Added separate provision_wired_device config to output (built with global filters)", "INFO")
                else:
                    self.log("No provisioned devices found from SDA endpoint", "DEBUG")

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

        # Check if generate_all_configurations mode is enabled and store as instance attribute
        # THIS MUST BE DONE FIRST before creating filters
        self.generate_all_configurations = yaml_config_generator.get("generate_all_configurations", False)
        if self.generate_all_configurations:
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
        if self.generate_all_configurations:
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

        self.log(
            "Global filters determined: {0}".format(global_filters),
            "DEBUG",
        )
        self.log(
            "Component-specific filters determined: {0}".format(
                component_specific_filters
            ),
            "DEBUG",
        )

        # First, extract components_list to check if user_defined_fields is requested
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        components_list = component_specific_filters.get(
            "components_list", module_supported_network_elements.keys()
        )

        # Convert to list if needed
        components_list = list(components_list) if not isinstance(components_list, list) else components_list

        # Validate user_defined_fields constraint: cannot be used with global_filters
        has_user_defined_fields = "user_defined_fields" in components_list
        has_global_filters = any(global_filters.values())

        if has_user_defined_fields and has_global_filters:
            self.log(
                "ERROR: user_defined_fields component cannot be used together with global_filters",
                "ERROR"
            )
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {
                    "reason": "user_defined_fields component cannot be used together with global_filters "
                              "(mutually exclusive - global filters are IP-based device filtering)",
                    "status": "INVALID_FILTER_COMBINATION"
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
        has_filter_only = any(
            module_supported_network_elements.get(c, {}).get("is_filter_only", False)
            for c in components_list
        )

        if has_filter_only and "device_details" not in components_to_fetch:
            self.log("Adding device_details to fetch list (required by filter-only components)", "DEBUG")
            components_to_fetch = ["device_details"] + components_to_fetch

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

            # Create filters dictionary properly with both global and component-specific filters
            # Include generate_all_configurations flag in the filters
            filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters.get(component, {}),
                "generate_all_configurations": self.generate_all_configurations
            }

            self.log("Processing component {0} with filters: {1}".format(component, filters), "DEBUG")

            operation_func = network_element.get("get_function_name")
            if callable(operation_func):
                details = operation_func(network_element, filters)
                self.log(
                    "Details retrieved for {0}: {1}".format(component, details), "DEBUG"
                )

                # Check if operation failed (validation error occurred)
                if self.status == "failed":
                    self.log("Component processing failed due to validation error", "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Details is already a list with one consolidated config dict
                # Extend instead of append to flatten the structure
                if details:
                    final_list.extend(details)

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

        self.log(
            "Starting to write {0} dictionaries to YAML file at: {1}".format(len(dicts_list), file_path),
            "DEBUG",
        )
        try:
            self.log("Starting conversion of dictionaries to YAML format.", "INFO")

            all_yaml_content = "---\n"

            for idx, data_dict in enumerate(dicts_list):
                # Extract and remove comment if present
                comment = None
                actual_data = data_dict

                if "_comment" in data_dict:
                    comment = data_dict["_comment"]
                    # If using _comment + data structure, extract the data
                    if "data" in data_dict:
                        actual_data = data_dict["data"]
                    else:
                        # Remove _comment from dict
                        actual_data = {k: v for k, v in data_dict.items() if k != "_comment"}

                # Add comment as YAML comment before the section
                if comment:
                    all_yaml_content += "# {0}\n".format(comment)

                yaml_content = yaml.dump(
                    actual_data,
                    Dumper=dumper,
                    default_flow_style=False,
                    indent=2,
                    allow_unicode=True,
                    sort_keys=False,
                )

                # Post-process to add blank lines only before top-level list items (config items)
                lines = yaml_content.split('\n')
                result_lines = []

                for i, line in enumerate(lines):
                    # Check if this line starts a top-level list item (no leading whitespace before -)
                    if line.startswith('- ') and i > 0:
                        # Check if previous line is not blank
                        if result_lines and result_lines[-1].strip() != '':
                            # Add a blank line before this top-level list item
                            result_lines.append('')
                    result_lines.append(line)

                yaml_content = '\n'.join(result_lines)
                all_yaml_content += yaml_content

                # Add document separator before next document (if not the last one)
                if idx < len(dicts_list) - 1:
                    all_yaml_content += "\n---\n"

            self.log("Dictionaries successfully converted to YAML format.", "DEBUG")

            # Ensure the directory exists
            self.ensure_directory_exists(file_path)

            self.log(
                "Preparing to write YAML content to file: {0}".format(file_path), "INFO"
            )
            with open(file_path, "w") as yaml_file:
                yaml_file.write(all_yaml_content)

            self.log(
                "Successfully written {0} YAML documents to {1}.".format(len(dicts_list), file_path), "INFO"
            )
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

    def transform_device_to_playbook_format(self, reverse_mapping_spec, device_response):
        """
        Transforms raw device data from Catalyst Center to playbook format using reverse mapping spec.
        Consolidates devices with matching attributes into single config blocks with merged IP addresses.

        Args:
            reverse_mapping_spec (OrderedDict): Mapping specification for transformation
            device_response (list): List of raw device dictionaries from API

        Returns:
            list: List of consolidated device configurations with merged IP addresses
        """

        # Input validation
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

        # First pass: Transform each device to playbook format
        transformed_devices = []
        optional_nested_keys = ["add_user_defined_field", "provision_wired_device", "update_interface_details"]
        
        for device_index, device in enumerate(device_response, start=1):
            if not isinstance(device, dict):
                self.log(
                    "Skipping invalid device payload at index {0}. Expected dictionary.".format(index),
                    "WARNING",
                )
                continue
            device_name = device.get("hostname") or device.get("managementIpAddress") or "Unknown"
            self.log(
                "Preparing playbook fields for device {0}/{1}: {2}".format(
                    device_index, len(device_response), device_name
                ),
                "DEBUG",
            )

            device_config = {}

            for playbook_key, mapping_spec in reverse_mapping_spec.items():
                if not isinstance(mapping_spec, dict):
                    self.log(
                        "Skipping key '{0}' due to invalid mapping specification.".format(playbook_key),
                        "WARNING",
                    )
                    continue

                source_key = mapping_spec.get("source_key")
                transform_func = mapping_spec.get("transform")

                try:
                    api_value = device.get(source_key) if source_key else None
                    transformed_value = transform_func(api_value) if callable(transform_func) else api_value
                except Exception as e:
                    self.log(
                        "Failed to transform key '{0}' for device '{1}': {2}".format(
                            playbook_key, device_name, str(e)
                        ),
                        "ERROR",
                    )
                    transformed_value = None

                if playbook_key in optional_nested_keys and transformed_value in (None, [], {}):
                    continue

                device_config[playbook_key] = transformed_value

            # Ensure ip_address_list is present with fallback values
            if "ip_address_list" not in device_config:
                fallback_ip = device.get("managementIpAddress") or device.get("ipAddress")
                device_config["ip_address_list"] = [fallback_ip] if fallback_ip else []

            transformed_devices.append(device_config)

            self.log("Device {0} ({1}) transformation complete".format(
                device_index + 1, device_name
            ), "INFO")

        if not transformed_devices:
            self.log("No valid devices were transformed into playbook format.", "WARNING")
            return []    

        # Second pass: Consolidate devices with matching attributes
        self.log("Starting consolidation of {0} transformed devices".format(len(transformed_devices)), "INFO")

        # Create a dictionary to group devices by their non-ip_address attributes
        consolidated_configs = {}

        for device_config in transformed_devices:
            # Create a key from all attributes except ip_address_list
            config_key_parts = []
            for key in sorted(device_config.keys()):
                if key != 'ip_address_list':
                    # Convert value to string for key creation
                    value = device_config[key]
                    config_key_parts.append("{0}={1}".format(key, str(value)))

            config_key = "|".join(config_key_parts)

            # If this config key doesn't exist, create it
            if config_key not in consolidated_configs:
                consolidated_configs[config_key] = device_config.copy()
                # Initialize ip_address_list as empty if not present
                if 'ip_address_list' not in consolidated_configs[config_key]:
                    consolidated_configs[config_key]['ip_address_list'] = []

            # Merge IP addresses
            current_ips = consolidated_configs[config_key].get('ip_address_list', [])
            device_ips = device_config.get('ip_address_list', [])

            if isinstance(device_ips, list):
                for ip in device_ips:
                    if ip and ip not in current_ips:
                        current_ips.append(ip)
            elif device_ips:
                if device_ips not in current_ips:
                    current_ips.append(device_ips)

            consolidated_configs[config_key]['ip_address_list'] = current_ips

        # Convert back to list format
        consolidated_list = list(consolidated_configs.values())

        self.log("Consolidation complete. Created {0} consolidated configurations from {1} devices".format(
            len(consolidated_list), len(transformed_devices)
        ), "INFO")

        for idx, config in enumerate(consolidated_list):
            ip_count = len(config.get('ip_address_list', []))
            self.log("Consolidated config {0}: {1} IP addresses, {2} attributes".format(
                idx + 1, ip_count, len(config)
            ), "INFO")

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
        if not component_filters:
            self.log("No component filters provided, returning all devices", "INFO")
            return devices

        self.log("Component filters received: {0}".format(component_filters), "DEBUG")

        # Normalize component_filters to a list of filter dicts
        filter_list = []

        if isinstance(component_filters, list):
            # Already a list
            filter_list = component_filters
            self.log("Component filters is a list with {0} filter set(s)".format(len(filter_list)), "DEBUG")
        elif isinstance(component_filters, dict):
            # Convert single dict to list
            filter_list = [component_filters]
            self.log("Component filters is a dict, converted to list with 1 filter set", "DEBUG")
        else:
            self.log("Component filters is not dict or list, returning all devices", "WARNING")
            return devices

        if not filter_list:
            self.log("Component filters list is empty, returning all devices", "INFO")
            return devices

        # Validate and clean filter list
        valid_filters = []
        for idx, filter_item in enumerate(filter_list):
            if isinstance(filter_item, dict):
                valid_filters.append(filter_item)
            else:
                self.log("Filter item {0} is not a dict, skipping: {1}".format(idx, filter_item), "WARNING")

        if not valid_filters:
            self.log("No valid filter dicts found, returning all devices", "WARNING")
            return devices

        self.log("Processing {0} filter set(s) with OR logic".format(len(valid_filters)), "INFO")

        filtered_devices = []
        devices_matched_filters = set()  # Track which devices matched any filter

        # Process each filter set (OR logic - device matches ANY filter set)
        for filter_idx, filter_criteria in enumerate(valid_filters):
            self.log("Processing filter set {0}/{1}: {2}".format(
                filter_idx + 1, len(valid_filters), filter_criteria
            ), "INFO")

            # Extract filter criteria from this filter set
            device_type = filter_criteria.get("type")
            device_role = filter_criteria.get("role")
            snmp_version = filter_criteria.get("snmp_version")
            cli_transport = filter_criteria.get("cli_transport")

            self.log("Filter set {0} - type: {1}, role: {2}, snmp: {3}, cli: {4}".format(
                filter_idx + 1, device_type, device_role, snmp_version, cli_transport
            ), "DEBUG")

            # Validate role filter if provided
            if device_role:
                valid_roles = ["ACCESS", "CORE", "DISTRIBUTION", "BORDER ROUTER", "UNKNOWN"]
                role_filter_list = device_role if isinstance(device_role, list) else [device_role]

                for role_value in role_filter_list:
                    if role_value.upper() not in [r.upper() for r in valid_roles]:
                        error_msg = "Invalid role '{0}' in component_specific_filters. Valid roles are: {1}".format(
                            role_value, ", ".join(valid_roles)
                        )
                        self.log(error_msg, "ERROR")
                        self.msg = error_msg
                        self.status = "failed"
                        return None

            # If no actual filter values provided in this set, skip it
            if not any([device_type, device_role, snmp_version, cli_transport]):
                self.log("Filter set {0} has no filter values, skipping".format(filter_idx + 1), "DEBUG")
                continue

            # Check each device against THIS filter set
            for device in devices:
                # Skip if device already matched a previous filter set
                device_id = device.get("id", device.get("instanceUuid", ""))
                if device_id in devices_matched_filters:
                    continue

                device_hostname = device.get("hostname", "Unknown")
                device_matched = True

                # Check device type (AND logic within filter set)
                if device_type:
                    device_type_value = device.get("type")
                    if not device_type_value or device_type_value.upper() != device_type.upper():
                        self.log("Device {0}: type MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, device_type, device_type_value
                        ), "DEBUG")
                        device_matched = False
                    else:
                        self.log("Device {0}: type MATCH ({1})".format(device_hostname, device_type_value), "DEBUG")

                # Check device role (AND logic within filter set)
                if device_role and device_matched:
                    device_role_value = device.get("role")

                    self.log("Device {0}: role check - Filter: '{1}', Device: '{2}'".format(
                        device_hostname, device_role, device_role_value
                    ), "DEBUG")

                    # Normalize device_role to a list for uniform comparison
                    role_filter_list = device_role if isinstance(device_role, list) else [device_role]

                    # Handle None or empty role
                    if not device_role_value or device_role_value == "":
                        # Check if any filter role is UNKNOWN or empty
                        if any(r.upper() in ["UNKNOWN", ""] for r in role_filter_list):
                            self.log("Device {0}: role MATCH - both are UNKNOWN/empty".format(device_hostname), "DEBUG")
                        else:
                            self.log("Device {0}: role MISMATCH - device role is None/empty (filter: {1})".format(
                                device_hostname, role_filter_list
                            ), "DEBUG")
                            device_matched = False
                    # Compare roles (case-insensitive) - check if device role matches ANY in the filter list
                    # Note: Role values are already validated to be in the allowed choices
                    elif any(device_role_value.upper() == r.upper() for r in role_filter_list):
                        self.log("Device {0}: role MATCH ({1}) - matches one of {2}".format(
                            device_hostname, device_role_value, role_filter_list
                        ), "DEBUG")
                    else:
                        self.log("Device {0}: role MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, role_filter_list, device_role_value
                        ), "DEBUG")
                        device_matched = False

                # Check SNMP version (AND logic within filter set)
                if snmp_version and device_matched:
                    device_snmp = device.get("snmpVersion", "")
                    normalized_filter = snmp_version.lower().replace("v2c", "v2")
                    normalized_device = device_snmp.lower().replace("v2c", "v2")

                    if normalized_device == normalized_filter:
                        self.log("Device {0}: SNMP MATCH ({1})".format(device_hostname, device_snmp), "DEBUG")
                    else:
                        self.log("Device {0}: SNMP MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, snmp_version, device_snmp
                        ), "DEBUG")
                        device_matched = False

                # Check CLI transport (AND logic within filter set)
                if cli_transport and device_matched:
                    device_cli = device.get("cliTransport", "")
                    if device_cli.lower() == cli_transport.lower():
                        self.log("Device {0}: CLI transport MATCH ({1})".format(device_hostname, device_cli), "DEBUG")
                    else:
                        self.log("Device {0}: CLI transport MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, cli_transport, device_cli
                        ), "DEBUG")
                        device_matched = False

                # If device passed ALL criteria in THIS filter set, mark it as matched
                if device_matched:
                    devices_matched_filters.add(device_id)
                    self.log("Device {0} PASSED filter set {1} criteria".format(
                        device_hostname, filter_idx + 1
                    ), "DEBUG")

        # Collect all devices that matched ANY filter set
        for device in devices:
            device_id = device.get("id", device.get("instanceUuid", ""))
            if device_id in devices_matched_filters:
                filtered_devices.append(device)
                self.log("Device {0} INCLUDED in result (matched a filter set)".format(
                    device.get("hostname", "Unknown")
                ), "INFO")

        self.log("Filtering complete: {0} devices matched from {1} total across {2} filter set(s)".format(
            len(filtered_devices), len(devices), len(valid_filters)
        ), "INFO")

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

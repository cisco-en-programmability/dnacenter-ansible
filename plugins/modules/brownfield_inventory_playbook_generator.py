#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wired Campus Automation Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Mridul Saurabh, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_inventory_playbook_generator
short_description: Generate YAML configurations playbook for 'inventory_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'inventory_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the network device inventory configurations
  such as device credentials, management IP addresses, device types, and other device-specific
  attributes configured on the Cisco Catalyst Center.
- Automatically generates provision_wired_device configurations by mapping devices to their assigned sites.
- Devices with type 'NETWORK_DEVICE' are automatically excluded from all generated configurations.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Mridul Saurabh (@msaurabh)
- Madhan Sankaranarayanan (@madhansansel)
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
          - Note - Devices with type 'NETWORK_DEVICE' are excluded from output.
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
            choices: ["device_details", "provision_device", "interface_details"]
          device_details:
            description:
            - Specific filters for device_details component.
            - These filters apply after global filters to further refine device selection.
            - Supports both single filter dict and list of filter dicts with OR logic.
            type: dict
            suboptions:
              role:
                description:
                - Filter devices by network role.
                - Can be a single role string or a list of roles (matches any in the list).
                - Valid values are ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN.
                - Examples: role="ACCESS" or role=["ACCESS", "CORE"]
                type: [str, list]
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
                - Filter provision devices by site name.
                - Example: "Global/India/Telangana/Hyderabad/BLD_1"
                type: str
      update_interface_details:
        description:
        - Configuration for updating interface details on devices.
        - When provided, the module will fetch actual interface details from the specified devices
          and generate update_interface_details configuration.
        - Uses the API analysis to retrieve device IDs and interface information.
        - Optional - only include if you want to generate interface update configurations.
        type: dict
        suboptions:
          device_ips:
            description:
            - List of device management IP addresses for which to fetch and configure interface details.
            - The module will lookup device IDs for these IPs and fetch interface information.
            - For example, ["204.1.2.2", "204.1.2.3"]
            type: list
            elements: str
            required: true
          interface_name:
            description:
            - List of interface names to update.
            - For example, ["GigabitEthernet1/0/11", "FortyGigabitEthernet1/1/1"]
            type: list
            elements: str
            required: true
          description:
            description:
            - Description text to assign to the interfaces.
            type: str
          admin_status:
            description:
            - Administrative status for interfaces (UP, DOWN, RESTART).
            type: str
            choices: [UP, DOWN, RESTART]
          vlan_id:
            description:
            - VLAN ID to assign to the interfaces.
            type: int
          voice_vlan_id:
            description:
            - Voice VLAN ID to assign to the interfaces.
            type: int
          deployment_mode:
            description:
            - Deployment mode (Deploy or Undeploy).
            type: str
            choices: [Deploy, Undeploy]
            default: Deploy
          clear_mac_address_table:
            description:
            - Whether to clear MAC address table on the interfaces (only for ACCESS devices).
            type: bool
            default: false
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - devices.Devices.get_device_list
    - devices.Devices.get_network_device_by_ip
    - devices.Devices.get_interface_details
    - licenses.Licenses.device_license_summary
- Paths used are
    - GET /dna/intent/api/v2/devices
    - GET /dna/intent/api/v2/network-device
    - GET /dna/intent/api/v2/interface/network-device/{id}/interface-name
    - GET /dna/intent/api/v1/licenses/device/summary
- Devices with type 'NETWORK_DEVICE' are automatically excluded from all generated configurations.
- A separate provision_wired_device configuration is generated below the device configs using site information from device_license_summary.
- The update_interface_details configuration fetches actual interface details from devices using the API analysis workflow.
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
          components_list: ["inventory_workflow_manager"]
          inventory_workflow_manager:
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

- name: Generate inventory playbook with update_interface_details configuration
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
      - update_interface_details:
          device_ips:
            - "204.1.2.2"
            - "204.1.2.3"
          interface_name:
            - "GigabitEthernet1/0/11"
            - "FortyGigabitEthernet1/1/1"
          description: "Updated by automation"
          admin_status: "UP"
          vlan_id: 100
          voice_vlan_id: 150
          deployment_mode: "Deploy"
          clear_mac_address_table: false
        file_path: "./inventory_update_interfaces.yml"
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
        # self.site_id_name_dict = self.get_site_id_name_mapping()
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
        self.log("Inside get_workflow_filters_schema function.", "DEBUG")
        return {
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
                    "is_filter_only": True,  # This component only filters existing provision data, doesn't fetch new data
                },
                "interface_details": {
                    "filters": [],
                    "is_filter_only": True,  # This component only controls interface details output, doesn't fetch new data
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
                "device_details": {
                    "type": {
                        "type": "str",
                        "required": False,
                        "choices": ["NETWORK_DEVICE", "COMPUTE_DEVICE", "MERAKI_DASHBOARD",
                                    "THIRD_PARTY_DEVICE", "FIREPOWER_MANAGEMENT_SYSTEM"]
                    },
                    "role": {
                        "type": "str",
                        "required": False,
                        "choices": ["ACCESS", "CORE", "DISTRIBUTION", "BORDER ROUTER", "UNKNOWN"]
                    },
                    "snmp_version": {
                        "type": "str",
                        "required": False,
                        "choices": ["v2", "v2c", "v3"]
                    },
                    "cli_transport": {
                        "type": "str",
                        "required": False,
                        "choices": ["ssh", "telnet", "SSH", "TELNET"]
                    }
                }
            }
        }

    def fetch_all_devices(self, reason=""):
        """
        Fetch all devices from Cisco Catalyst Center API.

        Args:
            reason (str): Optional reason for fetching all devices (for logging)

        Returns:
            list: List of all device dictionaries from API
        """
        self.log("Fetching all devices from Catalyst Center{0}".format(
            " - {0}".format(reason) if reason else ""
        ), "INFO")

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params={}
            )

            if response and "response" in response:
                devices = response.get("response", [])
                self.log("Retrieved {0} devices from get_device_list".format(len(devices)), "INFO")

                if devices:
                    self.log("Sample device fields from API: {0}".format(list(devices[0].keys())), "INFO")
                    self.log("Sample device full data: {0}".format(devices[0]), "DEBUG")

                return devices
            else:
                self.log("No devices returned from get_device_list", "WARNING")
                return []

        except Exception as e:
            self.log("Error fetching all devices: {0}".format(str(e)), "ERROR")
            return []

    def process_global_filters(self, global_filters):
        """
        Process global filters to retrieve device information from Cisco Catalyst Center.

        Args:
            global_filters (dict): Dictionary containing ip_address_list, hostname_list, serial_number_list, or mac_address_list

        Returns:
            dict: Dictionary containing device_ip_to_id_mapping with device details
        """
        self.log("Starting process_global_filters with filters: {0}".format(global_filters), "DEBUG")

        device_ip_to_id_mapping = {}

        try:
            # Extract filter lists
            ip_address_list = global_filters.get("ip_address_list", [])
            hostname_list = global_filters.get("hostname_list", [])
            serial_number_list = global_filters.get("serial_number_list", [])
            mac_address_list = global_filters.get("mac_address_list", [])

            self.log(
                "Extracted filters - IPs: {0}, Hostnames: {1}, Serials: {2}, MACs: {3}".format(
                    len(ip_address_list), len(hostname_list), len(serial_number_list), len(mac_address_list)
                ),
                "INFO",
            )

            # If no filters provided, return empty mapping
            # The calling function will handle retrieving all devices
            if not ip_address_list and not hostname_list and not serial_number_list and not mac_address_list:
                self.log("No specific filters provided", "DEBUG")
                return {"device_ip_to_id_mapping": {}}

            # Process IP address filters
            if ip_address_list:
                self.log("Processing {0} IP addresses".format(len(ip_address_list)), "INFO")
                for ip_address in ip_address_list:
                    try:
                        self.log("Fetching device details for IP: {0}".format(ip_address), "DEBUG")
                        response = self.dnac._exec(
                            family="devices",
                            function="get_network_device_by_ip",
                            params={"ip_address": ip_address}
                        )

                        if response and response.get("response"):
                            device_info = response["response"]
                            device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
                            if device_ip:
                                device_ip_to_id_mapping[device_ip] = device_info
                                self.log("Added device with IP: {0}".format(device_ip), "DEBUG")
                        else:
                            self.log("No device found for IP: {0}".format(ip_address), "WARNING")

                    except Exception as e:
                        self.log("Error fetching device by IP {0}: {1}".format(ip_address, str(e)), "ERROR")

            # Process hostname filters
            if hostname_list:
                self.log("Processing {0} hostnames".format(len(hostname_list)), "INFO")
                for hostname in hostname_list:
                    try:
                        self.log("Fetching device details for hostname: {0}".format(hostname), "DEBUG")
                        response = self.dnac._exec(
                            family="devices",
                            function="get_device_list",
                            params={"hostname": hostname}
                        )

                        if response and response.get("response"):
                            devices = response["response"]
                            for device_info in devices:
                                device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
                                if device_ip:
                                    device_ip_to_id_mapping[device_ip] = device_info
                                    self.log("Added device with hostname: {0}, IP: {1}".format(hostname, device_ip), "DEBUG")
                        else:
                            self.log("No device found for hostname: {0}".format(hostname), "WARNING")

                    except Exception as e:
                        self.log("Error fetching device by hostname {0}: {1}".format(hostname, str(e)), "ERROR")

            # Process serial number filters
            if serial_number_list:
                self.log("Processing {0} serial numbers".format(len(serial_number_list)), "INFO")
                for serial_number in serial_number_list:
                    try:
                        self.log("Fetching device details for serial: {0}".format(serial_number), "DEBUG")
                        response = self.dnac._exec(
                            family="devices",
                            function="get_device_list",
                            params={"serial_number": serial_number}
                        )

                        if response and response.get("response"):
                            devices = response["response"]
                            for device_info in devices:
                                device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
                                if device_ip:
                                    device_ip_to_id_mapping[device_ip] = device_info
                                    self.log("Added device with serial: {0}, IP: {1}".format(serial_number, device_ip), "DEBUG")
                        else:
                            self.log("No device found for serial number: {0}".format(serial_number), "WARNING")

                    except Exception as e:
                        self.log("Error fetching device by serial {0}: {1}".format(serial_number, str(e)), "ERROR")

            # Process MAC address filters
            if mac_address_list:
                self.log("Processing {0} MAC addresses".format(len(mac_address_list)), "INFO")
                for mac_address in mac_address_list:
                    try:
                        self.log("Fetching device details for MAC: {0}".format(mac_address), "DEBUG")
                        response = self.dnac._exec(
                            family="devices",
                            function="get_device_list",
                            params={"macAddress": mac_address}
                        )

                        if response and response.get("response"):
                            devices = response["response"]
                            for device_info in devices:
                                device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
                                if device_ip:
                                    device_ip_to_id_mapping[device_ip] = device_info
                                    self.log("Added device with MAC: {0}, IP: {1}".format(mac_address, device_ip), "DEBUG")
                        else:
                            self.log("No device found for MAC address: {0}".format(mac_address), "WARNING")

                    except Exception as e:
                        self.log("Error fetching device by MAC {0}: {1}".format(mac_address, str(e)), "ERROR")

            self.log(
                "Completed process_global_filters. Found {0} unique devices".format(
                    len(device_ip_to_id_mapping)
                ),
                "INFO",
            )
            return {"device_ip_to_id_mapping": device_ip_to_id_mapping}

        except Exception as e:
            self.log("Error in process_global_filters: {0}".format(str(e)), "ERROR")
            return {"device_ip_to_id_mapping": {}}

    def inventory_get_device_reverse_mapping(self):
        """
        Returns reverse mapping specification for inventory devices.
        Transforms API response from Catalyst Center to inventory_workflow_manager format.
        Maps device attributes from API response to playbook configuration structure.
        Includes only fields needed for inventory_workflow_manager module.
        """
        return OrderedDict({
            # Device IP Address (required for inventory_workflow_manager)
            "ip_address_list": {
                "type": "list",
                "source_key": "managementIpAddress",
                "transform": lambda x: [x] if x else []
            },
            
            # Device Type (required)
            "type": {
                "type": "str",
                "source_key": "type",
                "transform": lambda x: x if x else None
            },
            
            # Device Role
            "role": {
                "type": "str",
                "source_key": "role",
                "transform": lambda x: None
            },
            
            # CLI Transport (ssh/telnet)
            "cli_transport": {
                "type": "str",
                "source_key": "cliTransport",
                "transform": lambda x: x.lower() if x else "ssh"
            },
            
            # NETCONF Port
            "netconf_port": {
                "type": "str",
                "source_key": "netconfPort",
                "transform": lambda x: str(x) if x else "830"
            },
            
            # SNMP Mode
            "snmp_mode": {
                "type": "str",
                "source_key": "snmpVersion",
                "transform": lambda x: x if x else "{{ item.snmp_mode }}"
            },
            
            # SNMP Read-Only Community (for v2/v2c)
            "snmp_ro_community": {
                "type": "str",
                "source_key": "snmpRoCommunity",
                "transform": lambda x: x if x else "{{ item.snmp_ro_community }}"
            },
            
            # SNMP Read-Write Community (for v2/v2c)
            "snmp_rw_community": {
                "type": "str",
                "source_key": "snmpRwCommunity",
                "transform": lambda x: x if x else "{{ item.snmp_rw_community }}"
            },
            
            # SNMP Username (for v3)
            "snmp_username": {
                "type": "str",
                "source_key": "snmpUsername",
                "transform": lambda x: x if x else "{{ item.snmp_username }}"
            },
            
            # SNMP Auth Protocol (for v3)
            "snmp_auth_protocol": {
                "type": "str",
                "source_key": "snmpAuthProtocol",
                "transform": lambda x: x if x else "{{ item.snmp_auth_protocol }}"
            },
            
            # SNMP Privacy Protocol (for v3)
            "snmp_priv_protocol": {
                "type": "str",
                "source_key": "snmpPrivProtocol",
                "transform": lambda x: x if x else "{{ item.snmp_priv_protocol }}"
            },
            
            # SNMP Retry Count
            "snmp_retry": {
                "type": "int",
                "source_key": "snmpRetry",
                "transform": lambda x: int(x) if x else 3
            },
            
            # SNMP Timeout
            "snmp_timeout": {
                "type": "int",
                "source_key": "snmpTimeout",
                "transform": lambda x: int(x) if x else 5
            },
            
            # SNMP Version (alternate field name)
            "snmp_version": {
                "type": "str",
                "source_key": "snmpVersion",
                "transform": lambda x: x if x else "v2"
            },
            
            # HTTP Parameters (for specific device types)
            "http_username": {
                "type": "str",
                "source_key": "httpUserName",
                "transform": lambda x: x if x else "{{ item.http_username }}"
            },
            
            "http_password": {
                "type": "str",
                "source_key": "httpPassword",
                "transform": lambda x: x if x else "{{ item.http_password }}"
            },
            
            "http_port": {
                "type": "str",
                "source_key": "httpPort",
                "transform": lambda x: str(x) if x else "{{ item.http_port }}"
            },
            
            "http_secure": {
                "type": "bool",
                "source_key": "httpSecure",
                "transform": lambda x: x if x is not None else "{{ item.http_secure }}"
            },
            
            # Credential fields - NOT available from API (security reasons)
            # These must be provided by user in vars_files
            "username": {
                "type": "str",
                "source_key": None,
                "transform": lambda x: "{{ item.username }}"  # Template variable from vars_files
            },
            
            "password": {
                "type": "str",
                "source_key": None,
                "transform": lambda x: "{{ item.password }}"  # Template variable from vars_files
            },
            
            "enable_password": {
                "type": "str",
                "source_key": None,
                "transform": lambda x: "{{ item.enable_password }}"  # Template variable from vars_files
            },
            
            "snmp_auth_passphrase": {
                "type": "str",
                "source_key": None,
                "transform": lambda x: "{{ item.snmp_auth_passphrase }}"  # Template variable from vars_files
            },
            
            "snmp_priv_passphrase": {
                "type": "str",
                "source_key": None,
                "transform": lambda x: "{{ item.snmp_priv_passphrase }}"  # Template variable from vars_files
            },
            
            # Device operation flags
            "credential_update": {
                "type": "bool",
                "source_key": None,
                "transform": lambda x: "{{ item.credential_update }}"  # Template variable from vars_files
            },
            
            "clean_config": {
                "type": "bool",
                "source_key": None,
                "transform": lambda x: False  # Default to False
            },
            
            "device_resync": {
                "type": "bool",
                "source_key": None,
                "transform": lambda x: False  # Default to False
            },
            
            "reboot_device": {
                "type": "bool",
                "source_key": None,
                "transform": lambda x: False  # Default to False
            },
            
            # Complex nested structures - user must provide in vars_files
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
            }
        })

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

    def get_device_ids_by_ip(self, device_ips):
        """
        Get device IDs for a list of device IP addresses.
        Uses API #1: get_device_list by managementIpAddress
        
        Args:
            device_ips (list): List of management IP addresses
            
        Returns:
            dict: Mapping of IP address to device ID
        """
        self.log("Fetching device IDs for {0} IP addresses".format(len(device_ips)), "INFO")
        ip_to_id_map = {}
        
        try:
            for device_ip in device_ips:
                try:
                    response = self.dnac._exec(
                        family="devices",
                        function="get_device_list",
                        op_modifies=False,
                        params={"managementIpAddress": device_ip}
                    )
                    
                    self.log("Device lookup response for IP {0}: {1}".format(
                        device_ip, "received" if response else "empty"
                    ), "DEBUG")
                    
                    if response and "response" in response:
                        devices = response.get("response", [])
                        if devices and len(devices) > 0:
                            device_id = devices[0].get("id")
                            ip_to_id_map[device_ip] = device_id
                            self.log("Mapped IP {0} to device ID {1}".format(device_ip, device_id), "DEBUG")
                        else:
                            self.log("No device found for IP {0}".format(device_ip), "WARNING")
                    else:
                        self.log("Invalid response for IP {0}".format(device_ip), "WARNING")
                        
                except Exception as e:
                    self.log("Error fetching device ID for IP {0}: {1}".format(device_ip, str(e)), "WARNING")
                    continue
            
            self.log("Fetched device IDs for {0} IP addresses".format(len(ip_to_id_map)), "INFO")
            return ip_to_id_map
            
        except Exception as e:
            self.log("Error in get_device_ids_by_ip: {0}".format(str(e)), "ERROR")
            return {}

    def get_interface_details_for_device(self, device_id, interface_name):
        """
        Get interface details for a specific device and interface name.
        Uses API #2: get_interface_details
        
        Args:
            device_id (str): Device UUID
            interface_name (str): Interface name (e.g., "GigabitEthernet0/0/1")
            
        Returns:
            dict: Interface details including id, adminStatus, voiceVlan, vlanId, description
        """
        try:
            self.log("Fetching interface details for device {0}, interface {1}".format(
                device_id, interface_name
            ), "DEBUG")
            
            response = self.dnac._exec(
                family="devices",
                function="get_interface_details",
                op_modifies=False,
                params={
                    "device_id": device_id,
                    "name": interface_name
                }
            )
            
            self.log("Interface details response: {0}".format("received" if response else "empty"), "DEBUG")
            
            if response and "response" in response:
                interface_info = response.get("response")
                self.log("Successfully retrieved interface {0} details".format(interface_name), "DEBUG")
                return interface_info
            else:
                self.log("No interface details found for {0}".format(interface_name), "WARNING")
                return None
                
        except Exception as e:
            self.log("Error fetching interface details: {0}".format(str(e)), "WARNING")
            return None

    def build_update_interface_details_config(self, device_ips, interface_details_params):
        """
        Build update_interface_details configuration by fetching actual interface details
        from Catalyst Center API for specified device IPs and interfaces.
        
        Args:
            device_ips (list): List of device IP addresses
            interface_details_params (dict): Update parameters including interface_name, description, etc.
            
        Returns:
            dict: Configuration dictionary with ip_address_list and nested update_interface_details
        """
        self.log("Building update_interface_details config for {0} devices".format(
            len(device_ips)
        ), "INFO")
        
        try:
            # Step 1: Get device IDs from IP addresses (API #1)
            ip_to_id_map = self.get_device_ids_by_ip(device_ips)
            
            if not ip_to_id_map:
                self.log("No device IDs found for provided IPs", "WARNING")
                return {}
            
            self.log("Successfully mapped {0} IPs to device IDs".format(len(ip_to_id_map)), "INFO")
            
            # Step 2: Fetch interface details for each device (API #2)
            interface_names = interface_details_params.get("interface_name", [])
            if not isinstance(interface_names, list):
                interface_names = [interface_names]
            
            self.log("Fetching interface details for {0} interfaces".format(len(interface_names)), "INFO")
            
            fetched_interfaces = {}
            for device_ip, device_id in ip_to_id_map.items():
                fetched_interfaces[device_ip] = {}
                
                for interface_name in interface_names:
                    interface_info = self.get_interface_details_for_device(device_id, interface_name)
                    if interface_info:
                        fetched_interfaces[device_ip][interface_name] = interface_info
                        self.log("Fetched interface {0} for device {1}".format(
                            interface_name, device_ip
                        ), "DEBUG")
                    else:
                        self.log("Could not fetch interface {0} for device {1}".format(
                            interface_name, device_ip
                        ), "WARNING")
            
            # Step 3: Build update configuration in the format required by inventory_workflow_manager
            # Build nested update_interface_details structure
            update_interface_details = {
                "description": interface_details_params.get("description", ""),
                "admin_status": interface_details_params.get("admin_status"),
                "vlan_id": interface_details_params.get("vlan_id"),
                "voice_vlan_id": interface_details_params.get("voice_vlan_id"),
                "interface_name": interface_names,
                "deployment_mode": interface_details_params.get("deployment_mode", "Deploy"),
                "clear_mac_address_table": interface_details_params.get("clear_mac_address_table", False)
            }
            
            # Remove None values for cleaner YAML output
            update_interface_details = {k: v for k, v in update_interface_details.items() if v is not None and v != ""}
            
            # Build final config structure matching provision_wired_device format
            update_config = {
                "ip_address_list": device_ips,
                "update_interface_details": update_interface_details,
                "_fetched_interface_details": fetched_interfaces
            }
            
            self.log("Built update_interface_details config successfully", "INFO")
            return update_config
            
        except Exception as e:
            self.log("Error building update_interface_details config: {0}".format(str(e)), "ERROR")
            return {}

    def build_update_interface_details_from_all_devices(self, device_configs):
        """
        Fetch interface details from all devices in device_configs and consolidate
        into separate update_interface_details configs grouped by interface configuration.
        Uses get_interface_by_ip endpoint to fetch actual interface information.
        
        Args:
            device_configs (list): List of device configuration dicts with ip_address_list
            
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

        self.log("Retrieving module-supported network elements", "DEBUG")
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        self.log(
            "Retrieved {0} supported network elements: {1}".format(
                len(module_supported_network_elements),
                list(module_supported_network_elements.keys()),
            ),
            "DEBUG",
        )

        components_list = component_specific_filters.get(
            "components_list", module_supported_network_elements.keys()
        )

        # Convert to list if needed
        components_list = list(components_list) if not isinstance(components_list, list) else components_list

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
            if network_element.get("is_filter_only"):
                self.log("Skipping filter-only component: {0}".format(component), "DEBUG")
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
        
        # Check if update_interface_details is specified in yaml_config_generator
        update_interface_config = yaml_config_generator.get("update_interface_details")
        update_config_output = None
        if update_interface_config:
            self.log("Update interface details configuration provided: {0}".format(
                update_interface_config
            ), "INFO")
            
            device_ips = update_interface_config.get("device_ips", [])
            if device_ips:
                # Build update interface config by fetching actual interface details from API
                update_config = self.build_update_interface_details_config(
                    device_ips,
                    update_interface_config
                )
                
                if update_config:
                    # Remove internal fetched details before writing to YAML
                    if "_fetched_interface_details" in update_config:
                        fetched_details = update_config.pop("_fetched_interface_details")
                        self.log("Fetched interface details for {0} devices: {1}".format(
                            len(fetched_details), list(fetched_details.keys())
                        ), "DEBUG")
                    
                    # Store update config directly - it will be added to second_doc_config list
                    update_config_output = update_config
                    self.log("Prepared update_interface_details config for output", "INFO")
                else:
                    self.log("Failed to build update_interface_details config", "WARNING")
            else:
                self.log("No device_ips provided for update_interface_details", "WARNING")
        
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
            dicts_to_write.append({"config for adding network devices": device_configs})
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
                auto_interface_configs = self.build_update_interface_details_from_all_devices(all_transformed_for_interfaces)
                if auto_interface_configs:
                    self.log("Generated {0} interface detail configs (with global filters)".format(
                        len(auto_interface_configs)
                    ), "INFO")
            else:
                self.log("No devices found for interface details generation", "WARNING")
        
        # Second document with provision_wired_device and/or manual update_interface_details
        second_doc_config = []
        
        if include_provision_device and provision_config:
            # Only add if there are actual devices in the provision config
            provision_devices = provision_config.get("provision_wired_device", [])
            if provision_devices:
                second_doc_config.append(provision_config)
                self.log("Added provision_wired_device config section with {0} devices".format(len(provision_devices)), "DEBUG")
            else:
                self.log("Skipping empty provision_wired_device config (no devices after filtering)", "DEBUG")
        
        # Add manually specified update_interface_details if provided
        if update_config_output:
            second_doc_config.append(update_config_output)
            self.log("Added manually specified update_interface_details config", "DEBUG")
        
        if second_doc_config:
            dicts_to_write.append({"config for provisioning wired device": second_doc_config})
            self.log("Added second document with {0} config sections".format(len(second_doc_config)), "DEBUG")
        
        # Third document with auto-generated interface details
        if include_interface_details and auto_interface_configs:
            dicts_to_write.append({"config for updating interface details": auto_interface_configs})
            self.log("Added third document with {0} auto-generated interface configs".format(len(auto_interface_configs)), "DEBUG")
        
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
                yaml_content = yaml.dump(
                    data_dict,
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
        self.log("Starting transformation of {0} devices into CONSOLIDATED configurations".format(
            len(device_response)
        ), "INFO")

        # First pass: Transform each device to playbook format
        transformed_devices = []
        for device_index, device in enumerate(device_response):
            self.log("Processing device {0}/{1}: {2}".format(
                device_index + 1,
                len(device_response),
                device.get('hostname', 'Unknown')
            ), "DEBUG")

            device_config = {}

            for playbook_key, mapping_spec in reverse_mapping_spec.items():
                source_key = mapping_spec.get("source_key")
                transform_func = mapping_spec.get("transform")

                try:
                    if source_key:
                        api_value = device.get(source_key)
                    else:
                        api_value = None

                    # Apply transformation function
                    if transform_func and callable(transform_func):
                        transformed_value = transform_func(api_value)
                    else:
                        transformed_value = api_value

                    # Skip null/empty values for optional nested structures in device info
                    if playbook_key in [
                        "add_user_defined_field",
                        "provision_wired_device",
                        "update_interface_details",
                    ]:
                        if transformed_value is None or transformed_value == [] or transformed_value == {}:
                            continue

                    # Add to device configuration
                    device_config[playbook_key] = transformed_value

                except Exception as e:
                    self.log(
                        "Error transforming {0}: {1}".format(playbook_key, str(e)),
                        "ERROR"
                    )
                    device_config[playbook_key] = None

            transformed_devices.append(device_config)
            self.log("Device {0} ({1}) transformation complete".format(
                device_index + 1, device.get('hostname', 'Unknown')
            ), "INFO")

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
    # config = ccc_inventory_playbook_generator.validated_config
    # if len(config) == 1 and config[0].get("component_specific_filters") is None:
    #     ccc_inventory_playbook_generator.msg = (
    #         "No valid configurations found in the provided parameters."
    #     )
    #     ccc_inventory_playbook_generator.validated_config = [
    #         {
    #             'component_specific_filters':
    #             {
    #                 'components_list': []
    #             }
    #         }
    #     ]

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

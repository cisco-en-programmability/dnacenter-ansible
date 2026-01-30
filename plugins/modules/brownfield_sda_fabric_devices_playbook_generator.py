#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for SDA Fabric Devices Workflow Manager Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Archit Soni, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_sda_fabric_devices_playbook_generator
short_description: Generate YAML configurations playbook for 'sda_fabric_devices_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'sda_fabric_devices_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- Captures SDA fabric device configurations including fabric roles, border settings,
  L2/L3 handoffs, and wireless controller settings from existing deployments.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Archit Soni (@koderchit)
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
    - A list of filters for generating YAML playbook compatible with the `sda_fabric_devices_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all fabric sites and all supported features.
          - This mode discovers all SDA fabric sites in Cisco Catalyst Center and extracts all fabric device configurations.
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
          a default file name  "sda_fabric_devices_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "sda_fabric_devices_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
        required: false
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
            - Valid values are - "fabric_devices".
            - If specified, only the listed components will be included in the generated YAML file.
            - If not specified, all supported components will be included by default.
            type: list
            elements: str
            choices:
              - fabric_devices
          fabric_devices:
            description:
            - Filters specific to fabric device configuration retrieval.
            - Used to narrow down which fabric sites and devices should be included in the generated YAML file.
            - If no filters are provided, all fabric devices from all fabric sites in Cisco Catalyst Center will be retrieved.
            type: dict
            suboptions:
              fabric_name:
                description:
                - Name of the fabric site to filter by.
                - Retrieves all fabric devices configured in this fabric site.
                - This parameter is required when using fabric_devices filters.
                - Example Global/USA/SAN-JOSE, Global/India/Bangalore.
                type: str
                required: true
              device_ip:
                description:
                - IPv4 address of a specific device to filter by.
                - Retrieves configuration for the specific device within the fabric site.
                - The fabric_name parameter must be provided when using this filter.
                - Example 10.0.0.1, 192.168.1.100.
                type: str
              device_roles:
                description:
                - List of device roles to filter by.
                - Retrieves only devices with the specified fabric roles.
                - The fabric_name parameter must be provided when using this filter.
                - Can be combined with device_ip filter for more specific results.
                type: list
                elements: str
                choices:
                  - CONTROL_PLANE_NODE
                  - EDGE_NODE
                  - BORDER_NODE
                  - WIRELESS_CONTROLLER_NODE
                  - EXTENDED_NODE
"""

EXAMPLES = r"""
# Example 1: Generate all fabric device configurations for all fabric sites
- name: Generate complete brownfield SDA fabric devices configuration
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate all SDA fabric device configurations from Cisco Catalyst Center
      cisco.dnac.brownfield_sda_fabric_devices_playbook_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config_verify: true
        config:
          - generate_all_configurations: true

# Example 2: Generate all configurations with custom file path
- name: Generate complete brownfield SDA fabric devices configuration with custom filename
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate all SDA fabric device configurations to a specific file
      cisco.dnac.brownfield_sda_fabric_devices_playbook_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config_verify: true
        config:
          - file_path: "/tmp/complete_sda_fabric_devices_config.yaml"
            generate_all_configurations: true

# Example 3: Generate fabric device configurations for a specific fabric site
- name: Generate fabric device configurations for one fabric site
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export fabric devices from San Jose fabric
      cisco.dnac.brownfield_sda_fabric_devices_playbook_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config_verify: true
        config:
          - file_path: "/tmp/san_jose_fabric_devices.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"

# Example 4: Generate configuration for devices with specific roles in a fabric site
- name: Generate configuration for border and control plane devices
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export border and control plane fabric devices from San Jose fabric
      cisco.dnac.brownfield_sda_fabric_devices_playbook_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config_verify: true
        config:
          - file_path: "/tmp/border_and_cp_devices.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"
                device_roles: ["BORDER_NODE", "CONTROL_PLANE_NODE"]

# Example 5: Generate configuration for a specific device in a fabric site
- name: Generate configuration for a specific fabric device
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export specific fabric device configuration
      cisco.dnac.brownfield_sda_fabric_devices_playbook_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config_verify: true
        config:
          - file_path: "/tmp/specific_fabric_device.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"
                device_ip: "10.0.0.1"

# Example 6: Generate multiple configuration files in a single playbook run
- name: Generate multiple SDA fabric device configuration files
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate multiple brownfield SDA fabric device configurations
      cisco.dnac.brownfield_sda_fabric_devices_playbook_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config_verify: true
        config:
          - file_path: "/tmp/all_fabric_devices.yaml"
            generate_all_configurations: true
          - file_path: "/tmp/san_jose_only.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"
          - file_path: "/tmp/bangalore_border_devices.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/India/Bangalore"
                device_roles: ["BORDER_NODE"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "response": String,
          "version": String
        },
      "msg": String
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
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


class SdaFabricDevicesPlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.fabric_site_name_to_id_dict, self.fabric_site_id_to_name_dict = (
            self.get_fabric_site_name_to_id_mapping()
        )
        self.module_name = "sda_fabric_devices_workflow_manager"

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
        schema = {
            "network_elements": {
                "fabric_devices": {
                    "filters": {
                        "fabric_name": {"type": "str", "required": True},
                        "device_ip": {
                            "type": "str",
                            "pattern": r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        },
                        "device_roles": {
                            "type": "list",
                            "choices": [
                                "CONTROL_PLANE_NODE",
                                "EDGE_NODE",
                                "BORDER_NODE",
                                "WIRELESS_CONTROLLER_NODE",
                                "EXTENDED_NODE",
                            ],
                        },
                    },
                    "reverse_mapping_function": self.fabric_devices_temp_spec,
                    "api_function": "get_fabric_devices",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_devices_configuration,
                },
            },
            "global_filters": [],
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network elements: {network_elements}",
            "INFO",
        )

        return schema

    def fabric_devices_temp_spec(self):

        self.log("Generating temporary specification for fabric devices.", "DEBUG")
        fabric_devices = OrderedDict(
            {
                "fabric_name": {
                    "type": "str",
                    "required": True,
                    "special_handling": True,
                    "transform": self.transform_fabric_name,
                },
                "device_config": {
                    "type": "list",
                    "elements": "dict",
                    "required": True,
                    "special_handling": True,
                    "transform": self.transform_device_config,
                    "device_ip": {
                        "type": "str",
                        "required": True,
                    },
                    "device_roles": {
                        "type": "list",
                        "elements": "str",
                        "source_key": "fabricDeviceRoles",
                    },
                    "wireless_controller_settings": {
                        "type": "dict",
                        "enable": {"type": "bool"},
                        "reload": {"type": "bool", "default": False},
                        "primary_managed_ap_locations": {
                            "type": "list",
                            "elements": "str",
                        },
                        "secondary_managed_ap_locations": {
                            "type": "list",
                            "elements": "str",
                        },
                        "rolling_ap_upgrade": {
                            "type": "dict",
                            "enable": {"type": "bool"},
                            "ap_reboot_percentage": {
                                "type": "int",
                            },
                        },
                    },
                    "borders_settings": {
                        "type": "dict",
                        "layer3_settings": {
                            "type": "list",
                            "elements": "dict",
                            "local_autonomous_system_number": {
                                "type": "str",
                                "source_key": "localAutonomousSystemNumber",
                            },
                            "is_default_exit": {
                                "type": "bool",
                                "source_key": "isDefaultExit",
                                "default": True,
                            },
                            "import_external_routes": {
                                "type": "bool",
                                "source_key": "importExternalRoutes",
                                "default": True,
                            },
                            "border_priority": {
                                "type": "int",
                                "source_key": "borderPriority",
                                "default": 10,
                            },
                            "prepend_autonomous_system_count": {
                                "type": "int",
                                "source_key": "prependAutonomousSystemCount",
                                "default": 0,
                            },
                        },
                        "layer3_handoff_ip_transit": {
                            "type": "list",
                            "elements": "dict",
                            "transit_network_name": {
                                "type": "str",
                                "source_key": "transitNetworkName",
                            },
                            "interface_name": {
                                "type": "str",
                                "source_key": "interfaceName",
                            },
                            "external_connectivity_ip_pool_name": {
                                "type": "str",
                            },
                            "virtual_network_name": {
                                "type": "str",
                                "source_key": "virtualNetworkName",
                            },
                            "vlan_id": {
                                "type": "int",
                                "source_key": "vlanId",
                            },
                            "tcp_mss_adjustment": {
                                "type": "int",
                                "source_key": "tcpMssAdjustment",
                            },
                            "local_ip_address": {
                                "type": "str",
                                "source_key": "localIpAddress",
                            },
                            "remote_ip_address": {
                                "type": "str",
                                "source_key": "remoteIpAddress",
                            },
                            "local_ipv6_address": {
                                "type": "str",
                                "source_key": "localIpv6Address",
                            },
                            "remote_ipv6_address": {
                                "type": "str",
                                "source_key": "remoteIpv6Address",
                            },
                        },
                        "layer3_handoff_sda_transit": {
                            "type": "dict",
                            "transit_network_name": {
                                "type": "str",
                                "source_key": "transitNetworkName",
                            },
                            "affinity_id_prime": {
                                "type": "int",
                                "source_key": "affinityIdPrime",
                            },
                            "affinity_id_decider": {
                                "type": "int",
                                "source_key": "affinityIdDecider",
                            },
                            "connected_to_internet": {
                                "type": "bool",
                                "source_key": "connectedToInternet",
                                "default": False,
                            },
                            "is_multicast_over_transit_enabled": {
                                "type": "bool",
                                "source_key": "isMulticastOverTransitEnabled",
                                "default": False,
                            },
                        },
                        "layer2_handoff": {
                            "type": "list",
                            "elements": "dict",
                            "interface_name": {
                                "type": "str",
                                "source_key": "interfaceName",
                            },
                            "internal_vlan_id": {
                                "type": "int",
                                "source_key": "internalVlanId",
                            },
                            "external_vlan_id": {
                                "type": "int",
                                "source_key": "externalVlanId",
                            },
                        },
                    },
                },
            }
        )
        return fabric_devices

    def group_fabric_devices_by_fabric_id(self, all_fabric_devices):
        """
        Groups fabric devices by their fabric_id.

        Args:
            all_fabric_devices (list): List of device entries containing fabric_id and device_config

        Returns:
            dict: Dictionary mapping fabric_id to list of device configurations
        """
        self.log("Grouping fabric devices by fabric_id", "DEBUG")
        fabric_devices_by_fabric_id = {}

        for device_entry in all_fabric_devices:
            fabric_id = device_entry.get("fabric_id")
            device = device_entry.get("device_config")
            if fabric_id and device:
                if fabric_id not in fabric_devices_by_fabric_id:
                    fabric_devices_by_fabric_id[fabric_id] = []
                fabric_devices_by_fabric_id[fabric_id].append(device)
            else:
                self.log(
                    f"Device entry missing fabric_id or device_config: {self.pprint(device_entry)}",
                    "WARNING",
                )

        self.log(
            f"Grouped {len(all_fabric_devices)} devices into {len(fabric_devices_by_fabric_id)} fabric site(s)",
            "INFO",
        )
        self.log(
            f"Fabric IDs with device counts: {dict((fid, len(devices)) for fid, devices in fabric_devices_by_fabric_id.items())}",
            "DEBUG",
        )

        return fabric_devices_by_fabric_id

    def process_fabric_device_for_batch(
        self, device, device_id_to_ip_map, batch_idx, device_idx, total_devices
    ):
        """
        Process a single fabric device and format it for inclusion in the results.

        Args:
            device (dict): The device data from the API response
            device_id_to_ip_map (dict): Mapping of device IDs to IP addresses
            batch_idx (int): Current batch index for logging
            device_idx (int): Current device index for logging
            total_devices (int): Total number of devices in the batch for logging

        Returns:
            dict: Formatted device response with fabric_id, device_config, fabric_name, and device_ip
        """
        self.log(
            f"Processing device {device_idx}/{total_devices} in batch {batch_idx}",
            "DEBUG",
        )

        network_device_id = device.get("networkDeviceId")
        fabric_id = device.get("fabricId")
        fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id, "Unknown")
        device_ip = (
            device_id_to_ip_map.get(network_device_id) if network_device_id else None
        )

        self.log(
            f"Device details: network_device_id='{network_device_id}', device_ip='{device_ip}', "
            f"fabric_name='{fabric_name}', fabric_id='{fabric_id}'",
            "DEBUG",
        )

        if not device_ip:
            self.log(
                f"Warning: No IP address found for device with network_device_id '{network_device_id}' in fabric '{fabric_name}' (fabric_id: '{fabric_id}') in batch {batch_idx}",
                "WARNING",
            )

        formatted_device_response = {
            "fabric_id": device.get("fabricId"),
            "device_config": device,
            "fabric_name": fabric_name,
            "device_ip": device_ip,
        }
        return formatted_device_response

    def retrieve_all_fabric_devices_from_api(
        self, fabric_devices_params_list_to_query, api_family, api_function
    ):
        """
        Execute API calls to retrieve fabric devices based on provided query parameters.

        Args:
            fabric_devices_params_list_to_query (list): List of query parameter dictionaries
            api_family (str): API family name (e.g., 'sda')
            api_function (str): API function name (e.g., 'get_fabric_devices')

        Returns:
            list: List of fabric device entries with fabric_id, device_config, fabric_name, and device_ip
        """
        self.log("Starting API calls to retrieve fabric devices", "INFO")
        all_fabric_devices = []

        for idx, query_params in enumerate(fabric_devices_params_list_to_query, 1):
            self.log(
                f"Executing API call {idx}/{len(fabric_devices_params_list_to_query)} to get fabric device details with params: {self.pprint(query_params)}",
                "DEBUG",
            )

            try:
                response = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    params=query_params,
                )

                self.log(
                    f"API call {idx} response received: {self.pprint(response)}",
                    "DEBUG",
                )

                if response and isinstance(response, dict):
                    devices = response.get("response", [])
                    if devices:
                        self.log(
                            f"API call {idx} returned {len(devices)} fabric device(s)",
                            "INFO",
                        )

                        # Get device IDs for IP mapping
                        device_ids_in_batch = [
                            device.get("networkDeviceId")
                            for device in devices
                            if device.get("networkDeviceId")
                        ]

                        # Get device ID to IP mapping for this batch
                        device_id_to_ip_map = {}
                        if device_ids_in_batch:
                            self.log(
                                f"Retrieving device IPs for {len(device_ids_in_batch)} device(s) in this batch",
                                "DEBUG",
                            )
                            device_id_to_ip_map = self.get_device_ips_from_device_ids(
                                device_ids_in_batch
                            )
                            self.log(
                                f"Device ID to IP mapping for batch: {self.pprint(device_id_to_ip_map)}",
                                "DEBUG",
                            )
                        else:
                            self.log(
                                "No device IDs found in this batch for IP mapping",
                                "WARNING",
                            )

                        for device_idx, device in enumerate(devices, 1):
                            formatted_device_response = (
                                self.process_fabric_device_for_batch(
                                    device,
                                    device_id_to_ip_map,
                                    idx,
                                    device_idx,
                                    len(devices),
                                )
                            )
                            all_fabric_devices.append(formatted_device_response)
                    else:
                        self.log(
                            f"API call {idx} returned no fabric devices",
                            "DEBUG",
                        )
                else:
                    self.log(
                        f"API call {idx} returned unexpected response format",
                        "WARNING",
                    )

            except Exception as e:
                self.log(
                    f"Error during API call {idx} with params {query_params}: {str(e)}",
                    "ERROR",
                )
                continue

        self.log(
            f"Total fabric devices retrieved: {len(all_fabric_devices)}",
            "INFO",
        )

        return all_fabric_devices

    def get_fabric_devices_configuration(
        self, network_element, component_specific_filters=None
    ):

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            f"Getting fabric devices using API family '{api_family}' and function '{api_function}'",
            "INFO",
        )

        if not self.fabric_site_name_to_id_dict:
            self.log("No fabric sites found in Cisco Catalyst Center", "WARNING")
            return {"fabric_devices": []}

        fabric_devices_params_list_to_query = []

        if component_specific_filters:
            self.log(
                "Processing component-specific filters",
                "DEBUG",
            )
            params_for_query = {}

            if "fabric_name" in component_specific_filters:
                self.log("Fabric name filtering is required", "DEBUG")
                fabric_name = component_specific_filters.get("fabric_name")
                self.log(f"Processing fabric_name filter: '{fabric_name}'", "DEBUG")
                fabric_site_id = self.fabric_site_name_to_id_dict.get(fabric_name)

                if fabric_site_id:
                    self.log(
                        f"Fabric site '{fabric_name}' found with fabric_id '{fabric_site_id}'",
                        "DEBUG",
                    )
                    params_for_query["fabric_id"] = fabric_site_id
                else:
                    self.log(
                        f"Fabric site '{fabric_name}' not found in Cisco Catalyst Center.",
                        "WARNING",
                    )
                    return {"fabric_devices": []}

            if "device_ip" in component_specific_filters:
                device_ip = component_specific_filters.get("device_ip")
                self.log(
                    f"Processing device_ip filter: '{device_ip}'",
                    "DEBUG",
                )

                # Get device ID from device IP using helper function
                device_list_params = self.get_device_list_params(
                    ip_address_list=device_ip
                )
                device_info_map = self.get_device_list(device_list_params)
                if device_info_map and device_ip in device_info_map:
                    network_device_id = device_info_map[device_ip].get("device_id")
                    self.log(
                        f"Device with IP '{device_ip}' found with network_device_id '{network_device_id}'",
                        "DEBUG",
                    )
                    self.log(f"Adding device_id filter: {network_device_id}", "DEBUG")
                    params_for_query["networkDeviceId"] = network_device_id

                else:
                    self.log(
                        f"Device with IP '{device_ip}' not found in Cisco Catalyst Center.",
                        "WARNING",
                    )
                    return {"fabric_devices": []}

            if "device_roles" in component_specific_filters:
                device_roles = component_specific_filters.get("device_roles")
                self.log(
                    f"Adding device_roles filter: {device_roles}",
                    "DEBUG",
                )
                params_for_query["deviceRoles"] = device_roles

            if params_for_query:
                self.log(
                    f"Adding query parameters to list: {params_for_query}",
                    "DEBUG",
                )
                fabric_devices_params_list_to_query.append(params_for_query)
            else:
                self.log(
                    "No valid filters provided after processing component-specific filters.",
                    "WARNING",
                )
                return {"fabric_devices": []}
        else:
            self.log(
                "No component-specific filters provided. Retrieving all fabric devices from all fabric sites.",
                "INFO",
            )
            for fabric_name, fabric_id in self.fabric_site_name_to_id_dict.items():
                self.log(
                    f"Adding fabric site '{fabric_name}' with fabric_id '{fabric_id}' to query list",
                    "DEBUG",
                )
                fabric_devices_params_list_to_query.append({"fabric_id": fabric_id})

        self.log(
            f"Total fabric device queries to execute: {len(fabric_devices_params_list_to_query)}",
            "INFO",
        )
        # Pretty print the params
        self.log(
            f"Fabric device queries to execute:\n{self.pprint(fabric_devices_params_list_to_query)}",
            "DEBUG",
        )

        # Execute API calls to get fabric devices
        all_fabric_devices = self.retrieve_all_fabric_devices_from_api(
            fabric_devices_params_list_to_query, api_family, api_function
        )

        if not all_fabric_devices:
            self.log(
                "No fabric devices found matching the provided filters",
                "WARNING",
            )
            return {"fabric_devices": []}

        self.log(
            f"Details retrieved - all_fabric_devices:\n{self.pprint(all_fabric_devices)}",
            "DEBUG",
        )

        # Group fabric devices by fabric_id
        fabric_devices_by_fabric_id = self.group_fabric_devices_by_fabric_id(
            all_fabric_devices
        )

        ccc_version = self.get_ccc_version()
        if self.compare_dnac_versions(ccc_version, "2.3.7.9") < 0:
            self.log(
                f"Embedded wireless controller settings are not available in Catalyst Center version '{ccc_version}'. "
                f"Minimum required version is 2.3.7.9. Skipping embedded wireless controller settings retrieval.",
                "DEBUG",
            )
        else:
            self.log(
                f"Catalyst Center version '{ccc_version}' supports embedded wireless controller settings. "
                "Retrieving the embedded wireless controller settings details.",
                "INFO",
            )

            # Retrieve embedded wireless controller settings for all fabric sites
            wireless_settings_by_fabric_id = (
                self.retrieve_wireless_controller_settings_for_all_fabrics(
                    fabric_devices_by_fabric_id
                )
            )

            # Check if any embedded wireless controller settings were found
            if not wireless_settings_by_fabric_id:
                self.log(
                    "No embedded wireless controller settings found for any fabric site. Skipping managed AP locations retrieval.",
                    "INFO",
                )
            else:
                # Retrieve managed AP locations for all wireless controllers
                self.retrieve_managed_ap_locations_for_wireless_controllers(
                    wireless_settings_by_fabric_id
                )

            # Populate embedded wireless controller settings for each fabric site to its devices
            self.populate_wireless_controller_settings_to_devices(
                wireless_settings_by_fabric_id, fabric_devices_by_fabric_id
            )

        # Transform the data using the temp_spec
        self.log("Starting transformation of fabric devices data", "INFO")
        temp_spec = network_element.get("reverse_mapping_function")()

        transformed_fabric_devices_list = []
        for idx, device_entry in enumerate(all_fabric_devices, 1):
            fabric_device_details = device_entry.get("device_config")
            fabric_id = device_entry.get("fabric_id", "Unknown")
            fabric_name = device_entry.get("fabric_name", "Unknown")
            device_id = (
                fabric_device_details.get("networkDeviceId", "Unknown")
                if fabric_device_details
                else "Unknown"
            )

            self.log(
                f"Transforming device {idx}/{len(all_fabric_devices)} (device_id: {device_id}, fabric_id: {fabric_id}, fabric_name: '{fabric_name}')",
                "DEBUG",
            )

            if not fabric_device_details:
                self.log(
                    f"Skipping transformation for device entry {idx} - no device_config found",
                    "WARNING",
                )
                continue

            # Transform using modify_parameters
            transformed_data = self.modify_parameters(temp_spec, [device_entry])

            if transformed_data:
                transformed_fabric_devices_list.extend(transformed_data)

        self.log(
            f"Transformation complete. Generated {len(transformed_fabric_devices_list)} fabric device configuration(s)",
            "INFO",
        )

        return {"fabric_devices": transformed_fabric_devices_list}

    def transform_fabric_name(self, details):
        """
        Transform fabric_id to fabric_name using reverse mapping.

        Args:
            details (dict): Dictionary containing fabricId

        Returns:
            str: The fabric name corresponding to the fabric_id, or None if not found
        """

        self.log(
            f"Starting fabric_id to fabric_name transformation with details: {self.pprint(details)}",
            "DEBUG",
        )
        fabric_id = details.get("fabric_id")
        if not fabric_id:
            self.log("No fabric_id found in details", "WARNING")
            return None

        # Use reverse mapping dictionary for efficient lookup
        fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id)
        if fabric_name:
            self.log(
                f"Transformed fabric_id '{fabric_id}' to fabric_name '{fabric_name}'",
                "DEBUG",
            )
            return fabric_name

        self.log(
            f"No fabric_name found for fabric_id '{fabric_id}'",
            "WARNING",
        )
        return None

    def transform_device_config(self, details):
        """
        Transform device configuration data into playbook-ready format.

        Args:
            details (dict): Dictionary containing device_config and other device information

        Returns:
            dict: Transformed device configuration in playbook-ready format
        """
        self.log(
            f"Starting device_config transformation with details: {self.pprint(details)}",
            "DEBUG",
        )

        device_config = details.get("device_config")
        if not device_config:
            self.log("No device_config found in details", "WARNING")
            return None

        # Initialize playbook-ready device configuration
        transformed_device_config = {}

        # Add device_ip (required field)
        device_ip = details.get("device_ip")
        if device_ip:
            transformed_device_config["device_ip"] = device_ip
            self.log(
                f"Added device_ip '{device_ip}' to transformed_device_config",
                "DEBUG",
            )
        else:
            self.log(
                "No device_ip found in details - this is a required field",
                "WARNING",
            )

        # Transform device_roles from fabricDeviceRoles
        fabric_device_roles = device_config.get("deviceRoles", [])
        if fabric_device_roles:
            transformed_device_config["device_roles"] = fabric_device_roles
            self.log(
                f"Transformed deviceRoles to device_roles: {fabric_device_roles}",
                "DEBUG",
            )

        # Transform border settings if present
        border_settings = device_config.get("borderSettings")
        if border_settings:
            self.log(
                "Processing border settings",
                "DEBUG",
            )

            borders_settings = {}

            # Transform layer3Settings
            layer3_settings = border_settings.get("layer3Settings")
            if layer3_settings and isinstance(layer3_settings, list):
                borders_settings["layer3_settings"] = layer3_settings
                self.log(
                    f"Added {len(layer3_settings)} layer3_settings entry(ies)",
                    "DEBUG",
                )

            # Transform layer3HandoffIpTransit
            layer3_handoff_ip_transit = border_settings.get("layer3HandoffIpTransit")
            if layer3_handoff_ip_transit and isinstance(
                layer3_handoff_ip_transit, list
            ):
                borders_settings["layer3_handoff_ip_transit"] = (
                    layer3_handoff_ip_transit
                )
                self.log(
                    f"Added {len(layer3_handoff_ip_transit)} layer3_handoff_ip_transit entry(ies)",
                    "DEBUG",
                )

            # Transform layer3HandoffSdaTransit
            layer3_handoff_sda_transit = border_settings.get("layer3HandoffSdaTransit")
            if layer3_handoff_sda_transit:
                borders_settings["layer3_handoff_sda_transit"] = (
                    layer3_handoff_sda_transit
                )
                self.log(
                    "Added layer3_handoff_sda_transit settings",
                    "DEBUG",
                )

            # Transform layer2Handoff
            layer2_handoff = border_settings.get("layer2Handoff")
            if layer2_handoff and isinstance(layer2_handoff, list):
                borders_settings["layer2_handoff"] = layer2_handoff
                self.log(
                    f"Added {len(layer2_handoff)} layer2_handoff entry(ies)",
                    "DEBUG",
                )

            # Only add borders_settings if it has content
            if borders_settings:
                transformed_device_config["borders_settings"] = borders_settings
                self.log(
                    "Successfully transformed and added borders_settings to device_config",
                    "DEBUG",
                )
        else:
            self.log(
                "No border settings found in device_config",
                "DEBUG",
            )

        # Transform embedded wireless controller settings if present
        embedded_wireless_settings = device_config.get(
            "embeddedWirelessControllerSettings"
        )
        if embedded_wireless_settings:
            self.log(
                "Processing embedded wireless controller settings",
                "DEBUG",
            )

            # Transform to wireless_controller_settings format
            wireless_controller_settings = {}

            # Map basic settings
            wireless_controller_settings["enable"] = embedded_wireless_settings.get(
                "enableWireless"
            )
            self.log(self.pprint(embedded_wireless_settings), "DEBUG")
            wireless_controller_settings["primary_managed_ap_locations"] = [
                site_details.get("siteNameHierarchy")
                for site_details in embedded_wireless_settings.get(
                    "primaryManagedApLocations"
                )
            ]
            wireless_controller_settings["secondary_managed_ap_locations"] = [
                site_details.get("siteNameHierarchy")
                for site_details in embedded_wireless_settings.get(
                    "secondaryManagedApLocations"
                )
            ]

            rolling_ap_upgrade = embedded_wireless_settings.get("rollingApUpgrade")
            if rolling_ap_upgrade:
                wireless_controller_settings["rolling_ap_upgrade"] = {
                    "enable": rolling_ap_upgrade.get("enableRollingApUpgrade"),
                    "ap_reboot_percentage": rolling_ap_upgrade.get(
                        "apRebootPercentage"
                    ),
                }
                self.log(
                    "Added rolling_ap_upgrade settings",
                    "DEBUG",
                )
            else:
                self.log(
                    "No rolling_ap_upgrade settings found",
                    "WARNING",
                )

            transformed_device_config["wireless_controller_settings"] = (
                wireless_controller_settings
            )
            self.log(
                "Successfully transformed and added wireless_controller_settings to device_config",
                "DEBUG",
            )

        else:
            self.log(
                "No embedded wireless controller settings found in device_config",
                "DEBUG",
            )

        self.log(
            f"Device config transformation complete",
            "DEBUG",
        )

        return transformed_device_config

    def transform_device_ip(self, details):
        """
        Transform networkDeviceId to device IP address using device inventory lookup.

        Args:
            details (dict): Dictionary containing networkDeviceId and optionally device_ip

        Returns:
            str: The device IP address corresponding to the networkDeviceId, or None if not found
        """

        self.log(
            f"Starting networkDeviceId to device_ip transformation with details: {self.pprint(details)}",
            "DEBUG",
        )

        # Check if device_ip is already available in details (from earlier processing)
        device_ip = details.get("device_ip")
        if device_ip:
            self.log(
                f"Device IP '{device_ip}' already available in details",
                "DEBUG",
            )
            return device_ip

        network_device_id = details.get("networkDeviceId")
        if not network_device_id:
            self.log("No networkDeviceId found in details", "WARNING")
            return None

        # Get device IP from device ID using helper function (fallback)
        self.log(
            f"Device IP not in details, performing lookup for networkDeviceId '{network_device_id}'",
            "DEBUG",
        )
        try:
            device_id_to_ip_map = self.get_device_ips_from_device_ids(
                [network_device_id]
            )
            device_ip = device_id_to_ip_map.get(network_device_id)

            if device_ip:
                self.log(
                    f"Transformed networkDeviceId '{network_device_id}' to device_ip '{device_ip}'",
                    "DEBUG",
                )
                return device_ip
            else:
                self.log(
                    f"No device_ip found for networkDeviceId '{network_device_id}'",
                    "WARNING",
                )
                return None
        except Exception as e:
            self.log(
                f"Error transforming networkDeviceId '{network_device_id}' to device_ip: {str(e)}",
                "ERROR",
            )
            return None

    def retrieve_wireless_controller_settings_for_all_fabrics(
        self, fabric_devices_by_fabric_id
    ):
        """
        Iterate through fabric sites and retrieve embedded wireless controller settings for each.

        Args:
            fabric_devices_by_fabric_id (dict): Dictionary mapping fabric_id to list of device configurations

        Returns:
            dict: Dictionary mapping fabric_id to wireless controller settings
        """
        self.log(
            f"Iterating through {len(fabric_devices_by_fabric_id)} fabric site(s) to retrieve embedded wireless controller settings",
            "INFO",
        )

        wireless_settings_by_fabric_id = {}
        for fabric_id, devices in fabric_devices_by_fabric_id.items():
            fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id, "Unknown")
            self.log(
                f"Retrieving embedded wireless controller settings for fabric site '{fabric_name}' (fabric_id: '{fabric_id}') with {len(devices)} device(s)",
                "DEBUG",
            )

            wireless_settings = self.get_wireless_controller_settings_for_fabric(
                fabric_id
            )
            if wireless_settings:
                wireless_settings_by_fabric_id[fabric_id] = wireless_settings
                self.log(
                    f"Successfully retrieved and stored embedded wireless controller settings for fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                    "DEBUG",
                )
            else:
                self.log(
                    f"No embedded wireless controller settings found for fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                    "DEBUG",
                )

        self.log(
            f"Embedded wireless controller settings retrieval complete. Retrieved settings for {len(wireless_settings_by_fabric_id)} fabric site(s)",
            "INFO",
        )
        self.log(
            f"Embedded wireless controller settings by fabric ID:\n{self.pprint(wireless_settings_by_fabric_id)}",
            "DEBUG",
        )

        return wireless_settings_by_fabric_id

    def retrieve_managed_ap_locations_for_wireless_controllers(
        self, wireless_settings_by_fabric_id
    ):
        """
        Retrieve primary and secondary managed AP locations for all embedded wireless controllers.

        Args:
            wireless_settings_by_fabric_id (dict): Dictionary mapping fabric_id to wireless controller settings

        Returns:
            None: Modifies wireless_settings_by_fabric_id in place by adding primaryManagedApLocations
                  and secondaryManagedApLocations to each wireless controller's settings
        """
        self.log(
            "Retrieving primary and secondary managed AP locations for embedded wireless controllers",
            "INFO",
        )

        # Get device ID to IP mapping for all embedded wireless controllers
        all_embedded_wireless_controller_device_ids = [
            wireless_settings.get("id")
            for wireless_settings in wireless_settings_by_fabric_id.values()
            if wireless_settings.get("id")
        ]

        if all_embedded_wireless_controller_device_ids:
            self.log(
                f"Retrieving device IPs for {len(all_embedded_wireless_controller_device_ids)} embedded wireless controller device(s)",
                "DEBUG",
            )
            device_id_to_ip_map = self.get_device_ips_from_device_ids(
                all_embedded_wireless_controller_device_ids
            )
            self.log(
                f"Device ID to IP mapping: {self.pprint(device_id_to_ip_map)}",
                "DEBUG",
            )
        else:
            self.log(
                "No embedded wireless controller devices found. Skipping device IP mapping retrieval.",
                "DEBUG",
            )
            device_id_to_ip_map = {}

        for fabric_id, wireless_settings in wireless_settings_by_fabric_id.items():
            network_device_id = wireless_settings.get("id")
            device_ip = device_id_to_ip_map.get(network_device_id)
            fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id, "Unknown")
            self.log(
                f"Fetching primary and secondary managed AP locations for the device '{device_ip}' (device_id: '{network_device_id}') "
                f"in fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                "DEBUG",
            )

            # Get primary managed AP locations
            primary_ap_locations = self.get_managed_ap_locations_for_device(
                network_device_id, device_ip, ap_type="primary"
            )
            wireless_settings["primaryManagedApLocations"] = primary_ap_locations

            # Get secondary managed AP locations
            secondary_ap_locations = self.get_managed_ap_locations_for_device(
                network_device_id, device_ip, ap_type="secondary"
            )
            wireless_settings["secondaryManagedApLocations"] = secondary_ap_locations

            self.log(
                f"Retrieved {len(primary_ap_locations)} primary and {len(secondary_ap_locations)} secondary AP locations for device '{device_ip}'",
                "INFO",
            )

        self.log(
            "Completed retrieval of managed AP locations for all embedded wireless controllers",
            "INFO",
        )

    def populate_wireless_controller_settings_to_devices(
        self, wireless_settings_by_fabric_id, fabric_devices_by_fabric_id
    ):
        """
        Populate embedded wireless controller settings for each fabric site to its devices.

        Args:
            wireless_settings_by_fabric_id (dict): Dictionary mapping fabric_id to wireless controller settings
            fabric_devices_by_fabric_id (dict): Dictionary mapping fabric_id to list of device configurations

        Returns:
            None: Modifies fabric_devices_by_fabric_id in place by adding embeddedWirelessControllerSettings
                  to each device
        """
        self.log(
            "Populating embedded wireless controller settings for each fabric site to its devices",
            "INFO",
        )

        total_fabric_sites_to_process = len(wireless_settings_by_fabric_id)
        for idx, (fabric_id, wireless_settings) in enumerate(
            wireless_settings_by_fabric_id.items(), 1
        ):
            devices = fabric_devices_by_fabric_id.get(fabric_id)
            fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id, fabric_id)

            self.log(
                f"Processing fabric {idx}/{total_fabric_sites_to_process}: '{fabric_name}' (fabric_id: '{fabric_id}') with {len(devices) if devices else 0} device(s)",
                "DEBUG",
            )

            if not devices:
                self.log(
                    f"No devices found for fabric site '{fabric_name}' (fabric_id: '{fabric_id}'). Skipping.",
                    "WARNING",
                )
                continue

            devices_with_wireless_settings = 0
            devices_without_wireless_settings = 0

            total_devices = len(devices)
            for device_idx, device in enumerate(devices, 1):
                network_device_id = device.get("networkDeviceId")

                self.log(
                    f"Processing device {device_idx}/{total_devices} with network_device_id '{network_device_id}' in fabric '{fabric_name}'",
                    "DEBUG",
                )

                # Check if wireless settings exist for this fabric and if this device has embedded wireless controller settings
                if wireless_settings.get("id") == network_device_id:
                    device["embeddedWirelessControllerSettings"] = wireless_settings
                    devices_with_wireless_settings += 1
                    self.log(
                        f"Added embedded wireless controller settings to device '{network_device_id}' in fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                        "DEBUG",
                    )
                else:
                    device["embeddedWirelessControllerSettings"] = None
                    devices_without_wireless_settings += 1
                    self.log(
                        f"No embedded wireless controller settings found for device '{network_device_id}' in fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                        "DEBUG",
                    )

            self.log(
                f"Completed processing fabric '{fabric_name}': {devices_with_wireless_settings} device(s) with wireless settings, "
                f"{devices_without_wireless_settings} device(s) without wireless settings",
                "INFO",
            )

        self.log(
            f"Completed populating embedded wireless controller settings for all {total_fabric_sites_to_process} fabric site(s)",
            "INFO",
        )
        self.log(
            f"Fabric devices with populated embedded wireless controller settings:\n{self.pprint(fabric_devices_by_fabric_id)}",
            "DEBUG",
        )

    def get_wireless_controller_settings_for_fabric(self, fabric_id):
        """
        Retrieve wireless controller settings for a specific fabric site.

        Args:
            fabric_id (str): The fabric site ID

        Returns:
            dict: Wireless controller settings for the fabric, or None if not found/error
        """
        self.log(
            f"Retrieving wireless controller settings for fabric_id '{fabric_id}'",
            "DEBUG",
        )

        try:
            wireless_response = self.dnac._exec(
                family="fabric_wireless",
                function="get_sda_wireless_details_from_switches",
                params={"fabric_id": fabric_id},
            )

            self.log(
                f"Raw embedded wireless controller settings API response for fabric_id '{fabric_id}':\n{self.pprint(wireless_response)}",
                "DEBUG",
            )

            # Extract the response data
            if wireless_response and isinstance(wireless_response, dict):
                response_data = wireless_response.get("response")
                if (
                    response_data
                    and isinstance(response_data, list)
                    and len(response_data) > 0
                ):
                    wireless_response = response_data[0]
                    self.log(
                        f"Successfully retrieved wireless controller settings for fabric_id '{fabric_id}':\n{self.pprint(wireless_response)}",
                        "INFO",
                    )
                    return wireless_response
                else:
                    self.log(
                        f"No embedded wireless controller settings found for fabric_id '{fabric_id}'",
                        "DEBUG",
                    )
                    return None
            else:
                self.log(
                    f"Unexpected response format for embedded wireless controller settings for fabric_id '{fabric_id}'",
                    "WARNING",
                )
                return None

        except Exception as e:
            self.log(
                f"Error retrieving embedded wireless controller settings for fabric_id '{fabric_id}': {str(e)}",
                "WARNING",
            )
            return None

    def get_managed_ap_locations_for_device(
        self, network_device_id, device_ip, ap_type="primary"
    ):
        """
        Retrieve managed AP locations (primary or secondary) for a specific wireless controller.

        Args:
            network_device_id (str): Network device ID of the wireless controller
            device_ip (str): IP address of the wireless controller device
            ap_type (str): Type of AP locations to retrieve: 'primary' or 'secondary'. Defaults to 'primary'

        Returns:
            list: List of managed AP location dictionaries, or empty list if not found/error
        """
        self.log(
            f"Starting retrieval of {ap_type} managed AP locations for device '{network_device_id}' (IP: {device_ip})",
            "DEBUG",
        )

        allowed_ap_types = ["primary", "secondary"]
        if ap_type not in allowed_ap_types:
            self.log(
                f"Invalid ap_type: '{ap_type}' provided. Allowed types: {', '.join(allowed_ap_types)}",
                "ERROR",
            )
            return []

        api_function = (
            f"get_{ap_type}_managed_ap_locations_for_specific_wireless_controller"
        )
        managed_ap_locations_all = []
        offset = 1
        limit = 500
        batch_count = 0

        while True:
            batch_count += 1
            self.log(
                f"Batch {batch_count}: Requesting {ap_type} managed AP locations (offset={offset}, limit={limit}) for device '{device_ip}'",
                "DEBUG",
            )

            try:
                response = self.dnac._exec(
                    family="wireless",
                    function=api_function,
                    op_modifies=False,
                    params={
                        "network_device_id": network_device_id,
                        "limit": limit,
                        "offset": offset,
                    },
                )

                self.log(
                    f"API response ({ap_type} managed AP locations) for device '{device_ip}' (offset {offset}):\n{self.pprint(response)}",
                    "DEBUG",
                )

                if not isinstance(response, dict):
                    self.log(
                        f"Invalid API response type: {type(response)} received for {ap_type} AP locations",
                        "ERROR",
                    )
                    break

                managed_ap_response = response.get("response")
                if not managed_ap_response:
                    self.log(
                        f"Batch {batch_count}: No {ap_type} managed AP locations found in response for device '{device_ip}'. Stopping pagination",
                        "DEBUG",
                    )
                    break

                managed_ap_locations = managed_ap_response.get("managedApLocations", [])
                count = len(managed_ap_locations)

                self.log(
                    f"Batch {batch_count}: Retrieved {count} {ap_type} managed AP location(s) for device '{device_ip}'",
                    "DEBUG",
                )

                if count == 0:
                    self.log(
                        f"Batch {batch_count}: No more {ap_type} managed AP locations to retrieve. Stopping pagination",
                        "DEBUG",
                    )
                    break

                managed_ap_locations_all.extend(managed_ap_locations)
                offset += count

                # If we received fewer records than the limit, we've reached the end
                if count < limit:
                    self.log(
                        f"Batch {batch_count}: Received {count} records (less than limit {limit}). End of pagination",
                        "DEBUG",
                    )
                    break

            except Exception as e:
                self.log(
                    f"Error retrieving {ap_type} managed AP locations for device '{device_ip}': {str(e)}",
                    "WARNING",
                )
                break

        self.log(
            f"Total {ap_type} managed AP locations retrieved for device '{device_ip}': {len(managed_ap_locations_all)}",
            "INFO",
        )

        return managed_ap_locations_all

    def process_global_filters(self, global_filters):
        pass

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
            self.log(
                "Auto-discovery mode enabled - will process all devices and all features",
                "INFO",
            )

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No file_path provided by user, generating default filename", "DEBUG"
            )
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log(
            "YAML configuration file path determined: {0}".format(file_path), "DEBUG"
        )

        self.log("Initializing filter dictionaries", "DEBUG")
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log(
                "Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features",
                "INFO",
            )
            if yaml_config_generator.get("global_filters"):
                self.log(
                    "Warning: global_filters provided but will be ignored due to generate_all_configurations=True",
                    "WARNING",
                )
            if yaml_config_generator.get("component_specific_filters"):
                self.log(
                    "Warning: component_specific_filters provided but will be ignored due to generate_all_configurations=True",
                    "WARNING",
                )

            # Set empty filters to retrieve everything
            global_filters = {}
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = (
                yaml_config_generator.get("component_specific_filters") or {}
            )

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
            self.set_operation_result("ok", False, self.msg, "INFO")
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
            state (str): The desired state of the network elements ('gathered').
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
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    #  TODO: Check version 3.1.3.0 for the embedded wireless controller settings API support

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the SDA Fabric Devices Playbook Generator object with the module
    ccc_sda_fabric_devices_playbook_generator = SdaFabricDevicesPlaybookGenerator(
        module
    )
    if (
        ccc_sda_fabric_devices_playbook_generator.compare_dnac_versions(
            ccc_sda_fabric_devices_playbook_generator.get_ccc_version(), "2.3.7.6"
        )
        < 0
    ):
        ccc_sda_fabric_devices_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for SDA Fabric Devices Workflow Manager Module. Supported versions start from '2.3.7.6' onwards. ".format(
                ccc_sda_fabric_devices_playbook_generator.get_ccc_version()
            )
        )
        ccc_sda_fabric_devices_playbook_generator.set_operation_result(
            "failed", False, ccc_sda_fabric_devices_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_fabric_devices_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_sda_fabric_devices_playbook_generator.supported_states:
        ccc_sda_fabric_devices_playbook_generator.status = "invalid"
        ccc_sda_fabric_devices_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_sda_fabric_devices_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_sda_fabric_devices_playbook_generator.validate_input().check_return_status()
    config = ccc_sda_fabric_devices_playbook_generator.validated_config

    # Iterate over the validated configuration parameters
    for config in ccc_sda_fabric_devices_playbook_generator.validated_config:
        ccc_sda_fabric_devices_playbook_generator.reset_values()
        ccc_sda_fabric_devices_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_sda_fabric_devices_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_sda_fabric_devices_playbook_generator.result)


if __name__ == "__main__":
    main()

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
        self.fabric_site_name_to_id_dict = self.get_fabric_site_name_to_id_mapping()
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
                    "special_handling": True,
                    "transform": self.transform_fabric_name,
                },
                "device_config": {
                    "type": "list",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_device_config,
                },
            }
        )
        return fabric_devices

    def get_fabric_devices_configuration(
        self, network_element, component_specific_filters=None
    ):
        self.log("HELLO2")
        self.log(network_element)
        self.log(component_specific_filters)

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
            # No filters provided - get all fabric devices from all fabric sites
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
        self.log("Starting API calls to retrieve fabric devices", "INFO")
        all_fabric_devices = []

        for idx, query_params in enumerate(fabric_devices_params_list_to_query, 1):
            self.log(
                f"Executing API call {idx}/{len(fabric_devices_params_list_to_query)} with params: {self.pprint(query_params)}",
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
                        all_fabric_devices.extend(devices)
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

        if not all_fabric_devices:
            self.log(
                "No fabric devices found matching the provided filters",
                "WARNING",
            )
            return {"fabric_devices": []}

        else:
            self.log(
                f"Details retrieved - all_fabric_devices:\n{self.pprint(all_fabric_devices)}",
                "DEBUG",
            )

        # Group devices by fabric_id and transform using temp_spec
        self.log("Grouping fabric devices by fabric_id", "DEBUG")
        devices_by_fabric = {}

        for device in all_fabric_devices:
            fabric_id = device.get("fabricId")
            if fabric_id:
                if fabric_id not in devices_by_fabric:
                    devices_by_fabric[fabric_id] = []
                devices_by_fabric[fabric_id].append(device)

        self.log(
            f"Devices grouped into {len(devices_by_fabric)} fabric site(s)",
            "DEBUG",
        )

        # # Transform the data using the temp_spec
        # self.log("Starting transformation of fabric devices data", "INFO")
        # temp_spec = network_element.get("reverse_mapping_function")()

        # fabric_devices_list = []
        # for fabric_id, devices in devices_by_fabric.items():
        #     self.log(
        #         f"Transforming {len(devices)} device(s) for fabric_id: {fabric_id}",
        #         "DEBUG",
        #     )

        #     # Create a data structure that matches what modify_parameters expects
        #     fabric_data = {
        #         "fabricId": fabric_id,
        #         "devices": devices,
        #     }

        #     # Transform using modify_parameters
        #     transformed_data = self.modify_parameters(temp_spec, [fabric_data])

        #     if transformed_data:
        #         fabric_devices_list.extend(transformed_data)

        # self.log(
        #     f"Transformation complete. Generated {len(fabric_devices_list)} fabric device configuration(s)",
        #     "INFO",
        # )

        # return {"fabric_devices": fabric_devices_list}

    def transform_fabric_name(self, details):
        """
        Transform fabric_id to fabric_name using reverse mapping.

        Args:
            details (dict): Dictionary containing fabricId

        Returns:
            str: The fabric name corresponding to the fabric_id, or None if not found
        """
        fabric_id = details.get("fabricId")
        if not fabric_id:
            self.log("No fabricId found in details", "WARNING")
            return None

        # Reverse lookup: find fabric_name from fabric_id
        for fabric_name, fid in self.fabric_site_name_to_id_dict.items():
            if fid == fabric_id:
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
            ccc_sda_fabric_devices_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_sda_fabric_devices_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for SDA Fabric Devices Workflow Manager Module. Supported versions start from '2.3.7.9' onwards. ".format(
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

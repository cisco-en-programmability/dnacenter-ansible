#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wired Campus Automation Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ", Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_sda_fabric_transits_config_generator
short_description: Generate YAML configurations playbook for 'sda_fabric_transits_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'sda_fabric_transits_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
version_added: 6.17.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Abhishek Maheshwari (@abmahesh)
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
    - A list of filters for generating YAML playbook compatible with the `sda_fabric_transits_workflow_manager`
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
          a default file name  "sda_fabric_transits_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "sda_fabric_transits_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
      global_filters:
        description:
        - Global filters to apply when generating the YAML configuration file.
        - These filters apply to all components unless overridden by component-specific filters.
        type: dict
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
            - Valid values are "sda_fabric_transits"
            - If not specified, all components are included.
            - For example, ["sda_fabric_transits"].
            type: list
            elements: str
          sda_fabric_transits:
            description:
            - Fabric transits to filter by name or transit type.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                - Transit name to filter fabric transits by name.
                type: str
              transit_type:
                description:
                - Transit type to filter fabric transits by type.
                - Valid values are IP_BASED_TRANSIT, SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT
                type: str
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - sda.Sda.get_transit_networks
    - network_device.NetworkDevice.get_device_list
- Paths used are
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/sda/transit-networks
    - GET /dna/intent/api/v1/network-device
"""

EXAMPLES = r"""
- name: Auto-generate YAML Configuration for all fabric transits
  cisco.dnac.brownfield_sda_fabric_transits_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - generate_all_configurations: true
- name: Generate YAML Configuration with File Path specified
  cisco.dnac.brownfield_sda_fabric_transits_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - file_path: "/tmp/catc_fabric_transits_config.yaml"
- name: Generate YAML Configuration with specific fabric transits components only
  cisco.dnac.brownfield_sda_fabric_transits_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - file_path: "/tmp/catc_fabric_transits_config.yaml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]
- name: Generate YAML Configuration for fabric transits with transit type filter
  cisco.dnac.brownfield_sda_fabric_transits_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - file_path: "/tmp/catc_fabric_transits_config.yaml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]
          sda_fabric_transits:
            - transit_type: "IP_BASED_TRANSIT"
            - transit_type: "SDA_LISP_BGP_TRANSIT"
- name: Generate YAML Configuration for fabric transits with name filter
  cisco.dnac.brownfield_sda_fabric_transits_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - file_path: "/tmp/catc_fabric_transits_config.yaml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]
          sda_fabric_transits:
            - name: "Transit1"
            - name: "Transit2"
- name: Generate YAML Configuration for fabric transits with name and type filter
  cisco.dnac.brownfield_sda_fabric_transits_config_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: gathered
    config:
      - file_path: "/tmp/catc_fabric_transits_config.yaml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]
          sda_fabric_transits:
            - name: "Transit1"
              transit_type: "IP_BASED_TRANSIT"
            - name: "Transit2"
              transit_type: "SDA_LISP_PUB_SUB_TRANSIT"
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
)
from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
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


class SdaFabricTransitsPlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.device_id_ip_mapping = self.get_device_id_management_ip_mapping()
        self.module_name = "sda_fabric_transits_workflow_manager"

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
        """
        Get the workflow filters schema for SDA fabric transits.

        Returns:
            dict: A dictionary containing network elements configuration with filters,
                API details, and processing functions for fabric transits.
        """
        return {
            "network_elements": {
                "sda_fabric_transits": {
                    "filters": ["name", "transit_type"],
                    "temp_spec_function": self.fabric_transit_temp_spec,
                    "api_function": "get_transit_networks",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_transits_configuration,
                },
            },
            "global_filters": [],
        }

    def fabric_transit_temp_spec(self):
        """
        Constructs a temporary specification for fabric transits, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as transit name,
        transit type, site hierarchy, IP transit settings, and SDA transit settings.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of fabric transit attributes.
        """

        self.log("Generating temporary specification for fabric transits.", "DEBUG")

        fabric_transit = OrderedDict(
            {
                "name": {"type": "str", "source_key": "name"},
                "transit_site_hierarchy": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_transit_site_hierarchy,
                },
                "transit_type": {"type": "str", "source_key": "type"},
                "ip_transit_settings": {
                    "type": "dict",
                    "source_key": "ipTransitSettings",
                    "options": OrderedDict(
                        {
                            "routing_protocol_name": {
                                "type": "str",
                                "source_key": "routingProtocolName",
                            },
                            "autonomous_system_number": {
                                "type": "int",
                                "source_key": "autonomousSystemNumber",
                            },
                        }
                    ),
                },
                "sda_transit_settings": {
                    "type": "dict",
                    "source_key": "sdaTransitSettings",
                    "options": OrderedDict(
                        {
                            "is_multicast_over_transit_enabled": {
                                "type": "bool",
                                "source_key": "isMulticastOverTransitEnabled",
                            },
                            "control_plane_network_device_ips": {
                                "type": "list",
                                "elements": "str",
                                "special_handling": True,
                                "transform": self.transform_control_plane_device_ids_to_ips,
                            },
                        }
                    ),
                },
            }
        )

        self.log("Fabric transit temp spec generated successfully.", "DEBUG")

        return fabric_transit

    def transform_transit_site_hierarchy(self, transit_details):
        """
        Transforms a site ID into its corresponding site hierarchy name.
        Args:
            transit_details (dict): The transit details containing the siteId.
        Returns:
            str: The site hierarchy name corresponding to the provided site ID.
        """

        site_id = transit_details.get("siteId")
        self.log(
            "Transforming site ID to site hierarchy name: {0}".format(site_id), "DEBUG"
        )

        if not site_id:
            self.log("No site ID provided", "DEBUG")
            return ""

        site_hierarchy_name = self.site_id_name_dict.get(site_id)
        if not site_hierarchy_name:
            self.log(
                "Site ID {0} not found in site ID to name mapping.".format(site_id),
                "DEBUG",
            )
            return ""

        self.log(
            "Transformed site ID {0} to site hierarchy name {1}".format(
                site_id, site_hierarchy_name
            ),
            "DEBUG",
        )

        return site_hierarchy_name

    def transform_control_plane_device_ids_to_ips(self, sda_transit_settings):
        """
        Transforms control plane network device IDs to their corresponding IP addresses.

        Args:
            sda_transit_settings (dict): The SDA transit settings containing controlPlaneNetworkDeviceIds.

        Returns:
            list: A list of management IP addresses corresponding to the device IDs.
        """

        self.log(
            "Transforming control plane device IDs to IPs from SDA transit settings: {0}".format(
                sda_transit_settings
            ),
            "DEBUG",
        )

        # Extract controlPlaneNetworkDeviceIds from the settings
        control_plane_device_ids = sda_transit_settings.get(
            "controlPlaneNetworkDeviceIds", []
        )

        self.log(
            "Extracted control plane device IDs: {0}".format(control_plane_device_ids),
            "DEBUG",
        )

        if not control_plane_device_ids:
            self.log(
                "No control plane device IDs found in SDA transit settings", "DEBUG"
            )
            return []

        device_ips = []

        for device_id in control_plane_device_ids:
            device_ip = self.device_id_ip_mapping.get(device_id)
            if not device_ip:
                self.log(
                    "Device ID {0} not found in device ID to IP mapping.".format(
                        device_id
                    ),
                    "DEBUG",
                )
                continue

            self.log(
                "Mapping device ID {0} to IP {1}".format(device_id, device_ip), "DEBUG"
            )
            device_ips.append(device_ip)

        self.log(
            "Transformed control plane device IDs to IPs: {0}".format(device_ips),
            "DEBUG",
        )

        return sorted(device_ips) if device_ips else []

    def get_fabric_transits_configuration(
        self, network_element, component_specific_filters=None
    ):
        """
        Retrieves fabric transits based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving fabric transits.
            component_specific_filters (list, optional): A list of dictionaries containing filters for fabric transits.

        Returns:
            dict: A dictionary containing the modified details of fabric transits.
        """

        self.log(
            "Starting to retrieve fabric transits with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        # Extract API family and function from network_element
        final_fabric_transits = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting fabric transits using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {}
        if component_specific_filters:
            for filter_param in component_specific_filters:
                self.log(
                    "Processing filter parameter: {0}".format(filter_param), "DEBUG"
                )
                for key, value in filter_param.items():
                    if key == "name":
                        params["name"] = value
                    elif key == "transit_type":
                        params["type"] = value
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )

                # Execute API call to retrieve fabric transit details with filters
                fabric_transit_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )
                self.log(
                    "Retrieved fabric transit details: {0}".format(
                        fabric_transit_details
                    ),
                    "INFO",
                )
                final_fabric_transits.extend(fabric_transit_details)
                params.clear()

            self.log("Using component-specific filters for API call.", "INFO")
        else:
            # Execute API call to retrieve all fabric transit details
            fabric_transit_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )
            self.log(
                "Retrieved fabric transit details: {0}".format(fabric_transit_details),
                "INFO",
            )
            final_fabric_transits.extend(fabric_transit_details)

        # Modify fabric transit details using temp_spec
        fabric_transit_temp_spec = self.fabric_transit_temp_spec()
        transit_details = self.modify_parameters(
            fabric_transit_temp_spec, final_fabric_transits
        )
        modified_fabric_transits_details = {}
        modified_fabric_transits_details["fabric_transits"] = transit_details

        self.log(
            "Modified fabric transit details: {0}".format(
                modified_fabric_transits_details
            ),
            "INFO",
        )

        return modified_fabric_transits_details

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
        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )
        self.log(
            "Module supported network elements: {0}".format(
                module_supported_network_elements
            ),
            "DEBUG",
        )

        self.log("Determining components list for processing", "DEBUG")
        self.log(
            "Component specific filters provided: {0}".format(
                component_specific_filters
            ),
            "DEBUG",
        )
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )

        # If components_list is empty, default to all supported components
        if not components_list:
            self.log(
                "No components specified; processing all supported components.", "INFO"
            )
            components_list = list(module_supported_network_elements.keys())

        self.log("Components to process: {0}".format(components_list), "DEBUG")
        self.log(
            "Keys in module_supported_network_elements: {0}".format(
                module_supported_network_elements.keys()
            ),
            "DEBUG",
        )

        self.log("Initializing final configuration list", "DEBUG")

        final_list = []
        for component in components_list:
            self.log("Processing component: {0}".format(component), "DEBUG")
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Component {0} not supported by module, skipping processing".format(
                        component
                    ),
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
            self.log(
                "No configurations found to process, setting appropriate result",
                "WARNING",
            )
            self.msg = {
                "message": "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                    self.module_name
                )
            }
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
            state (str): The desired state of the network elements ('gathered' or 'deleted').
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

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_sda_fabric_transits_playbook_generator = SdaFabricTransitsPlaybookGenerator(
        module
    )
    if (
        ccc_sda_fabric_transits_playbook_generator.compare_dnac_versions(
            ccc_sda_fabric_transits_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_sda_fabric_transits_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for <module_name_caps> Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_sda_fabric_transits_playbook_generator.get_ccc_version()
            )
        )
        ccc_sda_fabric_transits_playbook_generator.set_operation_result(
            "failed", False, ccc_sda_fabric_transits_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_fabric_transits_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_sda_fabric_transits_playbook_generator.supported_states:
        ccc_sda_fabric_transits_playbook_generator.status = "invalid"
        ccc_sda_fabric_transits_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_sda_fabric_transits_playbook_generator.check_recturn_status()

    # Validate the input parameters and check the return statusk
    ccc_sda_fabric_transits_playbook_generator.validate_input().check_return_status()
    config = ccc_sda_fabric_transits_playbook_generator.validated_config
    if len(config) == 1 and config[0].get("component_specific_filters") is None:
        ccc_sda_fabric_transits_playbook_generator.msg = (
            "No valid configurations found in the provided parameters."
        )
        ccc_sda_fabric_transits_playbook_generator.validated_config = [
            {"component_specific_filters": {"components_list": []}}
        ]

    # Iterate over the validated configuration parameters
    for config in ccc_sda_fabric_transits_playbook_generator.validated_config:
        ccc_sda_fabric_transits_playbook_generator.reset_values()
        ccc_sda_fabric_transits_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_sda_fabric_transits_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_sda_fabric_transits_playbook_generator.result)


if __name__ == "__main__":
    main()

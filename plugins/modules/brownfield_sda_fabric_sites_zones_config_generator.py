#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to manage Extranet Policy Operations in SD-Access Fabric in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Abhishek Maheshwari, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_sda_fabric_sites_zones_config_generator
short_description: Generate YAML playbook for 'brownfield_sda_fabric_sites_zones_config_generator' module.
description:
- Generates YAML configurations compatible with the `brownfield_sda_fabric_sites_zones_config_generator`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the fabric sites and zones
  configured on the Cisco Catalyst Center.
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
    - A list of filters for generating YAML playbook compatible with the `brownfield_sda_fabric_sites_zones_config_generator`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - If true, all components are included in the YAML configuration file i.e fabric_sites,
          fabric_zones.
        - If false, only the components specified in "components_list" are included.
        type: bool
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "brownfield_sda_fabric_sites_zones_config_generator_playbook_22_Apr_2025_21_43_26_379.yml".
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
              - Fabric Sites "fabric_sites"
              - Fabric Zones "fabric_zones"
            - If not specified, all components are included.
            - For example, ["fabric_sites", "fabric_zones"].
            type: list
            elements: str
          fabric_sites:
            description:
            - Fabric Sites to filter fabric sites by site name or site id.
            type: list
            elements: dict
          fabric_zones:
            description:
            - Fabric Zones to filter fabric zones by zone name or zone id.
            type: list
            elements: dict

requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site - site_design.SiteDesigns.get_sites
    - sda.Sda.get_fabric_sites
    - sda.Sda.get_fabric_zones
    - sda.Sda.get_fabric_sites_by_id
    - sda.Sda.get_fabric_zones_by_id
- Paths used are
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/sda/fabric-sites
    - GET /dna/intent/api/v1/sda/fabric-zones
    - GET /dna/intent/api/v1/sda/fabric-sites/{id}
    - GET /dna/intent/api/v1/sda/fabric-zones/{id}
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with File Path specified
  cisco.dnac.brownfield_sda_fabric_sites_zones_config_generator:
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
      - file_path: "/tmp/catc_virtual_networks_components_config.yaml"
- name: Generate YAML Configuration with specific fabric sites components only
  cisco.dnac.brownfield_sda_fabric_sites_zones_config_generator:
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
      - file_path: "/tmp/catc_virtual_networks_components_config.yaml"
        component_specific_filters:
          components_list: ["fabric_sites"]
- name: Generate YAML Configuration with specific fabric zones components only
  cisco.dnac.brownfield_sda_fabric_sites_zones_config_generator:
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
      - file_path: "/tmp/catc_virtual_networks_components_config.yaml"
        component_specific_filters:
          components_list: ["fabric_zones"]
- name: Generate YAML Configuration for all components
  cisco.dnac.brownfield_sda_fabric_sites_zones_config_generator:
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
      - file_path: "/tmp/catc_virtual_networks_components_config.yaml"
        component_specific_filters:
          components_list: ["fabric_sites", "fabric_zones"]
- name: Generate YAML Configuration for all components
  cisco.dnac.brownfield_sda_fabric_sites_zones_config_generator:
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


class BrownFieldFabricSiteZonePlaybookGenerator(DnacBase, BrownFieldHelper):
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
        self.module_name = "brownfield_sda_fabric_sites_zones_config_generator"

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
        Description:
            Constructs and returns a structured mapping for managing various virtual network elements
            such as fabric VLANs, virtual networks, and anycast gateways. This mapping includes
            associated filters, temporary specification functions, API details, and fetch function references
            used in the virtual network workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods like
                `fabric_vlan_temp_spec`, `get_fabric_vlans`, etc.

        Return:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a network component
                (e.g., 'fabric_vlan', 'virtual_networks', 'anycast_gateways') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "temp_spec_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'sda').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
                - "global_filters": An empty list reserved for global filters applicable across all network elements.
        """

        return {
            "network_elements": {
                "fabric_sites": {
                    "filters": ["site_name_hierarchy"],
                    "temp_spec_function": self.fabric_site_temp_spec,
                    "api_function": "get_fabric_sites",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_sites_from_ccc,
                },
                "fabric_zones": {
                    "filters": ["site_name_hierarchy"],
                    "temp_spec_function": self.fabric_zone_temp_spec,
                    "api_function": "get_fabric_zones",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_zones_from_ccc,
                },
            },
            "global_filters": [],
        }

    def transform_fabric_site_name(self, site_details):
        """
        Transforms fabric site-related information for a given VLAN by extracting and mapping
        the site hierarchy and fabric type based on the fabric ID.

        Args:
            site_details (dict): A dictionary containing VLAN-specific information, including the 'fabricId' key.

        Returns:
            list: A list containing a single dictionary with the following keys:
                - "site_name_hierarchy" (str): The hierarchical name of the site (e.g., "Global/Site/Building").
                - "fabric_type" (str): The type of fabric, such as "fabric_site" or "fabric_zone".
        """

        self.log(
            "Transforming fabric site locations for VLAN details: {0}".format(site_details),
            "DEBUG"
        )
        site_id = site_details.get("siteId")
        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        self.log(f"Transformed site name hierarchy: {site_name_hierarchy} with site details: {site_details}", "DEBUG")

        return site_name_hierarchy

    def fabric_site_temp_spec(self):
        """
        Constructs a temporary specification for fabric VLANs, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as VLAN name,
        VLAN ID, fabric site locations, traffic type, and various flags related to wireless and resource management.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of fabric VLAN attributes.
        """

        self.log("Generating temporary specification for fabric VLANs.", "DEBUG")
        fabric_sites = OrderedDict(
            {
                "site_name_hierarchy": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_fabric_site_name,
                },
                "fabric_type": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda x: "fabric_site",
                },
                "is_pub_sub_enabled": {"type": "bool", "source_key": "isPubSubEnabled"},
                "authentication_profile": {"type": "str", "source_key": "authenticationProfileName"}
            }
        )
        return fabric_sites

    def fabric_zone_temp_spec(self):
        """
        Constructs a temporary specification for fabric zones, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as zone name,
        zone ID, fabric site locations, and various flags related to wireless and resource management.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of fabric zone attributes.
        """

        self.log("Generating temporary specification for fabric zones.", "DEBUG")
        fabric_sites = OrderedDict(
            {
                "site_name_hierarchy": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_fabric_site_name,
                },
                "fabric_type": {
                    "type": "str",
                    "special_handling": True,
                    "transform": lambda x: "fabric_zone",
                },
                "authentication_profile": {"type": "str", "source_key": "authenticationProfileName"}
            }
        )
        return fabric_sites

    def get_fabric_sites_from_ccc(self, network_element, component_specific_filters=None):
        """
        Retrieves fabric VLANs based on the provided network element and component-specific filters.
        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving fabric VLANs.
            component_specific_filters (list, optional): A list of dictionaries containing filters for fabric VLANs.

        Returns:
            dict: A dictionary containing the modified details of fabric VLANs.
        """

        self.log(
            "Starting to retrieve fabric sites using network element: {0}".format(
                network_element
            ),
            "DEBUG",
        )
        # Extract API family and function from network_element
        final_fabric_sites = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "Getting sda fabric sites using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {}
        if component_specific_filters:
            self.log("Using component-specific filters for API call.", "DEBUG")
            for filter_param in component_specific_filters:
                self.log("Processing filter parameter: {0}".format(filter_param), "DEBUG")
                for key, value in filter_param.items():
                    if key == "site_name_hierarchy":
                        site_exists, site_id = self.get_site_id(value)
                        if site_exists:
                            self.log(
                                "Mapped site name hierarchy '{0}' to site ID '{1}'.".format(
                                    value, site_id
                                ),
                                "DEBUG"
                            )
                            params["siteId"] = site_id
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )
                self.log("Executing API call to retrieve fabric sites details with params: {0}".format(params), "DEBUG")
                fabric_sites_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )
                self.log("Retrieved fabric sites details: {0}".format(fabric_sites_details), "INFO")
                final_fabric_sites.extend(fabric_sites_details)
                params.clear()
            self.log("Using component-specific filters for API call.", "INFO")
        else:
            # Execute API call to retrieve Interfaces details
            fabric_sites_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )
            self.log("Retrieved fabric sites details: {0}".format(fabric_sites_details), "INFO")
            final_fabric_sites.extend(fabric_sites_details)

        # Modify Fabric VLAN's details using temp_spec
        fabric_site_temp_spec = self.fabric_site_temp_spec()
        site_details = self.modify_parameters(
            fabric_site_temp_spec, final_fabric_sites
        )
        modified_fabric_site_details = {}
        modified_fabric_site_details['fabric_sites'] = site_details

        self.log(
            "Modified Fabric Site(s) details: {0}".format(
                modified_fabric_site_details
            ),
            "INFO",
        )

        return modified_fabric_site_details

    def get_fabric_zones_from_ccc(self, network_element, component_specific_filters=None):
        """
        Retrieves fabric zones based on the provided network element and component-specific filters.
        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving fabric zones.
            component_specific_filters (list, optional): A list of dictionaries containing filters for fabric zones.

        Returns:
            dict: A dictionary containing the modified details of fabric zones.
        """

        self.log(
            "Starting to retrieve fabric zones using network element: {0}".format(
                network_element
            ),
            "DEBUG",
        )
        # Extract API family and function from network_element
        final_fabric_zones = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "Getting sda fabric zones using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {}
        # Execute API call to retrieve fabric zone details
        if component_specific_filters:
            self.log("Using component-specific filters for API call.", "DEBUG")
            for filter_param in component_specific_filters:
                self.log("Processing filter parameter: {0}".format(filter_param), "DEBUG")
                for key, value in filter_param.items():
                    if key == "site_name_hierarchy":
                        site_id = self.get_site_id(value)
                        if site_id:
                            self.log(
                                "Mapped site name hierarchy '{0}' to site ID '{1}'.".format(
                                    value, site_id
                                ),
                                "DEBUG"
                            )
                            params["siteId"] = site_id
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )
                fabric_zones_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )
                self.log("Retrieved fabric zones details: {0}".format(fabric_zones_details), "INFO")
                final_fabric_zones.extend(fabric_zones_details)
                params.clear()
        else:
            # Execute API call to retrieve Interfaces details
            fabric_zones_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )
            self.log("Retrieved fabric zones details: {0}".format(fabric_zones_details), "INFO")
            final_fabric_zones.extend(fabric_zones_details)

        # Modify Fabric Zone's details using temp_spec
        fabric_zone_temp_spec = self.fabric_zone_temp_spec()
        zone_details = self.modify_parameters(
            fabric_zone_temp_spec, final_fabric_zones
        )
        modified_fabric_zone_details = {}
        modified_fabric_zone_details['fabric_sites'] = zone_details

        self.log(
            "Modified Fabric Zone(s) details: {0}".format(
                modified_fabric_zone_details
            ),
            "INFO",
        )

        return modified_fabric_zone_details

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
        self.log("Component specific filters provided: {0}".format(component_specific_filters), "DEBUG")
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )

        # If components_list is empty, default to all supported components
        if not components_list:
            self.log("No components specified; processing all supported components.", "INFO")
            components_list = list(module_supported_network_elements.keys())

        self.log("Keys in module_supported_network_elements: {0}".format(module_supported_network_elements.keys()), "DEBUG")
        self.log("Initializing final configuration list", "DEBUG")
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
    ccc_brownfield_fabric_sites_zones_playbook_generator = BrownFieldFabricSiteZonePlaybookGenerator(module)
    if (
        ccc_brownfield_fabric_sites_zones_playbook_generator.compare_dnac_versions(
            ccc_brownfield_fabric_sites_zones_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_brownfield_fabric_sites_zones_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for fabric_sites_zones_workflow_manager Module. Supported versions start from '2.3.7.9' onwards. "
            "Version '2.3.7.9' introduces APIs for retrieving existing fabric sites and zones "
            "and respective authentication profiles for the sites and zones configuration "
            "in the Cisco Catalyst Center."
            .format(
                ccc_brownfield_fabric_sites_zones_playbook_generator.get_ccc_version()
            )
        )
        ccc_brownfield_fabric_sites_zones_playbook_generator.set_operation_result(
            "failed", False, ccc_brownfield_fabric_sites_zones_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_brownfield_fabric_sites_zones_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_brownfield_fabric_sites_zones_playbook_generator.supported_states:
        ccc_brownfield_fabric_sites_zones_playbook_generator.status = "invalid"
        ccc_brownfield_fabric_sites_zones_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_brownfield_fabric_sites_zones_playbook_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_brownfield_fabric_sites_zones_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_brownfield_fabric_sites_zones_playbook_generator.validated_config:
        ccc_brownfield_fabric_sites_zones_playbook_generator.reset_values()
        ccc_brownfield_fabric_sites_zones_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_brownfield_fabric_sites_zones_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_brownfield_fabric_sites_zones_playbook_generator.result)


if __name__ == "__main__":
    main()

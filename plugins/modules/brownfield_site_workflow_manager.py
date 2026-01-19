#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbooks for Site Workflow Manager from Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Vidhya Rathinam"

DOCUMENTATION = r"""
---
module: brownfield_site_workflow_manager
short_description: Generate YAML playbook for 'site_workflow_manager' module.
description:
- Generates YAML configurations compatible with the `site_workflow_manager`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the site hierarchy (areas, buildings, floors)
  configured on the Cisco Catalyst Center.
version_added: 6.17.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Vidhya Rathinam (@virathin)
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
    - A list of filters for generating YAML playbook compatible with the `site_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all sites and all supported site types.
          - This mode discovers all managed sites in Cisco Catalyst Center and extracts all supported configurations.
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
          a default file name  "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "site_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
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
              - Areas "areas"
              - Buildings "buildings"
              - Floors "floors"
            - If not specified, all components are included.
            - For example, ["areas", "buildings", "floors"].
            type: list
            elements: str
          areas:
            description:
            - Areas to filter sites by site name or parent site name.
            type: list
            elements: dict
            suboptions:
              site_name:
                description:
                - Site name to filter areas by site name.
                type: str
              parent_site_name:
                description:
                - Parent site name to filter areas by parent site name.
                type: str
          buildings:
            description:
            - Buildings to filter sites by site name or parent site name.
            type: list
            elements: dict
            suboptions:
              site_name:
                description:
                - Site name to filter buildings by site name.
                type: str
              parent_site_name:
                description:
                - Parent site name to filter buildings by parent site name.
                type: str
          floors:
            description:
            - Floors to filter sites by site name, parent site name, or RF model.
            type: list
            elements: dict
            suboptions:
              site_name:
                description:
                - Site name to filter floors by site name.
                type: str
              parent_site_name:
                description:
                - Parent site name to filter floors by parent site name.
                type: str
              rf_model:
                description:
                - RF model to filter floors by RF model type.
                type: str
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - sites.Sites.get_site_v2
- Paths used are
    - GET /dna/intent/api/v1/site
    - GET /dna/intent/api/v2/site
"""

EXAMPLES = r"""
- name: Auto-generate YAML Configuration for all site components which
     includes areas, buildings, and floors.
  cisco.dnac.brownfield_site_workflow_manager:
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
  cisco.dnac.brownfield_site_workflow_manager:
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
      - file_path: "/tmp/catc_site_components_config.yaml"
- name: Generate YAML Configuration with specific area components only
  cisco.dnac.brownfield_site_workflow_manager:
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
      - file_path: "/tmp/catc_site_components_config.yaml"
        component_specific_filters:
          components_list: ["areas"]
- name: Generate YAML Configuration with specific building components only
  cisco.dnac.brownfield_site_workflow_manager:
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
      - file_path: "/tmp/catc_site_components_config.yaml"
        component_specific_filters:
          components_list: ["buildings"]
- name: Generate YAML Configuration with specific floor components only
  cisco.dnac.brownfield_site_workflow_manager:
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
      - file_path: "/tmp/catc_site_components_config.yaml"
        component_specific_filters:
          components_list: ["floors"]
- name: Generate YAML Configuration for areas with site name filter
  cisco.dnac.brownfield_site_workflow_manager:
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
      - file_path: "/tmp/catc_site_components_config.yaml"
        component_specific_filters:
          components_list: ["areas"]
          areas:
            - site_name: "Global/USA"
            - site_name: "Global/Europe"
- name: Generate YAML Configuration for buildings and floors with multiple filters
  cisco.dnac.brownfield_site_workflow_manager:
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
      - file_path: "/tmp/catc_site_components_config.yaml"
        component_specific_filters:
          components_list: ["buildings", "floors"]
          buildings:
            - site_name: "Global/USA/San Jose/Building1"
            - site_name: "Global/USA/San Jose/Building2"
          floors:
            - parent_site_name: "Global/USA/San Jose/Building1"
            - rf_model: "Cubes And Walled Offices"
"""


RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
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


class SitePlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for site hierarchy deployed within the Cisco Catalyst Center using the GET APIs.
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
        self.module_name = "site_workflow_manager"

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

    def get_workflow_elements_schema(self):
        """
        Description:
            Constructs and returns a structured mapping for managing various site elements
            such as areas, buildings, and floors. This mapping includes associated filters,
            temporary specification functions, API details, and fetch function references
            used in the site workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods.

        Return:
            dict: A dictionary with site element configurations.
        """

        return {
            "network_elements": {
                "areas": {
                    "filters": ["site_name", "parent_site_name"],
                    "reverse_mapping_function": self.area_temp_spec,
                    "api_function": "get_site_v2",
                    "api_family": "sites",
                    "get_function_name": self.get_areas_configuration,
                },
                "buildings": {
                    "filters": ["site_name", "parent_site_name"],
                    "reverse_mapping_function": self.building_temp_spec,
                    "api_function": "get_site_v2",
                    "api_family": "sites",
                    "get_function_name": self.get_buildings_configuration,
                },
                "floors": {
                    "filters": ["site_name", "parent_site_name", "rf_model"],
                    "reverse_mapping_function": self.floor_temp_spec,
                    "api_function": "get_site_v2",
                    "api_family": "sites",
                    "get_function_name": self.get_floors_configuration,
                },
            },
            "global_filters": [],
        }

    def area_temp_spec(self):
        """
        Constructs a temporary specification for areas.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of area attributes.
        """

        self.log("Generating temporary specification for areas.", "DEBUG")
        area = OrderedDict(
            {
                "area": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "name": {"type": "str", "source_key": "name"},
                            "parent_name": {"type": "str", "source_key": "parentName"},
                        }
                    ),
                },
                "site_type": {"type": "str", "default": "area"},
            }
        )
        return area

    def building_temp_spec(self):
        """
        Constructs a temporary specification for buildings.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of building attributes.
        """

        self.log("Generating temporary specification for buildings.", "DEBUG")
        building = OrderedDict(
            {
                "building": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "name": {"type": "str", "source_key": "name"},
                            "parent_name": {"type": "str", "source_key": "parentName"},
                            "address": {"type": "str", "source_key": "address"},
                            "latitude": {"type": "float", "source_key": "latitude"},
                            "longitude": {"type": "float", "source_key": "longitude"},
                            "country": {"type": "str", "source_key": "country"},
                        }
                    ),
                },
                "site_type": {"type": "str", "default": "building"},
            }
        )
        return building

    def floor_temp_spec(self):
        """
        Constructs a temporary specification for floors.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of floor attributes.
        """

        self.log("Generating temporary specification for floors.", "DEBUG")
        floor = OrderedDict(
            {
                "floor": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "name": {"type": "str", "source_key": "name"},
                            "parent_name": {"type": "str", "source_key": "parentName"},
                            "rf_model": {"type": "str", "source_key": "rfModel"},
                            "length": {"type": "float", "source_key": "length"},
                            "width": {"type": "float", "source_key": "width"},
                            "height": {"type": "float", "source_key": "height"},
                            "floor_number": {
                                "type": "int",
                                "source_key": "floorNumber",
                            },
                            "units_of_measure": {
                                "type": "str",
                                "source_key": "unitsOfMeasure",
                            },
                        }
                    ),
                },
                "site_type": {"type": "str", "default": "floor"},
            }
        )
        return floor

    def get_areas_configuration(self, network_element, component_specific_filters=None):
        """
        Retrieves areas based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving areas.
            component_specific_filters (list, optional): A list of dictionaries containing filters for areas.

        Returns:
            dict: A dictionary containing the modified details of areas.
        """

        self.log(
            "Starting to retrieve areas with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        final_areas = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting areas using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {"type": "area"}

        if component_specific_filters:
            for filter_param in component_specific_filters:
                self.log(
                    "Processing filter parameter: {0}".format(filter_param), "DEBUG"
                )
                for key, value in filter_param.items():
                    if key == "site_name":
                        params["name"] = value
                    elif key == "parent_site_name":
                        params["name_hierarchy"] = value
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )

                area_details = self.execute_get_with_pagination(
                    api_family, api_function, params, use_strings=True
                )
                self.log("Retrieved area details: {0}".format(area_details), "INFO")
                final_areas.extend(area_details)
                params = {"type": "area"}
        else:
            area_details = self.execute_get_with_pagination(
                api_family, api_function, params, use_strings=True
            )
            self.log("Retrieved area details: {0}".format(area_details), "INFO")
            final_areas.extend(area_details)

        # Modify area details using temp_spec
        area_temp_spec = self.area_temp_spec()
        areas_details = self.modify_parameters(area_temp_spec, final_areas)
        modified_areas_details = {}
        modified_areas_details["areas"] = areas_details

        self.log(
            "Modified area details: {0}".format(modified_areas_details),
            "INFO",
        )

        return modified_areas_details

    def get_buildings_configuration(
        self, network_element, component_specific_filters=None
    ):
        """
        Retrieves buildings based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving buildings.
            component_specific_filters (list, optional): A list of dictionaries containing filters for buildings.

        Returns:
            dict: A dictionary containing the modified details of buildings.
        """

        self.log(
            "Starting to retrieve buildings with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        final_buildings = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting buildings using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {"type": "building"}

        if component_specific_filters:
            for filter_param in component_specific_filters:
                for key, value in filter_param.items():
                    if key == "site_name":
                        params["name"] = value
                    elif key == "parent_site_name":
                        params["name_hierarchy"] = value
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )

                building_details = self.execute_get_with_pagination(
                    api_family, api_function, params, use_strings=True
                )
                self.log(
                    "Retrieved building details: {0}".format(building_details), "INFO"
                )
                final_buildings.extend(building_details)
                params = {"type": "building"}
        else:
            building_details = self.execute_get_with_pagination(
                api_family, api_function, params, use_strings=True
            )
            self.log("Retrieved building details: {0}".format(building_details), "INFO")
            final_buildings.extend(building_details)

        # Modify building details using temp_spec
        building_temp_spec = self.building_temp_spec()
        buildings_details = self.modify_parameters(building_temp_spec, final_buildings)
        modified_buildings_details = {}
        modified_buildings_details["buildings"] = buildings_details

        self.log(
            "Modified building details: {0}".format(modified_buildings_details),
            "INFO",
        )

        return modified_buildings_details

    def get_floors_configuration(
        self, network_element, component_specific_filters=None
    ):
        """
        Retrieves floors based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving floors.
            component_specific_filters (list, optional): A list of dictionaries containing filters for floors.

        Returns:
            dict: A dictionary containing the modified details of floors.
        """

        self.log(
            "Starting to retrieve floors with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        final_floors = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting floors using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {"type": "floor"}

        if component_specific_filters:
            for filter_param in component_specific_filters:
                for key, value in filter_param.items():
                    if key == "site_name":
                        params["name"] = value
                    elif key == "parent_site_name":
                        params["name_hierarchy"] = value
                    elif key == "rf_model":
                        # RF model filtering will be done post-retrieval
                        pass
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )

                floor_details = self.execute_get_with_pagination(
                    api_family, api_function, params, use_strings=True
                )
                self.log("Retrieved floor details: {0}".format(floor_details), "INFO")

                # Filter by RF model if specified
                if "rf_model" in filter_param:
                    rf_model = filter_param["rf_model"]
                    filtered_floors = [
                        floor
                        for floor in floor_details
                        if floor.get("rfModel") == rf_model
                    ]
                    final_floors.extend(filtered_floors)
                else:
                    final_floors.extend(floor_details)

                params = {"type": "floor"}
        else:
            floor_details = self.execute_get_with_pagination(
                api_family, api_function, params, use_strings=True
            )
            self.log("Retrieved floor details: {0}".format(floor_details), "INFO")
            final_floors.extend(floor_details)

        # Modify floor details using temp_spec
        floor_temp_spec = self.floor_temp_spec()
        floors_details = self.modify_parameters(floor_temp_spec, final_floors)
        modified_floors_details = {}
        modified_floors_details["floors"] = floors_details

        self.log(
            "Modified floor details: {0}".format(modified_floors_details),
            "INFO",
        )

        return modified_floors_details

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.

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
                "Auto-discovery mode enabled - will process all sites and all features",
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
            self.log(
                "Auto-discovery mode: Overriding any provided filters to retrieve all sites and all features",
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

            global_filters = {}
            component_specific_filters = {}
        else:
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = (
                yaml_config_generator.get("component_specific_filters") or {}
            )

        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        self.log("Determining components list for processing", "DEBUG")
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )
        self.log("Components to process: {0}".format(components_list), "DEBUG")

        self.log(
            "Initializing final configuration list and operation summary tracking",
            "DEBUG",
        )
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

        Args:
            config (dict): The configuration data for the site elements.
            state (str): The desired state of the site elements ('gathered').
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        # Set generate_all_configurations after validation
        self.generate_all_configurations = config.get(
            "generate_all_configurations", False
        )
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
        self.msg = "Successfully collected all parameters from the playbook for Site operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the gather operations for site configurations in the Cisco Catalyst Center.
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
    # Define the specification for the module's arguments
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
    # Initialize the SitePlaybookGenerator object with the module
    ccc_site_playbook_generator = SitePlaybookGenerator(module)
    if (
        ccc_site_playbook_generator.compare_dnac_versions(
            ccc_site_playbook_generator.get_ccc_version(), "2.3.7.6"
        )
        < 0
    ):
        ccc_site_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Site Workflow Manager Module. Supported versions start from '2.3.7.6' onwards. "
            "Version '2.3.7.6' introduces APIs for retrieving site hierarchy including "
            "areas, buildings, and floors from the Catalyst Center".format(
                ccc_site_playbook_generator.get_ccc_version()
            )
        )
        ccc_site_playbook_generator.set_operation_result(
            "failed", False, ccc_site_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_site_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_site_playbook_generator.supported_states:
        ccc_site_playbook_generator.status = "invalid"
        ccc_site_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_site_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_site_playbook_generator.validate_input().check_return_status()
    config = ccc_site_playbook_generator.validated_config

    # Iterate over the validated configuration parameters
    for config in ccc_site_playbook_generator.validated_config:
        ccc_site_playbook_generator.reset_values()
        ccc_site_playbook_generator.get_want(config, state).check_return_status()
        ccc_site_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_site_playbook_generator.result)


if __name__ == "__main__":
    main()

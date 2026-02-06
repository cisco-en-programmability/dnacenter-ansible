#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Access Point Location Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: brownfield_accesspoint_location_playbook_generator
short_description: >-
  Generate YAML configurations playbook for
  'accesspoint_location_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the
    'accesspoint_location_workflow_manager' module, reducing
    the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
  - Supports complete brownfield infrastructure discovery by
    collecting all access point locations from Cisco Catalyst Center.
  - Enables targeted extraction using filters (site hierarchies,
    planned access points, real access points, AP models, or MAC addresses).
  - Auto-generates timestamped YAML filenames when file path not
    specified.
version_added: 6.45.0
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
      - A list of filters for generating YAML playbook compatible
        with the 'brownfield_accesspoint_location_playbook_generator'
        module.
      - Filters specify which components to include in the YAML
        configuration file.
      - Either 'generate_all_configurations' or 'global_filters'
        must be specified to identify target access point locations.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML
            configurations for all access point locations and all
            supported features.
          - This mode discovers all floor locations with access points
            in Cisco Catalyst Center and extracts all supported
            configurations.
          - When enabled, the config parameter becomes optional
            and will use default values if not provided.
          - A default filename will be generated automatically
            if file_path is not specified.
          - This is useful for complete brownfield infrastructure
            discovery and documentation.
          - Any provided global_filters will be IGNORED in this
            mode.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current
            working directory with a default file name
            'accesspoint_location_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml'.
          - For example,
            'accesspoint_location_workflow_manager_playbook_2025-04-22_21-43-26.yml'.
          - Supports both absolute and relative file paths.
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML
            configuration file.
          - These filters apply to all components unless overridden
            by component-specific filters.
          - At least one filter type must be specified to identify
            target access point locations.
          - Filter priority (highest to lowest) is site_list,
            planned_accesspoint_list, real_accesspoint_list,
            accesspoint_model_list, mac_address_list.
          - Only the highest priority filter with valid data will
            be processed.
        type: dict
        required: false
        suboptions:
          site_list:
            description:
              - List of floor site hierarchies to extract access point
                location configurations from.
              - HIGHEST PRIORITY - Used first if provided with
                valid data.
              - Site paths must match floor locations registered
                in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all floor locations.
              - Example ["Global/USA/SAN JOSE/SJ_BLD20/FLOOR1",
                "Global/USA/SAN JOSE/SJ_BLD20/FLOOR2"]
              - Module will fail if any specified site does not
                exist in Catalyst Center.
            type: list
            elements: str
            required: false
          planned_accesspoint_list:
            description:
              - List of planned access point names to filter locations.
              - MEDIUM-HIGH PRIORITY - Only used if site_list
                is not provided.
              - Retrieves all floor locations containing any of
                the specified planned access points.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all planned
                access points.
              - Example ["test_ap_location", "test_ap2_location"]
            type: list
            elements: str
            required: false
          real_accesspoint_list:
            description:
              - List of real (provisioned) access point names to
                filter locations.
              - MEDIUM PRIORITY - Only used if neither
                site_list nor planned_accesspoint_list are
                provided.
              - Retrieves all floor locations containing any of
                the specified real access points.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all real
                access points.
              - Example ["Test_ap", "AP687D.B402.1614-AP-Test6"]
            type: list
            elements: str
            required: false
          accesspoint_model_list:
            description:
              - List of access point models to filter locations.
              - MEDIUM-LOW PRIORITY - Only used if higher priority
                filters are not provided.
              - Retrieves all floor locations containing any of
                the specified AP models.
              - Case-sensitive and must be exact matches.
              - Example ["AP9120E", "AP9130E"]
            type: list
            elements: str
            required: false
          mac_address_list:
            description:
              - List of access point MAC addresses to filter locations.
              - LOWEST PRIORITY - Only used if all other filters
                are not provided.
              - Retrieves all floor locations containing access points
                with the specified MAC addresses.
              - Case-sensitive and must be exact matches.
              - Example ["a4:88:73:d4:dd:80", "a4:88:73:d4:dd:81"]
            type: list
            elements: str
            required: false
requirements:
  - dnacentersdk >= 2.10.10
  - python >= 3.9
notes:
  - This module utilizes the following SDK methods
    site_design.get_planned_access_points_positions
    site_design.get_access_points_positions
    site_design.get_sites
  - The following API paths are used
    GET /dna/intent/api/v2/floors/${floorId}/plannedAccessPointPositions
    GET /dna/intent/api/v1/sites
    GET /dna/intent/api/v2/floors/${floorId}/accessPointPositions
  - Minimum Cisco Catalyst Center version required is 3.1.3.0 for
    YAML playbook generation support.
  - Filter priority hierarchy ensures only one filter type is
    processed per execution.
  - Module creates YAML file compatible with
    'accesspoint_location_workflow_manager' module for
    automation workflows.
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Access Point Location from all floor
  cisco.dnac.brownfield_accesspoint_location_playbook_generator:
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

- name: Auto-generate YAML Configuration for all Access Point Location with custom file path
  cisco.dnac.brownfield_accesspoint_location_playbook_generator:
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
      - file_path: "tmp/brownfield_accesspoint_location_workflow_playbook.yml"
        generate_all_configurations: true

- name: Generate YAML Configuration with file path based on site list filters
  cisco.dnac.brownfield_accesspoint_location_playbook_generator:
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
      - file_path: "tmp/brownfield_accesspoint_location_workflow_playbook_site_base.yml"
        global_filters:
          site_list:
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR1
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR2

- name: Generate YAML Configuration with file path based on planned access point list
  cisco.dnac.brownfield_accesspoint_location_playbook_generator:
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
      - global_filters:
          planned_accesspoint_list:
            - test_ap_location
            - test_ap2_location

- name: Generate YAML Configuration with file path based on real access point list
  cisco.dnac.brownfield_accesspoint_location_playbook_generator:
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
      - global_filters:
          real_accesspoint_list:
            - Test_ap
            - AP687D.B402.1614-AP-Test6

- name: Generate YAML Configuration with default file path based on access point model list
  cisco.dnac.brownfield_accesspoint_location_playbook_generator:
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
      - global_filters:
          accesspoint_model_list:
            - AP9120E
            - AP9130E

- name: Generate YAML Configuration with default file path based on MAC Address list
  cisco.dnac.brownfield_accesspoint_location_playbook_generator:
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
      - global_filters:
          mac_address_list:
            - a4:88:73:d4:dd:80
            - a4:88:73:d4:dd:81
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: >-
    A dictionary with the response returned by the Cisco Catalyst
    Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "YAML config generation Task succeeded for module
         'accesspoint_location_workflow_manager'.": {
            "file_path":
             "tmp/brownfield_accesspoint_location_workflow_playbook_templatebase.yml"
          }
        },
      "msg": {
        "YAML config generation Task succeeded for module
         'accesspoint_location_workflow_manager'.": {
            "file_path":
             "tmp/brownfield_accesspoint_location_workflow_playbook_templatebase.yml"
          }
        }
    }

# Case_2: Error Scenario
response_2:
  description: >-
    A string with the response returned by the Cisco Catalyst
    Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "No configurations or components to process for
                   module 'accesspoint_location_workflow_manager'.
                   Verify input filters or configuration.",
      "msg": "No configurations or components to process for module
              'accesspoint_location_workflow_manager'.
              Verify input filters or configuration."
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
import copy

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


class AccesspointLocationPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center
    using the GET APIs.
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        """
        Initialize an instance of the class.

        Parameters:
            module: The module associated with the class instance.

        Returns:
            The method does not return a value.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_name = "accesspoint_location_workflow_manager"
        self.module_schema = self.get_workflow_elements_schema()
        self.log("Initialized AccesspointLocationPlaybookGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False
        self.have["all_floor"], self.have["filtered_floor"], self.have["all_detailed_config"] = [], [], []
        self.have["all_config"], self.have["planned_aps"], self.have["real_aps"] = [], [], []

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
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "global_filters": {"type": "dict", "elements": "dict", "required": False},
        }

        allowed_keys = set(temp_spec.keys())

        # Validate that only allowed keys are present in the configuration
        for config_item in self.config:
            if not isinstance(config_item, dict):
                self.msg = "Configuration item must be a dictionary, got: {0}".format(type(config_item).__name__)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Check for invalid keys
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            if invalid_keys:
                self.msg = (
                    "Invalid parameters found in playbook configuration: {0}. "
                    "Only the following parameters are allowed: {1}. "
                    "Please remove the invalid parameters and try again.".format(
                        list(invalid_keys), list(allowed_keys)
                    )
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

        self.validate_minimum_requirements(self.config)
        self.log("Validating configuration parameters against the expected schema: {0}".format(temp_spec), "DEBUG")

        # Import validate_list_of_dicts function here to avoid circular imports
        # from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = f"Successfully validated playbook configuration parameters using 'validated_input': {valid_temp}"
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def validate_params(self, config):
        """
        Validates individual configuration parameters for brownfield access point location generation.

        Parameters:
            config (dict): Configuration parameters

        Returns:
            self: Current instance with validation status updated.
        """
        self.log("Starting validation of configuration parameters", "DEBUG")

        # Check for required parameters
        if not config:
            self.msg = "Configuration cannot be empty"
            self.status = "failed"
            return self

        # Validate file_path if provided
        file_path = config.get("file_path")
        if file_path:
            import os
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                try:
                    os.makedirs(directory, exist_ok=True)
                    self.log("Created directory: {0}".format(directory), "INFO")
                except Exception as e:
                    self.msg = "Cannot create directory for file_path: {0}. Error: {1}".format(directory, str(e))
                    self.status = "failed"
                    return self

        self.log("Configuration parameters validation completed successfully", "DEBUG")
        self.status = "success"
        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        This method prepares the parameters required for retrieving and managing
        access point location such as accesspoint name, model, position and radio
        in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.

        Parameters:
            config (dict): The configuration data for the access point location elements.
            state (str): The desired state of the network elements ('gathered').

        Returns:
            self: The current instance of the class with updated 'want' attributes.
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
                self.pprint(want["yaml_config_generator"])
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for access point location operations."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Retrieves the current state of access point location from the Cisco Catalyst Center.
        This method fetches the existing configurations for Access Point position
        such as accesspoint name, model, position and radio in the Cisco Catalyst Center.
        It logs detailed information about the retrieval process and updates the
        current state attributes accordingly.

        Parameters:
            config (dict): The configuration data for the access point location elements.

        Returns:
            object: An instance of the class with updated attributes:
                self.have: A dictionary containing the current state of access point location.
                self.msg: A message describing the retrieval result.
                self.status: The status of the retrieval (either "success" or "failed").
        """
        self.log(
            "Retrieving current state of access point location from Cisco Catalyst Center.",
            "INFO",
        )

        if config and isinstance(config, dict):
            if config.get("generate_all_configurations", False):
                self.log("Collecting all access point location details", "INFO")
                self.collect_all_accesspoint_location_list()
                if not self.have.get("all_config"):
                    self.msg = "No existing access point locations found in Cisco Catalyst Center."
                    self.status = "success"
                    return self

                self.log("All Configurations collected successfully : {0}".format(
                    self.pprint(self.have.get("all_config"))), "INFO")

            global_filters = config.get("global_filters")
            if global_filters:
                self.log(f"Collecting access point location details based on global filters: {global_filters}", "INFO")
                self.collect_all_accesspoint_location_list()

                site_list = global_filters.get("site_list", [])
                if site_list:
                    self.log(f"Collecting access point location details for site list: {site_list}", "INFO")

                    if len(site_list) == 1 and site_list[0].lower() == "all":
                        return self
                    else:
                        missing_floors = []
                        for floor_name in site_list:
                            self.log(f"Check access point location details exist for site: {floor_name}", "INFO")
                            floor_exist = self.find_dict_by_key_value(
                                self.have["filtered_floor"], "floor_site_hierarchy", floor_name)

                            if not floor_exist:
                                missing_floors.append(floor_name)
                                self.log(f"Given floor site hierarchy not exist for the : {floor_name}", "WARNING")

                        if missing_floors:
                            self.msg = f"The following floor site hierarchies do not exist: {missing_floors}."
                            self.fail_and_exit(self.msg)

                planned_ap_list = global_filters.get("planned_accesspoint_list", [])
                if planned_ap_list:
                    self.log(f"Collecting access point location details for planned access point list: {planned_ap_list}",
                             "INFO")

                    if len(planned_ap_list) == 1 and planned_ap_list[0].lower() == "all":
                        return self
                    else:
                        missing_planned_aps = []
                        for planned_ap in planned_ap_list:
                            self.log(f"Check planned access point exist for : {planned_ap}", "INFO")
                            ap_exist = self.find_dict_by_key_value(
                                self.have["all_detailed_config"], "accesspoint_name", planned_ap)

                            if not ap_exist or ap_exist.get("accesspoint_type") == "real":
                                missing_planned_aps.append(planned_ap)
                                self.log(f"Given planned access point not exist : {planned_ap}", "WARNING")

                        if missing_planned_aps:
                            self.msg = f"The following planned access points do not exist: {missing_planned_aps}."
                            self.fail_and_exit(self.msg)

                real_ap_list = global_filters.get("real_accesspoint_list", [])
                if real_ap_list:
                    self.log(f"Collecting access point location details for real access point list: {real_ap_list}",
                             "INFO")

                    if len(real_ap_list) == 1 and real_ap_list[0].lower() == "all":
                        return self
                    else:
                        missing_real_aps = []
                        for real_ap in real_ap_list:
                            self.log(f"Check real access point exist for : {real_ap}", "INFO")
                            ap_exist = self.find_dict_by_key_value(
                                self.have["all_detailed_config"], "accesspoint_name", real_ap)

                            if not ap_exist or ap_exist.get("accesspoint_type") != "real":
                                missing_real_aps.append(real_ap)
                                self.log(f"Given real access point not exist : {real_ap}", "WARNING")

                        if missing_real_aps:
                            self.msg = f"The following real access points do not exist: {missing_real_aps}."
                            self.fail_and_exit(self.msg)

                model_list = global_filters.get("accesspoint_model_list", [])
                if model_list:
                    self.log(f"Collecting access point location details for access point model list: {model_list}",
                             "INFO")

                    if len(model_list) == 1 and model_list[0].lower() == "all":
                        return self
                    else:
                        missing_models = []
                        for model in model_list:
                            self.log(f"Check access point model exist for : {model}", "INFO")
                            aps_exist = self.find_multiple_dict_by_key_value(
                                self.have["all_detailed_config"], "accesspoint_model", model)

                            if not aps_exist:
                                missing_models.append(model)
                                self.log(f"Given access point model not exist : {model}", "WARNING")

                        if missing_models:
                            self.msg = f"The following access point models do not exist: {missing_models}."
                            self.fail_and_exit(self.msg)

                mac_list = global_filters.get("mac_address_list", [])
                if mac_list:
                    self.log(f"Collecting access point location details for MAC address list: {mac_list}",
                             "INFO")

                    if len(mac_list) == 1 and mac_list[0].lower() == "all":
                        return self
                    else:
                        missing_macs = []
                        for mac in mac_list:
                            self.log(f"Check MAC address exist for : {mac}", "INFO")
                            aps_exist = self.find_multiple_dict_by_key_value(
                                self.have["all_detailed_config"], "mac_address", mac)

                            if not aps_exist:
                                missing_macs.append(mac)
                                self.log(f"Given MAC address not exist : {mac}", "WARNING")

                        if missing_macs:
                            self.msg = f"The following MAC addresses do not exist: {missing_macs}."
                            self.fail_and_exit(self.msg)

        self.log("Current State (have): {0}".format(self.pprint(self.have)), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        return self

    def find_multiple_dict_by_key_value(self, data_list, key, value):
        """
        Find a dictionary in a list by a matching key-value pair.

        Parameters:
            data_list (list): List of dictionaries to search.
            key (str): The key to match in each dictionary.
            value (any): The value to match against the given key.

        Returns:
            list or None: The list of dictionaries that match the key-value pair, or None if not found.

        Description:
            Iterates through the list of dictionaries and returns the first dictionary
            where the specified key has the specified value. If no match is found, returns None.
        """
        if not isinstance(data_list, list):
            self.log("The 'data_list' parameter must be a list.", "ERROR")
            return None

        if not all(isinstance(item, dict) for item in data_list):
            self.log("All items in 'data_list' must be dictionaries.", "ERROR")
            return None

        self.log(f"Searching for key '{key}' with value '{value}' in a list of {len(data_list)} items.",
                 "DEBUG")
        matched_items = []
        for idx, item in enumerate(data_list):
            self.log(f"Checking item at index {idx}: {item}", "DEBUG")
            if item.get(key) == value:
                self.log(f"Match found at index {idx}: {item}", "DEBUG")
                matched_items.append(item)

        if matched_items:
            self.log(f"Total matches found: {len(matched_items)}", "DEBUG")
            return matched_items

        self.log(f"No matching item found for key '{key}' with value '{value}'.", "DEBUG")
        return None

    def get_workflow_elements_schema(self):
        """
        Returns the mapping configuration for access point location workflow manager.
        Returns:
            dict: A dictionary containing network elements and global filters configuration with validation rules.
        """
        return {
            "global_filters": {
                "site_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "planned_accesspoint_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "real_accesspoint_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_model_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "mac_address_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            }
        }

    def get_all_floors_from_sites(self):
        """
        Get all floors from the sites in Cisco Catalyst Center

        Returns:
            list: A list of all floors from the sites
        """
        self.log("Collecting all floors from the sites in Cisco Catalyst Center", "INFO")

        response_all = []
        offset = 1
        limit = 500
        api_family, api_function, param_key = "site_design", "get_sites", "type"
        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
        request_params = {param_key: "floor", "offset": offset, "limit": limit}

        while resync_retry_count > 0:
            self.log(f"Sending initial API request: Family='{api_family}', Function='{api_function}', Params={request_params}",
                     "DEBUG")

            response = self.execute_get_request(api_family, api_function, request_params)
            if not response:
                self.log("No data received from API (Offset={0}). Exiting pagination.".
                         format(request_params["offset"]), "DEBUG")
                break

            self.log("Received {0} site(s) from API (Offset={1}).".format(
                len(response.get("response")), request_params["offset"]), "DEBUG")
            floor_list = response.get("response")
            if floor_list and isinstance(floor_list, list):
                self.log("Processing floor list: {0}".format(
                    self.pprint(floor_list)), "DEBUG")
                required_data_list = []
                for floor_response in floor_list:
                    required_data = {
                        "id": floor_response.get("id"),
                        "floor_site_hierarchy": floor_response.get("nameHierarchy")
                    }
                    required_data_list.append(required_data)

            response_all.extend(required_data_list)

            if len(response.get("response")) < limit:
                self.log("Received less than limit ({0}) results, assuming last page. Exiting pagination.".
                         format(len(response.get("response"))), "DEBUG")
                break

            offset += limit
            request_params["offset"] = offset  # Increment offset for pagination
            self.log("Incrementing offset to {0} for next API request.".format(
                request_params["offset"]), "DEBUG")

            self.log(
                "Pauses execution for {0} seconds.".format(resync_retry_interval),
                "INFO",
            )
            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval

        if response_all:
            self.log("Total {0} site(s) retrieved for the floor type: {1}".format(
                len(response_all), self.pprint(response_all)), "DEBUG")
        else:
            self.log("No site details found for floor type", "WARNING")

        return response_all

    def get_access_point_position(self, floor_id, floor_name, ap_type=False):
        """
        Retrieve access point position information from Cisco Catalyst Center.

        Queries either planned or real access point positions based on operation context
        and access point configuration. Supports both planned and real position queries.

        Parameters:
            floor_id (str) - The ID of the floor where the access point is located.
            floor_name (str) - The name of the floor where the access point is located.
            ap_type (bool) - Flag to indicate if this is a recheck for deletion.

        Returns:
            dict - Planned or real access point position information

        Description:
            - Determines whether to query planned or real position based on operation type
            - Constructs appropriate API payload with floor ID and name
            - Executes position retrieval via Catalyst Center site design APIs
            - Handles both planned position queries and real position validation
        """
        self.log(
            f"Collecting planned access point position for site: {floor_name}.",
            "INFO",
        )

        self.log(
            f"Retrieving position for floor '{floor_name}', operation '{ap_type}'",
            "DEBUG"
        )

        payload = {
            "offset": 1,
            "limit": 500,
            "floor_id": floor_id
        }

        function_name = "get_planned_access_points_positions"
        if ap_type == "real":
            function_name = "get_access_points_positions"

        try:
            response = self.execute_get_request(
                "site_design", function_name, payload
            )
            if not response:
                msg = f"No response received from API for the {ap_type} access point and floor {floor_name}"
                self.log(msg, "WARNING")
                return None

            if not isinstance(response, dict):
                warning_msg = (
                    "Invalid response format for {0} position query - expected dict, "
                    "got: {1}".format(ap_type, type(response).__name__)
                )
                self.log(warning_msg, "WARNING")
                return None

            self.log(f"{ap_type} Access Point Position API Response: {response}", "DEBUG")
            return response.get("response")

        except Exception as e:
            self.msg = f'An error occurred during get {ap_type} AP position. '
            self.log(self.msg + str(e), "ERROR")
            return None

    def parse_accesspoint_position_for_floor(self, floor_id, floor_site_hierarchy,
                                             floor_response, ap_type=None):
        """
        Parse access point position information for a specific floor.

        Parameters:
            floor_id (str) - The ID of the floor
            floor_site_hierarchy (str) - The site hierarchy of the floor
            floor_response (dict) - The access point position response for the floor
            ap_type (str) - The type of access point position ("planned" or "real")

        Returns:
            list - A list of parsed access point position information
        """
        self.log(
            f"Parsing access point position for floor ID: {floor_id}, Site Hierarchy: {floor_site_hierarchy}.",
            "INFO",
        )

        if not floor_response or not isinstance(floor_response, list):
            self.log(
                f"No valid access point position data to parse for floor ID: {floor_id}.",
                "WARNING",
            )
            return None

        parsed_floor_data = {}
        parsed_positions = []
        parsed_detailed_data = []

        for ap_position in floor_response:
            parsed_data = {
                "accesspoint_name": ap_position.get("name"),
                "accesspoint_model": ap_position.get("type"),
                "position": {
                    "x_position": int(ap_position.get("position", {}).get("x")),
                    "y_position": int(ap_position.get("position", {}).get("y")),
                    "z_position": int(ap_position.get("position", {}).get("z"))
                }
            }
            if ap_position.get("macAddress"):
                parsed_data["mac_address"] = ap_position.get("macAddress").lower()
            radio_params = ap_position.get("radios", [])
            if radio_params and isinstance(radio_params, list):
                parsed_radios = []
                for radio in radio_params:
                    radio_bands = []
                    for each_band in radio.get("bands", []):
                        if each_band == 2.4:
                            radio_bands.append("2.4")
                        elif each_band == 5 or each_band == 5.0:
                            radio_bands.append("5")
                        elif each_band == 6 or each_band == 6.0:
                            radio_bands.append("6")

                    parsed_radio = {
                        "bands": [str(band) for band in radio_bands],
                        "channel": radio.get("channel"),
                        "tx_power": radio.get("txPower"),
                        "antenna": {
                            "antenna_name": radio.get("antenna", {}).get("name"),
                            "azimuth": radio.get("antenna", {}).get("azimuth"),
                            "elevation": radio.get("antenna", {}).get("elevation")
                        }
                    }
                    parsed_radios.append(parsed_radio)
                parsed_data["radios"] = parsed_radios

                # Append detailed data for filtered floor if applicable
                detailed_data = copy.deepcopy(parsed_data)
                detailed_data["floor_site_hierarchy"] = floor_site_hierarchy
                detailed_data["accesspoint_type"] = ap_type if ap_type else "planned"
                detailed_data["floor_id"] = floor_id
                detailed_data["id"] = ap_position.get("id")
                parsed_detailed_data.append(detailed_data)

            self.log(
                f"Added detailed access point data for floor ID: {floor_id}, Parse Data: {self.pprint(detailed_data)}.",
                "DEBUG",
            )
            parsed_positions.append(parsed_data)

        self.log(
            f"Parsed {len(parsed_positions)} access point positions for floor ID: {floor_id}.",
            "DEBUG",
        )

        self.log("Parsed Floor Data: {0}, Parsed detailed Positions: {1}".format(
            self.pprint(parsed_floor_data), self.pprint(parsed_detailed_data)), "DEBUG"
        )

        return parsed_positions, parsed_detailed_data

    def collect_all_accesspoint_location_list(self):
        """
        Get required details for the given access point location from Cisco Catalyst Center

        Returns:
            self - The current object with Filtered or all profile list
        """
        self.log(
            "Collecting all access point location details:", "INFO",
        )

        collect_all_config = []
        collect_planned_config = []
        collect_real_config = []
        filtered_floor = []
        collect_all_detailed_config = []

        floor_response = self.get_all_floors_from_sites()
        if floor_response and isinstance(floor_response, list):
            self.have["all_floor"] = floor_response
            self.log(
                "Total {0} floor(s) retrieved: {1}.".format(
                    len(self.have["all_floor"]),
                    self.pprint(self.have["all_floor"]),
                ),
                "DEBUG",
            )
            for floor in floor_response:
                floor_id = floor.get("id")
                floor_site_hierarchy = floor.get("floor_site_hierarchy")
                collect_each_floor_config = []

                planned_ap_response = self.get_access_point_position(floor_id, floor_site_hierarchy)
                if planned_ap_response:
                    self.log(
                        "Planned Access Point Position Response for floor '{0}': {1}".format(
                            floor_site_hierarchy, self.pprint(planned_ap_response)
                        ),
                        "DEBUG",
                    )
                    each_planned_config, planned_detailed_config = self.parse_accesspoint_position_for_floor(
                        floor_id, floor_site_hierarchy, planned_ap_response, ap_type="planned"
                    )
                    if each_planned_config and planned_detailed_config:
                        collect_each_floor_config.extend(each_planned_config)
                        collect_all_detailed_config.extend(planned_detailed_config)
                        planned_floor_data = {
                            "floor_site_hierarchy": floor_site_hierarchy,
                            "access_points": each_planned_config
                        }
                        collect_planned_config.append(planned_floor_data)

                real_ap_response = self.get_access_point_position(floor_id, floor_site_hierarchy, ap_type="real")
                if real_ap_response:
                    self.log(
                        "Real Access Point Position Response for floor '{0}': {1}".format(
                            floor_site_hierarchy, self.pprint(real_ap_response)
                        ),
                        "DEBUG",
                    )
                    each_real_config, real_detailed_config = self.parse_accesspoint_position_for_floor(
                        floor_id, floor_site_hierarchy, real_ap_response, ap_type="real"
                    )
                    if each_real_config and real_detailed_config:
                        collect_all_detailed_config.extend(real_detailed_config)
                        collect_each_floor_config.extend(each_real_config)
                        real_floor_data = {
                            "floor_site_hierarchy": floor_site_hierarchy,
                            "access_points": each_real_config
                        }
                        collect_real_config.append(real_floor_data)

                if collect_each_floor_config:
                    floor_data = {
                        "floor_site_hierarchy": floor_site_hierarchy,
                        "access_points": collect_each_floor_config
                    }
                    collect_all_config.append(floor_data)

                if planned_ap_response or real_ap_response:
                    filtered_floor.append({"floor_id": floor_id,
                                           "floor_site_hierarchy": floor_site_hierarchy})

            self.have["all_config"] = collect_all_config
            self.have["planned_aps"] = collect_planned_config
            self.have["real_aps"] = collect_real_config
            self.have["filtered_floor"] = filtered_floor
            self.have["all_detailed_config"] = collect_all_detailed_config

        else:
            self.log("No existing access points location found.", "WARNING")

        return self

    def get_diff_gathered(self):
        """
        Gathers access point location details from Cisco Catalyst Center and generates YAML playbook.

        Returns:
            self: Returns the current object with status and result set.
        """
        self.log("Starting brownfield access point location gathering process", "INFO")

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

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters,
        processes the data and writes the YAML content to a specified file.
        It dynamically handles multiple network elements and their respective filters.

        Parameters:
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
            self.log("Generate all access point location configurations from Catalyst Center", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("Initializing filter dictionaries", "DEBUG")
        # Set empty filters to retrieve everything
        global_filters = {}
        final_list = []
        if generate_all:
            self.log("Preparing to collect all configurations for access point location workflow.",
                     "DEBUG")
            final_list = self.have.get("all_config", [])
            self.log(f"All configurations collected for generate_all_configurations mode: {final_list}", "DEBUG")

        else:
            # we get ALL configurations
            self.log("Overriding any provided filters to retrieve based on global filters", "INFO")
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True",
                         "WARNING")

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            if global_filters:
                final_list = self.process_global_filters(global_filters)

        if not final_list:
            self.msg = "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name
            )
            self.set_operation_result("success", False, self.msg, "INFO")
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

    def process_global_filters(self, global_filters):
        """
        Process global filters for access point location workflow.

        Parameters:
            global_filters (dict): A dictionary containing global filter parameters.

        Returns:
            dict: A dictionary containing processed global filter parameters.
        """
        self.log(f"Processing global filters: {global_filters}", "DEBUG")

        site_list = global_filters.get("site_list")
        planned_accesspoint_list = global_filters.get("planned_accesspoint_list")
        real_accesspoint_list = global_filters.get("real_accesspoint_list")
        accesspoint_model_list = global_filters.get("accesspoint_model_list")
        mac_address_list = global_filters.get("mac_address_list")
        final_list = []
        keys_to_remove = ["accesspoint_type", "floor_id", "id", "floor_site_hierarchy"]

        if site_list and isinstance(site_list, list):
            self.log(f"Filtering access point location based on site_list: {site_list}",
                     "DEBUG")
            if len(site_list) == 1 and site_list[0].lower() == "all":
                if not self.have.get("planned_aps"):
                    self.log("No planned access points found in the catalyst center.", "WARNING")

                final_list = self.have.get("planned_aps", [])
            else:
                prepare_planned_list = []
                for floor in site_list:
                    ap_site_exist = self.find_multiple_dict_by_key_value(
                        self.have.get("all_config", []), "floor_site_hierarchy", floor)

                    if ap_site_exist:
                        prepare_planned_list.append(ap_site_exist[0])
                final_list = prepare_planned_list
            self.log(f"Access points location collected for site list {site_list}: {final_list}", "DEBUG")

        elif planned_accesspoint_list and isinstance(planned_accesspoint_list, list):
            self.log(f"Filtering access point location based on planned accesspoint list: {planned_accesspoint_list}",
                     "DEBUG")

            if len(planned_accesspoint_list) == 1 and planned_accesspoint_list[0].lower() == "all":
                if not self.have.get("planned_aps"):
                    self.log("No planned access points found in the catalyst center.", "WARNING")
                final_list = self.have.get("planned_aps", [])
            else:
                collected_aps = []
                for planned_ap in planned_accesspoint_list:
                    self.log(f"Check planned access point exist for : {planned_ap}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_detailed_config"], "accesspoint_name", planned_ap)

                    ap_exist = self.find_multiple_dict_by_key_value(
                        ap_exist, "accesspoint_type", "planned")

                    if ap_exist:
                        collected_aps.extend(ap_exist)
                        self.log(f"Given planned access point exist : {ap_exist}", "INFO")

                if not collected_aps:
                    self.log("No planned access points found matching the provided list.", "WARNING")
                    return None

                if self.have.get("filtered_floor"):
                    floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                    prepare_planned_list = []
                    for floor in floors:
                        ap_site_exist = self.find_multiple_dict_by_key_value(
                            collected_aps, "floor_site_hierarchy", floor)

                        if ap_site_exist:
                            for each_ap_site in ap_site_exist:
                                for key in keys_to_remove:
                                    del each_ap_site[key]

                            floor_data = {
                                "floor_site_hierarchy": floor,
                                "access_points": ap_site_exist
                            }
                            prepare_planned_list.append(floor_data)
                    final_list = prepare_planned_list
            self.log(f"Access points location collected for planned access point list {planned_accesspoint_list}: {final_list}",
                     "DEBUG")

        elif real_accesspoint_list and isinstance(real_accesspoint_list, list):
            self.log(f"Filtering access point location based on real accesspoint list: {real_accesspoint_list}",
                     "DEBUG")

            if len(real_accesspoint_list) == 1 and real_accesspoint_list[0].lower() == "all":
                if not self.have.get("real_aps"):
                    self.log("No real access points found in the catalyst center.", "WARNING")

                final_list = self.have.get("real_aps", [])
            else:
                collected_aps = []
                for real_ap in real_accesspoint_list:
                    self.log(f"Check real access point exist for : {real_ap}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_detailed_config"], "accesspoint_name", real_ap)

                    ap_exist = self.find_multiple_dict_by_key_value(
                        ap_exist, "accesspoint_type", "real")

                    if ap_exist:
                        collected_aps.extend(ap_exist)
                        self.log(f"Given real access point exist : {ap_exist}", "INFO")

                if not collected_aps:
                    self.log("No real access points found matching the provided list.", "WARNING")
                    return None

                if self.have.get("filtered_floor"):
                    floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                    prepare_real_list = []
                    for floor in floors:
                        ap_site_exist = self.find_multiple_dict_by_key_value(
                            collected_aps, "floor_site_hierarchy", floor)

                        if ap_site_exist:
                            for each_ap_site in ap_site_exist:
                                for key in keys_to_remove:
                                    del each_ap_site[key]

                            floor_data = {
                                "floor_site_hierarchy": floor,
                                "access_points": ap_site_exist
                            }
                            prepare_real_list.append(floor_data)
                    final_list = prepare_real_list
            self.log(f"Access points location collected for real access point list {real_accesspoint_list}: {final_list}",
                     "DEBUG")

        elif accesspoint_model_list and isinstance(accesspoint_model_list, list):
            self.log(f"Filtering access point location based on access point model list: {accesspoint_model_list}",
                     "DEBUG")
            if len(accesspoint_model_list) == 1 and accesspoint_model_list[0].lower() == "all":
                if not self.have.get("all_config"):
                    self.log("No access points location found in the catalyst center.", "WARNING")

                final_list = self.have.get("all_config", [])
            else:
                collected_aps = []
                for each_model in accesspoint_model_list:
                    self.log(f"Check access point model exist for : {each_model}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_detailed_config"], "accesspoint_model", each_model)
                    if ap_exist:
                        collected_aps.extend(ap_exist)
                        self.log(f"Given access point model exist : {ap_exist}", "INFO")
                if not collected_aps:
                    self.log("No access points found matching the provided model list.", "WARNING")
                    return None
                if self.have.get("filtered_floor"):
                    floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                    prepare_model_list = []
                    for floor in floors:
                        ap_site_exist = self.find_multiple_dict_by_key_value(
                            collected_aps, "floor_site_hierarchy", floor)

                        if ap_site_exist:
                            for each_ap_site in ap_site_exist:
                                for key in keys_to_remove:
                                    del each_ap_site[key]

                            floor_data = {
                                "floor_site_hierarchy": floor,
                                "access_points": ap_site_exist
                            }
                            prepare_model_list.append(floor_data)
                    final_list = prepare_model_list

            self.log(f"Access point location config collected for model list {accesspoint_model_list}: {final_list}",
                     "DEBUG")

        elif mac_address_list and isinstance(mac_address_list, list):
            self.log(f"Filtering access point location based on MAC address list: {mac_address_list}",
                     "DEBUG")
            collected_aps = []

            for each_mac in mac_address_list:
                normalized_mac = each_mac.lower()
                self.log(f"Check access point exist for MAC address : {normalized_mac}", "INFO")
                ap_exist = self.find_multiple_dict_by_key_value(
                    self.have["all_detailed_config"], "mac_address", normalized_mac)

                if ap_exist:
                    collected_aps.extend(ap_exist)
                    self.log(f"Given access point exist for MAC address : {ap_exist}", "INFO")

            if not collected_aps:
                self.log("No access points found matching the provided MAC address list.", "WARNING")
                return None

            if self.have.get("filtered_floor"):
                floors = {floor.get("floor_site_hierarchy") for floor in self.have.get("filtered_floor", [])}
                prepare_mac_list = []
                for floor in floors:
                    ap_site_exist = self.find_multiple_dict_by_key_value(
                        collected_aps, "floor_site_hierarchy", floor)

                    if ap_site_exist:
                        for each_ap_site in ap_site_exist:
                            for key in keys_to_remove:
                                del each_ap_site[key]

                        floor_data = {
                            "floor_site_hierarchy": floor,
                            "access_points": ap_site_exist
                        }
                        prepare_mac_list.append(floor_data)
                final_list = prepare_mac_list

            self.log(f"Access point location config collected for MAC address list {mac_address_list}: {final_list}",
                     "DEBUG")

        else:
            self.log("No specific global filters provided, processing all profiles", "DEBUG")

        if not final_list:
            self.log("No access points position found in the catalyst center.", "WARNING")
            return None

        return final_list


def main():
    """
    Main entry point for the Ansible brownfield access point location playbook generator module.

    This function serves as the primary orchestrator for generating YAML playbooks that capture
    the current state of access point location assignments in Cisco Catalyst Center. It performs
    comprehensive validation, infrastructure discovery, and templated playbook generation.

    Workflow:
        1. Module Initialization:
           - Define argument specifications for all module parameters
           - Initialize AnsibleModule instance with check mode support
           - Create AccesspointLocationPlaybookGenerator instance
           - Enable structured logging for debugging and audit trails

        2. Version Validation:
           - Verify Catalyst Center version meets minimum requirement (3.1.3.0+)
           - Fail gracefully with clear error message if version is unsupported
           - Log version information for troubleshooting

        3. State Validation:
           - Verify requested state is 'gathered' (only supported state)
           - Fail immediately if invalid state is requested
           - Log state information for audit purposes

        4. Input Validation:
           - Validate all module parameters (credentials, filters, paths)
           - Check filter parameter combinations and priorities
           - Verify file path permissions and writability
           - Fail with detailed error messages on validation failures

        5. Configuration Processing:
           - Iterate through each validated config item
           - Reset internal state between config items
           - For each config:
             a. Get desired state (get_want) - parse and validate filters
             b. Get current state (get_have) - query Catalyst Center APIs
             c. Apply state logic (get_diff_state_apply) - generate playbook
           - Check return status after each step

        6. Result Return:
           - Exit with JSON result containing operation status
           - Include file paths for generated playbooks
           - Provide user-friendly success/failure messages

    Args:
        None. Module parameters are obtained from Ansible module specification.

    Module Parameters (element_spec):
        Connection Parameters:
            - dnac_host (str, required): Catalyst Center hostname or IP address
            - dnac_port (str, optional): API port number (default: "443")
            - dnac_username (str, optional): Authentication username (default: "admin")
            - dnac_password (str, required): Authentication password (no_log: True)
            - dnac_verify (bool, optional): Verify SSL certificates (default: True)
            - dnac_version (str, optional): API version (default: "2.2.3.3")
            - dnac_debug (bool, optional): Enable SDK debug logging (default: False)

        Logging Parameters:
            - dnac_log_level (str, optional): Log level (default: "WARNING")
            - dnac_log_file_path (str, optional): Log file path (default: "dnac.log")
            - dnac_log_append (bool, optional): Append to log file (default: True)
            - dnac_log (bool, optional): Enable file logging (default: False)

        Operational Parameters:
            - validate_response_schema (bool, optional): Validate API responses (default: True)
            - dnac_api_task_timeout (int, optional): API task timeout in seconds (default: 1200)
            - dnac_task_poll_interval (int, optional): Task polling interval in seconds (default: 2)

        Configuration Parameters:
            - config (list of dict, required): Filter configuration for AP selection
            - state (str, optional): Operation state, must be "gathered" (default: "gathered")

    Returns:
        dict: Ansible module result dictionary via module.exit_json() with keys:
            - changed (bool): Always False (read-only operation)
            - response (dict): Operation result including:
                * Success message string
                * file_path (str): Absolute path to generated playbook
            - msg (str): User-facing summary message

    Side Effects:
        - Establishes HTTPS connection to Cisco Catalyst Center API
        - Performs multiple API queries to retrieve:
            * Access point details and configurations
            * Site hierarchy and location information
            * Floor maps and physical location data
        - Writes YAML playbook file to filesystem at yaml_file_path
        - Creates log entries at configured log level (DEBUG, INFO, WARNING, ERROR)
        - May create output directories if they don't exist

    Raises:
        AnsibleFailJson: Via module.fail_json() for any error condition:
            - Version Check Failures:
                * Catalyst Center version < 3.1.3.0
                * Unable to determine Catalyst Center version
            - State Validation Failures:
                * Unsupported state requested (not 'gathered')
            - Input Validation Failures:
                * Missing or invalid credentials
                * Invalid filter parameters or combinations
                * Unreachable file paths or permission errors
            - API Communication Failures:
                * Network connectivity issues
                * Authentication failures
                * API timeout or rate limiting
            - Data Processing Failures:
                * Schema validation errors
                * Unexpected API response formats
                * Missing required data in API responses

    Success Scenarios:
        Case 1: Access points found and playbook generated successfully
            {
                "changed": False,
                "response": {
                    "YAML config generation Task succeeded for module 'accesspoint_location_workflow_manager'.": {
                        "file_path": "/path/to/brownfield_accesspoint_location_workflow_playbook.yml"
                    }
                },
                "msg": "YAML configuration playbook generation completed successfully"
            }

        Case 2: No access points match the specified filters
            {
                "changed": False,
                "response": "No configurations or components to process for module "
                            "'accesspoint_location_workflow_manager'. Verify input filters "
                            "or configuration.",
                "msg": "No access point locations found matching the specified filter criteria"
            }

    Error Scenarios:
        - Version Mismatch:
            "The specified version '2.3.5.3' does not support the YAML Playbook generation "
            "for ACCESSPOINT LOCATION WORKFLOW Module. Supported versions start from '3.1.3.0' "
            "onwards."

        - Invalid State:
            "State 'merged' is invalid. Only 'gathered' state is supported for this module."

        - Authentication Failure:
            "Failed to authenticate with Cisco Catalyst Center at <host>:<port>. "
            "Verify credentials and network connectivity."

        - Invalid Filters:
            "Validation failed for config parameter: Cannot use both 'site_hierarchy' and "
            "'site_name_filter' simultaneously. Choose one filter method."

        - File Write Error:
            "Failed to write playbook to '<path>': Permission denied. Ensure the directory exists and is writable."

    Example Usage:
        This function is invoked automatically by Ansible when the module is executed.
        It should never be called directly by user code.

        Typical Ansible playbook usage:
        ```yaml
        - name: Generate brownfield access point location playbook
          brownfield_accesspoint_location_playbook_generator:
            dnac_host: "{{ dnac_host }}"
            dnac_username: "{{ dnac_username }}"
            dnac_password: "{{ dnac_password }}"
            dnac_verify: False
            state: gathered
            config:
              - yaml_file_path: "output/ap_locations.yml"
                site_name_filter: "Global/San Jose"
        ```

    Performance Considerations:
        - Large environments (1000+ access points) may take 5-10 minutes
        - API queries are performed serially to avoid rate limiting
        - Memory usage scales with number of access points (approximately 1KB per AP)
        - Network latency significantly impacts total execution time

    Notes:
        - Requires Cisco Catalyst Center version 3.1.3.0 or later
        - Filter priorities (highest to lowest):
            1. hostname_filter (exact matches only)
            2. site_name_filter (includes all child sites)
            3. ap_name_filter (supports wildcards)
            4. site_hierarchy (full hierarchy path)
        - Generated playbooks use 'accesspoint_location_workflow_manager' as target module
        - Check mode (--check) is supported but has no effect (read-only operation)
        - Module always returns changed=False as it performs read-only discovery
        - Playbook generation is idempotent - repeated runs produce identical output
        - Output YAML files use UTF-8 encoding with LF line endings

    See Also:
        - AccesspointLocationPlaybookGenerator class for implementation details
        - validate_input() for complete filter validation logic
        - get_want() for desired state determination
        - get_have() for current state retrieval
        - get_diff_gathered() for playbook generation logic
    """
    # ========================================
    # Module Argument Specification
    # ========================================
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
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # ========================================
    # Module Initialization
    # ========================================
    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    # Initialize the AccesspointLocationPlaybookGenerator object with the module
    ccc_accesspoint_location_playbook_generator = AccesspointLocationPlaybookGenerator(module)

    # ========================================
    # Catalyst Center Version Validation
    # ========================================
    # Verify Catalyst Center version meets minimum requirement (3.1.3.0+)
    if (
        ccc_accesspoint_location_playbook_generator.compare_dnac_versions(
            ccc_accesspoint_location_playbook_generator.get_ccc_version(), "3.1.3.0"
        )
        < 0
    ):
        ccc_accesspoint_location_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for ACCESSPOINT LOCATION WORKFLOW Module. Supported versions start from '3.1.3.0' onwards. ".format(
                ccc_accesspoint_location_playbook_generator.get_ccc_version()
            )
        )
        ccc_accesspoint_location_playbook_generator.set_operation_result(
            "failed", False, ccc_accesspoint_location_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # ========================================
    # State Parameter Validation
    # ========================================
    # Get the state parameter from the provided parameters
    state = ccc_accesspoint_location_playbook_generator.params.get("state")

    # Check if the state is valid (must be 'gathered')
    if state not in ccc_accesspoint_location_playbook_generator.supported_states:
        ccc_accesspoint_location_playbook_generator.status = "invalid"
        ccc_accesspoint_location_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_accesspoint_location_playbook_generator.check_return_status()

    # ========================================
    # Input Parameter Validation
    # ========================================
    # Validate the input parameters and check the return status
    ccc_accesspoint_location_playbook_generator.validate_input().check_return_status()

    # ========================================
    # Configuration Processing Loop
    # ========================================
    # Iterate over the validated configuration parameters
    for config in ccc_accesspoint_location_playbook_generator.validated_config:
        # Reset internal values before processing each config item
        ccc_accesspoint_location_playbook_generator.reset_values()

        # Get desired state (parse and validate filters)
        ccc_accesspoint_location_playbook_generator.get_want(
            config, state).check_return_status()

        # Get current state (query Catalyst Center APIs)
        ccc_accesspoint_location_playbook_generator.get_have(
            config).check_return_status()

        # Apply state-specific logic (generate playbook)
        ccc_accesspoint_location_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    # ========================================
    # Result Return
    # ========================================
    # Exit with JSON result containing operation status and file paths
    module.exit_json(**ccc_accesspoint_location_playbook_generator.result)


if __name__ == "__main__":
    main()

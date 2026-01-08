#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Access Point workflow Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: brownfield_accesspoint_playbook_generator
short_description: Generate YAML configurations playbook for 'accesspoint_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the 'accesspoint_workflow_manager'
    module, reducing the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
version_added: 6.45.0
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
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
      - A list of filters for generating YAML playbook compatible with the
        'brownfield_accesspoint_playbook_generator' module.
      - Filters specify which components to include in the YAML configuration file.
      - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all access point configuration features.
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
          a default file name  "accesspoint_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "accesspoint_workflow_manager_playbook_12_Nov_2025_21_43_26_379.yml".
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML configuration file.
          - These filters apply to all components unless overridden by component-specific filters.
          - At least one filter type must be specified to identify target devices.
        type: dict
        required: false
        suboptions:
          site_list:
            description:
              - List of access point configuration names and details to extract configurations from.
              - LOWEST PRIORITY - Only used if neither site name nor hostname list are provided.
              - Access Point configuration names must match those registered in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all access point configurations.
              - Example ["Global/USA/SAN JOSE/SJ_BLD20/FLOOR1", "Global/USA/SAN JOSE/SJ_BLD20/FLOOR2"]
            type: list
            elements: str
            required: false
          provision_hostname_list:
            description:
              - List of access points provisioned configuration to the floor.
              - LOWEST PRIORITY - Only used if neither mac address nor hostname list are provided.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all planned access points.
              - Example ["test_ap_1", "test_ap_2"]
            type: list
            elements: str
            required: false
          accesspoint_config_list:
            description:
              - List of access points configuration based on the accesspoint hostnames.
              - LOWEST PRIORITY - Only used if neither mac address nor hostname list are provided.
              - Case-sensitive and must be exact matches.
              - Can also be set to "all" to include all real access points.
              - Example ["Test_ap_1", "Test_ap_2"]
            type: list
            elements: str
            required: false
          accesspoint_provision_config_list:
            description:
              - List of access points assigned to the floor.
              - LOWEST PRIORITY - Only used if neither mac address nor hostname are provided.
              - Case-sensitive and must be exact matches.
              - Example ["Test_ap_1", "Test_ap_2"]
            type: list
            elements: str
            required: false
          accesspoint_provision_config_mac_list:
            description:
              - List of Access point MAC addresses assigned to the floor.
              - LOWEST PRIORITY - Only used if neither mac address nor hostname are provided.
              - Case-sensitive and must be exact matches.
              - Example ["a4:88:73:d4:dd:80", "a4:88:73:d4:dd:81"]
            type: list
            elements: str
            required: false
requirements:
  - dnacentersdk >= 2.10.10
  - python >= 3.9
notes:
    # Version Compatibility
  - Minimum Catalyst Center version 2.3.5.3 required for accesspoint configuration generator.

  - This module utilizes the following SDK methods
    devices.get_device_list
    wireless.get_access_point_configuration
    sites.get_site
    sda.get_device_info
    sites.assign_devices_to_site
    wireless.ap_provision
    wireless.configure_access_points
    sites.get_membership

  - The following API paths are used
    GET  /dna/intent/api/v1/network-device
    GET  /dna/intent/api/v1/site
    GET  /dna/intent/api/v1/business/sda/device
    GET  /dna/intent/api/v1/membership/{siteId}
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Access Point provision and configuration
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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

- name: Auto-generate YAML Configuration for all Access Point provision and configuration with custom file path
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
      - file_path: "tmp/brownfield_accesspoint_workflow_playbook.yml"
        generate_all_configurations: true

- name: Generate YAML Configuration with file path based on site list filters
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
      - file_path: "tmp/brownfield_accesspoint_workflow_playbook_site_base.yml"
        global_filters:
          site_list:
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR1
            - Global/USA/SAN JOSE/SJ_BLD20/FLOOR2

- name: Generate YAML provision config with file path based on hostname list filters
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          provision_hostname_list:
            - test_ap_1
            - test_ap_2

- name: Generate YAML Configuration with file path based on hostname list
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          accesspoint_config_list:
            - Test_ap_1
            - Test_ap_2

- name: Generate YAML provision and configuration with default file path based on hostname list
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          accesspoint_provision_config_list:
            - Test_ap_1
            - Test_ap_2

- name: Generate YAML accesspoint provision Configuration based on MAC Address list
  cisco.dnac.brownfield_accesspoint_playbook_generator:
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
          accesspoint_provision_config_mac_list:
            - a4:88:73:d4:dd:80
            - a4:88:73:d4:dd:81
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "YAML config generation Task succeeded for module 'brownfield_accesspoint_playbook_generator'.": {
            "file_path": "tmp/brownfield_accesspoint_playbook_templatebase.yml"}
        },
      "msg": {
        "YAML config generation Task succeeded for module 'brownfield_accesspoint_playbook_generator'.": {
            "file_path": "tmp/brownfield_accesspoint_playbook_templatebase.yml"}
        }
    }

# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": "No configurations or components to process for module 'accesspoint_workflow_manager'.
                  Verify input filters or configuration.",
      "msg": "No configurations or components to process for module 'accesspoint_workflow_manager'.
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


class AccesspointGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center
    using the GET APIs.
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
        self.module_name = "accesspoint_workflow_manager"
        self.module_schema = self.get_workflow_elements_schema()
        self.log("Initialized AccesspointGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False
        self.have["devices_details"], self.have["all_ap_config"], self.have["all_detailed_config"] = [], [], []
        self.have["all_provision_config"], self.have["unprocessed"] = [], []

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
            "global_filters": {"type": "dict", "elements": "dict", "required": False},
        }

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
        Validates individual configuration parameters for brownfield access point generation.

        Args:
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
        access point config such as ap_name configuration and provision details
        in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.

        Args:
            config (dict): The configuration data for the access point config elements.
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
                self.pprint(want["yaml_config_generator"])
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for access point config operations."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Retrieves the current state of access point configuration from the Cisco Catalyst Center.
        This method fetches the existing configurations from Access Points
        such as accesspoint name, model, position and radio in the Cisco Catalyst Center.
        It logs detailed information about the retrieval process and updates the
        current state attributes accordingly.

        Args:
            config (dict): The configuration data for the access point configuration elements.

        Returns:
            object: An instance of the class with updated attributes:
                self.have: A dictionary containing the current state of access point configuration.
                self.msg: A message describing the retrieval result.
                self.status: The status of the retrieval (either "success" or "failed").
        """
        self.log(
            "Retrieving current state of access point configuration from Cisco Catalyst Center.",
            "INFO",
        )

        if config and isinstance(config, dict):
            if config.get("generate_all_configurations", False):
                self.log("Collecting all access point location details", "INFO")
                self.have["all_ap_config"] = self.get_current_config(config)

                if not self.have.get("all_ap_config"):
                    self.msg = "No existing access point locations found in Cisco Catalyst Center."
                    self.status = "success"
                    return self

                self.log("All Configurations collected successfully : {0}".format(
                    self.pprint(self.have.get("all_ap_config"))), "INFO")

            global_filters = config.get("global_filters")
            if global_filters:
                self.log(f"Collecting access point location details based on global filters: {global_filters}", "INFO")
                self.have["all_ap_config"] = self.get_current_config(global_filters)

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
        Returns the mapping configuration for access point workflow manager.
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
                "provision_hostname_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_config_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_provision_config_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "accesspoint_provision_config_mac_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            }
        }

    def get_current_config(self, input_config):
        """
        Retrieves the current configuration of an access point and site related details
        from Cisco Catalyst Center.

        Parameters:
          - self (object): An instance of the class containing the method.
          - input_config (dict): A dictionary containing the input configuration details.
        Returns:
            - tuple: A tuple containing a boolean indicating if the access point exists
                and a dictionary of the current configuration details.
        Description:
            Queries the Cisco Catalyst Center for the existence of an Access Point
            using the provided input configuration details such as MAC address,
            management IP address, or hostname. If found, it retrieves the current
            Access Point configuration and returns it.
        """
        self.log("Starting to retrieve current configuration with input: {0}".format(
            self.pprint(input_config)), "INFO")

        collect_all_config = []
        collect_all_config_details = []
        current_configuration = self.get_accesspoint_details()
        self.log("Retrieved current access point details: {0}".format(
            self.pprint(current_configuration)), "INFO")

        if not current_configuration or not isinstance(current_configuration, list):
            self.msg = "No access point details found in Cisco Catalyst Center."
            self.status = "success"
            return

        for ap_detail in current_configuration:
            eth_mac_address = ap_detail.get("eth_mac_address")
            current_eth_configuration = self.get_accesspoint_configuration(
                eth_mac_address)

            if not current_eth_configuration:
                self.log(f"No configuration found for access point with MAC address: {eth_mac_address}",
                         "WARNING")
                continue

            ap_detail["configuration"] = current_eth_configuration
            parsed_config = self.parse_accesspoint_configuration(current_eth_configuration, ap_detail)
            self.log(f"Parsed configuration for access point with MAC address {eth_mac_address}: {parsed_config}",
                     "INFO")
            collect_all_config.append(parsed_config)
            collect_all_config_details.append(ap_detail)

        self.log("Completed parsing all current configuration: {0}".format(
            self.pprint(collect_all_config)), "INFO")
        self.have["all_detailed_config"] = copy.deepcopy(collect_all_config_details)

        return collect_all_config

    def get_accesspoint_details(self):
        """
        Retrieves the current details of all access point devices in Cisco Catalyst Center.

        Parameters:
        - self (object): An instance of the class containing the method.

        Returns:
        A tuple containing a boolean indicating if the devices exists and a
        dictionary of the current inventory details

        Description:
        Retrieve all access point device details from Cisco Catalyst Center.
        """
        response_all = []
        offset = 1
        limit = 500
        api_family, api_function, param_key = "devices", "get_device_list", "family"
        request_params = {param_key: "Unified AP", "offset": offset, "limit": limit}
        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))

        while resync_retry_count > 0:
            self.log(f"Sending initial API request: Family='{api_family}', Function='{api_function}', Params={request_params}",
                     "DEBUG")

            response = self.execute_get_request(api_family, api_function, request_params)
            if not response:
                self.log("No data received from API (Offset={0}). Exiting pagination.".
                         format(request_params["offset"]), "DEBUG")
                break

            self.log("Received {0} devices(s) from API (Offset={1}).".format(
                len(response.get("response")), request_params["offset"]), "DEBUG")
            device_list = response.get("response")
            if device_list and isinstance(device_list, list):
                self.log("Processing device list: {0}".format(
                    self.pprint(device_list)), "DEBUG")
                required_data_list = []
                for device_response in device_list:
                    required_data = {
                        "id": device_response.get("id"),
                        "associated_wlc_ip": device_response.get("associatedWlcIp"),
                        "eth_mac_address": device_response.get("apEthernetMacAddress"),
                        "mac_address": device_response.get("macAddress"),
                        "hostname": device_response.get("hostname"),
                        "management_ip_address": device_response.get("managementIpAddress"),
                        "model": device_response.get("platformId"),
                        "serial_number": device_response.get("serialNumber"),
                        "site_hierarchy": device_response.get("snmpLocation"),
                        "reachability_status": device_response.get("reachabilityStatus"),
                        "type": device_response.get("type")
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
            self.log("Total {0} accesspoint(s) details retrieved. {1}".format(
                len(response_all), self.pprint(response_all)), "DEBUG")
        else:
            self.log("No accesspoint details found for the Unified AP.", "WARNING")

        return response_all

    def get_accesspoint_configuration(self, eth_mac_address):
        """
        Retrieves the current configuration of an access point from Cisco Catalyst Center.

        Parameters:
            eth_mac_address (str): The Ethernet MAC address of the access point.

        Returns:
            dict: A dictionary containing the current configuration details of the access point.

        Description:
            Queries the Cisco Catalyst Center for the configuration of an access point
            using its Ethernet MAC address. If found, it retrieves the current configuration
            details and returns them.
        """
        self.log("Starting to retrieve access point configuration for MAC: {0}".format(
            eth_mac_address), "INFO")

        if not eth_mac_address:
            self.msg = "Ethernet MAC address is required to retrieve access point configuration."
            self.log(self.msg, "ERROR")
            return None

        api_family, api_function, param_key = "wireless", "get_access_point_configuration", "key"
        request_params = {param_key: eth_mac_address}

        self.log(f"Sending initial API request: Family='{api_family}', Function='{api_function}', Params={request_params}",
                 "DEBUG")
        response = self.execute_get_request(api_family, api_function, request_params)
        if not response:
            self.log("No data received from access point config API.", "DEBUG")
            return None

        current_eth_configuration = self.camel_to_snake_case(response)
        self.log("Received API response from get_access_point_configuration: {0}".format(
            self.pprint(current_eth_configuration)), "INFO")

        return current_eth_configuration

    def parse_accesspoint_configuration(self, accesspoint_config, ap_details):
        """
        Parses the access point configuration details.

        Parameters:
            accesspoint_config (dict): The access point configuration details.
            ap_details (dict): Additional details about the access point.

        Returns:
            dict: A dictionary containing the parsed access point configuration details.
        """
        self.log("Starting to parse access point configuration: {0} and details: {1}".format(
            self.pprint(accesspoint_config), self.pprint(ap_details)), "INFO")

        parsed_config = {}
        if not accesspoint_config or not isinstance(accesspoint_config, dict):
            self.log("Invalid access point configuration provided for parsing.", "ERROR")
            return parsed_config

        list_of_ap_keys_to_parse = ["mac_address", "ap_name", "admin_status",
                                    "led_status", "led_brightness_level",
                                    "ap_mode", "location",
                                    "failover_priority", "secondary_controller_name",
                                    "secondary_ip_address", "tertiary_controller_name",
                                    "tertiary_ip_address", "primary_ip_address",
                                    "primary_controller_name"]

        for each_key in list_of_ap_keys_to_parse:
            if each_key == "location":
                if accesspoint_config.get(each_key) == "default location":
                    parsed_config["is_assigned_site_as_location"] = "Enabled"
                else:
                    parsed_config["location"] = accesspoint_config.get(each_key)
            elif each_key == "tertiary_controller_name" or each_key == "secondary_controller_name":
                if accesspoint_config.get(each_key) == "Clear" or accesspoint_config.get(each_key) is None:
                    parsed_config[each_key] = "Inherit from site / Clear"
            elif each_key == "secondary_ip_address" or each_key == "tertiary_ip_address":
                if accesspoint_config.get(each_key) != "0.0.0.0":
                    parsed_config[each_key] = accesspoint_config.get(each_key)
            elif each_key == "primary_controller_name":
                if accesspoint_config.get(each_key) == "Clear" or accesspoint_config.get(each_key) is None:
                    del parsed_config["secondary_controller_name"]
                    del parsed_config["tertiary_controller_name"]
                    del parsed_config["primary_ip_address"]
                else:
                    parsed_config[each_key] = accesspoint_config.get(each_key)
            else:
                parsed_config[each_key] = accesspoint_config.get(each_key)

        parsed_config["clean_air_si_2.4ghz"] = "Disabled"
        parsed_config["clean_air_si_5ghz"] = "Disabled"
        parsed_config["clean_air_si_6ghz"] = "Disabled"

        radio_config = accesspoint_config.get("radio_dtos")
        if radio_config and isinstance(radio_config, list):
            self.log(f"Parsing radio configuration from access point configuration: {radio_config}",
                     "INFO")
            parsed_all_radios = {}
            for radio in radio_config:
                parsed_radio = {}
                radio_config_key = None
                list_of_radio_keys_to_parse = ["if_type_value", "admin_status", "radio_role_assignment",
                                               "channel", "radio_band", "power_assignment_mode", "clean_air_si",
                                               "channel_width", "powerlevel", "channel_assignment_mode",
                                               "channel_number", "custom_power_level",
                                               "slot_id", "antenna_gain"]
                for each_radio_key in list_of_radio_keys_to_parse:
                    if each_radio_key == "if_type_value":
                        if radio.get(each_radio_key) == "2.4 GHz":
                            radio_config_key = "2.4ghz_radio"
                        elif radio.get(each_radio_key) == "5 GHz":
                            radio_config_key = "5ghz_radio"
                        elif radio.get(each_radio_key) == "6 GHz":
                            radio_config_key = "6ghz_radio"
                        elif radio.get(each_radio_key) == "Dual Radio":
                            radio_config_key = "xor_radio"
                        elif radio.get(each_radio_key) == "Tri Radio":
                            radio_config_key = "tri_radio"
                        else:
                            radio_config_key = "if_type_value"
                    elif each_radio_key == "powerlevel":
                        parsed_radio["power_level"] = radio.get(each_radio_key)
                    elif each_radio_key == "clean_air_si":
                        if radio.get(each_radio_key) == "Enabled":
                            if radio_config_key == "2.4ghz_radio":
                                parsed_config["clean_air_si_2.4ghz"] = "Enabled"
                            elif radio_config_key == "5ghz_radio":
                                parsed_config["clean_air_si_5ghz"] = "Enabled"
                            elif radio_config_key == "6ghz_radio":
                                parsed_config["clean_air_si_6ghz"] = "Enabled"
                    else:
                        if radio.get(each_radio_key) is not None:
                            parsed_radio[each_radio_key] = radio.get(each_radio_key)

                if parsed_radio.get("power_assignment_mode") == "Global":
                    del parsed_radio["power_level"]

                if parsed_radio.get("channel_assignment_mode") == "Global":
                    del parsed_radio["channel_number"]

                if radio_config_key:
                    parsed_all_radios[radio_config_key] = parsed_radio

            parsed_config.update(parsed_all_radios)

        if accesspoint_config.get("provisioning_status"):
            self.log("Access point is provisioned, parsing additional configuration details.", "INFO")
            site_hierarchy = ap_details.get("site_hierarchy")
            if site_hierarchy and site_hierarchy not in ["default-location", "default location"]:
                parent_path, floor = site_hierarchy.rsplit("/", 1)
                parsed_config["rf_profile"] = "HIGH"
                parsed_config["site"] = {}
                parsed_config["site"]["floor"] = {}
                parsed_config["site"]["floor"]["parent_name"] = parent_path
                parsed_config["site"]["floor"]["name"] = floor

        self.log("Completed parsing access point configuration: {0}".format(
            self.pprint(parsed_config)), "INFO")
        return parsed_config

    def get_diff_gathered(self):
        """
        Gathers access point configuration details from Cisco Catalyst Center and generates YAML playbook.

        Returns:
            self: Returns the current object with status and result set.
        """
        self.log("Starting brownfield access point configuration gathering process", "INFO")

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

        if self.have.get("unprocessed"):
            self.msg = "Some access point configurations were not processed: " + str(self.have.get("unprocessed"))
            self.set_operation_result("warning", True, self.msg, "WARNING")

        return self

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters,
        processes the data and writes the YAML content to a specified file.
        It dynamically handles multiple access points configuration and their respective filters.

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
            self.log("Generate all access point configurations from Catalyst Center", "INFO")

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
            self.log("Preparing to collect all configurations for access point configuration workflow.",
                     "DEBUG")
            final_list = self.have.get("all_ap_config", [])
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
        Process global filters for access point configuration workflow.

        Args:
            global_filters (dict): A dictionary containing global filter parameters.

        Returns:
            dict: A dictionary containing processed global filter parameters.
        """
        self.log(f"Processing global filters: {global_filters}", "DEBUG")

        site_list = global_filters.get("site_list")
        provision_hostname_list = global_filters.get("provision_hostname_list")
        accesspoint_config_list = global_filters.get("accesspoint_config_list")
        accesspoint_provision_config_list = global_filters.get("accesspoint_provision_config_list")
        accesspoint_provision_config_mac_list = global_filters.get("accesspoint_provision_config_mac_list")
        final_list = []
        unprocessed_aps = []

        if not self.have.get("all_ap_config"):
            self.msg = "No access points configuration found in the catalyst center."
            self.log(self.msg, "WARNING")
            self.fail_and_exit(self.msg)

        if site_list and isinstance(site_list, list):
            self.log(f"Filtering access point configuration based on site_list: {site_list}",
                     "DEBUG")
            if len(site_list) == 1 and site_list[0].lower() == "all":
                final_list = self.have.get("all_ap_config", [])
            else:
                ap_config_site_list = []
                for floor in site_list:
                    ap_site_exist = self.find_multiple_dict_by_key_value(
                        self.have.get("all_ap_config", []), "location", floor)

                    if not ap_site_exist:
                        self.log(f"Given site hierarchy not exist : {floor}", "WARNING")
                        unprocessed_aps.append(floor + ": Unable to find the configuration for the site hierarchy in the catalyst center.")
                        continue

                    ap_config_site_list.extend(ap_site_exist)
                final_list = ap_config_site_list
            self.log(f"Access points configuration collected for site list {site_list}: {final_list}", "DEBUG")

        elif provision_hostname_list and isinstance(provision_hostname_list, list):
            self.log(f"Filtering access point provision based on hostname list: {provision_hostname_list}",
                     "DEBUG")

            if len(provision_hostname_list) == 1 and provision_hostname_list[0].lower() == "all":
                ap_exist = self.find_multiple_dict_by_key_value(
                    self.have["all_ap_config"], "rf_profile", "HIGH")
                if not ap_exist:
                    self.log("No provisioned access points found in the catalyst center.", "WARNING")
                    self.msg = "No provisioned access points found in the catalyst center."
                    self.fail_and_exit(self.msg)

                provisioned_aps = []
                for each_ap in ap_exist:
                    provision_config = {
                        "mac_address": each_ap.get("mac_address"),
                        "rf_profile": each_ap.get("rf_profile"),
                        "site": each_ap.get("site")
                    }
                    provisioned_aps.append(provision_config)
                final_list = provisioned_aps
            else:
                provisioned_aps = []
                for each_host in provision_hostname_list:
                    self.log(f"Check provision AP config exist for : {each_host}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_host)
                    if not ap_exist:
                        self.log(f"Given provision access point hostname not exist : {each_host}", "WARNING")
                        unprocessed_aps.append(each_host + ": Unable to find the hostname in the catalyst center.")
                        continue
                    provisioned_aps.append({
                        "mac_address": ap_exist[0].get("mac_address"),
                        "rf_profile": ap_exist[0].get("rf_profile"),
                        "site": ap_exist[0].get("site")
                    })

                if not provisioned_aps:
                    self.msg = "No provisioned access points found in the catalyst center."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = provisioned_aps
            self.log(f"Access points configuration collected for provision access point list {provision_hostname_list}: {final_list}",
                     "DEBUG")

        elif accesspoint_config_list and isinstance(accesspoint_config_list, list):
            self.log(f"Filtering access point configuration based on ap config list: {accesspoint_config_list}",
                     "DEBUG")
            ap_config_list = []
            keys_to_remove = ["rf_profile", "site"]

            if len(accesspoint_config_list) == 1 and accesspoint_config_list[0].lower() == "all":
                ap_config_list = copy.deepcopy(self.have.get("all_ap_config", []))
                for each_ap in ap_config_list:
                    for key in keys_to_remove:
                        if each_ap.get(key):
                            del each_ap[key]
                self.log(f"All access point configurations found for 'all' filter. {ap_config_list}", "INFO")
                final_list = ap_config_list
            else:
                for each_ap in accesspoint_config_list:
                    self.log(f"Check real access point exist for : {each_ap}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_ap)

                    if not ap_exist:
                        self.log(f"Given provision access point hostname not exist : {each_ap}", "WARNING")
                        unprocessed_aps.append(each_ap + ": Unable to find the hostname in the catalyst center.")
                        continue

                    for each_ap in ap_exist:
                        for key in keys_to_remove:
                            if each_ap.get(key):
                                del each_ap[key]

                    ap_config_list.extend(ap_exist)
                    self.log(f"Given access point hostname exist : {ap_exist}", "INFO")

                if not ap_config_list:
                    self.msg = f"No access points found matching the provided list. {accesspoint_config_list}."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = ap_config_list
            self.log(f"Access points configuration collected for ap configuration list {accesspoint_config_list}: {final_list}",
                     "DEBUG")

        elif accesspoint_provision_config_list and isinstance(accesspoint_provision_config_list, list):
            self.log(f"Filtering access point configuration based on hostname list: {accesspoint_provision_config_list}",
                     "DEBUG")
            if len(accesspoint_provision_config_list) == 1 and accesspoint_provision_config_list[0].lower() == "all":
                final_list = self.have.get("all_ap_config", [])
                self.log(f"All access point configurations found for 'all' filter. {final_list}", "INFO")
            else:
                collected_aps = []
                for each_host_name in accesspoint_provision_config_list:
                    self.log(f"Check access point configuration exist for : {each_host_name}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "ap_name", each_host_name)

                    if not ap_exist:
                        self.log(f"Given provision access point hostname not exist : {each_host_name}", "WARNING")
                        unprocessed_aps.append(each_host_name + ": Unable to find the hostname in the catalyst center.")
                        continue

                    collected_aps.extend(ap_exist)
                    self.log(f"Given access point configuration exist : {ap_exist}", "INFO")

                if not collected_aps:
                    self.msg = "No access points found matching the provided hostname list."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = collected_aps

            self.log(f"Access point configuration collected for given hostname list {accesspoint_provision_config_list}: {final_list}",
                     "DEBUG")

        elif accesspoint_provision_config_mac_list and isinstance(accesspoint_provision_config_mac_list, list):
            self.log(f"Filtering access point configuration based on mac address list: {accesspoint_provision_config_mac_list}",
                     "DEBUG")
            if len(accesspoint_provision_config_mac_list) == 1 and accesspoint_provision_config_mac_list[0].lower() == "all":
                final_list = self.have.get("all_ap_config", [])
                self.log(f"All access point configurations found for 'all' filter. {final_list}", "INFO")
            else:
                collected_aps = []
                for each_mac in accesspoint_provision_config_mac_list:
                    self.log(f"Check access point configuration exist for : {each_mac}", "INFO")
                    ap_exist = self.find_multiple_dict_by_key_value(
                        self.have["all_ap_config"], "mac_address", each_mac)

                    if not ap_exist:
                        self.log(f"Given provision access point mac address not exist : {each_mac}", "WARNING")
                        unprocessed_aps.append(each_mac + ": Unable to find configuration for the MAC address in the catalyst center.")
                        continue

                    collected_aps.extend(ap_exist)
                    self.log(f"Given access point configuration exist : {ap_exist}", "INFO")

                if not collected_aps:
                    self.msg = "No access points found matching the provided mac address list."
                    self.log(self.msg, "WARNING")
                    self.fail_and_exit(self.msg)

                final_list = collected_aps

            self.log(f"Access point configuration collected for given mac address list {accesspoint_provision_config_mac_list}: {final_list}",
                     "DEBUG")

        else:
            self.log("No specific global filters provided, processing all access points configuration.", "DEBUG")

        if unprocessed_aps:
            self.msg = {
                "The following access points could not be processed:": unprocessed_aps
            }
            self.log(self.msg, "WARNING")
            self.have["unprocessed"] = unprocessed_aps

        if not final_list:
            self.log("No access points position found in the catalyst center.", "WARNING")
            return None

        return final_list


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
    ccc_accesspoint_playbook_generator = AccesspointGenerator(module)
    if (
        ccc_accesspoint_playbook_generator.compare_dnac_versions(
            ccc_accesspoint_playbook_generator.get_ccc_version(), "2.3.5.3"
        )
        < 0
    ):
        ccc_accesspoint_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for <module_name_caps> Module. Supported versions start from '2.3.5.3' onwards. ".format(
                ccc_accesspoint_playbook_generator.get_ccc_version()
            )
        )
        ccc_accesspoint_playbook_generator.set_operation_result(
            "failed", False, ccc_accesspoint_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_accesspoint_playbook_generator.params.get("state")
    # Check if the state is valid
    if state not in ccc_accesspoint_playbook_generator.supported_states:
        ccc_accesspoint_playbook_generator.status = "invalid"
        ccc_accesspoint_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_accesspoint_playbook_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_accesspoint_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_accesspoint_playbook_generator.validated_config:
        ccc_accesspoint_playbook_generator.reset_values()
        ccc_accesspoint_playbook_generator.get_want(
            config, state).check_return_status()
        ccc_accesspoint_playbook_generator.get_have(
            config).check_return_status()
        ccc_accesspoint_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_accesspoint_playbook_generator.result)


if __name__ == "__main__":
    main()

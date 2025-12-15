#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbook for Provision Workflow Management in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Madhan Sankaranarayanan, Syed Khadeer Ahmed, Ajith Andrew J"

DOCUMENTATION = r"""
---
module: brownfield_provision_playbook_generator
short_description: Generate YAML playbook for 'provision_workflow_manager' module.
description:
- Generates YAML configurations compatible with the `provision_workflow_manager`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the provisioned devices configured on
  the Cisco Catalyst Center.
version_added: 6.31.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Abinash Mishra (@abimishr)
- Madhan Sankaranarayanan (@madhansansel)
- Syed Khadeer Ahmed (@syed-khadeerahmed)
- Ajith Andrew J (@ajithandrewj)
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
    - A list of filters for generating YAML playbook compatible with the `provision_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "provision_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
      generate_all_configurations:
        description:
        - When set to C(true), generates a comprehensive YAML playbook containing all provisioned devices
          from Cisco Catalyst Center, including both wired and wireless devices.
        - This option ignores all filter parameters (C(global_filters) and C(component_specific_filters))
          and retrieves complete configuration for all devices across all sites.
        - If not provided or set to C(false), filters will be applied to retrieve specific devices.
        type: bool
        default: false
      global_filters:
        description:
        - Global filters to apply across all components.
        type: dict
        suboptions:
          management_ip_address:
            description:
            - Management IP address to filter devices globally.
            - Can specify single IP or list of IPs.
            type: list
            elements: str
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
              - Wired Devices "wired"
              - Wireless Devices "wireless"
            - If not specified, all components are included.
            - For example, ["wired", "wireless"].
            type: list
            elements: str
          wired:
            description:
            - Wired devices to filter devices by management IP, site name, or device family.
            type: list
            elements: dict
            suboptions:
              management_ip_address:
                description:
                - Management IP address to filter devices by IP address.
                type: str
              site_name_hierarchy:
                description:
                - Site name hierarchy to filter devices by site.
                - Can specify single site or list of sites.
                type: list
                elements: str
              device_family:
                description:
                - Device family to filter devices by type (e.g., 'Switches and Hubs', 'Routers').
                type: str
          wireless:
            description:
            - Wireless devices to filter devices by management IP, site name, or device family.
            type: list
            elements: dict
            suboptions:
              management_ip_address:
                description:
                - Management IP address to filter devices by IP address.
                type: str
              site_name_hierarchy:
                description:
                - Site name hierarchy to filter devices by site.
                - Can specify single site or list of sites.
                type: list
                elements: str
              device_family:
                description:
                - Device family to filter devices by type (e.g., 'Wireless Controller').
                type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
- SDK Methods used are
    - sda.Sda.get_provisioned_devices
    - devices.Devices.get_network_device_by_ip
    - devices.Devices.get_device_detail
    - sites.Sites.get_site
    - wireless.Wireless.get_access_point_configuration
    - wireless.Wireless.get_primary_managed_ap_locations_for_specific_wireless_controller
    - wireless.Wireless.get_secondary_managed_ap_locations_for_specific_wireless_controller
- Paths used are
    - GET /dna/intent/api/v1/sda/provisioned-devices
    - GET /dna/intent/api/v1/network-device/ip-address/{ipAddress}
    - GET /dna/intent/api/v1/network-device/{id}/detail
    - GET /dna/intent/api/v1/site
    - GET /dna/intent/api/v1/wireless/accesspoint-configuration/summary
    - GET /dna/intent/api/v1/wireless/primary-managed-ap-locations/{networkDeviceId}
    - GET /dna/intent/api/v1/wireless/secondary-managed-ap-locations/{networkDeviceId}
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with File Path specified
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_provision_config.yaml"

- name: Generate YAML Configuration with specific wired devices filter
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_provision_config.yaml"
        component_specific_filters:
          components_list: ["wired"]

- name: Generate YAML Configuration for devices with IP address filter (global)
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_provision_config.yaml"
        global_filters:
          management_ip_address:
            - "204.192.3.40"
            - "204.192.12.201"

- name: Generate YAML Configuration for wired devices with multiple site filters
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_provision_config.yaml"
        component_specific_filters:
          components_list: ["wired"]
          wired:
            - site_name_hierarchy:
                - "Global/USA/San Francisco/BGL_18"
                - "Global/USA/San Jose/SJ_BLD20"

- name: Generate YAML Configuration for all wired devices
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_provision_config.yaml"
        component_specific_filters:
          components_list: ["wired"]

- name: Generate YAML Configuration for wireless devices only
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_wireless_config.yaml"
        component_specific_filters:
          components_list: ["wireless"]

- name: Generate YAML Configuration for both wired and wireless devices
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_all_devices_config.yaml"
        component_specific_filters:
          components_list: ["wired", "wireless"]

- name: Generate YAML Configuration for wireless devices with specific site filter
  cisco.dnac.brownfield_provision_playbook_generator:
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
      - file_path: "/tmp/catc_site_wireless_config.yaml"
        component_specific_filters:
          components_list: ["wireless"]
          wireless:
            - site_name_hierarchy:
                - "Global/USA/San Francisco/BGL_18"
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


class ProvisionPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for provision workflow configured in Cisco Catalyst Center using the GET APIs.
    """

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
        self.module_name = "provision_workflow_manager"
        self.module_schema = self.provision_workflow_manager_mapping()
        self.log("Initialized ProvisionPlaybookGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")
        self.site_id_name_dict = self.get_site_id_name_mapping()

    def get_site_id_name_mapping(self):
        """
        Retrieves the site name hierarchy for all sites.
        Returns:
            dict: A dictionary mapping site IDs to their name hierarchies.
        Raises:
            Exception: If an error occurs while retrieving the site name hierarchy.
        """

        self.log(
            "Retrieving site name hierarchy for all sites.", "DEBUG"
        )
        self.log("Executing 'get_sites' API call to retrieve all sites.", "DEBUG")
        site_id_name_mapping = {}

        api_family, api_function, params = "site_design", "get_sites", {}
        site_details = self.execute_get_with_pagination(
            api_family, api_function, params
        )

        for site in site_details:
            site_id = site.get("id")
            if site_id:
                site_id_name_mapping[site_id] = site.get("nameHierarchy")

        return site_id_name_mapping

    def execute_get_with_pagination(self, api_family, api_function, params, offset=1, limit=500, use_strings=False):
        """
        Executes a paginated GET request using the specified API family, function, and parameters.
        Args:
            api_family (str): The API family to use for the call (For example, 'wireless', 'network', etc.).
            api_function (str): The specific API function to call for retrieving data (For example, 'get_ssid_by_site', 'get_interfaces').
            params (dict): Parameters for filtering the data.
            offset (int, optional): Starting offset for pagination. Defaults to 1.
            limit (int, optional): Maximum number of records to retrieve per page. Defaults to 500.
            use_strings (bool, optional): Whether to use string values for offset and limit. Defaults to False.
        Returns:
            list: A list of dictionaries containing the retrieved data based on the filtering parameters.
        """
        self.log("Starting paginated API execution for family '{0}', function '{1}'".format(
            api_family, api_function), "DEBUG")

        def update_params(current_offset, current_limit):
            """Update the params dictionary with pagination info."""
            # Create a copy of params to avoid modifying the original
            updated_params = params.copy()
            updated_params.update({
                "offset": str(current_offset) if use_strings else current_offset,
                "limit": str(current_limit) if use_strings else current_limit,
            })
            return updated_params

        try:
            # Initialize results list and keep offset/limit as integers for arithmetic
            results = []
            current_offset = offset
            current_limit = limit

            self.log("Pagination settings - offset: {0}, limit: {1}, use_strings: {2}".format(
                current_offset, current_limit, use_strings), "DEBUG")

            # Start the loop for paginated API calls
            while True:
                # Update parameters for pagination
                api_params = update_params(current_offset, current_limit)

                try:
                    # Execute the API call
                    self.log(
                        "Attempting API call with offset {0} and limit {1} for family '{2}', function '{3}': {4}".format(
                            current_offset,
                            current_limit,
                            api_family,
                            api_function,
                            api_params,
                        ),
                        "INFO",
                    )

                    # Execute the API call
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params=api_params,
                    )
                    self.log("Recived API response: {0}".format(response), "DEBUG")
                except Exception as e:
                    # Handle error during API call
                    self.msg = (
                        "An error occurred while retrieving data using family '{0}', function '{1}'. "
                        "Error: {2}".format(
                            api_family, api_function, str(e)
                        )
                    )
                    self.fail_and_exit(self.msg)

                self.log(
                    "Response received from API call for family '{0}', function '{1}': {2}".format(
                        api_family, api_function, response
                    ),
                    "DEBUG",
                )

                # Process the response if available
                response_data = response.get("response")
                if not response_data:
                    self.log(
                        "Exiting the loop because no data was returned after increasing the offset. "
                        "Current offset: {0}".format(current_offset),
                        "INFO",
                    )
                    break

                # Extend the results list with the response data
                results.extend(response_data)

                # Check if the response size is less than the limit
                if len(response_data) < current_limit:
                    self.log(
                        "Received less than limit ({0}) results, assuming last page. Exiting pagination.".format(
                            current_limit
                        ),
                        "DEBUG",
                    )
                    break

                # Increment the offset for the next iteration (always use integer arithmetic)
                current_offset = int(current_offset) + int(current_limit)

            if results:
                self.log(
                    "Data retrieved for family '{0}', function '{1}': Total records: {2}".format(
                        api_family, api_function, len(results)
                    ),
                    "INFO",
                )
            else:
                self.log(
                    "No data found for family '{0}', function '{1}'.".format(
                        api_family, api_function
                    ),
                    "DEBUG",
                )

            # Return the list of retrieved data
            return results

        except Exception as e:
            self.msg = (
                "An error occurred while retrieving data using family '{0}', function '{1}'. "
                "Error: {2}".format(
                    api_family, api_function, str(e)
                )
            )
            self.fail_and_exit(self.msg)

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

    def provision_workflow_manager_mapping(self):
        """
        Constructs and returns a structured mapping for managing provision workflow elements.
        """
        tempspec = {
            "network_elements": {
                "wired": {
                    "filters": ["management_ip_address", "site_name_hierarchy", "device_family"],
                    "temp_spec_function": self.wired_devices_temp_spec,
                    "api_function": "get_provisioned_devices",
                    "api_family": "sda",
                    "get_function_name": self.get_wired_devices,
                },
                "wireless": {
                    "filters": ["management_ip_address", "site_name_hierarchy", "device_family"],
                    "temp_spec_function": self.wireless_devices_temp_spec,
                    "api_function": "get_provisioned_devices",
                    "api_family": "sda",
                    "get_function_name": self.get_wireless_devices,
                },
            },
            "global_filters": ["management_ip_address"],
        }

        self.log("Constructed provision workflow manager mapping: {0}".format(tempspec), "DEBUG")
        return tempspec

    def wired_devices_temp_spec(self):
        """
        Constructs a temporary specification for wired devices.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wired device attributes.
        """
        self.log("Generating temporary specification for wired devices.", "DEBUG")
        wired_devices = OrderedDict({
            "management_ip_address": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_device_management_ip,
            },
            "site_name_hierarchy": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_device_site_hierarchy,
            },
            "provisioning": {"type": "bool", "default": True},
            "force_provisioning": {"type": "bool", "default": False},
        })
        self.log("Temporary specification for wired devices generated: {0}".format(wired_devices), "DEBUG")
        return wired_devices

    def wireless_devices_temp_spec(self):
        """
        Constructs a temporary specification for wireless devices.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of wireless device attributes.
        """
        self.log("Generating temporary specification for wireless devices.", "DEBUG")
        wireless_devices = OrderedDict({
            "management_ip_address": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_device_management_ip,
            },
            "site_name_hierarchy": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_device_site_hierarchy,
            },
            "provisioning": {"type": "bool", "default": True},
            "force_provisioning": {"type": "bool", "default": False},
            "primary_managed_ap_locations": {
                "type": "list",
                "special_handling": True,
                "transform": self.get_primary_managed_ap_locations_for_device,
                "wireless_only": True,
            },
            "secondary_managed_ap_locations": {
                "type": "list",
                "special_handling": True,
                "transform": self.get_secondary_managed_ap_locations_for_device,
                "wireless_only": True,
            },
        })
        self.log("Temporary specification for wireless devices generated: {0}".format(wireless_devices), "DEBUG")
        return wireless_devices

    def get_wired_devices(self, network_element, component_specific_filters=None):
        """
        Retrieves wired provisioned devices based on filters.

        Args:
            network_element (dict): Network element definition
            component_specific_filters (list): List of filter dictionaries

        Returns:
            list: List of wired device configurations
        """
        self.log("Starting to retrieve wired devices", "INFO")

        # Get all provisioned devices
        all_devices = self.get_all_provisioned_devices_internal()

        self.log("Total provisioned devices retrieved: {0}".format(len(all_devices)), "error")

        # Filter for wired devices only
        wired_devices = [device for device in all_devices
                         if self.is_wired_device(device)]

        self.log("Found {0} wired devices".format(len(wired_devices)), "INFO")

        # Apply component-specific filters
        if component_specific_filters:
            wired_devices = self.apply_device_filters(wired_devices, component_specific_filters)

        # Process devices into configuration format
        return self.process_device_list(wired_devices, is_wireless=False)

    def get_wireless_devices(self, network_element, component_specific_filters=None):
        """
        Retrieves wireless provisioned devices based on filters.

        Args:
            network_element (dict): Network element definition
            component_specific_filters (list): List of filter dictionaries

        Returns:
            list: List of wireless device configurations
        """
        self.log("Starting to retrieve wireless devices", "INFO")

        # Get all provisioned devices
        all_devices = self.get_all_provisioned_devices_internal()

        # Filter for wireless devices only
        wireless_devices = [device for device in all_devices
                            if self.is_wireless_device(device)]

        self.log("Found {0} wireless devices".format(len(wireless_devices)), "INFO")

        # Apply component-specific filters
        if component_specific_filters:
            wireless_devices = self.apply_device_filters(wireless_devices, component_specific_filters)

        # Process devices into configuration format
        return self.process_device_list(wireless_devices, is_wireless=True)

    def get_all_provisioned_devices_internal(self):
        """
        Internal method to get all provisioned devices from SDA API and add missing wireless controllers.

        Returns:
            list: List of all provisioned devices
        """
        try:
            # Get all provisioned devices from SDA API
            response = self.dnac._exec(
                family="sda",
                function="get_provisioned_devices",
                op_modifies=False,
            )
            self.log("Recived API response: {0}".format(response), "DEBUG")
            sda_devices = response.get("response", [])
            self.log("Retrieved {0} devices from SDA provisioned devices API".format(len(sda_devices)), "INFO")

            # WORKAROUND: Check for missing wireless controllers
            all_devices_response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
            )
            self.log("Recived API response: {0}".format(all_devices_response), "DEBUG")
            all_devices = all_devices_response.get("response", [])

            wireless_controllers_found = []
            sda_device_ids = {device.get("networkDeviceId") for device in sda_devices}

            for device in all_devices:
                device_id = device.get("id")
                management_ip = device.get("managementIpAddress")

                if device_id in sda_device_ids:
                    continue

                try:
                    device_detail_response = self.dnac._exec(
                        family="devices",
                        function="get_device_detail",
                        op_modifies=False,
                        params={"search_by": device_id, "identifier": "uuid"},
                    )
                    self.log("Recived API response: {0}".format(device_detail_response), "DEBUG")
                    device_info = device_detail_response.get("response", {})
                    device_family = device_info.get("nwDeviceFamily")

                    if device_family == "Wireless Controller":
                        try:
                            provision_response = self.dnac._exec(
                                family="sda",
                                function="get_provisioned_wired_device",
                                op_modifies=False,
                                params={"device_management_ip_address": management_ip}
                            )
                            self.log("Recived API response: {0}".format(provision_response), "DEBUG")
                            if provision_response.get("status") == "success":
                                mock_device = {
                                    "networkDeviceId": device_id,
                                    "siteId": device.get("siteId"),
                                    "deviceType": "WirelessController"
                                }
                                sda_devices.append(mock_device)
                                wireless_controllers_found.append(management_ip)
                        except Exception:
                            pass
                except Exception:
                    pass

            self.log("Found {0} additional provisioned wireless controllers".format(
                len(wireless_controllers_found)), "INFO")

            return sda_devices

        except Exception as e:
            self.log("Error retrieving provisioned devices: {0}".format(str(e)), "ERROR")
            return []

    def is_wired_device(self, device):
        """Check if device is a wired device."""
        device_family = self.transform_device_family_info(device)
        return device_family in ["Switches and Hubs", "Routers"]

    def is_wireless_device(self, device):
        """Check if device is a wireless device."""
        device_family = self.transform_device_family_info(device)
        return device_family == "Wireless Controller"

    def apply_device_filters(self, devices, filters):
        """
        Apply component-specific filters to device list.
        Now supports site_name_hierarchy as a list.

        Args:
            devices (list): List of devices to filter
            filters (list): List of filter dictionaries

        Returns:
            list: Filtered device list
        """
        filtered_devices = []

        for filter_param in filters:
            for device in devices:
                match = True

                for key, value in filter_param.items():
                    if key == "management_ip_address":
                        device_ip = self.transform_device_management_ip(device)
                        if device_ip != value:
                            match = False
                            break

                    elif key == "site_name_hierarchy":
                        site_hierarchy = self.transform_device_site_hierarchy(device)
                        # Handle site_name_hierarchy as list
                        if isinstance(value, list):
                            if site_hierarchy not in value:
                                match = False
                                break
                        else:
                            if site_hierarchy != value:
                                match = False
                                break

                    elif key == "device_family":
                        device_family = self.transform_device_family_info(device)
                        if device_family != value:
                            match = False
                            break

                if match and device not in filtered_devices:
                    filtered_devices.append(device)

        return filtered_devices

    def process_device_list(self, devices, is_wireless=False):
        """
        Process device list into configuration format.

        Args:
            devices (list): List of devices to process
            is_wireless (bool): Whether these are wireless devices

        Returns:
            list: List of device configurations
        """
        device_configs = []

        for device in devices:
            device_id = device.get("networkDeviceId")

            management_ip = self.transform_device_management_ip(device)
            if not management_ip:
                self.log("Skipping device without management IP: {0}".format(device_id), "WARNING")
                continue

            site_hierarchy = self.transform_device_site_hierarchy(device)
            if not site_hierarchy:
                self.log("Skipping device without site hierarchy: {0}".format(device_id), "WARNING")
                continue

            device_config = {
                "management_ip_address": management_ip,
                "site_name_hierarchy": site_hierarchy,
                "provisioning": True,
                "force_provisioning": False
            }

            if is_wireless:
                primary_locations, secondary_locations = self.get_wireless_ap_locations(device)
                device_config["primary_managed_ap_locations"] = primary_locations if primary_locations else []
                device_config["secondary_managed_ap_locations"] = secondary_locations if secondary_locations else []

            device_configs.append(device_config)

        return device_configs

    def transform_device_site_hierarchy(self, device_details):
        """
        Transforms device site hierarchy from site ID to site name hierarchy.

        Args:
            device_details (dict): Device details containing site ID information.

        Returns:
            str: Site name hierarchy corresponding to the site ID.
        """
        device_id = device_details.get("networkDeviceId")
        self.log("Transforming device site hierarchy for device: {0}".format(device_id), "DEBUG")

        # Get site details from device
        site_id = device_details.get("siteId")
        self.log("Device {0} has siteId: {1}".format(device_id, site_id), "DEBUG")

        # If we have a site ID, try to get site name from mapping
        if site_id:
            site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
            if site_name_hierarchy:
                self.log("Site ID {0} mapped to hierarchy: {1}".format(site_id, site_name_hierarchy), "DEBUG")
                return site_name_hierarchy
            else:
                self.log("WARNING: Site ID {0} not found in site mapping".format(site_id), "WARNING")

        # Fallback: If no siteId or mapping failed, get it from device detail API
        if not site_id or not site_name_hierarchy:
            self.log("Fallback: Getting site hierarchy from device detail API for device {0}".format(device_id), "DEBUG")
            try:
                # Get device details to find location/site information
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_detail",
                    op_modifies=False,
                    params={"search_by": device_id, "identifier": "uuid"},
                )
                self.log("Recived API response: {0}".format(response), "DEBUG")
                device_info = response.get("response", {})
                location = device_info.get("location")
                site_hierarchy_graph_id = device_info.get("siteHierarchyGraphId")

                self.log("Device detail - location: {0}, siteHierarchyGraphId: {1}".format(
                    location, site_hierarchy_graph_id), "DEBUG")

                # Try location field first
                if location and location.strip():
                    self.log("Using location field for site hierarchy: {0}".format(location), "DEBUG")
                    return location

                # Try to extract from siteHierarchyGraphId
                if site_hierarchy_graph_id:
                    # The siteHierarchyGraphId contains path like: /id1/id2/id3/
                    # We need to find the corresponding site name
                    site_id_parts = site_hierarchy_graph_id.strip('/').split('/')
                    if site_id_parts:
                        # Try the last site ID in the hierarchy
                        last_site_id = site_id_parts[-1]
                        site_name = self.site_id_name_dict.get(last_site_id)
                        if site_name:
                            self.log("Found site hierarchy from siteHierarchyGraphId: {0}".format(site_name), "DEBUG")
                            return site_name

            except Exception as e:
                self.log("Error getting device details for site hierarchy: {0}".format(str(e)), "WARNING")

        # Final fallback: Check if this is a wireless controller with provision status
        if not site_name_hierarchy and device_details.get("deviceType") == "WirelessController":
            try:
                # Get management IP first
                management_ip = self.transform_device_management_ip(device_details)
                if management_ip:
                    # Check provision status to get site hierarchy
                    provision_response = self.dnac._exec(
                        family="sda",
                        function="get_provisioned_wired_device",
                        op_modifies=False,
                        params={"device_management_ip_address": management_ip}
                    )
                    self.log("Recived API response: {0}".format(provision_response), "DEBUG")
                    provision_site_hierarchy = provision_response.get("siteNameHierarchy")
                    if provision_site_hierarchy:
                        self.log("Got site hierarchy from provision status: {0}".format(provision_site_hierarchy), "DEBUG")
                        return provision_site_hierarchy

            except Exception as e:
                self.log("Error getting site hierarchy from provision status: {0}".format(str(e)), "WARNING")

        # If all methods failed
        self.log("Could not determine site hierarchy for device {0}".format(device_id), "WARNING")
        return None

    def transform_device_family_info(self, device_details):
        """
        Transforms device family information by fetching device details from network device API.

        Args:
            device_details (dict): Device details containing network device ID.

        Returns:
            str: Device family type (e.g., 'Switches and Hubs', 'Wireless Controller').
        """
        device_id = device_details.get("networkDeviceId")
        self.log("Transforming device family info for device ID: {0}".format(device_id), "DEBUG")

        if not device_id:
            self.log("No network device ID found for device family lookup", "ERROR")
            return None

        try:
            # Get device details
            response = self.dnac._exec(
                family="devices",
                function="get_device_detail",
                op_modifies=False,
                params={"search_by": device_id, "identifier": "uuid"},
            )
            self.log("Recived API response: {0}".format(response), "DEBUG")
            device_info = response.get("response", {})
            # FIXED: Use nwDeviceFamily instead of family
            device_family = device_info.get("nwDeviceFamily")

            # Log additional device info for debugging
            device_type = device_info.get("nwDeviceType")
            device_name = device_info.get("nwDeviceName")
            management_ip = device_info.get("managementIpAddr")

            self.log("Device details - ID: {0}, Name: {1}, IP: {2}, Family: {3}, Type: {4}".format(
                device_id, device_name, management_ip, device_family, device_type), "INFO")

            return device_family

        except Exception as e:
            self.log("Error getting device family for ID {0}: {1}".format(device_id, str(e)), "ERROR")
            return None

    def transform_device_management_ip(self, device_details):
        """
        Transforms device management IP by fetching device details from network device API.

        Args:
            device_details (dict): Device details containing network device ID.

        Returns:
            str: Device management IP address.
        """
        self.log("Transforming device management IP for device: {0}".format(device_details.get("networkDeviceId")), "DEBUG")

        device_id = device_details.get("networkDeviceId")
        if not device_id:
            return None

        try:
            # Get device details
            response = self.dnac._exec(
                family="devices",
                function="get_device_detail",
                op_modifies=False,
                params={"search_by": device_id, "identifier": "uuid"},
            )
            self.log("Recived API response: {0}".format(response), "error")
            device_info = response.get("response", {})
            self.log("Device information extracted: {0}".format(device_info), "DEBUG")

            # Return the actual IP address
            management_ip = device_info.get("managementIpAddr")
            self.log("Extracted management IP: {0}".format(management_ip), "DEBUG")
            return management_ip

        except Exception as e:
            self.log("Error getting device IP for ID {0}: {1}".format(device_id, str(e)), "ERROR")
            return None

    def get_wireless_ap_locations(self, device_details):
        """
        Gets primary and secondary managed AP locations for a wireless controller.

        Args:
            device_details (dict): Device details containing network device ID.

        Returns:
            tuple: (primary_ap_locations, secondary_ap_locations) - both as lists of site hierarchies
        """
        self.log(device_details, "DEBUG")
        device_id = device_details.get("networkDeviceId")
        self.log("Getting wireless AP locations for device ID: {0}".format(device_id), "DEBUG")

        if not device_id:
            self.log("No network device ID found for wireless AP location lookup", "ERROR")
            return [], []

        primary_ap_locations = []
        secondary_ap_locations = []

        # Get Primary Managed AP Locations (MANDATORY for provisioned WLC)
        try:
            self.log("Fetching primary managed AP locations for device ID: {0}".format(device_id), "INFO")
            primary_response = self.dnac._exec(
                family="wireless",
                function="get_primary_managed_ap_locations_for_specific_wireless_controller",
                op_modifies=False,
                params={"network_device_id": device_id},
            )
            self.log("Recived API response: {0}".format(primary_response), "DEBUG")

            # FIXED: Handle the response structure correctly
            if "response" in primary_response:
                response_data = primary_response.get("response", {})
                # The actual data is in managedApLocations array
                managed_ap_locations = response_data.get("managedApLocations", [])

                if managed_ap_locations:
                    self.log("Found {0} primary AP locations for device {1}".format(len(managed_ap_locations), device_id), "INFO")
                    for i, location in enumerate(managed_ap_locations):
                        site_id = location.get("siteId")
                        site_name_hierarchy = location.get("siteNameHierarchy")

                        self.log("Primary location {0}: siteId={1}, siteNameHierarchy={2}".format(i + 1, site_id, site_name_hierarchy), "DEBUG")

                        if site_name_hierarchy:
                            # Use the siteNameHierarchy directly from the API response
                            primary_ap_locations.append(site_name_hierarchy)
                            self.log("Added primary AP location: {0}".format(site_name_hierarchy), "INFO")
                        elif site_id:
                            # Fallback to site mapping if siteNameHierarchy is missing
                            site_hierarchy = self.site_id_name_dict.get(site_id)
                            if site_hierarchy:
                                primary_ap_locations.append(site_hierarchy)
                                self.log("Added primary AP location: {0} (from site mapping)".format(site_hierarchy), "INFO")
                else:
                    self.log("No primary managed AP locations found for device {0}".format(device_id), "WARNING")
            else:
                self.log("Unexpected response format for primary AP locations", "WARNING")

        except Exception as e:
            self.log("Error getting primary managed AP locations for device ID {0}: {1}".format(device_id, str(e)), "ERROR")
            self.log("This could indicate the wireless controller is not fully configured or APIs are not available", "WARNING")

        # Get Secondary Managed AP Locations (OPTIONAL)
        try:
            self.log("Fetching secondary managed AP locations for device ID: {0}".format(device_id), "INFO")
            secondary_response = self.dnac._exec(
                family="wireless",
                function="get_secondary_managed_ap_locations_for_specific_wireless_controller",
                op_modifies=False,
                params={"network_device_id": device_id},
            )
            self.log("Received API response: {0}".format(secondary_response), "DEBUG")
            # FIXED: Handle the response structure correctly
            if "response" in secondary_response:
                response_data = secondary_response.get("response", {})
                # The actual data is in managedApLocations array
                managed_ap_locations = response_data.get("managedApLocations", [])

                if managed_ap_locations:
                    self.log("Found {0} secondary AP locations for device {1}".format(len(managed_ap_locations), device_id), "INFO")
                    for i, location in enumerate(managed_ap_locations):
                        site_id = location.get("siteId")
                        site_name_hierarchy = location.get("siteNameHierarchy")  # Direct from API response

                        self.log("Secondary location {0}: siteId={1}, siteNameHierarchy={2}".format(i + 1, site_id, site_name_hierarchy), "DEBUG")

                        if site_name_hierarchy:
                            # Use the siteNameHierarchy directly from the API response
                            secondary_ap_locations.append(site_name_hierarchy)
                            self.log("Added secondary AP location: {0}".format(site_name_hierarchy), "INFO")
                        elif site_id:
                            # Fallback to site mapping if siteNameHierarchy is missing
                            site_hierarchy = self.site_id_name_dict.get(site_id)
                            if site_hierarchy:
                                secondary_ap_locations.append(site_hierarchy)
                                self.log("Added secondary AP location: {0} (from site mapping)".format(site_hierarchy), "INFO")
                else:
                    self.log("No secondary managed AP locations found for device {0} - keeping as empty list".format(device_id), "INFO")
            else:
                self.log("Unexpected response format for secondary AP locations", "WARNING")

        except Exception as e:
            self.log("Error getting secondary managed AP locations for device ID {0}: {1}".format(device_id, str(e)), "WARNING")
            self.log("Secondary AP locations are optional, continuing with empty list", "INFO")

        # Final summary
        self.log("=== AP LOCATIONS SUMMARY for {0} ===".format(device_id), "INFO")
        self.log("Primary AP locations ({0}): {1}".format(len(primary_ap_locations), primary_ap_locations), "INFO")
        self.log("Secondary AP locations ({0}): {1}".format(len(secondary_ap_locations), secondary_ap_locations), "INFO")

        # Validation: For provisioned WLCs, primary should typically have locations
        if len(primary_ap_locations) == 0:
            self.log("WARNING: Provisioned wireless controller {0} has no primary AP locations configured".format(device_id), "WARNING")
            self.log("This could mean: 1) No APs are assigned yet, 2) WLC is newly provisioned, 3) Configuration pending", "WARNING")

        return primary_ap_locations, secondary_ap_locations

    def provisioned_devices_temp_spec(self):
        """
        Constructs a temporary specification for provisioned devices, defining the structure and types of attributes
        that will be used in the YAML configuration file.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of provisioned device attributes.
        """
        self.log("Generating temporary specification for provisioned devices.", "DEBUG")
        provisioned_devices = OrderedDict({
            "management_ip_address": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_device_management_ip,
            },
            "site_name_hierarchy": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_device_site_hierarchy,
            },
            "provisioning": {"type": "bool", "default": True},
            "force_provisioning": {"type": "bool", "default": False},
            "primary_managed_ap_locations": {
                "type": "list",
                "special_handling": True,
                "transform": self.get_primary_managed_ap_locations_for_device,
                "wireless_only": True,
            },
            "secondary_managed_ap_locations": {
                "type": "list",
                "special_handling": True,
                "transform": self.get_secondary_managed_ap_locations_for_device,
                "wireless_only": True,
            },
        })
        self.log("Temporary specification for provisioned devices generated: {0}".format(provisioned_devices), "DEBUG")
        return provisioned_devices

    def get_primary_managed_ap_locations_for_device(self, device_details):
        """
        Gets primary managed AP locations for a specific device.

        Args:
            device_details (dict): Device details containing network device ID.

        Returns:
            list: Primary managed AP locations as site hierarchies.
        """
        primary_locations, x = self.get_wireless_ap_locations(device_details)
        return primary_locations

    def get_secondary_managed_ap_locations_for_device(self, device_details):
        """
        Gets secondary managed AP locations for a specific device.

        Args:
            device_details (dict): Device details containing network device ID.

        Returns:
            list: Secondary managed AP locations as site hierarchies.
        """
        x, secondary_locations = self.get_wireless_ap_locations(device_details)
        return secondary_locations

    def non_provisioned_devices_temp_spec(self):
        """
        Constructs a temporary specification for non-provisioned devices, defining the structure and types of attributes
        that will be used in the YAML configuration file.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of non-provisioned device attributes.
        """
        self.log("Generating temporary specification for non-provisioned devices.", "DEBUG")
        non_provisioned_devices = OrderedDict({
            "management_ip_address": {
                "type": "str",
                "special_handling": False,  # Direct from device response
            },
            "site_name_hierarchy": {
                "type": "str",
                "special_handling": True,
                "transform": self.transform_device_site_hierarchy_from_device,
            },
            "provisioning": {"type": "bool", "default": False},  # Default to false for non-provisioned
            "force_provisioning": {"type": "bool", "default": False},
        })
        self.log("Temporary specification for non-provisioned devices generated: {0}".format(non_provisioned_devices), "DEBUG")
        return non_provisioned_devices

    def transform_device_site_hierarchy_from_device(self, device_details):
        """
        Transforms device site hierarchy from site ID to site name hierarchy for regular device objects.

        Args:
            device_details (dict): Device details from network device API containing site ID information.

        Returns:
            str: Site name hierarchy corresponding to the site ID.
        """
        self.log("Transforming device site hierarchy for device: {0}".format(device_details.get("id")), "DEBUG")

        # For regular devices, site information is in siteId field
        site_id = device_details.get("siteId")
        if not site_id:
            return None

        # Get site name from site mapping
        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        self.log("Site ID {0} mapped to hierarchy: {1}".format(site_id, site_name_hierarchy), "DEBUG")

        return site_name_hierarchy

    def get_provisioned_devices(self, network_element, component_specific_filters=None):
        """
        Retrieves provisioned devices based on the provided network element and component-specific filters.
        """
        self.log("Starting to retrieve provisioned devices", "INFO")

        try:
            # Get all provisioned devices from SDA API
            response = self.dnac._exec(
                family="sda",
                function="get_provisioned_devices",
                op_modifies=False,
            )
            self.log("Recived API response: {0}".format(response))
            sda_devices = response.get("response", [])
            self.log("Retrieved {0} devices from SDA provisioned devices API".format(len(sda_devices)), "INFO")

            # WORKAROUND: Check for missing wireless controllers
            self.log("=== CHECKING FOR MISSING WIRELESS CONTROLLERS ===", "INFO")

            # Get all devices and check which wireless controllers are provisioned
            all_devices_response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
            )
            self.log("Recived API response: {0}".format(all_devices_response), "DEBUG")
            all_devices = all_devices_response.get("response", [])

            wireless_controllers_found = []
            sda_device_ids = {device.get("networkDeviceId") for device in sda_devices}

            for device in all_devices:
                device_id = device.get("id")
                management_ip = device.get("managementIpAddress")

                # Skip if already in SDA list
                if device_id in sda_device_ids:
                    continue

                try:
                    # Check if this is a wireless controller
                    device_detail_response = self.dnac._exec(
                        family="devices",
                        function="get_device_detail",
                        op_modifies=False,
                        params={"search_by": device_id, "identifier": "uuid"},
                    )
                    self.log("Recived API response: {0}".format(device_detail_response), "DEBUG")
                    device_info = device_detail_response.get("response", {})
                    device_family = device_info.get("nwDeviceFamily")
                    device_name = device_info.get("nwDeviceName")

                    # If it's a wireless controller, check if it's provisioned
                    if device_family == "Wireless Controller":
                        self.log("Found wireless controller: {0} ({1})".format(device_name, management_ip), "INFO")

                        try:
                            # Check provision status using the provision status API
                            provision_response = self.dnac._exec(
                                family="sda",
                                function="get_provisioned_wired_device",
                                op_modifies=False,
                                params={"device_management_ip_address": management_ip}
                            )
                            self.log("Recived API response: {0}".format(provision_response), "DEBUG")
                            if provision_response.get("status") == "success":
                                self.log("Wireless controller {0} IS provisioned - adding to device list".format(management_ip), "INFO")

                                # Create a mock provisioned device entry compatible with SDA format
                                mock_device = {
                                    "networkDeviceId": device_id,
                                    "siteId": device.get("siteId"),
                                    "deviceType": "WirelessController"
                                }

                                # Add to our devices list
                                sda_devices.append(mock_device)
                                wireless_controllers_found.append(management_ip)

                            else:
                                self.log("Wireless controller {0} is not provisioned".format(management_ip), "DEBUG")

                        except Exception as e:
                            self.log("Error checking provision status for {0}: {1}".format(management_ip, str(e)), "WARNING")

                except Exception as e:
                    self.log("Error checking device {0}: {1}".format(device_id, str(e)), "DEBUG")

            self.log("Found {0} additional provisioned wireless controllers: {1}".format(
                len(wireless_controllers_found), wireless_controllers_found), "INFO")
            self.log("Total devices after wireless controller check: {0}".format(len(sda_devices)), "INFO")

            # Apply component-specific filters if provided
            if component_specific_filters:
                filtered_devices = []
                for filter_param in component_specific_filters:
                    for device in sda_devices:
                        match = True
                        for key, value in filter_param.items():
                            if key == "management_ip_address":
                                device_ip = self.transform_device_management_ip(device)
                                if device_ip != value:
                                    match = False
                                    break
                            elif key == "site_name_hierarchy":
                                site_hierarchy = self.transform_device_site_hierarchy(device)
                                if site_hierarchy != value:
                                    match = False
                                    break
                            elif key == "device_family":
                                device_family = self.transform_device_family_info(device)
                                if device_family != value:
                                    match = False
                                    break
                        if match and device not in filtered_devices:
                            filtered_devices.append(device)
                final_devices = filtered_devices
            else:
                final_devices = sda_devices

            # Process each device
            valid_device_details = []
            wireless_count = 0
            wired_count = 0

            for device in final_devices:
                device_id = device.get("networkDeviceId")

                # Get basic device info
                management_ip = self.transform_device_management_ip(device)
                if not management_ip:
                    self.log("yoooooooooooooooooooooo", "error")
                    self.log("Skipping device without management IP: {0}".format(device_id), "WARNING")
                    continue

                site_hierarchy = self.transform_device_site_hierarchy(device)
                if not site_hierarchy:
                    self.log("Skipping device without site hierarchy: {0} (IP: {1})".format(device_id, management_ip), "WARNING")
                    # For debugging, let's see what siteId we have
                    site_id = device.get("siteId")
                    self.log("Device {0} has siteId: {1}".format(management_ip, site_id), "WARNING")
                    if site_id and site_id in self.site_id_name_dict:
                        self.log("Site ID {0} maps to: {1}".format(site_id, self.site_id_name_dict[site_id]), "WARNING")
                    continue

                # Get device family
                device_family = self.transform_device_family_info(device)
                self.log("Processing device {0} with family: {1}".format(management_ip, device_family), "INFO")

                # Check if wireless
                is_wireless = device_family == "Wireless Controller"
                self.log("Device {0} is wireless: {1}".format(management_ip, is_wireless), "INFO")

                # Create device configuration
                device_config = {
                    "management_ip_address": management_ip,
                    "site_name_hierarchy": site_hierarchy,
                    "provisioning": True,
                    "force_provisioning": False
                }

                # Handle wireless-specific fields
                if is_wireless:
                    wireless_count += 1
                    self.log("PROCESSING WIRELESS CONTROLLER: {0}".format(management_ip), "INFO")

                    primary_locations, secondary_locations = self.get_wireless_ap_locations(device)
                    device_config["primary_managed_ap_locations"] = primary_locations if primary_locations else []
                    device_config["secondary_managed_ap_locations"] = secondary_locations if secondary_locations else []

                    self.log("Wireless controller {0} - Primary: {1}, Secondary: {2}".format(
                        management_ip, primary_locations, secondary_locations), "INFO")
                else:
                    wired_count += 1
                    self.log("Wired device: {0}".format(management_ip), "DEBUG")

                valid_device_details.append(device_config)

            # Summary
            self.log("=== FINAL PROCESSING SUMMARY ===", "INFO")
            self.log("Total devices processed: {0}".format(len(valid_device_details)), "INFO")
            self.log("Wireless controllers: {0}".format(wireless_count), "INFO")
            self.log("Wired devices: {0}".format(wired_count), "INFO")

            if wireless_count > 0:
                self.log("SUCCESS: Found {0} wireless controller(s) in final output!".format(wireless_count), "INFO")
            else:
                self.log("WARNING: No wireless controllers found in final output", "WARNING")

            return valid_device_details

        except Exception as e:
            self.log("Error retrieving provisioned devices: {0}".format(str(e)), "ERROR")
            return []

    def get_non_provisioned_devices(self, network_element, component_specific_filters=None):
        """
        Retrieves devices that are assigned to sites but not yet provisioned.
        """
        self.log("=== STARTING NON-PROVISIONED DEVICE RETRIEVAL ===", "INFO")

        try:
            # STEP 1: Get ALL devices from Catalyst Center
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
            )
            self.log("Recived API response: {0}".format(response), "DEBUG")
            all_devices = response.get("response", [])
            self.log("STEP 1: Retrieved {0} total devices from Catalyst Center".format(len(all_devices)), "INFO")

            if not all_devices:
                self.log("ERROR: No devices found in Catalyst Center!", "ERROR")
                return []

            # STEP 2: Get all provisioned devices to exclude them
            try:
                provisioned_response = self.dnac._exec(
                    family="sda",
                    function="get_provisioned_devices",
                    op_modifies=False,
                )
                self.log("Recived API response: {0}".format(provisioned_response), "DEBUG")
                provisioned_devices = provisioned_response.get("response", [])
                provisioned_device_ids = {device.get("networkDeviceId") for device in provisioned_devices}

                # ALSO exclude provisioned wireless controllers found via workaround
                # Get all devices and check for provisioned wireless controllers
                for device in all_devices:
                    device_id = device.get("id")
                    management_ip = device.get("managementIpAddress")

                    if device_id in provisioned_device_ids:
                        continue

                    try:
                        # Check if this is a wireless controller
                        device_detail_response = self.dnac._exec(
                            family="devices",
                            function="get_device_detail",
                            op_modifies=False,
                            params={"search_by": device_id, "identifier": "uuid"},
                        )
                        self.log("Recived API response: {0}".format(device_detail_response), "DEBUG")
                        device_info = device_detail_response.get("response", {})
                        device_family = device_info.get("nwDeviceFamily")

                        # If it's a wireless controller, check if it's provisioned
                        if device_family == "Wireless Controller":
                            try:
                                provision_response = self.dnac._exec(
                                    family="sda",
                                    function="get_provisioned_wired_device",
                                    op_modifies=False,
                                    params={"device_management_ip_address": management_ip}
                                )
                                self.log("Recived API response: {0}".format(provision_response), "DEBUG")
                                if provision_response.get("status") == "success":
                                    # This wireless controller is provisioned, exclude it
                                    provisioned_device_ids.add(device_id)
                                    self.log("Excluding provisioned wireless controller: {0}".format(management_ip), "INFO")

                            except Exception as e:
                                pass  # Continue if provision check fails

                    except Exception as e:
                        pass  # Continue if device detail check fails

                self.log("STEP 2: Found {0} total provisioned devices to exclude (including wireless controllers)".format(len(provisioned_device_ids)), "INFO")

            except Exception as e:
                self.log("STEP 2 WARNING: Could not get provisioned devices: {0}".format(str(e)), "WARNING")
                provisioned_device_ids = set()

            # STEP 3: Filter devices - find those assigned to sites but not provisioned
            site_assigned_non_provisioned = []

            for i, device in enumerate(all_devices, 1):
                device_id = device.get("id")
                management_ip = device.get("managementIpAddress")
                hostname = device.get("hostname", "Unknown")
                site_id = device.get("siteId")

                self.log("STEP 3.{0}: Processing device - ID: {1}, IP: {2}, Hostname: {3}, SiteId: {4}".format(
                    i, device_id, management_ip, hostname, site_id), "DEBUG")

                # Skip devices without basic info
                if not device_id or not management_ip:
                    self.log("  -> SKIPPED: Missing device ID or management IP", "DEBUG")
                    continue

                # Skip if device is already provisioned
                if device_id in provisioned_device_ids:
                    self.log("  -> SKIPPED: Device is already provisioned", "DEBUG")
                    continue

                # EXCLUDE ACCESS POINTS - Check device family
                try:
                    device_detail_response = self.dnac._exec(
                        family="devices",
                        function="get_device_detail",
                        op_modifies=False,
                        params={"search_by": device_id, "identifier": "uuid"},
                    )
                    self.log("Recived API response: {0}".format(device_detail_response), "DEBUG")
                    device_info = device_detail_response.get("response", {})
                    device_family = device_info.get("nwDeviceFamily")
                    device_type = device_info.get("nwDeviceType")

                    # SKIP ACCESS POINTS
                    if device_family in ["Unified AP", "Access Points"] or "Access Point" in str(device_type):
                        self.log("  -> SKIPPED: Access Point - {0} (Family: {1}, Type: {2})".format(
                            management_ip, device_family, device_type), "DEBUG")
                        continue

                    self.log("  -> Device family: {0}, type: {1}".format(device_family, device_type), "DEBUG")

                except Exception as e:
                    self.log("  -> WARNING: Could not get device family for {0}: {1}".format(management_ip, str(e)), "WARNING")

                # Check if device is assigned to a site
                is_site_assigned = False

                # Method 1: Check siteId directly from device response
                if site_id:
                    site_name = self.site_id_name_dict.get(site_id)
                    if site_name:
                        is_site_assigned = True
                        self.log("  -> SITE ASSIGNED via siteId: {0} -> {1}".format(site_id, site_name), "DEBUG")

                # Method 2: If no siteId, check via device detail API (already called above)
                if not is_site_assigned:
                    try:
                        location = device_info.get("location")  # Use already fetched device_info

                        if location and location != "":
                            is_site_assigned = True
                            # Update the device with location info if siteId was missing
                            if not site_id:
                                # Try to find the site ID from location hierarchy
                                for sid, site_name in self.site_id_name_dict.items():
                                    if site_name == location:
                                        device["siteId"] = sid
                                        break
                            self.log("  -> SITE ASSIGNED via location: {0}".format(location), "DEBUG")

                    except Exception as detail_error:
                        self.log("  -> ERROR getting device details: {0}".format(str(detail_error)), "ERROR")

                # Add device if it's assigned to a site but not provisioned
                if is_site_assigned:
                    self.log("  -> ADDING: Device is site-assigned but not provisioned", "INFO")
                    site_assigned_non_provisioned.append(device)
                else:
                    self.log("  -> SKIPPED: Device is not assigned to any site", "DEBUG")

            self.log("STEP 3 SUMMARY:", "INFO")
            self.log("  - Total devices processed: {0}".format(len(all_devices)), "INFO")
            self.log("  - Provisioned devices excluded: {0}".format(len(provisioned_device_ids)), "INFO")
            self.log("  - Non-provisioned site-assigned devices found: {0}".format(len(site_assigned_non_provisioned)), "INFO")

            if not site_assigned_non_provisioned:
                self.log("RESULT: No non-provisioned site-assigned devices found.", "INFO")
                return []

            # STEP 4: Apply component-specific filters if provided
            filtered_devices = site_assigned_non_provisioned
            if component_specific_filters:
                self.log("STEP 4: Applying component-specific filters: {0}".format(component_specific_filters), "DEBUG")
                filtered_devices = []

                for filter_param in component_specific_filters:
                    for device in site_assigned_non_provisioned:
                        match = True

                        for key, value in filter_param.items():
                            if key == "management_ip_address":
                                if device.get("managementIpAddress") != value:
                                    match = False
                                    break
                            elif key == "site_name_hierarchy":
                                site_id = device.get("siteId")
                                site_hierarchy = self.site_id_name_dict.get(site_id) if site_id else None
                                if site_hierarchy != value:
                                    match = False
                                    break

                        if match and device not in filtered_devices:
                            filtered_devices.append(device)

                self.log("STEP 4: After filtering, {0} devices remain".format(len(filtered_devices)), "INFO")

            # STEP 5: Transform devices for YAML output
            self.log("STEP 5: Transforming {0} devices for YAML output".format(len(filtered_devices)), "INFO")

            final_devices = []
            for device in filtered_devices:
                management_ip = device.get("managementIpAddress")
                site_id = device.get("siteId")
                site_hierarchy = self.site_id_name_dict.get(site_id) if site_id else None

                # Skip devices without required fields
                if not management_ip or not site_hierarchy:
                    self.log("  -> SKIPPED device: missing IP ({0}) or site hierarchy ({1})".format(
                        management_ip, site_hierarchy), "WARNING")
                    continue

                device_config = {
                    "management_ip_address": management_ip,
                    "site_name_hierarchy": site_hierarchy,
                    "provisioning": False,  # These devices need to be provisioned
                    "force_provisioning": False
                }

                final_devices.append(device_config)
                self.log("  -> ADDED: {0} at {1}".format(management_ip, site_hierarchy), "INFO")

            self.log("FINAL RESULT: {0} non-provisioned site-assigned devices ready for YAML".format(len(final_devices)), "INFO")
            return final_devices

        except Exception as e:
            self.log("CRITICAL ERROR in get_non_provisioned_devices: {0}".format(str(e)), "ERROR")
            return []

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves provisioned device details using component-specific filters, processes the data,
        and writes the YAML content to a specified file.

        Args:
            yaml_config_generator (dict): Contains file_path, global_filters, and component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """
        self.log("Starting YAML config generation with parameters: {0}".format(yaml_config_generator), "DEBUG")

        # Handle file_path - FIXED: Use the provided file_path from config
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            file_path = self.generate_filename()

        self.log("File path determined: {0}".format(file_path), "DEBUG")

        # Get global and component-specific filters
        global_filters = yaml_config_generator.get("global_filters") or {}
        component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        self.log("Global filters: {0}".format(global_filters), "DEBUG")
        self.log("Component-specific filters: {0}".format(component_specific_filters), "DEBUG")

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_schema.get("network_elements", {})
        components_list = component_specific_filters.get("components_list", module_supported_network_elements.keys())
        self.log("Components to process: {0}".format(components_list), "DEBUG")

        # Collect all devices
        all_devices = []
        for component in components_list:
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log("Skipping unsupported network element: {0}".format(component), "WARNING")
                continue

            filters = component_specific_filters.get(component, [])
            operation_func = network_element.get("get_function_name")

            if callable(operation_func):
                device_list = operation_func(network_element, filters)
                self.log("Retrieved {0} devices for component {1}".format(len(device_list), component), "DEBUG")
                all_devices.extend(device_list)

        self.log("Total devices before global filters: {0}".format(len(all_devices)), "DEBUG")

        # Apply global filters FIRST before continuing
        if global_filters.get("management_ip_address"):
            ip_filter_list = global_filters["management_ip_address"]
            if not isinstance(ip_filter_list, list):
                ip_filter_list = [ip_filter_list]

            self.log("Applying global IP filter: {0}".format(ip_filter_list), "INFO")

            # Log all device IPs before filtering
            device_ips = [device.get("management_ip_address") for device in all_devices]
            self.log("Available device IPs BEFORE filtering: {0}".format(device_ips), "INFO")

            filtered_devices = []
            for device in all_devices:
                device_ip = device.get("management_ip_address")
                if device_ip in ip_filter_list:
                    self.log("Device {0} matches global filter - KEEPING".format(device_ip), "INFO")
                    filtered_devices.append(device)
                else:
                    self.log("Device {0} does NOT match global filter - REMOVING".format(device_ip), "DEBUG")

            all_devices = filtered_devices
            self.log("After global IP filter: {0} devices remain".format(len(all_devices)), "INFO")

            # Log remaining device IPs after filtering
            remaining_ips = [device.get("management_ip_address") for device in all_devices]
            self.log("Remaining device IPs AFTER filtering: {0}".format(remaining_ips), "INFO")

        if not all_devices:
            self.msg = "No devices found matching the provided filters for module '{0}'. Global filters: {1}, Component filters: {2}".format(
                self.module_name, global_filters, component_specific_filters
            )
            self.set_operation_result("ok", False, self.msg, "WARNING")
            return self

        # Create the final structure
        final_dict = {"config": all_devices}
        self.log("Final dictionary created with {0} devices".format(len(all_devices)), "DEBUG")

        # WRITE TO THE CORRECT FILE PATH
        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(self.module_name):
                {"file_path": file_path, "devices_count": len(all_devices)}
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(self.module_name):
                {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.

        Args:
            config (dict): The configuration data for the provision elements.
            state (str): The desired state ('gathered').
        """
        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        want = {}
        # FIXED: Pass the entire config including global_filters
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator added to want: {0}".format(
                want["yaml_config_generator"]
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Provision operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the merge operations for provision configurations in the Cisco Catalyst Center.
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

    def generate_filename(self):
        """
        Generates a default filename for the YAML configuration file.

        Returns:
            str: Default filename with timestamp.
        """
        from datetime import datetime

        # Generate timestamp in the format DD_Mon_YYYY_HH_MM_SS_MS
        now = datetime.now()
        timestamp = now.strftime("%d_%b_%Y_%H_%M_%S_%f")[:-3]  # Remove last 3 digits from microseconds

        # Generate filename: <module_name>_playbook_<timestamp>.yml
        filename = "{0}_playbook_{1}.yml".format(self.module_name, timestamp)

        self.log("Generated default filename: {0}".format(filename), "DEBUG")
        return filename

    def is_device_assigned_to_site(self, uuid):
        """
        Checks if a device is assigned to any site by checking multiple fields.
        """
        self.log("Checking site assignment for device with UUID: {0}".format(uuid), "DEBUG")

        try:
            site_response = self.dnac._exec(
                family="devices",
                function="get_device_detail",
                op_modifies=False,
                params={"search_by": uuid, "identifier": "uuid"},
            )
            self.log("Recived API response: {0}".format(site_response), "DEBUG")

            device_info = site_response.get("response", {})

            # Check for site assignment using multiple possible fields
            site_id = device_info.get("siteId")
            location_name = device_info.get("locationName")
            location = device_info.get("location")
            site_hierarchy_graph_id = device_info.get("siteHierarchyGraphId")

            self.log("Device site info - siteId: {0}, locationName: {1}, location: {2}, siteHierarchyGraphId: {3}".format(
                site_id, location_name, location, site_hierarchy_graph_id), "DEBUG")

            # Device is assigned to site if any of these conditions are met
            if site_id or location_name or location or site_hierarchy_graph_id:
                self.log("Device {0} IS assigned to a site".format(uuid), "DEBUG")
                return True
            else:
                self.log("Device {0} is NOT assigned to any site".format(uuid), "DEBUG")
                return False

        except Exception as e:
            self.log("Error checking site assignment for device {0}: {1}".format(uuid, str(e)), "ERROR")
            return False


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

    # Initialize the ProvisionPlaybookGenerator object with the module
    ccc_provision_playbook_generator = ProvisionPlaybookGenerator(module)

    # Check version compatibility
    if (
        ccc_provision_playbook_generator.compare_dnac_versions(
            ccc_provision_playbook_generator.get_ccc_version(), "2.3.5.3"
        )
        < 0
    ):
        ccc_provision_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Provision Management Module. Supported versions start from '2.3.5.3' onwards. "
            "Version '2.3.5.3' introduces APIs for retrieving provisioned device settings from "
            "the Catalyst Center".format(
                ccc_provision_playbook_generator.get_ccc_version()
            )
        )
        ccc_provision_playbook_generator.set_operation_result(
            "failed", False, ccc_provision_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_provision_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_provision_playbook_generator.supported_states:
        ccc_provision_playbook_generator.status = "invalid"
        ccc_provision_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_provision_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_provision_playbook_generator.validate_input().check_return_status()
    config = ccc_provision_playbook_generator.validated_config

    # FIXED: Preserve file_path when adding default components_list
    if len(config) == 1:
        current_config = config[0]

        # If component_specific_filters is missing, add default
        if current_config.get("component_specific_filters") is None:
            current_config['component_specific_filters'] = {
                'components_list': ["wired", "wireless"]
            }
            ccc_provision_playbook_generator.validated_config = [current_config]
            ccc_provision_playbook_generator.msg = (
                "No 'component_specific_filters' found. Adding default components: ['wired', 'wireless']"
            )

    # Iterate over the validated configuration parameters
    for config in ccc_provision_playbook_generator.validated_config:
        ccc_provision_playbook_generator.reset_values()
        ccc_provision_playbook_generator.get_want(config, state).check_return_status()
        ccc_provision_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_provision_playbook_generator.result)


if __name__ == "__main__":
    main()

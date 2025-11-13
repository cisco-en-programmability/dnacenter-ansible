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
    choices: [merged]
    default: merged
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
              - Provisioned Devices "provisioned_devices"
              - Non-Provisioned Devices "non_provisioned_devices"
            - If not specified, all components are included.
            - For example, ["provisioned_devices", "non_provisioned_devices"].
            type: list
            elements: str
          provisioned_devices:
            description:
            - Provisioned devices to filter devices by management IP, site name, or device family.
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
                type: str
              device_family:
                description:
                - Device family to filter devices by type (e.g., 'Switches and Hubs', 'Wireless Controller').
                type: str
          non_provisioned_devices:
            description:
            - Non-provisioned devices to filter devices by management IP, site name, or device family.
            - These are devices that are assigned to sites but not yet provisioned.
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
                type: str
              device_family:
                description:
                - Device family to filter devices by type (e.g., 'Switches and Hubs', 'Wireless Controller').
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
- Paths used are
    - GET /dna/intent/api/v1/sda/provisioned-devices
    - GET /dna/intent/api/v1/network-device/ip-address/{ipAddress}
    - GET /dna/intent/api/v1/network-device/{id}/detail
    - GET /dna/intent/api/v1/site
    - GET /dna/intent/api/v1/wireless/accesspoint-configuration/summary
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
    state: merged
    config:
      - file_path: "/tmp/catc_provision_config.yaml"

- name: Generate YAML Configuration with specific provisioned devices filter
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
    state: merged
    config:
      - file_path: "/tmp/catc_provision_config.yaml"
        component_specific_filters:
          components_list: ["provisioned_devices"]

- name: Generate YAML Configuration for devices with IP address filter
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
    state: merged
    config:
      - file_path: "/tmp/catc_provision_config.yaml"
        component_specific_filters:
          components_list: ["provisioned_devices"]
          provisioned_devices:
            - management_ip_address: "204.192.3.40"
            - management_ip_address: "204.192.12.201"

- name: Generate YAML Configuration for devices with site filter
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
    state: merged
    config:
      - file_path: "/tmp/catc_provision_config.yaml"
        component_specific_filters:
          components_list: ["provisioned_devices"]
          provisioned_devices:
            - site_name_hierarchy: "Global/USA/San Francisco/BGL_18"

- name: Generate YAML Configuration for all provisioned devices
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
    state: merged
    config:
      - file_path: "/tmp/catc_provision_config.yaml"
        component_specific_filters:
          components_list: ["provisioned_devices"]

- name: Generate YAML Configuration for non-provisioned devices only
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
    state: merged
    config:
      - file_path: "/tmp/catc_non_provisioned_config.yaml"
        component_specific_filters:
          components_list: ["non_provisioned_devices"]

- name: Generate YAML Configuration for both provisioned and non-provisioned devices
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
    state: merged
    config:
      - file_path: "/tmp/catc_all_devices_config.yaml"
        component_specific_filters:
          components_list: ["provisioned_devices", "non_provisioned_devices"]

- name: Generate YAML Configuration for non-provisioned devices with specific site filter
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
    state: merged
    config:
      - file_path: "/tmp/catc_site_non_provisioned_config.yaml"
        component_specific_filters:
          components_list: ["non_provisioned_devices"]
          non_provisioned_devices:
            - site_name_hierarchy: "Global/USA/San Francisco/BGL_18"
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
        self.supported_states = ["merged"]
        super().__init__(module)
        self.module_name = "provision_workflow_manager"
        self.module_schema = self.provision_workflow_manager_mapping()
        self.log("Initialized ProvisionPlaybookGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")
        self.site_id_name_dict = self.get_site_id_name_mapping()

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
                "provisioned_devices": {
                    "filters": ["management_ip_address", "site_name_hierarchy", "device_family"],
                    "temp_spec_function": self.provisioned_devices_temp_spec,
                    "api_function": "get_provisioned_devices",
                    "api_family": "sda",
                    "get_function_name": self.get_provisioned_devices,
                },
                "non_provisioned_devices": {
                    "filters": ["management_ip_address", "site_name_hierarchy", "device_family"],
                    "temp_spec_function": self.non_provisioned_devices_temp_spec,
                    "api_function": "get_device_list",  # FIXED: Correct API function name
                    "api_family": "devices",
                    "get_function_name": self.get_non_provisioned_devices,
                },
            },
            "global_filters": [],
        }

        self.log("Constructed provision workflow manager mapping: {0}".format(tempspec), "DEBUG")
        return tempspec

    def transform_device_site_hierarchy(self, device_details):
        """
        Transforms device site hierarchy from site ID to site name hierarchy.
        
        Args:
            device_details (dict): Device details containing site ID information.
            
        Returns:
            str: Site name hierarchy corresponding to the site ID.
        """
        self.log("Transforming device site hierarchy for device: {0}".format(device_details.get("networkDeviceId")), "DEBUG")
        
        # Get site details from device
        site_id = device_details.get("siteId")
        if not site_id:
            return None
            
        # Get site name from site mapping
        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        
        return site_name_hierarchy

    def transform_device_family_info(self, device_details):
        """
        Transforms device family information by fetching device details from network device API.
        
        Args:
            device_details (dict): Device details containing network device ID.
            
        Returns:
            str: Device family type (e.g., 'Switches and Hubs', 'Wireless Controller').
        """
        self.log("Transforming device family info for device: {0}".format(device_details.get("networkDeviceId")), "DEBUG")
        
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
            
            device_info = response.get("response", {})
            return device_info.get("family")
            
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
            self.log("Device details response: {0}".format(response), "DEBUG")
            device_info = response.get("response", {})
            self.log("Device information extracted: {0}".format(device_info), "DEBUG")
            
            # FIXED: Return the actual IP address
            management_ip = device_info.get("managementIpAddr")
            self.log("Extracted management IP: {0}".format(management_ip), "DEBUG")
            return management_ip  # <-- This line was missing!
            
        except Exception as e:
            self.log("Error getting device IP for ID {0}: {1}".format(device_id, str(e)), "ERROR")
            return None

    def transform_wireless_managed_ap_locations(self, device_details):
        """
        Transforms wireless managed AP locations for wireless controllers.
        
        Args:
            device_details (dict): Device details containing network device ID.
            
        Returns:
            list: List of managed AP location site hierarchies.
        """
        self.log("Transforming wireless managed AP locations for device: {0}".format(device_details.get("networkDeviceId")), "DEBUG")
        
        device_id = device_details.get("networkDeviceId")
        if not device_id:
            return []
            
        try:
            # Check if device is wireless controller first
            device_family = self.transform_device_family_info(device_details)
            if device_family != "Wireless Controller":
                return []
                
            # Get wireless configuration - this would need to be implemented based on actual API
            # For now, return empty list as we don't have a direct API to get managed AP locations
            # from provisioned devices
            managed_locations = []
            return managed_locations
            
        except Exception as e:
            self.log("Error getting wireless AP locations for device ID {0}: {1}".format(device_id, str(e)), "ERROR")
            return []

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
            # Add wireless-specific fields if device is wireless controller
            "managed_ap_locations": {
                "type": "list",
                "elements": "str",
                "special_handling": True,
                "transform": self.transform_wireless_managed_ap_locations,
            },
        })
        self.log("Temporary specification for provisioned devices generated: {0}".format(provisioned_devices), "DEBUG")
        return provisioned_devices

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
            # Add wireless-specific fields if device is wireless controller
            "managed_ap_locations": {
                "type": "list",
                "elements": "str",
                "special_handling": True,
                "transform": self.transform_wireless_managed_ap_locations_from_device,
            },
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

    def transform_wireless_managed_ap_locations_from_device(self, device_details):
        """
        Transforms wireless managed AP locations for wireless controllers from regular device objects.
        
        Args:
            device_details (dict): Device details from network device API.
            
        Returns:
            list: List of managed AP location site hierarchies.
        """
        self.log("Transforming wireless managed AP locations for device: {0}".format(device_details.get("id")), "DEBUG")
        
        device_family = device_details.get("family")
        if device_family != "Wireless Controller":
            return []
            
        try:
            # For wireless controllers, we would need to get managed AP locations
            # This is a placeholder - you might need to implement actual logic
            # based on your specific wireless controller configuration
            managed_locations = []
            return managed_locations
            
        except Exception as e:
            self.log("Error getting wireless AP locations for device ID {0}: {1}".format(device_details.get("id"), str(e)), "ERROR")
            return []

    def get_provisioned_devices(self, network_element, component_specific_filters=None):
        """
        Retrieves provisioned devices based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving provisioned devices.
            component_specific_filters (list, optional): A list of dictionaries containing filters for provisioned devices.

        Returns:
            dict: A dictionary containing the modified details of provisioned devices.
        """
        self.log(
            "Starting to retrieve provisioned devices with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        final_devices = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        
        self.log(
            "Getting provisioned devices using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        try:
            # Get all provisioned devices
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
            devices = response.get("response", [])
            self.log("Retrieved {0} provisioned devices from Catalyst Center".format(len(devices)), "INFO")

            if component_specific_filters:
                filtered_devices = []
                for filter_param in component_specific_filters:
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
                final_devices = devices

        except Exception as e:
            self.log("Error retrieving provisioned devices: {0}".format(str(e)), "ERROR")
            self.fail_and_exit("Failed to retrieve provisioned devices from Catalyst Center")

        # Modify device details using temp_spec
        provisioned_devices_temp_spec = self.provisioned_devices_temp_spec()
        device_details = self.modify_parameters(provisioned_devices_temp_spec, final_devices)
        
        # Filter out devices without management IP (invalid devices) and clean up the data
        valid_device_details = []
        for device in device_details:
            # Extract management IP - it should be populated now
            management_ip = device.get("management_ip_address")
            
            if management_ip:
                # Set default values for None fields
                if device.get("provisioning") is None:
                    device["provisioning"] = True
                if device.get("force_provisioning") is None:
                    device["force_provisioning"] = False
                    
                # Get device family to determine if wireless-specific cleanup is needed  
                device_family = None
                for orig_device in final_devices:
                    if device.get("site_name_hierarchy") == self.site_id_name_dict.get(orig_device.get("siteId")):
                        device_id = orig_device.get("networkDeviceId")
                        if device_id:
                            device_family = self.transform_device_family_info({"networkDeviceId": device_id})
                        break
                
                # Remove managed_ap_locations if empty or device is not wireless
                if not device.get("managed_ap_locations") or device_family != "Wireless Controller":
                    device.pop("managed_ap_locations", None)
                
                # Remove any internal fields used for processing
                device.pop("networkDeviceId", None)
                
                valid_device_details.append(device)

        self.log("Processed {0} valid provisioned devices".format(len(valid_device_details)), "INFO")
        return valid_device_details

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
                provisioned_devices = provisioned_response.get("response", [])
                provisioned_device_ids = {device.get("networkDeviceId") for device in provisioned_devices}
                self.log("STEP 2: Found {0} SDA provisioned devices to exclude".format(len(provisioned_device_ids)), "INFO")
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
                
                # Check if device is assigned to a site
                is_site_assigned = False
                
                # Method 1: Check siteId directly from device response
                if site_id:
                    site_name = self.site_id_name_dict.get(site_id)
                    if site_name:
                        is_site_assigned = True
                        self.log("  -> SITE ASSIGNED via siteId: {0} -> {1}".format(site_id, site_name), "DEBUG")
                
                # Method 2: If no siteId, check via device detail API
                if not is_site_assigned:
                    try:
                        device_detail_response = self.dnac._exec(
                            family="devices",
                            function="get_device_detail",
                            op_modifies=False,
                            params={"search_by": device_id, "identifier": "uuid"},
                        )
                        
                        device_detail = device_detail_response.get("response", {})
                        location = device_detail.get("location")
                        
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
                
                # Add wireless-specific config if it's a wireless controller
                device_family = device.get("family")
                if device_family == "Wireless Controller":
                    device_config["managed_ap_locations"] = []  # User needs to specify these
                
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
            yaml_config_generator (dict): Contains file_path and component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """
        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )
        
        # FIXED: Better handling of file_path
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            # Generate default filename if not provided
            file_path = self.generate_filename() if hasattr(self, 'generate_filename') else None
            if not file_path:
                # Fallback to a simple default filename
                from datetime import datetime
                timestamp = datetime.now().strftime("%d_%b_%Y_%H_%M_%S_%f")[:-3]
                file_path = "{0}_playbook_{1}.yml".format(self.module_name, timestamp)
    
        self.log("File path determined: {0}".format(file_path), "DEBUG")

        component_specific_filters = (
            yaml_config_generator.get("component_specific_filters") or {}
        )
        self.log(
            "Component-specific filters: {0}".format(component_specific_filters),
            "DEBUG",
        )

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_schema.get("network_elements", {})
        components_list = component_specific_filters.get(
            "components_list", module_supported_network_elements.keys()
        )
        self.log("Components to process: {0}".format(components_list), "DEBUG")

        # Collect all devices directly into a flat list
        all_devices = []
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
                device_list = operation_func(network_element, filters)
                self.log(
                    "Retrieved {0} devices for component {1}".format(len(device_list), component), "DEBUG"
                )
                
                # Extend the all_devices list with the retrieved devices
                all_devices.extend(device_list)

        if not all_devices:
            self.msg = "No provisioned devices found to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name
            )
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        # Create the final structure with devices directly under config
        final_dict = {"config": all_devices}
        self.log("Final dictionary created with {0} devices".format(len(all_devices)), "DEBUG")

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
            config (dict): The configuration data for the provision elements.
            state (str): The desired state ('merged').
        """
        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        want = {}
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

    def get_diff_merged(self):
        """
        Executes the merge operations for provision configurations in the Cisco Catalyst Center.
        """
        start_time = time.time()
        self.log("Starting 'get_diff_merged' operation.", "DEBUG")
        
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
            "Completed 'get_diff_merged' operation in {0:.2f} seconds.".format(
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
            
            self.log("Response collected from the API 'get_device_detail' {0}".format(site_response), "DEBUG")
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
        "state": {"default": "merged", "choices": ["merged"]},
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
    
    if len(config) == 1 and config[0].get("component_specific_filters") is None:
        ccc_provision_playbook_generator.msg = (
            "No valid configurations found in the provided parameters."
        )
        ccc_provision_playbook_generator.validated_config = [
            {
                'component_specific_filters': {
                    'components_list': ["provisioned_devices"]
                }
            }
        ]

    # Iterate over the validated configuration parameters
    for config in ccc_provision_playbook_generator.validated_config:
        ccc_provision_playbook_generator.reset_values()
        ccc_provision_playbook_generator.get_want(config, state).check_return_status()
        ccc_provision_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_provision_playbook_generator.result)


if __name__ == "__main__":
    main()
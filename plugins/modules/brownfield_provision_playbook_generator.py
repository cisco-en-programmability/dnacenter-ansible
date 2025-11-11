#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbook for Provision Workflow Management in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Abinash Mishra, Madhan Sankaranarayanan, Syed Khadeer Ahmed, Ajith Andrew J"

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
    type: list
    elements: dict
    required: true
    suboptions:
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name.
        type: str
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration file.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are "provisioned_devices"
            type: list
            elements: str
          site_name_hierarchy:
            description:
            - Site name hierarchy to filter devices by site.
            type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
- SDK Methods used are
    - devices.Devices.get_device_list
    - sites.Sites.get_site
    - site_design.SiteDesign.get_site_assigned_network_device
- Paths used are
    - GET /dna/intent/api/v1/network-device
    - GET /dna/intent/api/v1/site
    - GET /dna/intent/api/v1/site/{site-id}/device
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

- name: Generate YAML Configuration for all devices
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

- name: Generate YAML Configuration for specific site
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
          site_name_hierarchy: "Global/USA/San Francisco/BGL_18"
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
        """
        self.supported_states = ["merged"]
        super().__init__(module)
        self.module_name = "provision_workflow_manager"
        self.module_mapping = self.provision_workflow_manager_mapping()
        self.site_id_name_dict = self.get_site_id_name_mapping()

    def validate_input(self):
        """
        Validates the input configuration parameters for the playbook.
        """
        self.log("Starting validation of input configuration parameters.", "DEBUG")

        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        temp_spec = {
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
        }

        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters"
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def provision_workflow_manager_mapping(self):
        """
        Constructs and returns a structured mapping for managing provision workflow elements.
        """
        return {
            "network_elements": {
                "provisioned_devices": {
                    "filters": ["site_name_hierarchy"],
                    "temp_spec_function": self.provisioned_devices_temp_spec,
                    "get_function_name": self.get_provisioned_devices,
                },
            },
            "global_filters": [],
        }

    def provisioned_devices_temp_spec(self):
        """
        Constructs a temporary specification for provisioned devices.
        """
        self.log("Generating temporary specification for provisioned devices.", "DEBUG")
        provisioned_devices = OrderedDict({
            "management_ip_address": {"type": "str"},
            "site_name_hierarchy": {"type": "str"},
            "provisioning": {"type": "bool", "default": True},
            "force_provisioning": {"type": "bool", "default": False},
        })
        return provisioned_devices

    def get_all_devices_from_sites(self):
        """
        Get all devices that are assigned to sites.
        """
        self.log("Getting all devices assigned to sites", "INFO")
        
        try:
            # Get all sites
            sites_response = self.dnac._exec(
                family="sites",
                function="get_site",
                op_modifies=False,
            )
            
            sites = sites_response.get("response", [])
            self.log("Retrieved {0} sites from Catalyst Center".format(len(sites)), "DEBUG")
            
            all_devices = []
            
            for site in sites:
                site_id = site.get("id")
                site_name = site.get("siteNameHierarchy")
                
                if not site_id or not site_name:
                    continue
                    
                # Skip Global site
                if site_name == "Global":
                    continue
                
                try:
                    # Get devices assigned to this site
                    devices_response = self.dnac._exec(
                        family="site_design",
                        function="get_site_assigned_network_devices",
                        params={"id": site_id},
                        op_modifies=False,
                    )
                    
                    site_devices = devices_response.get("response", [])
                    self.log("Site '{0}' has {1} devices".format(site_name, len(site_devices)), "DEBUG")
                    
                    for device in site_devices:
                        device_info = {
                            "management_ip_address": device.get("managementIpAddress"),
                            "site_name_hierarchy": site_name,
                            "device_id": device.get("id"),
                            "device_family": device.get("family"),
                            "hostname": device.get("hostname"),
                        }
                        
                        # Only add devices with valid IP addresses
                        if device_info["management_ip_address"]:
                            all_devices.append(device_info)
                            
                except Exception as e:
                    self.log("Error getting devices for site {0}: {1}".format(site_name, str(e)), "WARNING")
                    continue
            
            self.log("Found total {0} devices assigned to sites".format(len(all_devices)), "INFO")
            return all_devices
            
        except Exception as e:
            self.log("Error getting devices from sites: {0}".format(str(e)), "ERROR")
            return []

    def get_provisioned_devices(self, network_element, component_specific_filters=None):
        """
        Retrieves provisioned devices based on the provided network element and component-specific filters.
        """
        self.log("Starting to retrieve provisioned devices", "DEBUG")

        # Get all devices assigned to sites
        all_devices = self.get_all_devices_from_sites()
        
        if not all_devices:
            self.log("No devices found assigned to sites", "WARNING")
            return []

        # Apply site filter if specified
        filtered_devices = all_devices
        if component_specific_filters:
            site_filter = component_specific_filters.get("site_name_hierarchy")
            if site_filter:
                filtered_devices = [
                    device for device in all_devices 
                    if device.get("site_name_hierarchy") == site_filter
                ]
                self.log("Filtered to {0} devices for site {1}".format(len(filtered_devices), site_filter), "INFO")

        # Transform devices to the required format
        provisioned_devices_temp_spec = self.provisioned_devices_temp_spec()
        final_devices = []
        
        for device in filtered_devices:
            device_config = OrderedDict()
            
            # Set required fields
            device_config["management_ip_address"] = device.get("management_ip_address")
            device_config["site_name_hierarchy"] = device.get("site_name_hierarchy")
            device_config["provisioning"] = True
            device_config["force_provisioning"] = False
            
            # Add wireless-specific fields if it's a wireless controller
            if device.get("device_family") == "Wireless Controller":
                device_config["managed_ap_locations"] = [device.get("site_name_hierarchy")]
            
            final_devices.append(device_config)

        self.log("Processed {0} provisioned devices".format(len(final_devices)), "INFO")
        return final_devices

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        """
        self.log("Starting YAML config generation", "DEBUG")
        
        file_path = yaml_config_generator.get("file_path", self.generate_filename())
        self.log("File path determined: {0}".format(file_path), "DEBUG")

        component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}
        self.log("Component-specific filters: {0}".format(component_specific_filters), "DEBUG")

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_mapping.get("network_elements", {})
        components_list = component_specific_filters.get("components_list", ["provisioned_devices"])
        self.log("Components to process: {0}".format(components_list), "DEBUG")

        # Collect all devices directly into a flat list
        all_devices = []
        for component in components_list:
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log("Skipping unsupported network element: {0}".format(component), "WARNING")
                continue

            operation_func = network_element.get("get_function_name")
            if callable(operation_func):
                # Pass the filters to the function
                device_list = operation_func(network_element, component_specific_filters)
                self.log("Retrieved {0} devices for component {1}".format(len(device_list), component), "DEBUG")
                all_devices.extend(device_list)

        if not all_devices:
            self.msg = "No devices found to process for module '{0}'. This could mean no devices are assigned to sites or meet the filter criteria.".format(
                self.module_name
            )
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        # Create the final structure with devices directly under config
        final_dict = {"config": all_devices}
        self.log("Final dictionary created with {0} devices".format(len(all_devices)), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(self.module_name): {
                    "file_path": file_path,
                    "devices_count": len(all_devices)
                }
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(self.module_name): {
                    "file_path": file_path
                }
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        """
        self.log("Creating Parameters for API Calls with state: {0}".format(state), "INFO")

        self.validate_params(config)

        want = {}
        want["yaml_config_generator"] = config
        self.log("yaml_config_generator added to want", "INFO")

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
        for index, (param_key, operation_name, operation_func) in enumerate(operations, start=1):
            self.log("Iteration {0}: Checking parameters for {1} operation with param_key '{2}'.".format(
                index, operation_name, param_key), "DEBUG")
            params = self.want.get(param_key)
            if params:
                self.log("Iteration {0}: Parameters found for {1}. Starting processing.".format(
                    index, operation_name), "INFO")
                operation_func(params).check_return_status()
            else:
                self.log("Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                    index, operation_name), "WARNING")

        end_time = time.time()
        self.log("Completed 'get_diff_merged' operation in {0:.2f} seconds.".format(
            end_time - start_time), "DEBUG")

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
        "state": {"default": "merged", "choices": ["merged"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    
    # Initialize the ProvisionPlaybookGenerator object with the module
    ccc_provision_playbook_generator = ProvisionPlaybookGenerator(module)
    
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
        ccc_provision_playbook_generator.msg = "No valid configurations found in the provided parameters."
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
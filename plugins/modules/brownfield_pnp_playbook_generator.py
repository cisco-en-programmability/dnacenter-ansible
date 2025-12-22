#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for PnP Workflow Manager Module with device_info only."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Syed Khadeer Ahmed, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_pnp_playbook_generator
short_description: Generate YAML configurations playbook for 'pnp_workflow_manager' module with device_info only.
description:
- Generates simplified YAML configurations compatible with the 'pnp_workflow_manager'
  module, containing only essential device information.
- The YAML configurations generated represent basic device details of PnP devices
  registered in the Cisco Catalyst Center PnP inventory.
- Extracts core device attributes like serial number, hostname, state, PID, and SUDI requirements.
- Does not include site assignments, templates, projects, or other advanced configuration parameters.
- Supports extraction of both claimed and unclaimed devices with their basic device information.
version_added: 6.40.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Syed Khadeer Ahmed (@syed-khadeerahmed)
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
      - A list of filters for generating simplified YAML playbook compatible with the 'pnp_workflow_manager' module.
      - Filters specify which devices to include in the YAML configuration file.
      - Generated YAML contains only device_info section with essential device details.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all PnP devices.
          - This mode discovers all devices in the PnP inventory and extracts only basic device information.
          - Generated configuration includes only device_info with core device attributes.
          - When enabled, the config parameter becomes optional and will use default values if not specified.
          - A default filename will be generated automatically if file_path is not specified.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name "pnp_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        type: str
        required: false
      component_specific_filters:
        description:
          - Component-specific filters to specify which PnP components to include.
          - Currently supports only 'device_info' component for basic device information extraction.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
              - List of PnP components to include in the YAML configuration file.
              - Only 'device_info' is supported for extracting basic device information.
              - If not specified, defaults to ['device_info'].
            type: list
            elements: str
            choices: ['device_info']
            default: ['device_info']
      global_filters:
        description:
          - Global filters to apply across all PnP device extraction.
          - Allows filtering devices by various attributes before extracting device_info.
        type: dict
        required: false
        suboptions:
          device_state:
            description:
              - Filter devices by their PnP state.
              - Valid values are ["Unclaimed", "Planned", "Onboarding", "Provisioned", "Error"]
              - If not specified, all device states are included.
            type: list
            elements: str
            required: false
            choices: ["Unclaimed", "Planned", "Onboarding", "Provisioned", "Error"]
          device_family:
            description:
              - Filter devices by product family.
              - Example ["Switches and Hubs", "Routers", "Wireless Controller"]
            type: list
            elements: str
            required: false
          site_name:
            description:
              - Filter devices by site name hierarchy.
              - Only devices claimed to sites matching this filter will be included.
              - Example "Global/USA/San Francisco"
            type: str
            required: false
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
- SDK Methods used are
  - device_onboarding_pnp.DeviceOnboardingPnp.get_device_list
  - sites.Sites.get_site (for site filtering only)
- Paths used are
  - GET /dna/intent/api/v1/onboarding/pnp-device
  - GET /dna/intent/api/v1/site (for site filtering only)
- Generated YAML contains only device_info section with basic device attributes
- Site assignments, templates, projects, and other advanced parameters are not included
- This module is designed for simple device inventory and basic PnP device management
"""

EXAMPLES = r"""
- name: Generate basic device info for all PnP devices
  cisco.dnac.brownfield_pnp_playbook_generator:
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

- name: Generate device info with custom file path
  cisco.dnac.brownfield_pnp_playbook_generator:
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
      - file_path: "/tmp/pnp_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]

- name: Generate device info for unclaimed devices only
  cisco.dnac.brownfield_pnp_playbook_generator:
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
      - file_path: "/tmp/unclaimed_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          device_state: ["Unclaimed"]

- name: Generate device info for switches only
  cisco.dnac.brownfield_pnp_playbook_generator:
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
      - file_path: "/tmp/switches_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          device_family: ["Switches and Hubs"]

- name: Generate device info for devices at specific site
  cisco.dnac.brownfield_pnp_playbook_generator:
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
      - file_path: "/tmp/site_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          site_name: "Global/USA/San Francisco"

- name: Generate device info for provisioned wireless controllers
  cisco.dnac.brownfield_pnp_playbook_generator:
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
      - file_path: "/tmp/wlc_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          device_family: ["Wireless Controller"]
          device_state: ["Provisioned"]
"""

RETURN = r"""
response_1:
  description: Successful device info YAML generation
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "message": "YAML config generation succeeded for module 'pnp_workflow_manager'.",
        "file_path": "/tmp/pnp_device_info.yml",
        "config_groups": 1,
        "total_devices": 9,
        "operation_summary": {
          "total_devices_processed": 9,
          "total_successful_operations": 9,
          "total_failed_operations": 0,
          "success_details": [
            {
              "device_serial": "FJC2402A0TX",
              "device_state": "Unclaimed",
              "status": "success"
            },
            {
              "device_serial": "FJC243912MQ",
              "device_state": "Error",
              "status": "success"
            }
          ],
          "failure_details": []
        }
      },
      "msg": "YAML config generation succeeded for module 'pnp_workflow_manager'."
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


class PnPPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for PnP devices with device_info only.
    """

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            None
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "pnp_workflow_manager"

        # Initialize operation tracking
        self.operation_successes = []
        self.operation_failures = []
        self.total_devices_processed = 0

        # Initialize caches (reduced to only site cache since we're not using templates/images)
        self._site_cache = {}

        # Initialize generate_all_configurations
        self.generate_all_configurations = False

    def validate_input(self):
        """
        Validates the input configuration parameters for the playbook.
        Returns:
            self: Returns the instance with validation results
        """
        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        pnp_brownfield_spec = {
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        valid_config, invalid_params = validate_list_of_dicts(
            self.config, pnp_brownfield_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook config: {0}".format(
                "\n".join(invalid_params)
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.validated_config = valid_config
        self.msg = "Successfully validated playbook config"
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def get_workflow_elements_schema(self):
        """
        Define the schema for PnP workflow elements.
        Returns:
            dict: Schema definition for network elements
        """
        return {
            "module_name": "pnp_workflow_manager",
            "global_filters": {
                "device_state": {
                    "type": "list",
                    "valid_values": ["Unclaimed", "Planned", "Onboarding", "Provisioned", "Error"]
                },
                "device_family": {
                    "type": "list"
                },
                "site_name": {
                    "type": "str"
                }
            },
            "component_specific_filters": {
                "components_list": {
                    "type": "list",
                    "valid_values": ["device_info"],
                    "default": ["device_info"]
                }
            },
            "network_elements": {
                "device_info": {
                    "get_function_name": self.get_pnp_devices,
                }
            }
        }

    def transform_pnp_device(self, device):
        """
        Transform a single PnP device from API format to device_info format.
        """
        device_info_item = OrderedDict()

        # Extract device info
        device_info = device.get("deviceInfo", {})

        # Basic device information - serial_number is required
        serial_number = device_info.get("serialNumber")
        if not serial_number:
            self.log("Device missing serial number, skipping", "WARNING")
            return None

        device_info_item["serial_number"] = serial_number

        # Hostname (optional)
        hostname = device_info.get("hostname")
        if hostname:
            device_info_item["hostname"] = hostname

        # State
        device_info_item["state"] = device_info.get("state", "Unclaimed")

        # PID is required
        pid = device_info.get("pid")
        if not pid:
            self.log("Device '{0}' missing PID, skipping".format(serial_number), "WARNING")
            return None
        device_info_item["pid"] = pid

        # SUDI requirement (optional)
        sudi_required = device_info.get("sudiRequired")
        if sudi_required is not None:
            device_info_item["is_sudi_required"] = sudi_required

        # Authorization flag (optional)
        auth_operation = device_info.get("authOperation")
        if auth_operation and auth_operation != "AUTHORIZATION_NOT_REQUIRED":
            device_info_item["authorize"] = True

        return device_info_item

    def group_devices_by_config(self, devices):
        """
        Group devices by their configuration parameters - simplified to only include device_info.
        """
        # Create a single group for all devices with just device_info
        config_group = OrderedDict()
        config_group["device_info"] = []

        for device in devices:
            if not device or not isinstance(device, dict):
                continue

            device_info = device.get("deviceInfo", {})
            if not device_info:
                continue

            # Get device identifiers for logging
            serial_number = device_info.get("serialNumber", "Unknown")
            device_family = device_info.get("family", "Unknown")
            state = device_info.get("state", "Unknown")
            pid = device_info.get("pid", "Unknown")

            self.log("Processing device: {0}, Family: {1}, State: {2}, PID: {3}".format(
                serial_number, device_family, state, pid), "DEBUG")

            # Transform and add device info to the group
            try:
                device_info_item = self.transform_pnp_device(device)
                if device_info_item:
                    config_group["device_info"].append(device_info_item)
                    self.operation_successes.append({
                        "device_serial": device_info_item.get("serial_number"),
                        "device_state": device_info_item.get("state"),
                        "status": "success"
                    })
            except Exception as e:
                self.log("Error transforming device '{0}': {1}".format(serial_number, str(e)), "ERROR")
                self.operation_failures.append({
                    "device_serial": serial_number,
                    "error": str(e),
                    "status": "failed"
                })

        # Return single config group containing all devices
        return [config_group] if config_group["device_info"] else []

    def get_pnp_devices(self, network_element, config):
        """
        Get PnP devices from Catalyst Center.
        Args:
            network_element (dict): Network element definition
            config (dict): Configuration with filters
        Returns:
            dict: Dictionary containing raw pnp_devices list
        """
        self.log("Starting PnP device retrieval", "INFO")

        # Handle None config
        if not config:
            self.log("No config provided, using empty filters", "WARNING")
            config = {}

        # Extract filters from config
        global_filters = config.get("global_filters", {})
        # Ensure global_filters is not None
        if global_filters is None:
            global_filters = {}

        device_state_filter = global_filters.get("device_state", [])
        device_family_filter = global_filters.get("device_family", [])
        site_name_filter = global_filters.get("site_name")

        try:
            # Get all PnP devices
            params = {}
            if device_state_filter:
                params["state"] = device_state_filter

            response = self.dnac._exec(
                family="device_onboarding_pnp",
                function="get_device_list",
                params=params,
                op_modifies=False
            )
            self.log("Received API response for PnP devices: {0}".format(response), "DEBUG")
            if not response:
                self.log("No PnP devices found in response", "WARNING")
                return {"pnp_devices": []}

            devices = response if isinstance(response, list) else []
            self.log("Retrieved {0} total PnP devices from API".format(len(devices)), "INFO")

            # Apply additional filters
            filtered_devices = []
            for device in devices:
                # Skip None or invalid devices
                if not device or not isinstance(device, dict):
                    self.log("Skipping invalid device entry: {0}".format(device), "WARNING")
                    continue

                device_info = device.get("deviceInfo", {})

                # Skip if deviceInfo is missing
                if not device_info:
                    self.log("Skipping device with missing deviceInfo", "WARNING")
                    continue

                # Filter by device family
                if device_family_filter:
                    device_family = device_info.get("family")
                    if device_family not in device_family_filter:
                        continue

                # Filter by site name
                if site_name_filter:
                    site_id = device_info.get("siteId")
                    if site_id:
                        site_name = self.get_site_name_from_id(site_id)
                        if not site_name or site_name_filter not in site_name:
                            continue
                    else:
                        continue

                filtered_devices.append(device)

            self.log("Filtered to {0} devices based on criteria".format(len(filtered_devices)), "INFO")
            self.total_devices_processed = len(filtered_devices)

            # Return raw devices (not transformed)
            return {"pnp_devices": filtered_devices}

        except Exception as e:
            self.log("Error retrieving PnP devices: {0}".format(str(e)), "ERROR")
            import traceback
            self.log("Traceback: {0}".format(traceback.format_exc()), "ERROR")
            return {"pnp_devices": []}

    def get_site_name_from_id(self, site_id):
        """
        Get site name from site ID with caching.
        Args:
            site_id (str): Site ID
        Returns:
            str: Site name hierarchy or None
        """
        if not site_id:
            return None

        if site_id in self._site_cache:
            return self._site_cache[site_id]

        try:
            response = self.dnac._exec(
                family="sites",
                function="get_site",
                params={"site_id": site_id},
                op_modifies=False
            )

            self.log("Received API response for site '{0}': {1}".format(site_id, response), "DEBUG")

            if response and response.get("response"):
                site_info = response.get("response")
                # Handle both single dict and list responses
                if isinstance(site_info, list) and len(site_info) > 0:
                    site_name = site_info[0].get("siteNameHierarchy")
                elif isinstance(site_info, dict):
                    site_name = site_info.get("siteNameHierarchy")
                else:
                    self.log("Unexpected site response format: {0}".format(site_info), "WARNING")
                    return None

                if site_name:
                    self._site_cache[site_id] = site_name
                    return site_name

        except Exception as e:
            self.log("Error fetching site name for ID '{0}': {1}".format(site_id, str(e)), "WARNING")

        return None

    def yaml_config_generator(self, config):
        """Generate YAML configuration file with only device_info."""
        self.log("Starting YAML configuration generation", "INFO")

        # Handle None config
        if not config:
            self.log("No config provided, using empty config", "WARNING")
            config = {}

        file_path = config.get("file_path")
        if not file_path:
            file_path = self.generate_filename()

        # Get PnP devices
        network_element = self.module_schema["network_elements"]["device_info"]
        get_function = network_element["get_function_name"]

        devices_data = get_function(network_element, config)

        if not devices_data or not devices_data.get("pnp_devices"):
            self.msg = "No PnP devices found to generate configuration"
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        # Group devices by their configuration (simplified to single group)
        grouped_configs = self.group_devices_by_config(devices_data["pnp_devices"])

        if not grouped_configs:
            self.msg = "No valid devices found after processing"
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        # Prepare output with grouped configurations
        final_output = []
        for config_group in grouped_configs:
            final_output.append(config_group)

        # Wrap in config structure for pnp_workflow_manager
        output_structure = {"config": final_output}

        # Write to YAML file
        success = self.write_dict_to_yaml([output_structure], file_path)

        if success:
            self.msg = "YAML config generation succeeded for module '{0}'.".format(self.module_name)
            self.result["response"] = {
                "message": self.msg,
                "file_path": file_path,
                "config_groups": len(grouped_configs),
                "total_devices": sum(len(g["device_info"]) for g in grouped_configs),
                "operation_summary": {
                    "total_devices_processed": self.total_devices_processed,
                    "total_successful_operations": len(self.operation_successes),
                    "total_failed_operations": len(self.operation_failures),
                    "success_details": self.operation_successes,
                    "failure_details": self.operation_failures
                }
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = "Failed to write YAML configuration file"
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """Get desired state from config."""
        self.log("Processing configuration for state: {0}".format(state), "INFO")

        self.generate_all_configurations = config.get("generate_all_configurations", False)

        self.want = {
            "file_path": config.get("file_path"),
            "component_specific_filters": config.get("component_specific_filters", {}),
            "global_filters": config.get("global_filters", {}),
            "state": state
        }

        return self

    def get_diff_gathered(self):
        """Process merge state."""
        self.log("Processing gathered state", "INFO")

        config = self.validated_config[0] if self.validated_config else {}
        self.yaml_config_generator(config)

        return self


def main():
    """Main entry point for module execution."""
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

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    pnp_generator = PnPPlaybookGenerator(module)

    # Version check
    current_version = pnp_generator.get_ccc_version()
    min_supported_version = "2.3.5.3"

    if pnp_generator.compare_dnac_versions(current_version, min_supported_version) < 0:
        pnp_generator.msg = "PnP features require Cisco Catalyst Center version {0} or later. Current version: {1}".format(
            min_supported_version, current_version
        )
        pnp_generator.set_operation_result("failed", False, pnp_generator.msg, "CRITICAL")
        module.fail_json(msg=pnp_generator.msg)

    # Get state
    state = pnp_generator.params.get("state")

    if state not in pnp_generator.supported_states:
        pnp_generator.msg = "State '{0}' is not supported. Supported states: {1}".format(
            state, pnp_generator.supported_states
        )
        pnp_generator.set_operation_result("failed", False, pnp_generator.msg, "ERROR")
        module.fail_json(msg=pnp_generator.msg)

    # Validate input
    pnp_generator.validate_input().check_return_status()

    # Process configuration
    for config in pnp_generator.validated_config:
        pnp_generator.get_want(config, state).check_return_status()
        pnp_generator.get_diff_gathered().check_return_status()

    module.exit_json(**pnp_generator.result)


if __name__ == "__main__":
    main()

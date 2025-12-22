#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbook for RMA (Return Material Authorization) Workflow in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["Priyadharshini B", "Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: brownfield_rma_playbook_generator
short_description: Generate YAML playbook for 'rma_workflow_manager' module from existing RMA configurations.
description:
- Generates YAML configurations compatible with the `rma_workflow_manager` module,
  reducing the effort required to manually create Ansible playbooks for device replacement workflows.
- The YAML configurations generated represent the RMA device replacement configurations
  for faulty and replacement devices configured on the Cisco Catalyst Center.
- Supports extraction of device replacement workflows, marked devices for replacement,
  and replacement device details with their current status.
- Enables migration, backup, and replication of RMA configurations across different
  Cisco Catalyst Center instances.
version_added: '6.31.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Priyadharshini B (@pbalaku2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: false
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `rma_workflow_manager` module.
    - Filters specify which RMA configurations to include in the YAML configuration file.
    - If "generate_all_configurations" is specified, all RMA configurations are included.
    type: list
    elements: dict
    required: true
    suboptions:
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "rma_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
      generate_all_configurations:
        description:
        - Generate YAML configuration for all available RMA components.
        - When set to true, generates configuration for all device replacement workflows.
        - Takes precedence over component_specific_filters if both are specified.
        type: bool
        default: false
      component_specific_filters:
        description:
        - Filters to specify which RMA components to include in the YAML configuration file.
        - If "components_list" is specified, only those components are included.
        - Ignored when generate_all_configurations is set to true.
        type: dict
        suboptions:
          components_list:
            description:
            - List of RMA components to include in the YAML configuration file.
            - Valid values are "device_replacement_workflows" for RMA device replacement configurations.
            - If not specified, all components are included.
            type: list
            elements: str
            choices: ['device_replacement_workflows']
          device_replacement_workflows:
            description:
            - Device replacement workflow filtering options by device identifiers.
            type: list
            elements: dict
            suboptions:
              faulty_device_serial_number:
                description:
                - Serial number to filter device replacement workflows by faulty device.
                type: str
              replacement_device_serial_number:
                description:
                - Serial number to filter device replacement workflows by replacement device.
                type: str
              replacement_status:
                description:
                - Status to filter device replacement workflows by replacement status.
                - Valid values include "READY-FOR-REPLACEMENT", "REPLACEMENT-IN-PROGRESS", etc.
                type: str
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
- SDK Methods used are
    - device_replacement.return_replacement_devices_with_details
    - devices.get_device_list
- Paths used are
    - GET /dna/intent/api/v1/device-replacement
    - GET /dna/intent/api/v1/network-device
- Cisco Catalyst Center version 2.3.5.3 or higher is required for RMA functionality
"""

EXAMPLES = r"""
- name: Generate YAML Configuration for all RMA device replacement workflows
  cisco.dnac.brownfield_rma_playbook_generator:
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
      - file_path: "/tmp/rma_workflows_config.yaml"
        generate_all_configurations: true

- name: Generate YAML Configuration for specific device replacement workflows
  cisco.dnac.brownfield_rma_playbook_generator:
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
      - file_path: "/tmp/rma_specific_workflows.yaml"
        component_specific_filters:
          components_list: ["device_replacement_workflows"]
          device_replacement_workflows:
            - faulty_device_serial_number: "FJC2327U0S2"
            - replacement_status: "READY-FOR-REPLACEMENT"

- name: Generate YAML Configuration for device replacement workflows by replacement device
  cisco.dnac.brownfield_rma_playbook_generator:
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
      - file_path: "/tmp/rma_replacement_device_workflows.yaml"
        component_specific_filters:
          components_list: ["device_replacement_workflows"]
          device_replacement_workflows:
            - replacement_device_serial_number: "FCW2225C020"
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
          "YAML config generation Task succeeded for module 'rma_workflow_manager'.": {
            "file_path": "/tmp/rma_workflows_config.yaml",
            "components_processed": 1
          }
        },
      "msg": "YAML config generation Task succeeded for module 'rma_workflow_manager'."
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": "No configurations found to process for module 'rma_workflow_manager'.
      This may be because:\n- No device replacement workflows are configured in Catalyst Center\n- The API is not available in this version\n-
      User lacks required permissions\n- API function names have changed"
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


class RMAPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for RMA (Return Material Authorization) workflows
    in Cisco Catalyst Center using the GET APIs.
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
        self.module_schema = self.rma_workflow_manager_mapping()
        self.module_name = "rma_workflow_manager"

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
            "generate_all_configurations": {"type": "bool", "required": False},
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

    def rma_workflow_manager_mapping(self):
        """
        Constructs and returns a structured mapping for managing RMA workflow elements.
        This mapping includes associated filters, temporary specification functions, API details,
        and fetch function references used in the RMA workflow orchestration process.

        Returns:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a component
                (e.g., 'device_replacement_workflows') and maps to:
                    - "filters": Dictionary of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'device_replacement').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
                - "global_filters": An empty dict reserved for global filters applicable across all elements.
        """
        return {
            "network_elements": {
                "device_replacement_workflows": {
                    "filters": {
                        "faulty_device_serial_number": {"type": "str", "required": False},
                        "replacement_device_serial_number": {"type": "str", "required": False},
                        "replacement_status": {"type": "str", "required": False},
                    },
                    "reverse_mapping_function": self.device_replacement_workflows_reverse_mapping_function,
                    "api_function": "return_replacement_devices_with_details",
                    "api_family": "device_replacement",
                    "get_function_name": self.get_device_replacement_workflows,
                },
            },
            "global_filters": {},
        }

    def device_replacement_workflows_reverse_mapping_function(self, requested_features=None):
        """
        Returns the reverse mapping specification for device replacement workflow details.
        Args:
            requested_features (list, optional): List of specific features to include (not used for RMA workflows).
        Returns:
            dict: A dictionary containing reverse mapping specifications for device replacement workflow details
        """
        self.log("Generating reverse mapping specification for device replacement workflow details", "DEBUG")
        return self.device_replacement_workflows_temp_spec()

    def device_replacement_workflows_temp_spec(self):
        """
        Constructs a temporary specification for device replacement workflow details, defining the structure and types
        of attributes that will be used in the YAML configuration file.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of device replacement workflow attributes.
        """
        self.log("Generating temporary specification for device replacement workflow details.", "DEBUG")
        device_replacement_workflows_details = OrderedDict({
            "faulty_device_name": {
                "type": "str",
                "special_handling": True,
                "transform": self.get_faulty_device_name,
            },
            "faulty_device_ip_address": {
                "type": "str",
                "special_handling": True,
                "transform": self.get_faulty_device_ip_address,
            },
            "faulty_device_serial_number": {"type": "str", "source_key": "faultyDeviceSerialNumber"},
            "replacement_device_name": {
                "type": "str",
                "special_handling": True,
                "transform": self.get_replacement_device_name,
            },
            "replacement_device_ip_address": {
                "type": "str",
                "special_handling": True,
                "transform": self.get_replacement_device_ip_address,
            },
            "replacement_device_serial_number": {"type": "str", "source_key": "replacementDeviceSerialNumber"},
        })
        return device_replacement_workflows_details

    def get_device_replacement_workflows(self, network_element, filters):
        """
        Retrieves device replacement workflow details based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving device replacement workflows.
            filters (dict): A dictionary containing global_filters and component_specific_filters.

        Returns:
            dict: A dictionary containing the modified details of device replacement workflows.
        """
        self.log(
            "Starting to retrieve device replacement workflows with network element: {0} and filters: {1}".format(
                network_element, filters
            ),
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        workflow_filters = component_specific_filters.get("device_replacement_workflows", [])

        final_workflow_configs = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting device replacement workflows using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        try:
            # Get all device replacement workflows
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )

            # Log the raw response to debug
            self.log("Received API response: {0}".format(response), "DEBUG")

            # Handle different response structures
            if isinstance(response, dict):
                workflow_configs = response.get("response", [])
                # Some APIs return data directly in response
                if not workflow_configs and "data" in response:
                    workflow_configs = response.get("data", [])
            else:
                workflow_configs = response if isinstance(response, list) else []

            self.log("Retrieved {0} device replacement workflows from Catalyst Center".format(len(workflow_configs)), "INFO")

            # Log the structure of the first config if available
            if workflow_configs:
                self.log("Sample device replacement workflow structure: {0}".format(workflow_configs[0]), "DEBUG")

            if workflow_filters:
                filtered_configs = []
                for filter_param in workflow_filters:
                    for config in workflow_configs:
                        match = True

                        for key, value in filter_param.items():
                            config_value = None
                            if key == "faulty_device_serial_number":
                                config_value = config.get("faultyDeviceSerialNumber")
                            elif key == "replacement_device_serial_number":
                                config_value = config.get("replacementDeviceSerialNumber")
                            elif key == "replacement_status":
                                config_value = config.get("replacementStatus")

                            if config_value != value:
                                match = False
                                break

                        if match and config not in filtered_configs:
                            filtered_configs.append(config)

                final_workflow_configs = filtered_configs
            else:
                final_workflow_configs = workflow_configs

        except Exception as e:
            self.log("Error retrieving device replacement workflows: {0}".format(str(e)), "ERROR")
            # Instead of failing immediately, let's return empty result
            self.log("API call failed, returning empty device replacement workflow list", "WARNING")
            final_workflow_configs = []

        # Modify device replacement workflow details using temp_spec
        workflow_temp_spec = self.device_replacement_workflows_temp_spec()

        # Custom parameter modification to handle device name and IP resolution
        modified_workflow_configs = []
        for config in final_workflow_configs:
            mapped_config = OrderedDict()

            for key, spec_def in workflow_temp_spec.items():
                if spec_def.get("special_handling"):
                    transform_func = spec_def.get("transform")
                    if callable(transform_func):
                        value = transform_func(config)
                else:
                    source_key = spec_def.get("source_key", key)
                    value = config.get(source_key)

                if value is not None:
                    mapped_config[key] = value

            if mapped_config:  # Only add if we have valid data
                modified_workflow_configs.append(mapped_config)

        modified_workflow_details = {"device_replacement_workflows": modified_workflow_configs}
        self.log("Modified device replacement workflow details: {0}".format(modified_workflow_details), "INFO")

        return modified_workflow_details

    def get_faulty_device_name(self, workflow_config):
        """
        Get the faulty device name from the workflow configuration by resolving the serial number.

        Args:
            workflow_config (dict): The device replacement workflow configuration.

        Returns:
            str or None: The faulty device name if found, None otherwise.
        """
        faulty_serial = workflow_config.get("faultyDeviceSerialNumber")
        if not faulty_serial:
            return None

        self.log("Resolving faulty device name for serial number: {0}".format(faulty_serial), "DEBUG")

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": faulty_serial},
            )
            self.log("Received API response for faulty device name: {0}".format(response), "DEBUG")

            if response and response.get("response"):
                devices = response.get("response")
                if devices and len(devices) > 0:
                    device_name = devices[0].get("hostname")
                    self.log("Found faulty device name: {0}".format(device_name), "DEBUG")
                    return device_name

        except Exception as e:
            self.log("Error resolving faulty device name: {0}".format(str(e)), "WARNING")

        return None

    def get_faulty_device_ip_address(self, workflow_config):
        """
        Get the faulty device IP address from the workflow configuration by resolving the serial number.

        Args:
            workflow_config (dict): The device replacement workflow configuration.

        Returns:
            str or None: The faulty device IP address if found, None otherwise.
        """
        faulty_serial = workflow_config.get("faultyDeviceSerialNumber")
        if not faulty_serial:
            return None

        self.log("Resolving faulty device IP address for serial number: {0}".format(faulty_serial), "DEBUG")

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": faulty_serial},
            )
            self.log("Received API response for faulty device IP address: {0}".format(response), "DEBUG")

            if response and response.get("response"):
                devices = response.get("response")
                if devices and len(devices) > 0:
                    device_ip = devices[0].get("managementIpAddress")
                    self.log("Found faulty device IP address: {0}".format(device_ip), "DEBUG")
                    return device_ip

        except Exception as e:
            self.log("Error resolving faulty device IP address: {0}".format(str(e)), "WARNING")

        return None

    def get_replacement_device_name(self, workflow_config):
        """
        Get the replacement device name from the workflow configuration by resolving the serial number.

        Args:
            workflow_config (dict): The device replacement workflow configuration.

        Returns:
            str or None: The replacement device name if found, None otherwise.
        """
        replacement_serial = workflow_config.get("replacementDeviceSerialNumber")
        if not replacement_serial:
            return None

        self.log("Resolving replacement device name for serial number: {0}".format(replacement_serial), "DEBUG")

        try:
            # First try regular device inventory
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": replacement_serial},
            )

            if response and response.get("response"):
                devices = response.get("response")
                if devices and len(devices) > 0:
                    device_name = devices[0].get("hostname")
                    self.log("Found replacement device name in inventory: {0}".format(device_name), "DEBUG")
                    return device_name

            # If not found in regular inventory, try PnP
            self.log("Device not found in inventory, checking PnP for replacement device", "DEBUG")
            pnp_response = self.dnac._exec(
                family="device_onboarding_pnp",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": replacement_serial},
            )
            self.log("Received API response for replacement device name from PnP: {0}".format(pnp_response), "DEBUG")

            if pnp_response and len(pnp_response) > 0:
                device_info = pnp_response[0].get("deviceInfo", {})
                device_name = device_info.get("hostname")
                self.log("Found replacement device name in PnP: {0}".format(device_name), "DEBUG")
                return device_name

        except Exception as e:
            self.log("Error resolving replacement device name: {0}".format(str(e)), "WARNING")

        return None

    def get_replacement_device_ip_address(self, workflow_config):
        """
        Get the replacement device IP address from the workflow configuration by resolving the serial number.

        Args:
            workflow_config (dict): The device replacement workflow configuration.

        Returns:
            str or None: The replacement device IP address if found, None otherwise.
        """
        replacement_serial = workflow_config.get("replacementDeviceSerialNumber")
        if not replacement_serial:
            return None

        self.log("Resolving replacement device IP address for serial number: {0}".format(replacement_serial), "DEBUG")

        try:
            # First try regular device inventory
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": replacement_serial},
            )
            self.log("Received API response for replacement device IP address: {0}".format(response), "DEBUG")

            if response and response.get("response"):
                devices = response.get("response")
                if devices and len(devices) > 0:
                    device_ip = devices[0].get("managementIpAddress")
                    self.log("Found replacement device IP address in inventory: {0}".format(device_ip), "DEBUG")
                    return device_ip

            # If not found in regular inventory, try PnP
            self.log("Device not found in inventory, checking PnP for replacement device IP", "DEBUG")
            pnp_response = self.dnac._exec(
                family="device_onboarding_pnp",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": replacement_serial},
            )
            self.log("Received API response for replacement device IP address from PnP: {0}".format(pnp_response), "DEBUG")

            if pnp_response and len(pnp_response) > 0:
                device_info = pnp_response[0].get("deviceInfo", {})
                # PnP devices may not have IP addresses assigned yet
                device_ip = device_info.get("aaaCredentials", {}).get("mgmtIpAddress")
                if device_ip:
                    self.log("Found replacement device IP address in PnP: {0}".format(device_ip), "DEBUG")
                    return device_ip

        except Exception as e:
            self.log("Error resolving replacement device IP address: {0}".format(str(e)), "WARNING")

        return None

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        """
        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Fix: Properly handle file_path when it's None
        file_path = yaml_config_generator.get("file_path")
        if not file_path:  # Changed from yaml_config_generator.get("file_path", self.generate_filename())
            file_path = self.generate_filename()

        self.log("File path determined: {0}".format(file_path), "DEBUG")

        # Handle generate_all_configurations flag
        generate_all_configurations = yaml_config_generator.get("generate_all_configurations", False)

        component_specific_filters = (
            yaml_config_generator.get("component_specific_filters") or {}
        )
        self.log(
            "Component-specific filters: {0}".format(component_specific_filters),
            "DEBUG",
        )
        self.log(
            "Generate all configurations: {0}".format(generate_all_configurations),
            "DEBUG",
        )

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        # Determine which components to process
        if generate_all_configurations:
            components_list = list(module_supported_network_elements.keys())
            self.log("Using all available components due to generate_all_configurations=True: {0}".format(components_list), "INFO")
        else:
            components_list = component_specific_filters.get(
                "components_list", list(module_supported_network_elements.keys())
            )

        self.log("Components to process: {0}".format(components_list), "DEBUG")

        # Create the structured configuration
        config_list = []
        components_processed = 0

        for component in components_list:
            self.log("Processing component: {0}".format(component), "INFO")

            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Skipping unsupported network element: {0}".format(component),
                    "WARNING",
                )
                continue

            filters = {
                "global_filters": yaml_config_generator.get("global_filters", {}),
                "component_specific_filters": component_specific_filters
            }

            operation_func = network_element.get("get_function_name")
            self.log("Operation function for {0}: {1}".format(component, operation_func), "DEBUG")

            if callable(operation_func):
                try:
                    self.log("Calling operation function for component: {0}".format(component), "INFO")
                    details = operation_func(network_element, filters)
                    self.log(
                        "Details retrieved for {0}: {1}".format(component, details), "DEBUG"
                    )

                    # Add the component data to config list
                    if component in details and details[component]:
                        # For RMA, we want to generate a config list where each item is a device replacement workflow
                        for workflow in details[component]:
                            config_list.append(workflow)
                        components_processed += 1
                        self.log("Successfully added {0} configurations for component {1}".format(
                            len(details[component]), component), "INFO")
                    else:
                        self.log(
                            "No data found for component: {0}".format(component), "WARNING"
                        )

                except Exception as e:
                    self.log(
                        "Error retrieving data for component {0}: {1}".format(component, str(e)),
                        "ERROR"
                    )
                    import traceback
                    self.log("Full traceback: {0}".format(traceback.format_exc()), "DEBUG")
            else:
                self.log("No callable operation function for component: {0}".format(component), "ERROR")

        self.log("Processing summary: {0} components processed successfully".format(components_processed), "INFO")

        if not config_list:
            self.msg = (
                "No configurations found to process for module '{0}'. "
                "This may be because:\n"
                "- No device replacement workflows are configured in Catalyst Center\n"
                "- The API is not available in this version\n"
                "- User lacks required permissions\n"
                "- API function names have changed"
            ).format(self.module_name)
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        # Create the final structure for RMA workflows
        final_dict = {"config": config_list}
        self.log("Final dictionary created with {0} device replacement workflow configurations".format(len(config_list)), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path, "components_processed": components_processed}
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
            config (dict): The configuration data for the RMA elements.
            state (str): The desired state ('gathered').
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
        self.msg = "Successfully collected all parameters from the playbook for RMA operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the gather operations for RMA configurations in the Cisco Catalyst Center.
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

    # Initialize the RMAPlaybookGenerator object with the module
    ccc_rma_playbook_generator = RMAPlaybookGenerator(module)

    # Check version compatibility
    if (
        ccc_rma_playbook_generator.compare_dnac_versions(
            ccc_rma_playbook_generator.get_ccc_version(), "2.3.5.3"
        )
        < 0
    ):
        ccc_rma_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for RMA Workflow Manager Module. Supported versions start from '2.3.5.3' onwards. "
            "Version '2.3.5.3' introduces APIs for retrieving device replacement workflows from "
            "the Catalyst Center".format(
                ccc_rma_playbook_generator.get_ccc_version()
            )
        )
        ccc_rma_playbook_generator.set_operation_result(
            "failed", False, ccc_rma_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_rma_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_rma_playbook_generator.supported_states:
        ccc_rma_playbook_generator.status = "invalid"
        ccc_rma_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_rma_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_rma_playbook_generator.validate_input().check_return_status()
    config = ccc_rma_playbook_generator.validated_config

    # Handle default case when no filters are specified
    for config_item in config:
        if config_item.get("generate_all_configurations"):
            # Set default components when generate_all_configurations is True
            if not config_item.get("component_specific_filters"):
                config_item["component_specific_filters"] = {
                    "components_list": ["device_replacement_workflows"]
                }
                ccc_rma_playbook_generator.log("Set default components for generate_all_configurations", "INFO")
        elif config_item.get("component_specific_filters") is None:
            # Existing fallback logic
            ccc_rma_playbook_generator.msg = (
                "No component filters specified, defaulting to device_replacement_workflows."
            )
            config_item["component_specific_filters"] = {
                "components_list": ["device_replacement_workflows"]
            }

    # Update validated config
    ccc_rma_playbook_generator.validated_config = config

    # Iterate over the validated configuration parameters
    for config in ccc_rma_playbook_generator.validated_config:
        ccc_rma_playbook_generator.reset_values()
        ccc_rma_playbook_generator.get_want(config, state).check_return_status()
        ccc_rma_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_rma_playbook_generator.result)


if __name__ == "__main__":
    main()

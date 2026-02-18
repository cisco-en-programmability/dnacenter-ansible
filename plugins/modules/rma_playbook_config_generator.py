#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible brownfield playbook generator for RMA device replacement workflows in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["Priyadharshini B", "Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: rma_playbook_config_generator
short_description: Generate YAML playbooks for RMA device replacement
  workflows from existing configurations.
description:
- Generates YAML playbooks compatible with the
  C(rma_workflow_manager) module by extracting existing RMA
  device replacement configurations from Cisco Catalyst Center.
- Reduces manual effort by programmatically retrieving faulty
  and replacement device details, serial numbers, hostnames,
  and IP addresses from active device replacement workflows.
- Supports filtering by faulty device serial number, replacement
  device serial number, and replacement status to generate
  targeted playbooks.
- Enables complete infrastructure discovery with auto-generation
  mode when C(generate_all_configurations) is enabled.
- Resolves device serial numbers to hostnames and management IP
  addresses using both device inventory and PnP (Plug and Play)
  APIs for replacement devices that have not been fully onboarded.
- Requires Cisco Catalyst Center version 2.3.5.3 or higher for
  RMA device replacement API support.

version_added: '6.44.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Priyadharshini B (@pbalaku2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - The desired state for the module operation.
    - Only C(gathered) state is supported to generate YAML
      playbooks from existing RMA configurations.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of configuration filters for generating YAML
      playbooks compatible with the C(rma_workflow_manager) module.
    - Each configuration entry can include file path specification,
      component filters, and auto-discovery settings.
    - Multiple configuration entries can be provided to generate
      separate playbooks with different filter criteria.
    type: list
    elements: dict
    required: true
    suboptions:
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
        - For example, "rma_workflow_manager_playbook_2025-04-22_21-43-26.yml".
        - Ensure the directory path exists and has write
          permissions.
        type: str
      generate_all_configurations:
        description:
        - Enables automatic discovery and generation of YAML
          configurations for all RMA device replacement workflows.
        - When C(true), retrieves all device replacement workflows
          from Cisco Catalyst Center without requiring specific
          filters.
        - Overrides any provided C(component_specific_filters) to
          ensure complete configuration retrieval.
        - Ideal for complete brownfield infrastructure migration and
          comprehensive documentation of all RMA workflows.
        type: bool
        default: false
      component_specific_filters:
        description:
        - Component-level filters to selectively include specific
          RMA configurations in the generated playbook.
        - Allows fine-grained control over which device replacement
          workflows are extracted from Cisco Catalyst Center.
        - If C(generate_all_configurations) is C(true), these
          filters are ignored and all configurations are retrieved.
        type: dict
        suboptions:
          components_list:
            description:
            - List of RMA component types to include in the
              generated YAML playbook.
            - Currently supports only C(device_replacement_workflows)
              for RMA device replacement configurations.
            - If omitted, all supported components are included by
              default.
            type: list
            elements: str
            choices:
            - device_replacement_workflows
          device_replacement_workflows:
            description:
            - Filters for retrieving specific device replacement
              workflow configurations from Cisco Catalyst Center.
            - Multiple filter entries can be specified to target
              different devices or statuses.
            - When multiple filter entries are provided, they are
              combined into a single filter (AND logic).
            - If no filters are provided, all device replacement
              workflows are retrieved.
            type: list
            elements: dict
            suboptions:
              faulty_device_serial_number:
                description:
                - Serial number of the faulty device to filter
                  device replacement workflows.
                - Must be an 11-character alphanumeric string matching
                  the device serial number in Cisco Catalyst Center.
                - "Example: C(FJC2327U0S2)"
                type: str
              replacement_device_serial_number:
                description:
                - Serial number of the replacement device to filter
                  device replacement workflows.
                - Must be an 11-character alphanumeric string matching
                  the device serial number in Cisco Catalyst Center.
                - "Example: C(FCW2225C020)"
                type: str
              replacement_status:
                description:
                - Status to filter device replacement workflows by
                  their current replacement state.
                - "Valid values: C(READY-FOR-REPLACEMENT),
                  C(REPLACEMENT-IN-PROGRESS),
                  C(REPLACEMENT-SCHEDULED),
                  C(REPLACED), C(ERROR),
                  C(MARKED-FOR-REPLACEMENT)"
                type: str
      global_filters:
        description:
        - Global-level filters that apply across all components.
        - Currently not used by this module but reserved for
          future extensibility.
        type: dict
        required: false
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
- Cisco Catalyst Center >= 2.3.5.3

notes:
- Requires minimum Cisco Catalyst Center version 2.3.5.3 for
  RMA device replacement API support.
- Module will fail with an error if connected to an unsupported
  version.
- Generated playbooks are compatible with the
  C(rma_workflow_manager) module for device replacement
  operations.
- Device serial numbers are resolved to hostnames and management
  IP addresses via the device inventory API.
- For replacement devices not yet in inventory, the module falls
  back to the PnP (Plug and Play) API for device resolution.
- PnP devices may not have management IP addresses assigned,
  resulting in C(None) for the IP address field.
- The module operates in check mode but does not make any
  changes to Cisco Catalyst Center.
- Use C(dnac_log) and C(dnac_log_level) parameters for detailed
  operation logging and troubleshooting.

- SDK Methods used are
    - device_replacement.return_replacement_devices_with_details
    - devices.get_device_list
- Paths used are
    - GET /dna/intent/api/v1/device-replacement
    - GET /dna/intent/api/v1/network-device
- Cisco Catalyst Center version 2.3.5.3 or higher is required for RMA functionality

seealso:
- module: cisco.dnac.rma_workflow_manager
  description: Manage RMA (Return Material Authorization) workflows in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML Configuration for all RMA device replacement workflows
  cisco.dnac.rma_playbook_config_generator:
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
  cisco.dnac.rma_playbook_config_generator:
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
  cisco.dnac.rma_playbook_config_generator:
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
  description: A dictionary with the response returned by the Cisco Catalyst Center
  returned: always
  type: dict
  sample: >
    {
      "msg": "YAML configuration file generated successfully for module 'rma_workflow_manager'",
      "response": {
          "components_processed": 1,
          "components_skipped": 0,
          "configurations_count": 1,
          "file_path": "/Users/priyadharshini/Downloads/rma_info",
          "message": "YAML configuration file generated successfully for module 'rma_workflow_manager'",
          "status": "success"
      },
      "status": "success"
    }
# Case_2: Idempotency Scenario
response_2:
  description: A dict with the response returned by the Cisco Catalyst Center
  returned: always
  type: dict
  sample: >
    {
      msg = (
        "No device replacement workflows found to process for module "
        "'rma_workflow_manager'. Verify that RMA workflows are configured in "
        "Catalyst Center or check user permissions."
      ),
      "response": {
        "components_processed": 0,
        "components_skipped": 1,
        "configurations_count": 0,
        "message": (
          "No device replacement workflows found to process for module "
          "'rma_workflow_manager'. Verify that RMA workflows are configured in "
          "Catalyst Center or check user permissions."
        ),
        "status": "success"
      },
      "status": "success"
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
    Brownfield playbook generator for RMA device replacement workflows.

    Attributes:
        supported_states (list): Supported Ansible states (only 'gathered').
        module_schema (dict): Workflow mapping defining RMA components,
            API functions, filters, and processing methods.
        module_name (str): Target module name for generated playbooks
            ('rma_workflow_manager').

    Description:
        Retrieves existing RMA device replacement configurations from
        Cisco Catalyst Center and generates YAML playbooks compatible
        with the rma_workflow_manager module. Supports filtering by
        faulty device serial, replacement device serial, and replacement
        status. Resolves device serial numbers to hostnames and management
        IPs using both inventory and PnP APIs. Requires Cisco Catalyst
        Center version 2.3.5.3 or higher.
    """

    def __init__(self, module):
        """
        Initialize an instance of the RMAPlaybookGenerator class.

        Description:
            Sets up the class instance with module configuration, supported states,
            module schema mapping, and module name for RMA
            workflow operations in Cisco Catalyst Center.

        Args:
            module (AnsibleModule): The Ansible module instance containing configuration
                parameters and methods for module execution.

        Returns:
            None: This is a constructor method that initializes the instance.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.rma_workflow_manager_mapping()
        self.module_name = "rma_workflow_manager"

    def validate_input(self):
        """
        Validates the input configuration parameters for the RMA playbook.

        Description:
            Performs comprehensive validation of input configuration parameters to ensure
            they conform to the expected schema for RMA workflow generation. Validates
            parameter types, requirements, and structure for device replacement workflow
            configuration generation.

        Args:
            None: Uses self.config from the instance.

        Returns:
            object: Self instance with updated attributes:
                - self.msg (str): Message describing the validation result.
                - self.status (str): Status of validation ("success" or "failed").
                - self.validated_config (list): Validated configuration parameters if successful.
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
            "file_path": {"type": "str", "required": False},
            "generate_all_configurations": {"type": "bool", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        allowed_keys = set(temp_spec.keys())

        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                "Validating configuration item {0}/{1}".format(
                    config_index, len(self.config)
                ),
                "DEBUG",
            )
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

        self.log("Validating configuration parameters with schema - config: {0} and temp_spec: {1}".format(self.config, temp_spec), "DEBUG")

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
        Constructs comprehensive mapping configuration for RMA workflow components.

        Description:
            Creates a structured mapping that defines all supported RMA workflow
            components, their associated API functions, filter specifications, and
            processing functions. This mapping serves as the central configuration
            registry for the RMA workflow orchestration process.

        Args:
            None: Uses class methods and instance configuration.

        Returns:
            dict: A comprehensive mapping dictionary containing:
                - network_elements (dict): Component configurations with API details,
                  filter specifications, and processing function references.
                - global_filters (dict): Global filter configuration options.
        """
        self.log("Generating RMA workflow manager mapping configuration.", "DEBUG")

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

    def device_replacement_workflows_reverse_mapping_function(self):
        """
        Provides reverse mapping specification for device replacement workflow transformations.
        Description:
            Returns the reverse mapping specification used to transform device replacement
            workflow API responses into structured configuration format. This specification
            defines how API response fields should be mapped to the desired YAML structure.

        Args:
            None: Uses class methods and instance configuration.
        Returns:
            OrderedDict: The device replacement workflows temporary specification containing
            field mappings, data types, and transformation rules.
        """
        self.log("Generating reverse mapping specification for device replacement workflow details", "DEBUG")
        return self.device_replacement_workflows_temp_spec()

    def device_replacement_workflows_temp_spec(self):
        """
        Constructs detailed specification for device replacement workflow data transformation.

        Description:
            Creates a comprehensive specification that defines how device replacement workflow
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for device name and IP resolution through
            transformation functions.

        Args:
            None: Uses logging methods and transformation functions from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            transformation functions, and source key references for device replacement workflows.
        """
        self.log(
            "Building specification for device replacement "
            "workflow transformation",
            "DEBUG",
        )

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
        self.log("Built specification for device replacement workflow transformation", "DEBUG")
        return device_replacement_workflows_details

    def get_device_replacement_workflows(self, network_element, filters):
        """
        Retrieves device replacement workflow configurations from Cisco Catalyst Center.

        Description:
            Fetches device replacement workflow data from the API and applies component-specific
            filters. Supports filtering by faulty device serial number, replacement device
            serial number, and replacement status. Transforms API responses into structured
            format suitable for YAML generation.

        Args:
            network_element (dict): Configuration mapping containing API family and
                function details for device replacement workflow retrieval.
            filters (dict): Filter criteria containing component-specific filters
                for device replacement workflows.

        Returns:
            dict: A dictionary containing:
                - device_replacement_workflows (list): List of device replacement workflow
                  configurations with transformed parameters according to the specification.
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
            if not isinstance(response, dict):
                self.log(
                    "Unexpected response type from API: "
                    "{0}".format(type(response).__name__),
                    "WARNING",
                )
                return {"device_replacement_workflows": []}

            workflow_configs = response.get("response", [])

            self.log(
                "Retrieved {0} device replacement workflow(s) from "
                "Cisco Catalyst Center".format(len(workflow_configs)),
                "INFO",
            )

            if workflow_filters:
                self.log(
                    "Applying {0} workflow filter(s): {1}".format(
                        len(workflow_filters), workflow_filters
                    ),
                    "DEBUG",
                )

                if isinstance(workflow_filters, list):
                    combined_filters = {}
                    for filter_index, filter_item in enumerate(
                        workflow_filters, start=1
                    ):
                        self.log(
                            "Processing filter entry "
                            "{0}/{1}: {2}".format(
                                filter_index,
                                len(workflow_filters),
                                filter_item,
                            ),
                            "DEBUG",
                        )
                        if isinstance(filter_item, dict):
                            combined_filters.update(filter_item)
                elif isinstance(workflow_filters, dict):
                    combined_filters = workflow_filters
                else:
                    combined_filters = {}

                self.log("Combined filter criteria: {0}".format(combined_filters), "DEBUG")

                filtered_configs = []

                for config_index, config in enumerate(
                    workflow_configs, start=1
                ):
                    self.log(
                        "Evaluating workflow {0}/{1} against "
                        "filters".format(
                            config_index, len(workflow_configs)
                        ),
                        "DEBUG",
                    )
                    matches_all_filters = True

                    # Filter key to API response key mapping
                    filter_key_map = {
                        "faulty_device_serial_number": (
                            "faultyDeviceSerialNumber"
                        ),
                        "replacement_device_serial_number": (
                            "replacementDeviceSerialNumber"
                        ),
                        "replacement_status": "replacementStatus",
                    }

                    for key, expected_value in combined_filters.items():
                        api_key = filter_key_map.get(key)
                        if not api_key:
                            self.log(
                                "Unknown filter key '{0}', skipping".format(key),
                                "WARNING",
                            )
                            continue

                        config_value = config.get(api_key)
                        if config_value != expected_value:
                            matches_all_filters = False
                            self.log(
                                "Workflow {0} filtered out on "
                                "'{1}': expected '{2}', "
                                "got '{3}'".format(
                                    config_index, key,
                                    expected_value, config_value,
                                ),
                                "DEBUG",
                            )
                            break
                    if matches_all_filters:
                        filtered_configs.append(config)
                        self.log("Config matches all filters and included: faulty_serial={0}, replacement_serial={1}, status={2}".format(
                            config.get("faultyDeviceSerialNumber", "N/A"),
                            config.get("replacementDeviceSerialNumber", "N/A"),
                            config.get("replacementStatus", "N/A")), "DEBUG")

                final_workflow_configs = filtered_configs

                if filtered_configs:
                    self.log("Found {0} matching workflows after applying filters: {1}".format(
                        len(filtered_configs), combined_filters), "INFO")
                else:
                    self.log("No workflows match the specified filters: {0}. All {1} workflows were filtered out.".format(
                        combined_filters, len(workflow_configs)), "WARNING")
            else:
                final_workflow_configs = workflow_configs
                self.log("No filters specified, returning all {0} workflows".format(len(workflow_configs)), "INFO")

        except Exception as e:
            self.msg = "Error retrieving device replacement workflows: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return {"device_replacement_workflows": []}

        # Transform workflow configs using temp spec
        self.log(
            "Transforming {0} workflow configuration(s) using "
            "reverse mapping specification".format(
                len(final_workflow_configs)
            ),
            "DEBUG",
        )
        workflow_temp_spec = (
            self.device_replacement_workflows_temp_spec()
        )

        modified_workflow_configs = []
        for config_index, config in enumerate(
            final_workflow_configs, start=1
        ):
            self.log(
                "Transforming workflow {0}/{1}".format(
                    config_index, len(final_workflow_configs)
                ),
                "DEBUG",
            )
            mapped_config = OrderedDict()

            for key, spec_def in workflow_temp_spec.items():
                if spec_def.get("special_handling"):
                    transform_func = spec_def.get("transform")
                    if callable(transform_func):
                        self.log(
                            "Applying transform for key "
                            "'{0}'".format(key),
                            "DEBUG",
                        )
                        value = transform_func(config)
                    else:
                        self.log(
                            "Transform function not callable for "
                            "key '{0}'".format(key),
                            "WARNING",
                        )
                        value = None
                else:
                    source_key = spec_def.get("source_key", key)
                    value = config.get(source_key)

                if value is not None:
                    mapped_config[key] = value

            if mapped_config:
                modified_workflow_configs.append(mapped_config)
                self.log(
                    "Successfully transformed workflow "
                    "{0}".format(config_index),
                    "DEBUG",
                )

        modified_workflow_details = {"device_replacement_workflows": modified_workflow_configs}
        self.log("Modified device replacement workflow details: {0}".format(modified_workflow_details), "INFO")

        return modified_workflow_details

    def get_faulty_device_name(self, workflow_config):
        """
        Resolves faulty device name from workflow configuration using device serial number.

        Description:
            Queries the Cisco Catalyst Center device inventory API to resolve the faulty
            device serial number to its corresponding hostname. Used for transformation
            during YAML configuration generation to provide human-readable device identifiers.

        Args:
            workflow_config (dict): The device replacement workflow configuration containing
                the faulty device serial number.

        Returns:
            str or None: The faulty device hostname if found in the device inventory,
            otherwise None if the device is not found or API call fails.
        """
        self.log("Resolving faulty device name from workflow configuration.", "DEBUG")

        faulty_serial = workflow_config.get("faultyDeviceSerialNumber")
        if not faulty_serial:
            self.log(
                "No faulty device serial number found in "
                "workflow configuration, cannot resolve "
                "device name",
                "WARNING",
            )
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

            if not response:
                self.log(
                    "Empty response from device inventory API "
                    "for faulty serial '{0}'".format(
                        faulty_serial
                    ),
                    "WARNING",
                )
                return None

            devices = response.get("response")

            if not devices or len(devices) == 0:
                self.log(
                    "No device found in inventory for faulty "
                    "serial '{0}'. The device may have been "
                    "removed or the serial number is "
                    "incorrect.".format(faulty_serial),
                    "WARNING",
                )
                return None

            device_name = devices[0].get("hostname")

            if not device_name:
                self.log(
                    "Device found for faulty serial '{0}' but "
                    "hostname is empty or None".format(
                        faulty_serial
                    ),
                    "WARNING",
                )
                return None

            self.log(
                "Resolved faulty device serial '{0}' to "
                "hostname '{1}'".format(
                    faulty_serial, device_name
                ),
                "INFO",
            )
            return device_name

        except Exception as e:
            self.msg = (
                "Error resolving faulty device hostname for "
                "serial '{0}': {1}".format(
                    faulty_serial, str(e)
                ),
                "WARNING",
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return None

    def get_faulty_device_ip_address(self, workflow_config):
        """
        Resolves faulty device IP address from workflow configuration using device serial number.

        Description:
            Queries the Cisco Catalyst Center device inventory API to resolve the faulty
            device serial number to its management IP address. Provides network connectivity
            information for the faulty device in the generated YAML configuration.

        Args:
            workflow_config (dict): The device replacement workflow configuration containing
                the faulty device serial number.

        Returns:
            str or None: The faulty device management IP address if found in the device
            inventory, otherwise None if the device is not found or API call fails.
        """
        self.log("Resolving faulty device IP address from workflow configuration: {0}".format(workflow_config), "DEBUG")

        faulty_serial = workflow_config.get("faultyDeviceSerialNumber")
        if not faulty_serial:
            self.log(
                "No faulty device serial number found in workflow "
                "configuration",
                "DEBUG",
            )
            return None

        self.log("Resolving faulty device IP address for serial number: {0}".format(faulty_serial), "DEBUG")

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": faulty_serial},
            )
            self.log(
                "Received device inventory API response for "
                "faulty serial '{0}': {1}".format(
                    faulty_serial, response
                ),
                "DEBUG",
            )

            if not response:
                self.log(
                    "Empty response from device inventory API "
                    "for faulty serial '{0}'".format(
                        faulty_serial
                    ),
                    "WARNING",
                )
                return None

            devices = response.get("response")

            if not devices or len(devices) == 0:
                self.log(
                    "No device found in inventory for faulty "
                    "serial '{0}'. The device may have been "
                    "removed or the serial number is "
                    "incorrect.".format(faulty_serial),
                    "WARNING",
                )
                return None

            device_ip = devices[0].get("managementIpAddress")

            if not device_ip:
                self.log(
                    "Device found for faulty serial '{0}' but "
                    "management IP address is empty or "
                    "None".format(faulty_serial),
                    "WARNING",
                )
                return None

            self.log(
                "Resolved faulty device serial '{0}' to "
                "management IP '{1}'".format(
                    faulty_serial, device_ip
                ),
                "INFO",
            )
            return device_ip

        except Exception as e:
            self.msg = (
                "Error resolving faulty device IP for "
                "serial '{0}': {1}".format(
                    faulty_serial, str(e)
                ),
                "WARNING",
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return None

    def get_replacement_device_name(self, workflow_config):
        """
        Resolves replacement device name from workflow configuration using device serial number.

        Description:
            Queries both the Cisco Catalyst Center device inventory and PnP (Plug and Play)
            APIs to resolve the replacement device serial number to its hostname. Checks
            regular inventory first, then falls back to PnP inventory for devices that
            haven't been fully onboarded yet.

        Args:
            workflow_config (dict): The device replacement workflow configuration containing
                the replacement device serial number.

        Returns:
            str or None: The replacement device hostname if found in either device inventory
            or PnP inventory, otherwise None if the device is not found or API calls fail.
        """
        self.log("Resolving replacement device name from workflow configuration: {0}".format(workflow_config), "DEBUG")

        replacement_serial = workflow_config.get("replacementDeviceSerialNumber")
        if not replacement_serial:
            self.log(
                "No replacement device serial number found in "
                "workflow configuration, cannot resolve "
                "device name",
                "WARNING",
            )
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

            self.log(
                "Received device inventory API response for "
                "replacement serial '{0}': {1}".format(
                    replacement_serial, response
                ),
                "DEBUG",
            )

            if response:
                devices = response.get("response")

                if devices and len(devices) > 0:
                    device_name = devices[0].get("hostname")

                    if device_name:
                        self.log(
                            "Resolved replacement serial "
                            "'{0}' to hostname '{1}' from "
                            "device inventory".format(
                                replacement_serial,
                                device_name,
                            ),
                            "INFO",
                        )
                        return device_name

                    self.log(
                        "Device found in inventory for "
                        "replacement serial '{0}' but "
                        "hostname is empty or None".format(
                            replacement_serial
                        ),
                        "WARNING",
                    )
                else:
                    self.log(
                        "No device found in inventory for "
                        "replacement serial '{0}'".format(
                            replacement_serial
                        ),
                        "DEBUG",
                    )
            else:
                self.log(
                    "Empty response from device inventory "
                    "API for replacement serial "
                    "'{0}'".format(replacement_serial),
                    "WARNING",
                )
            # If not found in regular inventory, try PnP
            self.log(
                "Falling back to PnP inventory for "
                "replacement serial '{0}'".format(
                    replacement_serial
                ),
                "DEBUG",
            )
            pnp_response = self.dnac._exec(
                family="device_onboarding_pnp",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": replacement_serial},
            )
            self.log(
                "Received PnP API response for replacement "
                "serial '{0}': {1}".format(
                    replacement_serial, pnp_response
                ),
                "DEBUG",
            )

            if not pnp_response or len(pnp_response) == 0:
                self.log(
                    "Replacement device serial '{0}' not "
                    "found in either device inventory or "
                    "PnP. The device may not be registered "
                    "in Catalyst Center.".format(
                        replacement_serial
                    ),
                    "WARNING",
                )
                return None

            device_info = pnp_response[0].get(
                "deviceInfo", {}
            )
            device_name = device_info.get("hostname")

            if not device_name:
                self.log(
                    "PnP device found for replacement "
                    "serial '{0}' but hostname is empty "
                    "or None".format(replacement_serial),
                    "WARNING",
                )
                return None

            self.log(
                "Resolved replacement serial '{0}' to "
                "hostname '{1}' from PnP "
                "inventory".format(
                    replacement_serial, device_name
                ),
                "INFO",
            )
            return device_name

        except Exception as e:
            self.log(
                "Error resolving replacement device hostname "
                "for serial '{0}': {1}".format(
                    replacement_serial, str(e)
                ),
                "WARNING",
            )
            return None

    def get_replacement_device_ip_address(self, workflow_config):
        """
        Resolves replacement device IP address from workflow configuration using device serial number.

        Description:
            Queries both the Cisco Catalyst Center device inventory and PnP APIs to resolve
            the replacement device serial number to its management IP address. Checks regular
            inventory first, then falls back to PnP inventory, though PnP devices may not
            have IP addresses assigned yet.

        Args:
            workflow_config (dict): The device replacement workflow configuration containing
                the replacement device serial number.

        Returns:
            str or None: The replacement device management IP address if found in device
            inventory or PnP inventory, otherwise None if the device is not found,
            no IP is assigned, or API calls fail.
        """
        self.log("Resolving replacement device IP address from workflow configuration: {0}".format(workflow_config), "DEBUG")
        replacement_serial = workflow_config.get("replacementDeviceSerialNumber")
        if not replacement_serial:
            self.log(
                "No replacement device serial number found in "
                "workflow configuration, cannot resolve "
                "IP address",
                "WARNING",
            )
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
            self.log(
                "Received device inventory API response for "
                "replacement serial '{0}': {1}".format(
                    replacement_serial, response
                ),
                "DEBUG",
            )

            if response:
                devices = response.get("response")

                if devices and len(devices) > 0:
                    device_ip = devices[0].get(
                        "managementIpAddress"
                    )

                    if device_ip:
                        self.log(
                            "Resolved replacement serial "
                            "'{0}' to management IP '{1}' "
                            "from device inventory".format(
                                replacement_serial, device_ip
                            ),
                            "INFO",
                        )
                        return device_ip

                    self.log(
                        "Device found in inventory for "
                        "replacement serial '{0}' but "
                        "management IP is empty or "
                        "None".format(replacement_serial),
                        "WARNING",
                    )
                else:
                    self.log(
                        "No device found in inventory for "
                        "replacement serial '{0}'".format(
                            replacement_serial
                        ),
                        "DEBUG",
                    )
            else:
                self.log(
                    "Empty response from device inventory "
                    "API for replacement serial "
                    "'{0}'".format(replacement_serial),
                    "WARNING",
                )

            # If not found in regular inventory, try PnP
            self.log(
                "Falling back to PnP inventory for "
                "replacement serial '{0}' IP "
                "resolution".format(replacement_serial),
                "DEBUG",
            )
            pnp_response = self.dnac._exec(
                family="device_onboarding_pnp",
                function="get_device_list",
                op_modifies=False,
                params={"serialNumber": replacement_serial},
            )
            self.log(
                "Received PnP API response for replacement "
                "serial '{0}': {1}".format(
                    replacement_serial, pnp_response
                ),
                "DEBUG",
            )

            if not pnp_response or len(pnp_response) == 0:
                self.log(
                    "Replacement device serial '{0}' not "
                    "found in either device inventory or "
                    "PnP. Cannot resolve management "
                    "IP.".format(replacement_serial),
                    "WARNING",
                )
                return None

            device_info = pnp_response[0].get(
                "deviceInfo", {}
            )
            device_ip = (
                device_info.get("aaaCredentials", {})
                .get("mgmtIpAddress")
            )

            if not device_ip:
                self.log(
                    "PnP device found for replacement "
                    "serial '{0}' but management IP is "
                    "not assigned. PnP devices may not "
                    "have IP addresses until fully "
                    "onboarded.".format(replacement_serial),
                    "WARNING",
                )
                return None

            self.log(
                "Resolved replacement serial '{0}' to "
                "management IP '{1}' from PnP "
                "inventory".format(
                    replacement_serial, device_ip
                ),
                "INFO",
            )
            return device_ip

        except Exception as e:
            self.log(
                "Error resolving replacement device IP for "
                "serial '{0}': {1}".format(
                    replacement_serial, str(e)
                ),
                "WARNING",
            )
            return None

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates comprehensive YAML configuration files for RMA workflow management.

        Description:
            Orchestrates the complete YAML generation process by processing configuration
            parameters, retrieving device replacement workflow data, and creating structured
            YAML files. Handles component validation, data retrieval coordination, and
            file generation with comprehensive error handling and status reporting.

        Args:
            yaml_config_generator (dict): Configuration parameters containing:
                - file_path (str, optional): Target file path for YAML output.
                - generate_all_configurations (bool): Flag for retrieving all configurations.
                - component_specific_filters (dict, optional): Filtering criteria for specific workflows.
                - global_filters (dict, optional): Global filtering options.

        Returns:
            object: Self instance with updated status and results:
                - Sets operation result to success with file path information on success.
                - Sets operation result to failure with error details if issues occur.
                - Updates self.msg with operation status and component processing details.
        """
        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Fix: Properly handle file_path when it's None
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            file_path = self.generate_filename()
        else:
            self.log(
                "Using user-specified file path: {0}".format(
                    file_path
                ),
                "DEBUG",
            )

        self.log("File path determined: {0}".format(file_path), "DEBUG")

        # Handle generate_all_configurations flag
        generate_all_configurations = yaml_config_generator.get("generate_all_configurations", False)
        self.log(
            "Auto-discovery mode: {0}".format(
                "enabled" if generate_all_configurations else "disabled"
            ),
            "INFO",
        )

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

        module_supported_network_elements = self.module_schema.get("network_elements", {})

        if generate_all_configurations:
            components_list = list(module_supported_network_elements.keys())
            self.log(
                "Auto-discovery mode: using all available "
                "components: {0}".format(components_list),
                "INFO",
            )
        else:
            components_list = component_specific_filters.get(
                "components_list", list(module_supported_network_elements.keys())
            )

        self.log(
            "Processing {0} component(s): {1}".format(
                len(components_list), components_list
            ),
            "INFO",
        )

        components_processed = 0
        components_skipped = 0
        total_configurations = 0

        config_list = []

        for component_index, component in enumerate(
            components_list, start=1
        ):
            self.log(
                "Processing component {0}/{1}: '{2}'".format(
                    component_index, len(components_list), component
                ),
                "INFO",
            )

            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Skipping unsupported network element: {0}".format(component),
                    "WARNING",
                )
                components_skipped += 1
                continue

            filters = {
                "global_filters": yaml_config_generator.get("global_filters", {}),
                "component_specific_filters": component_specific_filters
            }

            operation_func = network_element.get("get_function_name")
            self.log("Operation function for {0}: {1}".format(component, operation_func), "DEBUG")

            if not callable(operation_func):
                self.log(
                    "No callable retrieval function found for "
                    "component '{0}'. Skipping.".format(component),
                    "ERROR",
                )
                components_skipped += 1
                continue

            try:
                self.log(
                    "Calling retrieval function for component "
                    "'{0}'".format(component),
                    "INFO",
                )
                details = operation_func(network_element, filters)
                self.log(
                    "Retrieved details for component '{0}': "
                    "{1}".format(component, details),
                    "DEBUG",
                )

                if component in details and details[component]:
                    for workflow in details[component]:
                        config_list.append(workflow)

                    config_count = len(details[component])
                    total_configurations += config_count
                    components_processed += 1
                    self.log("Successfully added {0} configurations for component {1}".format(
                        config_count, component), "INFO")
                else:
                    components_skipped += 1
                    self.log(
                        "No data found for component: {0}".format(component), "WARNING"
                    )

            except Exception as e:
                self.log("Error retrieving data for component {0}: {1}".format(component, str(e)), "ERROR")
                components_skipped += 1
                continue

        self.log("Processing summary: {0} components processed successfully, {1} skipped".format(
            components_processed, components_skipped), "INFO")

        if not config_list:
            no_config_message = (
                "No device replacement workflows found to process for module '{0}'. "
                "Verify that RMA workflows are configured in Catalyst Center or check user permissions."
            ).format(self.module_name)

            response_data = {
                "components_processed": components_processed,
                "components_skipped": components_skipped,
                "configurations_count": 0,
                "message": no_config_message,
                "status": "success"
            }

            self.set_operation_result("success", False, no_config_message, "INFO")

            self.msg = response_data
            self.result["response"] = response_data
            return self

        final_dict = {"config": config_list}
        self.log("Final dictionary created with {0} device replacement workflow configurations".format(len(config_list)), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            success_message = "YAML configuration file generated successfully for module '{0}'".format(self.module_name)

            response_data = {
                "components_processed": components_processed,
                "components_skipped": components_skipped,
                "configurations_count": total_configurations,
                "file_path": file_path,
                "message": success_message,
                "status": "success"
            }

            self.set_operation_result("success", True, success_message, "INFO")

            self.msg = response_data
            self.result["response"] = response_data
        else:
            error_message = "Failed to write YAML configuration to file: {0}".format(file_path)

            response_data = {
                "message": error_message,
                "status": "failed"
            }

            self.set_operation_result("failed", False, error_message, "ERROR")
            self.msg = response_data
            self.result["response"] = response_data

        return self

    def get_want(self, config, state):
        """
        Processes and validates configuration parameters for RMA API operations.

        Description:
            Transforms input configuration parameters into the internal 'want' structure
            used throughout the module. Validates parameters and prepares configuration
            data for subsequent processing steps in the RMA workflow generation process.

        Args:
            config (dict): The configuration data containing generation parameters,
                component filters, and RMA workflow settings.
            state (str): The desired state for the operation (must be 'gathered').

        Returns:
            object: Self instance with updated attributes:
                - self.want (dict): Contains validated configuration ready for processing.
                - self.msg (str): Success message indicating parameter collection completion.
                - self.status (str): Status set to "success" after parameter validation.
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
        Executes YAML configuration file generation for brownfield template workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.
        """

        start_time = time.time()
        self.log(
            "Starting YAML playbook generation workflow for "
            "RMA configurations",
            "INFO",
        )
        # Define workflow operations
        workflow_operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]
        operations_executed = 0
        operations_skipped = 0

        # Iterate over operations and process them
        self.log("Beginning iteration over defined workflow operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
        ):
            self.log(
                "Iteration {0}: Checking parameters for {1} operation with param_key '{2}'.".format(
                    index, operation_name, param_key
                ),
                "DEBUG",
            )
            params = self.want.get(param_key)
            if not params:
                self.log(
                    "No parameters found for '{0}'. Skipping "
                    "operation.".format(operation_name),
                    "WARNING",
                )
                operations_skipped += 1
                continue

            if params:
                self.log(
                    "Executing '{0}' operation with provided "
                    "parameters".format(operation_name),
                    "INFO",
                )
                self.log(
                    "Iteration {0}: Parameters found for {1}. Starting processing.".format(
                        index, operation_name
                    ),
                    "INFO",
                )

                try:
                    operation_func(params)
                    operations_executed += 1
                    self.log(
                        "{0} operation completed successfully".format(operation_name),
                        "DEBUG"
                    )
                except Exception as e:
                    self.log(
                        "{0} operation failed with error: {1}".format(operation_name, str(e)),
                        "ERROR"
                    )
                    self.set_operation_result(
                        "failed", True,
                        "{0} operation failed: {1}".format(operation_name, str(e)),
                        "ERROR"
                    ).check_return_status()

            else:
                operations_skipped += 1
                self.log(
                    "No parameters found for '{0}'. Skipping "
                    "operation.".format(operation_name),
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
    """
    Main entry point for the Cisco Catalyst Center brownfield RMA playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield RMA device replacement workflow extraction.

    Purpose:
        Initializes and executes the brownfield RMA playbook generator workflow to
        extract existing device replacement configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create RMAPlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 2.3.5.3)
        5. Validate and sanitize state parameter
        6. Execute input parameter validation
        7. Process each configuration item in the playbook
        8. Handle generate_all_configurations and default component logic
        9. Execute state-specific operations (gathered workflow)
        10. Return results via module.exit_json()

    Module Arguments:
        Connection Parameters:
            - dnac_host (str, required): Catalyst Center hostname/IP
            - dnac_port (str, default="443"): HTTPS port
            - dnac_username (str, default="admin"): Authentication username
            - dnac_password (str, required, no_log): Authentication password
            - dnac_verify (bool, default=True): SSL certificate verification

        API Configuration:
            - dnac_version (str, default="2.2.3.3"): Catalyst Center version
            - dnac_api_task_timeout (int, default=1200): API timeout (seconds)
            - dnac_task_poll_interval (int, default=2): Poll interval (seconds)
            - validate_response_schema (bool, default=True): Schema validation

        Logging Configuration:
            - dnac_debug (bool, default=False): Debug mode
            - dnac_log (bool, default=False): Enable file logging
            - dnac_log_level (str, default="WARNING"): Log level
            - dnac_log_file_path (str, default="dnac.log"): Log file path
            - dnac_log_append (bool, default=True): Append to log file

        Playbook Configuration:
            - config (list[dict], required): Configuration parameters list
            - state (str, default="gathered", choices=["gathered"]): Workflow state

    Version Requirements:
        - Minimum Catalyst Center version: 2.3.5.3
        - Introduced APIs for RMA device replacement workflow retrieval:
            * Device Replacement (return_replacement_devices_with_details)
            * Device Inventory (get_device_list)

    Supported States:
        - gathered: Extract existing RMA device replacement workflows and generate YAML playbook
        - Future: merged, deleted, replaced (reserved for future use)

    Error Handling:
        - Version compatibility failures: Module exits with error
        - Invalid state parameter: Module exits with error
        - Input validation failures: Module exits with error
        - Configuration processing errors: Module exits with error
        - All errors are logged and returned via module.fail_json()

    Return Format:
        Success: module.exit_json() with result containing:
            - changed (bool): Whether changes were made
            - msg (str/dict): Operation result message or structured response
            - response (dict): Detailed operation results with statistics
            - status (str): Operation status ("success")

        Failure: module.fail_json() with error details:
            - failed (bool): True
            - msg (str): Error message
            - error (str): Detailed error information
    """
    # Record module initialization start time for performance tracking
    module_start_time = time.time()

    # Define the specification for the module's arguments
    # This structure defines all parameters accepted by the module with their types,
    # defaults, and validation rules
    element_spec = {
        # ============================================
        # Catalyst Center Connection Parameters
        # ============================================
        "dnac_host": {
            "required": True,
            "type": "str"
        },
        "dnac_port": {
            "type": "str",
            "default": "443"
        },
        "dnac_username": {
            "type": "str",
            "default": "admin",
            "aliases": ["user"]
        },
        "dnac_password": {
            "type": "str",
            "no_log": True  # Prevent password from appearing in logs
        },
        "dnac_verify": {
            "type": "bool",
            "default": True
        },

        # ============================================
        # API Configuration Parameters
        # ============================================
        "dnac_version": {
            "type": "str",
            "default": "2.2.3.3"
        },
        "dnac_api_task_timeout": {
            "type": "int",
            "default": 1200
        },
        "dnac_task_poll_interval": {
            "type": "int",
            "default": 2
        },
        "validate_response_schema": {
            "type": "bool",
            "default": True
        },

        # ============================================
        # Logging Configuration Parameters
        # ============================================
        "dnac_debug": {
            "type": "bool",
            "default": False
        },
        "dnac_log_level": {
            "type": "str",
            "default": "WARNING"
        },
        "dnac_log_file_path": {
            "type": "str",
            "default": "dnac.log"
        },
        "dnac_log_append": {
            "type": "bool",
            "default": True
        },
        "dnac_log": {
            "type": "bool",
            "default": False
        },

        # ============================================
        # Playbook Configuration Parameters
        # ============================================
        "config": {
            "required": True,
            "type": "list",
            "elements": "dict"
        },
        "state": {
            "default": "gathered",
            "choices": ["gathered"]
        },
    }

    # Initialize the Ansible module with argument specification
    # supports_check_mode=True allows module to run in check mode (dry-run)
    module = AnsibleModule(
        argument_spec=element_spec,
        supports_check_mode=True
    )

    # Create initial log entry with module initialization timestamp
    # Note: Logging is not yet available since object isn't created
    initialization_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_start_time)
    )

    # Initialize the RMAPlaybookGenerator object
    # This creates the main orchestrator for brownfield RMA device replacement extraction
    ccc_rma_playbook_generator = RMAPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_rma_playbook_generator.log(
        "Starting Ansible module execution for brownfield RMA playbook "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_rma_playbook_generator.log(
        "Module initialized with parameters: dnac_host={0}, dnac_port={1}, "
        "dnac_username={2}, dnac_verify={3}, dnac_version={4}, state={5}, "
        "config_items={6}".format(
            module.params.get("dnac_host"),
            module.params.get("dnac_port"),
            module.params.get("dnac_username"),
            module.params.get("dnac_verify"),
            module.params.get("dnac_version"),
            module.params.get("state"),
            len(module.params.get("config", []))
        ),
        "DEBUG"
    )

    # ============================================
    # Version Compatibility Check
    # ============================================
    min_version = "2.3.5.3"
    ccc_version = ccc_rma_playbook_generator.get_ccc_version()

    ccc_rma_playbook_generator.log(
        "Validating Cisco Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of {1} for RMA device replacement APIs".format(
            ccc_version, min_version
        ),
        "INFO"
    )

    if (ccc_rma_playbook_generator.compare_dnac_versions(
            ccc_version, min_version) < 0):

        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for RMA Workflow Manager Module. Supported versions "
            "start from '{1}' onwards. Version '{1}' introduces APIs for retrieving "
            "device replacement workflows including return_replacement_devices_with_details "
            "and device inventory management (get_device_list) from the Catalyst Center.".format(
                ccc_version, min_version
            )
        )

        ccc_rma_playbook_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_rma_playbook_generator.msg = error_msg
        ccc_rma_playbook_generator.set_operation_result(
            "failed", False, ccc_rma_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_rma_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required RMA device replacement APIs".format(ccc_version),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_rma_playbook_generator.params.get("state")

    ccc_rma_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_rma_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_rma_playbook_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_rma_playbook_generator.supported_states
            )
        )

        ccc_rma_playbook_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_rma_playbook_generator.status = "invalid"
        ccc_rma_playbook_generator.msg = error_msg
        ccc_rma_playbook_generator.check_return_status()

    ccc_rma_playbook_generator.log(
        "State validation passed - using state '{0}' for RMA workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_rma_playbook_generator.log(
        "Starting comprehensive input parameter validation for RMA playbook configuration",
        "INFO"
    )

    ccc_rma_playbook_generator.validate_input().check_return_status()

    ccc_rma_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet RMA module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing and Default Handling
    # ============================================
    config_list = ccc_rma_playbook_generator.validated_config

    ccc_rma_playbook_generator.log(
        "Starting configuration processing and default handling - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    # Handle generate_all_configurations and set component defaults
    for config_index, config_item in enumerate(config_list, start=1):
        ccc_rma_playbook_generator.log(
            "Processing configuration item {0}/{1} for generate_all_configurations and default component handling".format(
                config_index, len(config_list)
            ),
            "DEBUG"
        )

        if config_item.get("generate_all_configurations", False):
            ccc_rma_playbook_generator.log(
                "Configuration item {0}: generate_all_configurations=True detected. Setting default "
                "components to include device_replacement_workflows".format(
                    config_index
                ),
                "INFO"
            )

            # Set default components when generate_all_configurations is True
            if not config_item.get("component_specific_filters"):
                config_item["component_specific_filters"] = {
                    "components_list": ["device_replacement_workflows"]
                }
                ccc_rma_playbook_generator.log(
                    "Configuration item {0}: Set default component_specific_filters for generate_all mode: {1}".format(
                        config_index, config_item["component_specific_filters"]
                    ),
                    "DEBUG"
                )
            else:
                ccc_rma_playbook_generator.log(
                    "Configuration item {0}: component_specific_filters already provided in generate_all mode - "
                    "using existing filters: {1}".format(
                        config_index, config_item.get("component_specific_filters")
                    ),
                    "DEBUG"
                )

        elif config_item.get("component_specific_filters") is None:
            ccc_rma_playbook_generator.log(
                "Configuration item {0}: No component_specific_filters provided in normal mode. "
                "Applying default configuration to retrieve device_replacement_workflows".format(
                    config_index
                ),
                "INFO"
            )

            # Existing fallback logic for when no filters are specified
            ccc_rma_playbook_generator.msg = (
                "No component filters specified, defaulting to device_replacement_workflows."
            )

            config_item["component_specific_filters"] = {
                "components_list": ["device_replacement_workflows"]
            }

            ccc_rma_playbook_generator.log(
                "Configuration item {0}: Applied default component_specific_filters: {1}".format(
                    config_index, config_item["component_specific_filters"]
                ),
                "DEBUG"
            )
        else:
            ccc_rma_playbook_generator.log(
                "Configuration item {0}: component_specific_filters already provided in normal mode - "
                "using existing filters: {1}".format(
                    config_index, config_item.get("component_specific_filters")
                ),
                "DEBUG"
            )

    # Update validated config after default handling
    ccc_rma_playbook_generator.validated_config = config_list

    ccc_rma_playbook_generator.log(
        "Configuration preprocessing completed. Updated validated_config with default component "
        "handling. Final configuration count: {0}".format(len(config_list)),
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    final_config_list = ccc_rma_playbook_generator.validated_config

    ccc_rma_playbook_generator.log(
        "Starting configuration processing loop - will process {0} final configuration "
        "item(s) after default handling".format(len(final_config_list)),
        "INFO"
    )

    for config_index, config_item in enumerate(final_config_list, start=1):
        components_list = config_item.get("component_specific_filters", {}).get("components_list", "all")

        ccc_rma_playbook_generator.log(
            "Processing configuration item {0}/{1} for state '{2}' with components: {3}".format(
                config_index, len(final_config_list), state, components_list
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_rma_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_rma_playbook_generator.reset_values()

        # Collect desired state (want) from configuration
        ccc_rma_playbook_generator.log(
            "Collecting desired state parameters from configuration item {0} - "
            "building want dictionary for RMA operations".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_rma_playbook_generator.get_want(
            config_item, state
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_rma_playbook_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1} - will retrieve device replacement workflows "
            "from Catalyst Center".format(state, config_index),
            "INFO"
        )
        ccc_rma_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_rma_playbook_generator.log(
            "Successfully completed processing for configuration item {0}/{1} - "
            "RMA device replacement workflow data extraction and YAML generation completed".format(
                config_index, len(final_config_list)
            ),
            "INFO"
        )

    # ============================================
    # Module Completion and Exit
    # ============================================
    module_end_time = time.time()
    module_duration = module_end_time - module_start_time

    completion_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_end_time)
    )

    ccc_rma_playbook_generator.log(
        "RMA playbook generator module execution completed successfully "
        "at timestamp {0}. Total execution time: {1:.2f} seconds. Processed {2} "
        "configuration item(s) with final status: {3}".format(
            completion_timestamp,
            module_duration,
            len(final_config_list),
            ccc_rma_playbook_generator.status
        ),
        "INFO"
    )

    ccc_rma_playbook_generator.log(
        "Final module result summary: changed={0}, msg_type={1}, response_available={2}".format(
            ccc_rma_playbook_generator.result.get("changed", False),
            type(ccc_rma_playbook_generator.result.get("msg")).__name__,
            "response" in ccc_rma_playbook_generator.result
        ),
        "DEBUG"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_rma_playbook_generator.log(
        "Exiting Ansible module with result containing RMA device replacement extraction results",
        "DEBUG"
    )

    module.exit_json(**ccc_rma_playbook_generator.result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for SD-Access Fabric Transits Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Abhishek Maheshwari, Sunil Shatagopa, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: sda_fabric_transits_playbook_config_generator
short_description: Generate YAML configurations playbook for C(sda_fabric_transits_workflow_manager) module.
description:
- Generates YAML configurations compatible with the C(sda_fabric_transits_workflow_manager)
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Abhishek Maheshwari (@abmahesh)
- Sunil Shatagopa (@shatagopasunil)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `sda_fabric_transits_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to C(true), automatically generates YAML configurations for all the fabric transits
            present in the Cisco Catalyst Center, ignoring any provided filters.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete playbook configuration infrastructure discovery and documentation.
          - When set to false, the module uses provided filters to generate a targeted YAML configuration.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  C(sda_fabric_transits_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(sda_fabric_transits_playbook_config_2026-02-20_13-48-23.yml).
        type: str
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration file.
        - If C(components_list) is specified, only those components are included, regardless of other filters.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are
              - Fabric Transits C(sda_fabric_transits)
            - For example, ["sda_fabric_transits"].
            - If not specified, all components are included.
            type: list
            elements: str
            choices: ["sda_fabric_transits"]
          sda_fabric_transits:
            description:
            - Fabric transits to filter by name or transit type.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                - Transit name to filter fabric transits by name.
                type: str
              transit_type:
                description:
                - Transit type to filter fabric transits by type.
                - Valid values are IP_BASED_TRANSIT, SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT
                type: str
requirements:
- dnacentersdk >= 2.3.7.9
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_site
    - sda.Sda.get_transit_networks
    - network_device.NetworkDevice.get_device_list
- Paths used are
    - GET /dna/intent/api/v1/sites
    - GET /dna/intent/api/v1/sda/transit-networks
    - GET /dna/intent/api/v1/network-device
seealso:
- module: cisco.dnac.sda_fabric_transits_workflow_manager
  description: Module for managing fabric transits in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Auto-generate YAML Configuration for all fabric transits
  cisco.dnac.sda_fabric_transits_playbook_config_generator:
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
  cisco.dnac.sda_fabric_transits_playbook_config_generator:
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
        file_path: "/tmp/all_config.yml"

- name: Generate YAML Configuration with specific fabric transits components only
  cisco.dnac.sda_fabric_transits_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_transits_config.yml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]

- name: Generate YAML Configuration for fabric transits with transit type filter
  cisco.dnac.sda_fabric_transits_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_transits_config.yml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]
          sda_fabric_transits:
            - transit_type: "IP_BASED_TRANSIT"
            - transit_type: "SDA_LISP_BGP_TRANSIT"

- name: Generate YAML Configuration for fabric transits with name filter
  cisco.dnac.sda_fabric_transits_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_transits_config.yaml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]
          sda_fabric_transits:
            - name: "Transit1"
            - name: "Transit2"

- name: Generate YAML Configuration for fabric transits with name and type filter
  cisco.dnac.sda_fabric_transits_playbook_config_generator:
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
      - file_path: "/tmp/catc_fabric_transits_config.yaml"
        component_specific_filters:
          components_list: ["sda_fabric_transits"]
          sda_fabric_transits:
            - name: "Transit1"
              transit_type: "IP_BASED_TRANSIT"
            - name: "Transit2"
              transit_type: "SDA_LISP_PUB_SUB_TRANSIT"
"""


RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": {
            "components_processed": 1,
            "components_skipped": 0,
            "configurations_count": 1,
            "file_path": "sda_fabric_transits_playbook_config_2026-02-20_13-48-23.yml",
            "message": "YAML configuration file generated successfully for module 'sda_fabric_transits_workflow_manager'",
            "status": "success"
        },
        "response": {
            "components_processed": 1,
            "components_skipped": 0,
            "configurations_count": 1,
            "file_path": "sda_fabric_transits_playbook_config_2026-02-20_13-48-23.yml",
            "message": "YAML configuration file generated successfully for module 'sda_fabric_transits_workflow_manager'",
            "status": "success"
        },
        "status": "success"
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg":
            "Validation Error in entry 1: 'component_specific_filters' must be provided with 'components_list' key
             when 'generate_all_configurations' is set to False.",
        "response":
            "Validation Error in entry 1: 'component_specific_filters' must be provided with 'components_list' key
             when 'generate_all_configurations' is set to False."
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
from collections import OrderedDict


class SdaFabricTransitsPlaybookConfigGenerator(DnacBase, BrownFieldHelper):
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
        self.device_id_ip_mapping = self.get_device_id_management_ip_mapping()
        self.module_name = "sda_fabric_transits_workflow_manager"

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
                "default": False
            },
            "file_path": {
                "type": "str",
                "required": False
            },
            "component_specific_filters": {
                "type": "dict",
                "required": False
            }
        }

        # Validate params
        self.log("Validating configuration against schema", "DEBUG")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log("Validating invalid parameters against provided config", "DEBUG")
        self.validate_invalid_params(self.config, temp_spec.keys())

        self.log("Validating minimum requirements against provided config: {0}".format(self.config), "DEBUG")
        self.validate_minimum_requirements(self.config)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_filters_schema(self):
        """
        Constructs and returns a structured mapping for managing fabric transits.
        This mapping includes associated filters, temporary specification functions, API details,
        and fetch function references used in the transits network workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods like
                `fabric_transit_temp_spec`, `get_fabric_transits_configuration`.

        Return:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a network component
                (e.g., 'sda_fabric_transits') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'sda').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
        """

        self.log("Building workflow filters schema for sda fabric transits networks module", "DEBUG")

        schema = {
            "network_elements": {
                "sda_fabric_transits": {
                    "filters": ["name", "transit_type"],
                    "temp_spec_function": self.fabric_transit_temp_spec,
                    "api_function": "get_transit_networks",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_transits_configuration,
                },
            }
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network element(s): {network_elements}",
            "INFO",
        )

        return schema

    def fabric_transit_temp_spec(self):
        """
        Constructs a temporary specification for fabric transits, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as transit name,
        transit type, site hierarchy, IP transit settings, and SDA transit settings.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of fabric transit attributes.
        """

        self.log("Generating temporary specification for fabric transits.", "DEBUG")

        fabric_transit = OrderedDict(
            {
                "name": {"type": "str", "source_key": "name"},
                "transit_site_hierarchy": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_transit_site_hierarchy,
                },
                "transit_type": {"type": "str", "source_key": "type"},
                "ip_transit_settings": {
                    "type": "dict",
                    "source_key": "ipTransitSettings",
                    "options": OrderedDict(
                        {
                            "routing_protocol_name": {
                                "type": "str",
                                "source_key": "routingProtocolName",
                            },
                            "autonomous_system_number": {
                                "type": "int",
                                "source_key": "autonomousSystemNumber",
                            },
                        }
                    ),
                },
                "sda_transit_settings": {
                    "type": "dict",
                    "source_key": "sdaTransitSettings",
                    "options": OrderedDict(
                        {
                            "is_multicast_over_transit_enabled": {
                                "type": "bool",
                                "source_key": "isMulticastOverTransitEnabled",
                            },
                            "control_plane_network_device_ips": {
                                "type": "list",
                                "elements": "str",
                                "special_handling": True,
                                "transform": self.transform_control_plane_device_ids_to_ips,
                            },
                        }
                    ),
                },
            }
        )

        self.log("Fabric transit temp spec generated successfully.", "DEBUG")

        return fabric_transit

    def transform_transit_site_hierarchy(self, transit_details):
        """
        Transforms a site ID into its corresponding site hierarchy name.

        Args:
            transit_details (dict): A dictionary containing transit network information,
                                    expected to include the key 'siteId'.

        Returns:
            str or None: The site hierarchy name corresponding to the provided site ID if found, otherwise None.
        """

        self.log(
            "Starting site name transformation for given site id: {0}"
            .format(transit_details.get("siteId", "Unknown")), "DEBUG"
        )

        site_id = transit_details.get("siteId")
        if not site_id:
            self.log(
                "No site ID found in transits details: {0}".format(transit_details),
                "DEBUG"
            )
            return site_id

        site_hierarchy_name = self.site_id_name_dict.get(site_id)
        if not site_hierarchy_name:
            self.log(
                "Site ID {0} not found in site ID to name mapping.".format(site_id),
                "WARNING",
            )
            return site_hierarchy_name

        self.log(
            "Completed site name transformation for site id: {0}. "
            "Transformed site name: {1}". format(site_id, site_hierarchy_name),
            "DEBUG"
        )

        return site_hierarchy_name

    def transform_control_plane_device_ids_to_ips(self, sda_transit_settings):
        """
        Transforms control plane network device IDs to their corresponding IP addresses.

        Args:
            sda_transit_settings (dict): A dictionary containing transits network information,
                expected to include a list of device IDs under the 'controlPlaneNetworkDeviceIds' key.

        Returns:
            list: A list of management IP addresses corresponding to the device IDs.
        """

        self.log(
            "Starting control plane device ip(s) transformation for given control plane device id(s): {0}"
            .format(sda_transit_settings.get("controlPlaneNetworkDeviceIds", "Unknown")),
            "DEBUG"
        )

        control_plane_device_ids = sda_transit_settings.get("controlPlaneNetworkDeviceIds")
        if not control_plane_device_ids:
            self.log(
                "No Control Plane Device IDs found in transits settings details: {0}".format(sda_transit_settings),
                "DEBUG"
            )
            return control_plane_device_ids

        self.log(
            "Processing {0} control plane devices for device id(s): {1}"
            .format(len(control_plane_device_ids), control_plane_device_ids),
            "DEBUG"
        )

        if not control_plane_device_ids:
            self.log(
                "No control plane device IDs found in SDA transit settings", "DEBUG"
            )
            return control_plane_device_ids

        device_ips = []

        for device_id in control_plane_device_ids:
            device_ip = self.device_id_ip_mapping.get(device_id)
            if not device_ip:
                self.log(
                    "Device ID {0} not found in device ID to IP mapping.".format(
                        device_id
                    ),
                    "DEBUG",
                )
                continue

            self.log(
                "Transformed device ip {0} for device id: {1}".format(
                    device_ip, device_id
                ),
                "DEBUG"
            )
            device_ips.append(device_ip)

        self.log(
            "Transformed control plane device IDs to IPs: {0}".format(device_ips),
            "DEBUG",
        )
        self.log(
            "Completed control plane device IPs transformation. Transformed device IP(s): {0}"
            .format(device_ips),
            "DEBUG"
        )

        return sorted(device_ips) if device_ips else []

    def get_fabric_transits_configuration(self, network_element, filters):
        """
        Retrieves fabric transits based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving fabric transits.
            filters (dict): Dictionary containing global filters and component_specific_filters for fabric transits.

        Returns:
            dict: A dictionary containing the modified details of fabric transits.
        """

        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")

        self.log(
            "Starting to retrieve fabric transits with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return {"fabric_transits": []}

        # Extract API family and function from network_element
        final_fabric_transits = []

        self.log(
            "Getting fabric transits using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for fabric transits retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                supported_keys = {"name", "transit_type"}

                if "name" in filter_param:
                    params["name"] = filter_param["name"]
                if "transit_type" in filter_param:
                    params["type"] = filter_param["transit_type"]

                unsupported_keys = set(filter_param.keys()) - supported_keys
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for fabric transits: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching fabric transits with parameters: {0}".format(params),
                    "DEBUG"
                )

                fabric_transit_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if fabric_transit_details:
                    final_fabric_transits.extend(fabric_transit_details)
                    self.log(
                        "Retrieved {0} fabric transit(s): {1}".format(
                            len(fabric_transit_details), fabric_transit_details
                        ),
                        "DEBUG",
                    )
                else:
                    self.log(
                        "No fabric transits found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for fabric transits retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

        else:
            self.log("Fetching all fabric transits from Catalyst Center", "DEBUG")

            fabric_transit_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if fabric_transit_details:
                final_fabric_transits.extend(fabric_transit_details)
                self.log(
                    "Retrieved {0} fabric transit(s) from Catalyst Center"
                    .format(len(fabric_transit_details)),
                    "DEBUG",
                )
            else:
                self.log("No fabric transits found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} fabric transit(s) using fabric_transit temp spec".format(
                len(final_fabric_transits)
            ),
            "DEBUG"
        )
        fabric_transit_temp_spec = self.fabric_transit_temp_spec()
        transit_details = self.modify_parameters(
            fabric_transit_temp_spec, final_fabric_transits
        )
        modified_fabric_transits_details = {}

        if transit_details:
            modified_fabric_transits_details["fabric_transits"] = transit_details

        self.log(
            "Completed retrieving fabric transit(s): {0}".format(
                modified_fabric_transits_details
            ),
            "INFO",
        )

        return modified_fabric_transits_details

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for sda fabric transits workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.
        """

        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
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
            if params:
                self.log(
                    "Iteration {0}: Parameters found for {1}. Starting processing.".format(
                        index, operation_name
                    ),
                    "INFO",
                )

                try:
                    operation_func(params).check_return_status()
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
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_sda_fabric_transits_playbook_config_generator = SdaFabricTransitsPlaybookConfigGenerator(
        module
    )
    if (
        ccc_sda_fabric_transits_playbook_config_generator.compare_dnac_versions(
            ccc_sda_fabric_transits_playbook_config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_sda_fabric_transits_playbook_config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for SDA FABRIC TRANSITS Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_sda_fabric_transits_playbook_config_generator.get_ccc_version()
            )
        )
        ccc_sda_fabric_transits_playbook_config_generator.set_operation_result(
            "failed", False, ccc_sda_fabric_transits_playbook_config_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_fabric_transits_playbook_config_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_sda_fabric_transits_playbook_config_generator.supported_states:
        ccc_sda_fabric_transits_playbook_config_generator.status = "invalid"
        ccc_sda_fabric_transits_playbook_config_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_sda_fabric_transits_playbook_config_generator.check_recturn_status()

    # Validate the input parameters and check the return statusk
    ccc_sda_fabric_transits_playbook_config_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_sda_fabric_transits_playbook_config_generator.validated_config:
        ccc_sda_fabric_transits_playbook_config_generator.reset_values()
        ccc_sda_fabric_transits_playbook_config_generator.get_want(
            config, state
        ).check_return_status()
        ccc_sda_fabric_transits_playbook_config_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_sda_fabric_transits_playbook_config_generator.result)


if __name__ == "__main__":
    main()

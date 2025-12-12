#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Assurance Device Health Score Settings Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Megha Kandari, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_assurance_device_health_score_settings_playbook_generator
short_description: Generate YAML configurations playbook for 'assurance_device_health_score_settings_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'assurance_device_health_score_settings_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the assurance device health score settings
  configured within the Cisco Catalyst Center.
- Supports extraction of device family KPI settings including thresholds, overall health inclusion,
  and issue threshold synchronization settings.
- Uses multiple API calls with includeForOverallHealth parameter (both true and false) to ensure complete data extraction.
- When device families are specified, makes separate API calls for each device family for optimal filtering.
- When no device families are specified, retrieves all available device health score settings from the system.
version_added: 6.40.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Megha Kandari (@mekandar)
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
      - A list of filters for generating YAML playbook compatible with the 'assurance_device_health_score_settings_workflow_manager'
        module.
      - Filters specify which device families and KPI settings to include in the YAML configuration file.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all device families and all available KPI settings.
          - This mode discovers all configured device health score settings in Cisco Catalyst Center.
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
            a default file name "assurance_device_health_score_settings_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
          - For example, "assurance_device_health_score_settings_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
        required: false
      component_specific_filters:
        description:
          - Filters to specify which device families and KPI settings to include in the YAML configuration file.
          - Allows granular selection of specific device families and their KPI configurations.
          - If not specified, all configured device health score settings will be extracted.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
              - List of components to extract. Currently supports "device_health_score_settings".
              - When specified, determines which components to process.
              - If only components_list is provided without device_health_score_settings filters, all device families will be extracted.
            type: list
            elements: str
            required: false
          device_health_score_settings:
            description:
              - Specific filters for device health score settings extraction.
              - Allows fine-grained control over device families and KPI settings to extract.
            type: dict
            required: false
            suboptions:
              device_families:
                description:
                  - List of specific device families to extract KPI settings for.
                  - Valid values include device family names like "UNIFIED_AP", "ROUTER", "SWITCH_AND_HUB", "WIRELESS_CONTROLLER", etc.
                  - If not specified, all device families with configured KPI settings will be extracted.
                  - Example ["UNIFIED_AP", "ROUTER", "SWITCH_AND_HUB"]
                type: list
                elements: str
                required: false

requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Method used is devices.Devices.get_all_health_score_definitions_for_given_filters
- Path used is GET /dna/intent/api/v1/device-health/health-score/definitions
"""

EXAMPLES = r"""

- name: Generate YAML Configuration for all device health score settings
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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

- name: Generate YAML Configuration with custom file path
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/assurance_health_score_settings.yml"

- name: Generate YAML Configuration for all device health score components
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/assurance_health_score_settings.yml"
        component_specific_filters:
          components_list: ["device_health_score_settings"]

- name: Generate YAML Configuration for specific device families
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/specific_device_health_score_settings.yml"
        component_specific_filters:
          components_list: ["device_health_score_settings"]
          device_health_score_settings:
            device_families: ["UNIFIED_AP", "ROUTER", "SWITCH_AND_HUB", "WIRELESS_CONTROLLER"]

- name: Generate YAML Configuration for specific device families and KPIs
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/filtered_device_health_score_settings.yml"
        component_specific_filters:
          components_list: ["device_health_score_settings"]
          device_health_score_settings:
            device_families: ["UNIFIED_AP", "ROUTER"]
            kpi_names: ["Interference 6 GHz", "Link Error", "CPU Utilization"]

- name: Generate YAML Configuration using legacy filter format
  cisco.dnac.brownfield_assurance_device_health_score_settings_playbook_generator:
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
      - file_path: "/tmp/legacy_device_health_score_settings.yml"
        component_specific_filters:
          device_families: ["UNIFIED_AP", "ROUTER"]

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
          "message": "YAML config generation succeeded for module 'assurance_device_health_score_settings_workflow_manager'.",
          "file_path": "/tmp/assurance_health_score_settings.yml",
          "configurations_generated": 15,
          "operation_summary": {
            "total_device_families_processed": 3,
            "total_kpis_processed": 15,
            "total_successful_operations": 15,
            "total_failed_operations": 0,
            "device_families_with_complete_success": ["UNIFIED_AP", "ROUTER", "SWITCH"],
            "device_families_with_partial_success": [],
            "device_families_with_complete_failure": [],
            "success_details": [
              {
                "device_family": "UNIFIED_AP",
                "kpi_name": "Interference 6 GHz",
                "status": "success"
              }
            ],
            "failure_details": []
          }
        },
      "msg": "YAML config generation succeeded for module 'assurance_device_health_score_settings_workflow_manager'."
    }

# Case_2: No Configurations Found Scenario
response_2:
  description: A dictionary with the response when no configurations are found
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "message": "No configurations or components to process for module "
                     "'assurance_device_health_score_settings_workflow_manager'. "
                     "Verify input filters or configuration.",
          "operation_summary": {
            "total_device_families_processed": 0,
            "total_kpis_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "device_families_with_complete_success": [],
            "device_families_with_partial_success": [],
            "device_families_with_complete_failure": [],
            "success_details": [],
            "failure_details": []
          }
        },
      "msg": "No configurations or components to process for module "
             "'assurance_device_health_score_settings_workflow_manager'. "
             "Verify input filters or configuration."
    }

# Case_3: Error Scenario
response_3:
  description: A dictionary with error details when YAML generation fails
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "message": "YAML config generation failed for module 'assurance_device_health_score_settings_workflow_manager'.",
          "file_path": "/tmp/assurance_health_score_settings.yml",
          "operation_summary": {
            "total_device_families_processed": 2,
            "total_kpis_processed": 10,
            "total_successful_operations": 8,
            "total_failed_operations": 2,
            "device_families_with_complete_success": ["UNIFIED_AP"],
            "device_families_with_partial_success": ["ROUTER"],
            "device_families_with_complete_failure": [],
            "success_details": [],
            "failure_details": [
              {
                "device_family": "ROUTER",
                "kpi_name": "Invalid KPI",
                "status": "failed",
                "error_info": {
                  "error_type": "kpi_not_found",
                  "error_message": "KPI not found for this device family",
                  "error_code": "KPI_NOT_FOUND"
                }
              }
            ]
          }
        },
      "msg": "YAML config generation failed for module 'assurance_device_health_score_settings_workflow_manager'."
    }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
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


class BrownfieldAssuranceDeviceHealthScoreSettingsPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for assurance device health score settings configured within the Cisco Catalyst Center using the GET APIs.
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
        self.module_name = "assurance_device_health_score_settings_workflow_manager"

        # Initialize class-level variables to track successes and failures
        self.operation_successes = []
        self.operation_failures = []
        self.total_device_families_processed = 0

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False

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
            "global_filters": {"type": "dict", "required": False},
        }

        # Import validate_list_of_dicts function here to avoid circular imports
        from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

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
        Returns the mapping configuration for assurance device health score settings workflow manager.
        Returns:
            dict: A dictionary containing network elements configuration with validation rules.
        """
        return {
            "network_elements": {
                "device_health_score_settings": {
                    "filters": {
                        "device_families": {
                            "type": "list",
                            "required": False,
                            "elements": "str"
                        },
                    },
                    "reverse_mapping_function": self.device_health_score_settings_reverse_mapping_function,
                    "api_function": "get_all_health_score_definitions_for_given_filters",
                    "api_family": "devices",
                    "get_function_name": self.get_device_health_score_settings,
                }
            }
        }

    def device_health_score_settings_reverse_mapping_function(self, requested_filters=None):
        """
        Returns the reverse mapping specification for device health score settings.
        Args:
            requested_filters (dict, optional): Dictionary of specific filters to apply
        Returns:
            dict: A dictionary containing reverse mapping specifications for device health score settings
        """
        self.log("Starting reverse mapping specification generation for device health score settings", "DEBUG")

        return self.get_device_health_score_reverse_mapping_spec()

    def get_kpi_name_reverse_mapping(self):
        """
        Returns mapping from internal API names to user-friendly KPI names.
        This is the reverse of the mapping in assurance_device_health_score_settings_workflow_manager.
        """
        return {
            "linkErrorThreshold": "Link Error",
            "rssiThreshold": "Connectivity RSSI",
            "snrThreshold": "Connectivity SNR",
            "rf_airQuality_2_4GThreshold": "Air Quality 2.4 GHz",
            "rf_airQuality_5GThreshold": "Air Quality 5 GHz",
            "rf_airQuality_6GThreshold": "Air Quality 6 GHz",
            "cpuUtilizationThreshold": "CPU Utilization",
            "rf_interference_2_4GThreshold": "Interference 2.4 GHz",
            "rf_interference_5GThreshold": "Interference 5 GHz",
            "rf_interference_6GThreshold": "Interference 6 GHz",
            "rf_noise_2_4GThreshold": "Noise 2.4 GHz",
            "rf_noise_5GThreshold": "Noise 5 GHz",
            "rf_noise_6GThreshold": "Noise 6 GHz",
            "rf_utilization_2_4GThreshold": "RF Utilization 2.4 GHz",
            "rf_utilization_5GThreshold": "RF Utilization 5 GHz",
            "rf_utilization_6GThreshold": "RF Utilization 6 GHz",
            "freeMbufThreshold": "Free Mbuf",
            "freeTimerThreshold": "Free Timer",
            "packetPool": "Packet Pool",
            "WQEPool": "WQE Pool",
            "aaaServerReachability": "AAA server reachability",
            "bgpBgpSiteThreshold": "BGP Session from Border to Control Plane (BGP)",
            "bgpPubsubSiteThreshold": "BGP Session from Border to Control Plane (PubSub)",
            "bgpPeerInfraVnThreshold": "BGP Session from Border to Peer Node for INFRA VN",
            "bgpPeerThreshold": "BGP Session from Border to Peer Node",
            "bgpTcpThreshold": "BGP Session from Border to Transit Control Plane",
            "bgpEvpnThreshold": "BGP Session to Spine",
            "ctsEnvDataThreshold": "Cisco TrustSec environment data download status",
            "fabricReachability": "Fabric Control Plane Reachability",
            "multicastRPReachability": "Fabric Multicast RP Reachability",
            "fpcLinkScoreThreshold": "Extended Node Connectivity",
            "infraLinkAvailabilityThreshold": "Inter-device Link Availability",
            "defaultRouteThreshold": "Internet Availability",
            "linkDiscardThreshold": "Link Discard",
            "linkUtilizationThreshold": "Link Utilization",
            "lispTransitConnScoreThreshold": "LISP Session from Border to Transit Site Control Plane",
            "lispCpConnScoreThreshold": "LISP Session Status",
            "memoryUtilizationThreshold": "Memory Utilization",
            "peerThreshold": "Peer Status",
            "pubsubTransitSessionScoreThreshold": "Pub-Sub Session from Border to Transit Site Control Plane",
            "pubsubInfraVNSessionScoreThreshold": "Pub-Sub Session Status for INFRA VN",
            "pubsubSessionThreshold": "Pub-Sub Session Status",
            "remoteRouteThreshold": "Remote Internet Availability",
            "vniStatusThreshold": "VNI Status",
            "fwConnThreshold": "Firewall Connection"
        }

    def transform_kpi_name(self, internal_kpi_name):
        """
        Transform internal API KPI name to user-friendly KPI name.
        Args:
            internal_kpi_name (str): Internal API KPI name like 'cpuUtilizationThreshold'
        Returns:
            str: User-friendly KPI name like 'CPU Utilization'
        """
        kpi_mapping = self.get_kpi_name_reverse_mapping()
        user_friendly_name = kpi_mapping.get(internal_kpi_name, internal_kpi_name)
        self.log("Transformed KPI name from '{0}' to '{1}'".format(internal_kpi_name, user_friendly_name), "DEBUG")
        return user_friendly_name

    def get_device_health_score_reverse_mapping_spec(self):
        """
        Constructs reverse mapping specification for device health score settings.
        Compatible with modify_parameters function from brownfield_helper.
        Returns:
            OrderedDict: Reverse mapping specification for device health score settings from API response to user format
        """
        self.log("Generating reverse mapping specification for device health score settings.", "DEBUG")

        return OrderedDict({
            "device_health_score": {
                "type": "list",
                "elements": "dict",
                "source_key": "response",
                "options": OrderedDict({
                    "device_family": {"type": "str", "source_key": "deviceFamily"},
                    "kpi_name": {
                        "type": "str",
                        "source_key": "name",
                        "transform": self.transform_kpi_name
                    },
                    "include_for_overall_health": {"type": "bool", "source_key": "includeForOverallHealth"},
                    "threshold_value": {"type": "float", "source_key": "thresholdValue"},
                    "synchronize_to_issue_threshold": {"type": "bool", "source_key": "synchronizeToIssueThreshold"}
                })
            }
        })

    def reset_operation_tracking(self):
        """
        Resets the operation tracking variables for a new operation.
        """
        self.log("Resetting operation tracking variables for new operation", "DEBUG")
        self.operation_successes = []
        self.operation_failures = []
        self.total_device_families_processed = 0
        self.total_kpis_processed = 0
        self.log("Operation tracking variables reset successfully", "DEBUG")

    def add_success(self, device_family, kpi_name, additional_info=None):
        """
        Adds a successful operation to the tracking list.
        Args:
            device_family (str): Device family name.
            kpi_name (str): KPI name that succeeded.
            additional_info (dict): Additional information about the success.
        """
        self.log("Creating success entry for device family {0}, KPI {1}".format(device_family, kpi_name), "DEBUG")
        success_entry = {
            "device_family": device_family,
            "kpi_name": kpi_name,
            "status": "success"
        }

        if additional_info:
            self.log("Adding additional information to success entry: {0}".format(additional_info), "DEBUG")
            success_entry.update(additional_info)

        self.operation_successes.append(success_entry)
        self.log("Successfully added success entry for device family {0}, KPI {1}. Total successes: {2}".format(
            device_family, kpi_name, len(self.operation_successes)), "DEBUG")

    def add_failure(self, device_family, kpi_name, error_info):
        """
        Adds a failed operation to the tracking list.
        Args:
            device_family (str): Device family name.
            kpi_name (str): KPI name that failed.
            error_info (dict): Error information containing error details.
        """
        self.log("Creating failure entry for device family {0}, KPI {1}".format(device_family, kpi_name), "DEBUG")
        failure_entry = {
            "device_family": device_family,
            "kpi_name": kpi_name,
            "status": "failed",
            "error_info": error_info
        }

        self.operation_failures.append(failure_entry)
        self.log("Successfully added failure entry for device family {0}, KPI {1}: {2}. Total failures: {3}".format(
            device_family, kpi_name, error_info.get("error_message", "Unknown error"), len(self.operation_failures)), "ERROR")

    def get_operation_summary(self):
        """
        Returns a summary of all operations performed.
        Returns:
            dict: Summary containing successes, failures, and statistics.
        """
        self.log("Generating operation summary from {0} successes and {1} failures".format(
            len(self.operation_successes), len(self.operation_failures)), "DEBUG")

        unique_successful_families = set()
        unique_failed_families = set()

        self.log("Processing successful operations to extract unique device family information", "DEBUG")
        for success in self.operation_successes:
            unique_successful_families.add(success["device_family"])

        self.log("Processing failed operations to extract unique device family information", "DEBUG")
        for failure in self.operation_failures:
            unique_failed_families.add(failure["device_family"])

        self.log("Calculating device family categorization based on success and failure patterns", "DEBUG")
        partial_success_families = unique_successful_families.intersection(unique_failed_families)
        self.log("Device families with partial success (both successes and failures): {0}".format(
            len(partial_success_families)), "DEBUG")

        complete_success_families = unique_successful_families - unique_failed_families
        self.log("Device families with complete success (only successes): {0}".format(
            len(complete_success_families)), "DEBUG")

        complete_failure_families = unique_failed_families - unique_successful_families
        self.log("Device families with complete failure (only failures): {0}".format(
            len(complete_failure_families)), "DEBUG")

        summary = {
            "total_device_families_processed": len(unique_successful_families.union(unique_failed_families)),
            "total_kpis_processed": self.total_kpis_processed,
            "total_successful_operations": len(self.operation_successes),
            "total_failed_operations": len(self.operation_failures),
            "device_families_with_complete_success": list(complete_success_families),
            "device_families_with_partial_success": list(partial_success_families),
            "device_families_with_complete_failure": list(complete_failure_families),
            "success_details": self.operation_successes,
            "failure_details": self.operation_failures
        }

        self.log("Operation summary generated successfully with {0} total device families processed".format(
            summary["total_device_families_processed"]), "INFO")

        return summary

    def get_device_health_score_settings(self, network_element, filters):
        """
        Retrieves device health score settings from Cisco Catalyst Center.
        Args:
            network_element (dict): Network element configuration containing API details.
            filters (dict): Filters containing component_specific_filters.
        Returns:
            dict: A dictionary containing device health score settings configurations.
        """
        self.log("Starting device health score settings retrieval process", "INFO")
        self.log("Network element configuration: {0}".format(network_element), "DEBUG")
        self.log("Applied filters: {0}".format(filters), "DEBUG")

        self.log("Resetting operation tracking for new retrieval session", "DEBUG")
        self.reset_operation_tracking()

        # Extract API configuration
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log("API family: {0}, API function: {1}".format(api_family, api_function), "DEBUG")

        # Prepare API parameters
        api_params = {}
        component_specific_filters = filters.get("component_specific_filters", {})

        # Support both global_filters and component_specific_filters structures
        device_families = []

        # Check for nested device_health_score_settings structure
        health_score_filters = component_specific_filters.get("device_health_score_settings", {})
        if health_score_filters.get("device_families"):
            device_families = health_score_filters["device_families"]
            self.log("Found device families in device_health_score_settings: {0}".format(device_families), "DEBUG")

        # Check for components_list - if only components_list is present without device_families
        components_list = component_specific_filters.get("components_list", [])
        if "device_health_score_settings" in components_list:
            if not device_families:
                self.log("components_list contains device_health_score_settings without device families - will retrieve all device families", "DEBUG")
            else:
                self.log("components_list contains device_health_score_settings with device families: {0}".format(device_families), "DEBUG")

        try:
            # Collect all response data from multiple API calls
            all_response_data = []

            # Determine if device families are specified
            has_device_families = bool(device_families)

            # Loop through includeForOverallHealth values
            for include_for_overall_health in [True, False]:
                self.log("Processing includeForOverallHealth: {0}".format(include_for_overall_health), "DEBUG")

                if has_device_families:
                    # If device families are specified, make API calls for each device family
                    for device_family in device_families:
                        self.log("Making API call for device family: {0}, includeForOverallHealth: {1}".format(
                            device_family, include_for_overall_health), "DEBUG")

                        api_params = {
                            "deviceType": device_family,
                            "includeForOverallHealth": include_for_overall_health,
                        }

                        self.log("API parameters being sent: {0}".format(api_params), "DEBUG")
                        response = self.execute_get_request(api_family, api_function, api_params)
                        self.log("API response received for device family {0}: {1}".format(
                            device_family, self.pprint(response)), "DEBUG")

                        if response and response.get("response"):
                            response_data = response.get("response", [])
                            all_response_data.extend(response_data)
                            self.log("Added {0} items from device family {1}, includeForOverallHealth={2}".format(
                                len(response_data), device_family, include_for_overall_health), "DEBUG")
                else:
                    # If no device families specified, make API call without deviceType filter
                    self.log("Making API call without device family filter, includeForOverallHealth: {0}".format(
                        include_for_overall_health), "DEBUG")

                    api_params = {
                        "includeForOverallHealth": include_for_overall_health,
                    }

                    self.log("API parameters being sent: {0}".format(api_params), "DEBUG")
                    response = self.execute_get_request(api_family, api_function, api_params)

                    if response and response.get("response"):
                        response_data = response.get("response", [])
                        all_response_data.extend(response_data)
                        self.log("Added {0} items from API call with includeForOverallHealth={1}".format(
                            len(response_data), include_for_overall_health), "DEBUG")

            self.log("Total response data collected: {0} items".format(len(all_response_data)), "DEBUG")

            # Log first few items for debugging
            if all_response_data and len(all_response_data) > 0:
                self.log("Sample response data item: {0}".format(all_response_data[0] if all_response_data else {}), "DEBUG")

            self.log("Processing {0} health score definitions from API".format(len(all_response_data)), "DEBUG")

            # Update response_data to use collected data
            response_data = all_response_data

            # Since API returns filtered data based on parameters, no additional filtering needed
            self.log("Using API response data directly: {0} health score settings".format(len(response_data)), "DEBUG")

            if response_data:
                # Track statistics
                device_families = set()
                for item in response_data:
                    device_families.add(item.get("deviceFamily"))
                    # Get user-friendly KPI name for tracking
                    kpi_internal_name = item.get("name")
                    kpi_user_name = self.get_kpi_name_reverse_mapping().get(kpi_internal_name, kpi_internal_name)
                    self.add_success(
                        item.get("deviceFamily"),
                        kpi_user_name,
                        {
                            "threshold_value": item.get("thresholdValue"),
                            "include_for_overall_health": item.get("includeForOverallHealth")
                        }
                    )

                self.total_device_families_processed = len(device_families)
                self.total_kpis_processed = len(response_data)

                # Apply reverse mapping
                reverse_mapping_function = network_element.get("reverse_mapping_function")
                reverse_mapping_spec = reverse_mapping_function()

                self.log("Applying reverse mapping to transform API data to user format", "DEBUG")
                transformed_data = self.modify_parameters(
                    reverse_mapping_spec,
                    [{"response": response_data}]
                )

                # Extract the device_health_score list from the transformed data
                device_health_score_list = []
                if transformed_data and len(transformed_data) > 0:
                    device_health_score_list = transformed_data[0].get("device_health_score", [])

                final_result = {
                    "device_health_score_settings": device_health_score_list,
                    "operation_summary": self.get_operation_summary()
                }

                self.log("Device health score settings retrieval completed successfully", "INFO")
                return final_result

            else:
                self.log("No health score settings found from API response", "WARNING")

        except Exception as e:
            error_msg = "Exception occurred while retrieving device health score settings: {0}".format(str(e))
            self.log(error_msg, "ERROR")
            self.add_failure("UNKNOWN", "UNKNOWN", {
                "error_type": "exception",
                "error_message": error_msg,
                "error_code": "API_EXCEPTION_ERROR"
            })

        return {
            "device_health_score_settings": [],
            "operation_summary": self.get_operation_summary()
        }

    def apply_health_score_filters(self, response_data, component_specific_filters):
        """
        Applies component-specific filters to device health score settings data.
        Args:
            response_data (list): Raw response data from API.
            component_specific_filters (dict): Component-specific filters.
        Returns:
            list: Filtered device health score settings data.
        """
        self.log("Starting health score settings filtering process", "DEBUG")
        self.log("Input response_data count: {0}".format(len(response_data) if response_data else 0), "DEBUG")
        self.log("Component specific filters: {0}".format(component_specific_filters), "DEBUG")

        if not response_data:
            self.log("No response data to filter", "DEBUG")
            return []

        filtered_data = response_data[:]
        original_count = len(filtered_data)

        # Support both global_filters and component_specific_filters structures
        device_families = []

        # Check for global_filters structure
        global_filters = component_specific_filters.get("global_filters", {})
        if global_filters.get("device_families"):
            device_families = global_filters["device_families"]
            self.log("Found device families in global_filters: {0}".format(device_families), "DEBUG")

        # Check for nested device_health_score_settings structure
        health_score_filters = component_specific_filters.get("device_health_score_settings", {})
        if not device_families and health_score_filters.get("device_families"):
            device_families = health_score_filters["device_families"]
            self.log("Found device families in device_health_score_settings: {0}".format(device_families), "DEBUG")

        # Check for components_list - if present, get all device families
        components_list = component_specific_filters.get("components_list", [])
        if "device_health_score_settings" in components_list and not device_families:
            self.log("components_list contains device_health_score_settings - no filtering by device family", "DEBUG")

        self.log("Final device families filter: {0}".format(device_families), "DEBUG")
        if device_families:
            self.log("Applying device families filter: {0}".format(device_families), "DEBUG")
            filtered_data = [
                item for item in filtered_data
                if item.get("deviceFamily") in device_families
            ]
            self.log("Device families filter: {0} -> {1} items".format(original_count, len(filtered_data)), "DEBUG")

        # Apply KPI names filter
        kpi_names = health_score_filters.get("kpi_names", component_specific_filters.get("kpi_names", []))
        if kpi_names:
            self.log("Applying KPI names filter: {0}".format(kpi_names), "DEBUG")
            pre_kpi_count = len(filtered_data)
            filtered_data = [
                item for item in filtered_data
                if item.get("kpiName") in kpi_names
            ]
            self.log("KPI names filter: {0} -> {1} items".format(pre_kpi_count, len(filtered_data)), "DEBUG")

        self.log("Health score settings filtering completed - Final count: {0}".format(len(filtered_data)), "INFO")
        return filtered_data

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        Args:
            yaml_config_generator (dict): Contains file_path and component_specific_filters.
        Returns:
            self: The current instance with the operation result and message updated.
        """
        self.log(
            "Initializing YAML configuration generation process with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log("Auto-discovery mode enabled - will process all device health score settings", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        if generate_all:
            # In generate_all_configurations mode, override any provided filters
            self.log("Auto-discovery mode: Overriding any provided filters to retrieve all settings", "INFO")
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

            # Also check for global_filters at the top level
            global_filters = yaml_config_generator.get("global_filters")
            if global_filters and not component_specific_filters:
                component_specific_filters = {"global_filters": global_filters}

            self.log("Component specific filters received: {0}".format(component_specific_filters), "DEBUG")

        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        self.log("Initializing final configuration list and operation summary tracking", "DEBUG")
        final_list = []
        consolidated_operation_summary = {
            "total_device_families_processed": 0,
            "total_kpis_processed": 0,
            "total_successful_operations": 0,
            "total_failed_operations": 0,
            "device_families_with_complete_success": [],
            "device_families_with_partial_success": [],
            "device_families_with_complete_failure": [],
            "success_details": [],
            "failure_details": []
        }

        # Process device health score settings
        component = "device_health_score_settings"
        self.log("Processing component: {0}".format(component), "DEBUG")
        network_element = module_supported_network_elements.get(component)

        if network_element:
            self.log("Preparing component-specific filter configuration", "DEBUG")
            # Pass the component_specific_filters directly to match the expected structure
            component_filters = {
                "component_specific_filters": component_specific_filters
            }

            self.log("Executing component operation function to retrieve details", "DEBUG")
            operation_func = network_element.get("get_function_name")
            details = operation_func(network_element, component_filters)
            self.log(
                "Details retrieved for component {0}: configurations count = {1}".format(
                    component, len(details.get("device_health_score_settings", []))), "DEBUG"
            )

            if details and details.get("device_health_score_settings"):
                self.log("Adding {0} configurations from component {1} to final list".format(
                    len(details["device_health_score_settings"]), component), "DEBUG")
                final_list.extend(details["device_health_score_settings"])

            # Consolidate operation summary
            if details and details.get("operation_summary"):
                summary = details["operation_summary"]
                consolidated_operation_summary.update(summary)

        self.log("Creating final dictionary structure with operation summary", "DEBUG")
        final_dict = OrderedDict()

        # Format the configuration properly according to the required structure
        # Changed to match expected format: config: - device_health_score: [list]
        if final_list:
            final_dict["config"] = [{"device_health_score": final_list}]
        else:
            final_dict["config"] = [{"device_health_score": []}]

        if not final_list:
            self.log("No configurations found to process, setting appropriate result", "WARNING")
            self.msg = {
                "message": "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                    self.module_name
                ),
                "file_path": file_path,
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        self.log("Final dictionary created successfully with {0} configurations".format(len(final_list)), "DEBUG")

        # Determine if operation should be considered failed based on partial or complete failures
        has_partial_failures = len(consolidated_operation_summary["device_families_with_partial_success"]) > 0
        has_complete_failures = len(consolidated_operation_summary["device_families_with_complete_failure"]) > 0
        has_any_failures = consolidated_operation_summary["total_failed_operations"] > 0

        self.log("Evaluating operation status - Partial failures: {0}, Complete failures: {1}, Total failed operations: {2}".format(
            has_partial_failures, has_complete_failures, consolidated_operation_summary["total_failed_operations"]), "DEBUG")

        self.log("Attempting to write final dictionary to YAML file", "DEBUG")
        if self.write_dict_to_yaml(final_dict, file_path):
            self.log("YAML file write operation completed successfully", "INFO")

            # Determine final operation status
            if has_partial_failures or has_complete_failures or has_any_failures:
                self.log("Operation contains failures - setting final status to failed", "WARNING")
                self.msg = {
                    "message": "YAML config generation completed with failures for module '{0}'. Check operation_summary for details.".format(self.module_name),
                    "file_path": file_path,
                    "configurations_generated": len(final_list),
                    "operation_summary": consolidated_operation_summary
                }
                self.set_operation_result("failed", True, self.msg, "ERROR")
            else:
                self.log("Operation completed successfully without failures", "INFO")
                self.msg = {
                    "message": "YAML config generation succeeded for module '{0}'.".format(self.module_name),
                    "file_path": file_path,
                    "configurations_generated": len(final_list),
                    "operation_summary": consolidated_operation_summary
                }
                self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.log("YAML file write operation failed", "ERROR")
            self.msg = {
                "message": "YAML config generation failed for module '{0}' - unable to write to file.".format(self.module_name),
                "file_path": file_path,
                "operation_summary": consolidated_operation_summary
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        self.log("YAML configuration generation process completed", "DEBUG")
        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('gathered').
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        # Set generate_all_configurations after validation
        self.generate_all_configurations = config.get("generate_all_configurations", False)
        self.log("Set generate_all_configurations mode: {0}".format(self.generate_all_configurations), "DEBUG")

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
        self.msg = "Successfully collected all parameters from the playbook for Assurance Device Health Score Settings operations."
        self.status = "success"
        return self

    def validate_params(self, config):
        """
        Validates the parameters provided for the playbook configuration.
        Args:
            config (dict): Configuration dictionary containing playbook parameters.
        """
        self.log("Starting parameter validation for the provided configuration", "DEBUG")
        # Basic validation - can be expanded based on specific requirements
        if not isinstance(config, dict):
            self.log("Configuration must be a dictionary", "ERROR")
            raise ValueError("Configuration must be a dictionary")
        self.log("Parameter validation completed successfully", "DEBUG")

    def generate_filename(self):
        """
        Generates a default filename for the YAML configuration file.
        Returns:
            str: Generated filename with timestamp.
        """
        import datetime
        timestamp = datetime.datetime.now()
        filename = "{0}_playbook_{1}.yml".format(
            self.module_name,
            timestamp.strftime("%d_%b_%Y_%H_%M_%S_%f")[:-3]
        )
        self.log("Generated default filename: {0}".format(filename), "DEBUG")
        return filename

    def generate_playbook_header(self, data_dict):
        """
        Generates header comments for the playbook file.
        Args:
            data_dict (dict): The configuration dictionary to analyze for summary.
        Returns:
            str: Header comments as a string.
        """
        import datetime

        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Calculate summary information
        device_health_score_list = []
        if data_dict.get("config"):
            for config_item in data_dict["config"]:
                if config_item.get("device_health_score"):
                    device_health_score_list = config_item["device_health_score"]
                    break

        total_configurations = len(device_health_score_list)
        device_families = set()
        kpi_names = set()

        for config in device_health_score_list:
            if config.get("device_family"):
                device_families.add(config["device_family"])
            if config.get("kpi_name"):
                kpi_names.add(config["kpi_name"])

        # Get DNAC host information
        dnac_host = 'Unknown'
        if hasattr(self, 'params') and self.params:
            dnac_host = self.params.get('dnac_host', 'Unknown')
        elif hasattr(self, 'dnac_host'):
            dnac_host = self.dnac_host
        elif hasattr(self, 'module') and self.module and hasattr(self.module, 'params'):
            dnac_host = self.module.params.get('dnac_host', 'Unknown')

        # Build header comments
        header_lines = [
            "# " + "=" * 80,
            "# Cisco Catalyst Center - Device Health Score Settings Configuration",
            "# " + "=" * 80,
            "#",
            "# Generated by: Cisco DNA Center Ansible Collection",
            "# Source: Cisco Catalyst Center (CatC)",
            "# DNAC Host: {0}".format(dnac_host),
            "# Generated on: {0}".format(timestamp),
            "#",
            "# Configuration Summary:",
            "#   Total KPI Configurations: {0}".format(total_configurations),
            "#   Device Families: {0}".format(", ".join(sorted(device_families)) if device_families else "None"),
            "#   Unique KPIs: {0}".format(len(kpi_names)),
            "#",
            "# This playbook contains device health score settings extracted from",
            "# Cisco Catalyst Center and can be used with the",
            "# cisco.dnac.assurance_device_health_score_settings_workflow_manager module",
            "# to apply the same configurations to other Catalyst Center instances.",
            "#",
            "# " + "=" * 80,
            ""
        ]

        return "\n".join(header_lines)

    def write_dict_to_yaml(self, data_dict, file_path):
        """
        Writes a dictionary to a YAML file with header comments.
        Args:
            data_dict (dict): Dictionary to write to YAML.
            file_path (str): Path where the YAML file should be saved.
        Returns:
            bool: True if successful, False otherwise.
        """
        self.log("Starting YAML file write operation to: {0}".format(file_path), "DEBUG")
        try:
            with open(file_path, 'w') as yaml_file:
                # Write header comments
                header = self.generate_playbook_header(data_dict)
                yaml_file.write(header)

                # Write YAML content
                if HAS_YAML and OrderedDumper:
                    yaml.dump(data_dict, yaml_file, Dumper=OrderedDumper,
                              default_flow_style=False, indent=2)
                else:
                    yaml.dump(data_dict, yaml_file, default_flow_style=False, indent=2)
            self.log("Successfully wrote YAML configuration to: {0}".format(file_path), "INFO")
            return True
        except Exception as e:
            self.log("Failed to write YAML file: {0}".format(str(e)), "ERROR")
            return False

    def get_diff_gathered(self):
        """
        Executes the merge operations for device health score settings configurations.
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

    # Initialize the BrownfieldAssuranceDeviceHealthScoreSettingsPlaybookGenerator object with the module
    ccc_brownfield_assurance_device_health_score_settings_playbook_generator = BrownfieldAssuranceDeviceHealthScoreSettingsPlaybookGenerator(module)

    if (
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.compare_dnac_versions(
            ccc_brownfield_assurance_device_health_score_settings_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for ASSURANCE_DEVICE_HEALTH_SCORE_SETTINGS Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_brownfield_assurance_device_health_score_settings_playbook_generator.get_ccc_version()
            )
        )
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.set_operation_result(
            "failed", False, ccc_brownfield_assurance_device_health_score_settings_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_brownfield_assurance_device_health_score_settings_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_brownfield_assurance_device_health_score_settings_playbook_generator.supported_states:
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.status = "invalid"
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_brownfield_assurance_device_health_score_settings_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_brownfield_assurance_device_health_score_settings_playbook_generator.validated_config:
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.reset_values()
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_brownfield_assurance_device_health_score_settings_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_brownfield_assurance_device_health_score_settings_playbook_generator.result)


if __name__ == "__main__":
    main()

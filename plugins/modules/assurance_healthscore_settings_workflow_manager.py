#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform update healthscore KPI's in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Megha Kandari, Madhan Sankaranarayanan']

DOCUMENTATION = r"""
---
module: assurance_healthscore_settings_workflow_manager
short_description: Resource module for managing assurance healthscore settings in Cisco Catalyst Center.
description:
- Manages assurance healthscore settings in Cisco DNA Center.
- It supports updating configurations for healthscore settings functionalities.
- This module interacts with Cisco DNA Center's Assurance settings to configure thresholds, rules, KPIs, and more for health score monitoring.
version_added: '6.6.0'
extends_documentation_fragment:
 - cisco.dnac.workflow_manager_params
author: Megha Kandari (@kandarimegha)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: >
      Set to `True` to enable configuration verification on Cisco DNA Center after applying the playbook config.
      This will ensure that the system validates the configuration state after the change is applied.
    type: bool
    default: False
  state:
    description: >
      Specifies the desired state for the configuration. If `merged`, the module will update the configuration modifying existing ones.
    type: str
    choices: [merged, deleted]
    default: merged
  config:
    description: >
      A list of settings and parameters for managing network issues in Cisco DNA Center,
      including synchronization with health thresholds, priority, KPI enablement, and threshold values.
    type: list
    elements: dict
    required: true
    suboptions:
      device_healthscore:
        description: >
          Configures the health score settings for network devices. Defines thresholds for KPIs like CPU utilization, memory, etc.
        type: dict
        suboptions:
          name:
            description: >
              The name of the Key Performance Indicator (KPI) to be monitored (e.g., cpu_utilization_threshold).
            type: str
          device_family:
            description: >
              Specifies the device family to which the health score applies (e.g., switches, routers, hubs).
            type: str
          include_for_overall_health:
            description: >
              Boolean value indicating whether this KPI should be included in the overall health score calculation.
            type: bool
          threshold_value:
            description: >
              The threshold value that, when exceeded, will affect the health score.
            type: int
          synchronize_to_issue_threshold:
            description: >
              Boolean value indicating whether the threshold should synchronize with issue resolution thresholds.
            type: bool
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
- SDK Method used are
    devices.AssuranceSettings.get_all_healthscore_definitions_for_given_filters,
    devices.AssuranceSettings.update_health_score_definitions
- Paths used are
    post /dna/intent/api/v1/healthScoreDefinitions/${id},
    post /dna/intent/api/v1/healthScoreDefinitions/bulkUpdate
"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  connection: local
  tasks:
    - name: Update healthscore and threshold settings
      cisco.dnac.assurance_healthscore_settings_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: debug
        dnac_log_append: true
        state: merged
        config_verify: true
        config:
        - device_healthscore:
          - name: cpu_utilization_threshold #required field
            device_family: switch and hubs #required field
            include_for_overall_health: true
            threshold_value: 90
            synchronize_to_issue_threshold: false
     """

RETURN = r"""
#Case 1: Successful updation of healthscore

response_1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
          "id": "string",
          "name": "string",
          "displayName": "string",
          "deviceFamily": "string",
          "description": "string",
          "includeForOverallHealth": "boolean",
          "definitionStatus": "string",
          "thresholdValue": "number",
          "synchronizeToIssueThreshold": "boolean",
          "lastModified": "string"
      },
      "version": "string"
    }

"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)


class Healthscore(DnacBase):
    """Class containing member attributes for Assurance setting workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.result["response"] = [
            {"device_healthscore_settings": {"response": {}, "msg": {}}},
        ]
        self.create_issue, self.update_issue, self.no_update_issue = [], [], []

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.

        Returns:
            The method updates these attributes of the instance:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation ('success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        """
        temp_spec = {
            'device_healthscore': {
                'type': 'list',
                'elements': 'dict',
                'name': {'type': 'str', 'required': True},
                'device_family': {'type': 'str', 'required': True},
                'include_for_overall_health': {'type': 'bool', 'required': True},
                'threshold_value': {'type': 'int', 'required': False},
                'synchronize_to_issue_threshold': {'type': 'bool', 'required': False}
            }
        }

        if not self.config:
            self.msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "The playbook contains invalid parameters: {0}".format(
                invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(
            str(valid_temp))
        self.log(self.msg, "INFO")

        return self

    def input_data_validation(self, config):
        """
        Additional validation to check if the provided input assurance data is correct
        and as per the UI Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            config (list or dict): Input data containing assurance details.

        Returns:
            object: Returns the current instance with validation results.

        Description:
            Validates the given assurance data by iterating through the nested structure
            and ensuring the KPIs and parameters comply with defined rules.
        """
        errormsg = []
        device_family_to_kpi = {
            "ROUTER": {
                "include_for_overall_health": [
                    "Fabric Multicast RP Reachability",
                    "Inter-device Link Availability",
                    "Internet Availability",
                    "LISP Session from Border to Transit Site Control Plane",
                    "LISP Session Status",
                    "Peer Status",
                    "BGP Session from Border to Control Plane (BGP)",
                    "BGP Session from Border to Control Plane (PubSub)",
                    "BGP Session from Border to Peer Node for INFRA VN",
                    "BGP Session from Border to Peer Node",
                    "BGP Session from Border to Transit Control Plane",
                    "BGP Session to Spine",
                    "Cisco TrustSec environment data download status",
                    "Extended Node Connectivity",
                    "Fabric Control Plane Reachability",
                    "Pub-Sub Session from Border to Transit Site Control Plane",
                    "Pub-Sub Session Status for INFRA VN",
                    "Pub-Sub Session Status",
                    "Remote Internet Availability",
                    "VNI Status",
                ],
                "include_Threshold_and_sync": [
                    "Link Discard",
                    "Link Error",
                    "Link Utilization",
                    "Memory Utilization",
                    "CPU Utilization",
                ],
                "include_Threshold": []
            },
            "SWITCH_AND_HUB": {
                "include_for_overall_health": [
                    "AAA server reachability",
                    "BGP Session from Border to Control Plane (BGP)",
                    "BGP Session from Border to Control Plane (PubSub)",
                    "BGP Session from Border to Peer Node for INFRA VN",
                    "BGP Session from Border to Peer Node",
                    "BGP Session from Border to Transit Control Plane",
                    "BGP Session to Spine",
                    "Cisco TrustSec environment data download status",
                    "Extended Node Connectivity",
                    "Fabric Multicast RP Reachability",
                    "Inter-device Link Availability",
                    "Internet Availability",
                    "LISP Session from Border to Transit Site Control Plane",
                    "LISP Session Status",
                    "Peer Status",
                    "Pub-Sub Session from Border to Transit Site Control Plane",
                    "Pub-Sub Session Status for INFRA VN",
                    "Pub-Sub Session Status",
                    "Remote Internet Availability",
                    "VNI Status",
                ],
                "include_Threshold_and_sync": [
                    "CPU Utilization",
                    "Link Discard",
                    "Link Error",
                    "Memory Utilization",
                ],
                "include_Threshold": []
            },
            "WIRELESS_CONTROLLER": {
                "include_for_overall_health": [
                    "Fabric Control Plane Reachability",
                    "LISP Session Status",
                    "Packet Pool",
                    "WQE Pool",
                ],
                "include_Threshold_and_sync": [
                    "Memory Utilization",
                ],
                "include_Threshold": [
                    "Free Mbuf",
                    "Free Timer",
                    "Link Error",
                ],
            },
            "UNIFIED_AP": {
                "include_for_overall_health": [],
                "include_Threshold_and_sync": [
                    "CPU Utilization",
                    "Interference 2.4 GHz",
                    "Interference 5 GHz",
                    "Interference 6 GHz",
                    "Memory Utilization",
                    "Noise 2.4 GHz",
                    "Noise 5 GHz",
                    "Noise 6 GHz",
                    "RF Utilization 2.4 GHz",
                    "RF Utilization 5 GHz",
                    "RF Utilization 6 GHz",
                ],
                "include_Threshold": [
                    "Air Quality 2.4 GHz",
                    "Air Quality 5 GHz",
                    "Air Quality 6 GHz",
                    "Link Error",
                ],
            },
            "WIRELESS_CLIENT": {
                "include_for_overall_health": [],
                "include_Threshold_and_sync": [
                    "Connectivity RSSI",
                ],
                "include_Threshold": [
                    "Connectivity SNR",
                ],
            },
            "WIRED_CLIENT": {
                "include_for_overall_health": [],
                "include_Threshold_and_sync": [],
                "include_Threshold": [
                    "Link Error",
                ],
            },
        }

        normalized_healthscores = []
        if isinstance(config, dict) and "device_healthscore" in config:
            normalized_healthscores.extend(config["device_healthscore"])
        elif isinstance(config, list):
            for item in config:
                if "device_healthscore" in item:
                    normalized_healthscores.extend(item["device_healthscore"])
        else:
            self.msg = "Invalid configuration format provided. Ensure 'device_healthscore' is present."
            self.log(self.msg, "ERROR")
            return self

        for entry in normalized_healthscores:
            device_family = entry.get("device_family")
            kpi_name = entry.get("kpi_name")
            include_for_overall_health = entry.get("include_for_overall_health", False)
            threshold_value = entry.get("threshold_value")
            synchronize_to_issue_threshold = entry.get("synchronize_to_issue_threshold", False)

            if not device_family or device_family not in device_family_to_kpi:
                errormsg.append("Device_Family: Invalid or missing Device Family '{}'.".format(device_family))
                continue

            valid_kpis = device_family_to_kpi[device_family]
            if not kpi_name:
                errormsg.append("kpi_name: KPI Name is missing.")
            else:
                if (kpi_name not in valid_kpis["include_for_overall_health"] and
                        kpi_name not in valid_kpis["include_Threshold_and_sync"] and kpi_name not in valid_kpis["include_Threshold"]):
                    errormsg.append("kpi_name: Invalid KPI '{}' for Device Family '{}'.".format(kpi_name, device_family))
                else:
                    category = (
                        "include_for_overall_health" if kpi_name in valid_kpis["include_for_overall_health"] else
                        "include_Threshold_and_sync"
                    )

                    if category == "include_for_overall_health" and (threshold_value or synchronize_to_issue_threshold):
                        errormsg.append(
                            "'threshold_value' or 'synchronize_to_issue_threshold not applicable for KPI '{}''.".format(kpi_name)
                        )
                    if category == "include_Threshold" and synchronize_to_issue_threshold:
                        errormsg.append(
                            "'synchronize_to_issue_threshold' is not applicable for KPI '{}' under 'include_Threshold_and_sync'.".format(kpi_name)
                        )
                    self.log("KPI '{}' belongs to category '{}' for Device Family '{}'".format(kpi_name, category, device_family), "INFO")

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: {}".format(errormsg)
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.msg = "Successfully validated config params: {}".format(config)
        self.log(self.msg, "INFO")
        return self

    def healthscore_obj_params(self, get_object):
        """
        Get the required comparison obj_params value

        Parameters:
            get_object (str) - identifier for the required obj_params

        Returns:
            obj_params (list) - obj_params value for comparison.
        """

        try:
            if get_object == "device_healthscore_settings":
                obj_params = [
                    ("name", "name"),
                    ("device_family", "device_family"),
                    ("include_for_overall_health", "include_for_overall_health"),
                    ("threshold_value", "threshold_value"),
                    ("synchronize_to_issue_threshold", "synchronize_to_issue_threshold"),
                ]
            else:
                raise ValueError("Received an unexpected value for 'get_object': {0}"
                                 .format(get_object))
        except Exception as msg:
            self.log("Received exception: {0}".format(msg), "CRITICAL")

        return obj_params

    def get_want(self, config):
        """
        Retrieve and store assurance healthscore details from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.
        Raises:
            AnsibleFailJson: If an incorrect import type is specified.

        """

        want = {}
        want["device_healthscore"] = config.get("device_healthscore")
        if "kpi_name" in want["device_healthscore"]:
            want["name"] = want.pop("kpi_name")

        kpi_name = {
            "Link Error": 'linkErrorThreshold',  # WIRED_CLIENT and # UNIFIED_AP and # WIRELESS_CLIENT
            "Connectivity RSSI": 'rssiThreshold',  # WIRELESS_CLIENT
            "Connectivity SNR": 'snrThreshold',  # WIRELESS_CLIENT
            "Air Quality 2.4 GHz": 'rf_airQuality_2_4GThreshold',  # UNIFIED_AP
            "Air Quality 5 GHz": 'rf_airQuality_5GThreshold',  # UNIFIED_AP
            "Air Quality 6 GHz": 'rf_airQuality_6GThreshold',  # UNIFIED_AP
            "CPU Utilization": 'cpuUtilizationThreshold',  # SWITCH_AND_HUB and # ROUTER and # UNIFIED_AP and # WIRELESS_CONTROLLER
            "Interference 2.4 GHz": 'rf_interference_2_4GThreshold',  # UNIFIED_AP
            "Interference 5 GHz": 'rf_interference_5GThreshold',  # UNIFIED_AP
            "Interference 6 GHz": 'rf_interference_6GThreshold',  # UNIFIED_AP
            "Noise 2.4 GHz": 'rf_noise_2_4GThreshold',  # UNIFIED_AP
            "Noise 5 GHz": 'rf_noise_5GThreshold',  # UNIFIED_AP
            "Noise 6 GHz": 'rf_noise_6GThreshold',  # UNIFIED_AP
            "RF Utilization 2.4 GHz": 'rf_utilization_2_4GThreshold',  # UNIFIED_AP
            "RF Utilization 5 GHz": 'rf_utilization_5GThreshold',  # UNIFIED_AP
            "RF Utilization 6 GHz": 'rf_utilization_6GThreshold',  # UNIFIED_AP
            "Free Mbuf": 'freeMbufThreshold',  # WIRELESS_CONTROLLER
            "Free Timer": 'freeTimerThreshold',  # WIRELESS_CONTROLLER
            "Packet Pool": 'packetPool',  # WIRELESS_CONTROLLER
            "WQE Pool": 'WQEPool',  # WIRELESS_CONTROLLER
            "AAA server reachability": 'aaaServerReachability',  # SWITCH_AND_HUB
            "BGP Session from Border to Control Plane (BGP)": 'bgpBgpSiteThreshold',  # SWITCH_AND_HUB and # ROUTER
            "BGP Session from Border to Control Plane (PubSub)": 'bgpPubsubSiteThreshold',  # SWITCH_AND_HUB and # ROUTER
            "BGP Session from Border to Peer Node for INFRA VN": 'bgpPeerInfraVnThreshold',  # SWITCH_AND_HUB and # ROUTER
            "BGP Session from Border to Peer Node": 'bgpPeerThreshold',  # SWITCH_AND_HUB and # ROUTER
            "BGP Session from Border to Transit Control Plane": 'bgpTcpThreshold',  # SWITCH_AND_HUB and # ROUTER
            "BGP Session to Spine": 'bgpEvpnThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Cisco TrustSec environment data download status": 'ctsEnvDataThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Fabric Control Plane Reachability": 'fabricReachability',  # SWITCH_AND_HUB and # ROUTER and # WIRELESS_CONTROLLER
            "Fabric Multicast RP Reachability": 'multicastRPReachability',  # SWITCH_AND_HUB and # ROUTER
            "Extended Node Connectivity": 'fpcLinkScoreThreshold',  # ROUTER and # WIRELESS_CONTROLLER
            "Inter-device Link Availability": 'infraLinkAvailabilityThreshold',  # SWITCH_AND_HUB
            "Internet Availability": 'defaultRouteThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Link Discard": 'linkDiscardThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Link Utilization": 'linkUtilizationThreshold',  # SWITCH_AND_HUB and # ROUTER
            "LISP Session from Border to Transit Site Control Plane": 'lispTransitConnScoreThreshold',  # SWITCH_AND_HUB and # ROUTER
            "LISP Session Status": 'lispCpConnScoreThreshold',  # SWITCH_AND_HUB and # ROUTER and # WIRELESS_CONTROLLER
            "Memory Utilization": 'memoryUtilizationThreshold',  # SWITCH_AND_HUB and # ROUTER and # WIRELESS_CONTROLLER and # UNIFIED_AP
            "Peer Status": 'peerThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Pub-Sub Session from Border to Transit Site Control Plane": 'pubsubTransitSessionScoreThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Pub-Sub Session Status for INFRA VN": 'pubsubInfraVNSessionScoreThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Pub-Sub Session Status": 'pubsubSessionThreshold',  # SWITCH_AND_HUB and # ROUTER
            "Remote Internet Availability": 'remoteRouteThreshold',  # SWITCH_AND_HUB and # ROUTER
            "VNI Status": 'vniStatusThreshold',  # SWITCH_AND_HUB and # ROUTER
        }

        for healthscore in want["device_healthscore"]:
            name = healthscore["kpi_name"]
            healthscore["kpi_name"] = kpi_name[name]

            # Check if kpi_name is "Connectivity RSSI" and device_family is "WIRELESS_CLIENT"
            if name == "Connectivity RSSI" and healthscore.get("device_family") == "WIRELESS_CLIENT":
                threshold_value = healthscore.get("threshold_value")
                if not (-128 <= threshold_value <= 0):
                    self.msg = "Threshold value for Connectivity RSSI should be between -128 and 0 dBm."
                    self.log("Received exception: {0}".format(self.msg), "CRITICAL")
                    self.status = "failed"
                    return self

            # Check if kpi_name is "Connectivity SNR" and device_family is "WIRELESS_CLIENT"
            if name == "Connectivity SNR" and healthscore.get("device_family") == "WIRELESS_CLIENT":
                threshold_value = healthscore.get("threshold_value")
                if not (1 <= threshold_value <= 40):
                    self.msg = "Threshold value for Connectivity SNR should be between 1 and 40 dBm."
                    self.log("Received exception: {0}".format(self.msg), "CRITICAL")
                    self.status = "failed"
                    return self

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        return self

    def get_have(self, config):
        """
        Get the current assurance healthscore and associated information from the Cisco Catalyst Center
        based on the provided playbook details.
        """
        device_healthscore_details = config.get("device_healthscore")
        self.log(device_healthscore_details)

        if not device_healthscore_details:
            self.msg = "No device_healthscore details provided in the configuration."
            self.status = "failed"
            return self

        have = []

        for healthscore_details in device_healthscore_details:
            if "kpi_name" in healthscore_details:
                healthscore_details["name"] = healthscore_details.pop("kpi_name")
            device_family = healthscore_details.get("device_family")
            if not device_family:
                self.msg = "Missing required parameter 'device_family' in device_healthscore settings."
                self.status = "failed"
                return self
            self.log(device_healthscore_details)
            kpi_details = self.get_kpi_details(device_family, healthscore_details)
            self.log(kpi_details)

            if not kpi_details:
                self.msg = "No KPI details found for device family '{0}'".format(device_family)
                self.status = "failed"
                return self

            have.append(kpi_details)

        key_replacements = {
            'deviceFamily': 'device_family',
            'includeForOverallHealth': 'include_for_overall_health',
            'thresholdValue': 'threshold_value',
            'synchronizeToIssueThreshold': 'synchronize_to_issue_threshold'
        }

        for item in have:
            for old_key, new_key in key_replacements.items():
                if old_key in item:
                    item[new_key] = item.pop(old_key)

        self.have = have

        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.msg = "Successfully retrieved the details from the system."
        self.status = "success"
        return self

    def get_kpi_details(self, device_family, healthscore_details):
        """
        Retrieve the KPI name based on the device family by calling the 'Get all health score definitions for given filters' API.
        """
        self.log("Retrieving KPI for device family '{0}'".format(device_family))

        total_response = []
        try:
            for include_for_overall_health in [True, False]:
                response = self.dnac._exec(
                    family="devices",
                    function="get_all_health_score_definitions_for_given_filters",
                    params={"deviceType": device_family, 'includeForOverallHealth': include_for_overall_health}
                )
                if isinstance(response.get("response"), list):
                    total_response.extend(response.get("response"))
            self.log(total_response)
        except Exception as msg:
            self.msg = "Exception occurred while getting KPI details: {0}".format(msg)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return None

        if not isinstance(response, dict):
            self.msg = "Failed to retrieve KPI details - Response is not a dictionary"
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return None

        kpi_details = total_response

        if not kpi_details:
            self.msg = "No KPI details found for device family '{0}'".format(device_family)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return None

        for kpi in kpi_details:
            if kpi.get("deviceFamily") == device_family and kpi.get("name") == healthscore_details.get("name"):
                self.log("KPI details for device family '{0}' and KPI '{1}': {2}".format(device_family, healthscore_details.get("name"), kpi), "INFO")
                return kpi

        self.msg = "No KPI found for device family '{0}' and KPI name '{1}'".format(device_family, kpi_details)
        self.log(self.msg, "ERROR")
        self.status = "failed"
        return None

    def get_diff_merged(self, config):
        """
        Update Assurance healthscore configurations in Cisco Catalyst Center based on the playbook details

        Parameters:
            config (list of dict) - Playbook details containing
            Assurance healthscore information.

        Returns:
            self - The current object with Assurance Issue information.
        """
        device_healthscore_details = config.get("device_healthscore")

        if device_healthscore_details is not None:
            self.update_healthscore_settings(device_healthscore_details).check_return_status()

        return self

    def update_healthscore_settings(self, device_healthscore_details):
        """
    Update the device healthscore settings in Cisco Catalyst Center.

    This method compares the current healthscore settings (`self.have`) with the desired healthscore settings (`device_healthscore_details`)
    from the playbook configuration. If there are any differences, it updates the healthscore settings in Cisco DNAC. It also checks if
    an update is needed for each setting, and if not, it logs that no update is required for that specific healthscore setting.

    Parameters:
        device_healthscore_details (list of dict): List of dictionaries containing the healthscore settings that need to be updated.
            Each dictionary must include the following keys:
            - "name" (str): The name of the healthscore setting.
            - "include_for_overall_health" (bool): Indicates if the healthscore is included for overall health.
            - "threshold_value" (int): The threshold value for the healthscore.
            - "synchronize_to_issue_threshold" (bool): Indicates if the healthscore should be synchronized to issue threshold.

    Returns:
        self: The current instance of the class with updated healthscore settings. If any setting fails to update, the operation will
              be marked as "failed", and the method will return early.
        """

        updated_healthscore_settings = []
        result_healthscore_settings = self.result.get("response")[0].get("device_healthscore_settings")

        for healthscore_setting in device_healthscore_details:
            name = healthscore_setting.get("name")
            if name is None:
                self.msg = "Missing required parameter 'name' in device_healthscore_details"
                self.status = "failed"
                return self

            healthscore_obj_params = self.healthscore_obj_params("device_healthscore_settings")

            for item in self.have:
                if healthscore_setting.get("name") == item.get("name") and healthscore_setting.get("device_family") == item.get("device_family"):
                    healthscore_params = {}
                    if not self.requires_update(item, healthscore_setting, healthscore_obj_params):
                        self.log(
                            "Healthscore setting '{0}' doesn't require an update".format(name), "INFO")
                        result_healthscore_settings.get("msg").update(
                            {name: "Healthscore setting doesn't require an update"})
                    else:
                        healthscore_params = {
                            "id": item.get("id"),
                            "payload": {
                                "includeForOverallHealth": healthscore_setting.get("include_for_overall_health"),
                                "thresholdValue": healthscore_setting.get("threshold_value"),
                                "synchronizeToIssueThreshold": healthscore_setting.get("synchronize_to_issue_threshold"),
                            }
                        }

                        self.log("Preparing update for healthscore settings '{0}' with params: {1}".format(name, healthscore_params), "DEBUG")

                        try:
                            response = self.dnac._exec(
                                family="devices",
                                function="update_health_score_definition_for_the_given_id",
                                op_modifies=True,
                                params=healthscore_params,
                            )

                            if response.get("response"):
                                response_data = response.get("response")
                                self.log("Successfully updated healthscore settings '{0}' with details: {1}".format(name, response_data), "INFO")
                                updated_healthscore_settings.append(response_data)
                            else:
                                self.log("Failed to update system issue '{0}'".format(name), "ERROR")
                        except Exception as e:
                            self.msg = "Exception occurred while updating the healthscore settings '{0}':'{1}'".format(str(name), str(e))
                            self.log(self.msg, "ERROR")
                            self.status = "failed"
                            return self

                        result_healthscore_settings.get("response").update(
                            {"device_healthscore_settings": updated_healthscore_settings})
                        result_healthscore_settings.get("msg").update(
                            {response_data.get("name"): "Healthscore settings Updated Successfully"})
                        self.msg = "Successfully updated Healthscore setiings."
                        self.result['changed'] = True

        self.status = "success"
        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing Assurance healthscore setting.

        Returns:
            self - The current object with Assurance healthscore information.
        """

        self.all_device_healthscore_details = {}
        self.get_have(config)
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Requested State (want): {0}".format(self.want.get("device_healthscore")), "INFO")

        if config.get("device_healthscore") is not None:
            device_healthscore_index = 0
            self.log("Desired State of assurance healthscore issue settings (want): {0}"
                     .format(self.want.get("device_healthscore")), "DEBUG")
            self.log("Current State of assurance healthscore issue settings (have): {0}"
                     .format(self.have), "DEBUG")

            for item in self.want.get("device_healthscore"):
                device_healthscore_details = self.have[device_healthscore_index]
                self.log(device_healthscore_details)
                healthscore_obj_params = self.healthscore_obj_params("device_healthscore_settings")

                if self.requires_update(device_healthscore_details, item, healthscore_obj_params):
                    self.msg = "Assurance healthscore Config is not applied to the Cisco Catalyst Center"
                    self.status = "failed"
                    return self

                device_healthscore_index += 1

                self.log("Successfully validated Assurance healthscore setting(s).", "INFO")
                self.result.get("response")[0].get(
                    "device_healthscore_settings").update({"Validation": "Success"})

        self.msg = "Successfully validated the Assurance user defined issue."
        self.status = "success"
        return self


def main():
    """main entry point for module execution"""
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": '443'},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": 'True'},
        "dnac_version": {"type": 'str', "default": '2.2.3.3'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": False},
        "dnac_api_task_timeout": {"type": 'int', "default": 1200},
        "dnac_task_poll_interval": {"type": 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    ccc_assurance = Healthscore(module)
    state = ccc_assurance.params.get("state")

    if state not in ccc_assurance.supported_states:
        ccc_assurance.status = "invalid"
        ccc_assurance.msg = "State {0} is invalid".format(state)
        ccc_assurance.check_return_status()

    if ccc_assurance.compare_dnac_versions(ccc_assurance.get_ccc_version(), "2.3.7.9") < 0:
        ccc_assurance.msg = (
            "The specified version '{0}' does not support the assurance healthscore features. Supported versions start from '2.3.7.9' onwards. "
            .format(ccc_assurance.get_ccc_version())
        )
        ccc_assurance.status = "failed"
        ccc_assurance.check_return_status()

    ccc_assurance.validate_input().check_return_status()
    config_verify = ccc_assurance.params.get("config_verify")

    for config in ccc_assurance.validated_config:
        ccc_assurance.reset_values()
        ccc_assurance.input_data_validation(config).check_return_status()
        ccc_assurance.get_want(config).check_return_status()
        ccc_assurance.get_have(config).check_return_status()
        ccc_assurance.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_assurance.verify_diff_state_apply[state](config).check_return_status()

        module.exit_json(**ccc_assurance.result)


if __name__ == "__main__":
    main()

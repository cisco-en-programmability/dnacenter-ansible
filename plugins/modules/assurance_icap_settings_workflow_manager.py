#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module to perform operations on Assurance ICAP (Intelligent Capture) settings in Cisco Catalyst Center.

ICAP allows network administrators to collect and analyze packet captures from network devices to troubleshoot
connectivity and performance issues. This module enables automation of ICAP configurations, making it easier
to manage assurance settings programmatically.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Megha Kandari, Madhan Sankaranarayanan']

DOCUMENTATION = r"""
---
module: assurance_icap_settings_workflow_manager
short_description: Configure and manage ICAP (Intelligent Capture) settings in Cisco Catalyst Center for network assurance.
description:
  - Automates the configuration and management of Intelligent Capture (ICAP) settings in Cisco Catalyst Center.
  - ICAP enables real-time packet capture and analysis for troubleshooting client and network device connectivity issues.
  - Supports capturing traffic based on parameters such as capture type, client MAC, AP, WLC, slot, OTA band, and channel.
  - Facilitates automated deployment and validation of ICAP configurations.
version_added: '6.31.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Megha Kandari (@kandarimegha)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
   description: Set to 'true' to verify the ICAP configuration on Cisco Catalyst Center after deployment.
   type: bool
   default: true
  state:
    description:
      - The state of Cisco Catalyst Center after module completion.
    type: str
    choices: ["merged"]
    default: merged
  config:
    description:
      - List of parameters required to configure, create, and deploy ICAP settings in Cisco Catalyst Center.
    type: list
    elements: dict
    required: true
    suboptions:
      assurance_icap_settings:
        description:
          - Defines ICAP settings for capturing client and network device information.
          - Used for onboarding, monitoring, and troubleshooting network connectivity issues.
        type: list
        elements: dict
        suboptions:
          capture_type:
            description: The type of Intelligent Capture to be performed (e.g., onboarding).
            type: str
            choices:
            - FULL  # Captures complete network traffic for deep analysis.
            - ONBOARDING  # Captures packets related to client onboarding processes.
            - OTA  # Captures over-the-air (OTA) wireless traffic.
            - RFSTATS  # Captures RF statistics to analyze signal and interference levels.
            - ANOMALY  # Captures specific anomalies detected in the network.
          duration_in_mins:
            description: The duration of the Intelligent Capture session in minutes.
            type: int
          preview_description:
            description: A short summary or metadata about the Intelligent Capture session,
              providing details such as purpose, expected outcomes, or session context.
            type: str
          client_mac:
            description: The MAC address of the client device for which the capture is being performed.
            type: str
          wlc_name:
            description: The name of the Wireless LAN Controller (WLC) involved in the Intelligent Capture.
            type: str
          ap_name:
            description: The name of the Access Point (AP) for the capture.
            type: str
          slot:
            description: List of slot numbers for the capture session.
            type: list
            elements: int
          ota_band:
            description:
              - Specifies the wireless frequency band for the ICAP capture.
              - Ensure the selected band is valid for the region and device capabilities.
            type: str
            choices:
              - 2.4GHz  # Supports legacy devices, may have interference.
              - 5GHz    # Faster speeds, DFS (Dynamic Frequency Selection) may apply for some channels.
              - 6GHz    # Wi-Fi 6E and Wi-Fi 7 only, check regional availability.
          ota_channel:
            description:
                - Wireless channel used for the ICAP capture (For example, 36, 40).
                - Available channels depend on the selected `ota_band` and regulatory restrictions.
            type: int
          ota_channel_width:
            description:
                - Specifies the channel width in MHz for the ICAP capture (For example, 20, 40).
                - Ensure compatibility with the selected `ota_band` and regulatory requirements.
            type: int

      assurance_icap_download:
        description:
            - Defines settings for downloading Intelligent Capture (ICAP) data.
            - Used to configure the parameters for capturing client data during a specific timeframe.
        type: dict
        suboptions:
          capture_type:
            description: The type of ICAP session to be executed.
            type: str
            choices:
                - FULL # Captures complete network traffic for deep analysis.
                - ONBOARDING  # Captures packets related to client onboarding processes.
                - OTA # Captures over-the-air (OTA) wireless traffic.
                - RFSTATS  # Captures RF statistics to analyze signal and interference levels.
                - ANOMALY # Captures specific anomalies detected in the network.
          duration_in_mins:
            description: The duration of the ICAP session in minutes.
            type: int
            required: false
          preview_description:
            description: A brief summary or metadata about the ICAP session, such as purpose, goals, or context.
            type: str
            required: false
          client_mac:
            description: The MAC address of the client device for which the capture is being performed.
            type: str
            required: true
          ap_mac:
            description: The Ap mac address of the AP for which the capture will be performed through.
            type: str
            required: true
          start_time:
            description: "The start date and time of the ICAP session (format: 'YYYY-MM-DD HH:MM:SS')."
            type: str
            required: false
          end_time:
            description: "The end date and time of the ICAP session (format: 'YYYY-MM-DD HH:MM:SS')."
            type: str
            required: false
          timezone:
            description: The timezone in which the ICAP session times are specified (e.g., Europe/Jersey).
            type: str
            required: false
          file_path:
            description: The location where the captured data will be saved or stored on the file system.
            type: str
            required: true

requirements:
  - dnacentersdk >=  2.8.6
  - python >= 3.9
notes:
  - SDK Method used are
    sensors.AssuranceSettings.get_device_deployment_status,
    sensors.AssuranceSettings.creates_an_icap_configuration_intent_for_preview_approve,
    sensors.AssuranceSettings.discards_the_icap_configuration_intent_by_activity_id
    sensors.AssuranceSettings.deploys_the_i_cap_configuration_intent_by_activity_id_v1
    sensors.AssuranceSettings.lists_i_cap_packet_capture_files_matching_specified_criteria
    sensors.AssuranceSettings.downloads_a_specific_i_cap_packet_capture_file

  - Paths used are
    GET /dna/intent/api/v1/icapSettings/deviceDeployments
    POST /dna/intent/api/icapSettings/configurationModels
    DELETE /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}
    POST /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/deploy
    GET /dna/data/api/v1/icap/captureFiles
    GET /dna/data/api/v1/icap/captureFiles/${id}/download
"""

EXAMPLES = r"""
---
  - hosts: dnac_servers
    vars_files:
      - credentials.yml
    gather_facts: no
    connection: local
    tasks:
      - name: Configure icap on Cisco Catalyst Center
        cisco.dnac.assurance_icap_settings_workflow_manager:
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
            - assurance_icap_settings:
              - capture_type: ONBOARDING
                preview_description: "ICAP onboarding capture"
                duration_in_mins: 30
                client_mac: 50:91:E3:47:AC:9E  #required field
                wlc_name: NY-IAC-EWLC.cisco.local  #required field
                file_path: loaction to save
              - capture_type: FULL
                preview_description: "Full ICAP capture for troubleshooting"
                duration_in_mins: 30
                client_mac: 50:91:E3:47:AC:9E  #required field
                wlc_name: NY-IAC-EWLC.cisco.local  #required field
                file_path: loaction to save

  - hosts: dnac_servers
    vars_files:
      - credentials.yml
    gather_facts: no
    connection: local
    tasks:
      - name: Download icap on Cisco Catalyst Center
        cisco.dnac.assurance_icap_settings_workflow_manager:
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
            - assurance_icap_download:
                  - capture_type: FULL
                    client_mac: 50:91:E3:47:AC:9E  #required field
                    start_time: "2025-03-05 11:56:00"
                    end_time: "2025-03-05 12:01:00"
                    file_path: /Users/senorpink/Documents
    """

RETURN = r"""
# Case 1: Successful creation of ICAP settings, deployment of ICAP configuration, and discarding failed tasks.
response_1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
          "taskId": "string",
           "url": "string"
    },
    "version": "string"
    }

"""


try:
    import pathlib
    HAS_PATHLIB = True
except ImportError:
    HAS_PATHLIB = False
    pathlib = None
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
from datetime import datetime
import time
import os


class Icap(DnacBase):
    """Class containing member attributes for ICAP setting workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged"]
        self.result["response"] = [{
            "assurance_icap_settings": {
                "response": {},
                "msg": {}
            },
            "assurance_icap_download": {
                "response": {
                    "msg": {}
                },
            }
        }]

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
            'assurance_icap_settings': {
                'type': 'list',
                'elements': 'dict',
                'capture_type': {'type': 'str', 'required': True, 'choices': ["FULL", "ONBOARDING", "OTA", "RFSTATS", "ANOMALY"]},
                'duration_in_mins': {'type': int, 'required': True},
                'client_mac': {'type': 'str', 'required': True},
                'wlc_id': {'type': 'str', 'required': False},
                'ap_id': {'type': 'str', 'required': False},
                'slot': {'type': list, 'required': False},
                'ota_band': {'type': 'str', 'required': False, 'choices': ["2.4GHz", "5GHz", "6GHz"]},
                'ota_channel': {'type': int, 'required': True},
                'ota_channel_width': {'type': int, 'required': True},

            },
            'assurance_icap_download': {
                'type': 'list',
                'elements': 'dict',
                'capture_type': {'type': 'str', 'required': True},
                'client_mac': {'type': 'str', 'required': True},
                'ap_mac': {'type': 'str', 'required': False},
                'start_datetime': {'type': 'str', 'required': False},
                'end_datetime': {'type': 'str', 'required': False},
                "file_path": {"type": "str", "required": True},
            }
        }

        if not self.config:
            self.msg = "Validation failed: The 'config' parameter is missing or empty."
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

    def get_want(self, config):
        """
        Retrieve and store assurance icap details from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.

        """

        want = {}
        want["assurance_icap_settings"] = config.get("assurance_icap_settings")
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_have(self, config):
        """
        Get the current ICAP-associated information from the Cisco Catalyst Center
        based on the provided playbook details.

        This function processes the playbook configuration to retrieve device IDs for
        Wireless LAN Controllers (WLC) and Access Points (AP) based on their names.
        It logs the progress and any failures encountered while fetching the device IDs.

        Parameters:
            config (dict): Playbook details containing a list of assurance Intelligent Capture Settings.
                        Each setting includes WLC and AP names that will be used to
                        retrieve the corresponding device IDs.

        Returns:
            self: The current object with updated assurance Intelligent Capture Settings, including
                the retrieved WLC and AP IDs.
            """
        assurance_icap_settings_list = config.get("assurance_icap_settings", [])
        self.log("Assurance Intelligent Capture Settings: {0}".format(assurance_icap_settings_list), "INFO")

        if not assurance_icap_settings_list:
            self.msg = "No data need to be retrieved for icap config creation "
            return self

        have = []
        errors = []

        for assurance_icap_settings in assurance_icap_settings_list:
            # Process WLC Name
            wlc_name = assurance_icap_settings.get("wlc_name")
            if wlc_name:
                self.log("Fetching device ID for WLC: {0}".format(wlc_name), "INFO")
                wlc_id = self.get_device_id(wlc_name)
                if wlc_id:
                    self.log("Retrieved WLC ID: {0} for WLC Name: {1}".format(wlc_id, wlc_name), "INFO")
                    assurance_icap_settings["wlc_id"] = wlc_id
                else:
                    error_msg = "WLC ID retrieval failed for '{0}'".format(wlc_name)
                    self.log(error_msg, "ERROR")
                    errors.append(error_msg)

            # Process AP Name
            ap_name = assurance_icap_settings.get("ap_name")
            if ap_name:
                self.log("Fetching device ID for AP: {0}".format(ap_name), "INFO")
                ap_id = self.get_device_id(ap_name)
                if ap_id:
                    self.log("Retrieved AP ID: {0} for AP Name: {1}".format(ap_id, ap_name), "INFO")
                    assurance_icap_settings["ap_id"] = ap_id
                else:
                    error_msg = "AP ID retrieval failed for '{0}'".format(ap_name)
                    self.log(error_msg, "ERROR")
                    errors.append(error_msg)

            have.append(assurance_icap_settings)

        self.have = have
        self.log("Final have state: {0}".format(self.have), "INFO")

        if errors:
            self.set_operation_result("failed", False, "\n".join(errors), "ERROR")

        return self

    def get_device_id(self, hostname):
        """
        Retrieve the device ID by querying the 'get_device_list' API using the hostname.

        Parameters:
        self (object): The instance interacting with Cisco Catalyst Center.
        hostname (str): The hostname of the device to retrieve the ID.

        Returns:
        str: The device ID if found, else None.
        """
        self.log("Retrieving device ID for hostname: {0}".format(hostname), "DEBUG")
        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                params={"hostname": hostname}  # Using hostname in the API call
            )

            devices = response.get("response", [])
            if not devices:
                self.msg = "No devices found for the hostname '{0}'.".format(hostname)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

            # Assuming the device list response contains a list of devices
            device_id = devices[0].get("id")
            if not device_id:
                msg = "Device ID not found for hostname '{0}'.".format(hostname)
                self.log(msg, "ERROR")
                self.set_operation_result("failed", False, msg, "ERROR")
                return None

            self.log("Retrieved device ID '{0}' for hostname '{1}'.".format(device_id, hostname), "INFO")
            return device_id

        except Exception as e:
            self.msg = "An error occurred while retrieving device ID for '{0}': {1}".format(hostname, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

    def get_pcap_ids(self, assurance_icap_download):
        """
        Retrieves a list of ICAP responses matching the specified criteria for each settings dictionary.

        Args:
            assurance_icap_download (dict): Dictionary containing filter parameters.
                - capture_type(str): Capture type (Required).
                - ap_mac (str): AP MAC address (Optional).
                - client_mac (str): Client MAC address (Required).
                - start_time (int): Start time in UNIX epoch (Optional).
                - end_time (int): End time in UNIX epoch (Optional).

        Returns:
            str: The first file ID found in the response, or None if not found.

        """
        self.log("Starting to retrieve the data for download", "DEBUG")

        try:
            # Extract parameters
            capture_type = assurance_icap_download.get('capture_type')
            ap_mac = assurance_icap_download.get('ap_mac')
            client_mac = assurance_icap_download.get('client_mac')
            start_time = assurance_icap_download.get('start_time')
            end_time = assurance_icap_download.get('end_time')

            if not capture_type:
                error_message = "'capture_type' is a required parameter."
                self.log(error_message, "ERROR")
                self.set_operation_result("failed", False, error_message, "ERROR")
                return None

            param = {
                'type': capture_type,
                'clientMac': client_mac
            }

            # Add optional parameters if they are not None
            if ap_mac is not None:
                param['apMac'] = ap_mac
            if start_time is not None and end_time is not None:
                # Convert timestamps to epoch with timezone
                errormsg = []
                start_time, end_time = self.validate_start_end_datetime(start_time, end_time, errormsg)
                self.log("Start Time (Epoch): {}".format(start_time))
                self.log("End Time (Epoch): {}".format(end_time))

                if errormsg:
                    self.msg = errormsg
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    self.log(self.msg, "ERROR")
                    return None

            # Ensure 'apMac' is mandatory for 'OTA' and 'ANOMALY' capture types
            if capture_type in ["OTA", "ANOMALY"] and ap_mac is None:
                self.msg = "'apMac' is required for capture types 'OTA' and 'ANOMALY'."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                self.log(self.msg, "ERROR")
                return None

            # Execute API call
            response = self.dnac._exec(
                family="sensors",
                function="lists_i_cap_packet_capture_files_matching_specified_criteria_v1",
                params=param
            )
            self.log("ICAP Packet Capture API Response: {}".format(response), "DEBUG")

            # Check if response is an empty list
            if isinstance(response, list) and not response:
                failure_reason = "Empty response received for ICAP parameters: {}".format(param)
                self.msg = "ICAP configuration deployment failed: {}".format(failure_reason)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                self.log(self.msg, "ERROR")
                return None

            # Extract response dictionary
            response_data = response.get("response", [])

            # Check if response_data is empty
            if not response_data:
                failure_reason = "No ICAP packet capture files found for parameters: {}".format(param)
                self.msg = "ICAP configuration deployment failed: {}".format(failure_reason)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                self.log(self.msg, "ERROR")
                return None

            # Extract the first file ID
            file_id = response_data[0].get("id")
            if not file_id:
                failure_reason = "ICAP packet capture file ID missing in response."
                self.msg = "ICAP configuration deployment failed: {}".format(failure_reason)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                self.log(self.msg, "ERROR")
                return None

            self.log("Extracted ICAP file ID: {}".format(file_id), "INFO")
            return file_id

        except Exception as e:
            failure_reason = "An error occurred while retrieving ICAP packet capture files: {}".format(str(e))
            self.msg = "ICAP configuration deployment failed: {}".format(failure_reason)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            self.log(self.msg, "ERROR")
            return None

    def validate_start_end_datetime(self, start_time, end_time, errormsg):
        """
        Validate the start and end datetime parameters from the input playbook
        and convert them into Unix epoch format (milliseconds).

        Parameters:
            start_time (str): The start datetime string in "%Y-%m-%d %H:%M:%S" format.
            end_time (str): The end datetime string in "%Y-%m-%d %H:%M:%S" format.
            errormsg (list): A list to store error messages if validation fails.

        Returns:
            tuple: (start_epoch_ms, end_epoch_ms) if valid, otherwise (None, None).
        """
        self.log("Validating start and end datetime: start='{}', end='{}'".format(start_time, end_time), "DEBUG")
        date_format = "%Y-%m-%d %H:%M:%S"

        try:
            start_datetime = datetime.strptime(start_time, date_format)
            end_datetime = datetime.strptime(end_time, date_format)

            if start_datetime > end_datetime:
                errormsg.append("Start datetime '{}' must be before end datetime '{}'.".format(start_time, end_time))
                return None, None

            start_epoch_ms = int(start_datetime.timestamp() * 1000)
            end_epoch_ms = int(end_datetime.timestamp() * 1000)
            self.log("Successfully validated start and end datetime.", "INFO")

            return start_epoch_ms, end_epoch_ms

        except ValueError as e:
            errormsg.append("Unable to validate Start date time, end date time. {}".format(e))
            return None, None  # Fixed return type

        except Exception as e:
            errormsg.append("An unexpected error occurred during datetime validation: {}".format(e))
            return None, None  # Ensure consistent return type

    def get_diff_merged(self, config):
        """
        Create Assurance ICAP configurations in Cisco Catalyst Center based on the playbook details

        Parameters:
            config (list of dict) - Playbook details containing
            Assurance icap information.

        Returns:
            self - The current object with Assurance icap information.
        """
        assurance_icap_settings = config.get("assurance_icap_settings")
        assurance_icap_download = config.get("assurance_icap_download")

        if assurance_icap_settings is not None:
            self.create_icap(assurance_icap_settings)

        if assurance_icap_download:
            self.download_icap_packet_traces(assurance_icap_download)

        return self

    def download_icap_packet_traces(self, assurance_icap_download):
        """
        Downloads ICAP packet capture files using the provided list of elements.

        Args:
            assurance_icap_download (list): List of elements used to fetch ICAP packet capture file IDs.

        Returns:
            list: List of responses containing downloaded file details or error messages.
        """
        responses = []
        self.log("Starting the ICAP packet capture download process.")

        try:
            for icap_element in assurance_icap_download:
                self.log(icap_element)

                download_id = self.get_pcap_ids(icap_element)

                if not download_id:
                    self.log("No ICAP ID found for element: {}".format(icap_element), "WARNING")
                    continue

                self.log("Fetching ICAP packet capture for ID: {}".format(download_id))
                response = self.dnac._exec(
                    family="sensors",
                    function="downloads_a_specific_i_cap_packet_capture_file_v1",
                    op_modifies=True,
                    params={"id": download_id}
                )
                response = response.data
                self.log("Response received for ICAP ID {}: {}".format(download_id, response))

                # If response contains binary data, save it as a .pcap file
                if response and isinstance(response, bytes):
                    file_path = icap_element.get("file_path")
                    if file_path:
                        file_path = os.path.join(file_path, download_id)
                        self.save_pcap_file(file_path, response)
                        responses.append({"icap_id": download_id, "status": "success", "file_path": file_path})
                        return responses
                    else:
                        self.log("No valid file path provided for ICAP ID: {}".format(download_id), "ERROR")
                        self.msg = "No valid file path provided for ICAP ID: {}".format(download_id)
                        responses.append({"icap_id": download_id, "status": "failed", "error": "No valid file path"})
                        self.set_operation_result("failed", False, self.msg, "ERROR")

        except Exception as e:
            error_msg = "Failed to download ICAP packet traces: {}".format(str(e))
            self.log({"error": error_msg})
            self.msg = error_msg
            self.set_operation_result("failed", False, self.msg, "ERROR")

    def save_pcap_file(self, file_path, data):
        """
        Saves the binary data as a .pcap file.

        Args:
            file_path (str): The file path where the .pcap file should be saved.
            data (bytes): The binary packet capture data.

        Returns:
            None
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "wb") as pcap_file:
                pcap_file.write(data)

            self.msg = "Successfully saved ICAP packet capture file at: {}".format(file_path)
            self.log(self.msg, "INFO")
            self.status = "success"
            self.result['changed'] = True
            self.result["response"][0]["assurance_icap_download"]["response"]["msg"] = self.msg
        except Exception as e:
            self.log("Failed to save ICAP file at {}: {}".format(file_path, str(e)), "ERROR")

    def deploy_icap_config(self, preview_activity_id, preview_description):
        """
        Deploy an Intelligent Capture Configuration intent in Cisco Catalyst Center.

        This method deploys the specified Intelligent Capture Configuration based on the provided details and
        preview activity ID. It handles task creation, monitors task status, and logs success or failure.

        Parameters:
            preview_activity_id (str): Preview activity ID.
            preview_description (str): Description of the ICAP deployment.

        Returns:
            self: The current object with operation result and status message.
        """
        self.log("Starting deployment of ICAP configuration: {0}".format(preview_activity_id), "INFO")
        try:
            self.log("Requested payload for deploying {0}".format(preview_activity_id), "DEBUG")
            task_name = "deploys_the_i_cap_configuration_intent_by_activity_id"
            response = self.dnac._exec(
                family="sensors",
                function="deploys_the_i_cap_configuration_intent_by_activity_id_v1",
                op_modifies=True,
                params={"preview_activity_id": preview_activity_id, "object": {}}
            )
            response = response.get("response")
            task_id = response.get("taskId")
            self.log("Received response for deploy icap congif as: {0}".format(response), "INFO")
            if not task_id:
                self.msg = "Failed to retrieve task ID for ICAP deployment."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            task_details = self.get_task_details(task_id)
            preview_activity_id = task_id
            if task_details.get("isError"):
                failure_reason = task_details.get("failureReason", "Unknown error")
                self.msg = "ICAP configuration deployment failed: {0}".format(failure_reason)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                self.log(self.msg, "ERROR")
                return self

            self.log("Successfully deployed ICAP configuration: {0}".format(preview_description), "INFO")
            self.want["want_deployment_task_id"] = task_id  # Store task ID
            return self

        except Exception as e:
            self.msg = "An exception occured while deploying ICAP config '{0}' in Cisco Catalyst Center: {1}".format(preview_description, str(e))
            self.log("Attempting to delete ICAP config due to deployment failure.", "WARNING")
            try:
                self.delete_icap_config(preview_activity_id, preview_description).check_return_status()
            except Exception as e:
                self.log("exception for deployment {0}".format(str(e)), "DEBUG")
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def update_keys(self, data, mapping):
        """
        Update dictionary keys in a list of dictionaries based on a given mapping.

        This function iterates over a list of dictionaries and replaces keys according
        to the provided mapping dictionary. If a key exists in the mapping, it is
        replaced with the corresponding value; otherwise, it remains unchanged.

        Parameters:
        data (list of dict): A list of dictionaries whose keys need to be updated.
        mapping (dict): A dictionary defining key replacements, where each key
                        represents the original key and the value is the new key.

        Returns:
        list of dict: A list of dictionaries with updated keys.
        """
        if not data:
            self.log("No data provided for key update.", "DEBUG")
            return []

        self.log("Updating dictionary keys based on mapping.", "DEBUG")
        return [{mapping.get(k, k): v for k, v in item.items()} for item in data]

    def create_icap(self, assurance_icap_details):
        """
        Creates Intelligent Capture Configuration in the Cisco Catalyst Center, monitors its task status, and takes appropriate actions
        based on the result of the task. If the task fails, a cleanup function is called to delete the configuration.
        If the task succeeds, the next step in the workflow is executed.

        Args:
            assurance_icap_details (list): A list of dictionaries containing the details for Intelligent Capture Configuration.

        Returns:
            self: Returns the instance of the class with updated `status` and `msg` attributes.
        """

        self.log("Starting ICAP configuration creation with details: {0}".format(assurance_icap_details), "INFO")
        result_icap_settings = self.result.get("response")[0].get("assurance_icap_settings")

        for icap in assurance_icap_details:
            capture_type = icap.get("capture_type")
            if capture_type is None:
                self.msg = "Missing required parameter 'capture_type' in assurance_icap_settings"
                self.set_operation_result("failed", False, self.msg, "ERROR")

        preview_description = assurance_icap_details[0].get("preview_description")
        key_mapping = {
            "capture_type": "captureType",
            "preview_description": "previewDescription",
            "duration_in_mins": "durationInMins",
            "client_mac": "clientMac",
            "wlc_id": "wlcId",
            "ap_id": "apId"
        }

        # Update keys in assurance_icap_details
        updated_assurance_icap_details = self.update_keys(assurance_icap_details, key_mapping)
        keys_to_delete = ['previewDescription', "wlc_name", "ap_name"]

        # Iterate through each dictionary in the list and pop the specified keys
        for item in updated_assurance_icap_details:
            for key in keys_to_delete:
                item.pop(key, None)

        try:
            task_name = "creates_an_i_cap_configuration_intent_for_preview_approve_v1"
            param = {"previewDescription": preview_description, "payload": updated_assurance_icap_details}
            self.log("Creating Intelligent Capture Configuration with the following parameters: {0}.".format(param))

            response = self.dnac._exec(
                family="sensors",
                function='creates_an_i_cap_configuration_intent_for_preview_approve_v1',
                op_modifies=True,
                params=param,
            )
            self.log("Received response for create icap congif as: {0}".format(response), "INFO")
            response = response.get("response")
            task_id = response.get("taskId")
            if not task_id:
                self.msg = "Unable to retrieve the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")

            task_details = self.get_task_details(task_id)
            preview_activity_id = task_id
            if task_details.get("isError") is True:
                failure_reason = task_details.get("failureReason")
                self.msg = "ICAP configuration creation failed: {0}".format(failure_reason)
                self.set_operation_result("failed", False, failure_reason, "ERROR")
                return self

            # Proceed with deployment if successful
            self.log("ICAP configuration created successfully. Proceeding with deployment.", "INFO")
            self.msg = "ICAP Configuration '{0}' deployed successfully.".format(preview_description)
            self.deploy_icap_config(preview_activity_id, preview_description)

            if isinstance(result_icap_settings, dict):
                result_icap_settings.setdefault("response", {}).update(
                    {"Deployed ICAP configuration": updated_assurance_icap_details}
                )
                result_icap_settings.setdefault("msg", {}).update(
                    {preview_description: "ICAP configuration deployed successfully"}
                )
            self.set_operation_result("success", True, self.msg, "INFO", self.result["response"])

        except Exception as e:
            self.msg = "An exception occurred while creating ICAP config in Cisco Catalyst Center: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

    def delete_icap_config(self, preview_activity_id, preview_description):
        """
        Discards an Intelligent Capture Configuration intent in Cisco Catalyst Center using the task ID.

        Args:
            task_id (str): The unique identifier of the task associated with the Intelligent Capture Configuration intent.
            preview_description (str):  SRepresents the ICAP intent's preview-deploy description string.

        Returns:
            self (object): Returns the current instance of the class with updated status and message attributes.

        Description:
            This method retrieves the `previewActivityId` using the provided task ID, then initiates the discard operation
            for the Intelligent Capture Configuration intent in Cisco Catalyst Center. It monitors the task's status and updates the
            instance attributes with the operation's result.

        """
        self.log("Starting deleting {0} the failed Intelligent Capture Configuration".format(preview_description), "INFO")

        try:
            response = self.dnac._exec(
                family="sensors",
                function='discards_the_i_cap_configuration_intent_by_activity_id_v1',
                op_modifies=True,
                params={"preview_activity_id": preview_activity_id}
            )
            self.log("Received response for dicard icap congif as: {0}".format(response.get("response")), "INFO")
            self.msg = "Successfully discarded ICAP config."
            return self

        except Exception as e:
            self.msg = "An exception occurred while discarding ICAP config in Cisco Catalyst Center: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

    def get_device_deployment_status(self, deployment_task_id):
        """
        Get the deployment status of a device from Cisco Catalyst Center.

        Parameters:
            deployment_task_id (str): The task ID for the deployment.

        Returns:
            list: The response containing deployment status details.
        """
        self.log("Fetching deployment status for task ID: {0}".format(deployment_task_id), "INFO")

        start_time = time.time()
        retry_interval = int(self.payload.get("dnac_task_poll_interval", 5))
        resync_retry_count = int(self.payload.get("dnac_api_task_timeout", 100))

        while True:
            try:
                response = self.dnac._exec(
                    family="sensors",
                    function="get_device_deployment_status_v1",
                    params={"deploy_activity_id": deployment_task_id}
                )
                self.log("Received deployment status response: {}".format(response), "INFO")

                # Check if response is valid
                if response.get("response"):
                    deployment_status = response["response"][0].get("status")

                    if deployment_status == "Success":
                        return response["response"]

            except Exception as e:
                self.log("Error fetching deployment status: {}".format(str(e)), "ERROR")

            # Check if timeout has been reached
            if time.time() - start_time >= resync_retry_count:
                self.log("Timeout reached while fetching deployment status.", "ERROR")
                return []

            time.sleep(retry_interval)  # Wait before retrying

    def verify_diff_merged(self, config):
        """
        Validates the Cisco Catalyst Center ICAP configuration with playbook details when state is merged.

        Parameters:
            config (dict): Playbook details containing ICAP configuration.

        Returns:
            self: The current object with ICAP configuration validation result.
        """
        self.log("Requested State (want): {0}".format(self.want), "INFO")

        assurance_icap_settings_list = config.get("assurance_icap_settings", [])
        self.log("Assurance ICAP Settings: {0}".format(assurance_icap_settings_list), "INFO")

        assurance_icap_download = config.get("assurance_icap_download", [])
        self.log("Assurance ICAP download details: {0}".format(assurance_icap_download), "INFO")

        if not assurance_icap_settings_list and not assurance_icap_download:
            self.msg = "No data need to be retrieved for icap config creation"
            return self

        if config.get("assurance_icap_settings") is not None:
            deployment_task_id = self.want.get("want_deployment_task_id")

            if deployment_task_id:
                deployment_response = self.get_device_deployment_status(deployment_task_id)
                self.log("Received deployment status for the current deployment id {0} as {1}"
                         .format(deployment_task_id, deployment_response), "INFO"
                         )
                deployment_success = False
                for deployment in deployment_response:
                    if deployment.get("status") == "Success":
                        deployment_success = True
                if deployment_success:
                    self.log("Successfully validated ICAP configuration(s).", "INFO")
                    self.result.get("response")[0].get(
                        "assurance_icap_settings").update({"Validation": "Success"})
                    return self  # Exit early if any successful validation is found

                # If none of the deployments were successful
                self.set_operation_result("failed", False, "ICAP deployment Verification is unsuccessful", "ERROR")

        if config.get("assurance_icap_download") is not None:
            for download_entry in assurance_icap_download:
                file_path = download_entry.get("file_path")
                self.log("Verifying ICAP download file path: {0}".format(file_path))
                if file_path:
                    abs_file_path = pathlib.Path(file_path).resolve()

                    window_seconds = 10
                    current_time = time.time()
                    window_start_time = current_time - window_seconds

                    files_found = []
                    try:
                        for f in abs_file_path.iterdir():
                            if f.stat().st_mtime > window_start_time:
                                files_found.append(f.name)
                    except Exception as e:
                        self.msg = (
                            "Failed to verify ICAP download output. Error checking file path: {0}".format(str(e))
                        )
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    if files_found:
                        self.msg = "ICAP download files verified successfully. Files: {0}".format(files_found)
                        self.log("ICAP download files verified successfully. Files: {0}".format(files_found), "INFO")
                        self.result.get("response")[0].get(
                            "assurance_icap_download").update({"Validation": "Success"})
                    else:
                        self.msg = "No ICAP download files found at path: {0}".format(abs_file_path)
                        self.log("No ICAP download files found at path: {0}".format(abs_file_path), "WARNING")
                        self.set_operation_result("Failed", False, self.msg, "INFO")

        return self


def main():
    """Main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": '443'},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": True},
        "dnac_version": {"type": 'str', "default": '2.2.3.3'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": True},
        "dnac_api_task_timeout": {"type": 'int', "default": 1200},
        "dnac_task_poll_interval": {"type": 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_assurance = Icap(module)
    state = ccc_assurance.params.get("state")
    ccc_version = ccc_assurance.get_ccc_version()

    if ccc_assurance.compare_dnac_versions(ccc_version, "2.3.7.9") < 0:
        ccc_assurance.msg = (
            "The specified version '{0}' does not support the Assurance Intelligent Capture Settings feature. Supported versions start from '2.3.7.9' onwards."
            .format(ccc_assurance.get_ccc_version())
        )
        ccc_assurance.status = "failed"
        ccc_assurance.check_return_status()

    if state not in ccc_assurance.supported_states:
        ccc_assurance.status = "invalid"
        ccc_assurance.msg = "State {0} is invalid".format(state)
        ccc_assurance.check_return_status()

    ccc_assurance.validate_input().check_return_status()
    config_verify = ccc_assurance.params.get("config_verify")

    for config in ccc_assurance.validated_config:
        ccc_assurance.reset_values()
        ccc_assurance.get_want(config).check_return_status()
        ccc_assurance.get_have(config).check_return_status()
        ccc_assurance.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_assurance.verify_diff_state_apply[state](config).check_return_status()

        module.exit_json(**ccc_assurance.result)


if __name__ == "__main__":
    main()

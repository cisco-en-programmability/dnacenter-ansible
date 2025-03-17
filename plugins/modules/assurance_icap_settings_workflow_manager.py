#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on Assurance ICAP settings in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Megha Kandari, Madhan Sankaranarayanan']

DOCUMENTATION = r"""
---
module: assurance_icap_settings_workflow_manager
short_description: Manage ICAP settings in Cisco Catalyst Center.
description:
  - Configures ICAP settings for capturing client and network device information for onboarding and monitoring.
  - This module interacts with Cisco DNA Center's Assurance settings to configure ICAP settings.
  - Supports automated deployment of ICAP configurations via this module.
version_added: '6.31.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Megha Kandari (@kandarimegha)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
   description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
   type: bool
   default: True
  state:
    description:
      - The state of Cisco Catalyst Center after module completion.
    type: str
    choices: ["merged"]
    default: merged
  config:
    description:
      - List of details required for ICAP configuration, creation, and deployment.
    type: list
    elements: dict
    required: true
    suboptions:
      assurance_icap_settings:
        description:
          - Configures ICAP settings for capturing client and network device information for onboarding and monitoring.
        type: list
        elements: dict
        suboptions:
          capture_type:
            description: The type of ICAP capture to be performed (e.g., onboarding).
            type: str
            choices: [FULL, ONBOARDING, OTA, RFSTATS, ANOMALY]
          duration_in_mins:
            description: The duration of the ICAP capture session in minutes.
            type: int
          client_mac:
            description: The MAC address of the client device for which the capture is being performed.
            type: str
          wlc_name:
            description: The name of the Wireless LAN Controller (WLC) involved in the ICAP capture.
            type: str
          ap_name:
            description: The name of the Access Point (AP) for the capture.
            type: str
          slot:
            description: List of slot numbers for the capture session.
            type: list
            elements: int
          ota_band:
            description: The OTA band (e.g., 5GHz, 2.4GHz) for the capture.
            type: str
          ota_channel:
            description: The OTA channel (e.g., 36, 40) for the capture.
            type: int
          ota_channel_width:
            description: The width of the OTA channel (e.g., 20MHz, 40MHz).
            type: int

requirements:
  - dnacentersdk >=  2.8.6
  - python >= 3.9
notes:
  - SDK Method used are
    sensors.AssuranceSettings.get_device_deployment_status,
    sensors.AssuranceSettings.creates_an_icap_configuration_intent_for_preview_approve,
    sensors.AssuranceSettings.discards_the_icap_configuration_intent_by_activity_id
    sensors.AssuranceSettings.deploys_the_i_cap_configuration_intent_by_activity_id_v1

  - Paths used are
    POST /dna/intent/api/icapSettings/configurationModels
    DELETE /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}
    POST /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/deploy
    GET /dna/data/api/v1/icap/captureFiles
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
                preview_description: test
                duration_in_mins: 30
                client_mac: 50:91:E3:47:AC:9E  #required field
                wlc_name: NY-IAC-EWLC.cisco.local  #required field
              - capture_type: FULL
                preview_description: onboard creation check
                duration_in_mins: 30
                client_mac: 50:91:E3:47:AC:9E  #required field
                wlc_name: NY-IAC-EWLC.cisco.local  #required field
    """

RETURN = r"""
#Case 1: Successful creation of Icap settings, deployment of icap config and discard failed tasks.
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


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)


class Icap(DnacBase):
    """Class containing member attributes for icap setting workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged"]
        self.result["response"] = [
            {"assurance_icap_settings": {"response": {}, "msg": {}}},
        ]

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
                'capture_type': {'type': 'str', 'required': True},
                'duration_in_mins': {'type': int, 'required': True},
                'client_mac': {'type': 'str', 'required': True},
                'wlc_id': {'type': 'str', 'required': False},
                'ap_id': {'type': 'str', 'required': False},
                'slot': {'type': list, 'required': False},
                'ota_band': {'type': 'str', 'required': False},
                'ota_channel': {'type': int, 'required': True},
                'ota_channel_width': {'type': int, 'required': True},

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

    def get_want(self, config):
        """
        Retrieve and store assurance icap details from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.
        Raises:
            AnsibleFailJson: If an incorrect import type is specified.

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
        """
        assurance_icap_settings_list = config.get("assurance_icap_settings", [])
        self.log("Assurance ICAP Settings: {0}".format(assurance_icap_settings_list), "INFO")

        have = []

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
                    self.log("Failed to retrieve WLC ID for '{0}'".format(wlc_name), "ERROR")
                    self.set_operation_result("failed", False, "WLC ID retrieval failed for '{0}'".format(wlc_name), "ERROR")
                    return self

            # Process AP Name
            ap_name = assurance_icap_settings.get("ap_name")
            if ap_name:
                self.log("Fetching device ID for AP: {0}".format(ap_name), "INFO")
                ap_id = self.get_device_id(ap_name)
                if ap_id:
                    self.log("Retrieved AP ID: {0} for AP Name: {1}".format(ap_id, ap_name), "INFO")
                    assurance_icap_settings["ap_id"] = ap_id
                else:
                    self.log("Failed to retrieve AP ID for '{0}'".format(ap_name), "ERROR")
                    self.set_operation_result("failed", False, "AP ID retrieval failed for '{}'".format(ap_name), "ERROR")
                    return self

            have.append(assurance_icap_settings)

        self.have = have
        self.log("Final have state: {0}".format(self.have), "INFO")
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
            if device_id:
                self.log("Device ID '{0}' retrieved for hostname '{1}'".format(device_id, hostname), "INFO")
                return device_id
            else:
                self.msg = "Device ID not found for the hostname '{0}'.".format(hostname)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        except Exception as e:
            self.msg = "An error occurred while retrieving device ID for '{0}': {1}".format(hostname, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

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

        if assurance_icap_settings is not None:
            self.create_icap(assurance_icap_settings)

        return self

    def deploy_icap_config(self, preview_activity_id, preview_description):
        """
        Deploy an ICAP configuration intent in Cisco Catalyst Center.

        This method deploys the specified ICAP configuration based on the provided details and
        preview activity ID. It handles task creation, monitors task status, and logs success or failure.

        Parameters:
            assurance_icap_details (dict): ICAP details including preview description.
            preview_activity_id (str): Preview activity ID.

        Returns:
            self: The current object with operation result and status message.
        """
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
                self.msg = "Unable to retrieve the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            task_details = self.get_task_details(task_id)
            preview_activity_id = task_id
            if task_details.get("isError") is True:
                failure_reason = task_details.get("failureReason")
                self.log("deployment of ICAP configuration failed.", "ERROR")
                self.msg = "deployment of ICAP configuration failed, due to: {0}".format(failure_reason)
                self.set_operation_result("failed", False, failure_reason, "ERROR")
            else:
                self.log("deployed icap config '{0}' successfully in the Cisco Catalyst Center".format(preview_description), "DEBUG")
                # Store task_id inside want with the key 'want_deployment_task_id'
                self.want["want_deployment_task_id"] = task_id  # Storing task ID
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

        except Exception as e:
            self.msg = "An exception occured while deploying icap config '{0}' in Cisco Catalyst Center: {1}".format(preview_description, str(e))
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
        return [{mapping.get(k, k): v for k, v in item.items()} for item in data]

    def create_icap(self, assurance_icap_details):
        """
        Creates ICAP configuration in the Cisco Catalyst Center, monitors its task status, and takes appropriate actions
        based on the result of the task. If the task fails, a cleanup function is called to delete the configuration.
        If the task succeeds, the next step in the workflow is executed.

        Args:
            assurance_icap_details (list): A list of dictionaries containing the details for ICAP configuration.

        Returns:
            self: Returns the instance of the class with updated `status` and `msg` attributes.
        """

        self.log("Starting creating ICAP configuration in the Cisco Catalyst Center with provided details:{0}".format(assurance_icap_details), "INFO")
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
            self.log("Creating ICAP configuration with the following parameters: {0}.".format(param))

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
                self.msg = "creation of ICAP configuration failed, due to: {0}".format(failure_reason)
                self.set_operation_result("failed", False, failure_reason, "ERROR")

            else:
                self.log("Task succeeded. Proceeding to the next function.", "INFO")
                self.msg = "ICAP Configuration '{0}' deployed successfully in the Cisco Catalyst Center".format(preview_description)
                self.deploy_icap_config(preview_activity_id, preview_description)
                result_icap_settings.get("response").update(
                    {"Deployed icap configuration": updated_assurance_icap_details})
                result_icap_settings.get("msg").update(
                    {icap.get("preview_description"): "Icap configuration Deployed Successfully"})
                self.set_operation_result("success", True, self.msg, "INFO", self.result["response"])

        except Exception as e:
            self.msg = "An exception occurred while creating ICAP config in Cisco Catalyst Center: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

    def delete_icap_config(self, preview_activity_id, preview_description):
        """
        Discards an ICAP configuration intent in Cisco Catalyst Center using the task ID.

        Args:
            task_id (str): The unique identifier of the task associated with the ICAP configuration intent.
            preview_description (str):  SRepresents the ICAP intent's preview-deploy description string.

        Returns:
            self (object): Returns the current instance of the class with updated status and message attributes.

        Description:
            This method retrieves the `previewActivityId` using the provided task ID, then initiates the discard operation
            for the ICAP configuration intent in Cisco Catalyst Center. It monitors the task's status and updates the
            instance attributes with the operation's result.

        """
        self.log("Starting deleting {0} the failed icap configuration".format(preview_description), "INFO")

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
        response = self.dnac._exec(
            family="sensors",
            function="get_device_deployment_status_v1",
            params={"deploy_activity_id": deployment_task_id}
        )
        return response.get("response", [])

    def verify_diff_merged(self, config):
        """
        Validates the Cisco Catalyst Center ICAP configuration with playbook details when state is merged (Create).

        Parameters:
            config (dict): Playbook details containing ICAP configuration.

        Returns:
            self: The current object with ICAP configuration validation result.
        """
        self.log("Requested State (want): {0}".format(self.want), "INFO")

        if config.get("assurance_icap_settings") is not None:
            deployment_task_id = self.want.get("want_deployment_task_id")
            # deployment_task_id = "15c30bff-c201-4ec6-9f0f-40f587904e45"

            if deployment_task_id:
                deployment_response = self.get_device_deployment_status(deployment_task_id)
                self.log("Recieved deployment status for the current deployment id {0} as {1}"
                         .format(deployment_task_id, deployment_response), "INFO")
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

        self.msg = "Successfully verified the ICAP configuration Deployment."
        self.set_operation_result("success", True, self.msg, "INFO")
        return self


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
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
    if ccc_assurance.compare_dnac_versions(ccc_assurance.get_ccc_version(), "2.3.7.9") < 0:
        ccc_assurance.msg = (
            "The specified version '{0}' does not support the Assurance ICAP settings feature. Supported versions start from '2.3.7.9' onwards."
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

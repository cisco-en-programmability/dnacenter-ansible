#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on create and delete path trace details between
two different IP addresses and network in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function


__metaclass__ = type
__author__ = ['A Mohamed Rafeek, Madhan Sankaranarayanan']

DOCUMENTATION = r"""
---
module: pathtrace_settings_workflow_manager
short_description: Resource module for managing PathTrace settings in Cisco Catalyst Center
description: This module allows the management of PathTrace settings in Cisco Catalyst Center.
  - It supports creating and deleting configurations path trace.
  - This module interacts with Cisco Catalyst Center's PathTrace settings to configure source ip,
  destination ip, source port, destination port and protcol.
version_added: '6.30.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description: |
      Set to `True` to enable configuration verification on Cisco DNA Center after applying
      the playbook config. This will ensure that the system validates the configuration
      state after the change is applied.
    type: bool
    default: false
  state:
    description: |
      Specifies the desired state for the configuration. If `merged`, the module will create
      or update the configuration, adding new settings or modifying existing ones. If `deleted`,
      it will remove the specified settings.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description: A list containing the details for Path trace.
    type: list
    elements: dict
    required: true
    suboptions:
      assurance_pathtrace:
        description: |
          Configures network path trace settings for monitoring the paths between
          source and destination IP addresses.
        type: list
        elements: dict
        suboptions:
          flow_analysis_id:
            description: |
              The Flow Analysis ID for the path trace used to delete already
              created path trace when at the delete state. 
              Optional param used if not provide this will search and delete
              based on the below search params.
            type: str
            required: false
          source_ip:
            description: The source IP address for the path trace. This is a required field.
            type: str
            required: true
          dest_ip:
            description: The destination IP address for the path trace. This is a required field.
            type: str
            required: true
          source_port:
            description: The source port for the path trace (optional).
            type: str
            required: false
          dest_port:
            description: The destination port for the path trace (optional).
            type: str
            required: false
          protocol:
            description: The protocol to use for the path trace, e.g., TCP, UDP (optional).
            type: str
            choices: ["TCP", "UDP"]
            required: false
          include_stats:
            description: |
              A list of optional include_stats for the path trace, such as QOS statistics
              or additional details. e.g., - "DEVICE-STATS", "INTERFACE-STATS",
              "QOS-STATS", "PERFORMANCE-STATS", "ACL-TRACE"
            type: list
            elements: str
            required: false
          periodic_refresh:
            description: Boolean value to enable periodic refresh for the path trace.
            type: bool
            required: false
          control_path:
            description: |
              Boolean value to specify whether the path trace should include
              the control path (optional).
            type: bool
            required: false
          get_last_pathtrace_result:
            description: Boolean value to show the last result again for the path trace.
            type: bool
            required: false

requirements:
- dnacentersdk >= 2.10.0
- python >= 3.9
notes:
 - SDK Method used are
    path_trace.PathTraceSettings.retrieves_all_previous_pathtraces_summary,
    path_trace.PathTraceSettings.retrieves_previous_pathtraces_summary,
    path_trace.PathTraceSettings.initiate_a_new_pathtrace,
    path_trace.PathTraceSettings.delete_pathtrace_by_id,

 - Paths used are
    GET/dna/intent/api/v1/flow-analysis
    POST/dna/intent/api/v1/flow-analysis
    GET/dna/intent/api/v1/flow-analysis/{flowAnalysisId}
    DELETE/dna/intent/api/v1/flow-analysis/{flowAnalysisId}
"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  connection: local
  tasks:
    - name: Create path trace
      cisco.dnac.path_trace_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: true
        state: merged
        config_verify: true
        config:
        - assurance_pathtrace:
          - source_ip: "204.1.2.3"  # required field
            dest_ip: "204.1.2.4"  # required field
            control_path: false  # optional field
            dest_port: 80  # optional field
            include_stats:  # optional field 
              - "DEVICE-STATS"
              - "INTERFACE-STATS"
              - "QOS-STATS"
              - "PERFORMANCE-STATS"
              - "ACL-TRACE"
            periodic_refresh: false  # optional field
            protocol: "TCP"  # optional field
            source_port: 80  # optional field
            get_last_pathtrace_result: true # optional field
            flow_analysis_id: 232424 # optional field

    - name: Delete path trace by id
      cisco.dnac.path_trace_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log_level: DEBUG
        dnac_log: true
        state: deleted
        config_verify: true
        config:
        - assurance_pathtrace:
          - source_ip: "204.1.2.3"  # required field
            dest_ip: "204.1.2.4"  # required field
     """


RETURN = r"""

#Case 1: Successful creation of trace path
response_1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        Response: Create
        {
            "response": {
                "flowAnalysisId": "string",
                "taskId": "string",
                "url": "string"
            },
            "version": "string"
        }
    }

#Case 2: Successful deletion of trace path
response_2:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        Response: Delete
        {
            "response": {
                "taskId": "any",
                "url": "string"
            },
            "version": "string"
        }
    }

"""

import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)


class PathTraceSettings(DnacBase):
    """Class containing member attributes for Assurance setting workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.create_path, self.delete_path, self.not_processed = [], [], []

        self.keymap = dict(
            source_ip="sourceIP",
            dest_ip="destIP",
            control_path="controlPath",
            dest_port="destPort",
            source_port="sourcePort",
            periodic_refresh="periodicRefresh"
        )

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
            'assurance_pathtrace': {
                'type': 'list',
                'elements': 'dict',
                'source_ip': {'type': 'str', 'required': False},
                'dest_ip': {'type': 'str', 'required': False},
                'source_port': {'type': 'int', 'range_min': 1, 'range_max': 65535, 'required': False},
                'dest_port': {'type': 'int', 'range_min': 1, 'range_max': 65535, 'required': False},
                'protocol': {'type': 'str', 'choices': ['TCP', 'UDP'], 'required': False},
                'periodic_refresh': {'type': 'bool', 'default': True},
                'control_path': {'type': 'bool', 'default': True},
                'include_stats': {
                    'type': 'list',
                    'elements': 'str',
                    'required': False,
                    'choices_on_elements': ["DEVICE-STATS", "INTERFACE-STATS", "QOS-STATS",
                                            "PERFORMANCE-STATS", "ACL-TRACE"]
                },
                'get_last_pathtrace_result': {'type': 'bool', 'default': False},
                'flow_analysis_id': {'type': 'str', 'required': False}
            }
        }

        if not self.config:
            self.msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Validate configuration against the specification
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "The playbook contains invalid parameters: {0}".format(
                invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters " +\
            "using 'validate_input': {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")

        return self

    def input_data_validation(self, config):
        """
        Additional validation to check if the provided input path trace data is correct
        and as per the UI Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            config (dict): Dictionary containing the input path trace details.

        Returns:
            self: Current object with path trace input data.

        Description:
            Iterates through available path trace data and Returns the list of invalid
            data for further action or validation.
        """
        errormsg = []
        path_trace = config.get("assurance_pathtrace")

        if path_trace:
            for each_path in path_trace:
                flow_analysis_id = each_path.get("flow_analysis_id")
                if flow_analysis_id:
                    break

                source_ip = each_path.get("source_ip")
                if source_ip is None:
                    errormsg.append("source_ip: Source IP Address is missing in playbook.")
                elif not (self.is_valid_ipv4(source_ip) or self.is_valid_ipv6(source_ip)):
                    errormsg.append("source_ip: Invalid Source IP Address '{0}' in playbook.".
                                    format(source_ip))

                dest_ip = each_path.get("dest_ip")
                if dest_ip is None:
                    errormsg.append("dest_ip: Destination IP Address is missing in playbook.")
                elif not (self.is_valid_ipv4(dest_ip) or self.is_valid_ipv6(dest_ip)):
                    errormsg.append("dest_ip: Invalid Destination IP Address '{0}' in playbook.".
                                    format(dest_ip))

                source_port = each_path.get("source_port")
                if source_port and source_port not in range(1, 65536):
                    errormsg.append("source_port: Invalid Source Port number '{0}' in playbook."
                                    .format(source_port))

                dest_port = each_path.get("dest_port")
                if dest_port and dest_port not in range(1, 65536):
                    errormsg.append("dest_port: Invalid Destination Port number '{0}' in playbook."
                                    .format(dest_port))

                protocol = each_path.get("protocol")
                if protocol and protocol not in ("TCP", "UDP"):
                    errormsg.append("protocol: Invalid protocol '{0}' in playbook. either 'TCP' or 'UDP'"
                                    .format(protocol))

                periodic_refresh = each_path.get("periodic_refresh")
                if periodic_refresh and periodic_refresh not in (True, False):
                    errormsg.append(
                        "periodic_refresh: Invalid periodic refresh " +
                        "'{0}' in playbook. either true or false.".format(periodic_refresh))

                control_path = each_path.get("control_path")
                if control_path and control_path not in (True, False):
                    errormsg.append("control_path: Invalid control path '{0}' in playbook. either true or false."
                                    .format(control_path))

                get_last_pathtrace_result = each_path.get("get_last_pathtrace_result")
                if get_last_pathtrace_result and get_last_pathtrace_result not in (True, False):
                    errormsg.append("get_last_pathtrace_result: Invalid get last pathtrace result " +\
                                    "'{0}' in playbook. either true or false."
                                    .format(get_last_pathtrace_result))

                include_stats = each_path.get("include_stats")
                inclusions_list = ("DEVICE-STATS", "INTERFACE-STATS", "QOS-STATS",
                                   "PERFORMANCE-STATS", "ACL-TRACE")
                if include_stats:
                    for each_include in include_stats:
                        if each_include not in inclusions_list:
                            errormsg.append("inclusions: Invalid Include Stats '{0}' in playbook. "
                                            "Must be list of: {1}.".format(
                                                each_include, ", ".join(inclusions_list)))

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: '{0}' ".format(errormsg)
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.msg = "Successfully validated config params: {0}".format(str(config))
        self.log(self.msg, "INFO")
        return self

    def get_want(self, config):
        """
        Retrieve path trace or delete path trace data from playbook configuration.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing path trace details.

        Returns:
            self: The current instance of the class with updated 'want' attributes.

        Description:
            This function parses the playbook configuration to extract information related to path
            trace. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """
        want = {}
        if config:
            self.input_data_validation(config).check_return_status()
            want["assurance_pathtrace"] = config.get("assurance_pathtrace")
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_have(self, config):
        """
        Get the current path trace details for the given config from Cisco Catalyst Center

        Parameters:
            config (dict) - Playbook details containing Path Trace

        Returns:
            self - The current object with updated Global Pool,
            Reserved Pool, and Network information.
        """
        if config:
            path_list = config.get("assurance_pathtrace")
            self.have["assurance_pathtrace"] = []
            for each_path in path_list:
                get_trace = self.get_path_trace(each_path)
                if not get_trace:
                    self.msg = "No data found for the given config: {0}".format(config)
                    self.log(self.msg, "DEBUG")
                else:
                    self.have["assurance_pathtrace"].extend(get_trace)

        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        self.status = "success"
        return self

    def get_path_trace(self, config_data):
        """
        Get the path trace for the given playbook data and response with
        flow analysis id.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dict containing input data to get id for path trace.

        Returns:
            list: return the list of flow analysis IDs or None.

        Description:
            This function used to get the flow analysis id from the input config.
        """
        payload_data = {}
        for key, value in config_data.items():
            if value is not None and key not in ("control_path", "dest_port",
                                                 "include_stats", "periodic_refresh",
                                                 "protocol", "source_port"):
                mapped_key = self.keymap.get(key, key)
                payload_data[mapped_key] = value

        self.log("Get path trace for parameters: {0}".format(self.pprint(payload_data)), "INFO")
        try:
            response = self.dnac._exec(
                family="path_trace",
                function="retrieves_all_previous_pathtraces_summary",
                op_modifies=True,
                params=payload_data
            )
            self.log("Response from retrieves_all_previous_pathtraces_summary API: {0}".
                     format(self.pprint(response)), "DEBUG")
            if response and isinstance(response, dict):
                self.log("Received the path trace response: {0}".format(
                    self.pprint(response)), "INFO")
                return response.get("response")
            else:
                return None

        except Exception as e:
            self.msg = 'An error occurred during get path trace: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def create_path_trace(self, config_data):
        """
        Create the path trace for the given config with source and destination IP.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing input config data from playbook.

        Returns:
            flow_analysis_id (str): Returns string contains flow analysis ID.

        Description:
            This function get the path trace config input data and create the path trace then
            return output as string flow analysis id.
        """
        payload_data = {}
        for key, value in config_data.items():
            excluded_key = ["flow_analysis_id", "get_last_pathtrace_result"]
            if value is not None and key not in excluded_key:
                mapped_key = self.keymap.get(key, key)
                if key == "include_stats" and isinstance(value, list):
                    api_value = []
                    for each_value in value:
                        api_value.append(self.keymap.get(each_value, each_value))
                    payload_data[mapped_key] = api_value
                else:
                    payload_data[mapped_key] = value

        self.log("Creating path trace with parameters: {0}".format(
            self.pprint(payload_data)), "INFO")
        try:
            response = self.dnac._exec(
                family="path_trace",
                function="initiate_a_new_pathtrace",
                op_modifies=True,
                params=payload_data
            )
            self.log("Response from path trace careate API response: {0}".format(
                response), "DEBUG")

            if response and isinstance(response, dict):
                flow_analysis_id = response.get("response", {}).get("flowAnalysisId")
                if flow_analysis_id is not None:
                    self.log("Received the path trace flow analysis id: {0}".
                             format(flow_analysis_id), "INFO")
                    return flow_analysis_id

            self.msg = "Unable to Create the path trace for the config: {0}".format(
                self.pprint(payload_data)
            )
            self.not_processed.append(payload_data)
            self.set_operation_result("failed", False, self.msg, "ERROR",
                                      payload_data).check_return_status()
        except Exception as e:
            self.msg = 'An error occurred during create path trace: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def get_path_trace_with_flow_id(self, flow_id):
        """
        Get the path trace for the given flow analysis id and response with
        complete path trace between source and destination IP.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            flow_id (str): A string containing flow analysis id from creae path trace.

        Returns:
            dict: A dictionary of path trace details.

        Description:
            This function get the path trace for flow analysis id and return the complete
            path trace from source and destination IPs.
        """
        self.log("Getting path trace flow analysis id: {0}".format(str(flow_id)), "INFO")
        try:
            dnac_api_task_timeout = int(self.payload.get("dnac_api_task_timeout"))
            resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))

            while dnac_api_task_timeout:
                response = self.dnac._exec(
                    family="path_trace",
                    function="retrieves_previous_pathtrace",
                    params=dict(flow_analysis_id=flow_id)
                )
                self.log("Response from get path trace API: {0}".format(
                    self.pprint(response)), "DEBUG")
                if response and isinstance(response, dict):
                    status = response.get("response", {}).get("request", {}).get("status")
                    if status == "COMPLETED" or status == "FAILED":
                        self.log("Received the path trace response: {0}".format(
                            self.pprint(response)), "INFO")
                        return response.get("response")

                time.sleep(resync_retry_interval)
                dnac_api_task_timeout = dnac_api_task_timeout - resync_retry_interval

            self.msg = "Unable to get path trace for the flow analysis id: {0}".format(flow_id)
            self.not_processed.append(flow_id)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
        except Exception as e:
            self.msg = 'An error occurred during get path trace: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def delete_path_trace(self, flow_id):
        """
        Delete the path trace for the given flow analysis id and return taskid.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            flow_id (str): A string containing flow analysis id to delete path trace.

        Returns:
            dict or none: Return task id details or None.

        Description:
            This function delete the path trace for flow analysis id and return the task id
            details.
        """
        self.log("Deleting path trace flow analysis id: {0}".format(str(flow_id)), "INFO")
        try:
            response = self.dnac._exec(
                family="path_trace",
                function="deletes_pathtrace_by_id",
                params=dict(flow_analysis_id=flow_id)
            )
            self.log("Response from delete path trace API: {0}".format(
                self.pprint(response)), "DEBUG")
            if response and isinstance(response, dict):
                task_id = response.get("response", {}).get("taskId")
                if task_id:
                    self.log("Received the task id: {0}".format(task_id), "INFO")
                    dnac_api_task_timeout = int(self.payload.get("dnac_api_task_timeout"))
                    resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))

                    while dnac_api_task_timeout:
                        delete_details = self.get_task_details_by_id(task_id)
                        if delete_details.get("progress"):
                            return delete_details

                        time.sleep(resync_retry_interval)
                        dnac_api_task_timeout = dnac_api_task_timeout - resync_retry_interval
                else:
                    self.msg = "Unable to delete path trace for the flow analysis id: {0}".format(
                        flow_id)
                    self.not_processed.append(self.msg)
                    self.set_operation_result("failed", False, self.msg,
                                              "ERROR").check_return_status()

        except Exception as e:
            self.msg = 'An error occurred during delete path trace: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def get_diff_merged(self, config):
        """
        Create the path trace in Cisco Catalyst Center based on the playbook details

        Parameters:
            config (list of dict) - Playbook details containing path trace information.

        Returns:
            self - The current object Path create response information.
        """
        self.msg = ""
        self.changed = False
        self.status = "failed"

        assurance_pathtrace = config.get("assurance_pathtrace")
        if assurance_pathtrace is not None and len(assurance_pathtrace) > 0:
            for each_path in assurance_pathtrace:
                flow_analysis_id = each_path.get("flow_analysis_id")
                if not flow_analysis_id:
                    flow_analysis_id = self.create_path_trace(each_path)

                if flow_analysis_id:
                    path_trace = self.get_path_trace_with_flow_id(flow_analysis_id)
                    self.create_path.append(path_trace)
                else:
                    self.not_processed.append(config)
                    self.msg = self.msg + "Unable to create below path '{0}'.".format(
                        str(self.not_processed))

            if len(self.create_path) > 0:
                self.msg = "Path trace created successfully for '{0}'.".format(
                    str(self.create_path))
                self.changed = True
                self.status = "success"

            if len(self.not_processed) > 0:
                self.msg = self.msg + "Unable to create below path '{0}'.".format(
                    str(self.not_processed))

        self.log(self.msg, "INFO")
        self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                                  self.create_path).check_return_status()
        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing path trace.

        Returns:
            self - The current object path trace information.
        """
        if config:
            path_trace = config.get("assurance_pathtrace")
            if path_trace is not None:
                self.msg = ""
                success_path = []

                for each_path in path_trace:
                    if len(self.create_path) > 0:
                        for each_trace in self.create_path:
                            trace_source_ip = each_trace.get("request").get("sourceIP")
                            trace_dest_ip = each_trace.get("request").get("destIP")
                            flow_id = each_trace.get("request").get("id")
                            if each_path.get("flow_analysis_id") and \
                                each_path.get("flow_analysis_id") == flow_id:
                                success_path.append(each_path)
                            elif trace_source_ip == each_path["source_ip"] and \
                                trace_dest_ip == each_path["dest_ip"]:
                                success_path.append(each_path)

                if len(success_path) > 0:
                    self.msg = "Path trace created and verified successfully for '{0}'.".format(
                        str(success_path))

                if len(self.not_processed) > 0:
                    self.msg = self.msg + "\n Unable to create below path '{0}'.".format(
                        str(self.not_processed))

                self.log(self.msg, "INFO")
                if (len(success_path) > 0 and len(self.not_processed) > 0) or (
                    len(success_path) > 0 and len(self.not_processed) == 0):
                    self.set_operation_result("success", True, self.msg, "INFO",
                                              self.create_path).check_return_status()
                else:
                    self.set_operation_result("failed", False, self.msg, "ERROR",
                                              self.not_processed).check_return_status()

            return self

    def get_diff_deleted(self, config):
        """
        Delete path trace based on flow analysis id.

        Parameters:
            config (list of dict) - Playbook details containing path trace information.

        Returns:
            self - The current object with status of path trace deleted.
        """
        path_trace = config.get("assurance_pathtrace")
        if path_trace is not None and len(path_trace) > 0:
            for each_path in path_trace:
                get_trace = self.get_path_trace(each_path)

                if len(get_trace) > 0:
                    flow_ids = []
                    for each_trace in get_trace:
                        delete_response = self.delete_path_trace(each_trace["id"])
                        if delete_response:
                            flow_ids.append(delete_response)

                    if len(get_trace) == len(flow_ids):
                        self.delete_path.append(each_path)
                    else:
                        self.not_processed.append(each_path)

            if len(self.delete_path) > 0:
                self.msg = "Path trace deleted successfully for '{0}'.".format(
                    str(self.delete_path))

            if len(self.not_processed) > 0:
                self.msg = self.msg + "Unable to delete below path '{0}'.".format(
                    str(self.not_processed))

            self.log(self.msg, "INFO")
            if (len(self.delete_path) > 0 and len(self.not_processed) > 0) or (
                len(self.delete_path) > 0 and len(self.not_processed) == 0):
                self.set_operation_result("success", True, self.msg, "INFO",
                                          self.delete_path).check_return_status()
            else:
                self.set_operation_result("failed", False, self.msg, "ERROR",
                                            self.not_processed).check_return_status()

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the path trace was deleted

        Parameters:
            config (dict) - Playbook config contains path trace.

        Returns:
            self - Return response as verified that path trace was deleted.
        """
        path_trace = config.get("assurance_pathtrace")
        if path_trace is not None:
            self.get_have(config)
            self.log("Get have function response {0}".format(
                self.have["assurance_pathtrace"]), "INFO")
            if len(self.have["assurance_pathtrace"]) > 0:
                self.msg = "Unable to delete below path '{0}'.".format(
                    self.have["assurance_pathtrace"])
            else:
                self.msg = "Path trace deleted and verified successfully for '{0}'.".format(
                    path_trace)

            self.log(self.msg, "INFO")
            self.set_operation_result("success", True, self.msg, "INFO").check_return_status()

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
        "config_verify": {"type": 'bool', "default": False},
        "dnac_api_task_timeout": {"type": 'int', "default": 1200},
        "dnac_task_poll_interval": {"type": 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_assurance = PathTraceSettings(module)
    state = ccc_assurance.params.get("state")

    if ccc_assurance.compare_dnac_versions(ccc_assurance.get_ccc_version(), "2.3.7.6") < 0:
        ccc_assurance.status = "failed"
        ccc_assurance.msg = (
            "The specified version '{0}' does not support the path trace workflow feature."
            "Supported version(s) start from '2.3.7.6' onwards.".
            format(ccc_assurance.get_ccc_version())
        )
        ccc_assurance.log(ccc_assurance.msg, "ERROR")
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

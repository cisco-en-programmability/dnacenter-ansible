#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on Assurance issue settings in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["A Mohamed Rafeek, Megha Kandari, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: assurance_issue_settings_workflow_manager
short_description: Resource module for managing assurance settings and issue resolution in Cisco Catalyst Center
description:
  - This module allows the management of assurance settings and issues in Cisco DNA Center.
  - It supports creating, updating, and deleting configurations for issue settings and issue resolution functionalities.
  - This module interacts with Cisco DNA Center's Assurance settings to configure thresholds, rules, KPIs, and more for issue settings and issue resolution.
version_added: '6.25.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Megha Kandari (@mekandar)
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description: >
      Set to `True` to enable configuration verification on Cisco DNA Center after applying the playbook config.
      This will ensure that the system validates the configuration state after the change is applied.
    type: bool
    default: False
  state:
    description: >
      Specifies the desired state for the configuration.
      If `merged`, the module will create or update the configuration, adding new settings or modifying existing ones.
      If `deleted`, it will remove the specified settings.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description: >
      A list of settings and parameters to be applied.
      It consists of different sub-configurations for managing assurance settings such as issue settings,
      health score, ICAP settings, issue resolution, and command execution.
    type: list
    elements: dict
    required: true
    suboptions:
      assurance_user_defined_issue_settings:
        description: >
          Manages the issue settings for assurance in Cisco DNA Center.
          You can configure the name, description, severity, priority, and rules that govern network issues.
        type: list
        elements: dict
        suboptions:
          name:
            description: >
              The name of the issue setting, used for identification in the system.
              Required when creating a new setting or updating an existing one.
            type: str
            required: true
          description:
            description: >
              A text description for the issue. Helps to explain the nature of the issue for clarity in reports and dashboards.
            type: str
          rules:
            description: >
              A set of rules that define the parameters for triggering the issue.
              It includes severity, facility, mnemonic, pattern, occurrences, and duration.
            type: list
            elements: dict
            suboptions:
              severity:
                description: >
                  The severity level of the issue. Common values are 1 (Critical) to 5 (Informational).
                type: int
              facility:
                description: >
                  The facility type that the rule applies to. This could refer to a system component like redundancy or power.
                type: str
              mnemonic:
                description: >
                  A mnemonic value representing the issue, which could be a system-generated identifier or label for the issue.
                type: str
              pattern:
                description: >
                  The pattern or regular expression used to detect the issue.
                type: str
              occurrences:
                description: >
                  The number of times the issue pattern must occur to trigger the issue.
                type: int
              duration_in_minutes:
                description: >
                  The duration, in minutes, for which the issue pattern must persist to be considered valid.
                type: int
          is_enabled:
            description: >
              Boolean value to enable or disable the issue setting.
            type: bool
          priority:
            description: >
              Specifies the priority of the issue. Typically, values are "P1", "P2", "P3", etc.
            type: str
          is_notification_enabled:
            description: >
              Boolean value to specify if notifications for this issue setting should be enabled.
            type: bool
          prev_name:
            description: >
              The previous name of the issue setting (used when updating an existing issue setting).
            type: str
requirements:
  - dnacentersdk >= 2.10.0
  - python >= 3.9

notes:
  - SDK Methods used are
      issues.AssuranceSettings.get_all_the_custom_issue_definitions_based_on_the_given_filters
      issues.AssuranceSettings.creates_a_new_user_defined_issue_definitions
      issues.AssuranceSettings.deletes_an_existing_custom_issue_definition
      issues.AssuranceSettings.resolve_the_given_lists_of_issues
      issues.AssuranceSettings.ignore_the_given_list_of_issues
      issues.AssuranceSettings.execute_suggested_action_commands

  - Paths used are
      POST /dna/intent/api/api/v1/customIssueDefinitions
      POST /dna/intent/api/v1/assuranceIssues/resolve
      POST /dna/intent/api/v1/execute-suggested-actions-commands
      POST /dna/intent/api/v1/assuranceIssues/ignore
      POST /dna/intent/api/v1/flow-analysis/${flowAnalysisId}
      POST /dna/intent/api/v1/flow-analysis
      PUT /dna/intent/api/v1/systemIssueDefinitions/${id}
      DELETE /dna/intent/api/v1/flow-analysis/{flowAnalysisId}
      DELETE /dna/intent/api/v1/customIssueDefinitions/{id}
"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  connection: local
  tasks:
    - name: Create issue settings
      cisco.dnac.assurance_issue_settings_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: True
        dnac_log_level: DEBUG
        dnac_log_append: True
        state: merged
        config_verify: True
        config:
        - assurance_user_defined_issue_settings:
          - name: test
            description: testing
            rules:
              - severity: 5
                facility: redundancy
                mnemonic: peer monitor event
                pattern: issue test
                occurrences: 1
                duration_in_minutes: 2
            is_enabled: false
            priority: P1
            is_notification_enabled: false

    - name: update issue settings
      cisco.dnac.assurance_issue_settings_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: True
        dnac_log_level: DEBUG
        dnac_log_append: True
        state: merged
        config_verify: True
        config:
        - assurance_user_defined_issue_settings:
          - prv_name: test
            name: test issue
            description: testing
            rules:
              - severity: 5
                facility: redundancy
                mnemonic: peer monitor event
                pattern: issue test
                occurrences: 1
                duration_in_minutes: 2
            is_enabled: false
            priority: P1
            is_notification_enabled: false

    - name: Delete issue settings
      cisco.dnac.assurance_issue_settings_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log_level: DEBUG
        dnac_log: True
        state: deleted
        config_verify: True
        config:
        - assurance_user_defined_issue_settings:
          - name: test

- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  connection: local
  tasks:
    - name: Update System issue
      cisco.dnac.assurance_issue_settings_workflow_manager:
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
          - assurance_system_issue_settings:
            - name: "test"
              synchronizeToHealthThreshold: false
              priority: "P2"
              issueEnabled: true
              thresholdValue: "90"

- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  connection: local
  tasks:
    - name: Resolving Issues
      cisco.dnac.assurance_issue_settings_workflow_manager:
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
          - assurance_issue:
            - issue_name: NewTest17Dec # required field
              issue_process_type: resolution # required field
              start_datetime: "2024-12-11 16:00:00" # optional field
              end_datetime: "2024-12-11 18:30:00" # optional field
              site_hierarchy: Global/USA/San Jose/BLDG23 # optional field
              device_name: NY-EN-9300.cisco.local # optional field
              priority: P4 # optional field
              issue_status: ACTIVE # optional field
              mac_address: e4:38:7e:42:bc:40 # optional field
              network_device_ip_address: 204.1.2.4 # optional field

    - name: Ignoring issues
      cisco.dnac.assurance_issue_settings_workflow_manager:
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
          - assurance_issue:
            - issue_name: NewTest17Dec # required field
              issue_process_type: ignore # required field
              start_datetime: "2024-12-11 16:00:00" # optional field
              end_datetime: "2024-12-11 18:30:00" # optional field
              site_hierarchy: Global/USA/San Jose/BLDG23 # optional field
              device_name: NY-EN-9300.cisco.local # optional field
              priority: P4 # optional field
              issue_status: ACTIVE # optional field
              mac_address: e4:38:7e:42:bc:40 # optional field
              network_device_ip_address: 204.1.2.4 # optional field

    - name: Execute suggested commands
      cisco.dnac.assurance_issue_settings_workflow_manager:
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
          - assurance_issue:
            - issue_name: NewTest17Dec # required field
              issue_process_type: command_execution # required field
              start_datetime: "2024-12-11 16:00:00" # optional field
              end_datetime: "2024-12-11 18:30:00" # optional field
              site_hierarchy: Global/USA/San Jose/BLDG23 # optional field
              device_name: NY-EN-9300.cisco.local # optional field
              priority: P4 # optional field
              issue_status: ACTIVE # optional field
              mac_address: e4:38:7e:42:bc:40 # optional field
              network_device_ip_address: 204.1.2.4 # optional field
     """

RETURN = r"""

#Case 1: Successful creation of issue
response_create:
  description: Details of the response returned by the assurance settings create API.
  returned: always
  type: dict
  sample: {
      "response": {
          "id": "string",
          "name": "string",
          "description": "string",
          "profileId": "string",
          "triggerId": "string",
          "rules": [
              {
                  "type": "string",
                  "severity": 1,
                  "facility": "string",
                  "mnemonic": "string",
                  "pattern": "string",
                  "occurrences": 3,
                  "durationInMinutes": 15
              }
          ],
          "isEnabled": true,
          "priority": "P1",
          "isDeletable": true,
          "isNotificationEnabled": true,
          "createdTime": 1672531200,
          "lastUpdatedTime": 1672617600
      }
  }


#Case 2: Successful updation of issue
response_update:
  description: Details of the response returned by the assurance settings update API.
  returned: always
  type: dict
  sample: {
      "response": {
          "id": "string",
          "name": "string",
          "description": "string",
          "profileId": "string",
          "triggerId": "string",
          "rules": [
              {
                  "type": "string",
                  "severity": 1,
                  "facility": "string",
                  "mnemonic": "string",
                  "pattern": "string",
                  "occurrences": 5,
                  "durationInMinutes": 10
              }
          ],
          "isEnabled": true,
          "priority": "P1",
          "isDeletable": true,
          "isNotificationEnabled": true,
          "createdTime": 1672531200,
          "lastUpdatedTime": 1672617600
      }
  }

#Case 3: Successfully Resolved issue
response_resolved:
  description: The response after resolving issues in Cisco DNA Center.
  returned: always
  type: dict
  sample: {
      "response": {
          "successfulIssueIds": [
              "string"
          ],
          "failureIssueIds": [
              "string"
          ]
      },
      "version": "string"
  }

#Case 4: Successfully ignored issue
Response_ignore:
  description: The response after ignoring issues in Cisco DNA Center.
  returned: always
  type: dict
  sample: {
      "response": {
          "successfulIssueIds": [
              "string"
          ],
          "failureIssueIds": [
              "string"
          ]
      },
      "version": "string"
  }

#Case 5: Successfully executed commands of issue
Response:
  description: The response object containing execution details of suggested action commands.
  returned: always
  type: list
  elements: dict
  sample: [
      {
          "bapiExecutionId": "f0c5d185-50bf-4abd-b9b0-235f49fdd4e7",
          "bapiKey": "cfb2-ab10-4cea-bfbb",
          "bapiName": "Execute Suggested Actions Commands",
          "bapiSyncResponse": "[{\"actionInfo\":\"Cisco Catalyst Center Suggested Action 1: Check redundant power status\",
          \"stepsCount\":1,\"entityId\":\"e62e6405-13e4-4f1b-ae1c-580a28a96a88\",\"hostname\":\"SJ-BN-9300.cisco.local\",
          \"stepsDescription\":\"Check system power status\",\"command\":\"show environment power all\",\"commandOutput\"
          :{\"show environment power all\":\"show environment power all\\nSW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
          \\n--  ------------------  ----------  ---------------  -------  -------  -----\\n1A  PWR-C1-1100WAC-P    QCS23253F1Y
          OK              Good     Good     1100\\n1B  Unknown             Unknown      No Input Power  Bad      Bad      Unknown    \\n\\nSJ-BN-9300#\"}}]",
          "bapiSyncResponseJson": [
              {
                  "actionInfo": "Cisco Catalyst Center Suggested Action 1: Check redundant power status",
                  "command": "show environment power all",
                  "commandOutput": {
                      "show environment power all": "show environment power all\nSW  PID
                      Serial#     Status           Sys Pwr  PoE Pwr  Watts\n--  ------------------  ----------  ---------------  -------  -------  -----\n1A
                      PWR-C1-1100WAC-P    QCS23253F1Y  OK              Good     Good     1100\n1B  Unknown             Unknown      No Input Power  Bad
                      Bad      Unknown    \n\nSJ-BN-9300#"
                  },
                  "entityId": "e62e6405-13e4-4f1b-ae1c-580a28a96a88",
                  "hostname": "SJ-BN-9300.cisco.local",
                  "stepsCount": 1,
                  "stepsDescription": "Check system power status"
              }
          ],
          "endTime": "Fri Dec 20 10:04:08 UTC 2024",
          "endTimeEpoch": 1734689048935,
          "runtimeInstanceId": "DNACP_Runtime_b0c741ca-0823-4a02-bbd9-83aa5c68950f",
          "startTime": "Fri Dec 20 10:03:57 UTC 2024",
          "startTimeEpoch": 1734689037146,
          "status": "SUCCESS",
          "timeDuration": 11789
      }
  ]

#Case 6: Successfully updated System issue
response_update_system_issue:
  description: The response object containing detailed information about the issue or configuration.
  returned: always
  type: dict
  sample: {
      "response": {
          "id": "string",
          "name": "string",
          "displayName": "string",
          "description": "string",
          "priority": "string",
          "defaultPriority": "string",
          "deviceType": "string",
          "issueEnabled": "boolean",
          "profileId": "string",
          "definitionStatus": "string",
          "categoryName": "string",
          "synchronizeToHealthThreshold": "boolean",
          "thresholdValue": "number",
          "lastModified": "string"
      }
  }
"""

import re
import time
from datetime import datetime
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    validate_str,
)


class AssuranceSettings(DnacBase):
    """Class containing member attributes for Assurance setting workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = [
            {"assurance_user_defined_issue_settings": {"response": {}, "msg": {}}},
            {"assurance_system_issue_settings": {"response": {}, "msg": {}}}
        ]
        self.user_defined_issue_obj_params = self.assurance_obj_params("assurance_user_defined_issue_settings")
        self.system_issue_obj_params = self.assurance_obj_params("assurance_system_issue_settings")
        self.supported_states = ["merged", "deleted"]
        self.create_issue, self.update_issue, self.no_update_issue = [], [], []
        self.issue_resolved, self.issue_ignored, self.issues_active = [], [], []
        self.success_list_resolved, self.failed_list_resolved = [], []
        self.success_list_ignored, self.failed_list_ignored = [], []
        self.cmd_executed, self.cmd_not_executed, self.issue_processed = [], [], []
        self.keymap = dict(
            source_ip="sourceIP",
            dest_ip="destIP",
            control_path="controlPath",
            dest_port="destPort",
            source_port="sourcePort",
            periodic_refresh="periodicRefresh",
            Interface="INTERFACE-STATS",
            QoS="QOS-STATS",
            Device="DEVICE-STATS",
            Performance="PERFORMANCE-STATS",
            ACL_Trace="ACL-TRACE",
            issue_name="name",
            start_datetime="start_time",
            end_datetime="end_time",
            site_hierarchy="site_id",
            device_id="device_id",
            mac_address="mac_address",
            issue_status="issue_status",
            network_device_ip_address="management_ip_address",
            device_name="hostname"
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

        # Specification for validation
        temp_spec = {
            'assurance_user_defined_issue_settings': {
                'type': 'list',
                'elements': 'dict',
                'name': {'type': 'str', 'required': True},
                'description': {'type': 'str'},
                'rules': {
                    'type': 'list',
                    'elements': 'dict',
                    'severity': {'type': 'int', 'choices': [0, 1, 2, 3, 4, 5, 6], 'required': True},
                    'facility': {'type': 'str'},
                    'mnemonic': {'type': 'str'},
                    'pattern': {'type': 'str', 'required': True},
                    'occurrences': {'type': 'int'},
                    'duration_in_minutes': {'type': 'int'}
                },
                'is_enabled': {'type': 'bool', 'default': True},
                'priority': {'type': 'str', 'choices': ['P1', 'P2', 'P3', 'P4']},
                'is_notification_enabled': {'type': 'bool', 'default': False},
                'prev_name': {'type': 'str'}
            },
            'assurance_issue': {
                'type': 'list',
                'elements': 'dict',
                'issue_name': {'type': 'str', 'required': True},
                'issue_process_type': {'type': 'str',
                                       'choices': ['resolution', 'ignore', 'command_execution'],
                                       'required': True},
                'start_datetime': {'type': 'str', 'required': False},
                'end_datetime': {'type': 'str', 'required': False},
                'site_hierarchy': {'type': 'str', 'required': False},
                'device_name': {'type': 'str', 'required': False},
                'priority': {'type': 'str', 'choices': ['P1', 'P2', 'P3', 'P4'],
                             'required': False},
                'issue_status': {'type': 'str',
                                 'choices': ['ACTIVE', 'RESOLVED', 'IGNORED'],
                                 'required': False},
                'network_device_ip_address': {'type': 'str', 'required': False},
                'mac_address': {'type': 'str', 'required': False}
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
            self.result['response'] = self.msg
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
            config (dict): Dictionary containing the input assurance details.

        Returns:
            list: List of invalid assurance data with details.

        Description:
            Iterates through available assurance data and Returns the list of invalid assurance
            data for further action or validation.
        """
        errormsg = []

        assurance_issue = config.get("assurance_issue")
        if assurance_issue and len(assurance_issue) > 0:
            for each_issue in assurance_issue:
                issue_name = each_issue.get("issue_name")
                if issue_name:
                    param_spec = dict(type="str", length_max=100)
                    validate_str(issue_name, param_spec, "issue_name", errormsg)
                else:
                    errormsg.append("issue_name: Issue Name is missing in playbook.")

                issue_process_type = each_issue.get("issue_process_type")
                issue_type = ("resolution", "ignore", "command_execution")
                if issue_process_type:
                    if issue_process_type not in issue_type:
                        errormsg.append("issue_process_type: Invalid issue process type '{0}' in playbook. "
                                        "Must be one of: {1}.".format(issue_process_type, ", ".join(issue_type)))
                else:
                    errormsg.append("issue_process_type: issue process type is missing in playbook.")

                site_hierarchy = each_issue.get("site_hierarchy")
                if site_hierarchy:
                    param_spec = dict(type="str", length_max=300)
                    validate_str(site_hierarchy, param_spec, "site_hierarchy", errormsg)

                priority = each_issue.get("priority")
                priority_list = ("P1", "P2", "P3", "P4")
                if priority and priority not in priority_list:
                    errormsg.append("priority: Invalid Priority '{0}' in playbook. "
                                    "Must be one of: {1}.".format(priority, ", ".join(priority_list)))

                issue_status = each_issue.get("issue_status")
                status_list = ("ACTIVE", "RESOLVED", "IGNORED")
                if issue_status and issue_status not in status_list:
                    errormsg.append("issue_status: Invalid issue status '{0}' in playbook. "
                                    "Must be one of: {1}.".format(issue_status, ", ".join(status_list)))

                device_name = each_issue.get("device_name")
                if device_name:
                    param_spec = dict(type="str", length_max=200)
                    validate_str(device_name, param_spec, "device_name", errormsg)

                start_datetime = each_issue.get("start_datetime")
                if start_datetime:
                    param_spec = dict(type="str", length_max=20)
                    validate_str(start_datetime, param_spec, "start_datetime", errormsg)

                end_datetime = each_issue.get("end_datetime")
                if end_datetime:
                    param_spec = dict(type="str", length_max=20)
                    validate_str(end_datetime, param_spec, "end_datetime", errormsg)

                mac_address = each_issue.get("mac_address")
                if mac_address:
                    mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
                    if not mac_regex.match(mac_address):
                        errormsg.append("mac_address: Invalid MAC Address '{0}' in playbook.".format(
                            mac_address))

                network_device_ip_address = each_issue.get("network_device_ip_address")
                if network_device_ip_address and (
                    not self.is_valid_ipv4(network_device_ip_address) and
                    not self.is_valid_ipv6(network_device_ip_address)
                ):
                    errormsg.append("network_device_ip_address: Invalid Network device IP Address '{0}'\
                        in playbook.".format(network_device_ip_address))

                if start_datetime and end_datetime:
                    validated_datetime = self.validate_start_end_datetime(
                        start_datetime, end_datetime, errormsg)

        execute_commands = config.get("assurance_execute_suggested_commands")
        if execute_commands:
            for each_commands in execute_commands:
                entity_type = each_commands.get("entity_type")
                if entity_type:
                    param_spec = dict(type="str", length_max=255)
                    validate_str(entity_type, param_spec, "entity_type", errormsg)
                else:
                    errormsg.append("entity_type: Entity Type is missing in playbook.")

                entity_value = each_commands.get("entity_value")
                if entity_value:
                    param_spec = dict(type="str", length_max=255)
                    validate_str(entity_value, param_spec, "entity_value", errormsg)
                else:
                    errormsg.append("entity_value: Entity Value is missing in playbook.")

        # Facility and mnemonic mappings for severities 3, 4, 5, and 6
        facility_mnemonic_map = {
            # Severity 3 facilities and mnemonics
            3: {
                "SFF8472": ["THRESHOLD_VIOLATION"],
                "WLANMGR_TRACE_MESSAGE": ["EWLC_WLANMGR_SCHEDULED_WLAN_DISABLE", "EWLC_WLANMGR_SCHEDULED_WLAN_ENABLE"],
                "POWER_SUPPLIES": ["PWR_FAIL"],
                "CLIENT_ORCH_AUDIT_MESSAGE": ["FIPS_AUDIT_FTA_TSE1_DENY_CLIENT_ACCESS"],
                "BGP": ["NOTIFICATION"],
                "REDUNDANCY": ["PEER_MONITOR", "SWITCHOVER", "STANDBY_LOST"],
                "CI": ["PARTIAL_FAN_FAIL", "PARTFANFAIL", "PSFANFAIL"],
                "STANDBY": ["DUPADDR"],
                "IOSXE_PEM": ["PEMCHASFSERR", "PEMFAIL", "FAN_FAIL_SHUTDOWN", "FANFAIL"],
                "CMRP_ENVMON": ["TEMP_SYS_SHUTDOWN_PENDING", "TEMP_WARN_CRITICAL", "TEMP_FRU_SHUTDOWN_PENDING"]
            },
            # Severity 4 facilities and mnemonics
            4: {
                "LISP": [
                    "MAP_CACHE_WARNING_THRESHOLD_REACHED",
                    "LOCAL_EID_NO_ROUTE",
                    "LOCAL_EID_MAP_REGISTER_FAILURE",
                    "CEF_DISABLED",
                    "LOCAL_EID_RLOC_INCONSISTENCY"
                ],
                "PM": ["ERR_DISABLE"],
                "PLATFORM_STACKPOWER": [
                    "UNDER_BUDGET",
                    "VERSION_MISMATCH",
                    "TOO_MANY_ERRORS",
                    "INSUFFICIENT_PWR",
                    "REDUNDANCY_LOSS"
                ],
                "UDLD": ["UDLD_PORT_DISABLED"],
                "IP": ["DUPADDR"],
                "SW_MATM": ["MACFLAP_NOTIF"],
                "CMRP_PFU": ["PFU_FAN_WARN"],
                "C4K_IOSMODPORTMAN": [
                    "MODULETEMPHIGH",
                    "POWERSUPPLYBAD",
                    "CRITICALTEMP",
                    "MODULECRITICALTEMP",
                    "TEMPHIGH",
                    "FANTRAYREMOVED"
                ],
                "C6KENV": ["TERMINATOR_PS_TEMP_MAJORALARM"],
                "MAC_MOVE": ["NOTIF"]
            },
            # Severity 5 facilities and mnemonics
            5: {
                "SFF8472": ["THRESHOLD_VIOLATION"],
                "DUAL": ["NBRCHANGE"],
                "DMI": ["SYNC_NEEDED", "SYNC_START"],
                "BGP": ["ADJCHANGE"],
                "REDUNDANCY": ["PEER_MONITOR_EVENT"],
                "IFDAMP": ["UPDOWN"],
                "CAPWAPAC_SMGR_TRACE_MESSAGE": ["AP_JOIN_DISJOIN"],
                "OSPF": ["ADJCHG"],
                "DOT1X": ["SUCCESS", "FAIL"],
                "ILPOWER": ["ILPOWER_POWER_DENY"]
            },
            # Severity 6 facilities and mnemonics
            6: {
                "IOSXE_OIR": ["REMSPA", "INSSPA", "OFFLINECARD"],
                "TRANSCEIVER": ["REMOVED", "INSERTED"],
                "SMART_LIC": ["AGENT_READY", "HA_ROLE_CHANGED", "AGENT_ENABLED"],
                "STANDBY": ["STATECHANGE"],
                "IOSXE_PEM": ["REMPEM_FM", "FANOK", "PEMOK"],
                "PLATFORM_STACKPOWER": ["CABLE_EVENT", "LINK_EVENT"],
                "ENV_MON": ["REMPEM"],
                "PLATFORM": ["HASTATUS_DETAIL", "HASTATUS"],
                "IOSXE_INFRA": ["PROCPATH_CLIENT_HOG"],
                "STACKMGR": ["STACK_LINK_CHANGE"]
            }
        }

        global_issue = config.get("assurance_user_defined_issue_settings")
        if global_issue and len(global_issue) > 0:
            for each_issue in global_issue:
                priority = each_issue.get("priority")
                priority_list = ("P1", "P2", "P3", "P4")
                if priority and priority not in priority_list:
                    errormsg.append("priority: Invalid Priority '{0}' in playbook. "
                                    "Must be one of: {1}.".format(priority, ", ".join(priority_list)))

                rules = each_issue.get("rules", [])
                for rule in rules:
                    severity = rule.get("severity")
                    severity = int(severity)
                    if severity < 0 or severity > 6:
                        errormsg.append("severity: Invalid Severity '{0}' in playbook. "
                                        "Must be an integer between 0 and 6.".format(severity))

                    if severity in facility_mnemonic_map:
                        facility = rule.get("facility")
                        if facility not in facility_mnemonic_map[severity]:
                            errormsg.append("facility: Facility '{0}' must be selected from pre-defined list for severity {1}: {2}.".format(
                                facility, severity, ", ".join(facility_mnemonic_map[severity].keys())))
                        else:
                            mnemonic = rule.get("mnemonic")
                            valid_mnemonics = facility_mnemonic_map[severity][facility]
                            if mnemonic not in valid_mnemonics:
                                errormsg.append("mnemonic: Invalid Mnemonic '{0}' for Facility '{1}' and Severity '{2}'. "
                                                "Must be one of: {3}.".format(mnemonic, facility, severity, ", ".join(valid_mnemonics)))

                    duration = rule.get("duration_in_minutes")
                    duration = int(duration)
                    if duration < 1 or duration > 15:
                        errormsg.append("duration_in_minutes: Invalid duration '{0}' in playbook. "
                                        "Must be an integer between 1 and 15.".format(duration))

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: '{0}' ".format(errormsg)
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.msg = "Successfully validated config params: {0}".format(str(config))
        self.log(self.msg, "INFO")
        return self

    def validate_start_end_datetime(self, start_time, end_time, errormsg):
        """
        Validate the start and end Date time param from the input playbook
        """
        date_format = "%Y-%m-%d %H:%M:%S"

        try:
            start_datetime = datetime.strptime(start_time, date_format)
            end_datetime = datetime.strptime(end_time, date_format)

            if start_datetime > end_datetime:
                errormsg.append("Start date time must be before end date time.")

            start_epoch_ms = int(start_datetime.timestamp() * 1000)
            end_epoch_ms = int(end_datetime.timestamp() * 1000)

            return start_epoch_ms, end_epoch_ms
        except ValueError as e:
            errormsg.append("Unable to validate Start date time, end date time. {0}".format(str(e)))
            return None

    def get_device_details(self, config):
        """
        get device id and mac address based on the device name.
        """
        input_param = {}
        for key in ["mac_address", "network_device_ip_address", "device_name"]:
            if config.get(key):
                input_param[self.keymap[key]] = config[key]
                break

        if not input_param:
            return None

        self.log("Input payload for the Device info: {0}".format(input_param), "INFO")
        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                params=input_param,
            )
            self.log("Response from the Device info: {0}".format(
                self.pprint(response)), "INFO")

            response_data = response.get("response") if response else None

            if response_data:
                device_response = self.camel_to_snake_case(response_data)
                return device_response[0]

        except Exception as e:
            self.msg = "The provided device '{0}' is either invalid or not present in the \
                     Cisco Catalyst Center.".format(str(input_param))
            self.log(self.msg + str(e), "WARNING")
            return None

        return self

    def assurance_obj_params(self, get_object):
        """
        Get the required comparison obj_params value

        Parameters:
            get_object (str) - identifier for the required obj_params

        Returns:
            obj_params (list) - obj_params value for comparison.
        """

        try:
            if get_object == "assurance_user_defined_issue_settings":
                obj_params = [
                    ("name", "name"),
                    ("description", "description"),
                    ("rules", "rules"),
                    ("is_enabled", "is_enabled"),
                    ("priority", "priority"),
                    ("is_notification_enabled", "is_notification_enabled")
                ]
            elif get_object == "assurance_system_issue_settings":
                obj_params = [
                    ("synchronizeToHealthThreshold", "synchronize_to_health_threshold"),
                    ("priority", "priority"),
                    ("issueEnabled", "issue_enabled"),
                    ("thresholdValue", "threshold_value"),
                ]
            else:
                raise ValueError("Received an unexpected value for 'get_object': {0}"
                                 .format(get_object))
        except Exception as msg:
            self.log("Received exception: {0}".format(msg), "CRITICAL")

        return obj_params

    def get_want(self, config):
        """
        Retrieve and store import, tagging, distribution, and activation details from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.
        Raises:
            AnsibleFailJson: If an incorrect import type is specified.
        Description:
            This function parses the playbook configuration to extract information related to image
            import, tagging, distribution, and activation. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """
        self.log(config)
        want = {}
        want["assurance_user_defined_issue_settings"] = config.get("assurance_user_defined_issue_settings")
        want["assurance_system_issue_settings"] = config.get("assurance_system_issue_settings")
        want["assurance_issue_resolution"] = config.get("assurance_issue_resolution")
        want["assurance_ignore_issue"] = config.get("assurance_ignore_issue")
        want["assurance_execute_suggested_commands"] = config.get("assurance_execute_suggested_commands")

        if want.get("assurance_user_defined_issue_settings"):
            for issue_setting in want.get("assurance_user_defined_issue_settings", []):
                for rule in issue_setting.get("rules", []):
                    if "occurrences" not in rule:
                        rule["occurrences"] = 1

                    if "severity" in rule:
                        rule["severity"] = str(want.get("assurance_user_defined_issue_settings")[0].get("rules")[0].get("severity"))

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_have(self, config):
        """
        Get the current Global Pool Reserved Pool and Network details from Cisco Catalyst Center

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self - The current object with updated Global Pool,
            Reserved Pool, and Network information.
        """
        assurance_user_defined_issue_details = config.get("assurance_user_defined_issue_settings")
        assurance_system_issue_details = config.get("assurance_system_issue_settings")

        if assurance_user_defined_issue_details is not None:
            self.get_have_assurance_user_issue(assurance_user_defined_issue_details).check_return_status()

        if assurance_system_issue_details is not None:
            self.get_have_assurance_system_issue(assurance_system_issue_details).check_return_status()

        self.have["assurance_issue_resolution"] = config.get("assurance_issue_resolution")

        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        self.status = "success"
        return self

    def get_system_issue_details(self, device_type):
        """
        Get system issue details from Cisco Catalyst Center based on the provided device type.
        This function retrieves all issues for the given device type and matches the displayName with the playbook.

        Parameters:
            device_type (str) - The device type to filter system issues by (e.g., APPLICATION, NETWORK).

        Returns:
            matching_system_issues (list) - A list of system issues that match the device type and displayName.
        """
        matching_system_issues = []
        total_response = []
        try:
            for issue_enabled in ['true', 'false']:
                response = self.dnac._exec(
                    family="issues",
                    function="returns_all_issue_trigger_definitions_for_given_filters",
                    params={'deviceType': device_type, 'issueEnabled': issue_enabled}
                )
                total_response.append(response.get("response"))
            self.log("Response from returns_all_issue_trigger_definitions_for_given_filters API:'{0}'".format(self.pprint(total_response)), "DEBUG")

            total_response = total_response[0] + total_response[1]

            if not total_response:
                raise Exception("No system issue details found for device type '{0}'.".format(device_type))

            return total_response

        except Exception as e:
            self.status = "failed"
            self.msg = "Failed to retrieve system issue details for device type '{0}': {1}".format(device_type, str(e))
            self.log(self.msg, "ERROR")
            return matching_system_issues

    def get_have_assurance_system_issue(self, assurance_system_issue_details):
        """
        Get the current System Defined Issues information from Cisco Catalyst Center
        based on the provided playbook details. This method collects and updates
        the issues based on device type and name from the playbook.

        Parameters:
            assurance_system_issue_details (dict) - Playbook details containing System Defined Issue configuration.

        Returns:
            self - The current object with updated system issue details.
        """
        Assurance_system_issues = []

        for issue_setting in assurance_system_issue_details:
            name = issue_setting.get("name")
            device_type = issue_setting.get("device_type")
            description = issue_setting.get("description")

            if not name:
                self.msg = "Missing required parameter 'name' in assurance_system_issue_details"
                self.status = "failed"
                self.log(self.msg, "ERROR")
                return self

            if not device_type:
                self.msg = "Missing required parameter 'device_type' in assurance_system_issue_details"
                self.status = "failed"
                self.log(self.msg, "ERROR")
                return self

            system_issues = self.get_system_issue_details(device_type)
            # system_issues = system_issues[0] + system_issues[1]

            if not system_issues:
                self.msg = "System issue details for '{0}' could not be retrieved.".format(name)
                self.status = "failed"
                self.log(self.msg, "ERROR")
                return self

            matching_issues = []
            for issue in system_issues:
                if issue.get("displayName") == name and (not description or issue.get("description") == description):
                    matching_issues.append(issue)

            if not matching_issues:
                self.msg = "No system issues with displayName '{0}' found for device type '{1}'.".format(name, device_type)
                self.status = "failed"
                self.log(self.msg, "ERROR")
                return self

            for issue in matching_issues:
                Assurance_system_issues.append(issue)
                self.log("System issue details for '{0}': {1}".format(name, issue), "DEBUG")

        self.have.update({"assurance_system_issue_settings": Assurance_system_issues})
        self.msg = "Successfully retrieved and updated system issue details from Cisco Catalyst Center."
        self.status = "success"

        return self

    def assurance_issues_exists(self, name):
        """
        Check if the Assurance issues with the given name exists

        Parameters:
            name (str) - The name of the Assurance issues to check for existence

        Returns:
            dict - A dictionary containing information about the Assurance Issue's existence:
            - 'exists' (bool): True if the Assurance issues exists, False otherwise.
            - 'id' (str or None): The ID of the Assurance Issue if it exists, or None if it doesn't.
            - 'details' (dict or None): Details of the Assurance Issue if it exists, else None.
        """
        self.log(name)
        assurance_issue = {
            "exists": False,
            "assurance_issue_details": None,
            "id": None
        }
        value = 1
        while True:
            try:
                response = self.dnac._exec(
                    family="issues",
                    function="get_all_the_custom_issue_definitions_based_on_the_given_filters",
                    params={"name": name}
                )
            except Exception as msg:
                match = re.search(r'status_code:\s*(\d+)', str(msg))
                if match and int(match.group(1)) == 404:
                    return {'response': [], 'exists': False, 'message': 'There is no assurance issue present in the system for the given input.'}

                else:
                    self.msg = (
                        "Exception occurred while getting the assurance issue details with name '{name}': {msg}" .format(
                            name=name, msg=msg))
                    self.log(str(msg), "ERROR")
                    self.status = "failed"
                    return self

            if not isinstance(response, dict):
                self.msg = "Failed to retrieve the assurance issue details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            all_user_issue_details = response.get("response")
            if all_user_issue_details == []:
                return {'response': [], 'exists': False, 'message': 'There is no assurance issue present in the system for the given input.'}

            all_assurance_issue_details = []
            for issue_detail in all_user_issue_details:
                rules = issue_detail.get("rules", [])
                for rule in rules:
                    rule["duration_in_minutes"] = rule.pop("durationInMinutes", None)
                    rule.pop("type")
                transformed_detail = {
                    "is_enabled": issue_detail.pop("isEnabled", None),
                    "is_notification_enabled": issue_detail.pop("isNotificationEnabled", None),
                    "rules": rules,
                    **issue_detail
                }
                all_assurance_issue_details.append(transformed_detail)

            self.log(all_assurance_issue_details)

            assurance_issue_details = get_dict_result(
                all_assurance_issue_details, "user_issue", name)

            if assurance_issue_details:
                self.log("Assurance issue found with name '{0}': {1}".format(
                    name, assurance_issue_details), "INFO")
                assurance_issue.update({"exists": True})
                assurance_issue.update({"id": assurance_issue_details.get("id")})
                assurance_issue["assurance_issue_details"] = assurance_issue_details
                break

        self.log("Formatted assurance issue details: {0}".format(
            assurance_issue), "DEBUG")
        return assurance_issue

    def get_have_assurance_user_issue(self, assurance_user_defined_issue_settings):
        """
        Get the current Assurance Issue information from
        Cisco Catalyst Center based on the provided playbook details.
        check this API using check_return_status.

        Parameters:
            assurance_issue_details (dict) - Playbook details containing Assurance Issue configuration.

        Returns:
            self - The current object with updated information.
        """
        Assurance_issue = []
        Assurance_issue_index = 0
        for issues_setting in assurance_user_defined_issue_settings:
            name = issues_setting.get("name")
            if name is None:
                self.msg = "Missing required parameter 'name' in assurance_user_defined_issue_settings"
                self.status = "failed"
                return self

            name_length = len(name)
            if name_length > 100:
                self.msg = "The length of the '{0}' in assurance_user_defined_issue_settings should be less or equal to 100. Invalid_config: {1}".format(
                    name, issues_setting)
                self.status = "failed"
                return self

            if " " in name:
                self.msg = "The 'name' in assurance_user_defined_issue_settings should not contain any spaces."
                self.status = "failed"
                return self

            pattern = r'^[\w\-./]+$'
            if not re.match(pattern, name):
                self.msg = "The 'name' in assurance_user_defined_issue_settings should contain only letters, numbers and -_./ characters."
                self.status = "failed"
                return self

            Assurance_issue.append(self.assurance_issues_exists(name))
            self.log("Assurance issue details of '{0}': {1}".format(
                name, Assurance_issue[Assurance_issue_index]), "DEBUG")
            prev_name = issues_setting.get("prev_name")
            if Assurance_issue[Assurance_issue_index].get("exists") is False and \
                    prev_name is not None:
                Assurance_issue.pop()
                Assurance_issue.append(self.assurance_issues_exists(prev_name))
                if Assurance_issue[Assurance_issue_index].get("exists") is False:
                    self.msg = "Prev name {0} doesn't exist in assurance_user_issue_details".format(
                        prev_name)
                    self.status = "failed"
                    return self

                Assurance_issue[Assurance_issue_index].update({"prev_name": name})
            Assurance_issue_index += 1

        self.log("Assurance issue details: {0}".format(Assurance_issue), "DEBUG")
        self.have.update({"assurance_user_defined_issue_settings": Assurance_issue})
        self.msg = "Collecting the assurance issue details from the Cisco Catalyst Center"
        return self

    def get_issue_ids_for_names(self, config_data, verify=None):
        """
        Get the issue ids from global or custom name.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config_data (dict): A dictionary containing input config data from playbook.

        Returns:
            list : Returns list of issue ids.

        Description:
            This function get the issue ids based on the issue name either global or custom
            issue name.
        """
        issue_keys = list(config_data.keys())

        if len(issue_keys) < 1:
            self.msg = "No aata available in the config input: {0}".format(str(config_data))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        payload_data = {}
        avoid_keys = ("site_hierarchy", "start_datetime", "end_datetime",
                      "issue_name", "network_device_ip_address", "device_name",
                      "issue_process_type")

        for key, value in config_data.items():
            if value is not None and key not in avoid_keys:
                mapped_key = self.keymap.get(key, key)
                payload_data[mapped_key] = value

        issue_ids = []

        site_name = config_data.get("site_hierarchy")
        if site_name:
            site_id = self.get_site_id(site_name)
            if site_id[0]:
                payload_data[self.keymap["site_hierarchy"]] = site_id[1]
            else:
                self.msg = "Unable to get the site details for given site: {0}".format(
                    str(site_name))
                self.log(self.msg, "INFO")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        start_date = config_data.get("start_datetime")
        end_date = config_data.get("end_datetime")
        if start_date and end_date:
            payload_data["start_time"], payload_data["end_time"] = self.validate_start_end_datetime(
                start_date, end_date, [])

        if config_data.get("device_name") or config_data.get("mac_address") or \
           config_data.get("network_device_ip_address"):
            device_info = self.get_device_details(config_data)

            if not device_info:
                self.msg = "Unable to get device info given device_name: {0}".format(
                    str(config_data.get("device_name")))
                self.log(self.msg, "INFO")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
            payload_data[self.keymap["mac_address"]] = device_info.get("mac_address")
            if payload_data.get(self.keymap["site_hierarchy"]):
                payload_data["deviceId"] = device_info.get("id")

        self.log("Collecting Issue ids for given config: {0}".format(
            self.pprint(payload_data)), "INFO")
        try:
            self.log("Getting issue ids for the names: {0}".format(
                self.pprint(payload_data)), "INFO")
            response = self.dnac._exec(
                family="issues",
                function="issues",
                params=payload_data
            )
            self.log("Response from the API: {0}".format(self.pprint(response)),
                     "INFO")

            if response and isinstance(response, dict):
                all_issues = response.get("response")
                if isinstance(all_issues, list) and len(all_issues) > 0:
                    start_time = payload_data.get("start_time")
                    end_time = payload_data.get("end_time")
                    if start_time and end_time:
                        issue_ids = ([issue["issueId"] for issue in all_issues
                                     if (issue["name"] == config_data.get("issue_name")) and
                                     (start_time <= issue["last_occurence_time"] <= end_time)])
                    else:
                        issue_ids = ([issue["issueId"] for issue in all_issues
                                     if issue["name"] == config_data.get("issue_name")])
            else:
                self.msg = "No data received for the issue: {0}".format(str(payload_data))
                self.log(self.msg, "INFO")

        except Exception as e:
            self.msg = 'An error occurred during get issue ids : {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")

        issue_ids = list(set(issue_ids))
        if len(issue_ids) > 0:
            self.msg = "Find the list of issue ids: {0}".format(self.pprint(issue_ids))
            self.log(self.msg, "INFO")
            return issue_ids

        self.msg = "No data received for the issue: {0}".format(config_data)
        self.log(self.msg, "ERROR")

    def resolve_issue(self, issue_ids):
        """
        Resolve the issue based on the input issues name.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            issue_ids (list): A list containing issue ids from get issue ids.

        Returns:
            dict: A dictionary of task id details.

        Description:
            This function used to resolve the issue and show the status of the resolved
            status of the issue id.
        """
        self.log("Resolve the issue with parameters: {0}".format(
                 self.pprint(issue_ids)), "INFO")
        try:
            response = self.dnac._exec(
                family="issues",
                function="resolve_the_given_lists_of_issues",
                op_modifies=True,
                params=dict(issueIds=issue_ids)
            )
            self.log("Response from Resolve issue API response: {0}".format(
                response), "DEBUG")

            if response and isinstance(response, dict):
                return response.get("response")
            else:
                return None

        except Exception as e:
            self.msg = 'An error occurred during resolve issue: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def ignore_issue(self, issue_ids):
        """
        Ignore the issue based on the input issues name.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            issue_ids (list): A list containing issue ids from get issue ids.

        Returns:
            dict: A dictionary of task id details.

        Description:
            This function used to ignore the issue and show the status of the processed
            status of the issue id.
        """

        self.log("Ignore issue with parameters: {0}".format(
                 self.pprint(issue_ids)), "INFO")

        try:
            response = self.dnac._exec(
                family="issues",
                function="ignore_the_given_list_of_issues",
                op_modifies=True,
                params=dict(issueIds=issue_ids)
            )
            self.log("Response from ignore issue API response: {0}".format(
                response), "DEBUG")

            if response and isinstance(response, dict):
                return response.get("response")
            else:
                return None

        except Exception as e:
            self.msg = 'An error occurred during ignore issue API: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def execute_commands(self, issue_id):
        """
        Execute command function based on the input issues name and Issue id.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing input config data from playbook.

        Returns:
            dict: A dictionary of task id details.

        Description:
            This function used to execute the comamnd and show the processed
            status of the issue id.
        """
        self.log("Execute the command with parameters: {0}".format(
            self.pprint(issue_id)), "INFO")

        try:
            response = self.dnac._exec(
                family="issues",
                function="execute_suggested_actions_commands",
                op_modifies=True,
                params={
                    "entity_type": "issue_id",
                    "entity_value": issue_id
                }
            )
            self.log("Response from execute command API response: {0}".format(
                response), "DEBUG")

            if response and isinstance(response, dict):
                executionid = response.get("executionId")
                resync_retry_count = int(self.payload.get("dnac_api_task_timeout", 100))
                resync_retry_interval = int(self.payload.get("dnac_task_poll_interval", 5))

                while resync_retry_count:
                    execution_details = self.get_execution_details(executionid)
                    self.log("Execution details: {0}".format(self.pprint(execution_details)), "INFO")
                    if execution_details.get("status") == "SUCCESS":
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        return execution_details
                    if execution_details.get("bapiError"):
                        msg = execution_details.get("bapiError")
                        self.set_operation_result("failed", False, msg, "ERROR",
                                                  execution_details).check_return_status()
                        return execution_details

                    time.sleep(resync_retry_interval)
                    resync_retry_count = resync_retry_count - 1
                return response
            else:
                return None

        except Exception as e:
            self.msg = 'An error occurred during ignore issue API: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def update_system_issue(self, assurance_system_issue_details):
        """
        Update the system-defined issues in Cisco Catalyst Center based on the provided playbook details.
        This method directly updates the issues without checking if the issue exists.

        Parameters:
            assurance_system_issue_details (dict) - Playbook details containing System Defined Issue configuration.

        Returns:
            self - The current object with updated system issue details.
        """

        updated_system_issues = []
        result_assurance_issue = self.result.get("response")[1].get("assurance_system_issue_settings")
        for issue_setting in assurance_system_issue_details:
            name = issue_setting.get("name")
            description = issue_setting.get("description")
            if name is None:
                self.msg = "Missing required parameter 'name' in assurance_system_issue_details"
                self.status = "failed"
                return self

            system_issue = self.have.get("assurance_system_issue_settings")

            if not system_issue:
                self.msg = f"System issue details for '{name}' could not be retrieved."
                self.status = "failed"
                return self

            for item in system_issue:
                if item.get("displayName") == name or (description and item.get("description") == description):
                    if not self.requires_update(item, issue_setting, self.system_issue_obj_params):
                        self.log(
                            "System defined issue '{0}' doesn't require an update".format(name), "INFO")
                        result_assurance_issue.get("msg").update(
                            {name: "System defined issue doesn't require an update"})
                    elif issue_setting not in updated_system_issues:
                        updated_system_issues.append(issue_setting)

            if updated_system_issues:
                for issue in system_issue:
                    if issue.get("displayName") == name and (not description or issue.get("description") == description):
                        system_issue_params = {
                            "id": issue.get("id"),
                            "payload": {
                                # "name": name,
                                "priority": issue_setting.get("priority"),
                                "issueEnabled": issue_setting.get("issue_enabled"),
                                "thresholdValue": issue_setting.get("threshold_value"),
                                "synchronizeToHealthThreshold": issue_setting.get("synchronize_to_health_threshold"),
                            }
                        }

                        self.log(f"Preparing update for system issue '{name}' with params: {system_issue_params}", "DEBUG")

                        try:
                            response = self.dnac._exec(
                                family="issues",
                                function="issue_trigger_definition_update",
                                op_modifies=True,
                                params=system_issue_params,
                            )
                            response_data = response.get("response")
                            if response_data:
                                self.log(f"Successfully updated system-defined issue '{name}' with details: {response_data}", "INFO")
                                updated_system_issues.append(response_data)
                            else:
                                self.log(f"Failed to update system issue '{name}'", "ERROR")

                        except Exception as e:
                            self.msg = "Exception occurred while updating the system-defined issue '{0}':".format(str(e))
                            self.log(self.msg, "ERROR")
                            self.status = "failed"
                            return self

                        result_assurance_issue.get("response").update(
                            {"system issue": system_issue_params})
                        result_assurance_issue.get("msg").update(
                            {response_data.get("displayName"): "System issue Updated Successfully"})
                        self.msg = "Successfully updated system-defined issue details."
                        self.status = "success"
                        self.result['changed'] = True

        return self

    def create_assurance_issue(self, assurance_details):
        """
        Update/Create Assurance issue in Cisco Catalyst Center with fields provided in playbook

        Parameters:
            assurance issue (list of dict) - Assurance Issue playbook details

        Returns:
            self - The current object with Assurance Issue information.
        """

        create_assurance_issue = []
        update_assurance_issue = []
        assurance_index = 0
        result_assurance_issue = self.result.get("response")[0].get("assurance_user_defined_issue_settings")
        want_assurance_issue = self.want.get("assurance_user_defined_issue_settings")
        self.log(want_assurance_issue[assurance_index])
        self.log(want_assurance_issue[assurance_index].get("name"))
        self.log("Assurance issue playbook details: {0}".format(
            assurance_details), "DEBUG")
        for item in self.have.get("assurance_user_defined_issue_settings"):
            result_assurance_issue.get("msg").update(
                {want_assurance_issue[assurance_index].get("name"): {}})
            if item.get("exists") is True:
                update_assurance_issue.append(want_assurance_issue[assurance_index])
            else:
                create_assurance_issue.append(want_assurance_issue[assurance_index])

            assurance_index += 1

        for issue in create_assurance_issue:
            self.log("Assurance issue(s) details to be created: {0}".format(
                issue), "INFO")
            user_issue_params = {
                "name": issue.get("name"),
                "description": issue.get("description"),
                "rules": [
                    {
                        "severity": rule.get("severity"),
                        "facility": rule.get("facility"),
                        "mnemonic": rule.get("mnemonic"),
                        "pattern": rule.get("pattern"),
                        "occurrences": rule.get("occurrences"),
                        "durationInMinutes": rule.get("duration_in_minutes")
                    }
                    for rule in issue.get("rules", [])
                ],
                "isEnabled": issue.get("is_enabled"),
                "priority": issue.get("priority"),
                "isNotificationEnabled": issue.get("is_notification_enabled")
            }

            try:
                response = self.dnac._exec(
                    family="issues",
                    function="creates_a_new_user_defined_issue_definitions",
                    op_modifies=True,
                    params=user_issue_params
                )
            except Exception as msg:
                self.msg = (
                    "Exception occurred while creating the user defined issue: {msg}"
                    .format(msg=msg)
                )
                self.log(str(msg), "ERROR")
                self.status = "failed"
                return self

            if response.get("response"):
                response_data = response.get("response")
                if "name" in response_data:
                    self.log(
                        "Successfully created user defined issue with these details: {0}"
                        .format(response_data),
                        "INFO"
                    )
                name = issue.get("name")
                self.log(
                    "User Defined Issue '{0}' created successfully.".format(name),
                    "INFO")
                result_assurance_issue.get("response").update(
                    {"created user-defined issue": issue})
                result_assurance_issue.get("msg").update(
                    {response_data.get("name"): "User Defined Issue Created Successfully"})
                self.result['changed'] = True

        if update_assurance_issue:
            self.update_user_defined_issue(assurance_details, update_assurance_issue)

        self.status = "Success"
        return self

    def update_user_defined_issue(self, assurance_details, update_assurance_issue):
        """
        Update the user-defined issues in Cisco Catalyst Center based on the provided assurance details.
        This method ensures updates are applied only to issues that require changes, based on the current system state.

        Parameters:
            assurance_details (dict): Details containing assurance configuration for user-defined issues.
            update_assurance_issue (list[dict]): A list of user-defined issue configurations to be updated.
            Each item should include details such as name, description, rules, and settings.

        Returns:
            self: The current object with updated user-defined issue details, including success or failure messages.
        """
        self.log("Updation start")
        result_assurance_issue = self.result.get("response")[0].get("assurance_user_defined_issue_settings")
        final_update_user_defined_issue = []
        for item in update_assurance_issue:
            name = item.get("name")
            for issue in self.have.get("assurance_user_defined_issue_settings"):
                if issue.get("exists") and (issue.get("assurance_issue_details").get(
                        "name") == name or issue.get("prev_name") == name):
                    if not self.requires_update(issue.get("assurance_issue_details"), item, self.user_defined_issue_obj_params):
                        self.log(
                            "Assurance issue '{0}' doesn't require an update".format(name), "INFO")
                        result_assurance_issue.get("msg").update(
                            {name: "Assurance issue doesn't require an update"})
                    elif item not in final_update_user_defined_issue:
                        final_update_user_defined_issue.append(item)

        self.log(final_update_user_defined_issue)
        for issue in final_update_user_defined_issue:
            name = issue.get("name")
            prev_name = issue.get("prev_name")
            for id in self.have.get("assurance_user_defined_issue_settings"):
                assurance_issue_details = id.get('assurance_issue_details')
                if assurance_issue_details:
                    assurance_name = assurance_issue_details.get("name")

                    # Check if prev_name exists, otherwise fallback to checking name
                    if (prev_name and assurance_name == prev_name) or assurance_name == name:
                        user_issue_params = {
                            "id": id.get("id"),
                            "payload":
                            {
                                "name": issue.get("name"),
                                "description": issue.get("description"),
                                "rules": [
                                    {
                                        "severity": rule.get("severity"),
                                        "facility": rule.get("facility"),
                                        "mnemonic": rule.get("mnemonic"),
                                        "pattern": rule.get("pattern"),
                                        "occurrences": rule.get("occurrences"),
                                        "durationInMinutes": rule.get("duration_in_minutes")
                                    }
                                    for rule in issue.get("rules", [])
                                ],
                                "isEnabled": issue.get("is_enabled"),
                                "priority": issue.get("priority"),
                                "isNotificationEnabled": issue.get("is_notification_enabled")
                            }
                        }

                        self.log("Desired State for user issue (want): {0}".format(
                            user_issue_params), "DEBUG")

                        try:
                            response = self.dnac._exec(
                                family="issues",
                                function="updates_an_existing_custom_issue_definition_based_on_the_provided_id",
                                op_modifies=True,
                                params=user_issue_params,
                            )
                            self.log(response)
                        except Exception as msg:
                            self.msg = (
                                "Exception occurred while updating the user defined: {msg}" .format(
                                    msg=msg))
                            self.log(str(msg), "ERROR")
                            self.status = "failed"
                            return self

                        if response.get("response"):
                            response_data = response.get("response")
                            if "name" in response_data:
                                self.log(
                                    "Successfully Updated defined issue with these details: {0}"
                                    .format(response_data),
                                    "INFO"
                                )
                            self.log(
                                "User Defined Issue '{0}' update successfully.".format(name), "INFO"
                            )
                            result_assurance_issue.get("response").update(
                                {"updated user defined issue Details": item})
                            result_assurance_issue.get("msg").update(
                                {name: "User defined issues updated Successfully"})
                            self.result['changed'] = True

        return self

    def delete_assurance_issue(self, assurance_user_defined_issue_details):
        """
        Delete a Assurance Issue by name in Cisco Catalyst Center

        Parameters:
            Assurance_issue_details (dict) - Assurance Issue details of the playbook

        Returns:
            self - The current object with Assurance Issue information.
        """
        try:
            result_assurance_issue = self.result.get("response")[0].get("assurance_user_defined_issue_settings")
            assurance_issue_index = 0
            for item in self.have.get("assurance_user_defined_issue_settings"):
                assurance_issue_exists = item.get("exists")
                name = assurance_user_defined_issue_details[assurance_issue_index].get("name")
                assurance_issue_index += 1
                if not assurance_issue_exists:
                    result_assurance_issue.get("msg").update({name: "Assurance Issue not found"})
                    self.log("Assurance Issue '{0}' not found".format(name), "INFO")
                    continue
                try:
                    id = item.get("id")
                    response = self.dnac._exec(
                        family="issues",
                        function="deletes_an_existing_custom_issue_definition",
                        op_modifies=True,
                        params={"id": id},
                    )
                    self.log("deletion log")
                    self.log(response)
                except Exception as e:
                    expected_exception_msgs = [
                        "Expecting value: line 1 column 1",
                        "not iterable",
                        "has no attribute"
                    ]
                    for msg in expected_exception_msgs:
                        if msg in str(e):
                            self.log("An exception occurred while checking the Assurance user issue with '{0}': {1}"
                                     .format(name, msg))
                        result_assurance_issue = self.result.get("response")[0].get("assurance_user_defined_issue_settings")
                        result_assurance_issue.get("response").update({name: {}})
                        result_assurance_issue.get("msg").update({name: "Assurance user issue deleted successfully"})
                        self.result['changed'] = True
                        self.msg = "Assurance Issues deleted successfully"
                        self.status = "success"
                        return self
        except Exception as e:
            self.status = "failed"
            self.msg = "An exception occurred while deleting the Assurance user issue with '{0}': {1}".format(name, str(e))
            self.log(self.msg, "ERROR")
            return self

    def get_diff_merged(self, config):
        """
        Update or create Global Pool, Reserve Pool, and
        Network configurations in Cisco Catalyst Center based on the playbook details

        Parameters:
            config (list of dict) - Playbook details containing
            Global Pool, Reserve Pool, and Network Management information.

        Returns:
            self - The current object with Global Pool, Reserved Pool, Network Servers information.
        """
        assurance_user_defined_issue_details = config.get("assurance_user_defined_issue_settings")
        if assurance_user_defined_issue_details is not None:
            self.create_assurance_issue(assurance_user_defined_issue_details).check_return_status()

        assurance_system_issue_details = config.get("assurance_system_issue_settings")
        if assurance_system_issue_details is not None:
            self.update_system_issue(assurance_system_issue_details).check_return_status()

        assurance_issue = config.get("assurance_issue")
        if assurance_issue and len(assurance_issue) > 0:
            success_list = []
            self.issue_unresolved = []
            self.msg = ""
            self.changed = False
            self.status = "failed"
            response = {}

            for each_issue in assurance_issue:
                issue_ids = self.get_issue_ids_for_names(each_issue)
                if issue_ids and len(issue_ids) > 0:

                    if each_issue["issue_process_type"] == "resolution":
                        response = self.resolve_issue(issue_ids)

                        if response and isinstance(response, dict):
                            self.success_list_resolved.append(each_issue)
                            self.issue_resolved.append(response)
                            self.log("Issue processed for: {0}, processed log: {1}".format(
                                self.pprint(self.success_list_resolved),
                                self.pprint(self.issue_resolved)), "INFO")
                        else:
                            self.failed_list_resolved.append(each_issue)
                            self.log("Unable to process the issue for: {0}.".format(
                                self.pprint(self.failed_list_resolved)), "INFO")

                    elif each_issue["issue_process_type"] == "ignore":
                        response = self.ignore_issue(issue_ids)

                        if response and isinstance(response, dict):
                            self.success_list_ignored.append(each_issue)
                            self.issue_ignored.append(response)
                            self.log("Issue processed for: {0}, processed log: {1}".format(
                                self.pprint(self.success_list_ignored),
                                self.pprint(self.issue_ignored)), "INFO")
                        else:
                            self.failed_list_ignored.append(each_issue)
                            self.log("Unable to process the issue for: {0}.".format(
                                self.pprint(self.failed_list_ignored)), "INFO")

                    elif each_issue["issue_process_type"] == "command_execution":
                        response = self.execute_commands(issue_ids[0])

                        if response:
                            success_list.append(each_issue)
                            self.cmd_executed.append(response)
                        else:
                            self.cmd_not_executed.append(each_issue)

            if len(self.success_list_resolved) > 0:
                self.msg = "Issue resolved successfully. '{0}'.".format(
                    str(self.issue_resolved))
                self.changed = True
                self.status = "success"
                self.log(self.msg, "INFO")

            if len(self.failed_list_resolved) > 0:
                self.msg = self.msg + "Unable to resolve the issue: '{0}'.".format(
                    str(self.failed_list_resolved))
                self.log(self.msg, "INFO")

            if len(self.success_list_ignored) > 0:
                self.msg = self.msg + "Issue ignored successfully. '{0}'.".format(
                    str(self.issue_ignored))
                self.changed = True
                self.status = "success"
                self.log(self.msg, "INFO")

            if len(self.failed_list_ignored) > 0:
                self.msg = self.msg + "Unable to ignore the issue: '{0}'.".format(
                    str(self.failed_list_ignored))
                self.log(self.msg, "INFO")

            if len(success_list) > 0:
                self.msg = self.msg + "Command executed successfully for {0}.".format(
                    str(self.cmd_executed))
                self.changed = True
                self.status = "success"

            if len(self.cmd_not_executed) > 0:
                self.msg = self.msg + "Unable to execute the command for {0}.".format(
                    str(self.cmd_not_executed))

            self.log(self.msg, "INFO")
            success_list.extend(self.issue_resolved)
            success_list.extend(self.issue_ignored)
            self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                                      success_list)
        return self

    def get_diff_deleted(self, config):
        """
        Update or create Global Pool, Reserve Pool, and
        Network configurations in Cisco Catalyst Center based on the playbook details

        Parameters:
            config (list of dict) - Playbook details containing
            Global Pool, Reserve Pool, and Network Management information.

        Returns:
            self - The current object with Global Pool, Reserved Pool, Network Servers information.
        """
        assurance_user_defined_issue_details = config.get("assurance_user_defined_issue_settings")
        if assurance_user_defined_issue_details is not None:
            self.delete_assurance_issue(assurance_user_defined_issue_details)
        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing Assurance issue.

        Returns:
            self - The current object with Global Pool, Reserved Pool, Network Servers information.
        """

        self.all_assurance_issue_details = {}
        self.get_have(config)
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Requested State (want): {0}".format(self.want), "INFO")
        if config.get("assurance_user_defined_issue_settings") is not None:
            assurance_user_issue_index = 0
            self.log("Desired State of assurance user issue (want): {0}"
                     .format(self.want.get("assurance_user_defined_issue_settings")), "DEBUG")
            self.log("Current State of assurance user issue (have): {0}"
                     .format(self.have.get("assurance_user_defined_issue_settings")), "DEBUG")
            for item in self.want.get("assurance_user_defined_issue_settings"):
                assurance_user_issue_details = self.have.get(
                    "assurance_user_defined_issue_settings")[assurance_user_issue_index].get("assurance_issue_details")
                self.log(assurance_user_issue_details)
                if not assurance_user_issue_details:
                    self.msg = "The Assurance user defined issue is not created with the config: {0}".format(
                        item)
                    self.status = "failed"
                    return self

                if self.requires_update(assurance_user_issue_details, item, self.user_defined_issue_obj_params):
                    self.msg = "Assurance user defined issue Config is not applied to the Cisco Catalyst Center"
                    self.status = "failed"
                    return self

                assurance_user_issue_index += 1

            self.log("Successfully validated Assurance user defined issue(s).", "INFO")
            self.result.get("response")[0].get(
                "assurance_user_defined_issue_settings").update({"Validation": "Success"})

        if config.get("assurance_system_issue_settings") is not None:
            assurance_system_index = 0
            self.log("Desired State of assurance system (want): {0}"
                     .format(self.want.get("assurance_system_issue_settings")), "DEBUG")
            self.log("Current State of assurance user issue (have): {0}"
                     .format(self.have.get("assurance_system_issue_settings")), "DEBUG")
            for item in self.want.get("assurance_system_issue_settings"):
                assurance_system_details = self.have.get(
                    "assurance_system_issue_settings")[assurance_system_index]
                self.log(assurance_system_details)

                if self.requires_update(assurance_system_details, item, self.system_issue_obj_params):
                    self.msg = "Assurance system issue Config is not applied to the Cisco Catalyst Center"
                    self.status = "failed"
                    return self

                assurance_system_index += 1

            self.log("Successfully validated Assurance system issue(s).", "INFO")
            self.result.get("response")[1].get(
                "assurance_system_issue_settings").update({"Validation": "Success"})

        assurance_issue = config.get("assurance_issue")
        if assurance_issue and len(assurance_issue) > 0:
            responses = {}
            responses["input_isssue_config"] = config.get("assurance_issue")
            self.msg = ""
            self.changed = False
            self.status = "failed"

            if len(self.success_list_resolved) > 0 or len(self.failed_list_resolved) > 0:
                response = {
                    "processed_issues_resolved": self.success_list_resolved,
                    "unprocessed_issues_resolved": self.failed_list_resolved,
                    "processed_logs_resolved": self.issue_resolved
                }

                if self.success_list_resolved == assurance_issue:
                    self.msg = "Issue resolution verified successfully for '{0}'.".format(
                        str(self.success_list_resolved))
                    self.log(self.msg, "INFO")
                    self.changed = True
                    self.status = "success"
                else:
                    self.msg = self.msg + "Unable to verify Issue resolution for '{0}'.".format(
                        str(assurance_issue))
                    self.log(self.msg, "INFO")

                responses["issue_resolved"] = response

            if len(self.success_list_ignored) > 0 or len(self.failed_list_ignored) > 0:
                response = {
                    "processed_issues_ignored": self.success_list_ignored,
                    "unprocessed_issues_ignored": self.failed_list_ignored,
                    "processed_logs_ignored": self.issue_ignored
                }

                if self.success_list_ignored in assurance_issue:
                    self.msg = self.msg + "Issue ignored verified successfully for '{0}'.".format(
                        str(self.success_list_ignored))
                    self.log(self.msg, "INFO")
                    self.changed = True
                    self.status = "success"
                else:
                    self.msg = self.msg + "Unable to verify Issue resolution for '{0}'.".format(
                        str(assurance_issue))
                    self.log(self.msg, "INFO")

                responses["issue_ignored"] = response

            if len(self.cmd_executed) > 0 or len(self.cmd_not_executed) > 0:
                response = {
                    "processed_command_execution": self.cmd_executed,
                    "unprocessed_command_execution": self.cmd_not_executed
                }

                if len(self.cmd_executed) > 0:
                    self.msg = self.msg + "Command executed and verified successfully for {0}.".format(
                        assurance_issue)
                    self.log(self.msg, "INFO")
                    self.changed = True
                    self.status = "success"
                else:
                    self.msg = self.msg + "Unable to verify execute suggested command for {0}.".format(
                        str(self.cmd_not_executed))
                    self.log(self.msg, "INFO")

                responses["command_executed"] = response

            self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                                      responses).check_return_status()

        self.msg = "Successfully validated the Assurance issue."
        self.status = "success"
        return self

    def verify_diff_deleted(self, config):
        """
        Verify the data was deleted

        Parameters:
            config (dict) - Playbook details containing Assurance issue.

        Returns:
            self - The current object with Global Pool, Reserved Pool, Network Servers information.
        """
        self.all_assurance_user_issue_details = {}
        if config.get("assurance_user_defined_issue_settings") is not None:
            self.get_have(config)
            self.log("Current State (have): {0}".format(self.have), "INFO")
            self.log("Desired State (want): {0}".format(self.want), "INFO")
            assurance_issue_index = 0
            assurance_issue_details = self.have.get("assurance_user_defined_issue_settings")
            for item in assurance_issue_details:
                assurance_issue_exists = item.get("exists")
                name = config.get("assurance_user_defined_issue_settings")[assurance_issue_index].get("name")
                if assurance_issue_exists:
                    self.msg = "Assurance user defined issue Config '{0}' is not applied to the Cisco Catalyst Center" \
                               .format(name)
                    self.status = "failed"
                    return self

                self.log("Successfully validated absence of Assurance user defined issue '{0}'.".format(name), "INFO")
                assurance_issue_index += 1
            self.result.get("response")[0].get("assurance_user_defined_issue_settings").update({"Validation": "Success"})

        self.msg = "Successfully validated the absence of Assurance user defined issue"
        self.status = "success"
        self.result['changed'] = True
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
    ccc_assurance = AssuranceSettings(module)
    state = ccc_assurance.params.get("state")

    if ccc_assurance.compare_dnac_versions(ccc_assurance.get_ccc_version(), "2.3.7.6") < 0:
        ccc_assurance.status = "failed"
        ccc_assurance.msg = (
            "The specified version '{0}' does not support the assurance issue settings workflow feature."
            "Supported version(s) start from '2.3.7.6' onwards.".format(ccc_assurance.get_ccc_version())
        )
        ccc_assurance.log(ccc_assurance.msg, "ERROR")
        ccc_assurance.check_return_status()

    if state not in ccc_assurance.supported_states:
        ccc_assurance.status = "invalid"
        ccc_assurance.msg = "State {0} is invalid".format(state)
        ccc_assurance.check_return_status()

    ccc_assurance.validate_input().check_return_status()
    config_verify = ccc_assurance.params.get("config_verify")

    for config in ccc_assurance.config:
        ccc_assurance.reset_values()
        ccc_assurance.input_data_validation(config).check_return_status()
        ccc_assurance.get_have(config).check_return_status()
        ccc_assurance.get_want(config).check_return_status()
        ccc_assurance.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_assurance.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_assurance.result)


if __name__ == "__main__":
    main()

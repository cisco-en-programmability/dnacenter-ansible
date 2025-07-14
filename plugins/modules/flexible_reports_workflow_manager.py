#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform update Health score KPI's in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["Megha Kandari, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: flexible_report_workflow_manager
short_description: Resource module for managing Flexible Reports in Cisco Catalyst Center.
description:
  - This module manages Flexible Report configurations in Cisco Catalyst Center.
  - It allows you to create, update, execute, and schedule customized reports across wired and wireless network entities.
  - Supports configuration of report name, time range, subreports, entity selection, report types (Trend, Summary, Top N, Distribution), filters, attributes, and aggregation options.
  - Enables scheduling, output format selection (CSV/ZIP), and delivery methods including Email and Webhook.
  - Requires successful device discovery in Catalyst Center for accurate reporting.
  - Flexible Reports help monitor network and client health, device behavior, and utilization trends.
  - The Flexible Report APIs support multiple operations including fetching schedules, executing reports, and downloading results.
  - Applicable from Cisco Catalyst Center version 2.3.3.1 and later.
version_added: '6.36.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Megha Kandari (@kandarimegha)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: >
      Set to `True` to enable configuration verification
      on Cisco Catalyst Center after applying the playbook
      config. This will ensure that the system validates
      the configuration state after the change is applied.
    type: bool
    default: false
  state:
    description: >
      Specifies the desired state for the configuration.
      If `merged`, the module will update the configuration
      modifying existing ones.
    type: str
    choices: [merged, deleted]
    default: merged
  config:
  description: >
    A list of configuration settings for generating a flexible report in Cisco Catalyst Center.
    This includes defining report metadata, scheduling, delivery options, view and field selections,
    report format, and applicable filters.
  type: list
  elements: dict
  required: true
  suboptions:
    generate_report:
      description: Configuration for generating a report in Catalyst Center.
      type: dict
      required: true
      suboptions:
        name:
          description: The name of the report to be generated.
          type: str
          required: true
        view_group_name:
          description: >
            The name of the view group as defined in Catalyst Center (e.g., "Inventory").
            Used to identify the viewGroupId via API.
          type: str
          required: true
        tags:
          description: >
            Optional list of tags to filter reports.
          type: list
          elements: str
          required: false
        category:
          description: >
            The category of the report, as defined in Catalyst Center (e.g., "Inventory").
            Used to look up viewGroupId.
          type: str
          required: true
        schedule:
          description: >
            Defines when the report should be executed (immediately, later, or on a recurring basis).
          type: dict
          required: true
          suboptions:
            type:
              description: >
                The scheduling type for the report.
                Options: "SCHEDULE_NOW", "SCHEDULE_LATER", "SCHEDULE_RECURRING".
              type: str
              required: true
            date_time:
              description: >
                Scheduled time for report execution (required if type is SCHEDULE_LATER).
                Must be converted to epoch before sending to Catalyst Center.
              type: str
              required: false
            time_zone_id:
              description: >
                Time zone identifier for the schedule (e.g., "Asia/Calcutta").
              type: str
              required: true
        delivery:
          description: >
            Specifies how the generated report should be delivered.
          type: dict
          required: true
          suboptions:
            type:
              description: >
                Delivery type for the report.
                Options: "DOWNLOAD", "NOTIFICATION", "WEBHOOK".
              type: str
              required: true
            location:
              description: >
                Local file system path where the report should be downloaded (only for DOWNLOAD type).
              type: str
              required: false
            email_addresses:
              description: >
                List of email recipients (only used for NOTIFICATION type).
              type: list
              elements: str
              required: false
            email_attach:
              description: >
                Whether the report should be attached in the notification email.
              type: bool
              required: false
            notify:
              description: >
                Notify condition for sending report via NOTIFICATION.
                Options: "IN_QUEUE", "IN_PROGRESS", "COMPLETED".
              type: str
              required: false
        view:
          description: >
            Contains view details such as subcategory, fields, filters, and format for the report.
          type: dict
          required: true
          suboptions:
            subcategory_name:
              description: >
                The subcategory or view name from which viewId is derived.
              type: str
              required: true
            field_groups:
              description: >
                Groups of fields to include in the report, as defined in the selected view.
              type: list
              elements: dict
              required: true
              suboptions:
                name:
                  description: Name of the field group.
                  type: str
                  required: true
                display_name:
                  description: UI display name of the field group.
                  type: str
                  required: true
                fields:
                  description: >
                    List of fields to include within the field group.
                  type: list
                  elements: dict
                  required: true
                  suboptions:
                    name:
                      description: Field identifier.
                      type: str
                      required: true
                    display_name:
                      description: Field display name in the UI.
                      type: str
                      required: true
            format:
              description: >
                Specifies the output format of the report.
              type: dict
              required: true
              suboptions:
                name:
                  description: >
                    Name of the format (e.g., "CSV").
                  type: str
                  required: true
                format_type:
                  description: >
                    Type of format to be used.
                    Supported: "CSV", "PDF", "JSON", "TDE".
                  type: str
                  required: true
            filters:
              description: >
                Filters to be applied to narrow down the report data.
              type: list
              elements: dict
              required: false
              suboptions:
                name:
                  description: Name of the filter.
                  type: str
                  required: true
                display_name:
                  description: Display name of the filter.
                  type: str
                  required: true
                type:
                  description: >
                    Type of the filter.
                    Examples: "MULTI_SELECT", "MULTI_SELECT_TREE", "SINGLE_SELECT_ARRAY", "TIME_RANGE".
                  type: str
                  required: true
                value:
                  description: >
                    Value(s) to apply in the filter.
                    For "TIME_RANGE", this is a dict with time_range_option, start_date_time, end_date_time, and time_zone_id.
                    For others, this is a list of dicts with "value" and "display_value".
                  type: raw
                  required: true
        view_group_version:
          description: >
            Version of the view group to be used.
            Can be fetched using the Catalyst Center API.
          type: str
          required: true
        download:
          description: >
            Boolean flag indicating whether the report should be downloaded
            automatically after it has been generated. This is especially relevant
            when the delivery type is set to "DOWNLOAD".
          type: bool
          required: false
          default: false
        file_path:
          description: >
            Local file system path where the downloaded report should be saved,
            if `download` is set to true. This path must be accessible from the
            system where the playbook is executed.
          type: str
          required: false


requirements:
  - dnacentersdk >= 2.8.6
  - python >= 3.9
notes:
  - SDK Method used are
    reports.Reports.get_all_view_groups,
    reports.Reports.get_views_for_a_given_view_group
    reports.Reports.get_view_details_for_a_given_view_group_and_view,
    reports.Reports.create_or_schedule_a_report
    reports.Reports.delete_a_scheduled_report,
    reports.Reports.download_report_content
    reports.Reports.get_execution_id_by_report_id,
    reports.Reports.get_all_flexible_report_schedules
    reports.Reports.executing_the_flexible_report,
    reports.Reports.executing_the_flexible_report
  - Paths used are
    - GET/dna/intent/api/v1/data/view-groups  
  	- GET/dna/intent/api/v1/data/view-groups/{viewGroupId}
  	- GET /dna/intent/api/v1/data/view-groups/{viewGroupId}/views/{viewId}
  	- POST /dna/intent/api/v1/data/reports
  	- DELETE /dna/intent/api/v1/data/reports/{reportId}
  	- GET /dna/intent/api/v1/data/reports/{reportId}/executions/{executionId}
  	- GET /dna/data/api/v1/flexible-report/report/{reportId}/executions
  	- POST /dna/data/api/v1/flexible-report/report/{reportId}/execute
"""

EXAMPLES = r"""
---
- name: Generate a flexible report
      cisco.dnac.flexible_report_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: True
        state: merged
        config_verify: True
        config:
        - generate_report:
            name: "Report Name" # The name of the report
            view_group_name: "Inventory" # The name of the view group as defined in Catalyst Center
            tags: [] # Tags to filter reports (optional)
            category: "Inventory" # The category as defined in Catalyst Center- used to fetch viewGroupId
            # subcategory: "All Data" # (this is report subtype) From this subcategory or view name, we need to fetch viewId (from viewGroupId we can fetch view and viewId based on the name of the view)
            schedule:
              type: "SCHEDULE_LATER" # Options: "SCHEDULE_NOW", "SCHEDULE_LATER", "SCHEDULE_RECURRING"
              date_time: "2025-04-19 08:00 AM" # Scheduled time for the report execution => This needs to be converted in epoch
              time_zone_id: "Asia/Calcutta" # Time zone ID for scheduling
            delivery:
              type: "DOWNLOAD" # Options: "DOWNLOAD", "NOTIFICATION", "WEBHOOK"
              # If type is WEBHOOK, fetch webhook ID from API using webhook name
              location: "../Desktop/Reports" # Local path to save the report (valid for DOWNLOAD type)
              # Alternative delivery option: NOTIFICATION
              # type: "NOTIFICATION"
              # email_addresses:  # List of recipients for email notifications
              #   - abc@zzz.com
              #   - xyz@zzz.com
              # email_attach: true  # Attach report to email (true/false)
              # notify: "COMPLETED"  # Options: "IN_QUEUE", "IN_PROGRESS", "COMPLETED"
            view:
              subcategory_name: "All Data"
              # name: "Default"
              field_groups:
                - name: "inventoryAllData"  # Name of the field group
                  display_name: "All Data"  # Display name in UI
                  fields:
                    - name: "type"  # Field name
                      display_name: "Device Type"  # Display name in UI
                    - name: "hostname"
                      display_name: "Device Name"
                    - name: "ipAddress"
                      display_name: "IP Address"
              format:
                name: "CSV" # The name of the report format
                format_type: "CSV" # Supported formats: "CSV", "PDF", "JSON", "TDE"

              filters:
                - name: "Location"  # Filter name
                  display_name: "Location"  # Display name in UI
                  type: "MULTI_SELECT_TREE"  # Type of filter
                  value:
                    - value: "/50f15f14-4c73-47a7-9dc3-cb10eb9508bd/"  # Location ID
                      display_value: "Global"  # Readable name for selection
                    - value: "/50f15f14-4c73-47a7-9dc3-cb10eb9508bd/4e7815d1-e33a-465c-a8b7-d5d4449640a7/" # Need to provide ID of each location specifically and attach it together
                      display_value: "Global/AB_Test"

                - name: "SSID"
                  display_name: "SSID"
                  type: "MULTI_SELECT"
                  value:
                    - value: "NY_SSID" # need to validate these SSIDs based on the site that users provides or default: global
                      display_value: "NY_SSID"
                    - value: "ent_ssid_1_wpa3"
                      display_value: "ent_ssid_1_wpa3"

                - name: "Band"
                  display_name: "Band"
                  type: "MULTI_SELECT"
                  value:
                    - value: "6"
                      display_value: "6"

                - name: "GroupBy"
                  display_name: "Group By"
                  type: "SINGLE_SELECT_ARRAY"
                  value:
                    - value: "BUILDING"
                      display_value: "BUILDING"

                - name: "TimeRange"
                  display_name: "Time Range"
                  type: "TIME_RANGE"
                  value:
                    time_range_option: "CUSTOM"  # Options: "CUSTOM", "LAST_24_HOURS", "LAST_7_DAYS"
                    start_date_time: "2025-03-01 08:00 AM"  # Custom start time (if CUSTOM is selected)
                    end_date_time: "2025-03-19 08:00 AM"  # Custom end time (if CUSTOM is selected)
                    time_zone_id: "America/Los_Angeles"  # Time zone ID for time range filtering
              
            view_group_version: "1.0"  # Version of the view group, can be fetched from API
	 -  download: true  # <--- NEW: Whether to download the report after execution
              file_path: "../Desktop/Reports"  # <--- NEW: Path where the report should be saved if download is True


- name: Download flexible reports
      cisco.dnac.flexible_report_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: True
        state: merged
        config_verify: True
        config:
        - generate_report:
            - name: "Report Name" # The name of the report
              view_group_name: "Inventory" # The name of the view group as defined in Catalyst Center
              tags: [] # Tags to filter reports (optional)
              category: "Inventory" # The category as defined in Catalyst Center- used to fetch viewGroupId
              # subcategory: "All Data" # (this is report subtype) From this subcategory or view name, we need to fetch viewId (from viewGroupId we can fetch view and viewId based on the name of the view)
              schedule:
                type: "SCHEDULE_LATER" # Options: "SCHEDULE_NOW", "SCHEDULE_LATER", "SCHEDULE_RECURRING"
                date_time: "2025-04-19 08:00 AM" # Scheduled time for the report execution => This needs to be converted in epoch
                time_zone_id: "Asia/Calcutta" # Time zone ID for scheduling
              delivery:
                type: "DOWNLOAD" # Options: "DOWNLOAD", "NOTIFICATION", "WEBHOOK"
                # If type is WEBHOOK, fetch webhook ID from API using webhook name
                location: "../Desktop/Reports" # Local path to save the report (valid for DOWNLOAD type)
                # Alternative delivery option: NOTIFICATION
                # type: "NOTIFICATION"
                # email_addresses:  # List of recipients for email notifications
                #   - abc@zzz.com
                #   - xyz@zzz.com
                # email_attach: true  # Attach report to email (true/false)
                # notify: "COMPLETED"  # Options: "IN_QUEUE", "IN_PROGRESS", "COMPLETED"
              view:
                subcategory_name: "All Data"
                # name: "Default"
                field_groups:
                  - name: "inventoryAllData"  # Name of the field group
                    display_name: "All Data"  # Display name in UI
                    fields:
                      - name: "type"  # Field name
                        display_name: "Device Type"  # Display name in UI
                      - name: "hostname"
                        display_name: "Device Name"
                      - name: "ipAddress"
                        display_name: "IP Address"
                format:
                  name: "CSV" # The name of the report format
                  format_type: "CSV" # Supported formats: "CSV", "PDF", "JSON", "TDE"
                filters:
                  - name: "Location"  # Filter name
                    display_name: "Location"  # Display name in UI
                    type: "MULTI_SELECT_TREE"  # Type of filter
                    value:
                      - value: "/50f15f14-4c73-47a7-9dc3-cb10eb9508bd/"  # Location ID
                        display_value: "Global"  # Readable name for selection
                      - value: "/50f15f14-4c73-47a7-9dc3-cb10eb9508bd/4e7815d1-e33a-465c-a8b7-d5d4449640a7/" # Need to provide ID of each location specifically and attach it together
                        display_value: "Global/AB_Test"

                  - name: "SSID"
                    display_name: "SSID"
                    type: "MULTI_SELECT"
                    value:
                      - value: "NY_SSID" # need to validate these SSIDs based on the site that users provides or default: global
                        display_value: "NY_SSID"
                      - value: "ent_ssid_1_wpa3"
                        display_value: "ent_ssid_1_wpa3"

                  - name: "Band"
                    display_name: "Band"
                    type: "MULTI_SELECT"
                    value:
                      - value: "6"
                        display_value: "6"

                  - name: "GroupBy"
                    display_name: "Group By"
                    type: "SINGLE_SELECT_ARRAY"
                    value:
                      - value: "BUILDING"
                        display_value: "BUILDING"

                  - name: "TimeRange"
                    display_name: "Time Range"
                    type: "TIME_RANGE"
                    value:
                      time_range_option: "CUSTOM"  # Options: "CUSTOM", "LAST_24_HOURS", "LAST_7_DAYS"
                      start_date_time: "2025-03-01 08:00 AM"  # Custom start time (if CUSTOM is selected)
                      end_date_time: "2025-03-19 08:00 AM"  # Custom end time (if CUSTOM is selected)
                      time_zone_id: "America/Los_Angeles"  # Time zone ID for time range filtering
              download: true  # <--- NEW: Whether to download the report after execution
              file_path: "../Desktop/Reports"  # <--- NEW: Path where the report should be saved if download is True
              view_group_version: "1.0"  # Version of the view group, can be fetched from API



    - name: Delete a flexible report
      cisco.dnac.flexible_report_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_version: "{{dnac_version}}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: True
        state: merged
        config_verify: True
        config:
        - generate_report:
            name: "Report Name" # The name of the report
"""

RETURN = r"""
# Case 1: Successful Flexible Report Generation
response_create_or_schedule_a_report:
  description: Response returned after successfully generating or scheduling a flexible report in Cisco Catalyst Center.
  returned: always
  type: dict
  sample: {
    "tags": [
        "string"
    ],
    "dataCategory": "string",
    "deliveries": [
        "any"
    ],
    "executionCount": "integer",
    "executions": [
        {
            "endTime": "integer",
            "errors": [
                "string"
            ],
            "executionId": "string",
            "processStatus": "string",
            "requestStatus": "string",
            "startTime": "integer",
            "warnings": [
                "string"
            ]
        }
    ],
    "name": "string",
    "reportId": "string",
    "reportWasExecuted": "boolean",
    "schedule": "any",
    "view": {
        "fieldGroups": [
            {
                "fieldGroupDisplayName": "string",
                "fieldGroupName": "string",
                "fields": [
                    {
                        "displayName": "string",
                        "name": "string"
                    }
                ]
            }
        ],
        "filters": [
            {
                "displayName": "string",
                "name": "string",
                "type": "string",
                "value": "any"
            }
        ],
        "format": {
            "formatType": "string",
            "name": "string"
        },
        "name": "string",
        "viewId": "string",
        "description": "string",
        "viewInfo": "string"
    },
    "viewGroupId": "string",
    "viewGroupVersion": "string"
  }

# Case 2: Successful Deletion of Flexible Reports
response_delete_a_scheduled_report:
  description: Response returned after successfully deleting a scheduled flexible report.
  returned: always
  type: dict
  sample: {
    "message": "string",
    "status": "integer"
  }

# Case 3: Successful Download of Flexible Reports
response_download_report_content:
  description: Contents of the flexible report retrieved from Cisco Catalyst Center for download.
  returned: always
  type: str
  sample: "CSV-formatted string content or report data"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)

class FlexibleReport(DnacBase):
    """Class containing member attributes for Flexible Report Workflow Manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.result["response"] = [
            {"flexible_report": {"response": {}, "msg": {}}},
        ]
        self.create_report, self.update_report, self.no_update_report = [], [], []


    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.
            self.config (dict): A dictionary representing the playbook configuration that needs validation.
            The 'config' should be structured according to a specification, with keys such as 'flexible_report'.
            Each key in the configuration should match the predefined data types and structure defined in `temp_spec`.

        Returns:
            The method updates these attributes of the instance:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation ('success' or 'failed').
                - self.validated_config (dict): The validated configuration, if successful, otherwise the method returns early with failure.
        """

        temp_spec = {
        "generate_report": {
            "type": "list",
            "elements": "dict",
            "options": {
                "name": {"type": "str", "required": True},
                "view_group_name": {"type": "str", "required": True},
                "tags": {"type": "list", "elements": "str", "required": False},
                "category": {"type": "str", "required": True},
                "schedule": {
                    "type": "dict",
                    "options": {
                        "type": {"type": "str", "required": True},
                        "date_time": {"type": "str", "required": False},
                        "time_zone_id": {"type": "str", "required": False}
                    }
                },
                "delivery": {
                    "type": "dict",
                    "options": {
                        "type": {"type": "str", "required": True},
                        "location": {"type": "str", "required": False},
                        "email_addresses": {"type": "list", "elements": "str", "required": False},
                        "email_attach": {"type": "bool", "required": False},
                        "notify": {"type": "str", "required": False}
                    }
                },
                "view": {
                    "type": "dict",
                    "options": {
                        "subcategory_name": {"type": "str", "required": True},
                        "field_groups": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "display_name": {"type": "str", "required": True},
                                "fields": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "name": {"type": "str", "required": True},
                                        "display_name": {"type": "str", "required": True}
                                    }
                                }
                            }
                        },
                        "format": {
                            "type": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "format_type": {"type": "str", "required": True}
                            }
                        },
                        "filters": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "display_name": {"type": "str", "required": True},
                                "type": {"type": "str", "required": True},
                                "value": {
                                    "type": "raw",  # allows dict or list of dicts depending on filter type
                                    "required": True
                                }
                            }
                        }
                    }
                },
                "download": {"type": "bool", "required": False},
                "file_path": {"type": "str", "required": False},
                "view_group_version": {"type": "str", "required": False}
            }
        }
        }

        if not self.config:
            self.msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "The playbook contains invalid parameters: {0}".format(
                invalid_params
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(
            str(valid_temp)
        )
        self.log(self.msg, "INFO")

        return self


    def get_want(self, config):
        """
        Retrieve and store assurance Health score details from playbook configuration.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.

        Returns:
            self: The current instance of the class with updated 'want' attributes.
        """

        want = {"generate_report": config.get("generate_report", [])}

        self.log(want["generate_report"])
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        return self


def main():
    """main entry point for module execution"""
    element_spec = {
        "dnac_host": {"type": "str", "required": True},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"type": "list", "required": True, "elements": "dict"},
        "state": {"default": "merged", "choices": ["merged", "deleted"], "type": "str"},
        "validate_response_schema": {"type": "bool", "default": True},
    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)

    ccc_report = FlexibleReport(module)
    state = ccc_report.params.get("state")

    if state not in ccc_report.supported_states:
        ccc_report.status = "invalid"
        ccc_report.msg = "State '{0}' is invalid. Supported states: {1}".format(
            state, ", ".join(ccc_report.supported_states)
        )
        ccc_report.check_return_status()

    ccc_version = ccc_report.get_ccc_version()
    if ccc_report.compare_dnac_versions(ccc_version, "2.3.7.10") < 0:
        ccc_report.msg = (
            "The specified version '{0}' does not support the Flexible Report features. "
            "Supported versions start from '2.3.7.10' onwards.".format(ccc_version)
        )
        ccc_report.status = "failed"
        ccc_report.check_return_status()
    ccc_report.validate_input().check_return_status()
    config_verify = ccc_report.params.get("config_verify")

    for config in ccc_report.validated_config:
        ccc_report.input_data_validation(config).check_return_status()
        ccc_report.get_want(config).check_return_status()
        ccc_report.get_have(config).check_return_status()
        ccc_report.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_report.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_report.result)


if __name__ == "__main__":
    main()

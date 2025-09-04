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
module: reports_workflow_manager
short_description: Resource module for managing Reports in Cisco Catalyst Center.
description:
  - This module manages Report configurations in Cisco Catalyst Center.
  - It allows you to create and schedule customized reports across wired and wireless network entities.
  - Supports configuration of report name, time range, subreports, entity selection, filters, attributes, and aggregation options.
  - Enables scheduling, output format selection (e.g., CSV/ZIP), and delivery methods including Email and Webhook.
  - Reports help monitor network and client health, device behavior, and utilization trends.
  - Applicable from Cisco Catalyst Center version 2.3.3.1 and later.
version_added: '6.36.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Megha Kandari (@kandarimegha)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description:
      - Set to C(True) to enable configuration verification on Cisco Catalyst Center after applying the playbook config.
      - This will ensure that the system validates the configuration state after the change is applied.
    type: bool
    default: false
  state:
    description:
      - Specifies the desired state for the configuration.
      - If C(merged), the module will update the configuration modifying existing ones.
    type: str
    choices: [merged, deleted]
    default: merged
  config:
    description:
      - A list of configuration settings for generating a report in Cisco Catalyst Center.
      - This includes defining report metadata, scheduling, delivery options, view and field selections, report format, and applicable filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_report:
        description:
          - Configuration for generating a report in Catalyst Center.
        type: dict
        required: true
        suboptions:
          name:
            description:
              - The name of the report to be generated.
              - If not provided, it will be automatically generated in the format
                "<data_category> - <view_name> - <timestamp>"
                (e.g., "Network - DeviceView - Jul 20 2025 08:26 PM").
            type: str
            required: false
          view_group_name:
            description:
              - The name of the view group as defined in Catalyst Center (e.g., C(Inventory)).
              - Used to identify the C(viewGroupId) via API.
            type: str
            required: true
            choices:
              - Compliance
              - Executive Summary
              - Inventory
              - SWIM
              - Access Point
              - Long Term
              - Network Devices
              - Group Pair Communication Analytics
              - Telemetry
              - Group Communication Summary
              - EoX
              - Rogue and aWIPS
              - Licensing
              - AI Endpoint Analytics
              - Audit Log
              - Configuration Archive
              - Client
              - Security Advisories
          tags:
            description:
              - Optional list of tags to filter reports.
            type: list
            elements: str
            required: false
          schedule:
            description:
              - Defines when the report should be executed (immediately, later, or on a recurring basis).
            type: dict
            required: true
            suboptions:
              type:
                description:
                  - The scheduling type for the report.
                choices:
                  - SCHEDULE_NOW
                  - SCHEDULE_LATER
                  - SCHEDULE_RECURRING
                type: str
                required: true
              date_time:
                description:
                  - Scheduled time for report execution (required if type is C(SCHEDULE_LATER)).
                  - For C(SCHEDULE_RECURRENCE)- Acts as the "Run everyday at" time.
                  - Must be converted to epoch before sending to Catalyst Center.
                  - In C(SCHEDULE_RECURRENCE), maps to both C(time) and C(startDate) fields in the payload.
                type: str
                required: false
              time_zone:
                description:
                  - Time zone identifier for the schedule (e.g., C(Asia/Calcutta)).
                type: str
                required: true
          deliveries:
            description:
              - Specifies how the generated report should be delivered.
            type: dict
            required: true
            suboptions:
              type:
                description:
                  - Delivery type for the report.
                choices:
                  - DOWNLOAD
                  - NOTIFICATION
                  - WEBHOOK
                type: str
                required: true
              file_path:
                description:
                  - Local file system path where the report should be downloaded (only for C(DOWNLOAD) type).
                type: str
                required: false
              notification_endpoints:
                description:
                  - Required when C(type) is C(NOTIFICATION).
                  - Specifies endpoints to receive notifications.
                type: list
                elements: dict
                required: false
                suboptions:
                  email_addresses:
                    description:
                    - List of email recipients (only used for C(NOTIFICATION) type).
                    type: list
                    elements: str
                    required: false
                  email_attach:
                    description:
                    - Whether the report should be attached in the notification email.
                    type: bool
                    required: false
                  notify:
                    description:
                    - List of report execution statuses that will trigger a notification.
                    choices:
                        - C(IN_QUEUE)
                        - C(IN_PROGRESS)
                        - C(COMPLETED)
                    type: list
                    elements: str
                    required: false
              webhook_name:
                description:
                  - The name of the webhook to be triggered for the report.
                type: str
                required: false
          view:
            description:
              - Contains view details such as subdata_category, fields, filters, and format for the report.
            type: dict
            required: true
            suboptions:
              view_name:
                description:
                  - The view name from which C(viewId) is derived.
                type: str
                required: true
                choices:
                  - Network Device Compliance # viewName in viewGroup Compliance
                  - Network Device Availability # viewName in viewGroup Network Devices
                  - Channel Change Count # viewName in viewGroup Network Devices
                  - Transmit Power Change Count # viewName in viewGroup Network Devices
                  - VLAN # viewName in viewGroup Network Devices
                  - Port Capacity # viewName in viewGroup Network Devices
                  - Energy Management # viewName in viewGroup Network Devices
                  - PoE # viewName in viewGroup Network Devices
                  - Device CPU and Memory Utilization # viewName in viewGroup Network Devices
                  - Network Interface Utilization # viewName in viewGroup Network Devices
                  - Executive Summary # viewName in viewGroup Executive Summary
                  - All Data # viewName in viewGroup Inventory
                  - Port Reclaim View # viewName in viewGroup Inventory
                  - All Data Version 2.0 # viewName in viewGroup Inventory
                  - All Data # viewName in viewGroup SWIM
                  - All Data Version 2.0 # viewName in viewGroup SWIM
                  - AP # viewName in viewGroup Access Point
                  - AP Radio # viewName in viewGroup Access Point
                  - AP - Usage and Client Breakdown # viewName in viewGroup Access Point
                  - Worst Interferers # viewName in viewGroup Access Point
                  - AP RRM Events # viewName in viewGroup Access Point
                  - AP Performance Report # viewName in viewGroup Long Term
                  - Long Term AP Detail # viewName in viewGroup Long Term
                  - Long Term AP Radio # viewName in viewGroup Long Term
                  - Long Term AP Usage and Client Breakdown # viewName in viewGroup Long Term
                  - Long Term Client Detail # viewName in viewGroup Long Term
                  - Long Term Client Session # viewName in viewGroup Long Term
                  - Long Term Network Device Availability # viewName in viewGroup Long Term
                  - Security Group to Security Group # viewName in viewGroup Group Pair Communication Analytics
                  - Security Group to ISE Endpoint Profile Group # viewName in viewGroup Group Pair Communication Analytics
                  - Security Group to Host Group # viewName in viewGroup Group Pair Communication Analytics
                  - ISE Endpoint Profile Group to Security Group # viewName in viewGroup Group Pair Communication Analytics
                  - ISE Endpoint Profile Group to ISE Endpoint Profile Group # viewName in viewGroup Group Pair Communication Analytics
                  - ISE Endpoint Profile Group to Host Group # viewName in viewGroup Group Pair Communication Analytics
                  - Host Group to Security Group # viewName in viewGroup Group Pair Communication Analytics
                  - Host Group to ISE Endpoint Profile Group # viewName in viewGroup Group Pair Communication Analytics
                  - Host Group to Host Group # viewName in viewGroup Group Pair Communication Analytics
                  - Device Lifecycle Information # viewName in viewGroup Telemetry
                  - Security Group to Security Groups # viewName in viewGroup Group Communication Summary
                  - Security Group to ISE Endpoint Profile Groups # viewName in viewGroup Group Communication Summary
                  - Security Group to Host Groups # viewName in viewGroup Group Communication Summary
                  - ISE Endpoint Profile Group to Security Groups # viewName in viewGroup Group Communication Summary
                  - ISE Endpoint Profile Group to ISE Endpoint Profile Groups # viewName in viewGroup Group Communication Summary
                  - ISE Endpoint Profile Group to Host Groups # viewName in viewGroup Group Communication Summary
                  - Host Group to Security Groups # viewName in viewGroup Group Communication Summary
                  - Host Group to ISE Endpoint Profile Group # viewName in viewGroup Group Communication Summary
                  - Host Group to Host Group # viewName in viewGroup Group Communication Summary
                  - EoX Data # viewName in viewGroup EoX
                  - Threat Detail # viewName in viewGroup Rogue and aWIPS
                  - New Threat # viewName in viewGroup Rogue and aWIPS
                  - Rogue Additional Detail # viewName in viewGroup Rogue and aWIPS
                  - Non Compliant Devices # viewName in viewGroup Licensing
                  - Non Compliance Summary # viewName in viewGroup Licensing
                  - AireOS Controllers Licenses # viewName in viewGroup Licensing
                  - License Usage Upload Details # viewName in viewGroup Licensing
                  - License Historical Usage # viewName in viewGroup Licensing
                  - Endpoint Profiling # viewName in viewGroup AI Endpoint Analytics
                  - Audit Log # viewName in viewGroup Audit Log
                  - Configuration Archive # viewName in viewGroup Configuration Archive
                  - Client # viewName in viewGroup Client
                  - Client Summary # viewName in viewGroup Client
                  - Top N Summary # viewName in viewGroup Client
                  - Client Detail # viewName in viewGroup Client
                  - Client Trend # viewName in viewGroup Client
                  - Client Session # viewName in viewGroup Client
                  - Busiest Client # viewName in viewGroup Client
                  - Unique Clients and Users Summary # viewName in viewGroup Client
              field_groups:
                description:
                  - Groups of fields to include in the report, as defined in the selected view.
                type: list
                elements: dict
                required: true
                suboptions:
                  name:
                    description:
                      - Name of the field group.
                    type: str
                    required: true
                  display_name:
                    description:
                      - UI display name of the field group.
                    type: str
                    required: true
                  fields:
                    description:
                      - List of fields to include within the field group.
                    type: list
                    elements: dict
                    required: true
                    suboptions:
                      name:
                        description:
                          - Field identifier.
                        type: str
                        required: true
                      display_name:
                        description:
                          - Field display name in the UI.
                        type: str
                        required: true
              format:
                description:
                  - Specifies the output format of the report.
                type: dict
                required: true
                suboptions:
                  format_type:
                    description:
                      - Type of format to be used.
                    choices:
                      - CSV
                      - PDF
                      - JSON
                      - TDE
                    type: str
                    required: true
              filters:
                description:
                  - Filters to be applied to narrow down the report data.
                type: list
                elements: dict
                required: false
                suboptions:
                  name:
                    description:
                      - Name of the filter.
                    type: str
                    required: true
                  display_name:
                    description:
                      - Display name of the filter.
                    type: str
                    required: true
                  type:
                    description:
                      - Type of the filter.
                    choices:
                      - MULTI_SELECT
                      - MULTI_SELECT_TREE
                      - SINGLE_SELECT_ARRAY
                      - TIME_RANGE
                    type: str
                    required: true
                  value:
                    description:
                      - Value(s) to apply in the filter.
                      - For C(TIME_RANGE), this is a dict with time_range_option, start_date_time, end_date_time, and time_zone_id.
                      - For others, this is a list of dicts with C(value) and C(display_value).
                    type: raw
                    required: true
requirements:
  - dnacentersdk >= 2.8.6
  - python >= 3.9
notes:
  - SDK Methods used are
    reports.Reports.get_all_view_groups
    reports.Reports.get_views_for_a_given_view_group
    reports.Reports.get_view_details_for_a_given_view_group_and_view
    reports.Reports.create_or_schedule_a_report
    reports.Reports.delete_a_scheduled_report
    reports.Reports.download_report_content
    reports.Reports.get_execution_id_by_report_id
  - Paths used are
    GET /dna/intent/api/v1/data/view-groups
    GET /dna/intent/api/v1/data/view-groups/{viewGroupId}
    GET /dna/intent/api/v1/data/view-groups/{viewGroupId}/views/{viewId}
    POST /dna/intent/api/v1/data/reports
    DELETE /dna/intent/api/v1/data/reports/{reportId}
    GET /dna/intent/api/v1/data/reports/{reportId}/executions/{executionId}
"""

EXAMPLES = r'''
- name: Create/Schedule a report configuration.
  cisco.dnac.reports_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log_level: DEBUG
    dnac_log: true
    state: merged
    config_verify: true
    config:
      - generate_report:
          - name: "compliance_report"
            view_group_name: "Compliance"
            deliveries:
              - type: "DOWNLOAD"
                file_path: "/Users/mekandar/Desktop"
            schedule:
              type: "SCHEDULE_NOW"
              time_zone: "Asia/Calcutta"
            view:
              view_name: "Network Device Compliance"
              field_groups:
                - name: "inventoryAllData"
              format:
                format_type: "CSV"
              filters: []
            tags: []

- name: Delete a report from Catalyst Center
  cisco.dnac.reports_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    state: deleted
    config_verify: true
    config:
      - generate_report:
          name: "compliance_report"  # The name of the report to be deleted
'''

RETURN = r"""
# Case 1: Successful Flexible Report Generation
response_create_or_schedule_a_report:
  description: Response returned after successfully generating or scheduling a report in Cisco Catalyst Center.
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

# Case 2: Successful Deletion of  Reports
response_delete_a_scheduled_report:
  description: Response returned after successfully deleting a scheduled report.
  returned: always
  type: dict
  sample: {
    "message": "string",
    "status": "integer"
  }

# Case 3: Successful Download of Reports
response_download_report_content:
  description: Contents of the report retrieved from Cisco Catalyst Center for download.
  returned: always
  type: str
  sample: "CSV-formatted string content or report data"
"""

from datetime import datetime
import time
import os
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
import json
import re


class Reports(DnacBase):
    """Class containing member attributes for Report Workflow Manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.state = self.params.get("state")
        self.result["response"] = []

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.

        Returns:
            self - The current object with Global Pool, Reserved Pool, Network Servers information.
        """

        temp_spec = {
            "generate_report": {
                "type": "list",
                "elements": "dict",
                "options": {
                    "name": {"type": "str", "required": True},
                    "view_group_name": {"type": "str", "required": True},
                    "tags": {
                        "type": "list",
                        "elements": "str",
                        "required": False
                    },
                    "schedule": {
                        "type": "dict",
                        "options": {
                            "type": {"type": "str", "required": True},
                            "date_time": {"type": "str", "required": False},
                            "time_zone_id": {"type": "str", "required": False}
                        }
                    },
                    "deliveries": {
                        "type": "dict",
                        "options": {
                            "type": {"type": "str", "required": True},
                            "location": {"type": "str", "required": False},
                            "email_addresses": {
                                "type": "list",
                                "elements": "str",
                                "required": False
                            },
                            "email_attach": {"type": "bool", "required": False},
                            "notify": {"type": "str", "required": False}
                        }
                    },
                    "view": {
                        "type": "dict",
                        "options": {
                            "view_name": {"type": "str", "required": True},
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
                                        # allows dict or list of dicts depending on filter type
                                        "type": "raw",
                                        "required": True
                                    }
                                }
                            }
                        }
                    }
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

    def input_data_validation(self, config):
        """
        Validate the input data provided in the playbook configuration.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.

        Returns:
            self: The current instance of the class with updated attribute.
        """

        self.log("Validating input data: {0}".format(self.pprint(config)), "DEBUG")
        generate_report = config.get("generate_report", [])
        for entry in generate_report:
            if not isinstance(entry, dict):
                self.msg = "Each entry in 'generate_report' must be a dictionary."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Validate required fields
            required_fields = ["view_group_name", "view", "schedule", "deliveries",]
            for field in required_fields:
                if field not in entry:
                    self.msg = f"Missing required field '{field}' in 'generate_report' entry."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

            # If 'name' is missing or empty, generate one dynamically
            if not entry.get("name"):
                timestamp = datetime.now().strftime("%b %d %Y %I:%M %p")  # e.g., Jul 20 2025 08:26 PM
                entry["name"] = f"{entry['data_category']} - {entry['view']['view_name']} - {timestamp}"

            deliveries = entry.get("deliveries", {})
            if deliveries:
                self.validate_deliveries(deliveries)

            # Pass default values for optional fields
            entry.setdefault("tags", [])
            entry.setdefault("view_group_version", "2.0.0")
            entry.get("view").setdefault("filters", [])
            self.log("view_group_version to {0}".format(entry["view_group_version"]), "DEBUG")
            if "view_group_version" not in entry:
                self.msg = "Missing required field 'view_group_version' in 'generate_report' entry."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            valid_schedule_type = ["SCHEDULE_NOW", "SCHEDULE_LATER", "SCHEDULE_RECURRENCE"]
            schedule_type = entry.get("schedule", {}).get("type")
            if not schedule_type:
                self.msg = "Missing required field 'schedule.type' in 'generate_report' entry."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            if schedule_type not in valid_schedule_type:
                self.msg = f"Invalid schedule type '{schedule_type}'. Must be one of {valid_schedule_type}."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            if schedule_type == "SCHEDULE_LATER":
                date_time = entry.get("schedule", {}).get("date_time")
                if not date_time:
                    self.msg = "Missing required field 'schedule.date_time' for 'SCHEDULE_LATER' in 'generate_report' entry."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Validate and convert date_time
                epoch_time = self.convert_to_epoch(date_time)
                if epoch_time is None:
                    self.msg = "Invalid date_time format. Expected 'YYYY-MM-DD HH:MM AM/PM'."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Store the converted epoch time back in the payload
                entry["schedule"]["date_time"] = epoch_time

            if schedule_type == "SCHEDULE_RECURRENCE":
                schedule = entry.get("schedule", {})
                recurrence = schedule.get("recurrence", {})
                recurrence_type = recurrence.get("type")
                time_zone = schedule.get("time_zone")
                recurrence_days = recurrence.get("days", [])
                date_time = entry.get("schedule", {}).get("date_time")

                # Ensure date_time is provided
                if "date_time" not in schedule or not schedule.get("date_time"):
                    self.msg = "Missing required schedule field: 'date_time'"
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Move date_time to time and start_date
                epoch_time = self.convert_to_epoch(date_time)
                schedule.pop("date_time")
                schedule["time"] = epoch_time
                schedule["start_date"] = epoch_time

                # Validate required fields
                required_fields = ["time_zone", "time", "start_date", "recurrence", "type"]
                for field in required_fields:
                    if field not in schedule:
                        self.msg = f"Missing required schedule field: '{field}'"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                # Case 1: Daily Recurrence via WEEKLY pattern with all days
                if recurrence_type == "WEEKLY":
                    if "days" not in schedule["recurrence"]:
                        self.msg = "Missing required schedule field: 'recurrence_days'"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self
                    expected_days = {"MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"}
                    if set(recurrence_days) != expected_days:
                        self.msg = "Only daily recurrence (WEEKLY with all 7 days) is supported in this module."
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                # Case 2: Monthly Recurrence
                elif recurrence_type == "MONTHLY":
                    last_day_of_month = recurrence.get("last_day_of_month", False)
                    day_of_month = recurrence.get("day_of_month")
                    if not last_day_of_month:
                        # Require dayOfMonth when lastDayOfMonth is false
                        if not isinstance(day_of_month, int) or not (1 <= day_of_month <= 31):
                            self.msg = (
                                "For MONTHLY recurrence, 'dayOfMonth' must be an integer between 1 and 31 "
                                "when 'lastDayOfMonth' is false."
                            )
                            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                    else:
                        # Ignore dayOfMonth if lastDayOfMonth is true
                        if "dayOfMonth" in recurrence:
                            self.log(
                                "'dayOfMonth' is ignored because 'lastDayOfMonth' is set to true.",
                                "DEBUG"
                            )
                            recurrence.pop("dayOfMonth")

                else:
                    # All other recurrence types are not supported
                    self.msg = f"Recurrence type '{recurrence_type}' is not supported in this module."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

            # Validate view structure
            view = entry.get("view", {})
            if not isinstance(view, dict):
                self.msg = "'view' must be a dictionary."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            filters = view.get("filters", [])
            if filters:
                if not isinstance(filters, list):
                    self.msg = "'filters' must be a list."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                for filter_entry in filters:
                    if not isinstance(filter_entry, dict):
                        self.msg = "Each filter entry must be a dictionary."
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    filter_value = filter_entry.get("value")
                    if filter_entry.get("name") == "Location" and filter_value:

                        # If value is not a list, assign empty list and skip
                        if not isinstance(filter_value, list):
                            if filter_value is None:
                                filter_entry["value"] = []
                                filter_entry["display_value"] = []
                                return self  # Assuming no location to process
                            else:
                                self.msg = "value for 'Location' filter must be a list."
                                self.set_operation_result("failed", False, self.msg, "ERROR")
                                return self

                        if isinstance(filter_value, list):
                            updated_values = []

                            for item in filter_value:
                                if not isinstance(item, dict) or "value" not in item:
                                    self.msg = "Each item in 'Location' filter value must contain 'value'."
                                    self.set_operation_result("failed", False, self.msg, "ERROR")
                                    return self

                                # Use provided display_value or fallback to value
                                display_value = item.get("display_value", item["value"])

                                # Call get_site to get the final resolved network hierarchy path
                                site_response = self.get_site(item["value"])
                                site_response = site_response["response"][0]
                                self.log("Site response: {0}".format(self.pprint(site_response)), "DEBUG")

                                site_hierarchy_id = site_response.get("siteHierarchyId")
                                if not site_hierarchy_id:
                                    self.msg = f"Failed to resolve siteHierarchyId for location: {item['value']}"
                                    self.set_operation_result("failed", False, self.msg, "ERROR")
                                    return self

                                # Append both value and display_value in the same item
                                updated_values.append({
                                    "value": site_hierarchy_id,
                                    "display_value": display_value
                                })

                            # Assign final list to filter_entry["value"]
                            filter_entry["value"] = updated_values

        return self

    def convert_to_epoch(self, date_str):
        """
        Convert a date string in the format 'YYYY-MM-DD HH:MM AM/PM' to epoch time in milliseconds.

        Parameters:
            date_str (str): Date and time string to be converted.
                Expected format: "YYYY-MM-DD HH:MM AM/PM"
                (e.g., "2025-09-02 07:30 PM").

        Returns:
            int | None: Epoch time in milliseconds if conversion succeeds,
            otherwise None if the input string is invalid or cannot be parsed.

        """
        try:
            time_struct = time.strptime(date_str, "%Y-%m-%d %I:%M %p")
            return int(time.mktime(time_struct) * 1000)
        except ValueError:
            self.log(f"exception occurred while converting date string to epoch time: {ValueError}", "ERROR")
            return None

    def validate_deliveries(self, deliveries):
        """
        Validate deliveries field according to rules:
        1. Must be a list with exactly one object.
        2. Type can be DOWNLOAD, NOTIFICATION (Email), or WEBHOOK.
        3. Enforce field-specific requirements for each type.

        Parameters:
            deliveries (list): User-provided delivery configuration.
                            Expected format varies by delivery type.

        Returns:
            bool: True if the input passes validation and normalization.
                False if the input is invalid, with error messages set
                in self.msg and logged via self.set_operation_result.

        """
        # 1. Check it's a list with exactly one object
        if not isinstance(deliveries, list) or len(deliveries) != 1:
            self.msg = (
                "'deliveries' must be a list containing exactly one delivery type object."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return False

        delivery = deliveries[0]
        if not isinstance(delivery, dict):
            self.msg = "Each delivery entry must be a dictionary."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return False

        delivery_type = delivery.get("type")
        if delivery_type not in ["DOWNLOAD", "NOTIFICATION", "WEBHOOK"]:
            self.msg = (
                f"Invalid delivery type '{delivery_type}'. Allowed types are: "
                "DOWNLOAD, NOTIFICATION (Email), WEBHOOK."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return False

        # 2. Type-specific validations
        if delivery_type == "DOWNLOAD":
            # No extra validation needed; default case
            pass

        elif delivery_type == "NOTIFICATION":
            # Must have notification_endpoints with EMAIL type
            endpoints = delivery.get("notification_endpoints", [])
            if not isinstance(endpoints, list) or len(endpoints) != 1:
                self.msg = "'notification_endpoints' must be a list containing exactly one endpoint."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

            endpoint = endpoints[0]
            # Default type to EMAIL if not provided
            endpoint_type = endpoint.get("type", "EMAIL")
            if endpoint_type != "EMAIL":
                self.msg = "'notification_endpoints[0].type' must be 'EMAIL'."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

            email_addresses = endpoint.get("email_addresses", [])
            if not isinstance(email_addresses, list) or not all(isinstance(e, str) for e in email_addresses):
                self.msg = "'email_addresses' must be a list of valid email strings."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

            # Map to API format
            api_endpoint = {
                "type": "EMAIL",
                "emailAddresses": email_addresses
            }

            # Optional email_attach
            email_attach = delivery.get("email_attach", False)
            if not isinstance(email_attach, bool):
                self.msg = "'email_attach' must be a boolean value."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

            # Optional notify array
            notify_values = ["IN_QUEUE", "IN_PROGRESS", "COMPLETED"]
            notify = delivery.get("notify", [])
            if notify and (not isinstance(notify, list) or not all(n in notify_values for n in notify)):
                self.msg = f"'notify' must be a list containing only: {notify_values}."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

            # Final normalized structure
            normalized_delivery = {
                "type": "NOTIFICATION",
                "notificationEndpoints": [api_endpoint],
                "emailAttach": email_attach,
                "notify": notify
            }

            # Replace original delivery with normalized one
            delivery.clear()
            delivery.update(normalized_delivery)

        elif delivery_type == "WEBHOOK":
            webhook_name = delivery.get("webhook_name")
            if not webhook_name or not isinstance(webhook_name, str):
                self.msg = "'webhook_name' is required for WEBHOOK delivery type."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return False

        return True

    def get_webhook_destination_in_ccc(self, name):
        """
        Retrieve details of Rest Webhook destinations present in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            name (str): The name of the syslog destination to retrieve details for.
        Returns:
            dict: A dictionary containing details of Rest Webhook destination present in Cisco Catalyst Center,
                or None if no Rest Webhook destinations are found.
        Description:
            This function retrieves the details of Rest Webhook destinations present in Cisco Catalyst Center
            using the 'event_management' API endpoint with the 'get_webhook_destination' function.
            If an error occurs during the retrieval process, it logs the error message and raises an Exception.
        """

        try:
            offset = 0
            limit = 10
            while True:
                try:
                    response = self.dnac._exec(
                        family="event_management",
                        function="get_webhook_destination",
                        params={"offset": offset * limit, "limit": limit},
                    )
                    offset = offset + 1
                    self.log(
                        "Received API response from 'get_webhook_destination': {0}".format(
                            str(response)
                        ),
                        "DEBUG",
                    )
                    response = response.get("statusMessage")

                    if not response:
                        self.log(
                            "There is no Rest Webhook destination present in Cisco Catalyst Center",
                            "INFO",
                        )
                        return response

                    for destination in response:
                        if destination.get("name") == name:
                            self.log(
                                "Webhook Destination '{0}' present in Cisco Catalyst Center".format(
                                    name
                                ),
                                "INFO",
                            )
                            return destination

                    time.sleep(1)
                except Exception as e:
                    expected_exception_msgs = [
                        "Expecting value: line 1 column 1",
                        "not iterable",
                        "has no attribute",
                    ]
                    for msg in expected_exception_msgs:
                        if msg in str(e):
                            self.log(
                                "An exception occurred while checking for the Webhook destination with the name '{0}'. "
                                "It was not found in Cisco Catalyst Center.".format(
                                    name
                                ),
                                "WARNING",
                            )
                            return None

        except Exception as e:
            self.status = "failed"
            self.msg = "Error while getting the details of Webhook destination(s) present in Cisco Catalyst Center: {0}".format(
                str(e)
            )
            self.log(self.msg, "ERROR")
            self.check_return_status()

    def get_want(self, config):
        """
        Retrieve and store assurance Health score details from playbook configuration.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing image import and other details.

        Returns:
            self: The current instance of the class with updated 'want' attributes.
        """
        self.log("Retrieving 'want' attributes from configuration: {0}".format(self.pprint(config)), "DEBUG")

        want = {"generate_report": config.get("generate_report", [])}
        if not want["generate_report"]:
            self.msg = "The 'generate_report' field is missing or empty in the configuration."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")
        return self

    def get_all_view_groups(self, view_group_name):
        """
        Retrieve all view groups from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            view_group_name (str): The name of the view group to retrieve.

        Returns:
            tuple[str, str] | object:
                - (view_group_id, data_category): When a matching view group is found.
                - self: If no view group is found or an error occurs, with error details
                logged and `self.msg` populated.
        """
        self.log("Retrieving all view groups for view_group_name: {0}".format(self.pprint(view_group_name)), "DEBUG")
        try:
            response = self.dnac._exec(
                family="reports",
                function="get_all_view_groups",
            )
            self.log("Response from get_all_view_groups: {0}".format(self.pprint(response)), "DEBUG")
            if not response:
                self.msg = "Failed to retrieve view groups from Cisco Catalyst Center."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self
            view_group_id = None
            for view_group_detail in response:
                if view_group_detail.get("name") == view_group_name:
                    self.log("Found data_category '{0}' in view groups.".format(view_group_name), "DEBUG")
                    view_group_id = view_group_detail.get("viewGroupId")
                    data_category = view_group_detail.get("category")
                    self.log("View group ID and data_category for view_group_name '{0}': {1}, {2}"
                             .format(view_group_name, view_group_id, data_category), "DEBUG")
                    break

            if not view_group_id:
                self.msg = "No view group found for view_group_name '{0}'.".format(view_group_name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                return self

            return view_group_id, data_category
        except Exception as e:
            self.msg = "An error occurred while retrieving all view groups: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

    def get_views_for_a_given_view_group(self, view_group_id, view_name):
        """
        Retrieve all views for a given view group from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            view_group_id (str): The ID of the view group for which to retrieve views.
            view_name (str): The name of the view to retrieve. If not provided, all views will be returned.

        Returns:
            str | object:
                - If a matching view is found: returns the view ID (str).
                - If no matching view is found or an error occurs: returns `self` with the operation
                result set to "failed".
        """
        self.log("Retrieving views for view group ID: {0}".format(view_group_id), "DEBUG")
        try:
            response = self.dnac._exec(
                family="reports",
                function="get_views_for_a_given_view_group",
                params={"view_group_id": view_group_id},
            )
            self.log("Response from get_views_for_a_given_view_group: {0}".format(self.pprint(response)), "DEBUG")
            if not response:
                self.msg = "Failed to retrieve views for view group ID '{0}'.".format(view_group_id)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            all_views_detail = response.get("views")
            self.log("All views detail for view group ID '{0}': {1}".format(view_group_id, self.pprint(all_views_detail)), "DEBUG")
            if not all_views_detail:
                self.msg = "No views found for view group ID '{0}'.".format(view_group_id)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Match the desired view by name
            if view_name:
                views_detail = None
                for view in all_views_detail:
                    if view.get("viewName") == view_name:
                        views_detail = view
                        self.log("Found view with name '{0}': {1}".format(view_name, self.pprint(views_detail)), "DEBUG")
                        break
                if not views_detail:
                    self.msg = "No views found with name '{0}' in view group ID '{1}'.".format(view_name, view_group_id)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                    return self

                view_id = views_detail.get("viewId")
                self.log("View ID for view name '{0}': {1}".format(view_name, view_id), "DEBUG")
                return view_id
        except Exception as e:
            self.msg = "An error occurred while retrieving views for view group ID '{0}': {1}".format(view_group_id, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

    def fetch_view_details(self, view_group_id, view_id):
        """
        Fetch view details for a given view group and view ID from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            view_group_id (str): The ID of the view group.
            view_id (str): The ID of the view.

        Returns:
            self: The current instance of the class with updated 'view_details' attribute.
        """
        self.log("Fetching view details for view group ID: {0}, view ID: {1}".format(view_group_id, view_id), "DEBUG")
        try:
            response = self.dnac._exec(
                family="reports",
                function="get_view_details_for_a_given_view_group_and_view",
                params={"view_group_id": view_group_id, "view_id": view_id},
            )
            self.log("Response from get_view_details_for_a_given_view_group_and_view: {0}".format(self.pprint(response)), "DEBUG")
            if not response:
                self.msg = "Failed to fetch view details for view group ID '{0}' and view ID '{1}'.".format(view_group_id, view_id)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.view_details = response
            self.log("Fetched view details: {0}".format(self.pprint(self.view_details)), "DEBUG")
        except Exception as e:
            self.msg = "An error occurred while fetching view details: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
        return self

    def get_have(self, config):
        """
        Retrieve and store the current state of the report from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing report details.

        Returns:
            self: The current instance of the class with updated 'have' attributes.
        """
        self.log("Retrieving 'have' attributes from configuration: {0}".format(self.pprint(config)), "DEBUG")
        generate_report = config.get("generate_report", [])

        for report_entry in generate_report:
            if report_entry.get("deliveries").get("type") == "WEBHOOK":
                webhook_name = report_entry.get("webhook_name")
                webhook_destinations = self.get_webhook_destination_in_ccc(webhook_name)
                if not webhook_destinations:
                    self.msg = f"No Webhook destination found in Cisco Catalyst Center for '{webhook_name}'."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return False
                webhookId = webhook_destinations.get("webhookId")
                report_entry["deliveries"]["webhook_id"] = webhookId
                report_entry["deliveries"].pop("webhook_name", None)

            view_group_name = report_entry.get("view_group_name")
            if not view_group_name:
                self.log(f"view_group_name '{view_group_name}' not found in view_groups_details", "WARNING")
                self.msg = "Mandatory parameter 'view_group_name' '{0}' not found in view_groups_details.".format(view_group_name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                return self

            view_group_id, data_category = self.get_all_view_groups(view_group_name)
            if view_group_id:
                report_entry["view_group_id"] = view_group_id
                report_entry["data_category"] = data_category
                self.log(f"Found view group ID '{view_group_id}' for view_group_name '{view_group_name}'", "DEBUG")
                view_name = report_entry["view"]["view_name"]
                view_id = self.get_views_for_a_given_view_group(view_group_id, view_name)
                if not view_id:
                    self.msg = "No views found for view group ID '{0}'.".format(view_group_id)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                    return self
                report_entry["view"]["view_id"] = view_id
                self.log(f"Mapped view_group_name '{view_group_name}' to view_group'_id '{view_group_id}'", "DEBUG")

            try:
                response = self.dnac._exec(
                    family="reports",
                    function="get_list_of_scheduled_reports",
                    params={
                        "viewGroupId": view_group_id,
                        "viewId": view_id
                    }
                )
                self.log("Response from get_list_of_scheduled_reports: {0}".format(self.pprint(response)), "DEBUG")
            except Exception as e:
                error_str = str(e)
                if "status_code: 404" in error_str or "\"status\":404" in error_str:
                    # Treat 404 as valid "not found"
                    self.msg = f"Report not found: {error_str}"
                    self.log(self.msg, "WARNING")
                    report_entry["exists"] = False
                    # Don't fail here, just return self
                    return self
                else:
                    self.msg = "An error occurred while checking for existing reports: {0}".format(str(e))
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self
            if not response and report_entry["exists"] is False:
                self.msg = "Failed to retrieve list of scheduled reports."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            report_name = report_entry.get("name")
            if not report_name:
                self.msg = "The 'name' field is mandatory in the 'generate_report' configuration."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # check if the report already exists
            get_list_of_scheduled_reports = response or []
            report_found = False

            for report in get_list_of_scheduled_reports:
                if report.get("name") == report_name:
                    self.log(f"Report '{report_name}' already exists.", "DEBUG")
                    report_entry["report_id"] = report.get("reportId")
                    report_entry["view_group_id"] = report.get("viewGroupId")
                    report_entry["view"]["view_id"] = report.get("view", {}).get("viewId")
                    report_entry["exists"] = True
                    report_found = True
                    self.log(report_entry, "DEBUG")
                    self.log(f"Report '{report_name}' exists with ID: {report.get('reportId')}", "DEBUG")
                    break

            if not report_found:
                self.log(f"Report '{report_name}' does not exist.", "DEBUG")
                report_entry["exists"] = False

        if self.state != "deleted":
            for report_entry in generate_report:
                view_group_id = report_entry.get("view_group_id")
                view_id = report_entry.get("view", {}).get("view_id")
                self.fetch_view_details(view_group_id, view_id)

        have = {"generate_report": config.get("generate_report", [])}
        self.have = have
        self.log("Current State (have): {0}".format(str(self.pprint(self.have))), "INFO")
        return self

    def snake_to_camel(self, snake_str):
        """Convert snake_case string to camelCase."""
        parts = snake_str.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])

    def convert_keys_to_camel_case(self, data):
        """
        Recursively convert all dict keys from snake_case to camelCase.
        Handles dicts, lists, and nested structures.
        """
        if isinstance(data, dict):
            new_dict = {}
            for k, v in data.items():
                new_key = self.snake_to_camel(k)
                new_dict[new_key] = self.convert_keys_to_camel_case(v)
            return new_dict
        elif isinstance(data, list):
            return [self.convert_keys_to_camel_case(item) for item in data]
        else:
            return data

    def create_n_schedule_reports(self, generate_report):
        """
        Create or schedule a report based on the provided configuration.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            generate_report (list): A list of report configurations to be created or scheduled.

        Returns:
            self: The current instance of the class with updated 'result' attribute.
        """
        self.log("Creating or scheduling reports with configuration: {0}".format(self.pprint(generate_report)), "DEBUG")
        if not generate_report:
            self.msg = "The 'generate_report' field is missing or empty in the configuration."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        try:
            for report_entry in generate_report:
                self.log("Processing report entry: {0}".format(self.pprint(report_entry)), "DEBUG")
                if not report_entry.get("name"):
                    self.msg = "The 'name' field is mandatory in the 'generate_report' configuration."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                if not report_entry.get("view_group_id"):
                    self.msg = "The 'view_group_id' field is mandatory in the 'generate_report' configuration."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                if not report_entry.get("view", {}).get("view_id"):
                    self.msg = "The 'view_id' field is mandatory in the 'view' configuration."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Check if the report already exists
                if report_entry.get("exists"):
                    report_id = report_entry.get("report_id")
                    self.log("Checking if report '{0}' with ID '{1}' already exists.".format(report_entry.get("name"), report_id), "DEBUG")
                    self.log("Report '{0}' already exists. Skipping creation.".format(report_entry.get("name")), "DEBUG")
                    result = {
                        "response": {
                            "report_id": report_entry.get("report_id"),
                            "view_group_id": report_entry.get("view_group_id"),
                            "view_id": report_entry.get("view", {}).get("view_id"),
                        },
                        "msg": "Report '{0}' already exists.".format(report_entry.get("name")),
                    }
                    self.result["response"].append({"create_report": result})
                    if any(d.get("type", "").lower() == "download" for d in report_entry.get("deliveries", [])):
                        self.log("Download requested for report '{0}'. Proceeding to download.".format(report_entry.get("name")), "DEBUG")
                        self.report_download(report_entry, report_entry.get("report_id"))
                    continue
                self.log("Processing report creation: {0}".format(self.pprint(report_entry)), "DEBUG")
                # Prepare the payload for creating or scheduling a report
                # --- Build Payload ---
                report_entry_camel = self.convert_keys_to_camel_case(report_entry)
                self.log("Converted report entry to camelCase: {0}".format(self.pprint(report_entry_camel)), "DEBUG")

                if "schedule" in report_entry_camel and "timeZone" in report_entry_camel["schedule"]:
                    report_entry_camel["schedule"]["timeZoneId"] = report_entry_camel["schedule"].pop("timeZone")

                if "view" in report_entry_camel and "format" in report_entry_camel["view"]:
                    format_dict = report_entry_camel["view"]["format"]
                    if "name" not in format_dict:
                        format_dict["name"] = format_dict.get("formatType", "CSV")

                    view_data = report_entry_camel["view"]
                    if "viewName" in view_data:
                        view_data["name"] = view_data.pop("viewName")

                self.log("Payload for create_or_schedule_a_report: {0}".format(self.pprint(report_entry_camel)), "DEBUG")
                response = self.dnac._exec(
                    family="reports",
                    function="create_or_schedule_a_report",
                    params=report_entry_camel
                )
                self.log("Response from create_or_schedule_a_report: {0}".format(self.pprint(response)), "DEBUG")
                if not response:
                    self.msg = "Failed to create or schedule report '{0}'.".format(report_entry.get("name"))
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self
                # Update result dictionary for success

                result = {
                    "response": {
                        "reportId": response.get("reportId"),
                        "viewGroupId": response.get("viewGroupId"),
                        "viewsId": response.get("view", {}).get("viewId"),
                    },
                    "msg": "Successfully created or scheduled report '{0}'.".format(report_entry.get("name"))
                }

                # Append once to final result
                self.result["response"].append({"create_report": result})
                self.log("Successfully created or scheduled report: {0}".format(report_entry.get("name")), "INFO")
                self.status = "success"
                self.result["changed"] = True
                if any(d.get("type", "").lower() == "download" for d in report_entry.get("deliveries", [])):
                    if report_entry_camel["schedule"].get("type") == "SCHEDULE_NOW":
                        self.log("Download requested for report '{0}'. Proceeding to download.".format(report_entry.get("name")), "DEBUG")
                        self.report_download(report_entry, response.get("reportId"))
        except Exception as e:
            self.msg = "An error occurred while creating or scheduling the report: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def get_diff_merged(self, config):
        """
        generate a customized report based on the configuration provided in the playbook.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing report details.

        Returns:
            self: The current instance of the class with updated 'diff' attributes.
        """
        self.log("Generating 'diff' for merged state from configuration: {0}".format(self.pprint(config)), "DEBUG")
        generate_report = config.get("generate_report", [])
        if not generate_report:
            self.msg = "The 'generate_report' field is missing or empty in the configuration."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.create_n_schedule_reports(generate_report).check_return_status()

        return self

    def get_execution_id_for_report(self, report_id):
        """
        Retrieve the execution ID for a given report ID from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            report_id (str): The ID of the report for which to retrieve the execution ID.

        Returns:
            str: The execution ID associated with the specified report ID.
        """
        time.sleep(20)  # Adding a delay to ensure the report is ready for execution
        self.log("Retrieving execution ID for report ID: {0}".format(report_id), "DEBUG")
        response = self.dnac._exec(
            family="reports",
            function="get_all_execution_details_for_a_given_report",
            params={"report_id": report_id}
        )
        self.log("Response from get_execution_id_for_report: {0}".format(self.pprint(response)), "DEBUG")
        if not response or not response.get("executions"):
            self.msg = "No executions found for report ID '{0}'.".format(report_id)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        # Assuming the first execution is the one we want
        execution_id = response["executions"][0].get("executionId")
        self.log("Execution ID for report ID '{0}': {1}".format(report_id, execution_id), "DEBUG")
        return execution_id

    def download_report_with_retry(self, report_id, execution_id):
        """
        Download report content from Catalyst Center with retry mechanism
        if the file is temporarily unavailable (404 - file removed).

        Parameters:
            report_id (str): The report ID.
            execution_id (str): The execution ID.

        Returns:
            download_data: The downloaded report content if successfully downloaded.
        """

        self.log(
            f"Attempting to download report with report_id={report_id}, execution_id={execution_id}",
            "INFO"
        )

        start_time = time.time()
        retry_interval = int(self.payload.get("dnac_task_poll_interval", 5))
        resync_retry_count = int(self.payload.get("dnac_api_task_timeout", 100))

        while True:
            try:
                download_response = self.dnac._exec(
                    family="reports",
                    function="download_report_content",
                    params={"report_id": report_id, "execution_id": execution_id}
                )

                download_data = download_response.data
                self.log(
                    "Response from download_report_content: {0}".format(download_data),
                    "DEBUG"
                )

                # If data is present and not error, return it
                if download_data and not isinstance(download_data, dict):
                    return download_data

            except Exception as e:
                err_str = str(e)
                error_code = None
                error_msg = None

                # Try to extract JSON part from exception
                match = re.search(r'(\{.*\})', err_str)
                if match:
                    try:
                        err_json = json.loads(match.group(1))
                        if "error" in err_json:
                            error_code = err_json["error"][0].get("errorCode")
                            error_msg = err_json["error"][0].get("errorMessage")
                    except json.JSONDecodeError:
                        pass

                if error_code == 4002:
                    self.log(
                        f"Report not ready yet (error {error_code}: {error_msg}), retrying...",
                        "WARNING"
                    )
                else:
                    self.msg = f"Exception during report download with retry: {err_str}"
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            # Timeout check
            if time.time() - start_time >= resync_retry_count:
                self.msg = f"Max retries reached. Report file not available (report_id={report_id}, execution_id={execution_id})."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            # Wait before retry
            self.log(
                f"Waiting {retry_interval} seconds before retrying report download (report_id={report_id}, execution_id={execution_id})",
                "DEBUG"
            )
            time.sleep(retry_interval)

    def report_download(self, report_entry, report_id):
        """
        Download the report content after it has been created or scheduled.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            report_entry (dict): The report entry containing details for downloading the report.
            response (dict): The response from the report creation or scheduling API call.

        Returns:
            self: The current instance of the class with updated 'result' attribute.
        """
        self.log("Downloading report content for report entry: {0}".format(self.pprint(report_entry)), "DEBUG")

        try:
            file_path = report_entry.get("file_path", "./")
            if not file_path:
                self.msg = "File path is required for downloading the report."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            execution_id = self.get_execution_id_for_report(report_id)
            if not execution_id:
                self.msg = "Failed to retrieve execution ID for report '{0}'.".format(report_entry.get("name"))
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            download_data = self.download_report_with_retry(report_id, execution_id)

            # Validate file_path
            deliveries = report_entry.get("deliveries", [])
            view = report_entry.get("view", {})
            file_format = view.get("format", {}).get("format_type")
            default_format = ".csv"  # Default file format if not specified

            for delivery in deliveries:
                if delivery.get("type", "").upper() == "DOWNLOAD" and "file_path" in delivery:
                    file_path = delivery["file_path"]
                    break  # Found it, no need to continue

            if not file_path:
                self.log("No 'file_path' provided. Cannot save the downloaded file.", "WARNING")
                self.msg = "File path is required for saving the downloaded report."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            # Determine file format
            if not file_format.startswith("."):
                file_format = "." + file_format  # Ensure it starts with "."

            # Determine file name (download_id or default name)
            report_name = report_entry.get("name", "report")

            # Construct full path
            full_path = os.path.join(file_path, f"{report_name}{file_format}")

            # Save the file
            try:
                os.makedirs(file_path, exist_ok=True)
                with open(full_path, "wb") as f:
                    f.write(download_data)
                self.log(f"File saved successfully at {full_path}", "INFO")
            except Exception as e:
                self.msg = "Failed to save the downloaded file: {0}".format(str(e))
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                return self

            result = {
                "response": download_data,
                "msg": "Successfully downloaded report '{0}' to '{1}'.".format(report_entry.get("name"), file_path),
            }
            self.result["response"].append({"download_report": result})
            self.log("Successfully downloaded report: {0}".format(report_entry.get("name")), "INFO")
            self.status = "success"
            self.result["changed"] = True
        except Exception as e:
            self.msg = "An error occurred while downloading the report: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
        return self

    def get_diff_deleted(self, config):
        """
        Delete a report based on the configuration provided in the playbook.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing report details.

        Returns:
            self: The current instance of the class with updated 'diff' attributes.
        """
        self.log("Starting deletion from configuration: {0}".format(self.pprint(config)), "DEBUG")
        generate_report = config.get("generate_report", [])
        if not generate_report:
            self.msg = "The 'generate_report' field is missing or empty in the configuration."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        try:
            for report_entry in generate_report:
                report_name = report_entry.get("name")
                self.log("Attempting to delete report: {0}".format(report_name), "DEBUG")
                if not report_entry.get("exists", False):
                    self.log("Report '{0}' does not exist, skipping deletion.".format(report_name), "DEBUG")
                    result = {
                        "response": {},
                        "msg": "Report '{0}' does not exist.".format(report_name),
                    }
                    self.result["response"].append({"delete_report": result})
                    self.msg = "Report '{0}' does not exist.".format(report_name)
                    self.log("Report '{0}' does not exist, skipping deletion.".format(report_name), "DEBUG")
                    continue
                if not report_entry.get("report_id"):
                    self.msg = "The 'report_id' field is mandatory in the 'generate_report' configuration for deletion."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                response = self.dnac._exec(
                    family="reports",
                    function="delete_a_scheduled_report",
                    params={"report_id": report_entry.get("report_id")},
                )
                self.log("Response from delete_a_scheduled_report: {0}".format(self.pprint(response)), "DEBUG")
                if not response.get("status") == 200:
                    self.msg = "Failed to delete report with ID '{0}'.".format(report_entry.get("report_id"))
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                result = {
                    "response": {},
                    "msg": "Report '{0}' has been successfully deleted.".format(report_entry.get("name")),
                }
                self.result["response"].append({"delete_report": result})
                self.msg = "Successfully deleted report with ID: {0}".format(report_entry.get("report_id"))
                self.log(self.msg, "INFO")
                self.status = "success"
                self.result["changed"] = True
        except Exception as e:
            self.msg = "An error occurred while deleting the report: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def verify_diff_merged(self, config):
        """ Verify the creation or scheduling of a report.
        This method checks if the specified report has been successfully created or scheduled in Cisco Catalyst Center.
        Returns:
            self: The current instance of the class with updated 'verify' attributes.
        """
        getattr(self, "get_have")(self.validated_config[0])
        generate_report = self.have.get("generate_report", [])
        if not generate_report:
            self.msg = "No reports found in the current state after creation."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self
        for report_entry in generate_report:
            if report_entry["exists"] is True and report_entry.get("deliveries"):
                report_name = report_entry.get("name")
                # Ensure "response" exists and has at least one item
                if "response" in self.result and self.result["response"]:
                    last_response = self.result["response"][-1]

                    # Check if "create_report" key exists, if not, create it
                    if "create_report" not in last_response:
                        last_response["create_report"] = {}

                    # Now safely assign the validation status
                    last_response["create_report"]["Validation"] = "Success"

                self.result["response"][-1]["create_report"]["Validation"] = "Success"
                self.msg = "Report '{0}' has been successfully created or scheduled.".format(report_name)
            else:
                self.log("Report '{0}' does not exist in the current state.".format(report_name), "DEBUG")
                self.msg = "Report '{0}' does not exist in the current state.".format(report_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

        return self

    def verify_diff_deleted(self, config):
        """ Verify the deletion of a report.
        This method checks if the specified report has been successfully deleted from Cisco Catalyst Center.
        Returns:
            self: The current instance of the class with updated 'verify' attributes.
        """
        getattr(self, "get_have")(self.validated_config[0])
        generate_report = self.have.get("generate_report", [])
        if not generate_report:
            self.msg = "No reports found in the current state after deletion."
            self.set_operation_result("Success", False, self.msg, "ERROR")
            return self

        for report_entry in generate_report:
            # Adding a delay to ensure the report deletion is processed
            report_name = report_entry.get("name")
            if not report_entry.get("exists", False):
                self.result["response"][-1]["delete_report"]["Validation"] = "Success"
                self.msg = "Report '{0}' has been successfully deleted.".format(report_name)
            else:
                self.log("Report '{0}' still exists in the current state.".format(report_name), "DEBUG")
                self.msg = "Report '{0}' still exists in the current state.".format(report_name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

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

    ccc_report = Reports(module)
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
        if state != "deleted":
            ccc_report.input_data_validation(config).check_return_status()
        ccc_report.get_want(config).check_return_status()
        ccc_report.get_have(config).check_return_status()
        ccc_report.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_report.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_report.result)


if __name__ == "__main__":
    main()

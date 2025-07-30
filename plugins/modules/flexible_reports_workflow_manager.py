#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform update Health score KPI's in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

import epdb

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
  - The Flexible Report APIs support multiple operations inluding fetching schedules, executing reports, and downloading results.
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
          type: str
          required: true
        tags:
          description: >
            Optional list of tags to filter reports.
          type: list
          elements: str
          required: false
        data_category:
          description: >
            The data_category of the report, as defined in Catalyst Center (e.g., "Inventory").
            Used to look up viewGroupId.
          choices:
            - Network #Compliance, Configuration Archive
            - Executive
            - Inventory
            - SWIM
            - AP
            - Cloud
            - Network Devices
            - Activity #Group Pair Communication Analytics, Group Communication Summary
            - Telemetry
            - EoX
            - Rogue and aWIPS
            - Licensing
            - AI Endpoint Analytics
            - AuditLog
            - Client
            - Security Advisories
          type: str
          required: false
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
            Contains view details such as subdata_category, fields, filters, and format for the report.
          type: dict
          required: true
          suboptions:
            subdata_category_name:
              description: >
                The subdata_category or view name from which viewId is derived.
              choices:
                - Network Device Compliance #viewname in viewGroup Compliance
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
                - Configuration Archive  #viewname in viewGroup Configuration Archive
                - Client #viewname in viewGroup Client
                - Client Summary # viewName in viewGroup Client
                - Top N Summary # viewName in viewGroup Client
                - Client Detail # viewName in viewGroup Client
                - Client Trend # viewName in viewGroup Client
                - Client Session # viewName in viewGroup Client
                - Busiest Client # viewName in viewGroup Client
                - Unique Clients and Users Summary # viewName in viewGroup Client
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
            view_group_name: "Inventory" # The name of the view group as defined in Catalyst Center - used to fetch viewGroupId
            tags: [] # Tags to filter reports (optional)
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
              subdata_category_name: "All Data"
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
              data_category: "Inventory" # The data_category as defined in Catalyst Center- used to fetch viewGroupId
              # subdata_category: "All Data" # (this is report subtype) From this subdata_category or view name, we need to fetch viewId (from viewGroupId we can fetch view and viewId based on the name of the view)
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
                subdata_category_name: "All Data"
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

from datetime import datetime
import time
import os
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
            # {"create_report": {"response": {}, "msg": {}}},
            # {"download_report": {"response": "", "msg": {}}},
            # {"delete_report": {"response": {}, "msg": {}}}
        ]
        self.create_report, self.update_report = [], []


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
                        "subdata_category_name": {"type": "str", "required": True},
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
            required_fields = ["view_group_name", "view"]
            for field in required_fields:
                if field not in entry:
                    self.msg = f"Missing required field '{field}' in 'generate_report' entry."
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

            # If 'name' is missing or empty, generate one dynamically
            if not entry.get("name"):
                timestamp = datetime.now().strftime("%b %d %Y %I:%M %p")  # e.g., Jul 20 2025 08:26 PM
                entry["name"] = f"{entry['data_category']} - {entry['view']['view_name']} - {timestamp}"

            #pass default values for optional fields
            entry.setdefault("tags", [])
            entry.setdefault("view_group_version", "2.0.0")
            entry.get("view").setdefault("filters", [])
            self.log("view_group_version to {0}".format(entry["view_group_version"]), "DEBUG")
            if "view_group_version" not in entry:
                self.msg = "Missing required field 'view_group_version' in 'generate_report' entry."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Validate view structure
            view = entry.get("view", {})
            if not isinstance(view, dict):
                self.msg = "'view' must be a dictionary."
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

        # self.config = config
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
            view_group_id (str): The ID of the view group that matches the specified name.
            If no view group is found for the specified name, returns None and sets an error message
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
                  self.log("View group ID and data_category for view_group_name '{0}': {1}, {2}".format(view_group_name, view_group_id, data_category), "DEBUG")
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
            list: A list of views associated with the specified view group.
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
            None: This method updates the 'view_details' attribute of the instance with the fetched details.
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
        Retrieve and store the current state of the flexible report from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing report details.

        Returns:
            self: The current instance of the class with updated 'have' attributes.
        """
        self.log("Retrieving 'have' attributes from configuration: {0}".format(self.pprint(config)), "DEBUG")
        # view_groups_details = self.get_all_view_groups(config)
        # view_details = self.get_view_details()
        generate_report = config.get("generate_report", [])

        for report_entry in generate_report:
          #check if the report already exists
          try:
              response = self.dnac._exec(
                  family="reports",
                  function="get_list_of_scheduled_reports",
              )
              self.log("Response from get_list_of_scheduled_reports: {0}".format(self.pprint(response)), "DEBUG")
          except Exception as e:
              self.msg = "An error occurred while checking for existing reports: {0}".format(str(e))
              self.set_operation_result("failed", False, self.msg, "ERROR")
              return self
          if not response:
              self.msg = "Failed to retrieve list of scheduled reports."
              self.set_operation_result("failed", False, self.msg, "ERROR")
              return self
          get_list_of_scheduled_reports = response
          report_name = report_entry.get("name")
          if not report_name:
              self.msg = "The 'name' field is mandatory in the 'generate_report' configuration."
              self.set_operation_result("failed", False, self.msg, "ERROR")
              return self

          for report in get_list_of_scheduled_reports:
              if report.get("name") == report_name:
                  self.log(f"Report '{report_name}' already exists.", "DEBUG")
                  report_entry["report_id"] = report.get("reportId")
                  report_entry["view_group_id"] = report.get("viewGroupId")
                  report_entry["view"]["views_id"] = report.get("view", {}).get("viewsId")
                  report_entry["exists"] = True
                  self.log(f"Report '{report_name}' exists with ID: {report.get('reportId')}", "DEBUG")
                  break
              else:
                  self.log(f"Report '{report_name}' does not exist.", "DEBUG")
                  report_entry["exists"] = False

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
              report_entry["view"]["views_id"] = view_id
              self.log(f"Mapped view_group_name '{view_group_name}' to view_group'_id '{view_group_id}'", "DEBUG")

        for report_entry in generate_report:
          view_group_id = report_entry.get("view_group_id")
          view_id = report_entry.get("view", {}).get("views_id")
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
            None: This method updates the 'result' attribute with the response from the report creation API call.
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

              if not report_entry.get("view", {}).get("views_id"):
                  self.msg = "The 'views_id' field is mandatory in the 'view' configuration."
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
                          "views_id": report_entry.get("view", {}).get("views_id"),
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
              result["response"].update({
                  "reportId": response.get("reportId"),
                  "viewGroupId": response.get("viewGroupId"),
                  "viewsId": response.get("view", {}).get("viewId"),
              })
              result["msg"] = "Successfully created or scheduled report '{0}'.".format(report_entry.get("name"))

              # Append once to final result
              self.result["response"].append({"create_report": result})
              self.log("Successfully created or scheduled report: {0}".format(report_entry.get("name")), "INFO")
              self.status="success"
              self.result["changed"]=True
              if any(d.get("type", "").lower() == "download" for d in report_entry.get("deliveries", [])):
                  self.log("Download requested for report '{0}'. Proceeding to download.".format(report_entry.get("name")), "DEBUG")
                  self.report_download(report_entry, response.get("reportId"))
        except Exception as e:
            self.msg = "An error occurred while creating or scheduling the report: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self  
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
            str: The execution ID associated with the specified report ID, or None if not found.
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
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

        # Assuming the first execution is the one we want
        execution_id = response["executions"][0].get("executionId")
        self.log("Execution ID for report ID '{0}': {1}".format(report_id, execution_id), "DEBUG")
        return execution_id

    def report_download(self, report_entry, report_id):
        """
        Download the report content after it has been created or scheduled.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            report_entry (dict): The report entry containing details for downloading the report.
            response (dict): The response from the report creation or scheduling API call.

        Returns:
            None: This method updates the 'result' attribute with the downloaded report content.
        """
        # import epdb;
        # epdb.serve(port=8888)
        self.log("Downloading report content for report entry: {0}".format(self.pprint(report_entry)), "DEBUG")

        # try:
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

        download_response = self.dnac._exec(
            family="reports",
            function="download_report_content",
            params={"report_id": report_id,
                    "execution_id": execution_id
                  }
        )
        # download_response = download_response.data
        self.log(download_response.data)
        # self.log("Response from download_report_content: {0}".format(self.pprint(download_response)), "DEBUG")

        if not download_response:
            self.msg = "Failed to download report content for '{0}'.".format(report_entry.get("name"))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return

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
            return

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
                f.write(download_response)
            self.log(f"File saved successfully at {full_path}", "INFO")
        except Exception as e:
            self.log(f"Failed to save file: {e}", "ERROR")

        result = {
            "response": download_response,
            "msg": "Successfully downloaded report '{0}' to '{1}'.".format(report_entry.get("name"), file_path),
        }
        self.result["response"].append({"download_report": result})
        self.log("Successfully downloaded report: {0}".format(report_entry.get("name")), "INFO")
        self.status = "success"
        self.result["changed"] = True
        # except Exception as e:
        #     self.msg = "An error occurred while downloading the report: {0}".format(str(e))
        #     self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
        return self

    def get_diff_deleted(self, config):
        """
        Delete a flexible report based on the configuration provided in the playbook.

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
              if not response.get("status")==200:
                  self.msg = "Failed to delete report with ID '{0}'.".format(report_entry.get("report_id"))
                  self.set_operation_result("failed", False, self.msg, "ERROR")
                  return self

              result = {
                      "response": {},
                      "msg": "Report '{0}' has been successfully deleted.".format(report_entry.get(report_name)),
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
        """ Verify the creation or scheduling of a flexible report.
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
            if report_entry["exists"] == True:
                report_name = report_entry.get("name")
                self.result["response"][-1]["create_report"]["Validation"] = "Success"
                self.msg = "Report '{0}' has been successfully created or scheduled.".format(report_name)
            else:
                self.log("Report '{0}' does not exist in the current state.".format(report_name), "DEBUG")
                self.msg = "Report '{0}' does not exist in the current state.".format(report_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

        return self

    def verify_diff_deleted(self, config):
        """ Verify the deletion of a flexible report.
        This method checks if the specified report has been successfully deleted from Cisco Catalyst Center.
        Returns:
            self: The current instance of the class with updated 'verify' attributes.
        """
        getattr(self, "get_have")(self.validated_config[0])
        generate_report = self.have.get("generate_report", [])
        if not generate_report:
            self.msg = "No reports found in the current state after deletion."
            self.set_operation_result("failed", False, self.msg, "ERROR")
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

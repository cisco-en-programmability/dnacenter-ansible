#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_info
short_description: Information module for Network Device Maintenance Schedules
description:
  - Get all Network Device Maintenance Schedules.
  - Get Network Device Maintenance Schedules by id.
  - API to retrieve the maintenance schedule information for the given id. - > This API retrieves a list of scheduled maintenance
    windows for network devices based on filter parameters. Each maintenance window is composed of a start schedule and end
    schedule, both of which have unique identifiers `startId` and `endId`. These identifiers can be used to fetch the status
    of the start schedule and end schedule using the `GET /dna/intent/api/v1/activities/{id}` API. Completed maintenance schedules
    are automatically removed from the system after two weeks. The API returns a paginated response based on 'limit' and 'offset'
    parameters, allowing up to 500 records per page. 'limit' specifies the number of records, and 'offset' sets the starting
    point using 1-based indexing. Use '/dna/intent/api/v1/networkDeviceMaintenanceSchedules/count' API to get the total record
    count. For data sets over 500 records, make multiple calls, adjusting 'limit' and 'offset' to retrieve all records incrementally.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceIds:
    description:
      - NetworkDeviceIds query parameter. List of network device ids.
    type: str
  status:
    description:
      - >
        Status query parameter. The status of the maintenance schedule. Possible values are UPCOMING,
        IN_PROGRESS, COMPLETED, FAILED. Refer features for more details.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page. Min 1, Max 500.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
  id:
    description:
      - Id path parameter. Unique identifier for the maintenance schedule.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices RetrieveScheduledMaintenanceWindowsForNetworkDevices
    description: Complete reference of the RetrieveScheduledMaintenanceWindowsForNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-scheduled-maintenance-windows-for-network-devices
  - name: Cisco DNA Center documentation for Devices RetrievesTheMaintenanceScheduleInformation
    description: Complete reference of the RetrievesTheMaintenanceScheduleInformation API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-maintenance-schedule-information
notes:
  - SDK Method used are
    devices.Devices.retrieve_scheduled_maintenance_windows_for_network_devices,
    devices.Devices.retrieves_the_maintenance_schedule_information,
  - Paths used are
    get /dna/intent/api/v1/networkDeviceMaintenanceSchedules,
    get /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id},
"""

EXAMPLES = r"""
---
- name: Get all Network Device Maintenance Schedules
  cisco.dnac.network_device_maintenance_schedules_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceIds: string
    status: string
    limit: 0
    offset: 0
    sortBy: string
    order: string
  register: result
- name: Get Network Device Maintenance Schedules by id
  cisco.dnac.network_device_maintenance_schedules_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "description": "string",
          "maintenanceSchedule": {
            "startId": "string",
            "endId": "string",
            "startTime": 0,
            "endTime": 0,
            "recurrence": {
              "interval": 0,
              "recurrenceEndTime": 0
            },
            "status": "string"
          },
          "networkDeviceIds": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_info
short_description: Information module for Network Device Maintenance Schedules Info
description:
  - This module represents an alias of the module network_device_maintenance_schedules_v1_info
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
        Status query parameter. The status of the maintenance schedule. Possible values
        are UPCOMING, IN_PROGRESS,
        COMPLETED, FAILED. Refer features for more details.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page. Min 1,
        Max 500.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: str
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used
        to sort the response.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices RetrieveScheduledMaintenanceWindowsForNetworkDevicesV1
    description: Complete reference of the RetrieveScheduledMaintenanceWindowsForNetworkDevicesV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-scheduled-maintenance-windows-for-network-devices
notes:
  - SDK Method used are devices.Devices.retrieve_scheduled_maintenance_windows_for_network_devices_v1,
  - Paths used are get /dna/intent/api/v1/networkDeviceMaintenanceSchedules,
  - It should be noted that this module is an alias of network_device_maintenance_schedules_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Device Maintenance Schedules Info
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
    limit: string
    offset: string
    sortBy: string
    order: string
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

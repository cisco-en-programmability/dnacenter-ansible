#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_id
short_description: Resource module for Network Device Maintenance Schedules Id
description:
- This module represents an alias of the module network_device_maintenance_schedules_id_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  description:
    description: A brief narrative describing the maintenance schedule.
    type: str
  id:
    description: Id path parameter. Unique identifier for the maintenance schedule.
    type: str
  maintenanceSchedule:
    description: Network Device Maintenance Schedules Id's maintenanceSchedule.
    suboptions:
      endTime:
        description: End time indicates the ending of the maintenance window in Unix
          epoch time in milliseconds.
        type: float
      recurrence:
        description: Network Device Maintenance Schedules Id's recurrence.
        suboptions:
          interval:
            description: Interval for recurrence in days. The interval must be longer
              than the duration of the schedules. The maximum allowed interval is 365
              days.
            type: int
          recurrenceEndTime:
            description: The end date for the recurrence in Unix epoch time in milliseconds.
              Recurrence end time should be greater than maintenance end date/time.
            type: float
        type: dict
      startTime:
        description: Start time indicates the beginning of the maintenance window in
          Unix epoch time in milliseconds.
        type: float
    type: dict
  networkDeviceIds:
    description: List of network device ids. This field is applicable only during creation
      of schedules; for updates, it is read-only.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices DeleteMaintenanceScheduleV1
  description: Complete reference of the DeleteMaintenanceScheduleV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-maintenance-schedule
- name: Cisco DNA Center documentation for Devices UpdatesTheMaintenanceScheduleInformationV1
  description: Complete reference of the UpdatesTheMaintenanceScheduleInformationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!updates-the-maintenance-schedule-information
notes:
  - SDK Method used are
    devices.Devices.delete_maintenance_schedule_v1,
    devices.Devices.updates_the_maintenance_schedule_information_v1,

  - Paths used are
    delete /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id},
    put /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id},
  - It should be noted that this module is an alias of network_device_maintenance_schedules_id_v1

"""

EXAMPLES = r"""
- name: Update by id
  cisco.dnac.network_device_maintenance_schedules_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    id: string
    maintenanceSchedule:
      endTime: 0
      recurrence:
        interval: 0
        recurrenceEndTime: 0
      startTime: 0
    networkDeviceIds:
    - string

- name: Delete by id
  cisco.dnac.network_device_maintenance_schedules_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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

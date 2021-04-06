#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_replacement
short_description: Manage DeviceReplacement objects of DeviceReplacement
description:
- >
   Get list of replacement devices with replacement details and it can filter replacement devices based on Faulty Device Name,Faulty Device Platform,
   Replacement Device Platform, Faulty Device Serial Number,Replacement Device Serial Number, Device Replacement status, Product Family.
- Marks device for replacement.
- UnMarks device for replacement.
- Get replacement devices count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  family:
    description:
    - List of families[Routers, Switches and Hubs, AP].
    type: str
  faulty_device_name:
    description:
    - Faulty Device Name.
    type: str
  faulty_device_platform:
    description:
    - Faulty Device Platform.
    type: str
  faulty_device_serial_number:
    description:
    - Faulty Device Serial Number.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: int
  offset:
    description:
    - Offset query parameter.
    type: int
  replacement_device_platform:
    description:
    - Replacement Device Platform.
    type: str
  replacement_device_serial_number:
    description:
    - Replacement Device Serial Number.
    type: str
  replacement_status:
    description:
    - >
       Device Replacement status [READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR,
       NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED].
    - Device Replacement status list[READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR].
    type: str
  sort_by:
    description:
    - SortBy this field. SortBy is mandatory when order is used.
    type: str
  sort_order:
    description:
    - Order on displayName[ASC,DESC].
    type: str
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      creationTime:
        description:
        - It is the device replacement's creationTime.
        type: int
      family:
        description:
        - It is the device replacement's family.
        type: str
      faultyDeviceId:
        description:
        - It is the device replacement's faultyDeviceId.
        - Required for states create and update.
        type: str
      faultyDeviceName:
        description:
        - It is the device replacement's faultyDeviceName.
        type: str
      faultyDevicePlatform:
        description:
        - It is the device replacement's faultyDevicePlatform.
        type: str
      faultyDeviceSerialNumber:
        description:
        - It is the device replacement's faultyDeviceSerialNumber.
        type: str
      id:
        description:
        - It is the device replacement's id.
        type: str
      neighbourDeviceId:
        description:
        - It is the device replacement's neighbourDeviceId.
        type: str
      networkReadinessTaskId:
        description:
        - It is the device replacement's networkReadinessTaskId.
        type: str
      replacementDevicePlatform:
        description:
        - It is the device replacement's replacementDevicePlatform.
        type: str
      replacementDeviceSerialNumber:
        description:
        - It is the device replacement's replacementDeviceSerialNumber.
        type: str
      replacementStatus:
        description:
        - It is the device replacement's replacementStatus.
        - Required for states create and update.
        type: str
      replacementTime:
        description:
        - It is the device replacement's replacementTime.
        type: int
      workflowId:
        description:
        - It is the device replacement's workflowId.
        type: str

  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_replacement
# Reference by Internet resource
- name: DeviceReplacement reference
  description: Complete reference of the DeviceReplacement object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceReplacement reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: return_replacement_devices_with_details
  cisco.dnac.device_replacement:
    state: query  # required
    family: SomeValue  # string
    faulty_device_name: SomeValue  # string
    faulty_device_platform: SomeValue  # string
    faulty_device_serial_number: SomeValue  # string
    limit: 1  #  integer
    offset: 1  #  integer
    replacement_device_platform: SomeValue  # string
    replacement_device_serial_number: SomeValue  # string
    replacement_status: SomeValue  # string
    sort_by: SomeValue  # string
    sort_order: SomeValue  # string
  register: query_result

- name: mark_device_for_replacement
  cisco.dnac.device_replacement:
    state: create  # required
    payload:  # required
    - faultyDeviceId: SomeValue  # string, required
      replacementStatus: SomeValue  # string, required
      creationTime: 1  #  integer
      family: SomeValue  # string
      faultyDeviceName: SomeValue  # string
      faultyDevicePlatform: SomeValue  # string
      faultyDeviceSerialNumber: SomeValue  # string
      id: SomeValue  # string
      neighbourDeviceId: SomeValue  # string
      networkReadinessTaskId: SomeValue  # string
      replacementDevicePlatform: SomeValue  # string
      replacementDeviceSerialNumber: SomeValue  # string
      replacementTime: 1  #  integer
      workflowId: SomeValue  # string

- name: unmark_device_for_replacement
  cisco.dnac.device_replacement:
    state: update  # required
    payload:  # required
    - faultyDeviceId: SomeValue  # string, required
      replacementStatus: SomeValue  # string, required
      creationTime: 1  #  integer
      family: SomeValue  # string
      faultyDeviceName: SomeValue  # string
      faultyDevicePlatform: SomeValue  # string
      faultyDeviceSerialNumber: SomeValue  # string
      id: SomeValue  # string
      neighbourDeviceId: SomeValue  # string
      networkReadinessTaskId: SomeValue  # string
      replacementDevicePlatform: SomeValue  # string
      replacementDeviceSerialNumber: SomeValue  # string
      replacementTime: 1  #  integer
      workflowId: SomeValue  # string

- name: return_replacement_devices_count
  cisco.dnac.device_replacement:
    state: query  # required
    count: True  # boolean, required
    replacement_status: SomeValue  # string
  register: query_result

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: array
  sample:
"""

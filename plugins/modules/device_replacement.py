#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_replacement
short_description: Resource module for Device Replacement
description:
- Manage operations create and update of the resource Device Replacement.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Device Replacement's payload.
    suboptions:
      creationTime:
        description: Device Replacement's creationTime.
        type: int
      family:
        description: Device Replacement's family.
        type: str
      faultyDeviceId:
        description: Device Replacement's faultyDeviceId.
        type: str
      faultyDeviceName:
        description: Device Replacement's faultyDeviceName.
        type: str
      faultyDevicePlatform:
        description: Device Replacement's faultyDevicePlatform.
        type: str
      faultyDeviceSerialNumber:
        description: Device Replacement's faultyDeviceSerialNumber.
        type: str
      id:
        description: Device Replacement's id.
        type: str
      neighbourDeviceId:
        description: Device Replacement's neighbourDeviceId.
        type: str
      networkReadinessTaskId:
        description: Device Replacement's networkReadinessTaskId.
        type: str
      replacementDevicePlatform:
        description: Device Replacement's replacementDevicePlatform.
        type: str
      replacementDeviceSerialNumber:
        description: Device Replacement's replacementDeviceSerialNumber.
        type: str
      replacementStatus:
        description: Device Replacement's replacementStatus.
        type: str
      replacementTime:
        description: Device Replacement's replacementTime.
        type: int
      workflowId:
        description: Device Replacement's workflowId.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Device Replacement reference
  description: Complete reference of the Device Replacement object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.device_replacement:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:

- name: Create
  cisco.dnac.device_replacement:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:

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

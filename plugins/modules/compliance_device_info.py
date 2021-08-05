#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_device_info
short_description: Information module for Compliance Device
description:
- Get all Compliance Device.
- Get Compliance Device by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceUuid:
    description:
    - DeviceUuid path parameter.
    type: str
  complianceStatus:
    description:
    - >
      ComplianceStatus query parameter. Compliance status can be have value among
      'COMPLIANT','NON_COMPLIANT','IN_PROGRESS', 'ERROR'.
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting row.
    type: int
  limit:
    description:
    - Limit query parameter. Number of records to be retrieved.
    type: int
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Compliance Device reference
  description: Complete reference of the Compliance Device object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Compliance Device
  cisco.dnac.compliance_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    complianceStatus: string
    deviceUuid: string
    offset: 0
    limit: 0
  register: result

- name: Get Compliance Device by id
  cisco.dnac.compliance_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceUuid: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "deviceUuid": "string",
        "complianceStatus": "string",
        "message": "string",
        "scheduleTime": 0,
        "lastUpdateTime": 0
      }
    }
"""

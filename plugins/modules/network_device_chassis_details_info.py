#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_chassis_details_info
short_description: Information module for Network Device Chassis Details
description:
- Get all Network Device Chassis Details.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceId:
    description:
    - DeviceId path parameter. Device ID.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Network Device Chassis Details reference
  description: Complete reference of the Network Device Chassis Details object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Device Chassis Details
  cisco.dnac.network_device_chassis_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
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
          "assemblyNumber": "string",
          "assemblyRevision": "string",
          "containmentEntity": "string",
          "description": "string",
          "entityPhysicalIndex": "string",
          "hardwareVersion": "string",
          "instanceUuid": "string",
          "isFieldReplaceable": "string",
          "isReportingAlarmsAllowed": "string",
          "manufacturer": "string",
          "name": "string",
          "partNumber": "string",
          "serialNumber": "string",
          "vendorEquipmentType": "string"
        }
      ],
      "version": "string"
    }
"""
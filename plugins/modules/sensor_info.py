#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sensor_info
short_description: Information module for Sensor
description:
- Get all Sensor.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sensor reference
  description: Complete reference of the Sensor object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sensor
  cisco.dnac.sensor_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    siteId: string
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
      "response": [
        {
          "name": "string",
          "status": "string",
          "radioMacAddress": "string",
          "ethernetMacAddress": "string",
          "location": "string",
          "backhaulType": "string",
          "serialNumber": "string",
          "ipAddress": "string",
          "version": "string",
          "lastSeen": 0,
          "type": "string",
          "sshConfig": {
            "sshState": "string",
            "sshUserName": "string",
            "sshPassword": "string",
            "enablePassword": "string"
          },
          "isLEDEnabled": true
        }
      ]
    }
"""

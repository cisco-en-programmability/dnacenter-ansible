#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sensor_info
short_description: Information module for Sensor Info
description:
- This module represents an alias of the module sensor_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
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
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors SensorsV1
  description: Complete reference of the SensorsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!sensors
notes:
  - SDK Method used are
    sensors.Sensors.sensors_v1,

  - Paths used are
    get /dna/intent/api/v1/sensor,
  - It should be noted that this module is an alias of sensor_v1_info

"""

EXAMPLES = r"""
- name: Get all Sensor Info
  cisco.dnac.sensor_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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
          "ssh": {
            "sshState": "string",
            "sshUserName": "string",
            "sshPassword": "string",
            "enablePassword": "string"
          },
          "led": true
        }
      ]
    }
"""

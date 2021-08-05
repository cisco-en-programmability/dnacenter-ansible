#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: threat_summary
short_description: Resource module for Threat Summary
description:
- Manage operation create of the resource Threat Summary.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  endTime:
    description: Threat Summary's endTime.
    type: int
  siteId:
    description: Threat Summary's siteId.
    elements: str
    type: list
  startTime:
    description: Threat Summary's startTime.
    type: int
  threatLevel:
    description: Threat Summary's threatLevel.
    elements: str
    type: list
  threatType:
    description: Threat Summary's threatType.
    elements: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Threat Summary reference
  description: Complete reference of the Threat Summary object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.threat_summary:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    endTime: 0
    siteId:
    - string
    startTime: 0
    threatLevel:
    - string
    threatType:
    - string

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
        "timestamp": 0,
        "threatData": [
          {
            "threatType": "string",
            "threatLevel": "string",
            "threatCount": 0
          }
        ]
      }
    }
"""

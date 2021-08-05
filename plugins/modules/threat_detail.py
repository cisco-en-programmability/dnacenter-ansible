#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: threat_detail
short_description: Resource module for Threat Detail
description:
- Manage operation create of the resource Threat Detail.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  endTime:
    description: Threat Detail's endTime.
    type: int
  isNewThreat:
    description: IsNewThreat flag.
    type: bool
  limit:
    description: Threat Detail's limit.
    type: int
  offset:
    description: Threat Detail's offset.
    type: int
  siteId:
    description: Threat Detail's siteId.
    elements: str
    type: list
  startTime:
    description: Threat Detail's startTime.
    type: int
  threatLevel:
    description: Threat Detail's threatLevel.
    elements: str
    type: list
  threatType:
    description: Threat Detail's threatType.
    elements: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Threat Detail reference
  description: Complete reference of the Threat Detail object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.threat_detail:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    endTime: 0
    isNewThreat: true
    limit: 0
    offset: 0
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
      "totalCount": 0,
      "response": [
        {
          "macAddress": "string",
          "updatedTime": 0,
          "vendor": "string",
          "threatType": "string",
          "threatLevel": [],
          "apName": "string",
          "ssid": "string",
          "siteNameHierarchy": "string"
        }
      ]
    }
"""

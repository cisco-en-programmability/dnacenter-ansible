#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_info
short_description: Information module for Event
description:
- Get all Event.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  eventId:
    description:
    - EventId query parameter. The registered EventId should be provided.
    type: str
  tags:
    description:
    - Tags query parameter. The registered Tags should be provided.
    type: str
  offset:
    description:
    - Offset query parameter. The number of Registries to offset in the resultset whose default value 0.
    type: int
  limit:
    description:
    - Limit query parameter. The number of Registries to limit in the resultset whose default value 10.
    type: int
  sortBy:
    description:
    - SortBy query parameter. SortBy field name.
    type: str
  order:
    description:
    - Order query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event reference
  description: Complete reference of the Event object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Event
  cisco.dnac.event_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    eventId: string
    tags: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "eventId": "string",
        "nameSpace": "string",
        "name": "string",
        "description": "string",
        "version": "string",
        "category": "string",
        "domain": "string",
        "subDomain": "string",
        "type": "string",
        "tags": [
          "string"
        ],
        "severity": 0,
        "details": {},
        "subscriptionTypes": [
          "string"
        ]
      }
    ]
"""
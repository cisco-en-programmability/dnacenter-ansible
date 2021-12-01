#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery_summary_info
short_description: Information module for Discovery Summary
description:
- Get all Discovery Summary.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Discovery ID.
    type: str
  taskId:
    description:
    - TaskId query parameter.
    type: str
  sortBy:
    description:
    - SortBy query parameter.
    type: str
  sortOrder:
    description:
    - SortOrder query parameter.
    type: str
  ipAddress:
    description:
    - IpAddress query parameter.
    type: list
  pingStatus:
    description:
    - PingStatus query parameter.
    type: list
  snmpStatus:
    description:
    - SnmpStatus query parameter.
    type: list
  cliStatus:
    description:
    - CliStatus query parameter.
    type: list
  netconfStatus:
    description:
    - NetconfStatus query parameter.
    type: list
  httpStatus:
    description:
    - HttpStatus query parameter.
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Discovery Summary reference
  description: Complete reference of the Discovery Summary object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Discovery Summary
  cisco.dnac.discovery_summary_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    taskId: string
    sortBy: string
    sortOrder: string
    ipAddress: []
    pingStatus: []
    snmpStatus: []
    cliStatus: []
    netconfStatus: []
    httpStatus: []
    id: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: client_proximity_info
short_description: Information module for Client Proximity
description:
- Get all Client Proximity.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  username:
    description:
    - Username query parameter. Wireless client username for which proximity information is required.
    type: str
  number_days:
    description:
    - >
      Number_days query parameter. Number of days to track proximity until current date. Defaults and maximum up
      to 14 days.
    type: int
  time_resolution:
    description:
    - >
      Time_resolution query parameter. Time interval (in minutes) to measure proximity. Defaults to 15 minutes
      with a minimum 5 minutes.
    type: int
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Client Proximity reference
  description: Complete reference of the Client Proximity object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Client Proximity
  cisco.dnac.client_proximity_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    username: string
    number_days: 0
    time_resolution: 0
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

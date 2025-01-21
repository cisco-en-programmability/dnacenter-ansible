#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: client_proximity_info
short_description: Information module for Client Proximity Info
description:
- This module represents an alias of the module client_proximity_v1_info
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
    type: float
  time_resolution:
    description:
    - >
      Time_resolution query parameter. Time interval (in minutes) to measure proximity. Defaults to 15 minutes
      with a minimum 5 minutes.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Clients ClientProximityV1
  description: Complete reference of the ClientProximityV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!client-proximity
notes:
  - SDK Method used are
    clients.Clients.client_proximity_v1,

  - Paths used are
    get /dna/intent/api/v1/client-proximity,
  - It should be noted that this module is an alias of client_proximity_v1_info

"""

EXAMPLES = r"""
- name: Get all Client Proximity Info
  cisco.dnac.client_proximity_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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

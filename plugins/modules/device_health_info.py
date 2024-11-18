#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: device_health_info
short_description: Information module for Device Health Info
description:
- This module represents an alias of the module device_health_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceRole:
    description:
    - DeviceRole query parameter. CORE, ACCESS, DISTRIBUTION, ROUTER, WLC, or AP (case insensitive).
    type: str
  siteId:
    description:
    - SiteId query parameter. DNAC site UUID.
    type: str
  health:
    description:
    - Health query parameter. DNAC health catagory POOR, FAIR, or GOOD (case insensitive).
    type: str
  startTime:
    description:
    - StartTime query parameter. UTC epoch time in milliseconds.
    type: float
  endTime:
    description:
    - EndTime query parameter. UTC epoch time in milliseconds.
    type: float
  limit:
    description:
    - Limit query parameter. Max number of device entries in the response (default to 50. Max at 500).
    type: float
  offset:
    description:
    - Offset query parameter. The offset of the first device in the returned data (Mutiple of 'limit' + 1).
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices DevicesV1
  description: Complete reference of the DevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!devices-v-1
notes:
  - SDK Method used are
    devices.Devices.devices_v1,

  - Paths used are
    get /dna/intent/api/v1/device-health,
  - It should be noted that this module is an alias of device_health_v1_info

"""

EXAMPLES = r"""
- name: Get all Device Health Info
  cisco.dnac.device_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceRole: string
    siteId: string
    health: string
    startTime: 0
    endTime: 0
    limit: 0
    offset: 0
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of device_health_v1_info.
"""

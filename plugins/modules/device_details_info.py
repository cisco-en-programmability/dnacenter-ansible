#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: device_details_info
short_description: Information module for Device Details Info
description:
- This module represents an alias of the module device_details_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  timestamp:
    description:
    - Timestamp query parameter. UTC timestamp of device data in milliseconds.
    type: float
  identifier:
    description:
    - Identifier query parameter. One of "macAddress", "nwDeviceName", "uuid" (case insensitive).
    type: str
  searchBy:
    description:
    - SearchBy query parameter. MAC Address, device name, or UUID of the network device.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetDeviceDetailV1
  description: Complete reference of the GetDeviceDetailV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-detail-v-1
notes:
  - SDK Method used are
    devices.Devices.get_device_detail_v1,

  - Paths used are
    get /dna/intent/api/v1/device-detail,
  - It should be noted that this module is an alias of device_details_v1_info

"""

EXAMPLES = r"""
- name: Get all Device Details Info
  cisco.dnac.device_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    timestamp: 0
    identifier: string
    searchBy: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of device_details_v1_info.
"""

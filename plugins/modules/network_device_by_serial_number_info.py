#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_by_serial_number_info
short_description: Information module for Network Device By Serial Number Info
description:
- This module represents an alias of the module network_device_by_serial_number_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  serialNumber:
    description:
    - SerialNumber path parameter. Device serial number.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetDeviceBySerialNumberV1
  description: Complete reference of the GetDeviceBySerialNumberV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-by-serial-number-v-1
notes:
  - SDK Method used are
    devices.Devices.get_device_by_serial_number_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/serial-number/{serialNumber},
  - It should be noted that this module is an alias of network_device_by_serial_number_v1_info

"""

EXAMPLES = r"""
- name: Get Network Device By Serial Number Info by id
  cisco.dnac.network_device_by_serial_number_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    serialNumber: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of network_device_by_serial_number_v1_info.
"""

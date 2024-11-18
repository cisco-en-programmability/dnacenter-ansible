#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_range_info
short_description: Information module for Network Device Range Info
description:
- This module represents an alias of the module network_device_range_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startIndex:
    description:
    - StartIndex path parameter. Start index >=1.
    type: int
  recordsToReturn:
    description:
    - RecordsToReturn path parameter. Number of records to return 1<= recordsToReturn <= 500.
    type: int
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetNetworkDeviceByPaginationRangeV1
  description: Complete reference of the GetNetworkDeviceByPaginationRangeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-network-device-by-pagination-range-v-1
notes:
  - SDK Method used are
    devices.Devices.get_network_device_by_pagination_range_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/{startIndex}/{recordsToReturn},
  - It should be noted that this module is an alias of network_device_range_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Range Info
  cisco.dnac.network_device_range_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    startIndex: 0
    recordsToReturn: 0
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of network_device_range_v1_info.
"""

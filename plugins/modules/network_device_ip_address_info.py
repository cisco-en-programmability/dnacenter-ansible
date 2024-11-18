#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_ip_address_info
short_description: Information module for Network Device Ip Address Info
description:
- This module represents an alias of the module network_device_ip_address_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  ipAddress:
    description:
    - IpAddress path parameter. Device IP address.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetNetworkDeviceByIPV1
  description: Complete reference of the GetNetworkDeviceByIPV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-network-device-by-ip-v-1
notes:
  - SDK Method used are
    devices.Devices.get_network_device_by_ip_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/ip-address/{ipAddress},
  - It should be noted that this module is an alias of network_device_ip_address_v1_info

"""

EXAMPLES = r"""
- name: Get Network Device Ip Address Info by id
  cisco.dnac.network_device_ip_address_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    ipAddress: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of network_device_ip_address_v1_info.
"""
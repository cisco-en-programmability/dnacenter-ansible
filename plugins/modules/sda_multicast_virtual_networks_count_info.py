#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_multicast_virtual_networks_count_info
short_description: Information module for Sda Multicast Virtual Networks Count Info
description:
  - This module represents an alias of the module sda_multicast_virtual_networks_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
      - FabricId query parameter. ID of the fabric site the multicast configuration
        is associated with.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetMulticastVirtualNetworkCountV1
    description: Complete reference of the GetMulticastVirtualNetworkCountV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-multicast-virtual-network-count
notes:
  - SDK Method used are sda.Sda.get_multicast_virtual_network_count_v1,
  - Paths used are get /dna/intent/api/v1/sda/multicast/virtualNetworks/count,
  - It should be noted that this module is an alias of sda_multicast_virtual_networks_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Sda Multicast Virtual Networks Count Info
  cisco.dnac.sda_multicast_virtual_networks_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""

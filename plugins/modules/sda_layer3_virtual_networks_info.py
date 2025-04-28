#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_layer3_virtual_networks_info
short_description: Information module for Sda Layer3 Virtual Networks Info
description:
  - This module represents an alias of the module sda_layer3_virtual_networks_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  virtualNetworkName:
    description:
      - VirtualNetworkName query parameter. Name of the layer 3 virtual network.
    type: str
  fabricId:
    description:
      - FabricId query parameter. ID of the fabric the layer 3 virtual network is
        assigned to.
    type: str
  anchoredSiteId:
    description:
      - AnchoredSiteId query parameter. Fabric ID of the fabric site the layer 3 virtual
        network is anchored at.
    type: str
  offset:
    description:
      - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
      - >
        Limit query parameter. Maximum number of records to return. The maximum number
        of objects supported in a
        single request is 500.
    type: float
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetLayer3VirtualNetworksV1
    description: Complete reference of the GetLayer3VirtualNetworksV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-layer-3-virtual-networks
notes:
  - SDK Method used are sda.Sda.get_layer3_virtual_networks_v1,
  - Paths used are get /dna/intent/api/v1/sda/layer3VirtualNetworks,
  - It should be noted that this module is an alias of sda_layer3_virtual_networks_v1_info
"""
EXAMPLES = r"""
- name: Get all Sda Layer3 Virtual Networks Info
  cisco.dnac.sda_layer3_virtual_networks_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    virtualNetworkName: string
    fabricId: string
    anchoredSiteId: string
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "virtualNetworkName": "string",
          "fabricIds": [
            "string"
          ],
          "anchoredSiteId": "string"
        }
      ],
      "version": "string"
    }
"""

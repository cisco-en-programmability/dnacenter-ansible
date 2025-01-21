#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_layer2_virtual_networks_v1_info
short_description: Information module for Sda Layer2 Virtual Networks V1
description:
- Get all Sda Layer2 Virtual Networks V1.
- Returns a list of layer 2 virtual networks that match the provided query parameters.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id query parameter. ID of the layer 2 virtual network.
    type: str
  fabricId:
    description:
    - FabricId query parameter. ID of the fabric the layer 2 virtual network is assigned to.
    type: str
  vlanName:
    description:
    - VlanName query parameter. The vlan name of the layer 2 virtual network.
    type: str
  vlanId:
    description:
    - VlanId query parameter. The vlan ID of the layer 2 virtual network.
    type: float
  trafficType:
    description:
    - TrafficType query parameter. The traffic type of the layer 2 virtual network.
    type: str
  associatedLayer3VirtualNetworkName:
    description:
    - AssociatedLayer3VirtualNetworkName query parameter. Name of the associated layer 3 virtual network.
    type: str
  offset:
    description:
    - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
    - >
      Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
      single request is 500.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetLayer2VirtualNetworksV1
  description: Complete reference of the GetLayer2VirtualNetworksV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-layer-2-virtual-networks
notes:
  - SDK Method used are
    sda.Sda.get_layer2_virtual_networks_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/layer2VirtualNetworks,

"""

EXAMPLES = r"""
- name: Get all Sda Layer2 Virtual Networks V1
  cisco.dnac.sda_layer2_virtual_networks_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    fabricId: string
    vlanName: string
    vlanId: 0
    trafficType: string
    associatedLayer3VirtualNetworkName: string
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
          "fabricId": "string",
          "vlanName": "string",
          "vlanId": 0,
          "trafficType": "string",
          "isFabricEnabledWireless": true,
          "isMultipleIpToMacAddresses": true,
          "associatedLayer3VirtualNetworkName": "string"
        }
      ],
      "version": "string"
    }
"""

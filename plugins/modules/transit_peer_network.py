#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: transit_peer_network
short_description: Resource module for Transit Peer Network
description:
  - This module represents an alias of the module transit_peer_network_v1
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  ipTransitSettings:
    description: Transit Peer Network's ipTransitSettings.
    suboptions:
      autonomousSystemNumber:
        description: Autonomous System Number.
        type: str
      routingProtocolName:
        description: Routing Protocol Name.
        type: str
    type: dict
  sdaTransitSettings:
    description: Transit Peer Network's sdaTransitSettings.
    suboptions:
      transitControlPlaneSettings:
        description: Transit Peer Network's transitControlPlaneSettings.
        elements: dict
        suboptions:
          deviceManagementIpAddress:
            description: Device Management Ip Address of provisioned device.
            type: str
          siteNameHierarchy:
            description: Site Name Hierarchy where device is provisioned.
            type: str
        type: list
    type: dict
  transitPeerNetworkName:
    description: TransitPeerNetworkName query parameter. Transit Peer Network Name.
    type: str
  transitPeerNetworkType:
    description: Transit Peer Network Type.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA AddTransitPeerNetworkV1
    description: Complete reference of the AddTransitPeerNetworkV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-transit-peer-network
  - name: Cisco DNA Center documentation for SDA DeleteTransitPeerNetworkV1
    description: Complete reference of the DeleteTransitPeerNetworkV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-transit-peer-network
notes:
  - SDK Method used are sda.Sda.add_transit_peer_network_v1, sda.Sda.delete_transit_peer_network_v1,
  - Paths used are post /dna/intent/api/v1/business/sda/transit-peer-network, delete
    /dna/intent/api/v1/business/sda/transit-peer-network,
  - It should be noted that this module is an alias of transit_peer_network_v1
"""
EXAMPLES = r"""
- name: Delete all
  cisco.dnac.transit_peer_network:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    transitPeerNetworkName: string
- name: Create
  cisco.dnac.transit_peer_network:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    ipTransitSettings:
      autonomousSystemNumber: string
      routingProtocolName: string
    sdaTransitSettings:
      transitControlPlaneSettings:
        - deviceManagementIpAddress: string
          siteNameHierarchy: string
    transitPeerNetworkName: string
    transitPeerNetworkType: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "taskId": "string",
      "taskStatusUrl": "string",
      "executionStatusUrl": "string",
      "executionId": "string"
    }
"""

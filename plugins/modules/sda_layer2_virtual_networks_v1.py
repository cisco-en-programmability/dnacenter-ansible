#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_layer2_virtual_networks_v1
short_description: Resource module for Sda Layer2 Virtual Networks V1
description:
  - Manage operations create, update and delete of the resource Sda Layer2 Virtual
    Networks V1.
  - Adds layer 2 virtual networks based on user input.
  - Deletes a layer 2 virtual network based on id.
  - Deletes layer 2 virtual networks based on user input.
  - Updates layer 2 virtual networks based on user input.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  associatedLayer3VirtualNetworkName:
    description: AssociatedLayer3VirtualNetworkName query parameter. Name of the associated
      layer 3 virtual network.
    type: str
  fabricId:
    description: FabricId query parameter. ID of the fabric the layer 2 virtual network
      is assigned to.
    type: str
  id:
    description: Id path parameter. ID of the layer 2 virtual network.
    type: str
  payload:
    description: Sda Layer2 Virtual Networks's payload.
    elements: dict
    suboptions:
      associatedLayer3VirtualNetworkName:
        description: Name of the layer 3 virtual network associated with the layer
          2 virtual network. This field is provided to support requests related to
          virtual network anchoring. The layer 3 virtual network must have already
          been added to the fabric before association. This field must either be present
          in all payload elements or none.
        type: str
      fabricId:
        description: ID of the fabric this layer 2 virtual network is to be assigned
          to.
        type: str
      isFabricEnabledWireless:
        description: Set to true to enable wireless. Default is false.
        type: bool
      isMultipleIpToMacAddresses:
        description: Set to true to enable multiple IP-to-MAC addresses (Wireless
          Bridged-Network Virtual Machine). This field defaults to false when associated
          with a layer 3 virtual network and cannot be used when not associated with
          a layer 3 virtual network.
        type: bool
      trafficType:
        description: The type of traffic that is served.
        type: str
      vlanId:
        description: ID of the VLAN of the layer 2 virtual network. Allowed VLAN range
          is 2-4093 except for reserved VLANs 1002-1005, and 2046. If deploying on
          a fabric zone, this vlanId must match the vlanId of the corresponding layer
          2 virtual network on the fabric site.
        type: int
      vlanName:
        description: Name of the VLAN of the layer 2 virtual network. Must contain
          only alphanumeric characters, underscores, and hyphens.
        type: str
    type: list
  trafficType:
    description: TrafficType query parameter. The traffic type of the layer 2 virtual
      network.
    type: str
  vlanId:
    description: VlanId query parameter. The vlan ID of the layer 2 virtual network.
    type: float
  vlanName:
    description: VlanName query parameter. The vlan name of the layer 2 virtual network.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA AddLayer2VirtualNetworksV1
    description: Complete reference of the AddLayer2VirtualNetworksV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-layer-2-virtual-networks
  - name: Cisco DNA Center documentation for SDA DeleteLayer2VirtualNetworkByIdV1
    description: Complete reference of the DeleteLayer2VirtualNetworkByIdV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-layer-2-virtual-network-by-id
  - name: Cisco DNA Center documentation for SDA DeleteLayer2VirtualNetworksV1
    description: Complete reference of the DeleteLayer2VirtualNetworksV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-layer-2-virtual-networks
  - name: Cisco DNA Center documentation for SDA UpdateLayer2VirtualNetworksV1
    description: Complete reference of the UpdateLayer2VirtualNetworksV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-layer-2-virtual-networks
notes:
  - SDK Method used are sda.Sda.add_layer2_virtual_networks_v1, sda.Sda.delete_layer2_virtual_network_by_id_v1,
    sda.Sda.update_layer2_virtual_networks_v1,
  - Paths used are post /dna/intent/api/v1/sda/layer2VirtualNetworks, delete /dna/intent/api/v1/sda/layer2VirtualNetworks,
    delete /dna/intent/api/v1/sda/layer2VirtualNetworks/{id}, put /dna/intent/api/v1/sda/layer2VirtualNetworks,
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_layer2_virtual_networks_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - associatedLayer3VirtualNetworkName: string
        fabricId: string
        isFabricEnabledWireless: true
        isMultipleIpToMacAddresses: true
        trafficType: string
        vlanId: 0
        vlanName: string
- name: Delete all
  cisco.dnac.sda_layer2_virtual_networks_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    associatedLayer3VirtualNetworkName: string
    fabricId: string
    trafficType: string
    vlanId: 0
    vlanName: string
- name: Update all
  cisco.dnac.sda_layer2_virtual_networks_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - associatedLayer3VirtualNetworkName: string
        fabricId: string
        id: string
        isFabricEnabledWireless: true
        isMultipleIpToMacAddresses: true
        trafficType: string
        vlanId: 0
        vlanName: string
- name: Delete by id
  cisco.dnac.sda_layer2_virtual_networks_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

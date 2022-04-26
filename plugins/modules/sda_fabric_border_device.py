#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_border_device
short_description: Resource module for Sda Fabric Border Device
description:
- Manage operations create and delete of the resource Sda Fabric Border Device.
- Adds border device in SDA Fabric.
- Deletes border device from SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  borderSessionType:
    description: Border Session Type.
    type: str
    version_added: 4.0.0
  connectedToInternet:
    description: Connected to Internet.
    type: bool
    version_added: 4.0.0
  deviceManagementIpAddress:
    description: Management Ip Address of the Device which is provisioned successfully.
    type: str
    version_added: 4.0.0
  externalAutonomouSystemNumber:
    description: External Autonomous System Number will be used to automate IP routing
      between Border Node and remote peer (e.g.,1-65535).
    type: str
    version_added: 4.0.0
  externalConnectivityIpPoolName:
    description: IP pool to use to automate IP routing between the border node and remote
      peer.
    type: str
    version_added: 4.0.0
  externalConnectivitySettings:
    description: External Connectivity Settings information of L3 Handoff.
    type: dict
    version_added: 4.0.0
  externalDomainRoutingProtocolName:
    description: External Domain Routing Protocol Name. (Example BGP).
    type: str
  interfaceName:
    description: Interface Name.
    type: str
    version_added: 4.0.0
  internalAutonomouSystemNumber:
    description: Internal Autonomouns System Number used by border node to communicate
      with remote peer (e.g.,1-65535).
    type: str
  l3Handoff:
    description: L3 Handoff information.
    type: dict
    version_added: 4.0.0
  siteNameHierarchy:
    description: Site Name Hierarchy for device location(site should be fabric site).
    type: str
  virtualNetwork:
    description: Virtual Network information of L3 Hand off.
    type: dict
    version_added: 4.0.0
  virtualNetworkName:
    description: Virtual Network Name assigned to site.
    type: str
    version_added: 4.0.0
  vlanId:
    description: Vlan Id (e.g.,2-4096 except for reserved VLANs (1002-1005, 2046, 4095)).
    type: str
    version_added: 4.0.0
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    sda.Sda.adds_border_device,
    sda.Sda.deletes_border_device,

  - Paths used are
    post /dna/intent/api/v1/business/sda/border-device,
    delete /dna/intent/api/v1/business/sda/border-device,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_fabric_border_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    borderSessionType: string
    connectedToInternet: true
    deviceManagementIpAddress: string
    externalAutonomouSystemNumber: string
    externalConnectivityIpPoolName: string
    externalConnectivitySettings: {}
    externalDomainRoutingProtocolName: string
    interfaceName: string
    internalAutonomouSystemNumber: string
    l3Handoff: {}
    siteNameHierarchy: string
    virtualNetwork: {}
    virtualNetworkName: string
    vlanId: string

- name: Delete all
  cisco.dnac.sda_fabric_border_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string

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

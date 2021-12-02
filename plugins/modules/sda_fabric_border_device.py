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
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  borderSessionType:
    version_added: "4.0.0"
    description: Border Session Type.
    type: str
  connectedToInternet:
    version_added: "4.0.0"
    description: Connected to Internet.
    type: bool
  deviceManagementIpAddress:
    version_added: "4.0.0"
    description: Management Ip Address of the Device which is provisioned successfully.
    type: str
  externalAutonomouSystemNumber:
    version_added: "4.0.0"
    description: External Autonomous System Number will be used to automate IP routing
      between Border Node and remote peer (e.g.,1-65535).
    type: str
  externalConnectivityIpPoolName:
    version_added: "4.0.0"
    description: IP pool to use to automate IP routing between the border node and remote
      peer.
    type: str
  externalConnectivitySettings:
    version_added: "4.0.0"
    description: External Connectivity Settings information of L3 Handoff.
    type: dict
  externalDomainRoutingProtocolName:
    version_added: "4.0.0"
    description: External Domain Routing Protocol Name. (Example BGP).
    type: str
  interfaceName:
    version_added: "4.0.0"
    description: Interface Name.
    type: str
  internalAutonomouSystemNumber:
    version_added: "4.0.0"
    description: Internal Autonomouns System Number used by border node to communicate
      with remote peer (e.g.,1-65535).
    type: str
  l3Handoff:
    version_added: "4.0.0"
    description: L3 Handoff information.
    type: dict
  siteNameHierarchy:
    version_added: "4.0.0"
    description: Site Name Hierarchy for device location(site should be fabric site).
    type: str
  virtualNetwork:
    version_added: "4.0.0"
    description: Virtual Network information of L3 Hand off.
    type: dict
  virtualNetworkName:
    version_added: "4.0.0"
    description: Virtual Network Name assigned to site.
    type: str
  vlanId:
    version_added: "4.0.0"
    description: Vlan Id (e.g.,2-4096 except for reserved VLANs (1002-1005, 2046, 4095)).
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sda Fabric Border Device reference
  description: Complete reference of the Sda Fabric Border Device object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
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

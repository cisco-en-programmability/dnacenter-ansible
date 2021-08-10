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
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceIPAddress:
    description: DeviceIPAddress query parameter. Device IP Address.
    type: str
  payload:
    description: Sda Fabric Border Device's payload.
    suboptions:
      borderSessionType:
        description: Border Session Type.
        type: str
      connectedToInternet:
        description: Connected To Internet.
        type: bool
      deviceManagementIpAddress:
        description: Device Management Ip Address.
        type: str
      externalConnectivityIpPoolName:
        description: External Connectivity Ip Pool Name.
        type: str
      externalConnectivitySettings:
        description: Sda Fabric Border Device's externalConnectivitySettings.
        suboptions:
          externalAutonomouSystemNumber:
            description: External Autonomou System Number.
            type: str
          interfaceName:
            description: Interface Name.
            type: str
          l3Handoff:
            description: Sda Fabric Border Device's l3Handoff.
            suboptions:
              virtualNetwork:
                description: Sda Fabric Border Device's virtualNetwork.
                suboptions:
                  virtualNetworkName:
                    description: Virtual Network Name.
                    type: str
                type: dict
            type: list
        type: list
      externalDomainRoutingProtocolName:
        description: External Domain Routing Protocol Name.
        type: str
      internalAutonomouSystemNumber:
        description: Internal Autonomou System Number.
        type: str
      siteNameHierarchy:
        description: Site Name Hierarchy.
        type: str
    type: list
requirements:
- dnacentersdk
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
    deviceIPAddress: string

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
      "executionStatusUrl": "string"
    }
"""

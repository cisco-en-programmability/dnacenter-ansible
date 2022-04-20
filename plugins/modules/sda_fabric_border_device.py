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
  externalConnectivityIpPoolName:
    version_added: "4.0.0"
    description: IP pool to use to automate IP routing between the border node and remote
      peer.
    type: str
  externalConnectivitySettings:
    version_added: "4.0.0"
    description: Sda Fabric Border Device's externalConnectivitySettings.
    suboptions:
      externalAutonomouSystemNumber:
        version_added: "4.0.0"
        description: External Autonomous System Number peer (e.g.,1-65535).
        type: str
      interfaceName:
        version_added: "4.0.0"
        description: Interface Name.
        type: str
      l3Handoff:
        version_added: "4.0.0"
        description: Sda Fabric Border Device's l3Handoff.
        suboptions:
          virtualNetwork:
            version_added: "4.0.0"
            description: Sda Fabric Border Device's virtualNetwork.
            suboptions:
              virtualNetworkName:
                version_added: "4.0.0"
                description: Virtual Network Name, that is associated to Fabric Site.
                type: str
              vlanId:
                version_added: "4.0.0"
                description: Vlan Id (e.g.,2-4096 except for reserved VLANs (1002-1005,
                  2046, 4095)).
                type: str
            type: dict
        elements: dict
        type: list
    elements: dict
    type: list
  externalDomainRoutingProtocolName:
    version_added: "4.0.0"
    description: External Domain Routing Protocol Name. (Example BGP).
    type: str
  internalAutonomouSystemNumber:
    version_added: "4.0.0"
    description: Internal Autonomouns System Number used by border node to communicate
      with remote peer (e.g.,1-65535).
    type: str
  siteNameHierarchy:
    version_added: "4.0.0"
    description: Site Name Hierarchy for device location(site should be fabric site).
    type: str
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
    externalConnectivityIpPoolName: string
    externalConnectivitySettings:
    - externalAutonomouSystemNumber: string
      interfaceName: string
      l3Handoff:
      - virtualNetwork:
          virtualNetworkName: string
          vlanId: string
    externalDomainRoutingProtocolName: string
    internalAutonomouSystemNumber: string
    siteNameHierarchy: string

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

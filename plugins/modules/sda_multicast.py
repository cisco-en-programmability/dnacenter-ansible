#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_multicast
short_description: Resource module for Sda Multicast
description:
- Manage operations create and delete of the resource Sda Multicast.
- Add multicast in SDA fabric.
- Delete multicast from SDA fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  multicastMethod:
    description: Multicast Methods.
    type: str
  multicastVnInfo:
    description: Sda Multicast's multicastVnInfo.
    suboptions:
      externalRpIpAddress:
        description: External Rp Ip Address, required for muticastType=asm_with_external_rp.
        type: str
      ipPoolName:
        description: Ip Pool Name, that is reserved to fabricSiteNameHierarchy.
        type: str
      ssmGroupRange:
        description: Valid SSM group range ip address(e.g., 230.0.0.0).
        type: str
      ssmInfo:
        description: Source-specific multicast information, required if muticastType=ssm.
        type: dict
      ssmWildcardMask:
        description: Valid SSM Wildcard Mask ip address(e.g.,0.255.255.255).
        type: str
      virtualNetworkName:
        description: Virtual Network Name, that is associated to fabricSiteNameHierarchy.
        type: str
    type: dict
  muticastType:
    description: Muticast Type.
    type: str
  siteNameHierarchy:
    description: Full path of sda fabric siteNameHierarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    sda.Sda.add_multicast_in_sda_fabric,
    sda.Sda.delete_multicast_from_sda_fabric,

  - Paths used are
    post /dna/intent/api/v1/business/sda/multicast,
    delete /dna/intent/api/v1/business/sda/multicast,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_multicast:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    multicastMethod: string
    multicastVnInfo:
      externalRpIpAddress: string
      ipPoolName: string
      ssmGroupRange: string
      ssmInfo: {}
      ssmWildcardMask: string
      virtualNetworkName: string
    muticastType: string
    siteNameHierarchy: string

- name: Delete all
  cisco.dnac.sda_multicast:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    siteNameHierarchy: string

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

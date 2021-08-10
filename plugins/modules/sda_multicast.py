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
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  fabricSiteNameHierarchy:
    description: FabricSiteNameHierarchy.
    type: str
  multicastMethod:
    description: Multicast methods.
    type: str
  multicastVnInfo:
    description: Sda Multicast's multicastVnInfo.
    suboptions:
      externalRpIpAddress:
        description: External Rp Ip Address, required for muticastType=asm_with_external_rp.
        type: str
      ipPoolName:
        description: Ip Pool Name in fabricSiteNameHierarchy.
        type: str
      ssmGroupRange:
        description: Valid ssm group range ip address.
        type: str
      ssmInfo:
        description: Source-specific multicast information, required if muticastType=ssm.
        type: dict
      ssmWildcardMask:
        description: Valid ssm Wildcard Mask ip address.
        type: str
      virtualNetworkName:
        description: Virtual network name in fabricSiteNameHierarchy.
        type: str
    type: dict
  muticastType:
    description: Muticast type.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Multicast reference
  description: Complete reference of the Sda Multicast object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
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
    fabricSiteNameHierarchy: string
    multicastMethod: string
    multicastVnInfo:
      externalRpIpAddress: string
      ipPoolName: string
      ssmGroupRange: string
      ssmInfo: {}
      ssmWildcardMask: string
      virtualNetworkName: string
    muticastType: string

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
    fabricSiteNameHierarchy: string

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
      "executionId": "string"
    }
"""

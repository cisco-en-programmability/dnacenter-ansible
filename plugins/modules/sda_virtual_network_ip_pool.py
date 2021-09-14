#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_virtual_network_ip_pool
short_description: Resource module for Sda Virtual Network Ip Pool
description:
- Manage operations create and delete of the resource Sda Virtual Network Ip Pool.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  ipPoolName:
    description: IpPoolName query parameter.
    type: str
  payload:
    description: Sda Virtual Network Ip Pool's payload.
    suboptions:
      authenticationPolicyName:
        description: Authentication Policy Name.
        type: str
      ipPoolName:
        description: Ip Pool Name.
        type: str
      isL2FloodingEnabled:
        description: Is L2 Flooding Enabled.
        type: bool
      isThisCriticalPool:
        description: Is This Critical Pool.
        type: bool
      poolType:
        description: Pool Type.
        type: str
      scalableGroupName:
        description: Scalable Group Name.
        type: str
      trafficType:
        description: Traffic Type.
        type: str
      virtualNetworkName:
        description: Virtual Network Name.
        type: str
    type: list
  virtualNetworkName:
    description: VirtualNetworkName query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Virtual Network Ip Pool reference
  description: Complete reference of the Sda Virtual Network Ip Pool object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    ipPoolName: string
    virtualNetworkName: string

- name: Create
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - virtualNetworkName: string
      ipPoolName: string
      trafficType: string
      authenticationPolicyName: string
      scalableGroupName: string
      isL2FloodingEnabled: true
      isThisCriticalPool: true
      poolType: string
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

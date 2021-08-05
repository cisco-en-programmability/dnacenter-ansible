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
        description: Sda Virtual Network Ip Pool's authenticationPolicyName.
        type: str
      ipPoolName:
        description: Sda Virtual Network Ip Pool's ipPoolName.
        type: str
      isL2FloodingEnabled:
        description: IsL2FloodingEnabled flag.
        type: bool
      isThisCriticalPool:
        description: IsThisCriticalPool flag.
        type: bool
      poolType:
        description: Sda Virtual Network Ip Pool's poolType.
        type: str
      scalableGroupName:
        description: Sda Virtual Network Ip Pool's scalableGroupName.
        type: str
      trafficType:
        description: Sda Virtual Network Ip Pool's trafficType.
        type: str
      virtualNetworkName:
        description: Sda Virtual Network Ip Pool's virtualNetworkName.
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

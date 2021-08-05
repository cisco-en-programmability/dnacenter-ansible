#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: reserve_ip_subpool
short_description: Resource module for Reserve Ip Subpool
description:
- Manage operations create, update and delete of the resource Reserve Ip Subpool.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description: Id query parameter. Id of subpool to be associated with the site.
    type: str
  ipv4DhcpServers:
    description: Reserve Ip Subpool's ipv4DhcpServers.
    elements: str
    type: list
  ipv4DnsServers:
    description: Reserve Ip Subpool's ipv4DnsServers.
    elements: str
    type: list
  ipv4GateWay:
    description: Reserve Ip Subpool's ipv4GateWay.
    type: str
  ipv4GlobalPool:
    description: Reserve Ip Subpool's ipv4GlobalPool.
    type: str
  ipv4Prefix:
    description: Ipv4Prefix flag.
    type: bool
  ipv4PrefixLength:
    description: Reserve Ip Subpool's ipv4PrefixLength.
    type: int
  ipv4Subnet:
    description: Reserve Ip Subpool's ipv4Subnet.
    type: str
  ipv4TotalHost:
    description: Reserve Ip Subpool's ipv4TotalHost.
    type: int
  ipv6AddressSpace:
    description: Ipv6AddressSpace flag.
    type: bool
  ipv6DhcpServers:
    description: Reserve Ip Subpool's ipv6DhcpServers.
    elements: str
    type: list
  ipv6DnsServers:
    description: Reserve Ip Subpool's ipv6DnsServers.
    elements: str
    type: list
  ipv6GateWay:
    description: Reserve Ip Subpool's ipv6GateWay.
    type: str
  ipv6GlobalPool:
    description: Reserve Ip Subpool's ipv6GlobalPool.
    type: str
  ipv6Prefix:
    description: Ipv6Prefix flag.
    type: bool
  ipv6PrefixLength:
    description: Reserve Ip Subpool's ipv6PrefixLength.
    type: int
  ipv6Subnet:
    description: Reserve Ip Subpool's ipv6Subnet.
    type: str
  ipv6TotalHost:
    description: Reserve Ip Subpool's ipv6TotalHost.
    type: int
  name:
    description: Reserve Ip Subpool's name.
    type: str
  siteId:
    description: SiteId path parameter. Site id of site to update sub pool.
    type: str
  slaacSupport:
    description: SlaacSupport flag.
    type: bool
  type:
    description: Reserve Ip Subpool's type.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Reserve Ip Subpool reference
  description: Complete reference of the Reserve Ip Subpool object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.dnac.reserve_ip_subpool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
    ipv4DhcpServers:
    - string
    ipv4DnsServers:
    - string
    ipv6AddressSpace: true
    ipv6DhcpServers:
    - string
    ipv6DnsServers:
    - string
    ipv6GateWay: string
    ipv6GlobalPool: string
    ipv6Prefix: true
    ipv6PrefixLength: 0
    ipv6Subnet: string
    ipv6TotalHost: 0
    name: string
    siteId: string
    slaacSupport: true

- name: Create
  cisco.dnac.reserve_ip_subpool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    ipv4DhcpServers:
    - string
    ipv4DnsServers:
    - string
    ipv4GateWay: string
    ipv4GlobalPool: string
    ipv4Prefix: true
    ipv4PrefixLength: 0
    ipv4Subnet: string
    ipv4TotalHost: 0
    ipv6AddressSpace: true
    ipv6DhcpServers:
    - string
    ipv6DnsServers:
    - string
    ipv6GateWay: string
    ipv6GlobalPool: string
    ipv6Prefix: true
    ipv6PrefixLength: 0
    ipv6Subnet: string
    ipv6TotalHost: 0
    name: string
    siteId: string
    slaacSupport: true
    type: string

- name: Delete by id
  cisco.dnac.reserve_ip_subpool:
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
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

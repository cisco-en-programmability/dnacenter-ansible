#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_authentication_profile
short_description: Resource module for Sda Fabric Authentication Profile
description:
- Manage operations create, update and delete of the resource Sda Fabric Authentication Profile.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  authenticateTemplateName:
    version_added: "4.0.0"
    description: Authenticate Template Name. Allowed values are 'No Authentication ',
      'Open Authentication', 'Closed Authentication', 'Low Impact'.
    type: str
  authenticationOrder:
    version_added: "4.0.0"
    description: Authentication Order. Allowed values are 'dot1x ', 'mac'.
    type: str
  dot1xToMabFallbackTimeout:
    version_added: "4.0.0"
    description: In a network that includes both devices that support and devices that
      do not support IEEE 802.1X, MAB can be deployed as a fallback, or complementary,
      mechanism to IEEE 802.1X. If the network does not have any IEEE 802.1X-capable
      devices, MAB can be deployed as a standalone authentication mechanism (e.g. 3-120).
    type: str
  numberOfHosts:
    version_added: "4.0.0"
    description: Number of hosts specifies the number of data hosts that can be connected
      to a port. With Single selected, you can have only one data client on the port.
      With Unlimited selected, you can have multiple data clients and one voice client
      on the port.
    type: str
  siteNameHierarchy:
    description: Site Name Hierarchy should be a valid fabric site name hierarchy. E.g
      Global/USA/San Jose.
    type: str
  wakeOnLan:
    version_added: "4.0.0"
    description: The IEEE 802.1X Wake on LAN (WoL) Support feature allows dormant systems
      to be powered up when the switch receives a specific Ethernet frame. You can use
      this feature in cases when hosts on power save and needs to receive a magic packet
      to turn them on. This feature works on a per subnet basis and send the subnet
      broadcast to all hosts in the subnet.
    type: bool
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sda Fabric Authentication Profile reference
  description: Complete reference of the Sda Fabric Authentication Profile object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authenticateTemplateName: string
    siteNameHierarchy: string

- name: Update all
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authenticateTemplateName: string
    authenticationOrder: string
    dot1xToMabFallbackTimeout: string
    numberOfHosts: string
    siteNameHierarchy: string
    wakeOnLan: true

- name: Delete all
  cisco.dnac.sda_fabric_authentication_profile:
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

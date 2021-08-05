#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_ssid_create_provision
short_description: Resource module for Wireless Provision Ssid Create Provision
description:
- Manage operation create of the resource Wireless Provision Ssid Create Provision.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  enableFabric:
    description: EnableFabric flag.
    type: bool
  flexConnect:
    description: Wireless Provision Ssid Create Provision's flexConnect.
    suboptions:
      enableFlexConnect:
        description: EnableFlexConnect flag.
        type: bool
      localToVlan:
        description: Wireless Provision Ssid Create Provision's localToVlan.
        type: int
    type: dict
  managedAPLocations:
    description: Wireless Provision Ssid Create Provision's managedAPLocations.
    elements: str
    type: list
  ssidDetails:
    description: Wireless Provision Ssid Create Provision's ssidDetails.
    suboptions:
      enableBroadcastSSID:
        description: EnableBroadcastSSID flag.
        type: bool
      enableFastLane:
        description: EnableFastLane flag.
        type: bool
      enableMACFiltering:
        description: EnableMACFiltering flag.
        type: bool
      fastTransition:
        description: Wireless Provision Ssid Create Provision's fastTransition.
        type: str
      name:
        description: Wireless Provision Ssid Create Provision's name.
        type: str
      passphrase:
        description: Wireless Provision Ssid Create Provision's passphrase.
        type: str
      radioPolicy:
        description: Wireless Provision Ssid Create Provision's radioPolicy.
        type: str
      securityLevel:
        description: Wireless Provision Ssid Create Provision's securityLevel.
        type: str
      trafficType:
        description: Wireless Provision Ssid Create Provision's trafficType.
        type: str
      webAuthURL:
        description: Wireless Provision Ssid Create Provision's webAuthURL.
        type: str
    type: dict
  ssidType:
    description: Wireless Provision Ssid Create Provision's ssidType.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Provision Ssid Create Provision reference
  description: Complete reference of the Wireless Provision Ssid Create Provision object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_provision_ssid_create_provision:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    enableFabric: true
    flexConnect:
      enableFlexConnect: true
      localToVlan: 0
    managedAPLocations:
    - string
    ssidDetails:
      enableBroadcastSSID: true
      enableFastLane: true
      enableMACFiltering: true
      fastTransition: string
      name: string
      passphrase: string
      radioPolicy: string
      securityLevel: string
      trafficType: string
      webAuthURL: string
    ssidType: string

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

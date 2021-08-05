#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_enterprise_ssid
short_description: Resource module for Wireless Enterprise Ssid
description:
- Manage operations create and delete of the resource Wireless Enterprise Ssid.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
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
    description: Wireless Enterprise Ssid's fastTransition.
    type: str
  name:
    description: Wireless Enterprise Ssid's name.
    type: str
  passphrase:
    description: Wireless Enterprise Ssid's passphrase.
    type: str
  radioPolicy:
    description: Wireless Enterprise Ssid's radioPolicy.
    type: str
  securityLevel:
    description: Wireless Enterprise Ssid's securityLevel.
    type: str
  ssidName:
    description: SsidName path parameter. Enter the SSID name to be deleted.
    type: str
  trafficType:
    description: Wireless Enterprise Ssid's trafficType.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Enterprise Ssid reference
  description: Complete reference of the Wireless Enterprise Ssid object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    enableBroadcastSSID: true
    enableFastLane: true
    enableMACFiltering: true
    fastTransition: string
    name: string
    passphrase: string
    radioPolicy: string
    securityLevel: string
    trafficType: string

- name: Delete by name
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    ssidName: string

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

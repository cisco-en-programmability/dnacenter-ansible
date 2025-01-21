#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_rogue_wireless_containment_stop
short_description: Resource module for Security Rogue Wireless Containment Stop
description:
- This module represents an alias of the module security_rogue_wireless_containment_stop_v1
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  macAddress:
    description: Mac Address.
    type: str
  type:
    description: Type.
    type: int
  wlcIp:
    description: Wlc Ip.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices StopWirelessRogueAPContainmentV1
  description: Complete reference of the StopWirelessRogueAPContainmentV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!stop-wireless-rogue-ap-containment
notes:
  - SDK Method used are
    devices.Devices.stop_wireless_rogue_ap_containment_v1,

  - Paths used are
    post /dna/intent/api/v1/security/rogue/wireless-containment/stop,
  - It should be noted that this module is an alias of security_rogue_wireless_containment_stop_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.security_rogue_wireless_containment_stop:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    macAddress: string
    type: 0
    wlcIp: string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "macAddress": "string",
        "type": 0,
        "initiatedOnWlcIp": "string",
        "taskId": "string",
        "taskType": "string",
        "initiatedOnBssid": [
          "string"
        ]
      },
      "version": "string"
    }
"""

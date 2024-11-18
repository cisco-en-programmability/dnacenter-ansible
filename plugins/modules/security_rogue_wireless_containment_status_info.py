#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_rogue_wireless_containment_status_info
short_description: Information module for Security Rogue Wireless Containment Status Info
description:
- This module represents an alias of the module security_rogue_wireless_containment_status_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  macAddress:
    description:
    - MacAddress path parameter. MAC Address of the Wireless Rogue AP.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices WirelessRogueAPContainmentStatusV1
  description: Complete reference of the WirelessRogueAPContainmentStatusV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!wireless-rogue-ap-containment-status-v-1
notes:
  - SDK Method used are
    devices.Devices.wireless_rogue_ap_containment_status_v1,

  - Paths used are
    get /dna/intent/api/v1/security/rogue/wireless-containment/status/{macAddress},
  - It should be noted that this module is an alias of security_rogue_wireless_containment_status_v1_info

"""

EXAMPLES = r"""
- name: Get Security Rogue Wireless Containment Status Info by id
  cisco.dnac.security_rogue_wireless_containment_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    macAddress: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of security_rogue_wireless_containment_status_v1_info.
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_controllers_anchor_capable_devices_info
short_description: Information module for Wireless Controllers Anchor Capable Devices Info
description:
- This module represents an alias of the module wireless_controllers_anchor_capable_devices_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetAnchorCapableDevicesV1
  description: Complete reference of the GetAnchorCapableDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-anchor-capable-devices
notes:
  - SDK Method used are
    wireless.Wireless.get_anchor_capable_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/anchorCapableDevices,
  - It should be noted that this module is an alias of wireless_controllers_anchor_capable_devices_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Controllers Anchor Capable Devices Info
  cisco.dnac.wireless_controllers_anchor_capable_devices_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "deviceIp": "string",
      "deviceName": "string",
      "wirelessMgmtIP": "string"
    }
"""

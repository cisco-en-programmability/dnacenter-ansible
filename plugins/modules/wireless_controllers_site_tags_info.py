#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_site_tags_info
short_description: Information module for Wireless Controllers Site Tags
description:
  - Get all Wireless Controllers Site Tags.
  - Get all Site Tags from Wireless Controller.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
      - >
        DeviceId path parameter. Network Device ID. This value can be obtained by using the API call GET
        /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetAllSiteTagsFromWirelessController
    description: Complete reference of the GetAllSiteTagsFromWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-site-tags-from-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_all_site_tags_from_wireless_controller,
  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/{deviceId}/siteTags,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Site Tags
  cisco.dnac.wireless_controllers_site_tags_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "siteTagUuid": "string",
        "siteTagName": "string"
      }
    ]
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_info
short_description: Information module for Wireless Profiles Info
description:
  - This module represents an alias of the module wireless_profiles_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: float
  wirelessProfileName:
    description:
      - WirelessProfileName query parameter. Wireless Profile Name.
    type: str
  id:
    description:
      - Id path parameter. Wireless Profile Id.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetWirelessProfileByIDV1
    description: Complete reference of the GetWirelessProfileByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profile-by-id
  - name: Cisco DNA Center documentation for Wireless GetWirelessProfilesV1
    description: Complete reference of the GetWirelessProfilesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles
notes:
  - SDK Method used are wireless.Wireless.get_wireless_profile_by_id_v1, wireless.Wireless.get_wireless_profiles_v1,
  - Paths used are get /dna/intent/api/v1/wirelessProfiles, get /dna/intent/api/v1/wirelessProfiles/{id},
  - It should be noted that this module is an alias of wireless_profiles_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Profiles Info
  cisco.dnac.wireless_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    wirelessProfileName: string
  register: result
- name: Get Wireless Profiles Info by id
  cisco.dnac.wireless_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "wirelessProfileName": "string",
        "ssidDetails": [
          {
            "ssidName": "string",
            "flexConnect": {
              "enableFlexConnect": true,
              "localToVlan": 0
            },
            "enableFabric": true,
            "wlanProfileName": "string",
            "interfaceName": "string",
            "policyProfileName": "string",
            "dot11beProfileId": "string",
            "anchorGroupName": "string",
            "vlanGroupName": "string"
          }
        ],
        "id": "string",
        "additionalInterfaces": [
          "string"
        ],
        "apZones": [
          {
            "apZoneName": "string",
            "rfProfileName": "string",
            "ssids": [
              "string"
            ]
          }
        ]
      },
      "version": "string"
    }
"""

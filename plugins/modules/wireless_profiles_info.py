#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessProfiles_info
short_description: Information module for Wirelessprofiles
description:
- Get all Wirelessprofiles.
- Get Wirelessprofiles by id.
- This API allows the user to get a Wireless Network Profile by ID.
- This API allows the user to get all Wireless Network Profiles.
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
    - Limit query parameter.
    type: float
  offset:
    description:
    - Offset query parameter.
    type: float
  id:
    description:
    - Id path parameter. Wireless Profile Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetWirelessProfileByID
  description: Complete reference of the GetWirelessProfileByID API.
  link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profile-by-id
- name: Cisco DNA Center documentation for Wireless GetWirelessProfiles
  description: Complete reference of the GetWirelessProfiles API.
  link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_wireless_profile_by_id,
    wireless.Wireless.get_wireless_profiles,

  - Paths used are
    get /dna/intent/api/v1/wirelessProfiles,
    get /dna/intent/api/v1/wirelessProfiles/{id},

"""

EXAMPLES = r"""
- name: Get all Wirelessprofiles
  cisco.dnac.wirelessProfiles_info:
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
  register: result

- name: Get Wirelessprofiles by id
  cisco.dnac.wirelessProfiles_info:
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
            "dot11beProfileId": "string"
          }
        ],
        "id": "string"
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_settings_dot11be_profiles
short_description: Resource module for Wireless Settings Dot11Be Profiles
description:
  - This module represents an alias of the module wireless_settings_dot11be_profiles_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. 802.11be Profile ID.
    type: str
  muMimoDownLink:
    description: MU-MIMO Downlink (Default false).
    type: bool
  muMimoUpLink:
    description: MU-MIMO Uplink (Default false).
    type: bool
  ofdmaDownLink:
    description: OFDMA Downlink (Default true).
    type: bool
  ofdmaMultiRu:
    description: OFDMA Multi-RU (Default false).
    type: bool
  ofdmaUpLink:
    description: OFDMA Uplink (Default true).
    type: bool
  profileName:
    description: 802.11be Profile Name.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateA80211beProfileV1
    description: Complete reference of the CreateA80211beProfileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-80-21-1be-profile
  - name: Cisco DNA Center documentation for Wireless DeleteA80211beProfileV1
    description: Complete reference of the DeleteA80211beProfileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-80-21-1be-profile
  - name: Cisco DNA Center documentation for Wireless Update80211beProfileV1
    description: Complete reference of the Update80211beProfileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-80-21-1be-profile
notes:
  - SDK Method used are wireless.Wireless.create_a80211be_profile_v1, wireless.Wireless.delete_a80211be_profile_v1,
    wireless.Wireless.update80211be_profile_v1,
  - Paths used are post /dna/intent/api/v1/wirelessSettings/dot11beProfiles, delete
    /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}, put /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
  - It should be noted that this module is an alias of wireless_settings_dot11be_profiles_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_settings_dot11be_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    muMimoDownLink: true
    muMimoUpLink: true
    ofdmaDownLink: true
    ofdmaMultiRu: true
    ofdmaUpLink: true
    profileName: string
- name: Delete by id
  cisco.dnac.wireless_settings_dot11be_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.dnac.wireless_settings_dot11be_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
    muMimoDownLink: true
    muMimoUpLink: true
    ofdmaDownLink: true
    ofdmaMultiRu: true
    ofdmaUpLink: true
    profileName: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

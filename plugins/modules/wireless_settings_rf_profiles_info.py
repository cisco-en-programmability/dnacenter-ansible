#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessSettings_rfProfiles_info
short_description: Information module for Wirelesssettings Rfprofiles
description:
- Get all Wirelesssettings Rfprofiles.
- Get Wirelesssettings Rfprofiles by id.
- This API allows the user to get a RF Profile by RF Profile ID.
- This API allows the user to get all RF Profiles.
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
    - Id path parameter. RF Profile ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetRFProfileByID
  description: Complete reference of the GetRFProfileByID API.
  link: https://developer.cisco.com/docs/dna-center/#!get-rf-profile-by-id
- name: Cisco DNA Center documentation for Wireless GetRFProfiles
  description: Complete reference of the GetRFProfiles API.
  link: https://developer.cisco.com/docs/dna-center/#!get-rf-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_rf_profile_by_id,
    wireless.Wireless.get_rf_profiles,

  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/rfProfiles,
    get /dna/intent/api/v1/wirelessSettings/rfProfiles/{id},

"""

EXAMPLES = r"""
- name: Get all Wirelesssettings Rfprofiles
  cisco.dnac.wirelessSettings_rfProfiles_info:
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

- name: Get Wirelesssettings Rfprofiles by id
  cisco.dnac.wirelessSettings_rfProfiles_info:
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
        "rfProfileName": "string",
        "defaultRfProfile": true,
        "enableRadioTypeA": true,
        "enableRadioTypeB": true,
        "enableRadioType6GHz": true,
        "enableCustom": true,
        "radioTypeAProperties": {
          "parentProfile": "string",
          "radioChannels": "string",
          "dataRates": "string",
          "mandatoryDataRates": "string",
          "powerThresholdV1": 0,
          "rxSopThreshold": "string",
          "minPowerLevel": 0,
          "maxPowerLevel": 0,
          "channelWidth": "string",
          "preamblePuncture": true
        },
        "radioTypeBProperties": {
          "parentProfile": "string",
          "radioChannels": "string",
          "dataRates": "string",
          "mandatoryDataRates": "string",
          "powerThresholdV1": 0,
          "rxSopThreshold": "string",
          "minPowerLevel": 0,
          "maxPowerLevel": 0
        },
        "radioType6GHzProperties": {
          "parentProfile": "string",
          "radioChannels": "string",
          "dataRates": "string",
          "mandatoryDataRates": "string",
          "powerThresholdV1": 0,
          "rxSopThreshold": "string",
          "minPowerLevel": 0,
          "maxPowerLevel": 0,
          "enableStandardPowerService": true,
          "multiBssidProperties": {
            "dot11axParameters": {
              "ofdmaDownLink": true,
              "ofdmaUpLink": true,
              "muMimoUpLink": true,
              "muMimoDownLink": true
            },
            "dot11beParameters": {
              "ofdmaDownLink": true,
              "ofdmaUpLink": true,
              "muMimoUpLink": true,
              "muMimoDownLink": true,
              "ofdmaMultiRu": true
            },
            "targetWakeTime": true,
            "twtBroadcastSupport": true
          },
          "preamblePuncture": true,
          "minDbsWidth": 0,
          "maxDbsWidth": 0
        },
        "id": "string"
      },
      "version": "string"
    }
"""

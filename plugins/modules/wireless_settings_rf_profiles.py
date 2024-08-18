#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessSettings_rfProfiles
short_description: Resource module for Wirelesssettings Rfprofiles
description:
- Manage operations create, update and delete of the resource Wirelesssettings Rfprofiles.
- This API allows the user to create a custom RF Profile.
- This API allows the user to delete a custom RF Profile.
- This API allows the user to update a custom RF Profile.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  defaultRfProfile:
    description: True if RF Profile is default, else False. Maximum of only 1 RF Profile
      can be marked as default at any given time.
    type: bool
  enableRadioType6GHz:
    description: True if 6 GHz radio band is enabled in the RF Profile, else False.
    type: bool
  enableRadioTypeA:
    description: True if 5 GHz radio band is enabled in the RF Profile, else False.
    type: bool
  enableRadioTypeB:
    description: True if 2.4 GHz radio band is enabled in the RF Profile, else False.
    type: bool
  id:
    description: Id path parameter. RF Profile ID.
    type: str
  radioType6GHzProperties:
    description: Wireless Settings Rf Profiles's radioType6GHzProperties.
    suboptions:
      dataRates:
        description: Data rates of 6 GHz radio band passed in comma separated format
          without any spaces. Permissible values 6, 9, 12, 18, 24, 36, 48, 54.
        type: str
      enableStandardPowerService:
        description: True if Standard Power Service is enabled, else False.
        type: bool
      mandatoryDataRates:
        description: Mandatory data rates of 6 GHz radio band passed in comma separated
          format without any spaces and must be a subset of selected dataRates with
          maximum of 2 values. Permissible values 6, 9, 12, 18, 24, 36, 48, 54.
        type: str
      maxDbsWidth:
        description: Maximum DBS Width (Permissible Values 20,40,80,160,320).
        type: int
      maxPowerLevel:
        description: Maximum power level of 6 GHz radio band.
        type: int
      minDbsWidth:
        description: Minimum DBS Width (Permissible Values 20,40,80,160,320).
        type: int
      minPowerLevel:
        description: Minimum power level of 6 GHz radio band.
        type: int
      multiBssidProperties:
        description: Wireless Settings Rf Profiles's multiBssidProperties.
        suboptions:
          dot11axParameters:
            description: Wireless Settings Rf Profiles's dot11axParameters.
            suboptions:
              muMimoDownLink:
                description: MU-MIMO Downlink.
                type: bool
              muMimoUpLink:
                description: MU-MIMO Uplink.
                type: bool
              ofdmaDownLink:
                description: OFDMA Downlink.
                type: bool
              ofdmaUpLink:
                description: OFDMA Uplink.
                type: bool
            type: dict
          dot11beParameters:
            description: Wireless Settings Rf Profiles's dot11beParameters.
            suboptions:
              muMimoDownLink:
                description: MU-MIMO Downlink.
                type: bool
              muMimoUpLink:
                description: MU-MIMO Uplink.
                type: bool
              ofdmaDownLink:
                description: OFDMA Downlink.
                type: bool
              ofdmaMultiRu:
                description: OFDMA Multi-RU.
                type: bool
              ofdmaUpLink:
                description: OFDMA Uplink.
                type: bool
            type: dict
          targetWakeTime:
            description: Target Wake Time.
            type: bool
          twtBroadcastSupport:
            description: TWT Broadcast Support.
            type: bool
        type: dict
      parentProfile:
        description: Parent profile of 6 GHz radio band.
        type: str
      powerThresholdV1:
        description: Power threshold of 6 GHz radio band.
        type: int
      preamblePuncture:
        description: Enable or Disable Preamble Puncturing. This Wifi 7 configuration
          is applicable to wireless IOS devices supporting 17.15 and higher.
        type: bool
      radioChannels:
        description: DCA channels of 6 GHz radio band passed in comma separated format
          without any spaces. Permissible values 1, 5, 9, 13, 17, 21, 25, 29, 33, 37,
          41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109,
          113, 117, 121, 125, 129, 133, 137, 141, 145, 149, 153, 157, 161, 165, 169,
          173, 177, 181, 185, 189, 193, 197, 201, 205, 209, 213, 217, 221, 225, 229,
          233.
        type: str
      rxSopThreshold:
        description: RX-SOP threshold of 6 GHz radio band.
        type: str
    type: dict
  radioTypeAProperties:
    description: Wireless Settings Rf Profiles's radioTypeAProperties.
    suboptions:
      channelWidth:
        description: Channel Width.
        type: str
      dataRates:
        description: Data rates of 5 GHz radio band passed in comma separated format
          without any spaces. Permissible values 6, 9, 12, 18, 24, 36, 48, 54.
        type: str
      mandatoryDataRates:
        description: Mandatory data rates of 5 GHz radio band passed in comma separated
          format without any spaces and must be a subset of selected dataRates with
          maximum of 2 values. Permissible values 6, 9, 12, 18, 24, 36, 48, 54.
        type: str
      maxPowerLevel:
        description: Maximum power level of 5 GHz radio band.
        type: int
      minPowerLevel:
        description: Minimum power level of 5 GHz radio band.
        type: int
      parentProfile:
        description: Parent profile of 5 GHz radio band.
        type: str
      powerThresholdV1:
        description: Power threshold of 5 GHz radio band.
        type: int
      preamblePuncture:
        description: Enable or Disable Preamble Puncturing. This Wifi 7 configuration
          is applicable to wireless IOS devices supporting 17.15 and higher.
        type: bool
      radioChannels:
        description: DCA channels of 5 GHz radio band passed in comma separated format
          without any spaces. Permissible values 36, 40, 44, 48, 52, 56, 60, 64, 100,
          104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 149, 153, 157, 161,
          165, 169, 173.
        type: str
      rxSopThreshold:
        description: RX-SOP threshold of 5 GHz radio band.
        type: str
    type: dict
  radioTypeBProperties:
    description: Wireless Settings Rf Profiles's radioTypeBProperties.
    suboptions:
      dataRates:
        description: Data rates of 2.4 GHz radio band passed in comma separated format
          without any spaces. Permissible values 1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36,
          48, 54.
        type: str
      mandatoryDataRates:
        description: Mandatory data rates of 2.4 GHz radio band passed in comma separated
          format without any spaces and must be a subset of selected dataRates with
          maximum of 2 values. Permissible values 1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36,
          48, 54.
        type: str
      maxPowerLevel:
        description: Maximum power level of 2.4 GHz radio band.
        type: int
      minPowerLevel:
        description: Minimum power level of 2.4 GHz radio band.
        type: int
      parentProfile:
        description: Parent profile of 2.4 GHz radio band.
        type: str
      powerThresholdV1:
        description: Power threshold of 2.4 GHz radio band.
        type: int
      radioChannels:
        description: DCA channels of 2.4 GHz radio band passed in comma separated format
          without any spaces. Permissible values 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
          12, 13, 14.
        type: str
      rxSopThreshold:
        description: RX-SOP threshold of 2.4 GHz radio band.
        type: str
    type: dict
  rfProfileName:
    description: RF Profile Name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless CreateRFProfile
  description: Complete reference of the CreateRFProfile API.
  link: https://developer.cisco.com/docs/dna-center/#!create-rf-profile
- name: Cisco DNA Center documentation for Wireless DeleteRFProfile
  description: Complete reference of the DeleteRFProfile API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-rf-profile
- name: Cisco DNA Center documentation for Wireless UpdateRFProfile
  description: Complete reference of the UpdateRFProfile API.
  link: https://developer.cisco.com/docs/dna-center/#!update-rf-profile
notes:
  - SDK Method used are
    wireless.Wireless.create_rf_profile,
    wireless.Wireless.delete_rf_profile,
    wireless.Wireless.update_rf_profile,

  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/rfProfiles,
    delete /dna/intent/api/v1/wirelessSettings/rfProfiles/{id},
    put /dna/intent/api/v1/wirelessSettings/rfProfiles/{id},

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wirelessSettings_rfProfiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    defaultRfProfile: true
    enableRadioType6GHz: true
    enableRadioTypeA: true
    enableRadioTypeB: true
    radioType6GHzProperties:
      dataRates: string
      enableStandardPowerService: true
      mandatoryDataRates: string
      maxDbsWidth: 0
      maxPowerLevel: 0
      minDbsWidth: 0
      minPowerLevel: 0
      multiBssidProperties:
        dot11axParameters:
          muMimoDownLink: true
          muMimoUpLink: true
          ofdmaDownLink: true
          ofdmaUpLink: true
        dot11beParameters:
          muMimoDownLink: true
          muMimoUpLink: true
          ofdmaDownLink: true
          ofdmaMultiRu: true
          ofdmaUpLink: true
        targetWakeTime: true
        twtBroadcastSupport: true
      parentProfile: string
      powerThresholdV1: 0
      preamblePuncture: true
      radioChannels: string
      rxSopThreshold: string
    radioTypeAProperties:
      channelWidth: string
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
      preamblePuncture: true
      radioChannels: string
      rxSopThreshold: string
    radioTypeBProperties:
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
      radioChannels: string
      rxSopThreshold: string
    rfProfileName: string

- name: Delete by id
  cisco.dnac.wirelessSettings_rfProfiles:
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
  cisco.dnac.wirelessSettings_rfProfiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    defaultRfProfile: true
    enableRadioType6GHz: true
    enableRadioTypeA: true
    enableRadioTypeB: true
    id: string
    radioType6GHzProperties:
      dataRates: string
      enableStandardPowerService: true
      mandatoryDataRates: string
      maxDbsWidth: 0
      maxPowerLevel: 0
      minDbsWidth: 0
      minPowerLevel: 0
      multiBssidProperties:
        dot11axParameters:
          muMimoDownLink: true
          muMimoUpLink: true
          ofdmaDownLink: true
          ofdmaUpLink: true
        dot11beParameters:
          muMimoDownLink: true
          muMimoUpLink: true
          ofdmaDownLink: true
          ofdmaMultiRu: true
          ofdmaUpLink: true
        targetWakeTime: true
        twtBroadcastSupport: true
      parentProfile: string
      powerThresholdV1: 0
      preamblePuncture: true
      radioChannels: string
      rxSopThreshold: string
    radioTypeAProperties:
      channelWidth: string
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
      preamblePuncture: true
      radioChannels: string
      rxSopThreshold: string
    radioTypeBProperties:
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
      radioChannels: string
      rxSopThreshold: string
    rfProfileName: string

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

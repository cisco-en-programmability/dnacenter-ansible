#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_rf_profile
short_description: Resource module for Wireless Rf Profile
description:
- Manage operations create and delete of the resource Wireless Rf Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  channelWidth:
    description: Wireless Rf Profile's channelWidth.
    type: str
  defaultRfProfile:
    description: DefaultRfProfile flag.
    type: bool
  enableBrownField:
    description: EnableBrownField flag.
    type: bool
  enableCustom:
    description: EnableCustom flag.
    type: bool
  enableRadioTypeA:
    description: EnableRadioTypeA flag.
    type: bool
  enableRadioTypeB:
    description: EnableRadioTypeB flag.
    type: bool
  name:
    description: Wireless Rf Profile's name.
    type: str
  radioTypeAProperties:
    description: Wireless Rf Profile's radioTypeAProperties.
    suboptions:
      dataRates:
        description: Wireless Rf Profile's dataRates.
        type: str
      mandatoryDataRates:
        description: Wireless Rf Profile's mandatoryDataRates.
        type: str
      maxPowerLevel:
        description: Wireless Rf Profile's maxPowerLevel.
        type: int
      minPowerLevel:
        description: Wireless Rf Profile's minPowerLevel.
        type: int
      parentProfile:
        description: Wireless Rf Profile's parentProfile.
        type: str
      powerThresholdV1:
        description: Wireless Rf Profile's powerThresholdV1.
        type: int
      radioChannels:
        description: Wireless Rf Profile's radioChannels.
        type: str
      rxSopThreshold:
        description: Wireless Rf Profile's rxSopThreshold.
        type: str
    type: dict
  radioTypeBProperties:
    description: Wireless Rf Profile's radioTypeBProperties.
    suboptions:
      dataRates:
        description: Wireless Rf Profile's dataRates.
        type: str
      mandatoryDataRates:
        description: Wireless Rf Profile's mandatoryDataRates.
        type: str
      maxPowerLevel:
        description: Wireless Rf Profile's maxPowerLevel.
        type: int
      minPowerLevel:
        description: Wireless Rf Profile's minPowerLevel.
        type: int
      parentProfile:
        description: Wireless Rf Profile's parentProfile.
        type: str
      powerThresholdV1:
        description: Wireless Rf Profile's powerThresholdV1.
        type: int
      radioChannels:
        description: Wireless Rf Profile's radioChannels.
        type: str
      rxSopThreshold:
        description: Wireless Rf Profile's rxSopThreshold.
        type: str
    type: dict
  rf_profile_name:
    description: Rf-profile-name path parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Rf Profile reference
  description: Complete reference of the Wireless Rf Profile object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_rf_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    channelWidth: string
    defaultRfProfile: true
    enableBrownField: true
    enableCustom: true
    enableRadioTypeA: true
    enableRadioTypeB: true
    name: string
    radioTypeAProperties:
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
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

- name: Delete by name
  cisco.dnac.wireless_rf_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    rf_profile_name: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionUrl": "string",
      "message": "string"
    }
"""

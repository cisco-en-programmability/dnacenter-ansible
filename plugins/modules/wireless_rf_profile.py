#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_rf_profile
short_description: Manage WirelessRfProfile objects of Wireless
description:
- Retrieve all RF profiles.
- Create or Update RF profile.
- Delete RF profile(s).
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  rf_profile_name:
    description:
    - Rf-profile-name query parameter.
    - Rf-profile-name path parameter.
    - Required for state delete.
    type: str
  channelWidth:
    description:
    - Channel Width, property of the request body.
    - Required for state create.
    type: str
  defaultRfProfile:
    description:
    - DefaultRfProfile, property of the request body.
    - Required for state create.
    type: bool
  enableBrownField:
    description:
    - EnableBrownField, property of the request body.
    - Required for state create.
    type: bool
  enableCustom:
    description:
    - EnableCustom, property of the request body.
    - Required for state create.
    type: bool
  enableRadioTypeA:
    description:
    - EnableRadioTypeA, property of the request body.
    - Required for state create.
    type: bool
  enableRadioTypeB:
    description:
    - EnableRadioTypeB, property of the request body.
    - Required for state create.
    type: bool
  name:
    description:
    - Name, property of the request body.
    - Required for state create.
    type: str
  radioTypeAProperties:
    description:
    - Radio Type AProperties, property of the request body.
    type: dict
    suboptions:
      parentProfile:
        description:
        - It is the wireless rf profile's parentProfile.
        type: str
      radioChannels:
        description:
        - It is the wireless rf profile's radioChannels.
        type: str
      dataRates:
        description:
        - It is the wireless rf profile's dataRates.
        type: str
      mandatoryDataRates:
        description:
        - It is the wireless rf profile's mandatoryDataRates.
        type: str
      powerThresholdV1:
        description:
        - It is the wireless rf profile's powerThresholdV1.
        type: int
      rxSopThreshold:
        description:
        - It is the wireless rf profile's rxSopThreshold.
        type: str
      minPowerLevel:
        description:
        - It is the wireless rf profile's minPowerLevel.
        type: int
      maxPowerLevel:
        description:
        - It is the wireless rf profile's maxPowerLevel.
        type: int

  radioTypeBProperties:
    description:
    - Radio Type BProperties, property of the request body.
    type: dict
    suboptions:
      parentProfile:
        description:
        - It is the wireless rf profile's parentProfile.
        type: str
      radioChannels:
        description:
        - It is the wireless rf profile's radioChannels.
        type: str
      dataRates:
        description:
        - It is the wireless rf profile's dataRates.
        type: str
      mandatoryDataRates:
        description:
        - It is the wireless rf profile's mandatoryDataRates.
        type: str
      powerThresholdV1:
        description:
        - It is the wireless rf profile's powerThresholdV1.
        type: int
      rxSopThreshold:
        description:
        - It is the wireless rf profile's rxSopThreshold.
        type: str
      minPowerLevel:
        description:
        - It is the wireless rf profile's minPowerLevel.
        type: int
      maxPowerLevel:
        description:
        - It is the wireless rf profile's maxPowerLevel.
        type: int


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.wireless_rf_profile
# Reference by Internet resource
- name: WirelessRfProfile reference
  description: Complete reference of the WirelessRfProfile object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: WirelessRfProfile reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: retrieve_rf_profiles
  cisco.dnac.wireless_rf_profile:
    state: query  # required
    rf_profile_name: SomeValue  # string
  register: query_result

- name: create_or_update_rf_profile
  cisco.dnac.wireless_rf_profile:
    state: create  # required
    channelWidth: SomeValue  # string, required
    defaultRfProfile: True  # boolean, required
    enableBrownField: True  # boolean, required
    enableCustom: True  # boolean, required
    enableRadioTypeA: True  # boolean, required
    enableRadioTypeB: True  # boolean, required
    name: SomeValue  # string, required
    radioTypeAProperties:
      parentProfile: SomeValue  # string
      radioChannels: SomeValue  # string
      dataRates: SomeValue  # string
      mandatoryDataRates: SomeValue  # string
      powerThresholdV1: 1  #  number
      rxSopThreshold: SomeValue  # string
      minPowerLevel: 1  #  number
      maxPowerLevel: 1  #  number
    radioTypeBProperties:
      parentProfile: SomeValue  # string
      radioChannels: SomeValue  # string
      dataRates: SomeValue  # string
      mandatoryDataRates: SomeValue  # string
      powerThresholdV1: 1  #  number
      rxSopThreshold: SomeValue  # string
      minPowerLevel: 1  #  number
      maxPowerLevel: 1  #  number

- name: delete_rf_profiles
  cisco.dnac.wireless_rf_profile:
    state: delete  # required
    rf_profile_name: SomeValue  # string, required

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: array
  sample:
"""

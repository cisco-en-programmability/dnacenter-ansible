#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

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

RETURN = """
retrieve_rf_profiles:
    description: Retrieve all RF profiles.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        name:
          description: It is the wireless rf profile's name.
          returned: always
          type: str
          sample: '<name>'
        parentProfileA:
          description: It is the wireless rf profile's parentProfileA.
          returned: always
          type: str
          sample: '<parentprofilea>'
        parentProfileB:
          description: It is the wireless rf profile's parentProfileB.
          returned: always
          type: str
          sample: '<parentprofileb>'
        enableARadioType:
          description: It is the wireless rf profile's enableARadioType.
          returned: always
          type: bool
          sample: false
        enableBRadioType:
          description: It is the wireless rf profile's enableBRadioType.
          returned: always
          type: bool
          sample: false
        channelWidth:
          description: It is the wireless rf profile's channelWidth.
          returned: always
          type: str
          sample: '<channelwidth>'
        aRadioChannels:
          description: It is the wireless rf profile's aRadioChannels.
          returned: always
          type: str
          sample: '<aradiochannels>'
        bRadioChannels:
          description: It is the wireless rf profile's bRadioChannels.
          returned: always
          type: str
          sample: '<bradiochannels>'
        dataRatesA:
          description: It is the wireless rf profile's dataRatesA.
          returned: always
          type: str
          sample: '<dataratesa>'
        dataRatesB:
          description: It is the wireless rf profile's dataRatesB.
          returned: always
          type: str
          sample: '<dataratesb>'
        mandatoryDataRatesA:
          description: It is the wireless rf profile's mandatoryDataRatesA.
          returned: always
          type: str
          sample: '<mandatorydataratesa>'
        mandatoryDataRatesB:
          description: It is the wireless rf profile's mandatoryDataRatesB.
          returned: always
          type: str
          sample: '<mandatorydataratesb>'
        enableCustom:
          description: It is the wireless rf profile's enableCustom.
          returned: always
          type: bool
          sample: false
        minPowerLevelA:
          description: It is the wireless rf profile's minPowerLevelA.
          returned: always
          type: str
          sample: '<minpowerlevela>'
        minPowerLevelB:
          description: It is the wireless rf profile's minPowerLevelB.
          returned: always
          type: str
          sample: '<minpowerlevelb>'
        maxPowerLevelA:
          description: It is the wireless rf profile's maxPowerLevelA.
          returned: always
          type: str
          sample: '<maxpowerlevela>'
        maxPowerLevelB:
          description: It is the wireless rf profile's maxPowerLevelB.
          returned: always
          type: str
          sample: '<maxpowerlevelb>'
        powerThresholdV1A:
          description: It is the wireless rf profile's powerThresholdV1A.
          returned: always
          type: int
          sample: 0
        powerThresholdV1B:
          description: It is the wireless rf profile's powerThresholdV1B.
          returned: always
          type: int
          sample: 0
        rxSopThresholdA:
          description: It is the wireless rf profile's rxSopThresholdA.
          returned: always
          type: str
          sample: '<rxsopthresholda>'
        rxSopThresholdB:
          description: It is the wireless rf profile's rxSopThresholdB.
          returned: always
          type: str
          sample: '<rxsopthresholdb>'
        defaultRfProfile:
          description: It is the wireless rf profile's defaultRfProfile.
          returned: always
          type: bool
          sample: false
        enableBrownField:
          description: It is the wireless rf profile's enableBrownField.
          returned: always
          type: bool
          sample: false


create_or_update_rf_profile:
    description: Create or Update RF profile.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionUrl:
      description: Execution Url, property of the response body.
      returned: success
      type: str
      sample: '<executionurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

delete_rf_profiles:
    description: Delete RF profile(s).
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionUrl:
      description: Execution Url, property of the response body.
      returned: success
      type: str
      sample: '<executionurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

"""

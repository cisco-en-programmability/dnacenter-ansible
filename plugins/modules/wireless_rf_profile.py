#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: wireless_rf_profile
short_description: Manage WirelessRfProfile objects of Wireless
description:
- Retrieve all RF profiles.
- Create or Update RF profile.
- Delete RF profile(s).
version_added: '1.0'
author: first last (@GitHubID)
options:
    rf_profile_name:
        description:
        - Rf-profile-name query parameter.
        - Required for state delete.
        type: str
    channelWidth:
        description:
        - Channel Width, property of the request body.
        type: str
        required: True
    defaultRfProfile:
        description:
        - DefaultRfProfile, property of the request body.
        type: bool
        required: True
    enableBrownField:
        description:
        - EnableBrownField, property of the request body.
        type: bool
        required: True
    enableCustom:
        description:
        - EnableCustom, property of the request body.
        type: bool
        required: True
    enableRadioTypeA:
        description:
        - EnableRadioTypeA, property of the request body.
        type: bool
        required: True
    enableRadioTypeB:
        description:
        - EnableRadioTypeB, property of the request body.
        type: bool
        required: True
    name:
        description:
        - Name, property of the request body.
        type: str
        required: True
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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Retrieve all RF profiles.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                name:
                    description: It is the wireless rf profile's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                parentProfileA:
                    description: It is the wireless rf profile's parentProfileA.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                parentProfileB:
                    description: It is the wireless rf profile's parentProfileB.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enableARadioType:
                    description: It is the wireless rf profile's enableARadioType.
                    returned: success,changed,always
                    type: bool
                    sample: false
                enableBRadioType:
                    description: It is the wireless rf profile's enableBRadioType.
                    returned: success,changed,always
                    type: bool
                    sample: false
                channelWidth:
                    description: It is the wireless rf profile's channelWidth.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                aRadioChannels:
                    description: It is the wireless rf profile's aRadioChannels.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                bRadioChannels:
                    description: It is the wireless rf profile's bRadioChannels.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                dataRatesA:
                    description: It is the wireless rf profile's dataRatesA.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                dataRatesB:
                    description: It is the wireless rf profile's dataRatesB.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mandatoryDataRatesA:
                    description: It is the wireless rf profile's mandatoryDataRatesA.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mandatoryDataRatesB:
                    description: It is the wireless rf profile's mandatoryDataRatesB.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enableCustom:
                    description: It is the wireless rf profile's enableCustom.
                    returned: success,changed,always
                    type: bool
                    sample: false
                minPowerLevelA:
                    description: It is the wireless rf profile's minPowerLevelA.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                minPowerLevelB:
                    description: It is the wireless rf profile's minPowerLevelB.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                maxPowerLevelA:
                    description: It is the wireless rf profile's maxPowerLevelA.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                maxPowerLevelB:
                    description: It is the wireless rf profile's maxPowerLevelB.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                powerThresholdV1A:
                    description: It is the wireless rf profile's powerThresholdV1A.
                    returned: success,changed,always
                    type: int
                    sample: 0
                powerThresholdV1B:
                    description: It is the wireless rf profile's powerThresholdV1B.
                    returned: success,changed,always
                    type: int
                    sample: 0
                rxSopThresholdA:
                    description: It is the wireless rf profile's rxSopThresholdA.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                rxSopThresholdB:
                    description: It is the wireless rf profile's rxSopThresholdB.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                defaultRfProfile:
                    description: It is the wireless rf profile's defaultRfProfile.
                    returned: success,changed,always
                    type: bool
                    sample: false
                enableBrownField:
                    description: It is the wireless rf profile's enableBrownField.
                    returned: success,changed,always
                    type: bool
                    sample: false


data_1:
    description: Create or Update RF profile.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionUrl:
            description: Execution Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Delete RF profile(s).
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionUrl:
            description: Execution Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.wireless_rf_profile import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
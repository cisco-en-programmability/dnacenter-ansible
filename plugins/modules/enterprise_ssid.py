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
module: enterprise_ssid
short_description: Manage EnterpriseSsid objects of Wireless
description:
- Gets either one or all the enterprise SSID.
- Creates enterprise SSID.
- Deletes given enterprise SSID.
version_added: '1.0'
author: first last (@GitHubID)
options:
    ssid_name:
        description:
        - Enter the enterprise SSID name that needs to be retrieved. If not entered, all the enterprise SSIDs will be retrieved.
        - Required for state delete.
        type: str
    enableBroadcastSSID:
        description:
        - EnableBroadcastSSID, property of the request body.
        type: bool
    enableFastLane:
        description:
        - EnableFastLane, property of the request body.
        type: bool
    enableMACFiltering:
        description:
        - EnableMACFiltering, property of the request body.
        type: bool
    fastTransition:
        description:
        - Fast Transition, property of the request body.
        - Available values are 'Adaptive', 'Enable' and 'Disable'.
        type: str
    name:
        description:
        - Enter SSID Name, property of the request body. Constraints: maxLength set to 32.
        type: str
        required: True
    passphrase:
        description:
        - Pass Phrase (Only applicable for SSID with PERSONAL security level), property of the request body. Constraints: maxLength set to 63 and minLength set to 8.
        type: str
    radioPolicy:
        description:
        - Radio Policy, property of the request body.
        - Available values are 'Dual band operation (2.4GHz and 5GHz)', 'Dual band operation with band select', '5GHz only' and '2.4GHz only'.
        type: str
    securityLevel:
        description:
        - Security Level, property of the request body.
        - Available values are 'WPA2_ENTERPRISE', 'WPA2_PERSONAL' and 'OPEN'.
        type: str
        required: True
    trafficType:
        description:
        - Traffic Type, property of the request body.
        - Available values are 'voicedata' and 'data'.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.enterprise_ssid
# Reference by Internet resource
- name: EnterpriseSsid reference
  description: Complete reference of the EnterpriseSsid object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EnterpriseSsid reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Gets either one or all the enterprise SSID.
    returned: success,changed,always
    type: list
    contains:
        instanceUuid:
            description: It is the enterprise ssid's instanceUuid.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: It is the enterprise ssid's version.
            returned: success,changed,always
            type: int
            sample: 0
        ssidDetails:
            description: It is the enterprise ssid's ssidDetails.
            returned: success,changed,always
            type: list
            contains:
                name:
                    description: It is the enterprise ssid's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wlanType:
                    description: It is the enterprise ssid's wlanType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enableFastLane:
                    description: It is the enterprise ssid's enableFastLane.
                    returned: success,changed,always
                    type: bool
                    sample: false
                securityLevel:
                    description: It is the enterprise ssid's securityLevel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authServer:
                    description: It is the enterprise ssid's authServer.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                passphrase:
                    description: It is the enterprise ssid's passphrase.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                trafficType:
                    description: It is the enterprise ssid's trafficType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enableMACFiltering:
                    description: It is the enterprise ssid's enableMACFiltering.
                    returned: success,changed,always
                    type: bool
                    sample: false
                isEnabled:
                    description: It is the enterprise ssid's isEnabled.
                    returned: success,changed,always
                    type: bool
                    sample: false
                isFabric:
                    description: It is the enterprise ssid's isFabric.
                    returned: success,changed,always
                    type: bool
                    sample: false
                fastTransition:
                    description: It is the enterprise ssid's fastTransition.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                radioPolicy:
                    description: It is the enterprise ssid's radioPolicy.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enableBroadcastSSID:
                    description: It is the enterprise ssid's enableBroadcastSSID.
                    returned: success,changed,always
                    type: bool
                    sample: false

        groupUuid:
            description: It is the enterprise ssid's groupUuid.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        inheritedGroupUuid:
            description: It is the enterprise ssid's inheritedGroupUuid.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        inheritedGroupName:
            description: It is the enterprise ssid's inheritedGroupName.
            returned: success,changed,always
            type: str
            sample: 'sample_string'


data_1:
    description: Creates enterprise SSID.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Deletes given enterprise SSID.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.enterprise_ssid import module_definition


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
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
module: ssid
short_description: Manage Ssid objects of Wireless
description:
- Creates SSID, updates the SSID to the corresponding site profiles and provision it to the devices matching the given sites.
- Removes SSID or WLAN from the network profile, reprovision the device(s) and deletes the SSID or WLAN from DNA Center.
version_added: '1.0'
author: first last (@GitHubID)
options:
    enable_fabric:
        description:
        - EnableFabric, property of the request body.
        type: bool
        required: True
    flex_connect:
        description:
        - Flex Connect - Applicable for non fabric profile, property of the request body.
        type: dict
        suboptions:
            enableFlexConnect:
                description:
                - It is the Ssid's enableFlexConnect.
                type: bool
            localToVlan:
                description:
                - It is the Ssid's localToVlan.
                type: int

    managed_aplocations:
        description:
        - Managed AP Locations (Enter entire Site(s) hierarchy), property of the request body (list of strings).
        type: list
        required: True
    ssid_details:
        description:
        - SsidDetails, property of the request body.
        type: dict
        required: True
        suboptions:
            name:
                description:
                - It is the Ssid's name.
                type: str
            securityLevel:
                description:
                - It is the Ssid's securityLevel.
                type: str
            enableFastLane:
                description:
                - It is the Ssid's enableFastLane.
                type: bool
            passphrase:
                description:
                - It is the Ssid's passphrase.
                type: str
            trafficType:
                description:
                - It is the Ssid's trafficType.
                type: str
            enableBroadcastSSID:
                description:
                - It is the Ssid's enableBroadcastSSID.
                type: bool
            radioPolicy:
                description:
                - It is the Ssid's radioPolicy.
                type: str
            enableMACFiltering:
                description:
                - It is the Ssid's enableMACFiltering.
                type: bool
            fastTransition:
                description:
                - It is the Ssid's fastTransition.
                type: str
            webAuthURL:
                description:
                - It is the Ssid's webAuthURL.
                type: str

    ssid_type:
        description:
        - SSID Type, property of the request body.
        type: str
        required: True
        choices: ['Guest', 'Enterprise']
    managed_aplocations:
        description:
        - ManagedAPLocations path parameter.
        type: str
        required: True
    ssid_name:
        description:
        - SsidName path parameter.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.ssid
# Reference by Internet resource
- name: Ssid reference
  description: Complete reference of the Ssid object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Ssid reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Creates SSID, updates the SSID to the corresponding site profiles and provision it to the devices matching the given sites.
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

data_1:
    description: Removes SSID or WLAN from the network profile, reprovision the device(s) and deletes the SSID or WLAN from DNA Center.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.ssid import module_definition


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

    if state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
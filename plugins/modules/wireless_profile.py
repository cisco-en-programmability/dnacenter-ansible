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
module: wireless_profile
short_description: Manage WirelessProfile objects of Wireless
description:
- Gets either one or all the wireless network profiles if no name is provided for network-profile.
- Creates Wireless Network Profile on DNAC and associates sites and SSIDs to it.
- Updates the wireless Network Profile with updated details provided. All sites to be present in the network profile should be provided.
- Delete the Wireless Profile from DNAC whose name is provided.
version_added: '1.0'
author: first last (@GitHubID)
options:
    profile_name:
        description:
        - ProfileName query parameter.
        type: str
    profileDetails:
        description:
        - Profile Details, property of the request body.
        type: dict
        required: True
        suboptions:
            name:
                description:
                - It is the wireless profile's name.
                type: str
            sites:
                description:
                - It is the wireless profile's sites.
                type: list
            ssidDetails:
                description:
                - It is the wireless profile's ssidDetails.
                type: list
                elements: dict
                suboptions:
                    enableFabric:
                        description:
                        - It is the wireless profile's enableFabric.
                        type: bool
                    flexConnect:
                        description:
                        - It is the wireless profile's flexConnect.
                        type: dict
                        suboptions:
                            enableFlexConnect:
                                description:
                                - It is the wireless profile's enableFlexConnect.
                                type: bool
                            localToVlan:
                                description:
                                - It is the wireless profile's localToVlan.
                                type: int

                    interfaceName:
                        description:
                        - It is the wireless profile's interfaceName.
                        type: str
                    name:
                        description:
                        - It is the wireless profile's name.
                        type: str
                    type:
                        description:
                        - It is the wireless profile's type.
                        type: str


    wireless_profile_name:
        description:
        - WirelessProfileName path parameter.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.wireless_profile
# Reference by Internet resource
- name: WirelessProfile reference
  description: Complete reference of the WirelessProfile object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: WirelessProfile reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Gets either one or all the wireless network profiles if no name is provided for network-profile.
    returned: success,changed,always
    type: list
    contains:
        profileDetails:
            description: It is the wireless profile's profileDetails.
            returned: success,changed,always
            type: dict
            contains:
                name:
                    description: It is the wireless profile's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                sites:
                    description: It is the wireless profile's sites.
                    returned: success,changed,always
                    type: list
                ssidDetails:
                    description: It is the wireless profile's ssidDetails.
                    returned: success,changed,always
                    type: list
                    contains:
                        name:
                            description: It is the wireless profile's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the wireless profile's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        enableFabric:
                            description: It is the wireless profile's enableFabric.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        flexConnect:
                            description: It is the wireless profile's flexConnect.
                            returned: success,changed,always
                            type: dict
                            contains:
                                enableFlexConnect:
                                    description: It is the wireless profile's enableFlexConnect.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                localToVlan:
                                    description: It is the wireless profile's localToVlan.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        interfaceName:
                            description: It is the wireless profile's interfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'




data_1:
    description: Creates Wireless Network Profile on DNAC and associates sites and SSIDs to it.
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
    description: Updates the wireless Network Profile with updated details provided. All sites to be present in the network profile should be provided.
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

data_3:
    description: Delete the Wireless Profile from DNAC whose name is provided.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.wireless_profile import module_definition


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

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
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
module: service_provider
short_description: Manage ServiceProvider objects of NetworkSettings
description:
- API to get service provider details (QoS).
- API to create service provider profile(QOS).
- API to update SP profile.
- API to delete Service Provider profile (QoS).
version_added: '1.0'
author: first last (@GitHubID)
options:
    settings:
        description:
        - Settings, property of the request body.
        type: dict
        required: True
        suboptions:
            qos:
                description:
                - It is the service provider's qos.
                type: list
                elements: dict
                suboptions:
                    profileName:
                        description:
                        - It is the service provider's profileName.
                        type: str
                        required: True
                    model:
                        description:
                        - It is the service provider's model.
                        type: str
                        required: True
                    wanProvider:
                        description:
                        - It is the service provider's wanProvider.
                        type: str
                        required: True


    settings:
        description:
        - Settings, property of the request body.
        type: dict
        required: True
        suboptions:
            qos:
                description:
                - It is the service provider's qos.
                type: list
                elements: dict
                suboptions:
                    profileName:
                        description:
                        - It is the service provider's profileName.
                        type: str
                    model:
                        description:
                        - It is the service provider's model.
                        type: str
                    wanProvider:
                        description:
                        - It is the service provider's wanProvider.
                        type: str
                    oldProfileName:
                        description:
                        - It is the service provider's oldProfileName.
                        type: str
                        required: True


    sp_profile_name:
        description:
        - Sp profile name.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.service_provider
# Reference by Internet resource
- name: ServiceProvider reference
  description: Complete reference of the ServiceProvider object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ServiceProvider reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: API to get service provider details (QoS).
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                instanceType:
                    description: It is the service provider's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the service provider's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                namespace:
                    description: It is the service provider's namespace.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the service provider's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                key:
                    description: It is the service provider's key.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the service provider's version.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                value:
                    description: It is the service provider's value.
                    returned: success,changed,always
                    type: list
                    contains:
                        wanProvider:
                            description: It is the service provider's wanProvider.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        spProfileName:
                            description: It is the service provider's spProfileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        slaProfileName:
                            description: It is the service provider's slaProfileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                groupUuid:
                    description: It is the service provider's groupUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inheritedGroupUuid:
                    description: It is the service provider's inheritedGroupUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inheritedGroupName:
                    description: It is the service provider's inheritedGroupName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: API to create service provider profile(QOS).
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
    description: API to update SP profile.
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
    description: API to delete Service Provider profile (QoS).
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.service_provider import module_definition


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
        dnac.exec("post")

    elif state == "update":
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
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
module: applications
short_description: Manage Applications objects of ApplicationPolicy
description:
- Get Applications by offset/limit or by name.
- Delete existing application by its id.
- Create new Custom application.
- Edit the attributes of an existing application.
- Get the number of all existing Applications.
version_added: '1.0'
author: first last (@GitHubID)
options:
    limit:
        description:
        - The maximum number of Applications to be returned.
        type: int
    name:
        description:
        - Application's name.
        type: str
    offset:
        description:
        - The offset of the first application to be returned.
        type: int
    id:
        description:
        - Application's Id.
        type: str
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            applicationSet:
                description:
                - It is the Applications's applicationSet.
                type: dict
                suboptions:
                    idRef:
                        description:
                        - It is the Applications's idRef.
                        type: str

            id:
                description:
                - It is the Applications's id.
                type: str
            name:
                description:
                - It is the Applications's name.
                type: str
            networkApplications:
                description:
                - It is the Applications's networkApplications.
                type: list
                elements: dict
                suboptions:
                    appProtocol:
                        description:
                        - It is the Applications's appProtocol.
                        type: str
                    applicationSubType:
                        description:
                        - It is the Applications's applicationSubType.
                        type: str
                    applicationType:
                        description:
                        - It is the Applications's applicationType.
                        type: str
                    categoryId:
                        description:
                        - It is the Applications's categoryId.
                        type: str
                    displayName:
                        description:
                        - It is the Applications's displayName.
                        type: str
                    dscp:
                        description:
                        - It is the Applications's dscp.
                        type: str
                    engineId:
                        description:
                        - It is the Applications's engineId.
                        type: str
                    helpString:
                        description:
                        - It is the Applications's helpString.
                        type: str
                    id:
                        description:
                        - It is the Applications's id.
                        type: str
                    ignoreConflict:
                        description:
                        - It is the Applications's ignoreConflict.
                        type: str
                    longDescription:
                        description:
                        - It is the Applications's longDescription.
                        type: str
                    name:
                        description:
                        - It is the Applications's name.
                        type: str
                    popularity:
                        description:
                        - It is the Applications's popularity.
                        type: str
                    rank:
                        description:
                        - It is the Applications's rank.
                        type: str
                    serverName:
                        description:
                        - It is the Applications's serverName.
                        type: str
                    trafficClass:
                        description:
                        - It is the Applications's trafficClass.
                        type: str
                    url:
                        description:
                        - It is the Applications's url.
                        type: str

            networkIdentity:
                description:
                - It is the Applications's networkIdentity.
                type: list
                elements: dict
                suboptions:
                    displayName:
                        description:
                        - It is the Applications's displayName.
                        type: str
                    id:
                        description:
                        - It is the Applications's id.
                        type: str
                    lowerPort:
                        description:
                        - It is the Applications's lowerPort.
                        type: str
                    ports:
                        description:
                        - It is the Applications's ports.
                        type: str
                    protocol:
                        description:
                        - It is the Applications's protocol.
                        type: str
                    upperPort:
                        description:
                        - It is the Applications's upperPort.
                        type: str


    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.applications
# Reference by Internet resource
- name: Applications reference
  description: Complete reference of the Applications object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Applications reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Get Applications by offset/limit or by name.
    returned: success,changed,always
    type: list
    contains:
        id:
            description: It is the Applications's id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: It is the Applications's name.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        networkApplications:
            description: It is the Applications's networkApplications.
            returned: success,changed,always
            type: list
            contains:
                id:
                    description: It is the Applications's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                appProtocol:
                    description: It is the Applications's appProtocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                applicationSubType:
                    description: It is the Applications's applicationSubType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                applicationType:
                    description: It is the Applications's applicationType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                categoryId:
                    description: It is the Applications's categoryId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                displayName:
                    description: It is the Applications's displayName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                engineId:
                    description: It is the Applications's engineId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                helpString:
                    description: It is the Applications's helpString.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                longDescription:
                    description: It is the Applications's longDescription.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the Applications's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                popularity:
                    description: It is the Applications's popularity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                rank:
                    description: It is the Applications's rank.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                trafficClass:
                    description: It is the Applications's trafficClass.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serverName:
                    description: It is the Applications's serverName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                url:
                    description: It is the Applications's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                dscp:
                    description: It is the Applications's dscp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ignoreConflict:
                    description: It is the Applications's ignoreConflict.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        networkIdentity:
            description: It is the Applications's networkIdentity.
            returned: success,changed,always
            type: list
            contains:
                id:
                    description: It is the Applications's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                displayName:
                    description: It is the Applications's displayName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lowerPort:
                    description: It is the Applications's lowerPort.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ports:
                    description: It is the Applications's ports.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                protocol:
                    description: It is the Applications's protocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                upperPort:
                    description: It is the Applications's upperPort.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        applicationSet:
            description: It is the Applications's applicationSet.
            returned: success,changed,always
            type: dict
            contains:
                idRef:
                    description: It is the Applications's idRef.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'



data_1:
    description: Delete existing application by its id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Applications's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                url:
                    description: It is the Applications's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Create new Custom application.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Applications's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                url:
                    description: It is the Applications's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Edit the attributes of an existing application.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Applications's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                url:
                    description: It is the Applications's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_4:
    description: Get the number of all existing Applications.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.applications import module_definition


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
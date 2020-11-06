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
module: application_set
short_description: Manage ApplicationSet objects of ApplicationPolicy
description:
- Delete existing application-set by it's id.
- Get appllication-sets by offset/limit or by name.
- Create new custom application-set/s.
- Get the number of existing application-sets.
version_added: '1.0'
author: first last (@GitHubID)
options:
    id:
        description:
        - Id query parameter.
        type: str
    limit:
        description:
        - Limit query parameter.
        type: int
    name:
        description:
        - Name query parameter.
        type: str
    offset:
        description:
        - Offset query parameter.
        type: int
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            name:
                description:
                - It is the application set's name.
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
- module: cisco.dnac.plugins.module_utils.definitions.application_set
# Reference by Internet resource
- name: ApplicationSet reference
  description: Complete reference of the ApplicationSet object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ApplicationSet reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Delete existing application-set by it's id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the application set's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                url:
                    description: It is the application set's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Get appllication-sets by offset/limit or by name.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                id:
                    description: It is the application set's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                identitySource:
                    description: It is the application set's identitySource.
                    returned: success,changed,always
                    type: dict
                    contains:
                        id:
                            description: It is the application set's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the application set's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                name:
                    description: It is the application set's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


data_2:
    description: Create new custom application-set/s.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the application set's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                url:
                    description: It is the application set's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Get the number of existing application-sets.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.application_set import module_definition


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
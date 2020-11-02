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
module: tag
short_description: Manage Tag objects of Tag
description:
- Returns the Tags for given filter criteria.
- Creates Tag with specified Tag attributes.
- Updates a Tag specified by id.
- Deletes a Tag specified by id.
- Returns Tag specified by Id.
- Returns Tag count.
version_added: '1.0'
author: first last (@GitHubID)
options:
    additional_info_attributes:
        description:
        - AdditionalInfo.attributes query parameter.
        type: str
    additional_info_name_space:
        description:
        - AdditionalInfo.nameSpace query parameter.
        type: str
    field:
        description:
        - Available field names are :'name,id,parentId,type,additionalInfo.nameSpace,additionalInfo.attributes'.
        type: str
    level:
        description:
        - Level query parameter.
        type: str
    limit:
        description:
        - Limit query parameter.
        type: str
    name:
        description:
        - Tag name is mandatory when filter operation is used.
        type: str
    offset:
        description:
        - Offset query parameter.
        type: str
    order:
        description:
        - Available values are asc and des.
        type: str
    size:
        description:
        - Size in kilobytes(KB).
        type: str
    sort_by:
        description:
        - Only supported attribute is name. SortyBy is mandatory when order is used.
        type: str
    system_tag:
        description:
        - SystemTag query parameter.
        type: str
    description:
        description:
        - TagDTO's description.
        type: str
    dynamic_rules:
        description:
        - TagDTO's dynamicRules (list of objects).
        type: list
        elements: dict
        suboptions:
            memberType:
                description:
                - It is the Tag's memberType.
                type: str
            rules:
                description:
                - It is the Tag's rules.
                type: dict
                suboptions:
                    values:
                        description:
                        - It is the Tag's values.
                        type: list
                    items:
                        description:
                        - It is the Tag's items.
                        type: list
                    operation:
                        description:
                        - It is the Tag's operation.
                        type: str
                    name:
                        description:
                        - It is the Tag's name.
                        type: str
                    value:
                        description:
                        - It is the Tag's value.
                        type: str


    id:
        description:
        - TagDTO's id.
        type: str
    instance_tenant_id:
        description:
        - TagDTO's instanceTenantId.
        type: str
    name:
        description:
        - TagDTO's name.
        type: str
    system_tag:
        description:
        - TagDTO's systemTag.
        type: bool
    description:
        description:
        - TagDTO's description.
        type: str
    dynamic_rules:
        description:
        - TagDTO's dynamicRules (list of objects).
        type: list
        elements: dict
        suboptions:
            memberType:
                description:
                - It is the Tag's memberType.
                type: str
            rules:
                description:
                - It is the Tag's rules.
                type: dict
                suboptions:
                    values:
                        description:
                        - It is the Tag's values.
                        type: list
                    items:
                        description:
                        - It is the Tag's items.
                        type: list
                    operation:
                        description:
                        - It is the Tag's operation.
                        type: str
                    name:
                        description:
                        - It is the Tag's name.
                        type: str
                    value:
                        description:
                        - It is the Tag's value.
                        type: str


    id:
        description:
        - TagDTO's id.
        type: str
    instance_tenant_id:
        description:
        - TagDTO's instanceTenantId.
        type: str
    name:
        description:
        - TagDTO's name.
        type: str
    system_tag:
        description:
        - TagDTO's systemTag.
        type: bool
    id:
        description:
        - Tag ID.
        type: str
        required: True
    id:
        description:
        - Tag ID.
        type: str
        required: True
    attribute_name:
        description:
        - AttributeName query parameter.
        type: str
    level:
        description:
        - Level query parameter.
        type: str
    name:
        description:
        - Name query parameter.
        type: str
    name_space:
        description:
        - NameSpace query parameter.
        type: str
    size:
        description:
        - Size in kilobytes(KB).
        type: str
    system_tag:
        description:
        - SystemTag query parameter.
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
- module: cisco.dnac.plugins.module_utils.definitions.tag
# Reference by Internet resource
- name: Tag reference
  description: Complete reference of the Tag object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Tag reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns the Tags for given filter criteria.
    returned: success,changed,always
    type: dict
    contains:
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                systemTag:
                    description: It is the Tag's systemTag.
                    returned: success,changed,always
                    type: bool
                    sample: false
                description:
                    description: It is the Tag's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                dynamicRules:
                    description: It is the Tag's dynamicRules.
                    returned: success,changed,always
                    type: list
                    contains:
                        memberType:
                            description: It is the Tag's memberType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        rules:
                            description: It is the Tag's rules.
                            returned: success,changed,always
                            type: dict
                            contains:
                                values:
                                    description: It is the Tag's values.
                                    returned: success,changed,always
                                    type: list
                                items:
                                    description: It is the Tag's items.
                                    returned: success,changed,always
                                    type: list
                                operation:
                                    description: It is the Tag's operation.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                name:
                                    description: It is the Tag's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the Tag's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                name:
                    description: It is the Tag's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Tag's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Tag's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


data_1:
    description: Creates Tag with specified Tag attributes.
    returned: success,changed,always
    type: dict
    contains:
        version:
            description: TagDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        response:
            description: TagDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Tag's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Tag's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


data_2:
    description: Updates a Tag specified by id.
    returned: success,changed,always
    type: dict
    contains:
        version:
            description: TagDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        response:
            description: TagDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Tag's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Tag's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


data_3:
    description: Deletes a Tag specified by id.
    returned: success,changed,always
    type: dict
    contains:
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Tag's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Tag's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


data_4:
    description: Returns Tag specified by Id.
    returned: success,changed,always
    type: dict
    contains:
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                systemTag:
                    description: It is the Tag's systemTag.
                    returned: success,changed,always
                    type: bool
                    sample: false
                description:
                    description: It is the Tag's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                dynamicRules:
                    description: It is the Tag's dynamicRules.
                    returned: success,changed,always
                    type: list
                    contains:
                        memberType:
                            description: It is the Tag's memberType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        rules:
                            description: It is the Tag's rules.
                            returned: success,changed,always
                            type: dict
                            contains:
                                values:
                                    description: It is the Tag's values.
                                    returned: success,changed,always
                                    type: list
                                items:
                                    description: It is the Tag's items.
                                    returned: success,changed,always
                                    type: list
                                operation:
                                    description: It is the Tag's operation.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                name:
                                    description: It is the Tag's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the Tag's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                name:
                    description: It is the Tag's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Tag's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Tag's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


data_5:
    description: Returns Tag count.
    returned: success,changed,always
    type: dict
    contains:
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.tag import module_definition, TagExistenceCriteria


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

    elif state == "absent":
        dnac.exec("delete")

    elif state == "present":
        ec = TagExistenceCriteria(dnac)

        if ec.object_exists():
            dnac.exec("put")
            dnac.result.update({"warning": ec.WARN_OBJECT_EXISTS})

        else:
            dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
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
module: template_version
short_description: Manage TemplateVersion objects of ConfigurationTemplates
description:
- Creates Versioning for the current contents of the template.
- Returns the versions of a specified template.
version_added: '1.0'
author: first last (@GitHubID)
options:
    comments:
        description:
        - TemplateVersionRequestDTO's comments.
        type: str
    template_id:
        description:
        - TemplateVersionRequestDTO's templateId.
        type: str
    template_id:
        description:
        - TemplateId path parameter.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template_version
# Reference by Internet resource
- name: TemplateVersion reference
  description: Complete reference of the TemplateVersion object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TemplateVersion reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Creates Versioning for the current contents of the template.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: TemplateVersionRequestDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the template version's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the template version's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: TemplateVersionRequestDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Returns the versions of a specified template.
    returned: success,changed,always
    type: list
    contains:
        name:
            description: It is the template version's name.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        projectName:
            description: It is the template version's projectName.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        projectId:
            description: It is the template version's projectId.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        templateId:
            description: It is the template version's templateId.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        versionsInfo:
            description: It is the template version's versionsInfo.
            returned: success,changed,always
            type: list
            contains:
                id:
                    description: It is the template version's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the template version's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                versionTime:
                    description: It is the template version's versionTime.
                    returned: success,changed,always
                    type: int
                    sample: 0

        composite:
            description: It is the template version's composite.
            returned: success,changed,always
            type: bool
            sample: false


'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.template_version import module_definition


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

    elif state == "create":
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
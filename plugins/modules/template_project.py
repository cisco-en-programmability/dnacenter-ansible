#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: template_project
short_description: Manage TemplateProject objects of ConfigurationTemplates
description:
- Returns the projects in the system.
- Creates a new project.
- Updates an existing project.
- Deletes an existing Project.
version_added: '1.0'
author: first last (@GitHubID)
options:
    name:
        description:
        - Name of project to be searched.
        type: str
    createTime:
        description:
        - ProjectDTO's createTime.
        type: int
    description:
        description:
        - ProjectDTO's description.
        type: str
    id:
        description:
        - ProjectDTO's id.
        type: str
    lastUpdateTime:
        description:
        - ProjectDTO's lastUpdateTime.
        type: int
    tags:
        description:
        - ProjectDTO's tags (list of strings).
        type: list
    templates:
        description:
        - ProjectDTO's templates.
        type: dict
    project_id:
        description:
        - ProjectId path parameter.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template_project
# Reference by Internet resource
- name: TemplateProject reference
  description: Complete reference of the TemplateProject object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TemplateProject reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Returns the projects in the system.
    returned: success,changed,always
    type: list
    contains:
        name:
            description: It is the template project's name.
            returned: success,changed,always
            type: str
            sample: '<name>'
        id:
            description: It is the template project's id.
            returned: success,changed,always
            type: str
            sample: '478012'
        templates:
            description: It is the template project's templates.
            returned: success,changed,always
            type: list
            contains:
                name:
                    description: It is the template project's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                composite:
                    description: It is the template project's composite.
                    returned: success,changed,always
                    type: bool
                    sample: false
                id:
                    description: It is the template project's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'



data_1:
    description: Creates a new project.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: ProjectDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the template project's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the template project's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: ProjectDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_2:
    description: Updates an existing project.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: ProjectDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the template project's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the template project's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: ProjectDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_3:
    description: Deletes an existing Project.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the template project's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the template project's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.template_project import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
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

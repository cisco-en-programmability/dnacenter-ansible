#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
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
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name of project to be searched.
    - ProjectDTO's name.
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
    - Required for state delete.
    type: str

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
- name: get_projects
  cisco.dnac.template_project:
    state: query  # required
    name: SomeValue  # string
  register: query_result
  
- name: create_project
  cisco.dnac.template_project:
    state: create  # required
    createTime: 1  #  integer
    description: SomeValue  # string
    id: SomeValue  # string
    lastUpdateTime: 1  #  integer
    name: SomeValue  # string
    tags:
    - SomeValue  # string
    templates: None
  
- name: update_project
  cisco.dnac.template_project:
    state: update  # required
    createTime: 1  #  integer
    description: SomeValue  # string
    id: SomeValue  # string
    lastUpdateTime: 1  #  integer
    name: SomeValue  # string
    tags:
    - SomeValue  # string
    templates: None
  
- name: delete_project
  cisco.dnac.template_project:
    state: delete  # required
    project_id: SomeValue  # string, required
  
"""

RETURN = """
get_projects:
    description: Returns the projects in the system.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the template project's payload.
      returned: always
      type: list
      contains:
        name:
          description: It is the template project's name.
          returned: always
          type: str
          sample: '<name>'
        id:
          description: It is the template project's id.
          returned: always
          type: str
          sample: '478012'
        templates:
          description: It is the template project's templates.
          returned: always
          type: list
          contains:
            name:
              description: It is the template project's name.
              returned: always
              type: str
              sample: '<name>'
            composite:
              description: It is the template project's composite.
              returned: always
              type: bool
              sample: false
            id:
              description: It is the template project's id.
              returned: always
              type: str
              sample: '478012'



create_project:
    description: Creates a new project.
    returned: success
    type: dict
    contains:
    response:
      description: ProjectDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the template project's taskId.
          returned: success
          type: dict
        url:
          description: It is the template project's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: ProjectDTO's version.
      returned: success
      type: str
      sample: '1.0'

update_project:
    description: Updates an existing project.
    returned: changed
    type: dict
    contains:
    response:
      description: ProjectDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the template project's taskId.
          returned: changed
          type: dict
        url:
          description: It is the template project's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: ProjectDTO's version.
      returned: changed
      type: str
      sample: '1.0'

delete_project:
    description: Deletes an existing Project.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the template project's taskId.
          returned: success
          type: dict
        url:
          description: It is the template project's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

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
  register: nm_get_projects

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

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: configuration_templates.create_project
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

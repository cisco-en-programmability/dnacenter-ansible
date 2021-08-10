#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_project
short_description: Resource module for Configuration Template Project
description:
- Manage operations create, update and delete of the resource Configuration Template Project.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  createTime:
    description: Create time of project.
    type: int
  description:
    description: Description of project.
    type: str
  id:
    description: UUID of project.
    type: str
  lastUpdateTime:
    description: Update time of project.
    type: int
  name:
    description: Name of project.
    type: str
  projectId:
    description: ProjectId path parameter. ProjectId(UUID) of project to be deleted.
    type: str
  tags:
    description: Configuration Template Project's tags.
    suboptions:
      id:
        description: UUID of tag.
        type: str
      name:
        description: Name of tag.
        type: str
    type: list
  templates:
    description: List of templates within the project.
    type: dict
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template Project reference
  description: Complete reference of the Configuration Template Project object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.configuration_template_project:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    createTime: 0
    description: string
    id: string
    lastUpdateTime: 0
    name: string
    tags:
    - id: string
      name: string
    templates: {}

- name: Update all
  cisco.dnac.configuration_template_project:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    createTime: 0
    description: string
    id: string
    lastUpdateTime: 0
    name: string
    tags:
    - id: string
      name: string
    templates: {}

- name: Delete by id
  cisco.dnac.configuration_template_project:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    projectId: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

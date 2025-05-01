#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: configuration_template_project
short_description: Resource module for Configuration Template Project
description:
  - This module represents an alias of the module configuration_template_project_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
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
    elements: dict
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
    elements: dict
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates CreateProjectV1
    description: Complete reference of the CreateProjectV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-project
  - name: Cisco DNA Center documentation for Configuration Templates DeletesTheProjectV1
    description: Complete reference of the DeletesTheProjectV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-the-project
  - name: Cisco DNA Center documentation for Configuration Templates UpdateProjectV1
    description: Complete reference of the UpdateProjectV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-project
notes:
  - SDK Method used are configuration_templates.ConfigurationTemplates.create_project_v1,
    configuration_templates.ConfigurationTemplates.deletes_the_project_v1, configuration_templates.ConfigurationTemplates.update_project_v1,
  - Paths used are post /dna/intent/api/v1/template-programmer/project, delete /dna/intent/api/v1/template-programmer/project/{projectId},
    put /dna/intent/api/v1/template-programmer/project,
  - It should be noted that this module is an alias of configuration_template_project_v1
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
    templates:
      - {}
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

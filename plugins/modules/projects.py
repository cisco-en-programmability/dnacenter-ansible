#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: projects
short_description: Resource module for Projects
description:
  - Manage operations create, update and delete of the resource Projects.
  - Create a template project.
  - Delete a template project by the project's ID.
  - Update a template project by the project's ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of the project.
    type: str
  name:
    description: Name of the project.
    type: str
  projectId:
    description: ProjectId path parameter. The id of the project to delete, retrieveable from `GET /dna/intent/api/v1/projects`.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates CreateTemplateProject
    description: Complete reference of the CreateTemplateProject API.
    link: https://developer.cisco.com/docs/dna-center/#!create-template-project
  - name: Cisco DNA Center documentation for Configuration Templates DeleteTemplateProject
    description: Complete reference of the DeleteTemplateProject API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-template-project
  - name: Cisco DNA Center documentation for Configuration Templates UpdateTemplateProject
    description: Complete reference of the UpdateTemplateProject API.
    link: https://developer.cisco.com/docs/dna-center/#!update-template-project
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_template_project,
    configuration_templates.ConfigurationTemplates.delete_template_project,
    configuration_templates.ConfigurationTemplates.update_template_project,
  - Paths used are
    post /dna/intent/api/v1/projects,
    delete /dna/intent/api/v1/projects/{projectId},
    put /dna/intent/api/v1/projects/{projectId},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.projects:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    name: string
- name: Delete by id
  cisco.dnac.projects:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    projectId: string
- name: Update by id
  cisco.dnac.projects:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    name: string
    projectId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""

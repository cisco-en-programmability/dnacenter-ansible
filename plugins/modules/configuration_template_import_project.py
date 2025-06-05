#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: configuration_template_import_project
short_description: Resource module for Configuration Template Import Project
description:
  - This module represents an alias of the module configuration_template_import_project_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  doVersion:
    description: DoVersion query parameter. If this flag is true then it creates a
      new version of the template with the imported contents in case if the templates
      already exists. " If this flag is false and if template already exists, then
      operation fails with 'Template already exists' error.
    type: bool
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates ImportsTheProjectsProvidedV1
    description: Complete reference of the ImportsTheProjectsProvidedV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!imports-the-projects-provided
notes:
  - SDK Method used are configuration_templates.ConfigurationTemplates.imports_the_projects_provided_v1,
  - Paths used are post /dna/intent/api/v1/template-programmer/project/importprojects,
  - It should be noted that this module is an alias of configuration_template_import_project_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.configuration_template_import_project:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    doVersion: true
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

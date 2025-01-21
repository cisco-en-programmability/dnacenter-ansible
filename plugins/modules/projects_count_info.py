#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: projects_count_info
short_description: Information module for Projects Count Info
description:
- This module represents an alias of the module projects_count_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
    - Name query parameter. Name of project to be searched.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Templates GetTemplateProjectCountV1
  description: Complete reference of the GetTemplateProjectCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-template-project-count
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.get_template_project_count_v1,

  - Paths used are
    get /dna/intent/api/v1/projects/count,
  - It should be noted that this module is an alias of projects_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Projects Count Info
  cisco.dnac.projects_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
  register: result

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

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: templates_template_id_versions_commit
short_description: Resource module for Templates Template Id Versions Commit
description:
- This module represents an alias of the module templates_template_id_versions_commit_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  commitNote:
    description: A message to leave as a note with the commit of a template. The maximum
      length allowed is 255 characters.
    type: str
  templateId:
    description: TemplateId path parameter. The id of the template to commit a new version
      for, retrieveable from `GET /dna/intent/api/v1/templates`.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Templates CommitTemplateForANewVersionV1
  description: Complete reference of the CommitTemplateForANewVersionV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!commit-template-for-a-new-version
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.commit_template_for_a_new_version_v1,

  - Paths used are
    post /dna/intent/api/v1/templates/{templateId}/versions/commit,
  - It should be noted that this module is an alias of templates_template_id_versions_commit_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.templates_template_id_versions_commit:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    commitNote: string
    templateId: string

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
        "url": "string",
        "taskId": "string"
      }
    }
"""

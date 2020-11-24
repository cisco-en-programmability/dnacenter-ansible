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
module: template_preview
short_description: Manage TemplatePreview objects of ConfigurationTemplates
description:
- Previews an existing template.
version_added: '1.0'
author: first last (@GitHubID)
options:
  params:
    description:
    - TemplatePreviewRequestDTO's params.
    type: dict
  templateId:
    description:
    - TemplatePreviewRequestDTO's templateId.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template_preview
# Reference by Internet resource
- name: TemplatePreview reference
  description: Complete reference of the TemplatePreview object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TemplatePreview reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: preview_template
  cisco.dnac.template_preview
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: update  # required
    params:
    templateId: SomeValue  # string
  delegate_to: localhost
  
"""

RETURN = """
preview_template:
    description: Previews an existing template.
    returned: changed
    type: dict
    contains:
    cliPreview:
      description: TemplatePreviewRequestDTO's cliPreview.
      returned: changed
      type: str
      sample: '<clipreview>'
    templateId:
      description: TemplatePreviewRequestDTO's templateId.
      returned: changed
      type: str
      sample: '<templateid>'
    validationErrors:
      description: TemplatePreviewRequestDTO's validationErrors.
      returned: changed
      type: dict

"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: template_preview
short_description: Manage TemplatePreview objects of ConfigurationTemplates
description:
- Previews an existing template.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
  cisco.dnac.template_preview:
    state: update  # required
    params:
    templateId: SomeValue  # string

"""

RETURN = """
"""

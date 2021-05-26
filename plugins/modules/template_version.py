#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: template_version
short_description: Manage TemplateVersion objects of ConfigurationTemplates
description:
- Creates Versioning for the current contents of the template.
- Returns the versions of a specified template.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  comments:
    description:
    - TemplateVersionRequestDTO's comments.
    type: str
  templateId:
    description:
    - TemplateVersionRequestDTO's templateId.
    type: str
  template_id:
    description:
    - TemplateId path parameter.
    - Required for state query.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template_version
# Reference by Internet resource
- name: TemplateVersion reference
  description: Complete reference of the TemplateVersion object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TemplateVersion reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: version_template
  cisco.dnac.template_version:
    state: create  # required
    comments: SomeValue  # string
    templateId: SomeValue  # string

- name: get_template_versions
  cisco.dnac.template_version:
    state: query  # required
    template_id: SomeValue  # string, required
  register: nm_get_template_versions

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
  sample: configuration_templates.get_template_versions
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: template_deploy
short_description: Manage TemplateDeploy objects of ConfigurationTemplates
description:
- Deploys a template.
- Returns the status of a deployed template.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  forcePushTemplate:
    description:
    - TemplateDeploymentInfo's forcePushTemplate.
    type: bool
  isComposite:
    description:
    - TemplateDeploymentInfo's isComposite.
    type: bool
  mainTemplateId:
    description:
    - TemplateDeploymentInfo's mainTemplateId.
    type: str
  memberTemplateDeploymentInfo:
    description:
    - TemplateDeploymentInfo's memberTemplateDeploymentInfo (list of any objects).
    type: list
  targetInfo:
    description:
    - TemplateDeploymentInfo's targetInfo (list of objects).
    type: list
    elements: dict
    suboptions:
      hostName:
        description:
        - It is the template deploy's hostName.
        type: str
      id:
        description:
        - It is the template deploy's id.
        type: str
      params:
        description:
        - It is the template deploy's params.
        type: dict
      type:
        description:
        - It is the template deploy's type.
        type: str

  templateId:
    description:
    - TemplateDeploymentInfo's templateId.
    type: str
  deployment_id:
    description:
    - DeploymentId path parameter.
    - Required for state query.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template_deploy
# Reference by Internet resource
- name: TemplateDeploy reference
  description: Complete reference of the TemplateDeploy object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TemplateDeploy reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: deploy_template
  cisco.dnac.template_deploy:
    state: create  # required
    forcePushTemplate: True  # boolean
    isComposite: True  # boolean
    mainTemplateId: SomeValue  # string
    memberTemplateDeploymentInfo: None
    targetInfo:
    - hostName: SomeValue  # string
      id: SomeValue  # string
      params:
      type: SomeValue  # string
    templateId: SomeValue  # string

- name: get_template_deployment_status
  cisco.dnac.template_deploy:
    state: query  # required
    deployment_id: SomeValue  # string, required
  register: nm_get_template_deployment_status

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
  sample: configuration_templates.deploy_template
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

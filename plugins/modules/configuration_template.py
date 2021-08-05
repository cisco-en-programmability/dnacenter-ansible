#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template
short_description: Resource module for Configuration Template
description:
- Manage operations update and delete of the resource Configuration Template.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  author:
    description: Configuration Template's author.
    type: str
  composite:
    description: Composite flag.
    type: bool
  containingTemplates:
    description: Configuration Template's containingTemplates.
    suboptions:
      composite:
        description: Composite flag.
        type: bool
      id:
        description: Configuration Template's id.
        type: str
      name:
        description: Configuration Template's name.
        type: str
      version:
        description: Configuration Template's version.
        type: str
    type: list
  createTime:
    description: Configuration Template's createTime.
    type: int
  description:
    description: Configuration Template's description.
    type: str
  deviceTypes:
    description: Configuration Template's deviceTypes.
    suboptions:
      productFamily:
        description: Configuration Template's productFamily.
        type: str
      productSeries:
        description: Configuration Template's productSeries.
        type: str
      productType:
        description: Configuration Template's productType.
        type: str
    type: list
  failurePolicy:
    description: Configuration Template's failurePolicy.
    type: str
  id:
    description: Configuration Template's id.
    type: str
  lastUpdateTime:
    description: Configuration Template's lastUpdateTime.
    type: int
  name:
    description: Configuration Template's name.
    type: str
  parentTemplateId:
    description: Configuration Template's parentTemplateId.
    type: str
  projectId:
    description: Configuration Template's projectId.
    type: str
  projectName:
    description: Configuration Template's projectName.
    type: str
  rollbackTemplateContent:
    description: Configuration Template's rollbackTemplateContent.
    type: str
  rollbackTemplateParams:
    description: Configuration Template's rollbackTemplateParams.
    suboptions:
      binding:
        description: Configuration Template's binding.
        type: str
      dataType:
        description: Configuration Template's dataType.
        type: str
      defaultValue:
        description: Configuration Template's defaultValue.
        type: str
      description:
        description: Configuration Template's description.
        type: str
      displayName:
        description: Configuration Template's displayName.
        type: str
      group:
        description: Configuration Template's group.
        type: str
      id:
        description: Configuration Template's id.
        type: str
      instructionText:
        description: Configuration Template's instructionText.
        type: str
      key:
        description: Configuration Template's key.
        type: str
      notParam:
        description: NotParam flag.
        type: bool
      order:
        description: Configuration Template's order.
        type: int
      paramArray:
        description: ParamArray flag.
        type: bool
      parameterName:
        description: Configuration Template's parameterName.
        type: str
      provider:
        description: Configuration Template's provider.
        type: str
      range:
        description: Configuration Template's range.
        suboptions:
          id:
            description: Configuration Template's id.
            type: str
          maxValue:
            description: Configuration Template's maxValue.
            type: int
          minValue:
            description: Configuration Template's minValue.
            type: int
        type: list
      required:
        description: Required flag.
        type: bool
      selection:
        description: Configuration Template's selection.
        suboptions:
          id:
            description: Configuration Template's id.
            type: str
          selectionType:
            description: Configuration Template's selectionType.
            type: str
          selectionValues:
            description: Configuration Template's selectionValues.
            type: dict
        type: dict
    type: list
  softwareType:
    description: Configuration Template's softwareType.
    type: str
  softwareVariant:
    description: Configuration Template's softwareVariant.
    type: str
  softwareVersion:
    description: Configuration Template's softwareVersion.
    type: str
  tags:
    description: Configuration Template's tags.
    elements: str
    type: list
  templateContent:
    description: Configuration Template's templateContent.
    type: str
  templateId:
    description: TemplateId path parameter.
    type: str
  templateParams:
    description: Configuration Template's templateParams.
    suboptions:
      binding:
        description: Configuration Template's binding.
        type: str
      dataType:
        description: Configuration Template's dataType.
        type: str
      defaultValue:
        description: Configuration Template's defaultValue.
        type: str
      description:
        description: Configuration Template's description.
        type: str
      displayName:
        description: Configuration Template's displayName.
        type: str
      group:
        description: Configuration Template's group.
        type: str
      id:
        description: Configuration Template's id.
        type: str
      instructionText:
        description: Configuration Template's instructionText.
        type: str
      key:
        description: Configuration Template's key.
        type: str
      notParam:
        description: NotParam flag.
        type: bool
      order:
        description: Configuration Template's order.
        type: int
      paramArray:
        description: ParamArray flag.
        type: bool
      parameterName:
        description: Configuration Template's parameterName.
        type: str
      provider:
        description: Configuration Template's provider.
        type: str
      range:
        description: Configuration Template's range.
        suboptions:
          id:
            description: Configuration Template's id.
            type: str
          maxValue:
            description: Configuration Template's maxValue.
            type: int
          minValue:
            description: Configuration Template's minValue.
            type: int
        type: list
      required:
        description: Required flag.
        type: bool
      selection:
        description: Configuration Template's selection.
        suboptions:
          id:
            description: Configuration Template's id.
            type: str
          selectionType:
            description: Configuration Template's selectionType.
            type: str
          selectionValues:
            description: Configuration Template's selectionValues.
            type: dict
        type: dict
    type: list
  version:
    description: Configuration Template's version.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template reference
  description: Complete reference of the Configuration Template object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.configuration_template:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    author: string
    composite: true
    containingTemplates:
    - composite: true
      id: string
      name: string
      version: string
    createTime: 0
    description: string
    deviceTypes:
    - productFamily: string
      productSeries: string
      productType: string
    failurePolicy: string
    id: string
    lastUpdateTime: 0
    name: string
    parentTemplateId: string
    projectId: string
    projectName: string
    rollbackTemplateContent: string
    rollbackTemplateParams:
    - binding: string
      dataType: string
      defaultValue: string
      description: string
      displayName: string
      group: string
      id: string
      instructionText: string
      key: string
      notParam: true
      order: 0
      paramArray: true
      parameterName: string
      provider: string
      range:
      - id: string
        maxValue: 0
        minValue: 0
      required: true
      selection:
        id: string
        selectionType: string
        selectionValues: {}
    softwareType: string
    softwareVariant: string
    softwareVersion: string
    tags:
    - string
    templateContent: string
    templateParams:
    - binding: string
      dataType: string
      defaultValue: string
      description: string
      displayName: string
      group: string
      id: string
      instructionText: string
      key: string
      notParam: true
      order: 0
      paramArray: true
      parameterName: string
      provider: string
      range:
      - id: string
        maxValue: 0
        minValue: 0
      required: true
      selection:
        id: string
        selectionType: string
        selectionValues: {}
    version: string

- name: Delete by id
  cisco.dnac.configuration_template:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    templateId: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": {},
        "url": "string"
      },
      "version": "string"
    }
"""

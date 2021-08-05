#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_create
short_description: Resource module for Configuration Template Create
description:
- Manage operation create of the resource Configuration Template Create.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  author:
    description: Configuration Template Create's author.
    type: str
  composite:
    description: Composite flag.
    type: bool
  containingTemplates:
    description: Configuration Template Create's containingTemplates.
    suboptions:
      composite:
        description: Composite flag.
        type: bool
      id:
        description: Configuration Template Create's id.
        type: str
      name:
        description: Configuration Template Create's name.
        type: str
      version:
        description: Configuration Template Create's version.
        type: str
    type: list
  createTime:
    description: Configuration Template Create's createTime.
    type: int
  description:
    description: Configuration Template Create's description.
    type: str
  deviceTypes:
    description: Configuration Template Create's deviceTypes.
    suboptions:
      productFamily:
        description: Configuration Template Create's productFamily.
        type: str
      productSeries:
        description: Configuration Template Create's productSeries.
        type: str
      productType:
        description: Configuration Template Create's productType.
        type: str
    type: list
  failurePolicy:
    description: Configuration Template Create's failurePolicy.
    type: str
  id:
    description: Configuration Template Create's id.
    type: str
  lastUpdateTime:
    description: Configuration Template Create's lastUpdateTime.
    type: int
  name:
    description: Configuration Template Create's name.
    type: str
  parentTemplateId:
    description: Configuration Template Create's parentTemplateId.
    type: str
  projectId:
    description: Configuration Template Create's projectId.
    type: str
  projectName:
    description: Configuration Template Create's projectName.
    type: str
  rollbackTemplateContent:
    description: Configuration Template Create's rollbackTemplateContent.
    type: str
  rollbackTemplateParams:
    description: Configuration Template Create's rollbackTemplateParams.
    suboptions:
      binding:
        description: Configuration Template Create's binding.
        type: str
      dataType:
        description: Configuration Template Create's dataType.
        type: str
      defaultValue:
        description: Configuration Template Create's defaultValue.
        type: str
      description:
        description: Configuration Template Create's description.
        type: str
      displayName:
        description: Configuration Template Create's displayName.
        type: str
      group:
        description: Configuration Template Create's group.
        type: str
      id:
        description: Configuration Template Create's id.
        type: str
      instructionText:
        description: Configuration Template Create's instructionText.
        type: str
      key:
        description: Configuration Template Create's key.
        type: str
      notParam:
        description: NotParam flag.
        type: bool
      order:
        description: Configuration Template Create's order.
        type: int
      paramArray:
        description: ParamArray flag.
        type: bool
      parameterName:
        description: Configuration Template Create's parameterName.
        type: str
      provider:
        description: Configuration Template Create's provider.
        type: str
      range:
        description: Configuration Template Create's range.
        suboptions:
          id:
            description: Configuration Template Create's id.
            type: str
          maxValue:
            description: Configuration Template Create's maxValue.
            type: int
          minValue:
            description: Configuration Template Create's minValue.
            type: int
        type: list
      required:
        description: Required flag.
        type: bool
      selection:
        description: Configuration Template Create's selection.
        suboptions:
          id:
            description: Configuration Template Create's id.
            type: str
          selectionType:
            description: Configuration Template Create's selectionType.
            type: str
          selectionValues:
            description: Configuration Template Create's selectionValues.
            type: dict
        type: dict
    type: list
  softwareType:
    description: Configuration Template Create's softwareType.
    type: str
  softwareVariant:
    description: Configuration Template Create's softwareVariant.
    type: str
  softwareVersion:
    description: Configuration Template Create's softwareVersion.
    type: str
  tags:
    description: Configuration Template Create's tags.
    elements: str
    type: list
  templateContent:
    description: Configuration Template Create's templateContent.
    type: str
  templateParams:
    description: Configuration Template Create's templateParams.
    suboptions:
      binding:
        description: Configuration Template Create's binding.
        type: str
      dataType:
        description: Configuration Template Create's dataType.
        type: str
      defaultValue:
        description: Configuration Template Create's defaultValue.
        type: str
      description:
        description: Configuration Template Create's description.
        type: str
      displayName:
        description: Configuration Template Create's displayName.
        type: str
      group:
        description: Configuration Template Create's group.
        type: str
      id:
        description: Configuration Template Create's id.
        type: str
      instructionText:
        description: Configuration Template Create's instructionText.
        type: str
      key:
        description: Configuration Template Create's key.
        type: str
      notParam:
        description: NotParam flag.
        type: bool
      order:
        description: Configuration Template Create's order.
        type: int
      paramArray:
        description: ParamArray flag.
        type: bool
      parameterName:
        description: Configuration Template Create's parameterName.
        type: str
      provider:
        description: Configuration Template Create's provider.
        type: str
      range:
        description: Configuration Template Create's range.
        suboptions:
          id:
            description: Configuration Template Create's id.
            type: str
          maxValue:
            description: Configuration Template Create's maxValue.
            type: int
          minValue:
            description: Configuration Template Create's minValue.
            type: int
        type: list
      required:
        description: Required flag.
        type: bool
      selection:
        description: Configuration Template Create's selection.
        suboptions:
          id:
            description: Configuration Template Create's id.
            type: str
          selectionType:
            description: Configuration Template Create's selectionType.
            type: str
          selectionValues:
            description: Configuration Template Create's selectionValues.
            type: dict
        type: dict
    type: list
  version:
    description: Configuration Template Create's version.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template Create reference
  description: Complete reference of the Configuration Template Create object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.configuration_template_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
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

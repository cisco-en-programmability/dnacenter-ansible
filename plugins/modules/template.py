#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: template
short_description: Manage Template objects of ConfigurationTemplates
description:
- Creates a new Template.
- List the Templates available.
- Updates an existing Template.
- Returns details of the specified Template.
- Deletes an existing Template.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  project_id:
    description:
    - ProjectId path parameter.
    - ProjectId query parameter.
    - Required for state create.
    type: str
    required: True
  author:
    description:
    - TemplateDTO's author.
    type: str
  composite:
    description:
    - TemplateDTO's composite.
    type: bool
  containingTemplates:
    description:
    - TemplateDTO's containingTemplates (list of objects).
    type: list
    elements: dict
    suboptions:
      composite:
        description:
        - It is the Template's composite.
        type: bool
      id:
        description:
        - It is the Template's id.
        type: str
      name:
        description:
        - It is the Template's name.
        type: str
      version:
        description:
        - It is the Template's version.
        type: str

  createTime:
    description:
    - TemplateDTO's createTime.
    type: int
  description:
    description:
    - TemplateDTO's description.
    type: str
  deviceTypes:
    description:
    - TemplateDTO's deviceTypes (list of objects).
    type: list
    elements: dict
    suboptions:
      productFamily:
        description:
        - It is the Template's productFamily.
        type: str
      productSeries:
        description:
        - It is the Template's productSeries.
        type: str
      productType:
        description:
        - It is the Template's productType.
        type: str

  failurePolicy:
    description:
    - TemplateDTO's failurePolicy.
    type: str
  id:
    description:
    - TemplateDTO's id.
    type: str
  lastUpdateTime:
    description:
    - TemplateDTO's lastUpdateTime.
    type: int
  name:
    description:
    - TemplateDTO's name.
    type: str
  parentTemplateId:
    description:
    - TemplateDTO's parentTemplateId.
    type: str
  projectId:
    description:
    - TemplateDTO's projectId.
    type: str
  projectName:
    description:
    - TemplateDTO's projectName.
    type: str
  rollbackTemplateContent:
    description:
    - TemplateDTO's rollbackTemplateContent.
    type: str
  rollbackTemplateParams:
    description:
    - TemplateDTO's rollbackTemplateParams (list of objects).
    type: list
    elements: dict
    suboptions:
      binding:
        description:
        - It is the Template's binding.
        type: str
      dataType:
        description:
        - It is the Template's dataType.
        type: str
      defaultValue:
        description:
        - It is the Template's defaultValue.
        type: str
      description:
        description:
        - It is the Template's description.
        type: str
      displayName:
        description:
        - It is the Template's displayName.
        type: str
      group:
        description:
        - It is the Template's group.
        type: str
      id:
        description:
        - It is the Template's id.
        type: str
      instructionText:
        description:
        - It is the Template's instructionText.
        type: str
      key:
        description:
        - It is the Template's key.
        type: str
      notParam:
        description:
        - It is the Template's notParam.
        type: bool
      order:
        description:
        - It is the Template's order.
        type: int
      paramArray:
        description:
        - It is the Template's paramArray.
        type: bool
      parameterName:
        description:
        - It is the Template's parameterName.
        type: str
      provider:
        description:
        - It is the Template's provider.
        type: str
      range:
        description:
        - It is the Template's range.
        type: list
        elements: dict
        suboptions:
          id:
            description:
            - It is the Template's id.
            type: str
          maxValue:
            description:
            - It is the Template's maxValue.
            type: int
          minValue:
            description:
            - It is the Template's minValue.
            type: int

      required:
        description:
        - It is the Template's required.
        type: bool
      selection:
        description:
        - It is the Template's selection.
        type: dict
        suboptions:
          id:
            description:
            - It is the Template's id.
            type: str
          selectionType:
            description:
            - It is the Template's selectionType.
            type: str
          selectionValues:
            description:
            - It is the Template's selectionValues.
            type: dict


  softwareType:
    description:
    - TemplateDTO's softwareType.
    type: str
  softwareVariant:
    description:
    - TemplateDTO's softwareVariant.
    type: str
  softwareVersion:
    description:
    - TemplateDTO's softwareVersion.
    type: str
  tags:
    description:
    - TemplateDTO's tags (list of strings).
    type: list
  templateContent:
    description:
    - TemplateDTO's TemplateContent.
    type: str
  templateParams:
    description:
    - TemplateDTO's TemplateParams (list of objects).
    type: list
    elements: dict
    suboptions:
      binding:
        description:
        - It is the Template's binding.
        type: str
      dataType:
        description:
        - It is the Template's dataType.
        type: str
      defaultValue:
        description:
        - It is the Template's defaultValue.
        type: str
      description:
        description:
        - It is the Template's description.
        type: str
      displayName:
        description:
        - It is the Template's displayName.
        type: str
      group:
        description:
        - It is the Template's group.
        type: str
      id:
        description:
        - It is the Template's id.
        type: str
      instructionText:
        description:
        - It is the Template's instructionText.
        type: str
      key:
        description:
        - It is the Template's key.
        type: str
      notParam:
        description:
        - It is the Template's notParam.
        type: bool
      order:
        description:
        - It is the Template's order.
        type: int
      paramArray:
        description:
        - It is the Template's paramArray.
        type: bool
      parameterName:
        description:
        - It is the Template's parameterName.
        type: str
      provider:
        description:
        - It is the Template's provider.
        type: str
      range:
        description:
        - It is the Template's range.
        type: list
        elements: dict
        suboptions:
          id:
            description:
            - It is the Template's id.
            type: str
          maxValue:
            description:
            - It is the Template's maxValue.
            type: int
          minValue:
            description:
            - It is the Template's minValue.
            type: int

      required:
        description:
        - It is the Template's required.
        type: bool
      selection:
        description:
        - It is the Template's selection.
        type: dict
        suboptions:
          id:
            description:
            - It is the Template's id.
            type: str
          selectionType:
            description:
            - It is the Template's selectionType.
            type: str
          selectionValues:
            description:
            - It is the Template's selectionValues.
            type: dict


  version:
    description:
    - TemplateDTO's version.
    type: str
  filter_conflicting_templates:
    description:
    - FilterConflictingTemplates query parameter.
    type: bool
  product_family:
    description:
    - ProductFamily query parameter.
    type: str
  product_series:
    description:
    - ProductSeries query parameter.
    type: str
  product_type:
    description:
    - ProductType query parameter.
    type: str
  software_type:
    description:
    - SoftwareType query parameter.
    type: str
  software_version:
    description:
    - SoftwareVersion query parameter.
    type: str
  template_id:
    description:
    - TemplateId path parameter.
    type: str
    required: True
  latest_version:
    description:
    - LatestVersion query parameter.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template
# Reference by Internet resource
- name: Template reference
  description: Complete reference of the Template object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Template reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_template
  cisco.dnac.template:
    state: create  # required
    project_id: SomeValue  # string, required
    author: SomeValue  # string
    composite: True  # boolean
    containingTemplates:
    - composite: True  # boolean
      id: SomeValue  # string
      name: SomeValue  # string
      version: SomeValue  # string
    createTime: 1  #  integer
    description: SomeValue  # string
    deviceTypes:
    - productFamily: SomeValue  # string
      productSeries: SomeValue  # string
      productType: SomeValue  # string
    failurePolicy: # valid values are 'ABORT_ON_ERROR',
      # 'CONTINUE_ON_ERROR',
      # 'ROLLBACK_ON_ERROR',
      # 'ROLLBACK_TARGET_ON_ERROR',
      # 'ABORT_TARGET_ON_ERROR'.
      SomeValue  # string
    id: SomeValue  # string
    lastUpdateTime: 1  #  integer
    name: SomeValue  # string
    parentTemplateId: SomeValue  # string
    projectId: SomeValue  # string
    projectName: SomeValue  # string
    rollbackTemplateContent: SomeValue  # string
    rollbackTemplateParams:
    - binding: SomeValue  # string
      dataType: SomeValue  # string
      defaultValue: SomeValue  # string
      description: SomeValue  # string
      displayName: SomeValue  # string
      group: SomeValue  # string
      id: SomeValue  # string
      instructionText: SomeValue  # string
      key: SomeValue  # string
      notParam: True  # boolean
      order: 1  #  integer
      paramArray: True  # boolean
      parameterName: SomeValue  # string
      provider: SomeValue  # string
      range:
      - id: SomeValue  # string
        maxValue: 1  #  integer
        minValue: 1  #  integer
      required: True  # boolean
      selection:
        id: SomeValue  # string
        selectionType: SomeValue  # string
        selectionValues:
    softwareType: SomeValue  # string
    softwareVariant: SomeValue  # string
    softwareVersion: SomeValue  # string
    tags:
    - SomeValue  # string
    templateContent: SomeValue  # string
    templateParams:
    - binding: SomeValue  # string
      dataType: SomeValue  # string
      defaultValue: SomeValue  # string
      description: SomeValue  # string
      displayName: SomeValue  # string
      group: SomeValue  # string
      id: SomeValue  # string
      instructionText: SomeValue  # string
      key: SomeValue  # string
      notParam: True  # boolean
      order: 1  #  integer
      paramArray: True  # boolean
      parameterName: SomeValue  # string
      provider: SomeValue  # string
      range:
      - id: SomeValue  # string
        maxValue: 1  #  integer
        minValue: 1  #  integer
      required: True  # boolean
      selection:
        id: SomeValue  # string
        selectionType: SomeValue  # string
        selectionValues:
    version: SomeValue  # string

- name: gets_the_templates_available
  cisco.dnac.template:
    state: query  # required
    filter_conflicting_templates: True  # boolean
    product_family: SomeValue  # string
    product_series: SomeValue  # string
    product_type: SomeValue  # string
    project_id: SomeValue  # string
    software_type: SomeValue  # string
    software_version: SomeValue  # string
  register: nm_gets_the_templates_available

- name: update_template
  cisco.dnac.template:
    state: update  # required
    author: SomeValue  # string
    composite: True  # boolean
    containingTemplates:
    - composite: True  # boolean
      id: SomeValue  # string
      name: SomeValue  # string
      version: SomeValue  # string
    createTime: 1  #  integer
    description: SomeValue  # string
    deviceTypes:
    - productFamily: SomeValue  # string
      productSeries: SomeValue  # string
      productType: SomeValue  # string
    failurePolicy: # valid values are 'ABORT_ON_ERROR',
      # 'CONTINUE_ON_ERROR',
      # 'ROLLBACK_ON_ERROR',
      # 'ROLLBACK_TARGET_ON_ERROR',
      # 'ABORT_TARGET_ON_ERROR'.
      SomeValue  # string
    id: SomeValue  # string
    lastUpdateTime: 1  #  integer
    name: SomeValue  # string
    parentTemplateId: SomeValue  # string
    projectId: SomeValue  # string
    projectName: SomeValue  # string
    rollbackTemplateContent: SomeValue  # string
    rollbackTemplateParams:
    - binding: SomeValue  # string
      dataType: SomeValue  # string
      defaultValue: SomeValue  # string
      description: SomeValue  # string
      displayName: SomeValue  # string
      group: SomeValue  # string
      id: SomeValue  # string
      instructionText: SomeValue  # string
      key: SomeValue  # string
      notParam: True  # boolean
      order: 1  #  integer
      paramArray: True  # boolean
      parameterName: SomeValue  # string
      provider: SomeValue  # string
      range:
      - id: SomeValue  # string
        maxValue: 1  #  integer
        minValue: 1  #  integer
      required: True  # boolean
      selection:
        id: SomeValue  # string
        selectionType: SomeValue  # string
        selectionValues:
    softwareType: SomeValue  # string
    softwareVariant: SomeValue  # string
    softwareVersion: SomeValue  # string
    tags:
    - SomeValue  # string
    templateContent: SomeValue  # string
    templateParams:
    - binding: SomeValue  # string
      dataType: SomeValue  # string
      defaultValue: SomeValue  # string
      description: SomeValue  # string
      displayName: SomeValue  # string
      group: SomeValue  # string
      id: SomeValue  # string
      instructionText: SomeValue  # string
      key: SomeValue  # string
      notParam: True  # boolean
      order: 1  #  integer
      paramArray: True  # boolean
      parameterName: SomeValue  # string
      provider: SomeValue  # string
      range:
      - id: SomeValue  # string
        maxValue: 1  #  integer
        minValue: 1  #  integer
      required: True  # boolean
      selection:
        id: SomeValue  # string
        selectionType: SomeValue  # string
        selectionValues:
    version: SomeValue  # string

- name: get_template_details
  cisco.dnac.template:
    state: query  # required
    template_id: SomeValue  # string, required
    latest_version: True  # boolean
  register: nm_get_template_details

- name: delete_template
  cisco.dnac.template:
    state: delete  # required
    template_id: SomeValue  # string, required

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
  sample: configuration_templates.create_template
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

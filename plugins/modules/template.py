#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

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
version_added: '1.0'
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
    failurePolicy: SomeValue  # string, valid values: 'ABORT_ON_ERROR', 'CONTINUE_ON_ERROR', 'ROLLBACK_ON_ERROR', 'ROLLBACK_TARGET_ON_ERROR', 'ABORT_TARGET_ON_ERROR'.
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
  register: query_result
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
    failurePolicy: SomeValue  # string, valid values: 'ABORT_ON_ERROR', 'CONTINUE_ON_ERROR', 'ROLLBACK_ON_ERROR', 'ROLLBACK_TARGET_ON_ERROR', 'ABORT_TARGET_ON_ERROR'.
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
  register: query_result
  - name: delete_template
  cisco.dnac.template:
    state: delete  # required
    template_id: SomeValue  # string, required
  """

RETURN = """
create_template:
    description: Creates a new Template.
    returned: success
    type: dict
    contains:
    response:
      description: TemplateDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Template's taskId.
          returned: success
          type: dict
        url:
          description: It is the Template's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: TemplateDTO's version.
      returned: success
      type: str
      sample: '1.0'

gets_the_templates_available:
    description: List the Templates available.
    returned: always
    type: dict
    contains:

update_template:
    description: Updates an existing Template.
    returned: changed
    type: dict
    contains:
    response:
      description: TemplateDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the Template's taskId.
          returned: changed
          type: dict
        url:
          description: It is the Template's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: TemplateDTO's version.
      returned: changed
      type: str
      sample: '1.0'

get_template_details:
    description: Returns details of the specified Template.
    returned: always
    type: dict
    contains:
    author:
      description: Author, property of the response body.
      returned: always
      type: str
      sample: '<author>'
    composite:
      description: Composite, property of the response body.
      returned: always
      type: bool
      sample: false
    containingTemplates:
      description: ContainingTemplates, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        composite:
          description: It is the Template's composite.
          returned: always
          type: bool
          sample: false
        id:
          description: It is the Template's id.
          returned: always
          type: str
          sample: '478012'
        name:
          description: It is the Template's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the Template's version.
          returned: always
          type: str
          sample: '1.0'

    createTime:
      description: CreateTime, property of the response body.
      returned: always
      type: int
      sample: 0
    description:
      description: Description, property of the response body.
      returned: always
      type: str
      sample: '<description>'
    deviceTypes:
      description: DeviceTypes, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        productFamily:
          description: It is the Template's productFamily.
          returned: always
          type: str
          sample: '<productfamily>'
        productSeries:
          description: It is the Template's productSeries.
          returned: always
          type: str
          sample: '<productseries>'
        productType:
          description: It is the Template's productType.
          returned: always
          type: str
          sample: '<producttype>'

    failurePolicy:
      description: FailurePolicy, property of the response body.
      returned: always
      type: str
      sample: '<failurepolicy>'
    id:
      description: Id, property of the response body.
      returned: always
      type: str
      sample: '478012'
    lastUpdateTime:
      description: LastUpdateTime, property of the response body.
      returned: always
      type: int
      sample: 0
    name:
      description: Name, property of the response body.
      returned: always
      type: str
      sample: '<name>'
    parentTemplateId:
      description: ParentTemplateId, property of the response body.
      returned: always
      type: str
      sample: '<parenttemplateid>'
    projectId:
      description: ProjectId, property of the response body.
      returned: always
      type: str
      sample: '<projectid>'
    projectName:
      description: ProjectName, property of the response body.
      returned: always
      type: str
      sample: '<projectname>'
    rollbackTemplateContent:
      description: RollbackTemplateContent, property of the response body.
      returned: always
      type: str
      sample: '<rollbacktemplatecontent>'
    rollbackTemplateParams:
      description: RollbackTemplateParams, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        binding:
          description: It is the Template's binding.
          returned: always
          type: str
          sample: '<binding>'
        dataType:
          description: It is the Template's dataType.
          returned: always
          type: str
          sample: '<datatype>'
        defaultValue:
          description: It is the Template's defaultValue.
          returned: always
          type: str
          sample: '<defaultvalue>'
        description:
          description: It is the Template's description.
          returned: always
          type: str
          sample: '<description>'
        displayName:
          description: It is the Template's displayName.
          returned: always
          type: str
          sample: '<displayname>'
        group:
          description: It is the Template's group.
          returned: always
          type: str
          sample: '<group>'
        id:
          description: It is the Template's id.
          returned: always
          type: str
          sample: '478012'
        instructionText:
          description: It is the Template's instructionText.
          returned: always
          type: str
          sample: '<instructiontext>'
        key:
          description: It is the Template's key.
          returned: always
          type: str
          sample: '<key>'
        notParam:
          description: It is the Template's notParam.
          returned: always
          type: bool
          sample: false
        order:
          description: It is the Template's order.
          returned: always
          type: int
          sample: 0
        paramArray:
          description: It is the Template's paramArray.
          returned: always
          type: bool
          sample: false
        parameterName:
          description: It is the Template's parameterName.
          returned: always
          type: str
          sample: '<parametername>'
        provider:
          description: It is the Template's provider.
          returned: always
          type: str
          sample: '<provider>'
        range:
          description: It is the Template's range.
          returned: always
          type: list
          contains:
            id:
              description: It is the Template's id.
              returned: always
              type: str
              sample: '478012'
            maxValue:
              description: It is the Template's maxValue.
              returned: always
              type: int
              sample: 0
            minValue:
              description: It is the Template's minValue.
              returned: always
              type: int
              sample: 0

        required:
          description: It is the Template's required.
          returned: always
          type: bool
          sample: false
        selection:
          description: It is the Template's selection.
          returned: always
          type: dict
          contains:
            id:
              description: It is the Template's id.
              returned: always
              type: str
              sample: '478012'
            selectionType:
              description: It is the Template's selectionType.
              returned: always
              type: str
              sample: '<selectiontype>'
            selectionValues:
              description: It is the Template's selectionValues.
              returned: always
              type: dict


    softwareType:
      description: SoftwareType, property of the response body.
      returned: always
      type: str
      sample: '<softwaretype>'
    softwareVariant:
      description: SoftwareVariant, property of the response body.
      returned: always
      type: str
      sample: '<softwarevariant>'
    softwareVersion:
      description: SoftwareVersion, property of the response body.
      returned: always
      type: str
      sample: '<softwareversion>'
    tags:
      description: Tags, property of the response body (list of strings).
      returned: always
      type: list
    templateContent:
      description: TemplateContent, property of the response body.
      returned: always
      type: str
      sample: '<templatecontent>'
    templateParams:
      description: TemplateParams, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        binding:
          description: It is the Template's binding.
          returned: always
          type: str
          sample: '<binding>'
        dataType:
          description: It is the Template's dataType.
          returned: always
          type: str
          sample: '<datatype>'
        defaultValue:
          description: It is the Template's defaultValue.
          returned: always
          type: str
          sample: '<defaultvalue>'
        description:
          description: It is the Template's description.
          returned: always
          type: str
          sample: '<description>'
        displayName:
          description: It is the Template's displayName.
          returned: always
          type: str
          sample: '<displayname>'
        group:
          description: It is the Template's group.
          returned: always
          type: str
          sample: '<group>'
        id:
          description: It is the Template's id.
          returned: always
          type: str
          sample: '478012'
        instructionText:
          description: It is the Template's instructionText.
          returned: always
          type: str
          sample: '<instructiontext>'
        key:
          description: It is the Template's key.
          returned: always
          type: str
          sample: '<key>'
        notParam:
          description: It is the Template's notParam.
          returned: always
          type: bool
          sample: false
        order:
          description: It is the Template's order.
          returned: always
          type: int
          sample: 0
        paramArray:
          description: It is the Template's paramArray.
          returned: always
          type: bool
          sample: false
        parameterName:
          description: It is the Template's parameterName.
          returned: always
          type: str
          sample: '<parametername>'
        provider:
          description: It is the Template's provider.
          returned: always
          type: str
          sample: '<provider>'
        range:
          description: It is the Template's range.
          returned: always
          type: list
          contains:
            id:
              description: It is the Template's id.
              returned: always
              type: str
              sample: '478012'
            maxValue:
              description: It is the Template's maxValue.
              returned: always
              type: int
              sample: 0
            minValue:
              description: It is the Template's minValue.
              returned: always
              type: int
              sample: 0

        required:
          description: It is the Template's required.
          returned: always
          type: bool
          sample: false
        selection:
          description: It is the Template's selection.
          returned: always
          type: dict
          contains:
            id:
              description: It is the Template's id.
              returned: always
              type: str
              sample: '478012'
            selectionType:
              description: It is the Template's selectionType.
              returned: always
              type: str
              sample: '<selectiontype>'
            selectionValues:
              description: It is the Template's selectionValues.
              returned: always
              type: dict


    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

delete_template:
    description: Deletes an existing Template.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Template's taskId.
          returned: success
          type: dict
        url:
          description: It is the Template's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

"""

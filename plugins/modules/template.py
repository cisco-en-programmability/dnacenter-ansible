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
module: template
short_description: Manage Template objects of ConfigurationTemplates
description:
- Creates a new Template.
- List the Templates available.
- Updates an existing Template.
- Returns details of the specified Template.
- Deletes an existing Template.
version_added: '1.0'
author: first last (@GitHubID)
options:
    project_id:
        description:
        - ProjectId path parameter.
        - Required for state create.
        type: str
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
"""

RETURN = r"""
data_0:
    description: Creates a new Template.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: TemplateDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Template's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Template's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: TemplateDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: List the Templates available.
    returned: success,changed,always
    type: dict
    contains:

data_2:
    description: Updates an existing Template.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: TemplateDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Template's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Template's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: TemplateDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_3:
    description: Returns details of the specified Template.
    returned: success,changed,always
    type: dict
    contains:
        author:
            description: Author, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<author>'
        composite:
            description: Composite, property of the response body.
            returned: success,changed,always
            type: bool
            sample: false
        containingTemplates:
            description: ContainingTemplates, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                composite:
                    description: It is the Template's composite.
                    returned: success,changed,always
                    type: bool
                    sample: false
                id:
                    description: It is the Template's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                name:
                    description: It is the Template's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                version:
                    description: It is the Template's version.
                    returned: success,changed,always
                    type: str
                    sample: '1.0'

        createTime:
            description: CreateTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<description>'
        deviceTypes:
            description: DeviceTypes, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                productFamily:
                    description: It is the Template's productFamily.
                    returned: success,changed,always
                    type: str
                    sample: '<productfamily>'
                productSeries:
                    description: It is the Template's productSeries.
                    returned: success,changed,always
                    type: str
                    sample: '<productseries>'
                productType:
                    description: It is the Template's productType.
                    returned: success,changed,always
                    type: str
                    sample: '<producttype>'

        failurePolicy:
            description: FailurePolicy, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<failurepolicy>'
        id:
            description: Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '478012'
        lastUpdateTime:
            description: LastUpdateTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        name:
            description: Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<name>'
        parentTemplateId:
            description: ParentTemplateId, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<parenttemplateid>'
        projectId:
            description: ProjectId, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<projectid>'
        projectName:
            description: ProjectName, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<projectname>'
        rollbackTemplateContent:
            description: RollbackTemplateContent, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<rollbacktemplatecontent>'
        rollbackTemplateParams:
            description: RollbackTemplateParams, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                binding:
                    description: It is the Template's binding.
                    returned: success,changed,always
                    type: str
                    sample: '<binding>'
                dataType:
                    description: It is the Template's dataType.
                    returned: success,changed,always
                    type: str
                    sample: '<datatype>'
                defaultValue:
                    description: It is the Template's defaultValue.
                    returned: success,changed,always
                    type: str
                    sample: '<defaultvalue>'
                description:
                    description: It is the Template's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                displayName:
                    description: It is the Template's displayName.
                    returned: success,changed,always
                    type: str
                    sample: '<displayname>'
                group:
                    description: It is the Template's group.
                    returned: success,changed,always
                    type: str
                    sample: '<group>'
                id:
                    description: It is the Template's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instructionText:
                    description: It is the Template's instructionText.
                    returned: success,changed,always
                    type: str
                    sample: '<instructiontext>'
                key:
                    description: It is the Template's key.
                    returned: success,changed,always
                    type: str
                    sample: '<key>'
                notParam:
                    description: It is the Template's notParam.
                    returned: success,changed,always
                    type: bool
                    sample: false
                order:
                    description: It is the Template's order.
                    returned: success,changed,always
                    type: int
                    sample: 0
                paramArray:
                    description: It is the Template's paramArray.
                    returned: success,changed,always
                    type: bool
                    sample: false
                parameterName:
                    description: It is the Template's parameterName.
                    returned: success,changed,always
                    type: str
                    sample: '<parametername>'
                provider:
                    description: It is the Template's provider.
                    returned: success,changed,always
                    type: str
                    sample: '<provider>'
                range:
                    description: It is the Template's range.
                    returned: success,changed,always
                    type: list
                    contains:
                        id:
                            description: It is the Template's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        maxValue:
                            description: It is the Template's maxValue.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        minValue:
                            description: It is the Template's minValue.
                            returned: success,changed,always
                            type: int
                            sample: 0

                required:
                    description: It is the Template's required.
                    returned: success,changed,always
                    type: bool
                    sample: false
                selection:
                    description: It is the Template's selection.
                    returned: success,changed,always
                    type: dict
                    contains:
                        id:
                            description: It is the Template's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        selectionType:
                            description: It is the Template's selectionType.
                            returned: success,changed,always
                            type: str
                            sample: '<selectiontype>'
                        selectionValues:
                            description: It is the Template's selectionValues.
                            returned: success,changed,always
                            type: dict


        softwareType:
            description: SoftwareType, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<softwaretype>'
        softwareVariant:
            description: SoftwareVariant, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<softwarevariant>'
        softwareVersion:
            description: SoftwareVersion, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<softwareversion>'
        tags:
            description: Tags, property of the response body (list of strings).
            returned: success,changed,always
            type: list
        templateContent:
            description: TemplateContent, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<templatecontent>'
        templateParams:
            description: TemplateParams, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                binding:
                    description: It is the Template's binding.
                    returned: success,changed,always
                    type: str
                    sample: '<binding>'
                dataType:
                    description: It is the Template's dataType.
                    returned: success,changed,always
                    type: str
                    sample: '<datatype>'
                defaultValue:
                    description: It is the Template's defaultValue.
                    returned: success,changed,always
                    type: str
                    sample: '<defaultvalue>'
                description:
                    description: It is the Template's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                displayName:
                    description: It is the Template's displayName.
                    returned: success,changed,always
                    type: str
                    sample: '<displayname>'
                group:
                    description: It is the Template's group.
                    returned: success,changed,always
                    type: str
                    sample: '<group>'
                id:
                    description: It is the Template's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instructionText:
                    description: It is the Template's instructionText.
                    returned: success,changed,always
                    type: str
                    sample: '<instructiontext>'
                key:
                    description: It is the Template's key.
                    returned: success,changed,always
                    type: str
                    sample: '<key>'
                notParam:
                    description: It is the Template's notParam.
                    returned: success,changed,always
                    type: bool
                    sample: false
                order:
                    description: It is the Template's order.
                    returned: success,changed,always
                    type: int
                    sample: 0
                paramArray:
                    description: It is the Template's paramArray.
                    returned: success,changed,always
                    type: bool
                    sample: false
                parameterName:
                    description: It is the Template's parameterName.
                    returned: success,changed,always
                    type: str
                    sample: '<parametername>'
                provider:
                    description: It is the Template's provider.
                    returned: success,changed,always
                    type: str
                    sample: '<provider>'
                range:
                    description: It is the Template's range.
                    returned: success,changed,always
                    type: list
                    contains:
                        id:
                            description: It is the Template's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        maxValue:
                            description: It is the Template's maxValue.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        minValue:
                            description: It is the Template's minValue.
                            returned: success,changed,always
                            type: int
                            sample: 0

                required:
                    description: It is the Template's required.
                    returned: success,changed,always
                    type: bool
                    sample: false
                selection:
                    description: It is the Template's selection.
                    returned: success,changed,always
                    type: dict
                    contains:
                        id:
                            description: It is the Template's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        selectionType:
                            description: It is the Template's selectionType.
                            returned: success,changed,always
                            type: str
                            sample: '<selectiontype>'
                        selectionValues:
                            description: It is the Template's selectionValues.
                            returned: success,changed,always
                            type: dict


        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_4:
    description: Deletes an existing Template.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Template's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Template's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.template import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()

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
module: template_deploy
short_description: Manage TemplateDeploy objects of ConfigurationTemplates
description:
- Deploys a template.
- Returns the status of a deployed template.
version_added: '1.0'
author: first last (@GitHubID)
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
        type: str
        required: True

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
"""

RETURN = r"""
data_0:
    description: Deploys a template.
    returned: success,changed,always
    type: dict
    contains:
        deploymentId:
            description: TemplateDeploymentInfo's deploymentId.
            returned: success,changed,always
            type: str
            sample: '<deploymentid>'
        deploymentName:
            description: TemplateDeploymentInfo's deploymentName.
            returned: success,changed,always
            type: str
            sample: '<deploymentname>'
        devices:
            description: TemplateDeploymentInfo's devices (list of objects).
            returned: success,changed,always
            type: list
            contains:
                deviceId:
                    description: It is the template deploy's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: '<deviceid>'
                duration:
                    description: It is the template deploy's duration.
                    returned: success,changed,always
                    type: str
                    sample: '<duration>'
                endTime:
                    description: It is the template deploy's endTime.
                    returned: success,changed,always
                    type: str
                    sample: '<endtime>'
                ipAddress:
                    description: It is the template deploy's ipAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<ipaddress>'
                name:
                    description: It is the template deploy's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                startTime:
                    description: It is the template deploy's startTime.
                    returned: success,changed,always
                    type: str
                    sample: '<starttime>'
                status:
                    description: It is the template deploy's status.
                    returned: success,changed,always
                    type: str
                    sample: '<status>'

        duration:
            description: TemplateDeploymentInfo's duration.
            returned: success,changed,always
            type: str
            sample: '<duration>'
        endTime:
            description: TemplateDeploymentInfo's endTime.
            returned: success,changed,always
            type: str
            sample: '<endtime>'
        projectName:
            description: TemplateDeploymentInfo's projectName.
            returned: success,changed,always
            type: str
            sample: '<projectname>'
        startTime:
            description: TemplateDeploymentInfo's startTime.
            returned: success,changed,always
            type: str
            sample: '<starttime>'
        status:
            description: TemplateDeploymentInfo's status.
            returned: success,changed,always
            type: str
            sample: '<status>'
        templateName:
            description: TemplateDeploymentInfo's templateName.
            returned: success,changed,always
            type: str
            sample: '<templatename>'
        templateVersion:
            description: TemplateDeploymentInfo's templateVersion.
            returned: success,changed,always
            type: str
            sample: '<templateversion>'

data_1:
    description: Returns the status of a deployed template.
    returned: success,changed,always
    type: dict
    contains:
        deploymentId:
            description: DeploymentId, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<deploymentid>'
        deploymentName:
            description: DeploymentName, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<deploymentname>'
        devices:
            description: Devices, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                deviceId:
                    description: It is the template deploy's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: '<deviceid>'
                duration:
                    description: It is the template deploy's duration.
                    returned: success,changed,always
                    type: str
                    sample: '<duration>'
                endTime:
                    description: It is the template deploy's endTime.
                    returned: success,changed,always
                    type: str
                    sample: '<endtime>'
                ipAddress:
                    description: It is the template deploy's ipAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<ipaddress>'
                name:
                    description: It is the template deploy's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                startTime:
                    description: It is the template deploy's startTime.
                    returned: success,changed,always
                    type: str
                    sample: '<starttime>'
                status:
                    description: It is the template deploy's status.
                    returned: success,changed,always
                    type: str
                    sample: '<status>'

        duration:
            description: Duration, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<duration>'
        endTime:
            description: EndTime, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<endtime>'
        projectName:
            description: ProjectName, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<projectname>'
        startTime:
            description: StartTime, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<starttime>'
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<status>'
        templateName:
            description: TemplateName, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<templatename>'
        templateVersion:
            description: TemplateVersion, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<templateversion>'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.template_deploy import (
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

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()

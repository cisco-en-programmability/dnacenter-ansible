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
module: template_deploy
short_description: Manage TemplateDeploy objects of ConfigurationTemplates
description:
- Deploys a template.
- Returns the status of a deployed template.
version_added: '1.0'
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
  register: query_result
  """

RETURN = """
deploy_template:
    description: Deploys a template.
    returned: success
    type: dict
    contains:
    deploymentId:
      description: TemplateDeploymentInfo's deploymentId.
      returned: success
      type: str
      sample: '<deploymentid>'
    deploymentName:
      description: TemplateDeploymentInfo's deploymentName.
      returned: success
      type: str
      sample: '<deploymentname>'
    devices:
      description: TemplateDeploymentInfo's devices (list of objects).
      returned: success
      type: list
      contains:
        deviceId:
          description: It is the template deploy's deviceId.
          returned: success
          type: str
          sample: '<deviceid>'
        duration:
          description: It is the template deploy's duration.
          returned: success
          type: str
          sample: '<duration>'
        endTime:
          description: It is the template deploy's endTime.
          returned: success
          type: str
          sample: '<endtime>'
        ipAddress:
          description: It is the template deploy's ipAddress.
          returned: success
          type: str
          sample: '<ipaddress>'
        name:
          description: It is the template deploy's name.
          returned: success
          type: str
          sample: '<name>'
        startTime:
          description: It is the template deploy's startTime.
          returned: success
          type: str
          sample: '<starttime>'
        status:
          description: It is the template deploy's status.
          returned: success
          type: str
          sample: '<status>'

    duration:
      description: TemplateDeploymentInfo's duration.
      returned: success
      type: str
      sample: '<duration>'
    endTime:
      description: TemplateDeploymentInfo's endTime.
      returned: success
      type: str
      sample: '<endtime>'
    projectName:
      description: TemplateDeploymentInfo's projectName.
      returned: success
      type: str
      sample: '<projectname>'
    startTime:
      description: TemplateDeploymentInfo's startTime.
      returned: success
      type: str
      sample: '<starttime>'
    status:
      description: TemplateDeploymentInfo's status.
      returned: success
      type: str
      sample: '<status>'
    templateName:
      description: TemplateDeploymentInfo's templateName.
      returned: success
      type: str
      sample: '<templatename>'
    templateVersion:
      description: TemplateDeploymentInfo's templateVersion.
      returned: success
      type: str
      sample: '<templateversion>'

get_template_deployment_status:
    description: Returns the status of a deployed template.
    returned: always
    type: dict
    contains:
    deploymentId:
      description: DeploymentId, property of the response body.
      returned: always
      type: str
      sample: '<deploymentid>'
    deploymentName:
      description: DeploymentName, property of the response body.
      returned: always
      type: str
      sample: '<deploymentname>'
    devices:
      description: Devices, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        deviceId:
          description: It is the template deploy's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duration:
          description: It is the template deploy's duration.
          returned: always
          type: str
          sample: '<duration>'
        endTime:
          description: It is the template deploy's endTime.
          returned: always
          type: str
          sample: '<endtime>'
        ipAddress:
          description: It is the template deploy's ipAddress.
          returned: always
          type: str
          sample: '<ipaddress>'
        name:
          description: It is the template deploy's name.
          returned: always
          type: str
          sample: '<name>'
        startTime:
          description: It is the template deploy's startTime.
          returned: always
          type: str
          sample: '<starttime>'
        status:
          description: It is the template deploy's status.
          returned: always
          type: str
          sample: '<status>'

    duration:
      description: Duration, property of the response body.
      returned: always
      type: str
      sample: '<duration>'
    endTime:
      description: EndTime, property of the response body.
      returned: always
      type: str
      sample: '<endtime>'
    projectName:
      description: ProjectName, property of the response body.
      returned: always
      type: str
      sample: '<projectname>'
    startTime:
      description: StartTime, property of the response body.
      returned: always
      type: str
      sample: '<starttime>'
    status:
      description: Status, property of the response body.
      returned: always
      type: str
      sample: '<status>'
    templateName:
      description: TemplateName, property of the response body.
      returned: always
      type: str
      sample: '<templatename>'
    templateVersion:
      description: TemplateVersion, property of the response body.
      returned: always
      type: str
      sample: '<templateversion>'

"""

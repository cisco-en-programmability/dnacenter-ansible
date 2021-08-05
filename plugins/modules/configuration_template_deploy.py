#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_deploy
short_description: Resource module for Configuration Template Deploy
description:
- Manage operation create of the resource Configuration Template Deploy.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  forcePushTemplate:
    description: ForcePushTemplate flag.
    type: bool
  isComposite:
    description: IsComposite flag.
    type: bool
  mainTemplateId:
    description: Configuration Template Deploy's mainTemplateId.
    type: str
  memberTemplateDeploymentInfo:
    description: Configuration Template Deploy's memberTemplateDeploymentInfo.
    elements: str
    type: list
  targetInfo:
    description: Configuration Template Deploy's targetInfo.
    suboptions:
      hostName:
        description: Configuration Template Deploy's hostName.
        type: str
      id:
        description: Configuration Template Deploy's id.
        type: str
      params:
        description: Configuration Template Deploy's params.
        type: dict
      type:
        description: Configuration Template Deploy's type.
        type: str
    type: list
  templateId:
    description: Configuration Template Deploy's templateId.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template Deploy reference
  description: Complete reference of the Configuration Template Deploy object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.configuration_template_deploy:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    forcePushTemplate: true
    isComposite: true
    mainTemplateId: string
    memberTemplateDeploymentInfo:
    - string
    targetInfo:
    - hostName: string
      id: string
      params: {}
      type: string
    templateId: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "deploymentId": "string",
      "deploymentName": "string",
      "devices": [
        {
          "deviceId": "string",
          "duration": "string",
          "endTime": "string",
          "ipAddress": "string",
          "name": "string",
          "startTime": "string",
          "status": "string"
        }
      ],
      "duration": "string",
      "endTime": "string",
      "projectName": "string",
      "startTime": "string",
      "status": "string",
      "templateName": "string",
      "templateVersion": "string"
    }
"""

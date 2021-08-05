#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_info
short_description: Information module for Configuration Template
description:
- Get all Configuration Template.
- Get Configuration Template by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  projectId:
    description:
    - ProjectId query parameter.
    type: str
  softwareType:
    description:
    - SoftwareType query parameter.
    type: str
  softwareVersion:
    description:
    - SoftwareVersion query parameter.
    type: str
  productFamily:
    description:
    - ProductFamily query parameter.
    type: str
  productSeries:
    description:
    - ProductSeries query parameter.
    type: str
  productType:
    description:
    - ProductType query parameter.
    type: str
  filterConflictingTemplates:
    description:
    - FilterConflictingTemplates query parameter.
    type: bool
  templateId:
    description:
    - TemplateId path parameter.
    type: str
  latestVersion:
    description:
    - LatestVersion query parameter.
    type: bool
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template reference
  description: Complete reference of the Configuration Template object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Configuration Template
  cisco.dnac.configuration_template_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    projectId: string
    softwareType: string
    softwareVersion: string
    productFamily: string
    productSeries: string
    productType: string
    filterConflictingTemplates: True
  register: result

- name: Get Configuration Template by id
  cisco.dnac.configuration_template_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    latestVersion: True
    templateId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "author": "string",
      "composite": true,
      "containingTemplates": [
        {
          "composite": true,
          "id": "string",
          "name": "string",
          "version": "string"
        }
      ],
      "createTime": 0,
      "description": "string",
      "deviceTypes": [
        {
          "productFamily": "string",
          "productSeries": "string",
          "productType": "string"
        }
      ],
      "failurePolicy": "string",
      "id": "string",
      "lastUpdateTime": 0,
      "name": "string",
      "parentTemplateId": "string",
      "projectId": "string",
      "projectName": "string",
      "rollbackTemplateContent": "string",
      "rollbackTemplateParams": [
        {
          "binding": "string",
          "dataType": "string",
          "defaultValue": "string",
          "description": "string",
          "displayName": "string",
          "group": "string",
          "id": "string",
          "instructionText": "string",
          "key": "string",
          "notParam": true,
          "order": 0,
          "paramArray": true,
          "parameterName": "string",
          "provider": "string",
          "range": [
            {
              "id": "string",
              "maxValue": 0,
              "minValue": 0
            }
          ],
          "required": true,
          "selection": {
            "id": "string",
            "selectionType": "string",
            "selectionValues": {}
          }
        }
      ],
      "softwareType": "string",
      "softwareVariant": "string",
      "softwareVersion": "string",
      "tags": [
        "string"
      ],
      "templateContent": "string",
      "templateParams": [
        {
          "binding": "string",
          "dataType": "string",
          "defaultValue": "string",
          "description": "string",
          "displayName": "string",
          "group": "string",
          "id": "string",
          "instructionText": "string",
          "key": "string",
          "notParam": true,
          "order": 0,
          "paramArray": true,
          "parameterName": "string",
          "provider": "string",
          "range": [
            {
              "id": "string",
              "maxValue": 0,
              "minValue": 0
            }
          ],
          "required": true,
          "selection": {
            "id": "string",
            "selectionType": "string",
            "selectionValues": {}
          }
        }
      ],
      "version": "string"
    }
"""

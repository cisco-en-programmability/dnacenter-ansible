#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: templates_template_id_versions_version_id_v1_info
short_description: Information module for Templates Template Id Versions Version Id
  V1
description:
  - Get Templates Template Id Versions Version Id V1 by id.
  - Get a template's version by the version ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  templateId:
    description:
      - >
        TemplateId path parameter. The id of the template to get versions of, retrieveable
        from `GET
        /dna/intent/api/v1/templates`.
    type: str
  versionId:
    description:
      - >
        VersionId path parameter. The id of the versioned template to get versions
        of, retrieveable from `GET
        /dna/intent/api/v1/templates/{id}/versions`.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates GetTemplateVersionV1
    description: Complete reference of the GetTemplateVersionV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-template-version
notes:
  - SDK Method used are configuration_templates.ConfigurationTemplates.get_template_version_v1,
  - Paths used are get /dna/intent/api/v1/templates/{templateId}/versions/{versionId},
"""
EXAMPLES = r"""
- name: Get Templates Template Id Versions Version Id V1 by id
  cisco.dnac.templates_template_id_versions_version_id_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    templateId: string
    versionId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "versionId": "string",
        "version": 0,
        "versionTime": 0,
        "RegularTemplate": {
          "templateId": "string",
          "name": "string",
          "projectId": "string",
          "description": "string",
          "softwareFamily": "string",
          "author": "string",
          "products": [
            {
              "productFamily": "string",
              "productSeries": "string",
              "productName": "string"
            }
          ],
          "lastUpdateTime": 0,
          "type": "string",
          "language": "string",
          "templateContent": "string"
        },
        "CompositeTemplate": {
          "templateId": "string",
          "name": "string",
          "projectId": "string",
          "description": "string",
          "softwareFamily": "string",
          "author": "string",
          "products": [
            {
              "productFamily": "string",
              "productSeries": "string",
              "productName": "string"
            }
          ],
          "lastUpdateTime": 0,
          "type": "string",
          "failurePolicy": "string"
        }
      }
    }
"""

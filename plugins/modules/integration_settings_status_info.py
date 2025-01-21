#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: integration_settings_status_info
short_description: Information module for Integration Settings Status Info
description:
- This module represents an alias of the module integration_settings_status_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for ITSM Integration GetITSMIntegrationStatusV1
  description: Complete reference of the GetITSMIntegrationStatusV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-itsm-integration-status
notes:
  - SDK Method used are
    itsm_integration.ItsmIntegration.get_itsm_integration_status_v1,

  - Paths used are
    get /dna/intent/api/v1/integration-settings/status,
  - It should be noted that this module is an alias of integration_settings_status_v1_info

"""

EXAMPLES = r"""
- name: Get all Integration Settings Status Info
  cisco.dnac.integration_settings_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "status": "string",
          "configurations": [
            {
              "dypSchemaName": "string",
              "dypInstanceId": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""

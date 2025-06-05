#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: roles_info
short_description: Information module for Roles Info
description:
  - This module represents an alias of the module roles_v1_info
version_added: '3.1.0'
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
  - name: Cisco DNA Center documentation for User and Roles GetRolesAPIV1
    description: Complete reference of the GetRolesAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-roles-api
notes:
  - SDK Method used are user_and_roles.UserandRoles.get_roles_api_v1,
  - Paths used are get /dna/system/api/v1/roles,
  - It should be noted that this module is an alias of roles_v1_info
"""
EXAMPLES = r"""
- name: Get all Roles Info
  cisco.dnac.roles_info:
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
      "roles": [
        {
          "resourceTypes": [
            {
              "operations": [
                "string"
              ],
              "type": "string"
            }
          ],
          "meta": {
            "createdBy": "string",
            "created": "string",
            "lastModified": "string"
          },
          "roleId": "string",
          "name": "string",
          "description": "string",
          "type": "string"
        }
      ]
    }
"""

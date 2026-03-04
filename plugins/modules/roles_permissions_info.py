#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: roles_permissions_info
short_description: Information module for Roles Permissions
description:
  - Get all Roles Permissions.
  - Get all v2 permissions that can be used to create or update a custom role in the system.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for User and Roles GetPermissionsV2
    description: Complete reference of the GetPermissionsV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-permissions-v-2
notes:
  - SDK Method used are
    userand_roles.UserandRoles.get_permissions_v2,
  - Paths used are
    get /dna/system/api/v2/roles/permissions,
"""

EXAMPLES = r"""
---
- name: Get all Roles Permissions
  cisco.dnac.roles_permissions_info:
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
          "description": "string",
          "displayName": "string",
          "defaultPrivilege": "string",
          "minimumPrivilege": "string",
          "maximumPrivilege": "string",
          "dependencies": [
            {
              "id": "string",
              "privilege": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""

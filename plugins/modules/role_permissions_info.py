#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: role_permissions_info
short_description: Information module for Role Permissions
description:
  - Get all Role Permissions.
  - Get permissions for a role in the system.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.10.1
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for User and
      Roles GetPermissionsAPI
    description: Complete reference of the GetPermissionsAPI
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-permissions-api
notes:
  - SDK Method used are
    user_and_roles.UserandRoles.get_permissions_api,
  - Paths used are
    get /dna/system/api/v1/role/permissions,
"""

EXAMPLES = r"""
---
- name: Get all Role Permissions
  cisco.dnac.role_permissions_info:
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
      "resource-types": [
        {
          "type": "string",
          "displayName": "string",
          "description": "string",
          "defaultPermission": "string"
        }
      ]
    }
"""

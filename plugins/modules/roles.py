#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: roles
short_description: Resource module for Roles
description:
  - This module represents an alias of the module roles_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of role.
    type: str
  resourceTypes:
    description: Roles's resourceTypes.
    elements: dict
    suboptions:
      operations:
        description: List of operations allowed for the application. Possible values
          are "gRead", "gCreate", "gUpdate", "gRemove", or some combination of these.
        elements: str
        type: list
      type:
        description: Name of the application in the System.
        type: str
    type: list
  role:
    description: Name of the role.
    type: str
  roleId:
    description: Id of the role.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for User and Roles AddRoleAPIV1
    description: Complete reference of the AddRoleAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-role-api
  - name: Cisco DNA Center documentation for User and Roles DeleteRoleAPIV1
    description: Complete reference of the DeleteRoleAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-role-api
  - name: Cisco DNA Center documentation for User and Roles UpdateRoleAPIV1
    description: Complete reference of the UpdateRoleAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-role-api
notes:
  - SDK Method used are user_and_roles.UserandRoles.add_role_api_v1, user_and_roles.UserandRoles.delete_role_api_v1,
    user_and_roles.UserandRoles.update_role_api_v1,
  - Paths used are post /dna/system/api/v1/role, delete /dna/system/api/v1/role/{roleId},
    put /dna/system/api/v1/role,
  - It should be noted that this module is an alias of roles_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.roles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    resourceTypes:
      - operations:
          - string
        type: string
    role: string
- name: Update all
  cisco.dnac.roles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    resourceTypes:
      - operations:
          - string
        type: string
    roleId: string
- name: Delete by id
  cisco.dnac.roles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    roleId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "roleId": "string",
      "message": "string"
    }
"""

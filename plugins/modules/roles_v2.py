#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: roles_v2
short_description: Resource module for Roles V2
description:
  - Manage operations create, update and delete of the resource Roles V2.
  - Add a new role into system v2-.
  - Delete a role in the system.
  - Update a role in the system v2-.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of role.
    type: str
  id:
    description: Id path parameter. The Id of the role to be deleted.
    type: str
  name:
    description: Name of the role.
    type: str
  permissions:
    description: Roles V2's permissions.
    elements: dict
    suboptions:
      operations:
        description: List of operations allowed for the application. Possible values are "gRead", "gCreate", "gUpdate", "gRemove",
          or some combination of these.
        elements: str
        type: list
      type:
        description: Name of the application in the System.
        type: str
    type: list
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for User and Roles AddRoleV2
    description: Complete reference of the AddRoleV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-role-v-2
  - name: Cisco DNA Center documentation for User and Roles DeleteRoleV2
    description: Complete reference of the DeleteRoleV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-role-v-2
  - name: Cisco DNA Center documentation for User and Roles UpdateRoleV2
    description: Complete reference of the UpdateRoleV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-role-v-2
notes:
  - SDK Method used are
    userand_roles.UserandRoles.add_role_v2,
    userand_roles.UserandRoles.delete_role_v2,
    userand_roles.UserandRoles.update_role_v2,
  - Paths used are
    post /dna/system/api/v2/roles,
    delete /dna/system/api/v2/roles/{id},
    put /dna/system/api/v2/roles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.roles_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    name: string
    permissions:
      - operations:
          - string
        type: string
- name: Delete by id
  cisco.dnac.roles_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.dnac.roles_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    id: string
    name: string
    permissions:
      - operations:
          - string
        type: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "permissions": [
        {
          "privilege": "string",
          "id": "string"
        }
      ],
      "type": "string",
      "version": "string",
      "meta": {
        "created": "string",
        "createdBy": "string",
        "lastModified": "string",
        "lastModifiedBy": "string"
      }
    }
"""

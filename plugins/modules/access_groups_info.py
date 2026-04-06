#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: access_groups_info
short_description: Information module for Access Groups
description:
  - Get all Access Groups.
  - Get Access Groups by id.
  - Get all access groups in the system.
  - Get an access group in the system.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  userCount:
    description:
      - >
        UserCount query parameter. If set to true, it will return number of users associated with each access
        group. Default is false.
    type: str
  names:
    description:
      - >
        Names query parameter. Get access groups by passing comma separated list of names. It performs an exact
        character match.
    type: str
  type:
    description:
      - Type query parameter. Get access groups by passing the type of the resource such as site.
    type: str
  sourceResourceIds:
    description:
      - >
        SourceResourceIds query parameter. Get access groups by passing the ids of the resource associated with
        it such as the site hierarchy id.
    type: str
  ids:
    description:
      - Ids query parameter. Get access groups by passing a comma separated list of their ids.
    type: str
  offset:
    description:
      - Offset query parameter. An integer representing the starting access group in the page returned.
    type: int
  limit:
    description:
      - Limit query parameter. Limit on the number of access groups on a page. Default page size is 20.
    type: int
  id:
    description:
      - Id path parameter. Id of the access group to query.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for User and Roles GetAccessGroup
    description: Complete reference of the GetAccessGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-group
  - name: Cisco DNA Center documentation for User and Roles GetAccessGroups
    description: Complete reference of the GetAccessGroups API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-groups
notes:
  - SDK Method used are
    userand_roles.UserandRoles.get_access_group,
    userand_roles.UserandRoles.get_access_groups,
  - Paths used are
    get /dna/system/api/v1/accessGroups,
    get /dna/system/api/v1/accessGroups/{id},
"""

EXAMPLES = r"""
---
- name: Get all Access Groups
  cisco.dnac.access_groups_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    userCount: string
    names: string
    type: string
    sourceResourceIds: string
    ids: string
    offset: 0
    limit: 0
  register: result
- name: Get Access Groups by id
  cisco.dnac.access_groups_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "accessGroupInfo": {
        "name": "string",
        "description": "string",
        "resourceGroups": [
          {
            "name": "string",
            "srcResourceId": "string",
            "type": "string"
          }
        ],
        "role": [
          "string"
        ]
      },
      "meta": {
        "created": "string",
        "createdBy": "string",
        "lastModified": "string",
        "lastModifiedBy": "string"
      }
    }
"""

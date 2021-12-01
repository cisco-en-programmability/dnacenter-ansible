#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: projects_details_info
short_description: Information module for Projects Details
description:
- Get all Projects Details.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id query parameter. Id of project to be searched.
    type: str
  name:
    description:
    - Name query parameter. Name of project to be searched.
    type: str
  offset:
    description:
    - Offset query parameter. Index of first result.
    type: int
  limit:
    description:
    - Limit query parameter. Limits number of results.
    type: int
  sortOrder:
    description:
    - SortOrder query parameter. Sort Order Ascending (asc) or Descending (dsc).
    type: str
requirements:
- dnacentersdk >= 2.3.1
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Projects Details reference
  description: Complete reference of the Projects Details object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Projects Details
  cisco.dnac.projects_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    id: string
    name: string
    offset: 0
    limit: 0
    sortOrder: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "createTime": 0,
      "description": "string",
      "id": "string",
      "isDeletable": true,
      "lastUpdateTime": 0,
      "name": "string",
      "tags": [
        {
          "id": "string",
          "name": "string"
        }
      ],
      "templates": {}
    }
"""

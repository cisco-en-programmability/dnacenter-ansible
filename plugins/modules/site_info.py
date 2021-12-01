#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_info
short_description: Information module for Site
description:
- Get all Site.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
    - Name query parameter. SiteNameHierarchy (ex global/groupName).
    type: str
  siteId:
    description:
    - SiteId query parameter. Site id to which site details to retrieve.
    type: str
  type:
    description:
    - Type query parameter. Type (ex area, building, floor).
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting row.
    type: str
  limit:
    description:
    - Limit query parameter. Number of sites to be retrieved.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Site reference
  description: Complete reference of the Site object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Site
  cisco.dnac.site_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    name: string
    siteId: string
    type: string
    offset: string
    limit: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "parentId": "string",
        "name": "string",
        "additionalInfo": [
          "string"
        ],
        "siteHierarchy": "string",
        "siteNameHierarchy": "string",
        "instanceTenantId": "string",
        "id": "string"
      }
    ]
"""

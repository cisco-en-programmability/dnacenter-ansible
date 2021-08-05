#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_create
short_description: Resource module for Site Create
description:
- Manage operation create of the resource Site Create.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site:
    description: Site Create's site.
    suboptions:
      area:
        description: Site Create's area.
        suboptions:
          name:
            description: Site Create's name.
            type: str
          parentName:
            description: Site Create's parentName.
            type: str
        type: dict
      building:
        description: Site Create's building.
        suboptions:
          address:
            description: Site Create's address.
            type: str
          latitude:
            description: Site Create's latitude.
            type: int
          longitude:
            description: Site Create's longitude.
            type: int
          name:
            description: Site Create's name.
            type: str
          parentName:
            description: Site Create's parentName.
            type: str
        type: dict
      floor:
        description: Site Create's floor.
        suboptions:
          height:
            description: Site Create's height.
            type: int
          length:
            description: Site Create's length.
            type: int
          name:
            description: Site Create's name.
            type: str
          parentName:
            description: Site Create's parentName.
            type: str
          rfModel:
            description: Site Create's rfModel.
            type: str
          width:
            description: Site Create's width.
            type: int
        type: dict
    type: dict
  type:
    description: Site Create's type.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Site Create reference
  description: Complete reference of the Site Create object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.site_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    site:
      area:
        name: string
        parentName: string
      building:
        address: string
        latitude: 0
        longitude: 0
        name: string
        parentName: string
      floor:
        height: 0
        length: 0
        name: string
        parentName: string
        rfModel: string
        width: 0
    type: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

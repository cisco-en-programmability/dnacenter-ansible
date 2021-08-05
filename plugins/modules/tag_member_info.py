#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tag_member_info
short_description: Information module for Tag Member
description:
- Get Tag Member by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter. Tag ID.
    type: str
  memberType:
    description:
    - >
      MemberType query parameter. Entity type of the member. Possible values can be retrieved by using
      /tag/member/type API.
    type: str
  offset:
    description:
    - Offset query parameter. Used for pagination. It indicates the starting row number out of available member records.
    type: str
  limit:
    description:
    - Limit query parameter. Used to Number of maximum members to return in the result.
    type: str
  memberAssociationType:
    description:
    - >
      MemberAssociationType query parameter. Indicates how the member is associated with the tag. Possible values
      and description. 1) DYNAMIC The member is associated to the tag through rules. 2) STATIC – The member is
      associated to the tag manually. 3) MIXED – The member is associated manually and also satisfies the rule
      defined for the tag.
    type: str
  level:
    description:
    - Level query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Tag Member reference
  description: Complete reference of the Tag Member object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Tag Member by id
  cisco.dnac.tag_member_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    memberType: string
    offset: string
    limit: string
    memberAssociationType: string
    level: string
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
      "version": "string",
      "response": [
        {
          "instanceUuid": "string"
        }
      ]
    }
"""

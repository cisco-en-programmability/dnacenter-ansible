#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tag_membership
short_description: Resource module for Tag Membership
description:
- Manage operation update of the resource Tag Membership.
- Updates tag membership. As part of the request payload through this API,
  only the specified members are added / retained to the given input tags.
  Possible values of memberType attribute in the request payload can be queried by using the /tag/member/type API.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  memberToTags:
    description: Tag Membership's memberToTags.
    elements: dict
    type: list
  memberType:
    description: Tag Membership's memberType.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    tag.Tag.updates_tag_membership,

  - Paths used are
    put /dna/intent/api/v1/tag/member,

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.tag_membership:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    memberToTags:
      - 8bf887f3-7cc2-4bd2-9407-df0fe6b7f63a:
        - 7bf887f3-7cc2-7bd2-9407-df0fe6b7f63a
    memberType: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "taskId": "string",
        "url": "string"
      }
    }
"""

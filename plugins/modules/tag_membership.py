#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: tag_membership
short_description: Resource module for Tag Membership
description:
  - This module represents an alias of the module tag_membership_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  memberToTags:
    description: Tag Membership's memberToTags.
    suboptions:
      key:
        description: Tag Membership's key.
        elements: str
        type: list
    type: dict
  memberType:
    description: Tag Membership's memberType.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag UpdateTagMembershipV1
    description: Complete reference of the UpdateTagMembershipV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-tag-membership
notes:
  - SDK Method used are tag.Tag.update_tag_membership_v1,
  - Paths used are put /dna/intent/api/v1/tag/member,
  - It should be noted that this module is an alias of tag_membership_v1
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
      key:
        - string
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

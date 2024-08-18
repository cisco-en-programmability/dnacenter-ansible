#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interfaces_membersAssociations_count_info
short_description: Information module for Interfaces Membersassociations Count
description:
- Get all Interfaces Membersassociations Count.
- >
   Fetches the count of interfaces that are associated with at least one tag. A tag is a user-defined or system-
   defined construct to group resources. When an interface is tagged, it is called a member of the tag.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Tag RetrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag
  description: Complete reference of the RetrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-interfaces-that-are-associated-with-at-least-one-tag
notes:
  - SDK Method used are
    tag.Tag.retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag,

  - Paths used are
    get /intent/api/v1/tags/interfaces/membersAssociations/count,

"""

EXAMPLES = r"""
- name: Get all Interfaces Membersassociations Count
  cisco.dnac.interfaces_membersAssociations_count_info:
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
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""

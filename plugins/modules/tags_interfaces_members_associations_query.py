#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: tags_interfaces_members_associations_query
short_description: Resource module for Tags Interfaces Members Associations Query
description:
  - This module represents an alias of the module tags_interfaces_members_associations_query_v1
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  ids:
    description: List of member ids (network device or interface), maximum 500 ids
      can be passed.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag QueryTheTagsAssociatedWithInterfacesV1
    description: Complete reference of the QueryTheTagsAssociatedWithInterfacesV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!query-the-tags-associated-with-interfaces
notes:
  - SDK Method used are tag.Tag.query_the_tags_associated_with_interfaces_v1,
  - Paths used are post /dna/intent/api/v1/tags/interfaces/membersAssociations/query,
  - It should be noted that this module is an alias of tags_interfaces_members_associations_query_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.tags_interfaces_members_associations_query:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    ids:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "tags": [
            {
              "id": "string",
              "name": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""

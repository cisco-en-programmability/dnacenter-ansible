#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: user_enrichment_details
short_description: Manage UserEnrichmentDetails objects of Users
description:
- Enriches a given network End User context (a network user-id or end user's device Mac Address) with details about the user and devices that the user is connected to.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description:
    - Adds the header parameters.
    type: dict
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.user_enrichment_details
# Reference by Internet resource
- name: UserEnrichmentDetails reference
  description: Complete reference of the UserEnrichmentDetails object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: UserEnrichmentDetails reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_user_enrichment_details
  cisco.dnac.user_enrichment_details:
    state: query  # required
    headers:  # required
  register: query_result

"""

RETURN = """
"""

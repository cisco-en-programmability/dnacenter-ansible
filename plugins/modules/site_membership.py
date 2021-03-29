#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_membership
short_description: Manage SiteMembership objects of Sites
description:
- Getting the site children details and device details.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site_id:
    description:
    - Site id to retrieve device associated with the site.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.site_membership
# Reference by Internet resource
- name: SiteMembership reference
  description: Complete reference of the SiteMembership object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SiteMembership reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_membership
  cisco.dnac.site_membership:
    state: query  # required
    site_id: SomeValue  # string, required
  register: query_result

"""

RETURN = """
"""

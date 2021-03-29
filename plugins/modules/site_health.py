#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_health
short_description: Manage SiteHealth objects of Sites
description:
- Returns Overall Health information for all sites.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  timestamp:
    description:
    - Epoch time(in milliseconds) when the Site Hierarchy data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.site_health
# Reference by Internet resource
- name: SiteHealth reference
  description: Complete reference of the SiteHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SiteHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_site_health
  cisco.dnac.site_health:
    state: query  # required
    timestamp: 1  #  integer
  register: query_result

"""

RETURN = """
"""

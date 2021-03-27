#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: network_health
short_description: Manage NetworkHealth objects of Topology
description:
- Returns Overall Network Health information by Device category (Access, Distribution, Core, Router, Wireless) for any given point of time.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  timestamp:
    description:
    - Epoch time(in milliseconds) when the Network health data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_health
# Reference by Internet resource
- name: NetworkHealth reference
  description: Complete reference of the NetworkHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_overall_network_health
  cisco.dnac.network_health:
    state: query  # required
    timestamp: 1  #  integer
  register: query_result
  
"""

RETURN = """
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

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
  register: nm_get_membership

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: sites.get_membership
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

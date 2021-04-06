#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_site
short_description: Manage SdaFabricSite objects of Sda
description:
- Delete Site from SDA Fabric.
- Get Site info from SDA Fabric.
- Add Site in SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site_name_hierarchy:
    description:
    - Site Name Hierarchy.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      fabricName:
        description:
        - It is the sda fabric site's fabricName.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda fabric site's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_fabric_site
# Reference by Internet resource
- name: SdaFabricSite reference
  description: Complete reference of the SdaFabricSite object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaFabricSite reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_site
  cisco.dnac.sda_fabric_site:
    state: delete  # required
    site_name_hierarchy: SomeValue  # string, required

- name: get_site
  cisco.dnac.sda_fabric_site:
    state: query  # required
    site_name_hierarchy: SomeValue  # string, required
  register: query_result

- name: add_site
  cisco.dnac.sda_fabric_site:
    state: create  # required
    payload:  # required
    - fabricName: SomeValue  # string
      siteNameHierarchy: SomeValue  # string

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
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

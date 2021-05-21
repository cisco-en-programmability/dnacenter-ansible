#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: sda_auth_profile
short_description: Manage SdaAuthProfile objects of Sda
description:
- Add default authentication profile in SDA Fabric.
- Get default authentication profile from SDA Fabric.
- Add default authentication profile in SDA Fabric.
- Update default authentication profile in SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site_name_hierarchy:
    description:
    - SiteNameHierarchy query parameter.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      authenticateTemplateName:
        description:
        - It is the sda auth profile's authenticateTemplateName.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda auth profile's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_auth_profile
# Reference by Internet resource
- name: SdaAuthProfile reference
  description: Complete reference of the SdaAuthProfile object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaAuthProfile reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: delete  # required
    site_name_hierarchy: SomeValue  # string, required

- name: get_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: query  # required
    site_name_hierarchy: SomeValue  # string, required
  register: nm_get_default_authentication_profile

- name: add_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: create  # required
    payload:  # required
    - siteNameHierarchy: SomeValue  # string
      authenticateTemplateName: SomeValue  # string

- name: update_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: update  # required
    payload:  # required
    - siteNameHierarchy: SomeValue  # string
      authenticateTemplateName: SomeValue  # string

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
  sample: sda.add_default_authentication_profile
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

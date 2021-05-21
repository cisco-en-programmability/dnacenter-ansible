#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: sda_virtual_network
short_description: Manage SdaVirtualNetwork objects of Sda
description:
- Get virtual network (VN) from SDA Fabric.
- Delete virtual network (VN) from SDA Fabric.
- Add virtual network (VN) in SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site_name_hierarchy:
    description:
    - SiteNameHierarchy query parameter.
    type: str
    required: True
  virtual_network_name:
    description:
    - VirtualNetworkName query parameter.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      virtualNetworkName:
        description:
        - It is the sda virtual network's virtualNetworkName.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda virtual network's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_virtual_network
# Reference by Internet resource
- name: SdaVirtualNetwork reference
  description: Complete reference of the SdaVirtualNetwork object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaVirtualNetwork reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_vn
  cisco.dnac.sda_virtual_network:
    state: query  # required
    site_name_hierarchy: SomeValue  # string, required
    virtual_network_name: SomeValue  # string, required
  register: nm_get_vn

- name: delete_vn
  cisco.dnac.sda_virtual_network:
    state: delete  # required
    site_name_hierarchy: SomeValue  # string, required
    virtual_network_name: SomeValue  # string, required

- name: add_vn
  cisco.dnac.sda_virtual_network:
    state: create  # required
    payload:  # required
    - virtualNetworkName: SomeValue  # string
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
  sample: sda.add_vn
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

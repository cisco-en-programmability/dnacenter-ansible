#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: file_namespace
short_description: Manage FileNamespace objects of File
description:
- Returns list of available namespaces.
- Returns list of files under a specific namespace.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  name_space:
    description:
    - A listing of fileId's.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.file_namespace
# Reference by Internet resource
- name: FileNamespace reference
  description: Complete reference of the FileNamespace object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: FileNamespace reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_list_of_available_namespaces
  cisco.dnac.file_namespace:
    state: query  # required
  register: nm_get_list_of_available_namespaces

- name: get_list_of_files
  cisco.dnac.file_namespace:
    state: query  # required
    name_space: SomeValue  # string, required
  register: nm_get_list_of_files

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
  sample: file.get_list_of_available_namespaces
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

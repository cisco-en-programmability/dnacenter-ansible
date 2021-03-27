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

  register: query_result
  
- name: get_list_of_files
  cisco.dnac.file_namespace:
    state: query  # required
    name_space: SomeValue  # string, required
  register: query_result
  
"""

RETURN = """
"""

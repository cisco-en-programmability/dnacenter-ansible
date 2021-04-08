#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file
short_description: Manage File objects of File
description:
- Downloads a File specified by FileId.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  file_id:
    description:
    - File Identification number.
    type: str
    required: True
  dirpath:
    description:
    - Directory absolute path. Defaults to current working directory.
    type: str
  save_file:
    description:
    - Enable or disable automatic File creation of raw response.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.file
# Reference by Internet resource
- name: File reference
  description: Complete reference of the File object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: File reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: download_a_file_by_fileid
  cisco.dnac.file:
    state: query  # required
    file_id: SomeValue  # string, required
    dirpath: SomeValue  # string
    save_file: True  # boolean
  register: nm_download_a_file_by_fileid

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
  sample: file.download_a_file_by_fileid
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

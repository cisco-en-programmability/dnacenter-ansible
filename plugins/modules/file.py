#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: file
short_description: Manage File objects of File
description:
- Downloads a File specified by FileId.
version_added: '1.0'
author: first last (@GitHubID)
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
  cisco.dnac.file
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    file_id: SomeValue  # string, required
    dirpath: SomeValue  # string
    save_file: True  # boolean
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
download_a_file_by_fileid:
    description: Downloads a File specified by FileId.
    returned: always
    type: dict
    contains:

"""

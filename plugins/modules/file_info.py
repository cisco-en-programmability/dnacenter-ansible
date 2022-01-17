#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_info
short_description: Information module for File
description:
- Get File by id.
- Downloads a file specified by fileId.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fileId:
    description:
    - FileId path parameter. File Identification number.
    type: str
  dirPath:
    description:
    - Directory absolute path. Defaults to the current working directory.
    type: str
  saveFile:
    description:
    - Enable or disable automatic file creation of raw response.
    type: bool
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function download_a_file_by_fileid used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.file.File.download_a_file_by_fileid

notes:
  - Paths used: get /dna/intent/api/v1/file/{fileId}
"""

EXAMPLES = r"""
- name: Get File by id
  cisco.dnac.file_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    fileId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""

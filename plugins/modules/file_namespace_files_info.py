#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: file_namespace_files_info
short_description: Information module for File Namespace Files Info
description:
- This module represents an alias of the module file_namespace_files_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  nameSpace:
    description:
    - NameSpace path parameter. A listing of fileId's.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for File GetListOfFilesV1
  description: Complete reference of the GetListOfFilesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-list-of-files
notes:
  - SDK Method used are
    file.File.get_list_of_files_v1,

  - Paths used are
    get /dna/intent/api/v1/file/namespace/{nameSpace},
  - It should be noted that this module is an alias of file_namespace_files_v1_info

"""

EXAMPLES = r"""
- name: Get File Namespace Files Info by name
  cisco.dnac.file_namespace_files_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    nameSpace: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "attributeInfo": {},
          "downloadPath": "string",
          "encrypted": true,
          "fileFormat": "string",
          "fileSize": "string",
          "id": "string",
          "md5Checksum": "string",
          "name": "string",
          "nameSpace": "string",
          "sftpServerList": [
            {}
          ],
          "sha1Checksum": "string",
          "taskId": "string"
        }
      ],
      "version": "string"
    }
"""

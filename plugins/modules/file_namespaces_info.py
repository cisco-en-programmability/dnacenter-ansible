#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_namespaces_info
short_description: Information module for File Namespaces
description:
  - Get all File Namespaces.
  - Get File Namespaces by name.
  - Returns list of available namespaces.
  - Returns list of files under a specific namespace.
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
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for File GetListOfAvailableNamespaces
    description: Complete reference of the GetListOfAvailableNamespaces API.
    link: https://developer.cisco.com/docs/dna-center/#!get-list-of-available-namespaces
  - name: Cisco DNA Center documentation for File GetListOfFiles
    description: Complete reference of the GetListOfFiles API.
    link: https://developer.cisco.com/docs/dna-center/#!get-list-of-files
notes:
  - SDK Method used are
    file.File.get_list_of_available_namespaces,
    file.File.get_list_of_files,
  - Paths used are
    get /dna/intent/api/v1/file/namespace,
    get /dna/intent/api/v1/file/namespace/{nameSpace},
"""

EXAMPLES = r"""
---
- name: Get all File Namespaces
  cisco.dnac.file_namespaces_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
- name: Get File Namespaces by name
  cisco.dnac.file_namespaces_info:
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
            "string"
          ],
          "sha1Checksum": "string",
          "taskId": "string"
        }
      ],
      "version": "string"
    }
"""

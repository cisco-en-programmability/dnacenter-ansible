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
version_added: '1.0'
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
get_list_of_available_namespaces:
    description: Returns list of available namespaces.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of strings).
      returned: always
      type: list
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_list_of_files:
    description: Returns list of files under a specific namespace.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        attributeInfo:
          description: It is the file namespace's attributeInfo.
          returned: always
          type: dict
        downloadPath:
          description: It is the file namespace's downloadPath.
          returned: always
          type: str
          sample: '<downloadpath>'
        encrypted:
          description: It is the file namespace's encrypted.
          returned: always
          type: bool
          sample: false
        fileFormat:
          description: It is the file namespace's fileFormat.
          returned: always
          type: str
          sample: '<fileformat>'
        fileSize:
          description: It is the file namespace's fileSize.
          returned: always
          type: str
          sample: '<filesize>'
        id:
          description: It is the file namespace's id.
          returned: always
          type: str
          sample: '478012'
        md5Checksum:
          description: It is the file namespace's md5Checksum.
          returned: always
          type: str
          sample: '<md5checksum>'
        name:
          description: It is the file namespace's name.
          returned: always
          type: str
          sample: '<name>'
        nameSpace:
          description: It is the file namespace's nameSpace.
          returned: always
          type: str
          sample: '<namespace>'
        sftpServerList:
          description: It is the file namespace's sftpServerList.
          returned: always
          type: list
        sha1Checksum:
          description: It is the file namespace's sha1Checksum.
          returned: always
          type: str
          sample: '<sha1checksum>'
        taskId:
          description: It is the file namespace's taskId.
          returned: always
          type: dict

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: file_import
short_description: Resource module for File Import
description:
  - This module represents an alias of the module file_import_v1
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  nameSpace:
    description: NameSpace path parameter.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for File UploadFileV1
    description: Complete reference of the UploadFileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!upload-file
notes:
  - SDK Method used are file.File.upload_file_v1,
  - Paths used are post /dna/intent/api/v1/file/{nameSpace},
  - It should be noted that this module is an alias of file_import_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.file_import:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    nameSpace: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""

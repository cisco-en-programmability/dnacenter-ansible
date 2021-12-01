#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: authentication_import_certificate_p12
short_description: Resource module for Authentication Import Certificate P12
description:
- Manage operation create of the resource Authentication Import Certificate P12.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  listOfUsers:
    description: ListOfUsers query parameter.
    type: list
  p12FilePath:
    description: P12 file absolute path.
    type: str
  p12Password:
    description: P12Password query parameter. P12 Passsword.
    type: str
  pkPassword:
    description: PkPassword query parameter. Private Key Passsword.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Authentication Import Certificate P12 reference
  description: Complete reference of the Authentication Import Certificate P12 object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.authentication_import_certificate_p12:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    listOfUsers: []
    p12FilePath: /tmp/uploads/Test-242.p12
    p12Password: string
    pkPassword: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

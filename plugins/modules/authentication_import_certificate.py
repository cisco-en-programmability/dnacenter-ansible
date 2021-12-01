#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: authentication_import_certificate
short_description: Resource module for Authentication Import Certificate
description:
- Manage operation create of the resource Authentication Import Certificate.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  certFilePath:
    description: Cert file absolute path.
    type: str
  listOfUsers:
    description: ListOfUsers query parameter.
    type: list
  pkFilePath:
    description: Pk file absolute path.
    type: str
  pkPassword:
    description: PkPassword query parameter. Private Key Passsword.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Authentication Import Certificate reference
  description: Complete reference of the Authentication Import Certificate object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.authentication_import_certificate:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    certFilePath: /tmp/uploads/Test-242.pem
    listOfUsers: []
    pkFilePath: /tmp/uploads/Test-242.key
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

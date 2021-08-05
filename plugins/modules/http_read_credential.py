#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: http_read_credential
short_description: Resource module for Http Read Credential
description:
- Manage operations create and update of the resource Http Read Credential.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Http Read Credential's payload.
    suboptions:
      comments:
        description: Http Read Credential's comments.
        type: str
      credentialType:
        description: Http Read Credential's credentialType.
        type: str
      description:
        description: Http Read Credential's description.
        type: str
      id:
        description: Http Read Credential's id.
        type: str
      instanceTenantId:
        description: Http Read Credential's instanceTenantId.
        type: str
      instanceUuid:
        description: Http Read Credential's instanceUuid.
        type: str
      password:
        description: Http Read Credential's password.
        type: str
      port:
        description: Http Read Credential's port.
        type: int
      secure:
        description: Secure flag.
        type: bool
      username:
        description: Http Read Credential's username.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Http Read Credential reference
  description: Complete reference of the Http Read Credential object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.http_read_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Create
  cisco.dnac.http_read_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": {},
        "url": "string"
      },
      "version": "string"
    }
"""

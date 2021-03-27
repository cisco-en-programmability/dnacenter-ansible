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
module: global_credential_http_write
short_description: Manage GlobalCredentialHttpWrite objects of Discovery
description:
- Adds global HTTP write credentials.
- Updates global HTTP write credentials.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      comments:
        description:
        - It is the global credential http write's comments.
        type: str
      credentialType:
        description:
        - It is the global credential http write's credentialType.
        type: str
      description:
        description:
        - It is the global credential http write's description.
        type: str
      id:
        description:
        - It is the global credential http write's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential http write's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential http write's instanceUuid.
        type: str
      password:
        description:
        - It is the global credential http write's password.
        type: str
        required: True
      port:
        description:
        - It is the global credential http write's port.
        type: int
        required: True
      secure:
        description:
        - It is the global credential http write's secure.
        type: bool
      username:
        description:
        - It is the global credential http write's username.
        type: str
        required: True

  comments:
    description:
    - HTTPWriteCredentialDTO's comments.
    type: str
  credentialType:
    description:
    - HTTPWriteCredentialDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - HTTPWriteCredentialDTO's description.
    type: str
  id:
    description:
    - HTTPWriteCredentialDTO's id.
    type: str
  instanceTenantId:
    description:
    - HTTPWriteCredentialDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - HTTPWriteCredentialDTO's instanceUuid.
    type: str
  password:
    description:
    - HTTPWriteCredentialDTO's password.
    - Required for state update.
    type: str
  port:
    description:
    - HTTPWriteCredentialDTO's port.
    - Required for state update.
    type: int
  secure:
    description:
    - HTTPWriteCredentialDTO's secure.
    type: bool
  username:
    description:
    - HTTPWriteCredentialDTO's username.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_http_write
# Reference by Internet resource
- name: GlobalCredentialHttpWrite reference
  description: Complete reference of the GlobalCredentialHttpWrite object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialHttpWrite reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_http_write_credentials
  cisco.dnac.global_credential_http_write:
    state: create  # required
    payload:  # required
    - password: SomeValue  # string, required
      port: 1  #  integer, required
      username: SomeValue  # string, required
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      secure: True  # boolean

- name: update_http_write_credentials
  cisco.dnac.global_credential_http_write:
    state: update  # required
    password: SomeValue  # string, required
    port: 1  #  integer, required
    username: SomeValue  # string, required
    comments: SomeValue  # string
    credentialType: SomeValue  # string, valid values: 'GLOBAL', 'APP'.
    description: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    instanceUuid: SomeValue  # string
    secure: True  # boolean

"""

RETURN = """
"""

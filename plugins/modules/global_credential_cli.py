#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credential_cli
short_description: Manage GlobalCredentialCli objects of Discovery
description:
- Adds global CLI credential.
- Updates global CLI credentials.
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
        - It is the global credential cli's comments.
        type: str
      credentialType:
        description:
        - It is the global credential cli's credentialType.
        type: str
      description:
        description:
        - It is the global credential cli's description.
        type: str
      enablePassword:
        description:
        - It is the global credential cli's enablePassword.
        type: str
        required: True
      id:
        description:
        - It is the global credential cli's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential cli's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential cli's instanceUuid.
        type: str
      password:
        description:
        - It is the global credential cli's password.
        type: str
        required: True
      username:
        description:
        - It is the global credential cli's username.
        type: str
        required: True

  comments:
    description:
    - CLICredentialDTO's comments.
    type: str
  credentialType:
    description:
    - CLICredentialDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - CLICredentialDTO's description.
    type: str
  enablePassword:
    description:
    - CLICredentialDTO's enablePassword.
    - Required for state update.
    type: str
  id:
    description:
    - CLICredentialDTO's id.
    type: str
  instanceTenantId:
    description:
    - CLICredentialDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - CLICredentialDTO's instanceUuid.
    type: str
  password:
    description:
    - CLICredentialDTO's password.
    - Required for state update.
    type: str
  username:
    description:
    - CLICredentialDTO's username.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_cli
# Reference by Internet resource
- name: GlobalCredentialCli reference
  description: Complete reference of the GlobalCredentialCli object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialCli reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_cli_credentials
  cisco.dnac.global_credential_cli:
    state: create  # required
    payload:  # required
    - enablePassword: SomeValue  # string, required
      password: SomeValue  # string, required
      username: SomeValue  # string, required
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string

- name: update_cli_credentials
  cisco.dnac.global_credential_cli:
    state: update  # required
    enablePassword: SomeValue  # string, required
    password: SomeValue  # string, required
    username: SomeValue  # string, required
    comments: SomeValue  # string
    credentialType: # valid values are 'GLOBAL',
      # 'APP'.
      SomeValue  # string
    description: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    instanceUuid: SomeValue  # string

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: discovery.create_cli_credentials
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

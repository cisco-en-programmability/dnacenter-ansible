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
module: global_credential_http_read
short_description: Manage GlobalCredentialHttpRead objects of Discovery
description:
- Adds HTTP read credentials.
- Updates global HTTP Read credential.
version_added: '1.0'
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
        - It is the global credential http read's comments.
        type: str
      credentialType:
        description:
        - It is the global credential http read's credentialType.
        type: str
      description:
        description:
        - It is the global credential http read's description.
        type: str
      id:
        description:
        - It is the global credential http read's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential http read's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential http read's instanceUuid.
        type: str
      password:
        description:
        - It is the global credential http read's password.
        type: str
        required: True
      port:
        description:
        - It is the global credential http read's port.
        type: int
        required: True
      secure:
        description:
        - It is the global credential http read's secure.
        type: bool
      username:
        description:
        - It is the global credential http read's username.
        type: str
        required: True

  comments:
    description:
    - HTTPReadCredentialDTO's comments.
    type: str
  credentialType:
    description:
    - HTTPReadCredentialDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - HTTPReadCredentialDTO's description.
    type: str
  id:
    description:
    - HTTPReadCredentialDTO's id.
    type: str
  instanceTenantId:
    description:
    - HTTPReadCredentialDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - HTTPReadCredentialDTO's instanceUuid.
    type: str
  password:
    description:
    - HTTPReadCredentialDTO's password.
    - Required for state update.
    type: str
  port:
    description:
    - HTTPReadCredentialDTO's port.
    - Required for state update.
    type: int
  secure:
    description:
    - HTTPReadCredentialDTO's secure.
    type: bool
  username:
    description:
    - HTTPReadCredentialDTO's username.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_http_read
# Reference by Internet resource
- name: GlobalCredentialHttpRead reference
  description: Complete reference of the GlobalCredentialHttpRead object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialHttpRead reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_http_read_credentials
  cisco.dnac.global_credential_http_read:
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
  
- name: update_http_read_credential
  cisco.dnac.global_credential_http_read:
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
create_http_read_credentials:
    description: Adds HTTP read credentials.
    returned: success
    type: dict
    contains:
    response:
      description: HTTPReadCredentialDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the global credential http read's taskId.
          returned: success
          type: dict
        url:
          description: It is the global credential http read's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: HTTPReadCredentialDTO's version.
      returned: success
      type: str
      sample: '1.0'

update_http_read_credential:
    description: Updates global HTTP Read credential.
    returned: changed
    type: dict
    contains:
    response:
      description: HTTPReadCredentialDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the global credential http read's taskId.
          returned: changed
          type: dict
        url:
          description: It is the global credential http read's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: HTTPReadCredentialDTO's version.
      returned: changed
      type: str
      sample: '1.0'

"""

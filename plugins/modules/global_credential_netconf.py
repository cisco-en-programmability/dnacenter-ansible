#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credential_netconf
short_description: Manage GlobalCredentialNetconf objects of Discovery
description:
- Adds global netconf credentials.
- Updates global netconf credentials.
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
        - It is the global credential netconf's comments.
        type: str
      credentialType:
        description:
        - It is the global credential netconf's credentialType.
        type: str
      description:
        description:
        - It is the global credential netconf's description.
        type: str
      id:
        description:
        - It is the global credential netconf's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential netconf's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential netconf's instanceUuid.
        type: str
      netconfPort:
        description:
        - It is the global credential netconf's netconfPort.
        type: str
        required: True

  comments:
    description:
    - NetconfCredentialDTO's comments.
    type: str
  credentialType:
    description:
    - NetconfCredentialDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - NetconfCredentialDTO's description.
    type: str
  id:
    description:
    - NetconfCredentialDTO's id.
    type: str
  instanceTenantId:
    description:
    - NetconfCredentialDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - NetconfCredentialDTO's instanceUuid.
    type: str
  netconfPort:
    description:
    - NetconfCredentialDTO's netconfPort.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_netconf
# Reference by Internet resource
- name: GlobalCredentialNetconf reference
  description: Complete reference of the GlobalCredentialNetconf object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialNetconf reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_netconf_credentials
  cisco.dnac.global_credential_netconf:
    state: create  # required
    payload:  # required
    - netconfPort: SomeValue  # string, required
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string

- name: update_netconf_credentials
  cisco.dnac.global_credential_netconf:
    state: update  # required
    netconfPort: SomeValue  # string, required
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
  sample: discovery.create_netconf_credentials
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credential_snmpv3
short_description: Manage GlobalCredentialSnmpv3 objects of Discovery
description:
- Adds global SNMPv3 credentials.
- Updates global SNMPv3 credential.
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
      authPassword:
        description:
        - It is the global credential snmpv3's authPassword.
        type: str
      authType:
        description:
        - It is the global credential snmpv3's authType.
        type: str
      comments:
        description:
        - It is the global credential snmpv3's comments.
        type: str
      credentialType:
        description:
        - It is the global credential snmpv3's credentialType.
        type: str
      description:
        description:
        - It is the global credential snmpv3's description.
        type: str
      id:
        description:
        - It is the global credential snmpv3's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential snmpv3's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential snmpv3's instanceUuid.
        type: str
      privacyPassword:
        description:
        - It is the global credential snmpv3's privacyPassword.
        type: str
      privacyType:
        description:
        - It is the global credential snmpv3's privacyType.
        type: str
      snmpMode:
        description:
        - It is the global credential snmpv3's snmpMode.
        type: str
        required: True
      username:
        description:
        - It is the global credential snmpv3's username.
        type: str
        required: True

  authPassword:
    description:
    - SNMPv3CredentialDTO's authPassword.
    type: str
  authType:
    description:
    - SNMPv3CredentialDTO's authType.
    - Available values are 'SHA' and 'MD5'.
    type: str
  comments:
    description:
    - SNMPv3CredentialDTO's comments.
    type: str
  credentialType:
    description:
    - SNMPv3CredentialDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - SNMPv3CredentialDTO's description.
    type: str
  id:
    description:
    - SNMPv3CredentialDTO's id.
    type: str
  instanceTenantId:
    description:
    - SNMPv3CredentialDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - SNMPv3CredentialDTO's instanceUuid.
    type: str
  privacyPassword:
    description:
    - SNMPv3CredentialDTO's privacyPassword.
    type: str
  privacyType:
    description:
    - SNMPv3CredentialDTO's privacyType.
    - Available values are 'DES' and 'AES128'.
    type: str
  snmpMode:
    description:
    - SNMPv3CredentialDTO's snmpMode.
    - Available values are 'AUTHPRIV', 'AUTHNOPRIV' and 'NOAUTHNOPRIV'.
    - Required for state update.
    type: str
  username:
    description:
    - SNMPv3CredentialDTO's username.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv3
# Reference by Internet resource
- name: GlobalCredentialSnmpv3 reference
  description: Complete reference of the GlobalCredentialSnmpv3 object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialSnmpv3 reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_snmpv3_credentials
  cisco.dnac.global_credential_snmpv3:
    state: create  # required
    payload:  # required
    - snmpMode: SomeValue  # string, required
      username: SomeValue  # string, required
      authPassword: SomeValue  # string
      authType: SomeValue  # string
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      privacyPassword: SomeValue  # string
      privacyType: SomeValue  # string

- name: update_snmpv3_credentials
  cisco.dnac.global_credential_snmpv3:
    state: update  # required
    snmpMode: SomeValue  # string, required, valid values: 'AUTHPRIV', 'AUTHNOPRIV', 'NOAUTHNOPRIV'.
    username: SomeValue  # string, required
    authPassword: SomeValue  # string
    authType: SomeValue  # string, valid values: 'SHA', 'MD5'.
    comments: SomeValue  # string
    credentialType: SomeValue  # string, valid values: 'GLOBAL', 'APP'.
    description: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    instanceUuid: SomeValue  # string
    privacyPassword: SomeValue  # string
    privacyType: SomeValue  # string, valid values: 'DES', 'AES128'.

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
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: array
  sample:
"""

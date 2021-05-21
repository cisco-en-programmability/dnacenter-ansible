#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: global_credential_snmpv2_read_community
short_description: Manage GlobalCredentialSnmpv2ReadCommunity objects of Discovery
description:
- Adds global SNMP read community.
- Updates global SNMP read community.
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
        - It is the global credential snmpv2 read community's comments.
        type: str
      credentialType:
        description:
        - It is the global credential snmpv2 read community's credentialType.
        type: str
      description:
        description:
        - It is the global credential snmpv2 read community's description.
        type: str
      id:
        description:
        - It is the global credential snmpv2 read community's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential snmpv2 read community's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential snmpv2 read community's instanceUuid.
        type: str
      readCommunity:
        description:
        - It is the global credential snmpv2 read community's readCommunity.
        type: str
        required: True

  comments:
    description:
    - SNMPv2ReadCommunityDTO's comments.
    type: str
  credentialType:
    description:
    - SNMPv2ReadCommunityDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - SNMPv2ReadCommunityDTO's description.
    type: str
  id:
    description:
    - SNMPv2ReadCommunityDTO's id.
    type: str
  instanceTenantId:
    description:
    - SNMPv2ReadCommunityDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - SNMPv2ReadCommunityDTO's instanceUuid.
    type: str
  readCommunity:
    description:
    - SNMPv2ReadCommunityDTO's readCommunity.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv2_read_community
# Reference by Internet resource
- name: GlobalCredentialSnmpv2ReadCommunity reference
  description: Complete reference of the GlobalCredentialSnmpv2ReadCommunity object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialSnmpv2ReadCommunity reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_snmp_read_community
  cisco.dnac.global_credential_snmpv2_read_community:
    state: create  # required
    payload:  # required
    - readCommunity: SomeValue  # string, required
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string

- name: update_snmp_read_community
  cisco.dnac.global_credential_snmpv2_read_community:
    state: update  # required
    readCommunity: SomeValue  # string, required
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
  sample: discovery.create_snmp_read_community
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

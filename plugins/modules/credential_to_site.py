#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: credential_to_site
short_description: Manage CredentialToSite objects of NetworkSettings
description:
- Assign Device Credential To Site.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site_id:
    description:
    - Site id to assign credential.
    type: str
    required: True
  cliId:
    description:
    - Cli Id, property of the request body.
    type: str
  httpRead:
    description:
    - Http Read, property of the request body.
    type: str
  httpWrite:
    description:
    - Http Write, property of the request body.
    type: str
  snmpV2ReadId:
    description:
    - Snmp V2 Read Id, property of the request body.
    type: str
  snmpV2WriteId:
    description:
    - Snmp V2 Write Id, property of the request body.
    type: str
  snmpV3Id:
    description:
    - Snmp V3 Id, property of the request body.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.credential_to_site
# Reference by Internet resource
- name: CredentialToSite reference
  description: Complete reference of the CredentialToSite object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: CredentialToSite reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: assign_credential_to_site
  cisco.dnac.credential_to_site:
    state: create  # required
    site_id: SomeValue  # string, required
    cliId: SomeValue  # string
    httpRead: SomeValue  # string
    httpWrite: SomeValue  # string
    snmpV2ReadId: SomeValue  # string
    snmpV2WriteId: SomeValue  # string
    snmpV3Id: SomeValue  # string

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
  type: list
  sample:
"""

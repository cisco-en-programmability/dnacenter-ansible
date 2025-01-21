#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: global_credential_info
short_description: Information module for Global Credential Info
description:
- This module represents an alias of the module global_credential_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  credentialSubType:
    description:
    - >
      CredentialSubType query parameter. Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY /
      SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF.
    type: str
  sortBy:
    description:
    - SortBy query parameter. Field to sort the results by. Sorts by 'instanceId' if no value is provided.
    type: str
  order:
    description:
    - Order query parameter. Order of sorting. 'asc' or 'des'.
    type: str
  id:
    description:
    - Id path parameter. Global Credential ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Discovery GetCredentialSubTypeByCredentialIdV1
  description: Complete reference of the GetCredentialSubTypeByCredentialIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-credential-sub-type-by-credential-id
- name: Cisco DNA Center documentation for Discovery GetGlobalCredentialsV1
  description: Complete reference of the GetGlobalCredentialsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-global-credentials
notes:
  - SDK Method used are
    discovery.Discovery.get_credential_sub_type_by_credential_id_v1,
    discovery.Discovery.get_global_credentials_v1,

  - Paths used are
    get /dna/intent/api/v1/global-credential,
    get /dna/intent/api/v1/global-credential/{id},
  - It should be noted that this module is an alias of global_credential_v1_info

"""

EXAMPLES = r"""
- name: Get all Global Credential Info
  cisco.dnac.global_credential_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    credentialSubType: string
    sortBy: string
    order: string
  register: result

- name: Get Global Credential Info by id
  cisco.dnac.global_credential_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "string",
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: snmpv2_read_community_credential
short_description: Resource module for Snmpv2 Read Community Credential
description:
- Manage operations create and update of the resource Snmpv2 Read Community Credential.
- Updates global SNMP read community.
- Adds global SNMP read community.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Comments to identify the credential.
    type: str
  credentialType:
    description: Credential type to identify the application that uses the credential.
    type: str
  description:
    description: Name/Description of the credential.
    type: str
  instanceUuid:
    description: Snmpv2 Read Community Credential's instanceUuid.
    type: str
  payload:
    description: Snmpv2 Read Community Credential's payload.
    suboptions:
      comments:
        description: Comments to identify the credential.
        type: str
      credentialType:
        description: Credential type to identify the application that uses the credential.
        type: str
      description:
        description: Name/Description of the credential.
        type: str
      readCommunity:
        description: SNMP read community.
        type: str
    type: list
  readCommunity:
    description: SNMP read community. NO!$DATA!$ for no value change.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function update_snmp_read_community used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.update_snmp_read_community

- name: SDK function create_snmp_read_community used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.create_snmp_read_community

notes:
  - Paths used: put /dna/intent/api/v1/global-credential/snmpv2-read-community,
    post /dna/intent/api/v1/global-credential/snmpv2-read-community
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.snmpv2_read_community_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    instanceUuid: string
    readCommunity: string

- name: Create
  cisco.dnac.snmpv2_read_community_credential:
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

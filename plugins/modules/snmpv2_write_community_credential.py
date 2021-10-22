#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: snmpv2_write_community_credential
short_description: Resource module for Snmpv2 Write Community Credential
description:
- Manage operations create and update of the resource Snmpv2 Write Community Credential.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Snmpv2 Write Community Credential's comments.
    type: str
  credentialType:
    description: Snmpv2 Write Community Credential's credentialType.
    type: str
  description:
    description: Snmpv2 Write Community Credential's description.
    type: str
  id:
    description: Snmpv2 Write Community Credential's id.
    type: str
  instanceTenantId:
    description: Snmpv2 Write Community Credential's instanceTenantId.
    type: str
  instanceUuid:
    description: Snmpv2 Write Community Credential's instanceUuid.
    type: str
  writeCommunity:
    description: Snmpv2 Write Community Credential's writeCommunity.
    type: str
requirements:
- dnacentersdk >= 2.3.1
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Snmpv2 Write Community Credential reference
  description: Complete reference of the Snmpv2 Write Community Credential object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.snmpv2_write_community_credential:
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
    id: string
    instanceTenantId: string
    instanceUuid: string
    writeCommunity: string

- name: Update all
  cisco.dnac.snmpv2_write_community_credential:
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
    id: string
    instanceTenantId: string
    instanceUuid: string
    writeCommunity: string

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

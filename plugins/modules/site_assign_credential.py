#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_assign_credential
short_description: Resource module for Site Assign Credential
description:
- Manage operation create of the resource Site Assign Credential.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  cliId:
    description: Site Assign Credential's cliId.
    type: str
  httpRead:
    description: Site Assign Credential's httpRead.
    type: str
  httpWrite:
    description: Site Assign Credential's httpWrite.
    type: str
  siteId:
    description: SiteId path parameter. Site id to assign credential.
    type: str
  snmpV2ReadId:
    description: Site Assign Credential's snmpV2ReadId.
    type: str
  snmpV2WriteId:
    description: Site Assign Credential's snmpV2WriteId.
    type: str
  snmpV3Id:
    description: Site Assign Credential's snmpV3Id.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Site Assign Credential reference
  description: Complete reference of the Site Assign Credential object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.site_assign_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    cliId: string
    httpRead: string
    httpWrite: string
    siteId: string
    snmpV2ReadId: string
    snmpV2WriteId: string
    snmpV3Id: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

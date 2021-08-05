#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_credential_create
short_description: Resource module for Device Credential Create
description:
- Manage operation create of the resource Device Credential Create.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  settings:
    description: Device Credential Create's settings.
    suboptions:
      cliCredential:
        description: Device Credential Create's cliCredential.
        suboptions:
          description:
            description: Device Credential Create's description.
            type: str
          enablePassword:
            description: Device Credential Create's enablePassword.
            type: str
          id:
            description: Device Credential Create's id.
            type: str
          password:
            description: Device Credential Create's password.
            type: str
          username:
            description: Device Credential Create's username.
            type: str
        type: dict
      httpsRead:
        description: Device Credential Create's httpsRead.
        suboptions:
          id:
            description: Device Credential Create's id.
            type: str
          name:
            description: Device Credential Create's name.
            type: str
          password:
            description: Device Credential Create's password.
            type: str
          port:
            description: Device Credential Create's port.
            type: str
          username:
            description: Device Credential Create's username.
            type: str
        type: dict
      httpsWrite:
        description: Device Credential Create's httpsWrite.
        suboptions:
          id:
            description: Device Credential Create's id.
            type: str
          name:
            description: Device Credential Create's name.
            type: str
          password:
            description: Device Credential Create's password.
            type: str
          port:
            description: Device Credential Create's port.
            type: str
          username:
            description: Device Credential Create's username.
            type: str
        type: dict
      snmpV2cRead:
        description: Device Credential Create's snmpV2cRead.
        suboptions:
          description:
            description: Device Credential Create's description.
            type: str
          id:
            description: Device Credential Create's id.
            type: str
          readCommunity:
            description: Device Credential Create's readCommunity.
            type: str
        type: dict
      snmpV2cWrite:
        description: Device Credential Create's snmpV2cWrite.
        suboptions:
          description:
            description: Device Credential Create's description.
            type: str
          id:
            description: Device Credential Create's id.
            type: str
          writeCommunity:
            description: Device Credential Create's writeCommunity.
            type: str
        type: dict
      snmpV3:
        description: Device Credential Create's snmpV3.
        suboptions:
          authPassword:
            description: Device Credential Create's authPassword.
            type: str
          authType:
            description: Device Credential Create's authType.
            type: str
          description:
            description: Device Credential Create's description.
            type: str
          id:
            description: Device Credential Create's id.
            type: str
          privacyPassword:
            description: Device Credential Create's privacyPassword.
            type: str
          privacyType:
            description: Device Credential Create's privacyType.
            type: str
          snmpMode:
            description: Device Credential Create's snmpMode.
            type: str
          username:
            description: Device Credential Create's username.
            type: str
        type: dict
    type: dict
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Device Credential Create reference
  description: Complete reference of the Device Credential Create object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.device_credential_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      cliCredential:
        description: string
        enablePassword: string
        id: string
        password: string
        username: string
      httpsRead:
        id: string
        name: string
        password: string
        port: string
        username: string
      httpsWrite:
        id: string
        name: string
        password: string
        port: string
        username: string
      snmpV2cRead:
        description: string
        id: string
        readCommunity: string
      snmpV2cWrite:
        description: string
        id: string
        writeCommunity: string
      snmpV3:
        authPassword: string
        authType: string
        description: string
        id: string
        privacyPassword: string
        privacyType: string
        snmpMode: string
        username: string

- name: Create
  cisco.dnac.device_credential_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      cliCredential:
      - description: string
        enablePassword: string
        password: string
        username: string
      httpsRead:
      - name: string
        password: string
        port: 0
        username: string
      httpsWrite:
      - name: string
        password: string
        port: 0
        username: string
      snmpV2cRead:
      - description: string
        readCommunity: string
      snmpV2cWrite:
      - description: string
        writeCommunity: string
      snmpV3:
      - authPassword: string
        authType: string
        description: string
        privacyPassword: string
        privacyType: string
        snmpMode: string
        username: string

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

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_credential
short_description: Manage DeviceCredential objects of NetworkSettings
description:
- API to get device credential details.
- API to create device credentials.
- API to update device credentials.
- Delete device credential.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site_id:
    description:
    - Site id to retrieve the credential details associated with the site.
    type: str
  settings:
    description:
    - Settings, property of the request body.
    type: dict
    required: True
    suboptions:
      cliCredential:
        description:
        - It is the device credential's cliCredential.
        - Type list for state create.
        - Type dict for state update.
        type: raw
      httpsRead:
        description:
        - It is the device credential's httpsRead.
        - Type list for state create.
        - Type dict for state update.
        type: raw
      httpsWrite:
        description:
        - It is the device credential's httpsWrite.
        - Type list for state create.
        - Type dict for state update.
        type: raw
      snmpV2cRead:
        description:
        - It is the device credential's snmpV2cRead.
        - Type list for state create.
        - Type dict for state update.
        type: raw
      snmpV2cWrite:
        description:
        - It is the device credential's snmpV2cWrite.
        - Type list for state create.
        - Type dict for state update.
        type: raw
      snmpV3:
        description:
        - It is the device credential's snmpV3.
        - Type list for state create.
        - Type dict for state update.
        type: raw

  id:
    description:
    - Global credential id.
    - Required for state delete.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_credential
# Reference by Internet resource
- name: DeviceCredential reference
  description: Complete reference of the DeviceCredential object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceCredential reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_credential_details
  cisco.dnac.device_credential:
    state: query  # required
    site_id: SomeValue  # string
  register: query_result

- name: create_device_credentials
  cisco.dnac.device_credential:
    state: create  # required
    settings:  # required
      cliCredential:
      - description: SomeValue  # string, required
        username: SomeValue  # string, required
        password: SomeValue  # string, required
        enablePassword: SomeValue  # string
      snmpV2cRead:
      - readCommunity: SomeValue  # string, required
        description: SomeValue  # string
      snmpV2cWrite:
      - writeCommunity: SomeValue  # string, required
        description: SomeValue  # string
      snmpV3:
      - description: SomeValue  # string, required
        username: SomeValue  # string, required
        privacyType: SomeValue  # string, required
        privacyPassword: SomeValue  # string, required
        authType: SomeValue  # string, required
        snmpMode: SomeValue  # string, required
        authPassword: SomeValue  # string
      httpsRead:
      - username: SomeValue  # string, required
        password: SomeValue  # string, required
        name: SomeValue  # string
        port: 1  #  number
      httpsWrite:
      - username: SomeValue  # string, required
        password: SomeValue  # string, required
        name: SomeValue  # string
        port: 1  #  number

- name: update_device_credentials
  cisco.dnac.device_credential:
    state: update  # required
    settings:  # required
      cliCredential:
        description: SomeValue  # string
        username: SomeValue  # string
        password: SomeValue  # string
        enablePassword: SomeValue  # string
        id: SomeValue  # string
      snmpV2cRead:
        description: SomeValue  # string
        readCommunity: SomeValue  # string
        id: SomeValue  # string
      snmpV2cWrite:
        description: SomeValue  # string
        writeCommunity: SomeValue  # string
        id: SomeValue  # string
      snmpV3:
        authPassword: SomeValue  # string
        authType: SomeValue  # string
        snmpMode: SomeValue  # string
        privacyPassword: SomeValue  # string
        privacyType: SomeValue  # string
        username: SomeValue  # string
        description: SomeValue  # string
        id: SomeValue  # string
      httpsRead:
        name: SomeValue  # string
        username: SomeValue  # string
        password: SomeValue  # string
        port: SomeValue  # string
        id: SomeValue  # string
      httpsWrite:
        name: SomeValue  # string
        username: SomeValue  # string
        password: SomeValue  # string
        port: SomeValue  # string
        id: SomeValue  # string

- name: delete_device_credential
  cisco.dnac.device_credential:
    state: delete  # required
    id: SomeValue  # string, required

"""

RETURN = """
"""

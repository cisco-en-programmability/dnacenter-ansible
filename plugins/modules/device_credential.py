#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: device_credential
short_description: Manage DeviceCredential objects of NetworkSettings
description:
- API to get device credential details.
- API to create device credentials.
- API to update device credentials.
- Delete device credential.
version_added: '1.0'
author: first last (@GitHubID)
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
get_device_credential_details:
    description: API to get device credential details.
    returned: always
    type: dict
    contains:
    snmp_v3:
      description: Snmp V3, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        username:
          description: It is the device credential's username.
          returned: always
          type: str
          sample: 'devnetuser'
        authPassword:
          description: It is the device credential's authPassword.
          returned: always
          type: str
          sample: '<authpassword>'
        authType:
          description: It is the device credential's authType.
          returned: always
          type: str
          sample: '<authtype>'
        privacyPassword:
          description: It is the device credential's privacyPassword.
          returned: always
          type: str
          sample: '<privacypassword>'
        privacyType:
          description: It is the device credential's privacyType.
          returned: always
          type: str
          sample: '<privacytype>'
        snmpMode:
          description: It is the device credential's snmpMode.
          returned: always
          type: str
          sample: '<snmpmode>'
        comments:
          description: It is the device credential's comments.
          returned: always
          type: str
          sample: '<comments>'
        description:
          description: It is the device credential's description.
          returned: always
          type: str
          sample: '<description>'
        credentialType:
          description: It is the device credential's credentialType.
          returned: always
          type: str
          sample: '<credentialtype>'
        instanceUuid:
          description: It is the device credential's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        instanceTenantId:
          description: It is the device credential's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the device credential's id.
          returned: always
          type: str
          sample: '478012'

    http_read:
      description: Http Read, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        secure:
          description: It is the device credential's secure.
          returned: always
          type: str
          sample: '<secure>'
        username:
          description: It is the device credential's username.
          returned: always
          type: str
          sample: 'devnetuser'
        password:
          description: It is the device credential's password.
          returned: always
          type: str
          sample: '*******'
        port:
          description: It is the device credential's port.
          returned: always
          type: str
          sample: '<port>'
        comments:
          description: It is the device credential's comments.
          returned: always
          type: str
          sample: '<comments>'
        description:
          description: It is the device credential's description.
          returned: always
          type: str
          sample: '<description>'
        credentialType:
          description: It is the device credential's credentialType.
          returned: always
          type: str
          sample: '<credentialtype>'
        instanceUuid:
          description: It is the device credential's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        instanceTenantId:
          description: It is the device credential's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the device credential's id.
          returned: always
          type: str
          sample: '478012'

    http_write:
      description: Http Write, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        secure:
          description: It is the device credential's secure.
          returned: always
          type: str
          sample: '<secure>'
        username:
          description: It is the device credential's username.
          returned: always
          type: str
          sample: 'devnetuser'
        password:
          description: It is the device credential's password.
          returned: always
          type: str
          sample: '*******'
        port:
          description: It is the device credential's port.
          returned: always
          type: str
          sample: '<port>'
        comments:
          description: It is the device credential's comments.
          returned: always
          type: str
          sample: '<comments>'
        description:
          description: It is the device credential's description.
          returned: always
          type: str
          sample: '<description>'
        credentialType:
          description: It is the device credential's credentialType.
          returned: always
          type: str
          sample: '<credentialtype>'
        instanceUuid:
          description: It is the device credential's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        instanceTenantId:
          description: It is the device credential's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the device credential's id.
          returned: always
          type: str
          sample: '478012'

    snmp_v2_write:
      description: Snmp V2 Write, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        writeCommunity:
          description: It is the device credential's writeCommunity.
          returned: always
          type: str
          sample: '<writecommunity>'
        comments:
          description: It is the device credential's comments.
          returned: always
          type: str
          sample: '<comments>'
        description:
          description: It is the device credential's description.
          returned: always
          type: str
          sample: '<description>'
        credentialType:
          description: It is the device credential's credentialType.
          returned: always
          type: str
          sample: '<credentialtype>'
        instanceUuid:
          description: It is the device credential's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        instanceTenantId:
          description: It is the device credential's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the device credential's id.
          returned: always
          type: str
          sample: '478012'

    snmp_v2_read:
      description: Snmp V2 Read, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        readCommunity:
          description: It is the device credential's readCommunity.
          returned: always
          type: str
          sample: '<readcommunity>'
        comments:
          description: It is the device credential's comments.
          returned: always
          type: str
          sample: '<comments>'
        description:
          description: It is the device credential's description.
          returned: always
          type: str
          sample: '<description>'
        credentialType:
          description: It is the device credential's credentialType.
          returned: always
          type: str
          sample: '<credentialtype>'
        instanceUuid:
          description: It is the device credential's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        instanceTenantId:
          description: It is the device credential's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the device credential's id.
          returned: always
          type: str
          sample: '478012'

    cli:
      description: Cli, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        username:
          description: It is the device credential's username.
          returned: always
          type: str
          sample: 'devnetuser'
        enablePassword:
          description: It is the device credential's enablePassword.
          returned: always
          type: str
          sample: '<enablepassword>'
        password:
          description: It is the device credential's password.
          returned: always
          type: str
          sample: '*******'
        comments:
          description: It is the device credential's comments.
          returned: always
          type: str
          sample: '<comments>'
        description:
          description: It is the device credential's description.
          returned: always
          type: str
          sample: '<description>'
        credentialType:
          description: It is the device credential's credentialType.
          returned: always
          type: str
          sample: '<credentialtype>'
        instanceUuid:
          description: It is the device credential's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        instanceTenantId:
          description: It is the device credential's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the device credential's id.
          returned: always
          type: str
          sample: '478012'


create_device_credentials:
    description: API to create device credentials.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

update_device_credentials:
    description: API to update device credentials.
    returned: changed
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: changed
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: changed
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: changed
      type: str
      sample: '<message>'

delete_device_credential:
    description: Delete device credential.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

"""

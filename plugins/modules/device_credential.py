#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
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
                type: list
                elements: dict
                suboptions:
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                        required: True
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                        required: True
                    password:
                        description:
                        - It is the device credential's password.
                        type: str
                        required: True
                    enablePassword:
                        description:
                        - It is the device credential's enablePassword.
                        type: str

            snmpV2cRead:
                description:
                - It is the device credential's snmpV2cRead.
                type: list
                elements: dict
                suboptions:
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                    readCommunity:
                        description:
                        - It is the device credential's readCommunity.
                        type: str
                        required: True

            snmpV2cWrite:
                description:
                - It is the device credential's snmpV2cWrite.
                type: list
                elements: dict
                suboptions:
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                    writeCommunity:
                        description:
                        - It is the device credential's writeCommunity.
                        type: str
                        required: True

            snmpV3:
                description:
                - It is the device credential's snmpV3.
                type: list
                elements: dict
                suboptions:
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                        required: True
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                        required: True
                    privacyType:
                        description:
                        - It is the device credential's privacyType.
                        type: str
                        required: True
                    privacyPassword:
                        description:
                        - It is the device credential's privacyPassword.
                        type: str
                        required: True
                    authType:
                        description:
                        - It is the device credential's authType.
                        type: str
                        required: True
                    authPassword:
                        description:
                        - It is the device credential's authPassword.
                        type: str
                    snmpMode:
                        description:
                        - It is the device credential's snmpMode.
                        type: str
                        required: True

            httpsRead:
                description:
                - It is the device credential's httpsRead.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                        - It is the device credential's name.
                        type: str
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                        required: True
                    password:
                        description:
                        - It is the device credential's password.
                        type: str
                        required: True
                    port:
                        description:
                        - It is the device credential's port.
                        type: int

            httpsWrite:
                description:
                - It is the device credential's httpsWrite.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                        - It is the device credential's name.
                        type: str
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                        required: True
                    password:
                        description:
                        - It is the device credential's password.
                        type: str
                        required: True
                    port:
                        description:
                        - It is the device credential's port.
                        type: int


    settings:
        description:
        - Settings, property of the request body.
        type: dict
        required: True
        suboptions:
            cliCredential:
                description:
                - It is the device credential's cliCredential.
                type: dict
                suboptions:
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                    password:
                        description:
                        - It is the device credential's password.
                        type: str
                    enablePassword:
                        description:
                        - It is the device credential's enablePassword.
                        type: str
                    id:
                        description:
                        - It is the device credential's id.
                        type: str

            snmpV2cRead:
                description:
                - It is the device credential's snmpV2cRead.
                type: dict
                suboptions:
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                    readCommunity:
                        description:
                        - It is the device credential's readCommunity.
                        type: str
                    id:
                        description:
                        - It is the device credential's id.
                        type: str

            snmpV2cWrite:
                description:
                - It is the device credential's snmpV2cWrite.
                type: dict
                suboptions:
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                    writeCommunity:
                        description:
                        - It is the device credential's writeCommunity.
                        type: str
                    id:
                        description:
                        - It is the device credential's id.
                        type: str

            snmpV3:
                description:
                - It is the device credential's snmpV3.
                type: dict
                suboptions:
                    authPassword:
                        description:
                        - It is the device credential's authPassword.
                        type: str
                    authType:
                        description:
                        - It is the device credential's authType.
                        type: str
                    snmpMode:
                        description:
                        - It is the device credential's snmpMode.
                        type: str
                    privacyPassword:
                        description:
                        - It is the device credential's privacyPassword.
                        type: str
                    privacyType:
                        description:
                        - It is the device credential's privacyType.
                        type: str
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                    description:
                        description:
                        - It is the device credential's description.
                        type: str
                    id:
                        description:
                        - It is the device credential's id.
                        type: str

            httpsRead:
                description:
                - It is the device credential's httpsRead.
                type: dict
                suboptions:
                    name:
                        description:
                        - It is the device credential's name.
                        type: str
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                    password:
                        description:
                        - It is the device credential's password.
                        type: str
                    port:
                        description:
                        - It is the device credential's port.
                        type: str
                    id:
                        description:
                        - It is the device credential's id.
                        type: str

            httpsWrite:
                description:
                - It is the device credential's httpsWrite.
                type: dict
                suboptions:
                    name:
                        description:
                        - It is the device credential's name.
                        type: str
                    username:
                        description:
                        - It is the device credential's username.
                        type: str
                    password:
                        description:
                        - It is the device credential's password.
                        type: str
                    port:
                        description:
                        - It is the device credential's port.
                        type: str
                    id:
                        description:
                        - It is the device credential's id.
                        type: str


    id:
        description:
        - Global credential id.
        type: str
        required: True

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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: API to get device credential details.
    returned: success,changed,always
    type: dict
    contains:
        snmp_v3:
            description: Snmp V3, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                username:
                    description: It is the device credential's username.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authPassword:
                    description: It is the device credential's authPassword.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authType:
                    description: It is the device credential's authType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                privacyPassword:
                    description: It is the device credential's privacyPassword.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                privacyType:
                    description: It is the device credential's privacyType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpMode:
                    description: It is the device credential's snmpMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        http_read:
            description: Http Read, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                secure:
                    description: It is the device credential's secure.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                username:
                    description: It is the device credential's username.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                password:
                    description: It is the device credential's password.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                port:
                    description: It is the device credential's port.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        http_write:
            description: Http Write, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                secure:
                    description: It is the device credential's secure.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                username:
                    description: It is the device credential's username.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                password:
                    description: It is the device credential's password.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                port:
                    description: It is the device credential's port.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        snmp_v2_write:
            description: Snmp V2 Write, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                writeCommunity:
                    description: It is the device credential's writeCommunity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        snmp_v2_read:
            description: Snmp V2 Read, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                readCommunity:
                    description: It is the device credential's readCommunity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        cli:
            description: Cli, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                username:
                    description: It is the device credential's username.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enablePassword:
                    description: It is the device credential's enablePassword.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                password:
                    description: It is the device credential's password.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


data_1:
    description: API to create device credentials.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: API to update device credentials.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Delete device credential.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.device_credential import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.exec("post")

    elif state == "update":
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
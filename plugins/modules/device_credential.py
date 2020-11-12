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
"""

EXAMPLES = r"""
"""

RETURN = r"""
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
                    sample: 'devnetuser'
                authPassword:
                    description: It is the device credential's authPassword.
                    returned: success,changed,always
                    type: str
                    sample: '<authpassword>'
                authType:
                    description: It is the device credential's authType.
                    returned: success,changed,always
                    type: str
                    sample: '<authtype>'
                privacyPassword:
                    description: It is the device credential's privacyPassword.
                    returned: success,changed,always
                    type: str
                    sample: '<privacypassword>'
                privacyType:
                    description: It is the device credential's privacyType.
                    returned: success,changed,always
                    type: str
                    sample: '<privacytype>'
                snmpMode:
                    description: It is the device credential's snmpMode.
                    returned: success,changed,always
                    type: str
                    sample: '<snmpmode>'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: '<comments>'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: '<credentialtype>'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

        http_read:
            description: Http Read, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                secure:
                    description: It is the device credential's secure.
                    returned: success,changed,always
                    type: str
                    sample: '<secure>'
                username:
                    description: It is the device credential's username.
                    returned: success,changed,always
                    type: str
                    sample: 'devnetuser'
                password:
                    description: It is the device credential's password.
                    returned: success,changed,always
                    type: str
                    sample: '*******'
                port:
                    description: It is the device credential's port.
                    returned: success,changed,always
                    type: str
                    sample: '<port>'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: '<comments>'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: '<credentialtype>'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

        http_write:
            description: Http Write, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                secure:
                    description: It is the device credential's secure.
                    returned: success,changed,always
                    type: str
                    sample: '<secure>'
                username:
                    description: It is the device credential's username.
                    returned: success,changed,always
                    type: str
                    sample: 'devnetuser'
                password:
                    description: It is the device credential's password.
                    returned: success,changed,always
                    type: str
                    sample: '*******'
                port:
                    description: It is the device credential's port.
                    returned: success,changed,always
                    type: str
                    sample: '<port>'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: '<comments>'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: '<credentialtype>'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

        snmp_v2_write:
            description: Snmp V2 Write, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                writeCommunity:
                    description: It is the device credential's writeCommunity.
                    returned: success,changed,always
                    type: str
                    sample: '<writecommunity>'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: '<comments>'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: '<credentialtype>'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

        snmp_v2_read:
            description: Snmp V2 Read, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                readCommunity:
                    description: It is the device credential's readCommunity.
                    returned: success,changed,always
                    type: str
                    sample: '<readcommunity>'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: '<comments>'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: '<credentialtype>'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

        cli:
            description: Cli, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                username:
                    description: It is the device credential's username.
                    returned: success,changed,always
                    type: str
                    sample: 'devnetuser'
                enablePassword:
                    description: It is the device credential's enablePassword.
                    returned: success,changed,always
                    type: str
                    sample: '<enablepassword>'
                password:
                    description: It is the device credential's password.
                    returned: success,changed,always
                    type: str
                    sample: '*******'
                comments:
                    description: It is the device credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: '<comments>'
                description:
                    description: It is the device credential's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                credentialType:
                    description: It is the device credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: '<credentialtype>'
                instanceUuid:
                    description: It is the device credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                instanceTenantId:
                    description: It is the device credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                id:
                    description: It is the device credential's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'


data_1:
    description: API to create device credentials.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionstatusurl>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

data_2:
    description: API to update device credentials.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionstatusurl>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

data_3:
    description: Delete device credential.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionstatusurl>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.device_credential import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()

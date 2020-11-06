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
module: pnp_settings
short_description: Manage PnpSettings objects of DeviceOnboardingPnp
description:
- Returns global PnP settings of the user.
- Updates the user's list of global PnP settings.
version_added: '1.0'
author: first last (@GitHubID)
options:
    _id:
        description:
        - Settings's _id.
        type: str
    aaaCredentials:
        description:
        - Settings's aaaCredentials.
        type: dict
        suboptions:
            password:
                description:
                - It is the pnp settings's password.
                type: str
            username:
                description:
                - It is the pnp settings's username.
                type: str

    acceptEula:
        description:
        - Settings's acceptEula.
        type: bool
    defaultProfile:
        description:
        - Settings's defaultProfile.
        type: dict
        suboptions:
            cert:
                description:
                - It is the pnp settings's cert.
                type: str
            fqdnAddresses:
                description:
                - It is the pnp settings's fqdnAddresses.
                type: list
            ipAddresses:
                description:
                - It is the pnp settings's ipAddresses.
                type: list
            port:
                description:
                - It is the pnp settings's port.
                type: int
            proxy:
                description:
                - It is the pnp settings's proxy.
                type: bool

    savaMappingList:
        description:
        - Settings's savaMappingList (list of objects).
        type: list
        elements: dict
        suboptions:
            autoSyncPeriod:
                description:
                - It is the pnp settings's autoSyncPeriod.
                type: int
            ccoUser:
                description:
                - It is the pnp settings's ccoUser.
                type: str
            expiry:
                description:
                - It is the pnp settings's expiry.
                type: int
            lastSync:
                description:
                - It is the pnp settings's lastSync.
                type: int
            profile:
                description:
                - It is the pnp settings's profile.
                type: dict
                required: True
                suboptions:
                    addressFqdn:
                        description:
                        - It is the pnp settings's addressFqdn.
                        type: str
                    addressIpV4:
                        description:
                        - It is the pnp settings's addressIpV4.
                        type: str
                    cert:
                        description:
                        - It is the pnp settings's cert.
                        type: str
                    makeDefault:
                        description:
                        - It is the pnp settings's makeDefault.
                        type: bool
                    name:
                        description:
                        - It is the pnp settings's name.
                        type: str
                    port:
                        description:
                        - It is the pnp settings's port.
                        type: int
                    profileId:
                        description:
                        - It is the pnp settings's profileId.
                        type: str
                    proxy:
                        description:
                        - It is the pnp settings's proxy.
                        type: bool

            smartAccountId:
                description:
                - It is the pnp settings's smartAccountId.
                type: str
                required: True
            syncResult:
                description:
                - It is the pnp settings's syncResult.
                type: dict
                suboptions:
                    syncList:
                        description:
                        - It is the pnp settings's syncList.
                        type: list
                        elements: dict
                        suboptions:
                            deviceSnList:
                                description:
                                - It is the pnp settings's deviceSnList.
                                type: list
                            syncType:
                                description:
                                - It is the pnp settings's syncType.
                                type: str

                    syncMsg:
                        description:
                        - It is the pnp settings's syncMsg.
                        type: str

            syncResultStr:
                description:
                - It is the pnp settings's syncResultStr.
                type: str
            syncStartTime:
                description:
                - It is the pnp settings's syncStartTime.
                type: int
            syncStatus:
                description:
                - It is the pnp settings's syncStatus.
                type: str
                required: True
            tenantId:
                description:
                - It is the pnp settings's tenantId.
                type: str
            token:
                description:
                - It is the pnp settings's token.
                type: str
            virtualAccountId:
                description:
                - It is the pnp settings's virtualAccountId.
                type: str
                required: True

    taskTimeOuts:
        description:
        - Settings's taskTimeOuts.
        type: dict
        suboptions:
            configTimeOut:
                description:
                - It is the pnp settings's configTimeOut.
                type: int
            generalTimeOut:
                description:
                - It is the pnp settings's generalTimeOut.
                type: int
            imageDownloadTimeOut:
                description:
                - It is the pnp settings's imageDownloadTimeOut.
                type: int

    tenantId:
        description:
        - Settings's tenantId.
        type: str
    version:
        description:
        - Settings's version.
        type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_settings
# Reference by Internet resource
- name: PnpSettings reference
  description: Complete reference of the PnpSettings object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpSettings reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns global PnP settings of the user.
    returned: success,changed,always
    type: dict
    contains:
        savaMappingList:
            description: Sava Mapping List, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                syncStatus:
                    description: It is the pnp settings's syncStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                syncStartTime:
                    description: It is the pnp settings's syncStartTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                syncResult:
                    description: It is the pnp settings's syncResult.
                    returned: success,changed,always
                    type: dict
                    contains:
                        syncList:
                            description: It is the pnp settings's syncList.
                            returned: success,changed,always
                            type: list
                            contains:
                                syncType:
                                    description: It is the pnp settings's syncType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                deviceSnList:
                                    description: It is the pnp settings's deviceSnList.
                                    returned: success,changed,always
                                    type: list

                        syncMsg:
                            description: It is the pnp settings's syncMsg.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastSync:
                    description: It is the pnp settings's lastSync.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp settings's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                profile:
                    description: It is the pnp settings's profile.
                    returned: success,changed,always
                    type: dict
                    contains:
                        port:
                            description: It is the pnp settings's port.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addressIpV4:
                            description: It is the pnp settings's addressIpV4.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        addressFqdn:
                            description: It is the pnp settings's addressFqdn.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        profileId:
                            description: It is the pnp settings's profileId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        proxy:
                            description: It is the pnp settings's proxy.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        makeDefault:
                            description: It is the pnp settings's makeDefault.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        cert:
                            description: It is the pnp settings's cert.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the pnp settings's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                token:
                    description: It is the pnp settings's token.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                expiry:
                    description: It is the pnp settings's expiry.
                    returned: success,changed,always
                    type: int
                    sample: 0
                ccoUser:
                    description: It is the pnp settings's ccoUser.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                smartAccountId:
                    description: It is the pnp settings's smartAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                virtualAccountId:
                    description: It is the pnp settings's virtualAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                autoSyncPeriod:
                    description: It is the pnp settings's autoSyncPeriod.
                    returned: success,changed,always
                    type: int
                    sample: 0
                syncResultStr:
                    description: It is the pnp settings's syncResultStr.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        taskTimeOuts:
            description: Task Time Outs, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                imageDownloadTimeOut:
                    description: It is the pnp settings's imageDownloadTimeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0
                configTimeOut:
                    description: It is the pnp settings's configTimeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0
                generalTimeOut:
                    description: It is the pnp settings's generalTimeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0

        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        aaaCredentials:
            description: Aaa Credentials, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                password:
                    description: It is the pnp settings's password.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                username:
                    description: It is the pnp settings's username.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        defaultProfile:
            description: Default Profile, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                fqdnAddresses:
                    description: It is the pnp settings's fqdnAddresses.
                    returned: success,changed,always
                    type: list
                proxy:
                    description: It is the pnp settings's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                cert:
                    description: It is the pnp settings's cert.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipAddresses:
                    description: It is the pnp settings's ipAddresses.
                    returned: success,changed,always
                    type: list
                port:
                    description: It is the pnp settings's port.
                    returned: success,changed,always
                    type: int
                    sample: 0

        acceptEula:
            description: AcceptEula, property of the response body.
            returned: success,changed,always
            type: bool
            sample: false
        id:
            description: Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        _id:
            description: Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0

data_1:
    description: Updates the user's list of global PnP settings.
    returned: success,changed,always
    type: dict
    contains:
        savaMappingList:
            description: Settings's Sava Mapping List (list of objects).
            returned: success,changed,always
            type: list
            contains:
                syncStatus:
                    description: It is the pnp settings's syncStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                syncStartTime:
                    description: It is the pnp settings's syncStartTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                syncResult:
                    description: It is the pnp settings's syncResult.
                    returned: success,changed,always
                    type: dict
                    contains:
                        syncList:
                            description: It is the pnp settings's syncList.
                            returned: success,changed,always
                            type: list
                            contains:
                                syncType:
                                    description: It is the pnp settings's syncType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                deviceSnList:
                                    description: It is the pnp settings's deviceSnList.
                                    returned: success,changed,always
                                    type: list

                        syncMsg:
                            description: It is the pnp settings's syncMsg.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastSync:
                    description: It is the pnp settings's lastSync.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp settings's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                profile:
                    description: It is the pnp settings's profile.
                    returned: success,changed,always
                    type: dict
                    contains:
                        port:
                            description: It is the pnp settings's port.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addressIpV4:
                            description: It is the pnp settings's addressIpV4.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        addressFqdn:
                            description: It is the pnp settings's addressFqdn.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        profileId:
                            description: It is the pnp settings's profileId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        proxy:
                            description: It is the pnp settings's proxy.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        makeDefault:
                            description: It is the pnp settings's makeDefault.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        cert:
                            description: It is the pnp settings's cert.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the pnp settings's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                token:
                    description: It is the pnp settings's token.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                expiry:
                    description: It is the pnp settings's expiry.
                    returned: success,changed,always
                    type: int
                    sample: 0
                ccoUser:
                    description: It is the pnp settings's ccoUser.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                smartAccountId:
                    description: It is the pnp settings's smartAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                virtualAccountId:
                    description: It is the pnp settings's virtualAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                autoSyncPeriod:
                    description: It is the pnp settings's autoSyncPeriod.
                    returned: success,changed,always
                    type: int
                    sample: 0
                syncResultStr:
                    description: It is the pnp settings's syncResultStr.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        taskTimeOuts:
            description: Settings's Task Time Outs.
            returned: success,changed,always
            type: dict
            contains:
                imageDownloadTimeOut:
                    description: It is the pnp settings's imageDownloadTimeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0
                configTimeOut:
                    description: It is the pnp settings's configTimeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0
                generalTimeOut:
                    description: It is the pnp settings's generalTimeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0

        tenantId:
            description: Settings's Tenant Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        aaaCredentials:
            description: Settings's Aaa Credentials.
            returned: success,changed,always
            type: dict
            contains:
                password:
                    description: It is the pnp settings's password.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                username:
                    description: It is the pnp settings's username.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        defaultProfile:
            description: Settings's Default Profile.
            returned: success,changed,always
            type: dict
            contains:
                fqdnAddresses:
                    description: It is the pnp settings's fqdnAddresses.
                    returned: success,changed,always
                    type: list
                proxy:
                    description: It is the pnp settings's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                cert:
                    description: It is the pnp settings's cert.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipAddresses:
                    description: It is the pnp settings's ipAddresses.
                    returned: success,changed,always
                    type: list
                port:
                    description: It is the pnp settings's port.
                    returned: success,changed,always
                    type: int
                    sample: 0

        acceptEula:
            description: Settings's acceptEula.
            returned: success,changed,always
            type: bool
            sample: false
        id:
            description: Settings's Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        _id:
            description: Settings's Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        version:
            description: Settings's version.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_settings import module_definition


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

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
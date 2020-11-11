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
module: virtual_account_sync
short_description: Manage VirtualAccountSync objects of DeviceOnboardingPnp
description:
- Synchronizes the device info from the given smart account & virtual account with the PnP database. The response payload returns a list of synced devices.
- Returns the summary of devices synced from the given smart account & virtual account with PnP.
version_added: '1.0'
author: first last (@GitHubID)
options:
    autoSyncPeriod:
        description:
        - SAVAMapping's autoSyncPeriod.
        type: int
    ccoUser:
        description:
        - SAVAMapping's ccoUser.
        type: str
    expiry:
        description:
        - SAVAMapping's expiry.
        type: int
    lastSync:
        description:
        - SAVAMapping's lastSync.
        type: int
    profile:
        description:
        - SAVAMapping's profile.
        type: dict
        required: True
        suboptions:
            addressFqdn:
                description:
                - It is the virtual account sync's addressFqdn.
                type: str
            addressIpV4:
                description:
                - It is the virtual account sync's addressIpV4.
                type: str
            cert:
                description:
                - It is the virtual account sync's cert.
                type: str
            makeDefault:
                description:
                - It is the virtual account sync's makeDefault.
                type: bool
            name:
                description:
                - It is the virtual account sync's name.
                type: str
            port:
                description:
                - It is the virtual account sync's port.
                type: int
            profileId:
                description:
                - It is the virtual account sync's profileId.
                type: str
            proxy:
                description:
                - It is the virtual account sync's proxy.
                type: bool

    smartAccountId:
        description:
        - SAVAMapping's smartAccountId.
        type: str
        required: True
    syncResult:
        description:
        - SAVAMapping's syncResult.
        type: dict
        suboptions:
            syncList:
                description:
                - It is the virtual account sync's syncList.
                type: list
                elements: dict
                suboptions:
                    deviceSnList:
                        description:
                        - It is the virtual account sync's deviceSnList.
                        type: list
                    syncType:
                        description:
                        - It is the virtual account sync's syncType.
                        type: str

            syncMsg:
                description:
                - It is the virtual account sync's syncMsg.
                type: str

    syncResultStr:
        description:
        - SAVAMapping's syncResultStr.
        type: str
    syncStartTime:
        description:
        - SAVAMapping's syncStartTime.
        type: int
    syncStatus:
        description:
        - SAVAMapping's syncStatus.
        - Available values are 'NOT_SYNCED', 'SYNCING', 'SUCCESS' and 'FAILURE'.
        type: str
        required: True
    tenantId:
        description:
        - SAVAMapping's tenantId.
        type: str
    token:
        description:
        - SAVAMapping's token.
        type: str
    virtualAccountId:
        description:
        - SAVAMapping's virtualAccountId.
        type: str
        required: True
    domain:
        description:
        - Smart Account Domain.
        type: str
        required: True
    name:
        description:
        - Virtual Account Name.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.virtual_account_sync
# Reference by Internet resource
- name: VirtualAccountSync reference
  description: Complete reference of the VirtualAccountSync object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: VirtualAccountSync reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Synchronizes the device info from the given smart account & virtual account with the PnP database. The response payload returns a list of synced devices.
    returned: success,changed,always
    type: dict
    contains:
        virtualAccountId:
            description: SAVAMapping's Virtual Account Id.
            returned: success,changed,always
            type: str
            sample: '<virtualaccountid>'
        autoSyncPeriod:
            description: SAVAMapping's autoSyncPeriod.
            returned: success,changed,always
            type: int
            sample: 0
        syncResultStr:
            description: SAVAMapping's Sync Result Str.
            returned: success,changed,always
            type: str
            sample: '<syncresultstr>'
        profile:
            description: SAVAMapping's Profile.
            returned: success,changed,always
            type: dict
            contains:
                proxy:
                    description: It is the virtual account sync's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                makeDefault:
                    description: It is the virtual account sync's makeDefault.
                    returned: success,changed,always
                    type: bool
                    sample: false
                port:
                    description: It is the virtual account sync's port.
                    returned: success,changed,always
                    type: int
                    sample: 0
                profileId:
                    description: It is the virtual account sync's profileId.
                    returned: success,changed,always
                    type: str
                    sample: '<profileid>'
                name:
                    description: It is the virtual account sync's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                addressIpV4:
                    description: It is the virtual account sync's addressIpV4.
                    returned: success,changed,always
                    type: str
                    sample: '<addressipv4>'
                cert:
                    description: It is the virtual account sync's cert.
                    returned: success,changed,always
                    type: str
                    sample: '<cert>'
                addressFqdn:
                    description: It is the virtual account sync's addressFqdn.
                    returned: success,changed,always
                    type: str
                    sample: '<addressfqdn>'

        ccoUser:
            description: SAVAMapping's Cco User.
            returned: success,changed,always
            type: str
            sample: '<ccouser>'
        syncResult:
            description: SAVAMapping's Sync Result.
            returned: success,changed,always
            type: dict
            contains:
                syncList:
                    description: It is the virtual account sync's syncList.
                    returned: success,changed,always
                    type: list
                    contains:
                        syncType:
                            description: It is the virtual account sync's syncType.
                            returned: success,changed,always
                            type: str
                            sample: '<synctype>'
                        deviceSnList:
                            description: It is the virtual account sync's deviceSnList.
                            returned: success,changed,always
                            type: list

                syncMsg:
                    description: It is the virtual account sync's syncMsg.
                    returned: success,changed,always
                    type: str
                    sample: '<syncmsg>'

        token:
            description: SAVAMapping's Token.
            returned: success,changed,always
            type: str
            sample: '<token>'
        syncStartTime:
            description: SAVAMapping's syncStartTime.
            returned: success,changed,always
            type: int
            sample: 0
        lastSync:
            description: SAVAMapping's lastSync.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: SAVAMapping's Tenant Id.
            returned: success,changed,always
            type: str
            sample: '<tenantid>'
        smartAccountId:
            description: SAVAMapping's Smart Account Id.
            returned: success,changed,always
            type: str
            sample: '<smartaccountid>'
        expiry:
            description: SAVAMapping's expiry.
            returned: success,changed,always
            type: int
            sample: 0
        syncStatus:
            description: SAVAMapping's Sync Status.
            returned: success,changed,always
            type: str
            sample: '<syncstatus>'

data_1:
    description: Returns the summary of devices synced from the given smart account & virtual account with PnP.
    returned: success,changed,always
    type: dict
    contains:
        virtualAccountId:
            description: Virtual Account Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<virtualaccountid>'
        autoSyncPeriod:
            description: AutoSyncPeriod, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        syncResultStr:
            description: Sync Result Str, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<syncresultstr>'
        profile:
            description: Profile, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                proxy:
                    description: It is the virtual account sync's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                makeDefault:
                    description: It is the virtual account sync's makeDefault.
                    returned: success,changed,always
                    type: bool
                    sample: false
                port:
                    description: It is the virtual account sync's port.
                    returned: success,changed,always
                    type: int
                    sample: 0
                profileId:
                    description: It is the virtual account sync's profileId.
                    returned: success,changed,always
                    type: str
                    sample: '<profileid>'
                name:
                    description: It is the virtual account sync's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                addressIpV4:
                    description: It is the virtual account sync's addressIpV4.
                    returned: success,changed,always
                    type: str
                    sample: '<addressipv4>'
                cert:
                    description: It is the virtual account sync's cert.
                    returned: success,changed,always
                    type: str
                    sample: '<cert>'
                addressFqdn:
                    description: It is the virtual account sync's addressFqdn.
                    returned: success,changed,always
                    type: str
                    sample: '<addressfqdn>'

        ccoUser:
            description: Cco User, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<ccouser>'
        syncResult:
            description: Sync Result, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                syncList:
                    description: It is the virtual account sync's syncList.
                    returned: success,changed,always
                    type: list
                    contains:
                        syncType:
                            description: It is the virtual account sync's syncType.
                            returned: success,changed,always
                            type: str
                            sample: '<synctype>'
                        deviceSnList:
                            description: It is the virtual account sync's deviceSnList.
                            returned: success,changed,always
                            type: list

                syncMsg:
                    description: It is the virtual account sync's syncMsg.
                    returned: success,changed,always
                    type: str
                    sample: '<syncmsg>'

        token:
            description: Token, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<token>'
        syncStartTime:
            description: SyncStartTime, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        lastSync:
            description: LastSync, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<tenantid>'
        smartAccountId:
            description: Smart Account Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<smartaccountid>'
        expiry:
            description: Expiry, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        syncStatus:
            description: Sync Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<syncstatus>'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.virtual_account_sync import module_definition


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

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
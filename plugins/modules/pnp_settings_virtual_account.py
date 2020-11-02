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
module: pnp_settings_virtual_account
short_description: Manage PnpSettingsVirtualAccount objects of DeviceOnboardingPnp
description:
- Returns list of virtual accounts associated with the specified smart account.
- Registers a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database. The devices present in the registered virtual account are synced with the PnP database as well. The response payload returns the new profile.
- Updates the PnP Server profile in a registered Virtual Account in the PnP database. The response payload returns the updated smart & virtual account info.
- Deregisters the specified smart account & virtual account info and the associated device information from the PnP System & database. The devices associated with the deregistered virtual account are removed from the PnP database as well. The response payload contains the deregistered smart & virtual account information.
version_added: '1.0'
author: first last (@GitHubID)
options:
    domain:
        description:
        - Smart Account Domain.
        type: str
        required: True
    auto_sync_period:
        description:
        - SAVAMapping's autoSyncPeriod.
        type: int
    cco_user:
        description:
        - SAVAMapping's ccoUser.
        type: str
    expiry:
        description:
        - SAVAMapping's expiry.
        type: int
    last_sync:
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
                - It is the pnp settings virtual account's addressFqdn.
                type: str
            addressIpV4:
                description:
                - It is the pnp settings virtual account's addressIpV4.
                type: str
            cert:
                description:
                - It is the pnp settings virtual account's cert.
                type: str
            makeDefault:
                description:
                - It is the pnp settings virtual account's makeDefault.
                type: bool
            name:
                description:
                - It is the pnp settings virtual account's name.
                type: str
            port:
                description:
                - It is the pnp settings virtual account's port.
                type: int
            profileId:
                description:
                - It is the pnp settings virtual account's profileId.
                type: str
            proxy:
                description:
                - It is the pnp settings virtual account's proxy.
                type: bool

    smart_account_id:
        description:
        - SAVAMapping's smartAccountId.
        type: str
        required: True
    sync_result:
        description:
        - SAVAMapping's syncResult.
        type: dict
        suboptions:
            syncList:
                description:
                - It is the pnp settings virtual account's syncList.
                type: list
                elements: dict
                suboptions:
                    deviceSnList:
                        description:
                        - It is the pnp settings virtual account's deviceSnList.
                        type: list
                    syncType:
                        description:
                        - It is the pnp settings virtual account's syncType.
                        type: str

            syncMsg:
                description:
                - It is the pnp settings virtual account's syncMsg.
                type: str

    sync_result_str:
        description:
        - SAVAMapping's syncResultStr.
        type: str
    sync_start_time:
        description:
        - SAVAMapping's syncStartTime.
        type: int
    sync_status:
        description:
        - SAVAMapping's syncStatus.
        type: str
        required: True
        choices: ['NOT_SYNCED', 'SYNCING', 'SUCCESS', 'FAILURE']
    tenant_id:
        description:
        - SAVAMapping's tenantId.
        type: str
    token:
        description:
        - SAVAMapping's token.
        type: str
    virtual_account_id:
        description:
        - SAVAMapping's virtualAccountId.
        type: str
        required: True
    auto_sync_period:
        description:
        - SAVAMapping's autoSyncPeriod.
        type: int
    cco_user:
        description:
        - SAVAMapping's ccoUser.
        type: str
    expiry:
        description:
        - SAVAMapping's expiry.
        type: int
    last_sync:
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
                - It is the pnp settings virtual account's addressFqdn.
                type: str
            addressIpV4:
                description:
                - It is the pnp settings virtual account's addressIpV4.
                type: str
            cert:
                description:
                - It is the pnp settings virtual account's cert.
                type: str
            makeDefault:
                description:
                - It is the pnp settings virtual account's makeDefault.
                type: bool
            name:
                description:
                - It is the pnp settings virtual account's name.
                type: str
            port:
                description:
                - It is the pnp settings virtual account's port.
                type: int
            profileId:
                description:
                - It is the pnp settings virtual account's profileId.
                type: str
            proxy:
                description:
                - It is the pnp settings virtual account's proxy.
                type: bool

    smart_account_id:
        description:
        - SAVAMapping's smartAccountId.
        type: str
        required: True
    sync_result:
        description:
        - SAVAMapping's syncResult.
        type: dict
        suboptions:
            syncList:
                description:
                - It is the pnp settings virtual account's syncList.
                type: list
                elements: dict
                suboptions:
                    deviceSnList:
                        description:
                        - It is the pnp settings virtual account's deviceSnList.
                        type: list
                    syncType:
                        description:
                        - It is the pnp settings virtual account's syncType.
                        type: str

            syncMsg:
                description:
                - It is the pnp settings virtual account's syncMsg.
                type: str

    sync_result_str:
        description:
        - SAVAMapping's syncResultStr.
        type: str
    sync_start_time:
        description:
        - SAVAMapping's syncStartTime.
        type: int
    sync_status:
        description:
        - SAVAMapping's syncStatus.
        type: str
        required: True
        choices: ['NOT_SYNCED', 'SYNCING', 'SUCCESS', 'FAILURE']
    tenant_id:
        description:
        - SAVAMapping's tenantId.
        type: str
    token:
        description:
        - SAVAMapping's token.
        type: str
    virtual_account_id:
        description:
        - SAVAMapping's virtualAccountId.
        type: str
        required: True
    domain:
        description:
        - Smart Account Domain.
        type: str
    name:
        description:
        - Virtual Account Name.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_settings_virtual_account
# Reference by Internet resource
- name: PnpSettingsVirtualAccount reference
  description: Complete reference of the PnpSettingsVirtualAccount object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpSettingsVirtualAccount reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns list of virtual accounts associated with the specified smart account.
    returned: success,changed,always
    type: list
    contains:


data_1:
    description: Registers a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database. The devices present in the registered virtual account are synced with the PnP database as well. The response payload returns the new profile.
    returned: success,changed,always
    type: dict
    contains:
        virtualAccountId:
            description: SAVAMapping's Virtual Account Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        autoSyncPeriod:
            description: SAVAMapping's autoSyncPeriod.
            returned: success,changed,always
            type: int
            sample: 0
        syncResultStr:
            description: SAVAMapping's Sync Result Str.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        profile:
            description: SAVAMapping's Profile.
            returned: success,changed,always
            type: dict
            contains:
                proxy:
                    description: It is the pnp settings virtual account's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                makeDefault:
                    description: It is the pnp settings virtual account's makeDefault.
                    returned: success,changed,always
                    type: bool
                    sample: false
                port:
                    description: It is the pnp settings virtual account's port.
                    returned: success,changed,always
                    type: int
                    sample: 0
                profileId:
                    description: It is the pnp settings virtual account's profileId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp settings virtual account's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressIpV4:
                    description: It is the pnp settings virtual account's addressIpV4.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cert:
                    description: It is the pnp settings virtual account's cert.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressFqdn:
                    description: It is the pnp settings virtual account's addressFqdn.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        ccoUser:
            description: SAVAMapping's Cco User.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        syncResult:
            description: SAVAMapping's Sync Result.
            returned: success,changed,always
            type: dict
            contains:
                syncList:
                    description: It is the pnp settings virtual account's syncList.
                    returned: success,changed,always
                    type: list
                    contains:
                        syncType:
                            description: It is the pnp settings virtual account's syncType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceSnList:
                            description: It is the pnp settings virtual account's deviceSnList.
                            returned: success,changed,always
                            type: list

                syncMsg:
                    description: It is the pnp settings virtual account's syncMsg.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        token:
            description: SAVAMapping's Token.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
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
            sample: 'sample_string'
        smartAccountId:
            description: SAVAMapping's Smart Account Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        expiry:
            description: SAVAMapping's expiry.
            returned: success,changed,always
            type: int
            sample: 0
        syncStatus:
            description: SAVAMapping's Sync Status.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Updates the PnP Server profile in a registered Virtual Account in the PnP database. The response payload returns the updated smart & virtual account info.
    returned: success,changed,always
    type: dict
    contains:
        virtualAccountId:
            description: SAVAMapping's Virtual Account Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        autoSyncPeriod:
            description: SAVAMapping's autoSyncPeriod.
            returned: success,changed,always
            type: int
            sample: 0
        syncResultStr:
            description: SAVAMapping's Sync Result Str.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        profile:
            description: SAVAMapping's Profile.
            returned: success,changed,always
            type: dict
            contains:
                proxy:
                    description: It is the pnp settings virtual account's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                makeDefault:
                    description: It is the pnp settings virtual account's makeDefault.
                    returned: success,changed,always
                    type: bool
                    sample: false
                port:
                    description: It is the pnp settings virtual account's port.
                    returned: success,changed,always
                    type: int
                    sample: 0
                profileId:
                    description: It is the pnp settings virtual account's profileId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp settings virtual account's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressIpV4:
                    description: It is the pnp settings virtual account's addressIpV4.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cert:
                    description: It is the pnp settings virtual account's cert.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressFqdn:
                    description: It is the pnp settings virtual account's addressFqdn.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        ccoUser:
            description: SAVAMapping's Cco User.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        syncResult:
            description: SAVAMapping's Sync Result.
            returned: success,changed,always
            type: dict
            contains:
                syncList:
                    description: It is the pnp settings virtual account's syncList.
                    returned: success,changed,always
                    type: list
                    contains:
                        syncType:
                            description: It is the pnp settings virtual account's syncType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceSnList:
                            description: It is the pnp settings virtual account's deviceSnList.
                            returned: success,changed,always
                            type: list

                syncMsg:
                    description: It is the pnp settings virtual account's syncMsg.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        token:
            description: SAVAMapping's Token.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
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
            sample: 'sample_string'
        smartAccountId:
            description: SAVAMapping's Smart Account Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        expiry:
            description: SAVAMapping's expiry.
            returned: success,changed,always
            type: int
            sample: 0
        syncStatus:
            description: SAVAMapping's Sync Status.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Deregisters the specified smart account & virtual account info and the associated device information from the PnP System & database. The devices associated with the deregistered virtual account are removed from the PnP database as well. The response payload contains the deregistered smart & virtual account information.
    returned: success,changed,always
    type: dict
    contains:
        virtualAccountId:
            description: Virtual Account Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        autoSyncPeriod:
            description: AutoSyncPeriod, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        syncResultStr:
            description: Sync Result Str, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        profile:
            description: Profile, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                proxy:
                    description: It is the pnp settings virtual account's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                makeDefault:
                    description: It is the pnp settings virtual account's makeDefault.
                    returned: success,changed,always
                    type: bool
                    sample: false
                port:
                    description: It is the pnp settings virtual account's port.
                    returned: success,changed,always
                    type: int
                    sample: 0
                profileId:
                    description: It is the pnp settings virtual account's profileId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp settings virtual account's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressIpV4:
                    description: It is the pnp settings virtual account's addressIpV4.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cert:
                    description: It is the pnp settings virtual account's cert.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressFqdn:
                    description: It is the pnp settings virtual account's addressFqdn.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        ccoUser:
            description: Cco User, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        syncResult:
            description: Sync Result, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                syncList:
                    description: It is the pnp settings virtual account's syncList.
                    returned: success,changed,always
                    type: list
                    contains:
                        syncType:
                            description: It is the pnp settings virtual account's syncType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceSnList:
                            description: It is the pnp settings virtual account's deviceSnList.
                            returned: success,changed,always
                            type: list

                syncMsg:
                    description: It is the pnp settings virtual account's syncMsg.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        token:
            description: Token, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
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
            sample: 'sample_string'
        smartAccountId:
            description: Smart Account Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        expiry:
            description: Expiry, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        syncStatus:
            description: Sync Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_settings_virtual_account import module_definition


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
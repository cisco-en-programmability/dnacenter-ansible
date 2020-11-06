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
module: pnp_device_virtual_account_sync
short_description: Manage PnpDeviceVirtualAccountSync objects of DeviceOnboardingPnp
description:
- Synchronizes the device info from the given smart account & virtual account with the PnP database. The response payload returns a list of synced devices.
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
                - It is the pnp device virtual account sync's addressFqdn.
                type: str
            addressIpV4:
                description:
                - It is the pnp device virtual account sync's addressIpV4.
                type: str
            cert:
                description:
                - It is the pnp device virtual account sync's cert.
                type: str
            makeDefault:
                description:
                - It is the pnp device virtual account sync's makeDefault.
                type: bool
            name:
                description:
                - It is the pnp device virtual account sync's name.
                type: str
            port:
                description:
                - It is the pnp device virtual account sync's port.
                type: int
            profileId:
                description:
                - It is the pnp device virtual account sync's profileId.
                type: str
            proxy:
                description:
                - It is the pnp device virtual account sync's proxy.
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
                - It is the pnp device virtual account sync's syncList.
                type: list
                elements: dict
                suboptions:
                    deviceSnList:
                        description:
                        - It is the pnp device virtual account sync's deviceSnList.
                        type: list
                    syncType:
                        description:
                        - It is the pnp device virtual account sync's syncType.
                        type: str

            syncMsg:
                description:
                - It is the pnp device virtual account sync's syncMsg.
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

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_virtual_account_sync
# Reference by Internet resource
- name: PnpDeviceVirtualAccountSync reference
  description: Complete reference of the PnpDeviceVirtualAccountSync object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceVirtualAccountSync reference
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
                    description: It is the pnp device virtual account sync's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                makeDefault:
                    description: It is the pnp device virtual account sync's makeDefault.
                    returned: success,changed,always
                    type: bool
                    sample: false
                port:
                    description: It is the pnp device virtual account sync's port.
                    returned: success,changed,always
                    type: int
                    sample: 0
                profileId:
                    description: It is the pnp device virtual account sync's profileId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device virtual account sync's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressIpV4:
                    description: It is the pnp device virtual account sync's addressIpV4.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cert:
                    description: It is the pnp device virtual account sync's cert.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressFqdn:
                    description: It is the pnp device virtual account sync's addressFqdn.
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
                    description: It is the pnp device virtual account sync's syncList.
                    returned: success,changed,always
                    type: list
                    contains:
                        syncType:
                            description: It is the pnp device virtual account sync's syncType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceSnList:
                            description: It is the pnp device virtual account sync's deviceSnList.
                            returned: success,changed,always
                            type: list

                syncMsg:
                    description: It is the pnp device virtual account sync's syncMsg.
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

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_virtual_account_sync import module_definition


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

    if state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
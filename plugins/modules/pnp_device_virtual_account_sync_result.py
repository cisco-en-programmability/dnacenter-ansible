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
module: pnp_device_virtual_account_sync_result
short_description: Manage PnpDeviceVirtualAccountSyncResult objects of DeviceOnboardingPnp
description:
- Returns the summary of devices synced from the given smart account & virtual account with PnP.
version_added: '1.0'
author: first last (@GitHubID)
options:
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
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_virtual_account_sync_result
# Reference by Internet resource
- name: PnpDeviceVirtualAccountSyncResult reference
  description: Complete reference of the PnpDeviceVirtualAccountSyncResult object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceVirtualAccountSyncResult reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns the summary of devices synced from the given smart account & virtual account with PnP.
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
                    description: It is the pnp device virtual account sync result's proxy.
                    returned: success,changed,always
                    type: bool
                    sample: false
                makeDefault:
                    description: It is the pnp device virtual account sync result's makeDefault.
                    returned: success,changed,always
                    type: bool
                    sample: false
                port:
                    description: It is the pnp device virtual account sync result's port.
                    returned: success,changed,always
                    type: int
                    sample: 0
                profileId:
                    description: It is the pnp device virtual account sync result's profileId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device virtual account sync result's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressIpV4:
                    description: It is the pnp device virtual account sync result's addressIpV4.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cert:
                    description: It is the pnp device virtual account sync result's cert.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                addressFqdn:
                    description: It is the pnp device virtual account sync result's addressFqdn.
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
                    description: It is the pnp device virtual account sync result's syncList.
                    returned: success,changed,always
                    type: list
                    contains:
                        syncType:
                            description: It is the pnp device virtual account sync result's syncType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceSnList:
                            description: It is the pnp device virtual account sync result's deviceSnList.
                            returned: success,changed,always
                            type: list

                syncMsg:
                    description: It is the pnp device virtual account sync result's syncMsg.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_virtual_account_sync_result import module_definition


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

    dnac.exit_json()


if __name__ == "__main__":
    main()
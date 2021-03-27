#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: smart_virtual_account
short_description: Manage SmartVirtualAccount objects of DeviceOnboardingPnp
description:
- Returns the list of Smart Account domains.
- Returns list of virtual accounts associated with the specified smart account.
- Registers a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database. The devices present in the registered virtual account are synced with the PnP database as well. The response payload returns the new profile.
- Updates the PnP Server profile in a registered Virtual Account in the PnP database. The response payload returns the updated smart & virtual account info.
- Deregisters the specified smart account & virtual account info and the associated device information from the PnP System & database. The devices associated with the deregistered virtual account are removed from the PnP database as well. The response payload contains the deregistered smart & virtual account information.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  domain:
    description:
    - Smart Account Domain.
    type: str
    required: True
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
        - It is the smart virtual account's addressFqdn.
        type: str
      addressIpV4:
        description:
        - It is the smart virtual account's addressIpV4.
        type: str
      cert:
        description:
        - It is the smart virtual account's cert.
        type: str
      makeDefault:
        description:
        - It is the smart virtual account's makeDefault.
        type: bool
      name:
        description:
        - It is the smart virtual account's name.
        type: str
      port:
        description:
        - It is the smart virtual account's port.
        type: int
      profileId:
        description:
        - It is the smart virtual account's profileId.
        type: str
      proxy:
        description:
        - It is the smart virtual account's proxy.
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
        - It is the smart virtual account's syncList.
        type: list
        elements: dict
        suboptions:
          deviceSnList:
            description:
            - It is the smart virtual account's deviceSnList.
            type: list
          syncType:
            description:
            - It is the smart virtual account's syncType.
            type: str

      syncMsg:
        description:
        - It is the smart virtual account's syncMsg.
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
  name:
    description:
    - Virtual Account Name.
    - Required for state delete.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.smart_virtual_account
# Reference by Internet resource
- name: SmartVirtualAccount reference
  description: Complete reference of the SmartVirtualAccount object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SmartVirtualAccount reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_smart_account_list
  cisco.dnac.smart_virtual_account:
    state: query  # required

  register: query_result
  
- name: get_virtual_account_list
  cisco.dnac.smart_virtual_account:
    state: query  # required
    domain: SomeValue  # string, required
  register: query_result
  
- name: add_virtual_account
  cisco.dnac.smart_virtual_account:
    state: create  # required
    profile:  # required
      addressFqdn: SomeValue  # string
      addressIpV4: SomeValue  # string
      cert: SomeValue  # string
      makeDefault: True  # boolean
      name: SomeValue  # string
      port: 1  #  integer
      profileId: SomeValue  # string
      proxy: True  # boolean
    smartAccountId: SomeValue  # string, required
    syncStatus: SomeValue  # string, required, valid values: 'NOT_SYNCED', 'SYNCING', 'SUCCESS', 'FAILURE'.
    virtualAccountId: SomeValue  # string, required
    autoSyncPeriod: 1  #  integer
    ccoUser: SomeValue  # string
    expiry: 1  #  integer
    lastSync: 1  #  integer
    syncResult:
      syncList:
      - deviceSnList:
        - SomeValue  # string
        syncType: SomeValue  # string
      syncMsg: SomeValue  # string
    syncResultStr: SomeValue  # string
    syncStartTime: 1  #  integer
    tenantId: SomeValue  # string
    token: SomeValue  # string
  
- name: update_pnp_server_profile
  cisco.dnac.smart_virtual_account:
    state: update  # required
    profile:  # required
      addressFqdn: SomeValue  # string
      addressIpV4: SomeValue  # string
      cert: SomeValue  # string
      makeDefault: True  # boolean
      name: SomeValue  # string
      port: 1  #  integer
      profileId: SomeValue  # string
      proxy: True  # boolean
    smartAccountId: SomeValue  # string, required
    syncStatus: SomeValue  # string, required, valid values: 'NOT_SYNCED', 'SYNCING', 'SUCCESS', 'FAILURE'.
    virtualAccountId: SomeValue  # string, required
    autoSyncPeriod: 1  #  integer
    ccoUser: SomeValue  # string
    expiry: 1  #  integer
    lastSync: 1  #  integer
    syncResult:
      syncList:
      - deviceSnList:
        - SomeValue  # string
        syncType: SomeValue  # string
      syncMsg: SomeValue  # string
    syncResultStr: SomeValue  # string
    syncStartTime: 1  #  integer
    tenantId: SomeValue  # string
    token: SomeValue  # string
  
- name: deregister_virtual_account
  cisco.dnac.smart_virtual_account:
    state: delete  # required
    domain: SomeValue  # string, required
    name: SomeValue  # string, required
  
"""

RETURN = """
get_smart_account_list:
    description: Returns the list of Smart Account domains.
    returned: always
    type: dict
    contains:
      payload:
      description: It is the smart virtual account's payload.
      returned: always
      type: list

get_virtual_account_list:
    description: Returns list of virtual accounts associated with the specified smart account.
    returned: always
    type: dict
    contains:
      payload:
      description: It is the smart virtual account's payload.
      returned: always
      type: list

add_virtual_account:
    description: Registers a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database. The devices present in the registered virtual account are synced with the PnP database as well. The response payload returns the new profile.
    returned: success
    type: dict
    contains:
      virtualAccountId:
      description: SAVAMapping's Virtual Account Id.
      returned: success
      type: str
      sample: '<virtualaccountid>'
    autoSyncPeriod:
      description: SAVAMapping's autoSyncPeriod.
      returned: success
      type: int
      sample: 0
    syncResultStr:
      description: SAVAMapping's Sync Result Str.
      returned: success
      type: str
      sample: '<syncresultstr>'
    profile:
      description: SAVAMapping's Profile.
      returned: success
      type: dict
      contains:
        proxy:
          description: It is the smart virtual account's proxy.
          returned: success
          type: bool
          sample: false
        makeDefault:
          description: It is the smart virtual account's makeDefault.
          returned: success
          type: bool
          sample: false
        port:
          description: It is the smart virtual account's port.
          returned: success
          type: int
          sample: 0
        profileId:
          description: It is the smart virtual account's profileId.
          returned: success
          type: str
          sample: '<profileid>'
        name:
          description: It is the smart virtual account's name.
          returned: success
          type: str
          sample: '<name>'
        addressIpV4:
          description: It is the smart virtual account's addressIpV4.
          returned: success
          type: str
          sample: '<addressipv4>'
        cert:
          description: It is the smart virtual account's cert.
          returned: success
          type: str
          sample: '<cert>'
        addressFqdn:
          description: It is the smart virtual account's addressFqdn.
          returned: success
          type: str
          sample: '<addressfqdn>'

    ccoUser:
      description: SAVAMapping's Cco User.
      returned: success
      type: str
      sample: '<ccouser>'
    syncResult:
      description: SAVAMapping's Sync Result.
      returned: success
      type: dict
      contains:
        syncList:
          description: It is the smart virtual account's syncList.
          returned: success
          type: list
          contains:
            syncType:
              description: It is the smart virtual account's syncType.
              returned: success
              type: str
              sample: '<synctype>'
            deviceSnList:
              description: It is the smart virtual account's deviceSnList.
              returned: success
              type: list

        syncMsg:
          description: It is the smart virtual account's syncMsg.
          returned: success
          type: str
          sample: '<syncmsg>'

    token:
      description: SAVAMapping's Token.
      returned: success
      type: str
      sample: '<token>'
    syncStartTime:
      description: SAVAMapping's syncStartTime.
      returned: success
      type: int
      sample: 0
    lastSync:
      description: SAVAMapping's lastSync.
      returned: success
      type: int
      sample: 0
    tenantId:
      description: SAVAMapping's Tenant Id.
      returned: success
      type: str
      sample: '<tenantid>'
    smartAccountId:
      description: SAVAMapping's Smart Account Id.
      returned: success
      type: str
      sample: '<smartaccountid>'
    expiry:
      description: SAVAMapping's expiry.
      returned: success
      type: int
      sample: 0
    syncStatus:
      description: SAVAMapping's Sync Status.
      returned: success
      type: str
      sample: '<syncstatus>'

update_pnp_server_profile:
    description: Updates the PnP Server profile in a registered Virtual Account in the PnP database. The response payload returns the updated smart & virtual account info.
    returned: changed
    type: dict
    contains:
      virtualAccountId:
      description: SAVAMapping's Virtual Account Id.
      returned: changed
      type: str
      sample: '<virtualaccountid>'
    autoSyncPeriod:
      description: SAVAMapping's autoSyncPeriod.
      returned: changed
      type: int
      sample: 0
    syncResultStr:
      description: SAVAMapping's Sync Result Str.
      returned: changed
      type: str
      sample: '<syncresultstr>'
    profile:
      description: SAVAMapping's Profile.
      returned: changed
      type: dict
      contains:
        proxy:
          description: It is the smart virtual account's proxy.
          returned: changed
          type: bool
          sample: false
        makeDefault:
          description: It is the smart virtual account's makeDefault.
          returned: changed
          type: bool
          sample: false
        port:
          description: It is the smart virtual account's port.
          returned: changed
          type: int
          sample: 0
        profileId:
          description: It is the smart virtual account's profileId.
          returned: changed
          type: str
          sample: '<profileid>'
        name:
          description: It is the smart virtual account's name.
          returned: changed
          type: str
          sample: '<name>'
        addressIpV4:
          description: It is the smart virtual account's addressIpV4.
          returned: changed
          type: str
          sample: '<addressipv4>'
        cert:
          description: It is the smart virtual account's cert.
          returned: changed
          type: str
          sample: '<cert>'
        addressFqdn:
          description: It is the smart virtual account's addressFqdn.
          returned: changed
          type: str
          sample: '<addressfqdn>'

    ccoUser:
      description: SAVAMapping's Cco User.
      returned: changed
      type: str
      sample: '<ccouser>'
    syncResult:
      description: SAVAMapping's Sync Result.
      returned: changed
      type: dict
      contains:
        syncList:
          description: It is the smart virtual account's syncList.
          returned: changed
          type: list
          contains:
            syncType:
              description: It is the smart virtual account's syncType.
              returned: changed
              type: str
              sample: '<synctype>'
            deviceSnList:
              description: It is the smart virtual account's deviceSnList.
              returned: changed
              type: list

        syncMsg:
          description: It is the smart virtual account's syncMsg.
          returned: changed
          type: str
          sample: '<syncmsg>'

    token:
      description: SAVAMapping's Token.
      returned: changed
      type: str
      sample: '<token>'
    syncStartTime:
      description: SAVAMapping's syncStartTime.
      returned: changed
      type: int
      sample: 0
    lastSync:
      description: SAVAMapping's lastSync.
      returned: changed
      type: int
      sample: 0
    tenantId:
      description: SAVAMapping's Tenant Id.
      returned: changed
      type: str
      sample: '<tenantid>'
    smartAccountId:
      description: SAVAMapping's Smart Account Id.
      returned: changed
      type: str
      sample: '<smartaccountid>'
    expiry:
      description: SAVAMapping's expiry.
      returned: changed
      type: int
      sample: 0
    syncStatus:
      description: SAVAMapping's Sync Status.
      returned: changed
      type: str
      sample: '<syncstatus>'

deregister_virtual_account:
    description: Deregisters the specified smart account & virtual account info and the associated device information from the PnP System & database. The devices associated with the deregistered virtual account are removed from the PnP database as well. The response payload contains the deregistered smart & virtual account information.
    returned: success
    type: dict
    contains:
      virtualAccountId:
      description: Virtual Account Id, property of the response body.
      returned: success
      type: str
      sample: '<virtualaccountid>'
    autoSyncPeriod:
      description: AutoSyncPeriod, property of the response body.
      returned: success
      type: int
      sample: 0
    syncResultStr:
      description: Sync Result Str, property of the response body.
      returned: success
      type: str
      sample: '<syncresultstr>'
    profile:
      description: Profile, property of the response body.
      returned: success
      type: dict
      contains:
        proxy:
          description: It is the smart virtual account's proxy.
          returned: success
          type: bool
          sample: false
        makeDefault:
          description: It is the smart virtual account's makeDefault.
          returned: success
          type: bool
          sample: false
        port:
          description: It is the smart virtual account's port.
          returned: success
          type: int
          sample: 0
        profileId:
          description: It is the smart virtual account's profileId.
          returned: success
          type: str
          sample: '<profileid>'
        name:
          description: It is the smart virtual account's name.
          returned: success
          type: str
          sample: '<name>'
        addressIpV4:
          description: It is the smart virtual account's addressIpV4.
          returned: success
          type: str
          sample: '<addressipv4>'
        cert:
          description: It is the smart virtual account's cert.
          returned: success
          type: str
          sample: '<cert>'
        addressFqdn:
          description: It is the smart virtual account's addressFqdn.
          returned: success
          type: str
          sample: '<addressfqdn>'

    ccoUser:
      description: Cco User, property of the response body.
      returned: success
      type: str
      sample: '<ccouser>'
    syncResult:
      description: Sync Result, property of the response body.
      returned: success
      type: dict
      contains:
        syncList:
          description: It is the smart virtual account's syncList.
          returned: success
          type: list
          contains:
            syncType:
              description: It is the smart virtual account's syncType.
              returned: success
              type: str
              sample: '<synctype>'
            deviceSnList:
              description: It is the smart virtual account's deviceSnList.
              returned: success
              type: list

        syncMsg:
          description: It is the smart virtual account's syncMsg.
          returned: success
          type: str
          sample: '<syncmsg>'

    token:
      description: Token, property of the response body.
      returned: success
      type: str
      sample: '<token>'
    syncStartTime:
      description: SyncStartTime, property of the response body.
      returned: success
      type: int
      sample: 0
    lastSync:
      description: LastSync, property of the response body.
      returned: success
      type: int
      sample: 0
    tenantId:
      description: Tenant Id, property of the response body.
      returned: success
      type: str
      sample: '<tenantid>'
    smartAccountId:
      description: Smart Account Id, property of the response body.
      returned: success
      type: str
      sample: '<smartaccountid>'
    expiry:
      description: Expiry, property of the response body.
      returned: success
      type: int
      sample: 0
    syncStatus:
      description: Sync Status, property of the response body.
      returned: success
      type: str
      sample: '<syncstatus>'

"""

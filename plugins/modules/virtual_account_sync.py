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
    - Required for state create.
    type: dict
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
    - Required for state create.
    type: str
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
    - Required for state create.
    type: str
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
    - Required for state create.
    type: str
  domain:
    description:
    - Smart Account Domain.
    - Required for state query.
    type: str
  name:
    description:
    - Virtual Account Name.
    - Required for state query.
    type: str

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
"""

EXAMPLES = r"""
- name: sync_virtual_account_devices
  cisco.dnac.virtual_account_sync:
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
  
- name: get_sync_result_for_virtual_account
  cisco.dnac.virtual_account_sync:
    state: query  # required
    domain: SomeValue  # string, required
    name: SomeValue  # string, required
  register: query_result
  
"""

RETURN = """
sync_virtual_account_devices:
    description: Synchronizes the device info from the given smart account & virtual account with the PnP database. The response payload returns a list of synced devices.
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
          description: It is the virtual account sync's proxy.
          returned: success
          type: bool
          sample: false
        makeDefault:
          description: It is the virtual account sync's makeDefault.
          returned: success
          type: bool
          sample: false
        port:
          description: It is the virtual account sync's port.
          returned: success
          type: int
          sample: 0
        profileId:
          description: It is the virtual account sync's profileId.
          returned: success
          type: str
          sample: '<profileid>'
        name:
          description: It is the virtual account sync's name.
          returned: success
          type: str
          sample: '<name>'
        addressIpV4:
          description: It is the virtual account sync's addressIpV4.
          returned: success
          type: str
          sample: '<addressipv4>'
        cert:
          description: It is the virtual account sync's cert.
          returned: success
          type: str
          sample: '<cert>'
        addressFqdn:
          description: It is the virtual account sync's addressFqdn.
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
          description: It is the virtual account sync's syncList.
          returned: success
          type: list
          contains:
            syncType:
              description: It is the virtual account sync's syncType.
              returned: success
              type: str
              sample: '<synctype>'
            deviceSnList:
              description: It is the virtual account sync's deviceSnList.
              returned: success
              type: list

        syncMsg:
          description: It is the virtual account sync's syncMsg.
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

get_sync_result_for_virtual_account:
    description: Returns the summary of devices synced from the given smart account & virtual account with PnP.
    returned: always
    type: dict
    contains:
    virtualAccountId:
      description: Virtual Account Id, property of the response body.
      returned: always
      type: str
      sample: '<virtualaccountid>'
    autoSyncPeriod:
      description: AutoSyncPeriod, property of the response body.
      returned: always
      type: int
      sample: 0
    syncResultStr:
      description: Sync Result Str, property of the response body.
      returned: always
      type: str
      sample: '<syncresultstr>'
    profile:
      description: Profile, property of the response body.
      returned: always
      type: dict
      contains:
        proxy:
          description: It is the virtual account sync's proxy.
          returned: always
          type: bool
          sample: false
        makeDefault:
          description: It is the virtual account sync's makeDefault.
          returned: always
          type: bool
          sample: false
        port:
          description: It is the virtual account sync's port.
          returned: always
          type: int
          sample: 0
        profileId:
          description: It is the virtual account sync's profileId.
          returned: always
          type: str
          sample: '<profileid>'
        name:
          description: It is the virtual account sync's name.
          returned: always
          type: str
          sample: '<name>'
        addressIpV4:
          description: It is the virtual account sync's addressIpV4.
          returned: always
          type: str
          sample: '<addressipv4>'
        cert:
          description: It is the virtual account sync's cert.
          returned: always
          type: str
          sample: '<cert>'
        addressFqdn:
          description: It is the virtual account sync's addressFqdn.
          returned: always
          type: str
          sample: '<addressfqdn>'

    ccoUser:
      description: Cco User, property of the response body.
      returned: always
      type: str
      sample: '<ccouser>'
    syncResult:
      description: Sync Result, property of the response body.
      returned: always
      type: dict
      contains:
        syncList:
          description: It is the virtual account sync's syncList.
          returned: always
          type: list
          contains:
            syncType:
              description: It is the virtual account sync's syncType.
              returned: always
              type: str
              sample: '<synctype>'
            deviceSnList:
              description: It is the virtual account sync's deviceSnList.
              returned: always
              type: list

        syncMsg:
          description: It is the virtual account sync's syncMsg.
          returned: always
          type: str
          sample: '<syncmsg>'

    token:
      description: Token, property of the response body.
      returned: always
      type: str
      sample: '<token>'
    syncStartTime:
      description: SyncStartTime, property of the response body.
      returned: always
      type: int
      sample: 0
    lastSync:
      description: LastSync, property of the response body.
      returned: always
      type: int
      sample: 0
    tenantId:
      description: Tenant Id, property of the response body.
      returned: always
      type: str
      sample: '<tenantid>'
    smartAccountId:
      description: Smart Account Id, property of the response body.
      returned: always
      type: str
      sample: '<smartaccountid>'
    expiry:
      description: Expiry, property of the response body.
      returned: always
      type: int
      sample: 0
    syncStatus:
      description: Sync Status, property of the response body.
      returned: always
      type: str
      sample: '<syncstatus>'

"""

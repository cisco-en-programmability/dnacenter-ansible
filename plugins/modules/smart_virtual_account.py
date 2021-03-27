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
"""

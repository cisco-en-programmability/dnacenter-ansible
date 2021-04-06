#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: virtual_account_sync
short_description: Manage VirtualAccountSync objects of DeviceOnboardingPnp
description:
- Synchronizes the device info from the given smart account & virtual account with the PnP database. The response payload returns a list of synced devices.
- Returns the summary of devices synced from the given smart account & virtual account with PnP.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: array
  sample:
"""

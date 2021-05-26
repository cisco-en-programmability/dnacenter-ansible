#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_settings
short_description: Manage PnpSettings objects of DeviceOnboardingPnp
description:
- Returns global PnP settings of the user.
- Updates the user's list of global PnP settings.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
"""

EXAMPLES = r"""
- name: get_pnp_global_settings
  cisco.dnac.pnp_settings:
    state: query  # required
  register: nm_get_pnp_global_settings

- name: update_pnp_global_settings
  cisco.dnac.pnp_settings:
    state: update  # required
    _id: SomeValue  # string
    aaaCredentials:
      password: SomeValue  # string
      username: SomeValue  # string
    acceptEula: True  # boolean
    defaultProfile:
      cert: SomeValue  # string
      fqdnAddresses:
      - SomeValue  # string
      ipAddresses:
      - SomeValue  # string
      port: 1  #  integer
      proxy: True  # boolean
    savaMappingList:
    - profile:  # required
        addressFqdn: SomeValue  # string
        addressIpV4: SomeValue  # string
        cert: SomeValue  # string
        makeDefault: True  # boolean
        name: SomeValue  # string
        port: 1  #  integer
        profileId: SomeValue  # string
        proxy: True  # boolean
      smartAccountId: SomeValue  # string, required
      syncStatus: SomeValue  # string, required
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
    taskTimeOuts:
      configTimeOut: 1  #  integer
      generalTimeOut: 1  #  integer
      imageDownloadTimeOut: 1  #  integer
    tenantId: SomeValue  # string
    version: 1  #  integer

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
  sample: device_onboarding_pnp.get_pnp_global_settings
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

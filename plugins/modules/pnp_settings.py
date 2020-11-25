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
"""

EXAMPLES = r"""
- name: get_pnp_global_settings
  cisco.dnac.pnp_settings:
    state: query  # required

  register: query_result
  
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

RETURN = """
get_pnp_global_settings:
    description: Returns global PnP settings of the user.
    returned: always
    type: dict
    contains:
    savaMappingList:
      description: Sava Mapping List, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        syncStatus:
          description: It is the pnp settings's syncStatus.
          returned: always
          type: str
          sample: '<syncstatus>'
        syncStartTime:
          description: It is the pnp settings's syncStartTime.
          returned: always
          type: int
          sample: 0
        syncResult:
          description: It is the pnp settings's syncResult.
          returned: always
          type: dict
          contains:
            syncList:
              description: It is the pnp settings's syncList.
              returned: always
              type: list
              contains:
                syncType:
                  description: It is the pnp settings's syncType.
                  returned: always
                  type: str
                  sample: '<synctype>'
                deviceSnList:
                  description: It is the pnp settings's deviceSnList.
                  returned: always
                  type: list

            syncMsg:
              description: It is the pnp settings's syncMsg.
              returned: always
              type: str
              sample: '<syncmsg>'

        lastSync:
          description: It is the pnp settings's lastSync.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp settings's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'
        profile:
          description: It is the pnp settings's profile.
          returned: always
          type: dict
          contains:
            port:
              description: It is the pnp settings's port.
              returned: always
              type: int
              sample: 0
            addressIpV4:
              description: It is the pnp settings's addressIpV4.
              returned: always
              type: str
              sample: '<addressipv4>'
            addressFqdn:
              description: It is the pnp settings's addressFqdn.
              returned: always
              type: str
              sample: '<addressfqdn>'
            profileId:
              description: It is the pnp settings's profileId.
              returned: always
              type: str
              sample: '<profileid>'
            proxy:
              description: It is the pnp settings's proxy.
              returned: always
              type: bool
              sample: false
            makeDefault:
              description: It is the pnp settings's makeDefault.
              returned: always
              type: bool
              sample: false
            cert:
              description: It is the pnp settings's cert.
              returned: always
              type: str
              sample: '<cert>'
            name:
              description: It is the pnp settings's name.
              returned: always
              type: str
              sample: '<name>'

        token:
          description: It is the pnp settings's token.
          returned: always
          type: str
          sample: '<token>'
        expiry:
          description: It is the pnp settings's expiry.
          returned: always
          type: int
          sample: 0
        ccoUser:
          description: It is the pnp settings's ccoUser.
          returned: always
          type: str
          sample: '<ccouser>'
        smartAccountId:
          description: It is the pnp settings's smartAccountId.
          returned: always
          type: str
          sample: '<smartaccountid>'
        virtualAccountId:
          description: It is the pnp settings's virtualAccountId.
          returned: always
          type: str
          sample: '<virtualaccountid>'
        autoSyncPeriod:
          description: It is the pnp settings's autoSyncPeriod.
          returned: always
          type: int
          sample: 0
        syncResultStr:
          description: It is the pnp settings's syncResultStr.
          returned: always
          type: str
          sample: '<syncresultstr>'

    taskTimeOuts:
      description: Task Time Outs, property of the response body.
      returned: always
      type: dict
      contains:
        imageDownloadTimeOut:
          description: It is the pnp settings's imageDownloadTimeOut.
          returned: always
          type: int
          sample: 0
        configTimeOut:
          description: It is the pnp settings's configTimeOut.
          returned: always
          type: int
          sample: 0
        generalTimeOut:
          description: It is the pnp settings's generalTimeOut.
          returned: always
          type: int
          sample: 0

    tenantId:
      description: Tenant Id, property of the response body.
      returned: always
      type: str
      sample: '<tenantid>'
    aaaCredentials:
      description: Aaa Credentials, property of the response body.
      returned: always
      type: dict
      contains:
        password:
          description: It is the pnp settings's password.
          returned: always
          type: str
          sample: '*******'
        username:
          description: It is the pnp settings's username.
          returned: always
          type: str
          sample: 'devnetuser'

    defaultProfile:
      description: Default Profile, property of the response body.
      returned: always
      type: dict
      contains:
        fqdnAddresses:
          description: It is the pnp settings's fqdnAddresses.
          returned: always
          type: list
        proxy:
          description: It is the pnp settings's proxy.
          returned: always
          type: bool
          sample: false
        cert:
          description: It is the pnp settings's cert.
          returned: always
          type: str
          sample: '<cert>'
        ipAddresses:
          description: It is the pnp settings's ipAddresses.
          returned: always
          type: list
        port:
          description: It is the pnp settings's port.
          returned: always
          type: int
          sample: 0

    acceptEula:
      description: AcceptEula, property of the response body.
      returned: always
      type: bool
      sample: false
    id:
      description: Id, property of the response body.
      returned: always
      type: str
      sample: '478012'
    _id:
      description: Id, property of the response body.
      returned: always
      type: str
      sample: '<_id>'
    version:
      description: Version, property of the response body.
      returned: always
      type: int
      sample: 0

update_pnp_global_settings:
    description: Updates the user's list of global PnP settings.
    returned: changed
    type: dict
    contains:
    savaMappingList:
      description: Settings's Sava Mapping List (list of objects).
      returned: changed
      type: list
      contains:
        syncStatus:
          description: It is the pnp settings's syncStatus.
          returned: changed
          type: str
          sample: '<syncstatus>'
        syncStartTime:
          description: It is the pnp settings's syncStartTime.
          returned: changed
          type: int
          sample: 0
        syncResult:
          description: It is the pnp settings's syncResult.
          returned: changed
          type: dict
          contains:
            syncList:
              description: It is the pnp settings's syncList.
              returned: changed
              type: list
              contains:
                syncType:
                  description: It is the pnp settings's syncType.
                  returned: changed
                  type: str
                  sample: '<synctype>'
                deviceSnList:
                  description: It is the pnp settings's deviceSnList.
                  returned: changed
                  type: list

            syncMsg:
              description: It is the pnp settings's syncMsg.
              returned: changed
              type: str
              sample: '<syncmsg>'

        lastSync:
          description: It is the pnp settings's lastSync.
          returned: changed
          type: int
          sample: 0
        tenantId:
          description: It is the pnp settings's tenantId.
          returned: changed
          type: str
          sample: '<tenantid>'
        profile:
          description: It is the pnp settings's profile.
          returned: changed
          type: dict
          contains:
            port:
              description: It is the pnp settings's port.
              returned: changed
              type: int
              sample: 0
            addressIpV4:
              description: It is the pnp settings's addressIpV4.
              returned: changed
              type: str
              sample: '<addressipv4>'
            addressFqdn:
              description: It is the pnp settings's addressFqdn.
              returned: changed
              type: str
              sample: '<addressfqdn>'
            profileId:
              description: It is the pnp settings's profileId.
              returned: changed
              type: str
              sample: '<profileid>'
            proxy:
              description: It is the pnp settings's proxy.
              returned: changed
              type: bool
              sample: false
            makeDefault:
              description: It is the pnp settings's makeDefault.
              returned: changed
              type: bool
              sample: false
            cert:
              description: It is the pnp settings's cert.
              returned: changed
              type: str
              sample: '<cert>'
            name:
              description: It is the pnp settings's name.
              returned: changed
              type: str
              sample: '<name>'

        token:
          description: It is the pnp settings's token.
          returned: changed
          type: str
          sample: '<token>'
        expiry:
          description: It is the pnp settings's expiry.
          returned: changed
          type: int
          sample: 0
        ccoUser:
          description: It is the pnp settings's ccoUser.
          returned: changed
          type: str
          sample: '<ccouser>'
        smartAccountId:
          description: It is the pnp settings's smartAccountId.
          returned: changed
          type: str
          sample: '<smartaccountid>'
        virtualAccountId:
          description: It is the pnp settings's virtualAccountId.
          returned: changed
          type: str
          sample: '<virtualaccountid>'
        autoSyncPeriod:
          description: It is the pnp settings's autoSyncPeriod.
          returned: changed
          type: int
          sample: 0
        syncResultStr:
          description: It is the pnp settings's syncResultStr.
          returned: changed
          type: str
          sample: '<syncresultstr>'

    taskTimeOuts:
      description: Settings's Task Time Outs.
      returned: changed
      type: dict
      contains:
        imageDownloadTimeOut:
          description: It is the pnp settings's imageDownloadTimeOut.
          returned: changed
          type: int
          sample: 0
        configTimeOut:
          description: It is the pnp settings's configTimeOut.
          returned: changed
          type: int
          sample: 0
        generalTimeOut:
          description: It is the pnp settings's generalTimeOut.
          returned: changed
          type: int
          sample: 0

    tenantId:
      description: Settings's Tenant Id.
      returned: changed
      type: str
      sample: '<tenantid>'
    aaaCredentials:
      description: Settings's Aaa Credentials.
      returned: changed
      type: dict
      contains:
        password:
          description: It is the pnp settings's password.
          returned: changed
          type: str
          sample: '*******'
        username:
          description: It is the pnp settings's username.
          returned: changed
          type: str
          sample: 'devnetuser'

    defaultProfile:
      description: Settings's Default Profile.
      returned: changed
      type: dict
      contains:
        fqdnAddresses:
          description: It is the pnp settings's fqdnAddresses.
          returned: changed
          type: list
        proxy:
          description: It is the pnp settings's proxy.
          returned: changed
          type: bool
          sample: false
        cert:
          description: It is the pnp settings's cert.
          returned: changed
          type: str
          sample: '<cert>'
        ipAddresses:
          description: It is the pnp settings's ipAddresses.
          returned: changed
          type: list
        port:
          description: It is the pnp settings's port.
          returned: changed
          type: int
          sample: 0

    acceptEula:
      description: Settings's acceptEula.
      returned: changed
      type: bool
      sample: false
    id:
      description: Settings's Id.
      returned: changed
      type: str
      sample: '478012'
    _id:
      description: Settings's Id.
      returned: changed
      type: str
      sample: '<_id>'
    version:
      description: Settings's version.
      returned: changed
      type: int
      sample: 0

"""

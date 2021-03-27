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
module: discovery
short_description: Manage Discovery objects of Discovery
description:
- Stops all the discoveries and removes them.
- Initiates Discovery with the given parameters.
- Stops or starts an existing Discovery.
- Returns the count of all available Discovery jobs.
- Stops the Discovery for the given Discovery ID and removes it. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns Discovery by Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Stops Discovery for the given range and removes them.
- Returns the Discovery by specified range.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  cdpLevel:
    description:
    - InventoryRequest's cdpLevel.
    - DiscoveryNIO's cdpLevel.
    type: int
  discoveryType:
    description:
    - InventoryRequest's DiscoveryType.
    - DiscoveryNIO's DiscoveryType.
    - Required for state create.
    type: str
    required: True
  enablePasswordList:
    description:
    - InventoryRequest's enablePasswordList (list of strings).
    - DiscoveryNIO's enablePasswordList.
    - Type list for state create.
    - Type str for state update.
    type: raw
  globalCredentialIdList:
    description:
    - InventoryRequest's globalCredentialIdList (list of strings).
    - DiscoveryNIO's globalCredentialIdList (list of strings).
    type: list
  httpReadCredential:
    description:
    - InventoryRequest's httpReadCredential.
    - DiscoveryNIO's httpReadCredential.
    type: dict
    suboptions:
      comments:
        description:
        - It is the Discovery's comments.
        type: str
      credentialType:
        description:
        - It is the Discovery's credentialType.
        type: str
      description:
        description:
        - It is the Discovery's description.
        type: str
      id:
        description:
        - It is the Discovery's id.
        type: str
      instanceTenantId:
        description:
        - It is the Discovery's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the Discovery's instanceUuid.
        type: str
      password:
        description:
        - It is the Discovery's password.
        type: str
      port:
        description:
        - It is the Discovery's port.
        type: int
      secure:
        description:
        - It is the Discovery's secure.
        type: bool
      username:
        description:
        - It is the Discovery's username.
        type: str

  httpWriteCredential:
    description:
    - InventoryRequest's httpWriteCredential.
    - DiscoveryNIO's httpWriteCredential.
    type: dict
    suboptions:
      comments:
        description:
        - It is the Discovery's comments.
        type: str
      credentialType:
        description:
        - It is the Discovery's credentialType.
        type: str
      description:
        description:
        - It is the Discovery's description.
        type: str
      id:
        description:
        - It is the Discovery's id.
        type: str
      instanceTenantId:
        description:
        - It is the Discovery's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the Discovery's instanceUuid.
        type: str
      password:
        description:
        - It is the Discovery's password.
        type: str
      port:
        description:
        - It is the Discovery's port.
        type: int
      secure:
        description:
        - It is the Discovery's secure.
        type: bool
      username:
        description:
        - It is the Discovery's username.
        type: str

  ipAddressList:
    description:
    - InventoryRequest's ipAddressList.
    - DiscoveryNIO's ipAddressList.
    - Required for state create.
    type: str
    required: True
  ipFilterList:
    description:
    - InventoryRequest's ipFilterList (list of strings).
    - DiscoveryNIO's ipFilterList.
    - Type list for state create.
    - Type str for state update.
    type: raw
  lldpLevel:
    description:
    - InventoryRequest's lldpLevel.
    - DiscoveryNIO's lldpLevel.
    type: int
  name:
    description:
    - InventoryRequest's name.
    - DiscoveryNIO's name.
    - Required for state create.
    type: str
    required: True
  netconfPort:
    description:
    - InventoryRequest's netconfPort.
    - DiscoveryNIO's netconfPort.
    type: str
  noAddNewDevice:
    description:
    - InventoryRequest's noAddNewDevice.
    type: bool
  parentDiscoveryId:
    description:
    - InventoryRequest's parentDiscoveryId.
    - DiscoveryNIO's parentDiscoveryId.
    type: str
  passwordList:
    description:
    - InventoryRequest's passwordList (list of strings).
    - DiscoveryNIO's passwordList.
    - Type list for state create.
    - Type str for state update.
    type: raw
  preferredMgmtIPMethod:
    description:
    - InventoryRequest's preferredMgmtIPMethod.
    - DiscoveryNIO's preferredMgmtIPMethod.
    type: str
  protocolOrder:
    description:
    - InventoryRequest's protocolOrder.
    - DiscoveryNIO's protocolOrder.
    type: str
  reDiscovery:
    description:
    - InventoryRequest's reDiscovery.
    type: bool
  retry:
    description:
    - InventoryRequest's retry.
    type: int
  snmpAuthPassphrase:
    description:
    - InventoryRequest's snmpAuthPassphrase.
    - DiscoveryNIO's snmpAuthPassphrase.
    type: str
  snmpAuthProtocol:
    description:
    - InventoryRequest's snmpAuthProtocol.
    - DiscoveryNIO's snmpAuthProtocol.
    type: str
  snmpMode:
    description:
    - InventoryRequest's snmpMode.
    - DiscoveryNIO's snmpMode.
    type: str
  snmpPrivPassphrase:
    description:
    - InventoryRequest's snmpPrivPassphrase.
    - DiscoveryNIO's snmpPrivPassphrase.
    type: str
  snmpPrivProtocol:
    description:
    - InventoryRequest's snmpPrivProtocol.
    - DiscoveryNIO's snmpPrivProtocol.
    type: str
  snmpROCommunity:
    description:
    - InventoryRequest's snmpROCommunity.
    type: str
  snmpROCommunityDesc:
    description:
    - InventoryRequest's snmpROCommunityDesc.
    type: str
  snmpRWCommunity:
    description:
    - InventoryRequest's snmpRWCommunity.
    type: str
  snmpRWCommunityDesc:
    description:
    - InventoryRequest's snmpRWCommunityDesc.
    type: str
  snmpUserName:
    description:
    - InventoryRequest's snmpUserName.
    - DiscoveryNIO's snmpUserName.
    type: str
  snmpVersion:
    description:
    - InventoryRequest's snmpVersion.
    - Required for state create.
    type: str
  timeout:
    description:
    - InventoryRequest's timeout.
    type: int
  updateMgmtIp:
    description:
    - InventoryRequest's updateMgmtIp.
    - DiscoveryNIO's updateMgmtIp.
    type: bool
  userNameList:
    description:
    - InventoryRequest's userNameList (list of strings).
    - DiscoveryNIO's userNameList.
    - Type list for state create.
    - Type str for state update.
    type: raw
  attributeInfo:
    description:
    - DiscoveryNIO's attributeInfo.
    type: dict
  deviceIds:
    description:
    - DiscoveryNIO's deviceIds.
    type: str
  discoveryCondition:
    description:
    - DiscoveryNIO's DiscoveryCondition.
    type: str
  discoveryStatus:
    description:
    - DiscoveryNIO's DiscoveryStatus.
    - Required for state update.
    type: str
  id:
    description:
    - DiscoveryNIO's id.
    - Discovery ID.
    type: str
    required: True
  isAutoCdp:
    description:
    - DiscoveryNIO's isAutoCdp.
    type: bool
  numDevices:
    description:
    - DiscoveryNIO's numDevices.
    type: int
  retryCount:
    description:
    - DiscoveryNIO's retryCount.
    type: int
  snmpRoCommunity:
    description:
    - DiscoveryNIO's snmpRoCommunity.
    type: str
  snmpRoCommunityDesc:
    description:
    - DiscoveryNIO's snmpRoCommunityDesc.
    type: str
  snmpRwCommunity:
    description:
    - DiscoveryNIO's snmpRwCommunity.
    type: str
  snmpRwCommunityDesc:
    description:
    - DiscoveryNIO's snmpRwCommunityDesc.
    type: str
  timeOut:
    description:
    - DiscoveryNIO's timeOut.
    type: int
  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool
  records_to_delete:
    description:
    - Number of records to delete.
    - Required for state delete.
    type: int
  start_index:
    description:
    - Start index.
    type: int
    required: True
  records_to_return:
    description:
    - Number of records to return.
    - Required for state query.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.discovery
# Reference by Internet resource
- name: Discovery reference
  description: Complete reference of the Discovery object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Discovery reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_all_discovery
  cisco.dnac.discovery:
    state: delete  # required

  
- name: start_discovery
  cisco.dnac.discovery:
    state: create  # required
    discoveryType: SomeValue  # string, required
    ipAddressList: SomeValue  # string, required
    name: SomeValue  # string, required
    snmpVersion: SomeValue  # string, required
    cdpLevel: 1  #  integer
    enablePasswordList:
    - SomeValue  # string
    globalCredentialIdList:
    - SomeValue  # string
    httpReadCredential:
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      password: SomeValue  # string
      port: 1  #  integer
      secure: True  # boolean
      username: SomeValue  # string
    httpWriteCredential:
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      password: SomeValue  # string
      port: 1  #  integer
      secure: True  # boolean
      username: SomeValue  # string
    ipFilterList:
    - SomeValue  # string
    lldpLevel: 1  #  integer
    netconfPort: SomeValue  # string
    noAddNewDevice: True  # boolean
    parentDiscoveryId: SomeValue  # string
    passwordList:
    - SomeValue  # string
    preferredMgmtIPMethod: SomeValue  # string
    protocolOrder: SomeValue  # string
    reDiscovery: True  # boolean
    retry: 1  #  integer
    snmpAuthPassphrase: SomeValue  # string
    snmpAuthProtocol: SomeValue  # string
    snmpMode: SomeValue  # string
    snmpPrivPassphrase: SomeValue  # string
    snmpPrivProtocol: SomeValue  # string
    snmpROCommunity: SomeValue  # string
    snmpROCommunityDesc: SomeValue  # string
    snmpRWCommunity: SomeValue  # string
    snmpRWCommunityDesc: SomeValue  # string
    snmpUserName: SomeValue  # string
    timeout: 1  #  integer
    updateMgmtIp: True  # boolean
    userNameList:
    - SomeValue  # string
  
- name: updates_discovery_by_id
  cisco.dnac.discovery:
    state: update  # required
    discoveryStatus: SomeValue  # string, required
    id: SomeValue  # string, required
    attributeInfo:
    cdpLevel: 1  #  integer
    deviceIds: SomeValue  # string
    discoveryCondition: SomeValue  # string
    discoveryType: SomeValue  # string
    enablePasswordList: SomeValue  # string
    globalCredentialIdList:
    - SomeValue  # string
    httpReadCredential:
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      password: SomeValue  # string
      port: 1  #  integer
      secure: True  # boolean
      username: SomeValue  # string
    httpWriteCredential:
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      password: SomeValue  # string
      port: 1  #  integer
      secure: True  # boolean
      username: SomeValue  # string
    ipAddressList: SomeValue  # string
    ipFilterList: SomeValue  # string
    isAutoCdp: True  # boolean
    lldpLevel: 1  #  integer
    name: SomeValue  # string
    netconfPort: SomeValue  # string
    numDevices: 1  #  integer
    parentDiscoveryId: SomeValue  # string
    passwordList: SomeValue  # string
    preferredMgmtIPMethod: SomeValue  # string
    protocolOrder: SomeValue  # string
    retryCount: 1  #  integer
    snmpAuthPassphrase: SomeValue  # string
    snmpAuthProtocol: SomeValue  # string
    snmpMode: SomeValue  # string
    snmpPrivPassphrase: SomeValue  # string
    snmpPrivProtocol: SomeValue  # string
    snmpRoCommunity: SomeValue  # string
    snmpRoCommunityDesc: SomeValue  # string
    snmpRwCommunity: SomeValue  # string
    snmpRwCommunityDesc: SomeValue  # string
    snmpUserName: SomeValue  # string
    timeOut: 1  #  integer
    updateMgmtIp: True  # boolean
    userNameList: SomeValue  # string
  
- name: get_count_of_all_discovery_jobs
  cisco.dnac.discovery:
    state: query  # required
    count: True  # boolean, required
  register: query_result
  
- name: delete_discovery_by_id
  cisco.dnac.discovery:
    state: delete  # required
    id: SomeValue  # string, required
  
- name: get_discovery_by_id
  cisco.dnac.discovery:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
- name: delete_discovery_by_specified_range
  cisco.dnac.discovery:
    state: delete  # required
    records_to_delete: 1  #  integer, required
    start_index: 1  #  integer, required
  
- name: get_discoveries_by_range
  cisco.dnac.discovery:
    state: query  # required
    records_to_return: 1  #  integer, required
    start_index: 1  #  integer, required
  register: query_result
  
"""

RETURN = """
delete_all_discovery:
    description: Stops all the discoveries and removes them.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Discovery's taskId.
          returned: success
          type: dict
        url:
          description: It is the Discovery's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

start_discovery:
    description: Initiates Discovery with the given parameters.
    returned: success
    type: dict
    contains:
    response:
      description: InventoryRequest's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Discovery's taskId.
          returned: success
          type: dict
        url:
          description: It is the Discovery's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: InventoryRequest's version.
      returned: success
      type: str
      sample: '1.0'

updates_discovery_by_id:
    description: Stops or starts an existing Discovery.
    returned: changed
    type: dict
    contains:
    response:
      description: DiscoveryNIO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the Discovery's taskId.
          returned: changed
          type: dict
        url:
          description: It is the Discovery's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: DiscoveryNIO's version.
      returned: changed
      type: str
      sample: '1.0'

get_count_of_all_discovery_jobs:
    description: Returns the count of all available Discovery jobs.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

delete_discovery_by_id:
    description: Stops the Discovery for the given Discovery ID and removes it. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Discovery's taskId.
          returned: success
          type: dict
        url:
          description: It is the Discovery's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

get_discovery_by_id:
    description: Returns Discovery by Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        attributeInfo:
          description: It is the Discovery's attributeInfo.
          returned: always
          type: dict
        cdpLevel:
          description: It is the Discovery's cdpLevel.
          returned: always
          type: int
          sample: 0
        deviceIds:
          description: It is the Discovery's deviceIds.
          returned: always
          type: str
          sample: '<deviceids>'
        discoveryCondition:
          description: It is the Discovery's DiscoveryCondition.
          returned: always
          type: str
          sample: '<discoverycondition>'
        discoveryStatus:
          description: It is the Discovery's DiscoveryStatus.
          returned: always
          type: str
          sample: '<discoverystatus>'
        discoveryType:
          description: It is the Discovery's DiscoveryType.
          returned: always
          type: str
          sample: '<discoverytype>'
        enablePasswordList:
          description: It is the Discovery's enablePasswordList.
          returned: always
          type: str
          sample: '<enablepasswordlist>'
        globalCredentialIdList:
          description: It is the Discovery's globalCredentialIdList.
          returned: always
          type: list
        httpReadCredential:
          description: It is the Discovery's httpReadCredential.
          returned: always
          type: dict
          contains:
            comments:
              description: It is the Discovery's comments.
              returned: always
              type: str
              sample: '<comments>'
            credentialType:
              description: It is the Discovery's credentialType.
              returned: always
              type: str
              sample: '<credentialtype>'
            description:
              description: It is the Discovery's description.
              returned: always
              type: str
              sample: '<description>'
            id:
              description: It is the Discovery's id.
              returned: always
              type: str
              sample: '478012'
            instanceTenantId:
              description: It is the Discovery's instanceTenantId.
              returned: always
              type: str
              sample: '<instancetenantid>'
            instanceUuid:
              description: It is the Discovery's instanceUuid.
              returned: always
              type: str
              sample: '<instanceuuid>'
            password:
              description: It is the Discovery's password.
              returned: always
              type: str
              sample: '*******'
            port:
              description: It is the Discovery's port.
              returned: always
              type: int
              sample: 0
            secure:
              description: It is the Discovery's secure.
              returned: always
              type: bool
              sample: false
            username:
              description: It is the Discovery's username.
              returned: always
              type: str
              sample: 'devnetuser'

        httpWriteCredential:
          description: It is the Discovery's httpWriteCredential.
          returned: always
          type: dict
          contains:
            comments:
              description: It is the Discovery's comments.
              returned: always
              type: str
              sample: '<comments>'
            credentialType:
              description: It is the Discovery's credentialType.
              returned: always
              type: str
              sample: '<credentialtype>'
            description:
              description: It is the Discovery's description.
              returned: always
              type: str
              sample: '<description>'
            id:
              description: It is the Discovery's id.
              returned: always
              type: str
              sample: '478012'
            instanceTenantId:
              description: It is the Discovery's instanceTenantId.
              returned: always
              type: str
              sample: '<instancetenantid>'
            instanceUuid:
              description: It is the Discovery's instanceUuid.
              returned: always
              type: str
              sample: '<instanceuuid>'
            password:
              description: It is the Discovery's password.
              returned: always
              type: str
              sample: '*******'
            port:
              description: It is the Discovery's port.
              returned: always
              type: int
              sample: 0
            secure:
              description: It is the Discovery's secure.
              returned: always
              type: bool
              sample: false
            username:
              description: It is the Discovery's username.
              returned: always
              type: str
              sample: 'devnetuser'

        id:
          description: It is the Discovery's id.
          returned: always
          type: str
          sample: '478012'
        ipAddressList:
          description: It is the Discovery's ipAddressList.
          returned: always
          type: str
          sample: '<ipaddresslist>'
        ipFilterList:
          description: It is the Discovery's ipFilterList.
          returned: always
          type: str
          sample: '<ipfilterlist>'
        isAutoCdp:
          description: It is the Discovery's isAutoCdp.
          returned: always
          type: bool
          sample: false
        lldpLevel:
          description: It is the Discovery's lldpLevel.
          returned: always
          type: int
          sample: 0
        name:
          description: It is the Discovery's name.
          returned: always
          type: str
          sample: '<name>'
        netconfPort:
          description: It is the Discovery's netconfPort.
          returned: always
          type: str
          sample: '<netconfport>'
        numDevices:
          description: It is the Discovery's numDevices.
          returned: always
          type: int
          sample: 0
        parentDiscoveryId:
          description: It is the Discovery's parentDiscoveryId.
          returned: always
          type: str
          sample: '<parentdiscoveryid>'
        passwordList:
          description: It is the Discovery's passwordList.
          returned: always
          type: str
          sample: '<passwordlist>'
        preferredMgmtIPMethod:
          description: It is the Discovery's preferredMgmtIPMethod.
          returned: always
          type: str
          sample: '<preferredmgmtipmethod>'
        protocolOrder:
          description: It is the Discovery's protocolOrder.
          returned: always
          type: str
          sample: '<protocolorder>'
        retryCount:
          description: It is the Discovery's retryCount.
          returned: always
          type: int
          sample: 0
        snmpAuthPassphrase:
          description: It is the Discovery's snmpAuthPassphrase.
          returned: always
          type: str
          sample: '<snmpauthpassphrase>'
        snmpAuthProtocol:
          description: It is the Discovery's snmpAuthProtocol.
          returned: always
          type: str
          sample: '<snmpauthprotocol>'
        snmpMode:
          description: It is the Discovery's snmpMode.
          returned: always
          type: str
          sample: '<snmpmode>'
        snmpPrivPassphrase:
          description: It is the Discovery's snmpPrivPassphrase.
          returned: always
          type: str
          sample: '<snmpprivpassphrase>'
        snmpPrivProtocol:
          description: It is the Discovery's snmpPrivProtocol.
          returned: always
          type: str
          sample: '<snmpprivprotocol>'
        snmpRoCommunity:
          description: It is the Discovery's snmpRoCommunity.
          returned: always
          type: str
          sample: '<snmprocommunity>'
        snmpRoCommunityDesc:
          description: It is the Discovery's snmpRoCommunityDesc.
          returned: always
          type: str
          sample: '<snmprocommunitydesc>'
        snmpRwCommunity:
          description: It is the Discovery's snmpRwCommunity.
          returned: always
          type: str
          sample: '<snmprwcommunity>'
        snmpRwCommunityDesc:
          description: It is the Discovery's snmpRwCommunityDesc.
          returned: always
          type: str
          sample: '<snmprwcommunitydesc>'
        snmpUserName:
          description: It is the Discovery's snmpUserName.
          returned: always
          type: str
          sample: '<snmpusername>'
        timeOut:
          description: It is the Discovery's timeOut.
          returned: always
          type: int
          sample: 0
        updateMgmtIp:
          description: It is the Discovery's updateMgmtIp.
          returned: always
          type: bool
          sample: false
        userNameList:
          description: It is the Discovery's userNameList.
          returned: always
          type: str
          sample: '<usernamelist>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

delete_discovery_by_specified_range:
    description: Stops Discovery for the given range and removes them.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Discovery's taskId.
          returned: success
          type: dict
        url:
          description: It is the Discovery's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

get_discoveries_by_range:
    description: Returns the Discovery by specified range.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        attributeInfo:
          description: It is the Discovery's attributeInfo.
          returned: always
          type: dict
        cdpLevel:
          description: It is the Discovery's cdpLevel.
          returned: always
          type: int
          sample: 0
        deviceIds:
          description: It is the Discovery's deviceIds.
          returned: always
          type: str
          sample: '<deviceids>'
        discoveryCondition:
          description: It is the Discovery's DiscoveryCondition.
          returned: always
          type: str
          sample: '<discoverycondition>'
        discoveryStatus:
          description: It is the Discovery's DiscoveryStatus.
          returned: always
          type: str
          sample: '<discoverystatus>'
        discoveryType:
          description: It is the Discovery's DiscoveryType.
          returned: always
          type: str
          sample: '<discoverytype>'
        enablePasswordList:
          description: It is the Discovery's enablePasswordList.
          returned: always
          type: str
          sample: '<enablepasswordlist>'
        globalCredentialIdList:
          description: It is the Discovery's globalCredentialIdList.
          returned: always
          type: list
        httpReadCredential:
          description: It is the Discovery's httpReadCredential.
          returned: always
          type: dict
          contains:
            comments:
              description: It is the Discovery's comments.
              returned: always
              type: str
              sample: '<comments>'
            credentialType:
              description: It is the Discovery's credentialType.
              returned: always
              type: str
              sample: '<credentialtype>'
            description:
              description: It is the Discovery's description.
              returned: always
              type: str
              sample: '<description>'
            id:
              description: It is the Discovery's id.
              returned: always
              type: str
              sample: '478012'
            instanceTenantId:
              description: It is the Discovery's instanceTenantId.
              returned: always
              type: str
              sample: '<instancetenantid>'
            instanceUuid:
              description: It is the Discovery's instanceUuid.
              returned: always
              type: str
              sample: '<instanceuuid>'
            password:
              description: It is the Discovery's password.
              returned: always
              type: str
              sample: '*******'
            port:
              description: It is the Discovery's port.
              returned: always
              type: int
              sample: 0
            secure:
              description: It is the Discovery's secure.
              returned: always
              type: bool
              sample: false
            username:
              description: It is the Discovery's username.
              returned: always
              type: str
              sample: 'devnetuser'

        httpWriteCredential:
          description: It is the Discovery's httpWriteCredential.
          returned: always
          type: dict
          contains:
            comments:
              description: It is the Discovery's comments.
              returned: always
              type: str
              sample: '<comments>'
            credentialType:
              description: It is the Discovery's credentialType.
              returned: always
              type: str
              sample: '<credentialtype>'
            description:
              description: It is the Discovery's description.
              returned: always
              type: str
              sample: '<description>'
            id:
              description: It is the Discovery's id.
              returned: always
              type: str
              sample: '478012'
            instanceTenantId:
              description: It is the Discovery's instanceTenantId.
              returned: always
              type: str
              sample: '<instancetenantid>'
            instanceUuid:
              description: It is the Discovery's instanceUuid.
              returned: always
              type: str
              sample: '<instanceuuid>'
            password:
              description: It is the Discovery's password.
              returned: always
              type: str
              sample: '*******'
            port:
              description: It is the Discovery's port.
              returned: always
              type: int
              sample: 0
            secure:
              description: It is the Discovery's secure.
              returned: always
              type: bool
              sample: false
            username:
              description: It is the Discovery's username.
              returned: always
              type: str
              sample: 'devnetuser'

        id:
          description: It is the Discovery's id.
          returned: always
          type: str
          sample: '478012'
        ipAddressList:
          description: It is the Discovery's ipAddressList.
          returned: always
          type: str
          sample: '<ipaddresslist>'
        ipFilterList:
          description: It is the Discovery's ipFilterList.
          returned: always
          type: str
          sample: '<ipfilterlist>'
        isAutoCdp:
          description: It is the Discovery's isAutoCdp.
          returned: always
          type: bool
          sample: false
        lldpLevel:
          description: It is the Discovery's lldpLevel.
          returned: always
          type: int
          sample: 0
        name:
          description: It is the Discovery's name.
          returned: always
          type: str
          sample: '<name>'
        netconfPort:
          description: It is the Discovery's netconfPort.
          returned: always
          type: str
          sample: '<netconfport>'
        numDevices:
          description: It is the Discovery's numDevices.
          returned: always
          type: int
          sample: 0
        parentDiscoveryId:
          description: It is the Discovery's parentDiscoveryId.
          returned: always
          type: str
          sample: '<parentdiscoveryid>'
        passwordList:
          description: It is the Discovery's passwordList.
          returned: always
          type: str
          sample: '<passwordlist>'
        preferredMgmtIPMethod:
          description: It is the Discovery's preferredMgmtIPMethod.
          returned: always
          type: str
          sample: '<preferredmgmtipmethod>'
        protocolOrder:
          description: It is the Discovery's protocolOrder.
          returned: always
          type: str
          sample: '<protocolorder>'
        retryCount:
          description: It is the Discovery's retryCount.
          returned: always
          type: int
          sample: 0
        snmpAuthPassphrase:
          description: It is the Discovery's snmpAuthPassphrase.
          returned: always
          type: str
          sample: '<snmpauthpassphrase>'
        snmpAuthProtocol:
          description: It is the Discovery's snmpAuthProtocol.
          returned: always
          type: str
          sample: '<snmpauthprotocol>'
        snmpMode:
          description: It is the Discovery's snmpMode.
          returned: always
          type: str
          sample: '<snmpmode>'
        snmpPrivPassphrase:
          description: It is the Discovery's snmpPrivPassphrase.
          returned: always
          type: str
          sample: '<snmpprivpassphrase>'
        snmpPrivProtocol:
          description: It is the Discovery's snmpPrivProtocol.
          returned: always
          type: str
          sample: '<snmpprivprotocol>'
        snmpRoCommunity:
          description: It is the Discovery's snmpRoCommunity.
          returned: always
          type: str
          sample: '<snmprocommunity>'
        snmpRoCommunityDesc:
          description: It is the Discovery's snmpRoCommunityDesc.
          returned: always
          type: str
          sample: '<snmprocommunitydesc>'
        snmpRwCommunity:
          description: It is the Discovery's snmpRwCommunity.
          returned: always
          type: str
          sample: '<snmprwcommunity>'
        snmpRwCommunityDesc:
          description: It is the Discovery's snmpRwCommunityDesc.
          returned: always
          type: str
          sample: '<snmprwcommunitydesc>'
        snmpUserName:
          description: It is the Discovery's snmpUserName.
          returned: always
          type: str
          sample: '<snmpusername>'
        timeOut:
          description: It is the Discovery's timeOut.
          returned: always
          type: int
          sample: 0
        updateMgmtIp:
          description: It is the Discovery's updateMgmtIp.
          returned: always
          type: bool
          sample: false
        userNameList:
          description: It is the Discovery's userNameList.
          returned: always
          type: str
          sample: '<usernamelist>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

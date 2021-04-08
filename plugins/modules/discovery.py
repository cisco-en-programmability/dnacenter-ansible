#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery
short_description: Manage Discovery objects of Discovery
description:
- Stops all the discoveries and removes them.
- Initiates Discovery with the given parameters.
- Stops or starts an existing Discovery.
- Returns the count of all available Discovery jobs.
- >
   Stops the Discovery for the given Discovery ID and removes it. Discovery ID can be obtained using the "Get
   Discoveries by range" API.
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
  register: nm_get_count_of_all_discovery_jobs

- name: delete_discovery_by_id
  cisco.dnac.discovery:
    state: delete  # required
    id: SomeValue  # string, required

- name: get_discovery_by_id
  cisco.dnac.discovery:
    state: query  # required
    id: SomeValue  # string, required
  register: nm_get_discovery_by_id

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
  register: nm_get_discoveries_by_range

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
  sample: discovery.delete_all_discovery
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery
short_description: Resource module for Discovery
description:
  - Manage operations create, update and delete of the resource Discovery.
  - Initiates discovery with the given parameters.
  - Stops all the discoveries and removes them. - > Stops the discovery for the given Discovery ID and removes it. Discovery
    ID can be obtained using the "Get Discoveries by range" API.
  - Stops or starts an existing discovery.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  attributeInfo:
    description: Discovery's attributeInfo.
    type: dict
  cdpLevel:
    description: CDP level to which neighbor devices are to be discovered.
    type: int
  deviceIds:
    description: Ids of the devices discovered in a discovery.
    type: str
  discoveryCondition:
    description: To indicate the discovery status. Available options Complete or In Progress.
    type: str
  discoveryStatus:
    description: Status of the discovery. Available options are Active, Inactive, Edit.
    type: str
  discoveryType:
    description: Type of the discovery. 'Single', 'Range', 'Multi Range', 'CDP', 'LLDP', 'CIDR'.
    type: str
  enablePasswordList:
    description: Enable Password of the devices to be discovered.
    elements: str
    type: list
  globalCredentialIdList:
    description: Global Credential Ids to be used for discovery.
    elements: str
    type: list
  httpReadCredential:
    description: Discovery's httpReadCredential.
    suboptions:
      password:
        description: HTTP(S) password.
        type: str
      port:
        description: HTTP(S) port.
        type: int
      secure:
        description: Flag for HTTPS.
        type: bool
      username:
        description: HTTP(S) username.
        type: str
    type: dict
  httpWriteCredential:
    description: Discovery's httpWriteCredential.
    suboptions:
      password:
        description: HTTP(S) password.
        type: str
      port:
        description: HTTP(S) port.
        type: int
      secure:
        description: Flag for HTTPS.
        type: bool
      username:
        description: HTTP(S) username.
        type: str
    type: dict
  id:
    description: Unique Discovery Id.
    type: str
  ipAddressList:
    description: IP Address of devices to be discovered. Ex '172.30.0.1' for SINGLE, CDP and LLDP; '72.30.0.1-172.30.0.4'
      for RANGE; '72.30.0.1-172.30.0.4,172.31.0.1-172.31.0.4' for MULTI RANGE; '172.30.0.1/20' for CIDR.
    type: str
  ipFilterList:
    description: IP Addresses of the devices to be filtered out during discovery.
    elements: str
    type: list
  isAutoCdp:
    description: Flag to mention if CDP discovery or not.
    type: bool
  lldpLevel:
    description: LLDP level to which neighbor devices to be discovered.
    type: int
  name:
    description: Name of the discovery.
    type: str
  netconfPort:
    description: Netconf Port. It will need valid SSH credentials to work.
    type: str
  numDevices:
    description: Number of devices discovered in the discovery.
    type: int
  parentDiscoveryId:
    description: Parent Discovery Id from which the discovery was initiated.
    type: str
  passwordList:
    description: Password of the devices to be discovered.
    elements: str
    type: list
  preferredMgmtIPMethod:
    description: Preferred Management IP Method.'None' or 'UseLoopBack'. Default is 'None'.
    type: str
  protocolOrder:
    description: Order of protocol (ssh/telnet) in which device connection will be tried. Ex 'telnet' only telnet; 'ssh,telnet'
      ssh with higher order than telnet.
    type: str
  retry:
    description: Number of times to try establishing connection to device.
    type: int
  retryCount:
    description: Number of times to try establishing connection to device.
    type: int
  snmpAuthPassphrase:
    description: Auth passphrase for SNMP.
    type: str
  snmpAuthProtocol:
    description: SNMP auth protocol. SHA' or 'MD5'.
    type: str
  snmpMode:
    description: Mode of SNMP. 'AUTHPRIV' or 'AUTHNOPRIV' or 'NOAUTHNOPRIV'.
    type: str
  snmpPrivPassphrase:
    description: Pass phrase for SNMP privacy.
    type: str
  snmpPrivProtocol:
    description: SNMP privacy protocol. 'AES128'.
    type: str
  snmpRoCommunity:
    description: SNMP RO community of the devices to be discovered.
    type: str
  snmpRoCommunityDesc:
    description: Description for SNMP RO community.
    type: str
  snmpRwCommunity:
    description: SNMP RW community of the devices to be discovered.
    type: str
  snmpRwCommunityDesc:
    description: Description for SNMP RW community.
    type: str
  snmpUserName:
    description: SNMP username of the device.
    type: str
  snmpVersion:
    description: Version of SNMP. V2 or v3.
    type: str
  timeout:
    description: Time to wait for device response in seconds.
    type: int
  updateMgmtIp:
    description: Updates Management IP if multiple IPs are available for a device. If set to true, when a device is rediscovered
      with a different IP, the management IP is updated. Default value is false.
    type: bool
  userNameList:
    description: Username of the devices to be discovered.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Discovery StartDiscovery
    description: Complete reference of the StartDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!start-discovery
  - name: Cisco DNA Center documentation for Discovery DeleteAllDiscovery
    description: Complete reference of the DeleteAllDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-all-discovery
  - name: Cisco DNA Center documentation for Discovery DeleteDiscoveryById
    description: Complete reference of the DeleteDiscoveryById API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-discovery-by-id
  - name: Cisco DNA Center documentation for Discovery UpdatesAnExistingDiscoveryBySpecifiedId
    description: Complete reference of the UpdatesAnExistingDiscoveryBySpecifiedId API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-an-existing-discovery-by-specified-id
notes:
  - SDK Method used are
    discovery.Discovery.delete_discovery_by_id,
    discovery.Discovery.start_discovery,
    discovery.Discovery.updates_discovery_by_id,
  - Paths used are
    post /dna/intent/api/v1/discovery,
    delete /dna/intent/api/v1/discovery,
    delete /dna/intent/api/v1/discovery/{id},
    put /dna/intent/api/v1/discovery,
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
- name: Create
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cdpLevel: 0
    discoveryType: string
    enablePasswordList:
      - string
    globalCredentialIdList:
      - string
    httpReadCredential:
      password: string
      port: 0
      secure: true
      username: string
    httpWriteCredential:
      password: string
      port: 0
      secure: true
      username: string
    ipAddressList: string
    ipFilterList:
      - string
    lldpLevel: 0
    name: string
    netconfPort: string
    passwordList:
      - string
    preferredMgmtIPMethod: string
    protocolOrder: string
    retry: 0
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpRoCommunity: string
    snmpRoCommunityDesc: string
    snmpRwCommunity: string
    snmpRwCommunityDesc: string
    snmpUserName: string
    snmpVersion: string
    timeout: 0
    userNameList:
      - string
- name: Update all
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    attributeInfo: {}
    cdpLevel: 0
    deviceIds: string
    discoveryCondition: string
    discoveryStatus: string
    discoveryType: string
    enablePasswordList: string
    globalCredentialIdList:
      - string
    httpReadCredential:
      comments: string
      credentialType: string
      description: string
      id: string
      instanceTenantId: string
      instanceUuid: string
      password: string
      port: 0
      secure: true
      username: string
    httpWriteCredential:
      comments: string
      credentialType: string
      description: string
      id: string
      instanceTenantId: string
      instanceUuid: string
      password: string
      port: 0
      secure: true
      username: string
    id: string
    ipAddressList: string
    ipFilterList: string
    isAutoCdp: true
    lldpLevel: 0
    name: string
    netconfPort: string
    numDevices: 0
    parentDiscoveryId: string
    passwordList: string
    preferredMgmtIPMethod: string
    protocolOrder: string
    retryCount: 0
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpRoCommunity: string
    snmpRoCommunityDesc: string
    snmpRwCommunity: string
    snmpRwCommunityDesc: string
    snmpUserName: string
    timeout: 0
    updateMgmtIp: true
    userNameList: string
- name: Delete by id
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

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
module: sda_border_device
short_description: Manage SdaBorderDevice objects of Sda
description:
- Gets border device detail from SDA Fabric.
- Deletes border device from SDA Fabric.
- Adds border device in SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_ipaddress:
    description:
    - Device IP Address.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      deviceManagementIpAddress:
        description:
        - It is the sda border device's deviceManagementIpAddress.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda border device's siteNameHierarchy.
        type: str
      externalDomainRoutingProtocolName:
        description:
        - It is the sda border device's externalDomainRoutingProtocolName.
        type: str
      externalConnectivityIpPoolName:
        description:
        - It is the sda border device's externalConnectivityIpPoolName.
        type: str
      internalAutonomouSystemNumber:
        description:
        - It is the sda border device's internalAutonomouSystemNumber.
        type: str
      borderSessionType:
        description:
        - It is the sda border device's borderSessionType.
        type: str
      connectedToInternet:
        description:
        - It is the sda border device's connectedToInternet.
        type: bool
      externalConnectivitySettings:
        description:
        - It is the sda border device's externalConnectivitySettings.
        type: list
        elements: dict
        suboptions:
          interfaceName:
            description:
            - It is the sda border device's interfaceName.
            type: str
          externalAutonomouSystemNumber:
            description:
            - It is the sda border device's externalAutonomouSystemNumber.
            type: str
          l3Handoff:
            description:
            - It is the sda border device's l3Handoff.
            type: list
            elements: dict
            suboptions:
              virtualNetwork:
                description:
                - It is the sda border device's virtualNetwork.
                type: dict
                suboptions:
                  virtualNetworkName:
                    description:
                    - It is the sda border device's virtualNetworkName.
                    type: str





requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_border_device
# Reference by Internet resource
- name: SdaBorderDevice reference
  description: Complete reference of the SdaBorderDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaBorderDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: gets_border_device_detail
  cisco.dnac.sda_border_device:
    state: query  # required
    device_ipaddress: SomeValue  # string, required
  register: query_result
  
- name: deletes_border_device
  cisco.dnac.sda_border_device:
    state: delete  # required
    device_ipaddress: SomeValue  # string, required
  
- name: adds_border_device
  cisco.dnac.sda_border_device:
    state: create  # required
    payload:  # required
    - deviceManagementIpAddress: SomeValue  # string
      siteNameHierarchy: SomeValue  # string
      externalDomainRoutingProtocolName: SomeValue  # string
      externalConnectivityIpPoolName: SomeValue  # string
      internalAutonomouSystemNumber: SomeValue  # string
      borderSessionType: SomeValue  # string
      connectedToInternet: True  # boolean
      externalConnectivitySettings:
      - interfaceName: SomeValue  # string
        externalAutonomouSystemNumber: SomeValue  # string
        l3Handoff:
        - virtualNetwork:
            virtualNetworkName: SomeValue  # string
  
"""

RETURN = """
gets_border_device_detail:
    description: Gets border device detail from SDA Fabric.
    returned: always
    type: dict
    contains:
      status:
      description: Status, property of the response body.
      returned: always
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: always
      type: str
      sample: '<description>'
    payload:
      description: Payload, property of the response body.
      returned: always
      type: dict
      contains:
        id:
          description: It is the sda border device's id.
          returned: always
          type: str
          sample: '478012'
        instanceId:
          description: It is the sda border device's instanceId.
          returned: always
          type: int
          sample: 0
        authEntityId:
          description: It is the sda border device's authEntityId.
          returned: always
          type: int
          sample: 0
        displayName:
          description: It is the sda border device's displayName.
          returned: always
          type: str
          sample: '<displayname>'
        authEntityClass:
          description: It is the sda border device's authEntityClass.
          returned: always
          type: int
          sample: 0
        instanceTenantId:
          description: It is the sda border device's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        deployPending:
          description: It is the sda border device's deployPending.
          returned: always
          type: str
          sample: '<deploypending>'
        instanceVersion:
          description: It is the sda border device's instanceVersion.
          returned: always
          type: int
          sample: 0
        createTime:
          description: It is the sda border device's createTime.
          returned: always
          type: int
          sample: 0
        deployed:
          description: It is the sda border device's deployed.
          returned: always
          type: bool
          sample: false
        isSeeded:
          description: It is the sda border device's isSeeded.
          returned: always
          type: bool
          sample: false
        isStale:
          description: It is the sda border device's isStale.
          returned: always
          type: bool
          sample: false
        lastUpdateTime:
          description: It is the sda border device's lastUpdateTime.
          returned: always
          type: int
          sample: 0
        name:
          description: It is the sda border device's name.
          returned: always
          type: str
          sample: '<name>'
        namespace:
          description: It is the sda border device's namespace.
          returned: always
          type: str
          sample: '<namespace>'
        provisioningState:
          description: It is the sda border device's provisioningState.
          returned: always
          type: str
          sample: '<provisioningstate>'
        resourceVersion:
          description: It is the sda border device's resourceVersion.
          returned: always
          type: int
          sample: 0
        targetIdList:
          description: It is the sda border device's targetIdList.
          returned: always
          type: list
        type:
          description: It is the sda border device's type.
          returned: always
          type: str
          sample: '<type>'
        cfsChangeInfo:
          description: It is the sda border device's cfsChangeInfo.
          returned: always
          type: list
        customProvisions:
          description: It is the sda border device's customProvisions.
          returned: always
          type: list
        configs:
          description: It is the sda border device's configs.
          returned: always
          type: list
        managedSites:
          description: It is the sda border device's managedSites.
          returned: always
          type: list
        networkDeviceId:
          description: It is the sda border device's networkDeviceId.
          returned: always
          type: str
          sample: '<networkdeviceid>'
        roles:
          description: It is the sda border device's roles.
          returned: always
          type: list
        saveWanConnectivityDetailsOnly:
          description: It is the sda border device's saveWanConnectivityDetailsOnly.
          returned: always
          type: bool
          sample: false
        siteId:
          description: It is the sda border device's siteId.
          returned: always
          type: str
          sample: '<siteid>'
        akcSettingsCfs:
          description: It is the sda border device's akcSettingsCfs.
          returned: always
          type: list
        deviceInterfaceInfo:
          description: It is the sda border device's deviceInterfaceInfo.
          returned: always
          type: list
        deviceSettings:
          description: It is the sda border device's deviceSettings.
          returned: always
          type: dict
          contains:
            id:
              description: It is the sda border device's id.
              returned: always
              type: str
              sample: '478012'
            instanceId:
              description: It is the sda border device's instanceId.
              returned: always
              type: int
              sample: 0
            displayName:
              description: It is the sda border device's displayName.
              returned: always
              type: str
              sample: '<displayname>'
            instanceTenantId:
              description: It is the sda border device's instanceTenantId.
              returned: always
              type: str
              sample: '<instancetenantid>'
            deployPending:
              description: It is the sda border device's deployPending.
              returned: always
              type: str
              sample: '<deploypending>'
            instanceVersion:
              description: It is the sda border device's instanceVersion.
              returned: always
              type: int
              sample: 0
            connectedTo:
              description: It is the sda border device's connectedTo.
              returned: always
              type: list
            cpu:
              description: It is the sda border device's cpu.
              returned: always
              type: int
              sample: 0
            dhcpEnabled:
              description: It is the sda border device's dhcpEnabled.
              returned: always
              type: bool
              sample: false
            externalConnectivityIpPool:
              description: It is the sda border device's externalConnectivityIpPool.
              returned: always
              type: str
              sample: '<externalconnectivityippool>'
            externalDomainRoutingProtocol:
              description: It is the sda border device's externalDomainRoutingProtocol.
              returned: always
              type: str
              sample: '<externaldomainroutingprotocol>'
            internalDomainProtocolNumber:
              description: It is the sda border device's internalDomainProtocolNumber.
              returned: always
              type: str
              sample: '<internaldomainprotocolnumber>'
            memory:
              description: It is the sda border device's memory.
              returned: always
              type: int
              sample: 0
            nodeType:
              description: It is the sda border device's nodeType.
              returned: always
              type: list
            storage:
              description: It is the sda border device's storage.
              returned: always
              type: int
              sample: 0
            extConnectivitySettings:
              description: It is the sda border device's extConnectivitySettings.
              returned: always
              type: list
              contains:
                id:
                  description: It is the sda border device's id.
                  returned: always
                  type: str
                  sample: '478012'
                instanceId:
                  description: It is the sda border device's instanceId.
                  returned: always
                  type: int
                  sample: 0
                displayName:
                  description: It is the sda border device's displayName.
                  returned: always
                  type: str
                  sample: '<displayname>'
                instanceTenantId:
                  description: It is the sda border device's instanceTenantId.
                  returned: always
                  type: str
                  sample: '<instancetenantid>'
                deployPending:
                  description: It is the sda border device's deployPending.
                  returned: always
                  type: str
                  sample: '<deploypending>'
                instanceVersion:
                  description: It is the sda border device's instanceVersion.
                  returned: always
                  type: int
                  sample: 0
                externalDomainProtocolNumber:
                  description: It is the sda border device's externalDomainProtocolNumber.
                  returned: always
                  type: str
                  sample: '<externaldomainprotocolnumber>'
                interfaceUuid:
                  description: It is the sda border device's interfaceUuid.
                  returned: always
                  type: str
                  sample: '<interfaceuuid>'
                policyPropagationEnabled:
                  description: It is the sda border device's policyPropagationEnabled.
                  returned: always
                  type: bool
                  sample: false
                policySgtTag:
                  description: It is the sda border device's policySgtTag.
                  returned: always
                  type: int
                  sample: 0
                l2Handoff:
                  description: It is the sda border device's l2Handoff.
                  returned: always
                  type: list
                l3Handoff:
                  description: It is the sda border device's l3Handoff.
                  returned: always
                  type: list
                  contains:
                    id:
                      description: It is the sda border device's id.
                      returned: always
                      type: str
                      sample: '478012'
                    instanceId:
                      description: It is the sda border device's instanceId.
                      returned: always
                      type: int
                      sample: 0
                    displayName:
                      description: It is the sda border device's displayName.
                      returned: always
                      type: str
                      sample: '<displayname>'
                    instanceTenantId:
                      description: It is the sda border device's instanceTenantId.
                      returned: always
                      type: str
                      sample: '<instancetenantid>'
                    deployPending:
                      description: It is the sda border device's deployPending.
                      returned: always
                      type: str
                      sample: '<deploypending>'
                    instanceVersion:
                      description: It is the sda border device's instanceVersion.
                      returned: always
                      type: int
                      sample: 0
                    localIpAddress:
                      description: It is the sda border device's localIpAddress.
                      returned: always
                      type: str
                      sample: '<localipaddress>'
                    remoteIpAddress:
                      description: It is the sda border device's remoteIpAddress.
                      returned: always
                      type: str
                      sample: '<remoteipaddress>'
                    vlanId:
                      description: It is the sda border device's vlanId.
                      returned: always
                      type: int
                      sample: 0
                    virtualNetwork:
                      description: It is the sda border device's virtualNetwork.
                      returned: always
                      type: dict
                      contains:
                        idRef:
                          description: It is the sda border device's idRef.
                          returned: always
                          type: str
                          sample: '<idref>'




        networkWideSettings:
          description: It is the sda border device's networkWideSettings.
          returned: always
          type: dict
          contains:
            id:
              description: It is the sda border device's id.
              returned: always
              type: str
              sample: '478012'
            instanceId:
              description: It is the sda border device's instanceId.
              returned: always
              type: int
              sample: 0
            displayName:
              description: It is the sda border device's displayName.
              returned: always
              type: str
              sample: '<displayname>'
            instanceTenantId:
              description: It is the sda border device's instanceTenantId.
              returned: always
              type: str
              sample: '<instancetenantid>'
            deployPending:
              description: It is the sda border device's deployPending.
              returned: always
              type: str
              sample: '<deploypending>'
            instanceVersion:
              description: It is the sda border device's instanceVersion.
              returned: always
              type: int
              sample: 0
            aaa:
              description: It is the sda border device's aaa.
              returned: always
              type: list
            cmx:
              description: It is the sda border device's cmx.
              returned: always
              type: list
            dhcp:
              description: It is the sda border device's dhcp.
              returned: always
              type: list
              contains:
                id:
                  description: It is the sda border device's id.
                  returned: always
                  type: str
                  sample: '478012'
                ipAddress:
                  description: It is the sda border device's ipAddress.
                  returned: always
                  type: dict
                  contains:
                    id:
                      description: It is the sda border device's id.
                      returned: always
                      type: str
                      sample: '478012'
                    paddedAddress:
                      description: It is the sda border device's paddedAddress.
                      returned: always
                      type: str
                      sample: '<paddedaddress>'
                    addressType:
                      description: It is the sda border device's addressType.
                      returned: always
                      type: str
                      sample: '<addresstype>'
                    address:
                      description: It is the sda border device's address.
                      returned: always
                      type: str
                      sample: '<address>'


            dns:
              description: It is the sda border device's dns.
              returned: always
              type: list
              contains:
                id:
                  description: It is the sda border device's id.
                  returned: always
                  type: str
                  sample: '478012'
                domainName:
                  description: It is the sda border device's domainName.
                  returned: always
                  type: str
                  sample: '<domainname>'
                ip:
                  description: It is the sda border device's ip.
                  returned: always
                  type: dict
                  contains:
                    id:
                      description: It is the sda border device's id.
                      returned: always
                      type: str
                      sample: '478012'
                    paddedAddress:
                      description: It is the sda border device's paddedAddress.
                      returned: always
                      type: str
                      sample: '<paddedaddress>'
                    addressType:
                      description: It is the sda border device's addressType.
                      returned: always
                      type: str
                      sample: '<addresstype>'
                    address:
                      description: It is the sda border device's address.
                      returned: always
                      type: str
                      sample: '<address>'


            ldap:
              description: It is the sda border device's ldap.
              returned: always
              type: list
            nativeVlan:
              description: It is the sda border device's nativeVlan.
              returned: always
              type: list
            netflow:
              description: It is the sda border device's netflow.
              returned: always
              type: list
            ntp:
              description: It is the sda border device's ntp.
              returned: always
              type: list
            snmp:
              description: It is the sda border device's snmp.
              returned: always
              type: list
            syslogs:
              description: It is the sda border device's syslogs.
              returned: always
              type: list

        otherDevice:
          description: It is the sda border device's otherDevice.
          returned: always
          type: list
        transitNetworks:
          description: It is the sda border device's transitNetworks.
          returned: always
          type: list
          contains:
            idRef:
              description: It is the sda border device's idRef.
              returned: always
              type: str
              sample: '<idref>'

        virtualNetwork:
          description: It is the sda border device's virtualNetwork.
          returned: always
          type: list
        wlan:
          description: It is the sda border device's wlan.
          returned: always
          type: list


deletes_border_device:
    description: Deletes border device from SDA Fabric.
    returned: success
    type: dict
    contains:
      status:
      description: Status, property of the response body.
      returned: success
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: success
      type: str
      sample: '<description>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'

adds_border_device:
    description: Adds border device in SDA Fabric.
    returned: success
    type: dict
    contains:
      status:
      description: Status, property of the response body.
      returned: success
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: success
      type: str
      sample: '<description>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'

"""

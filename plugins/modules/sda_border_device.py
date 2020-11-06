#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: sda_border_device
short_description: Manage SdaBorderDevice objects of Sda
description:
- Gets border device detail from SDA Fabric.
- Deletes border device from SDA Fabric.
- Adds border device in SDA Fabric.
version_added: '1.0'
author: first last (@GitHubID)
options:
    device_ipaddress:
        description:
        - Device IP Address.
        type: str
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Gets border device detail from SDA Fabric.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        payload:
            description: Payload, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the sda border device's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceId:
                    description: It is the sda border device's instanceId.
                    returned: success,changed,always
                    type: int
                    sample: 0
                authEntityId:
                    description: It is the sda border device's authEntityId.
                    returned: success,changed,always
                    type: int
                    sample: 0
                displayName:
                    description: It is the sda border device's displayName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authEntityClass:
                    description: It is the sda border device's authEntityClass.
                    returned: success,changed,always
                    type: int
                    sample: 0
                instanceTenantId:
                    description: It is the sda border device's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deployPending:
                    description: It is the sda border device's deployPending.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceVersion:
                    description: It is the sda border device's instanceVersion.
                    returned: success,changed,always
                    type: int
                    sample: 0
                createTime:
                    description: It is the sda border device's createTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                deployed:
                    description: It is the sda border device's deployed.
                    returned: success,changed,always
                    type: bool
                    sample: false
                isSeeded:
                    description: It is the sda border device's isSeeded.
                    returned: success,changed,always
                    type: bool
                    sample: false
                isStale:
                    description: It is the sda border device's isStale.
                    returned: success,changed,always
                    type: bool
                    sample: false
                lastUpdateTime:
                    description: It is the sda border device's lastUpdateTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the sda border device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                namespace:
                    description: It is the sda border device's namespace.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                provisioningState:
                    description: It is the sda border device's provisioningState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                resourceVersion:
                    description: It is the sda border device's resourceVersion.
                    returned: success,changed,always
                    type: int
                    sample: 0
                targetIdList:
                    description: It is the sda border device's targetIdList.
                    returned: success,changed,always
                    type: list
                type:
                    description: It is the sda border device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cfsChangeInfo:
                    description: It is the sda border device's cfsChangeInfo.
                    returned: success,changed,always
                    type: list
                customProvisions:
                    description: It is the sda border device's customProvisions.
                    returned: success,changed,always
                    type: list
                configs:
                    description: It is the sda border device's configs.
                    returned: success,changed,always
                    type: list
                managedSites:
                    description: It is the sda border device's managedSites.
                    returned: success,changed,always
                    type: list
                networkDeviceId:
                    description: It is the sda border device's networkDeviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                roles:
                    description: It is the sda border device's roles.
                    returned: success,changed,always
                    type: list
                saveWanConnectivityDetailsOnly:
                    description: It is the sda border device's saveWanConnectivityDetailsOnly.
                    returned: success,changed,always
                    type: bool
                    sample: false
                siteId:
                    description: It is the sda border device's siteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                akcSettingsCfs:
                    description: It is the sda border device's akcSettingsCfs.
                    returned: success,changed,always
                    type: list
                deviceInterfaceInfo:
                    description: It is the sda border device's deviceInterfaceInfo.
                    returned: success,changed,always
                    type: list
                deviceSettings:
                    description: It is the sda border device's deviceSettings.
                    returned: success,changed,always
                    type: dict
                    contains:
                        id:
                            description: It is the sda border device's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceId:
                            description: It is the sda border device's instanceId.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        displayName:
                            description: It is the sda border device's displayName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceTenantId:
                            description: It is the sda border device's instanceTenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deployPending:
                            description: It is the sda border device's deployPending.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceVersion:
                            description: It is the sda border device's instanceVersion.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        connectedTo:
                            description: It is the sda border device's connectedTo.
                            returned: success,changed,always
                            type: list
                        cpu:
                            description: It is the sda border device's cpu.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        dhcpEnabled:
                            description: It is the sda border device's dhcpEnabled.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        externalConnectivityIpPool:
                            description: It is the sda border device's externalConnectivityIpPool.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        externalDomainRoutingProtocol:
                            description: It is the sda border device's externalDomainRoutingProtocol.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        internalDomainProtocolNumber:
                            description: It is the sda border device's internalDomainProtocolNumber.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        memory:
                            description: It is the sda border device's memory.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        nodeType:
                            description: It is the sda border device's nodeType.
                            returned: success,changed,always
                            type: list
                        storage:
                            description: It is the sda border device's storage.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        extConnectivitySettings:
                            description: It is the sda border device's extConnectivitySettings.
                            returned: success,changed,always
                            type: list
                            contains:
                                id:
                                    description: It is the sda border device's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                instanceId:
                                    description: It is the sda border device's instanceId.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                displayName:
                                    description: It is the sda border device's displayName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                instanceTenantId:
                                    description: It is the sda border device's instanceTenantId.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                deployPending:
                                    description: It is the sda border device's deployPending.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                instanceVersion:
                                    description: It is the sda border device's instanceVersion.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                externalDomainProtocolNumber:
                                    description: It is the sda border device's externalDomainProtocolNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceUuid:
                                    description: It is the sda border device's interfaceUuid.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                policyPropagationEnabled:
                                    description: It is the sda border device's policyPropagationEnabled.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                policySgtTag:
                                    description: It is the sda border device's policySgtTag.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                l2Handoff:
                                    description: It is the sda border device's l2Handoff.
                                    returned: success,changed,always
                                    type: list
                                l3Handoff:
                                    description: It is the sda border device's l3Handoff.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        id:
                                            description: It is the sda border device's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        instanceId:
                                            description: It is the sda border device's instanceId.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        displayName:
                                            description: It is the sda border device's displayName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        instanceTenantId:
                                            description: It is the sda border device's instanceTenantId.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        deployPending:
                                            description: It is the sda border device's deployPending.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        instanceVersion:
                                            description: It is the sda border device's instanceVersion.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        localIpAddress:
                                            description: It is the sda border device's localIpAddress.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        remoteIpAddress:
                                            description: It is the sda border device's remoteIpAddress.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vlanId:
                                            description: It is the sda border device's vlanId.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        virtualNetwork:
                                            description: It is the sda border device's virtualNetwork.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                idRef:
                                                    description: It is the sda border device's idRef.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'




                networkWideSettings:
                    description: It is the sda border device's networkWideSettings.
                    returned: success,changed,always
                    type: dict
                    contains:
                        id:
                            description: It is the sda border device's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceId:
                            description: It is the sda border device's instanceId.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        displayName:
                            description: It is the sda border device's displayName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceTenantId:
                            description: It is the sda border device's instanceTenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deployPending:
                            description: It is the sda border device's deployPending.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceVersion:
                            description: It is the sda border device's instanceVersion.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        aaa:
                            description: It is the sda border device's aaa.
                            returned: success,changed,always
                            type: list
                        cmx:
                            description: It is the sda border device's cmx.
                            returned: success,changed,always
                            type: list
                        dhcp:
                            description: It is the sda border device's dhcp.
                            returned: success,changed,always
                            type: list
                            contains:
                                id:
                                    description: It is the sda border device's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipAddress:
                                    description: It is the sda border device's ipAddress.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        id:
                                            description: It is the sda border device's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        paddedAddress:
                                            description: It is the sda border device's paddedAddress.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        addressType:
                                            description: It is the sda border device's addressType.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        address:
                                            description: It is the sda border device's address.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'


                        dns:
                            description: It is the sda border device's dns.
                            returned: success,changed,always
                            type: list
                            contains:
                                id:
                                    description: It is the sda border device's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                domainName:
                                    description: It is the sda border device's domainName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ip:
                                    description: It is the sda border device's ip.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        id:
                                            description: It is the sda border device's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        paddedAddress:
                                            description: It is the sda border device's paddedAddress.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        addressType:
                                            description: It is the sda border device's addressType.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        address:
                                            description: It is the sda border device's address.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'


                        ldap:
                            description: It is the sda border device's ldap.
                            returned: success,changed,always
                            type: list
                        nativeVlan:
                            description: It is the sda border device's nativeVlan.
                            returned: success,changed,always
                            type: list
                        netflow:
                            description: It is the sda border device's netflow.
                            returned: success,changed,always
                            type: list
                        ntp:
                            description: It is the sda border device's ntp.
                            returned: success,changed,always
                            type: list
                        snmp:
                            description: It is the sda border device's snmp.
                            returned: success,changed,always
                            type: list
                        syslogs:
                            description: It is the sda border device's syslogs.
                            returned: success,changed,always
                            type: list

                otherDevice:
                    description: It is the sda border device's otherDevice.
                    returned: success,changed,always
                    type: list
                transitNetworks:
                    description: It is the sda border device's transitNetworks.
                    returned: success,changed,always
                    type: list
                    contains:
                        idRef:
                            description: It is the sda border device's idRef.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                virtualNetwork:
                    description: It is the sda border device's virtualNetwork.
                    returned: success,changed,always
                    type: list
                wlan:
                    description: It is the sda border device's wlan.
                    returned: success,changed,always
                    type: list


data_1:
    description: Deletes border device from SDA Fabric.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Adds border device in SDA Fabric.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.sda_border_device import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
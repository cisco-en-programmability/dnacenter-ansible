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
version_added: '1.0'
author: first last (@GitHubID)
options:
    cdp_level:
        description:
        - InventoryRequest's cdpLevel.
        type: int
    discovery_type:
        description:
        - InventoryRequest's DiscoveryType.
        type: str
        required: True
    enable_password_list:
        description:
        - InventoryRequest's enablePasswordList (list of strings).
        type: list
    global_credential_id_list:
        description:
        - InventoryRequest's globalCredentialIdList (list of strings).
        type: list
    http_read_credential:
        description:
        - InventoryRequest's httpReadCredential.
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

    http_write_credential:
        description:
        - InventoryRequest's httpWriteCredential.
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

    ip_address_list:
        description:
        - InventoryRequest's ipAddressList.
        type: str
        required: True
    ip_filter_list:
        description:
        - InventoryRequest's ipFilterList (list of strings).
        type: list
    lldp_level:
        description:
        - InventoryRequest's lldpLevel.
        type: int
    name:
        description:
        - InventoryRequest's name.
        type: str
        required: True
    netconf_port:
        description:
        - InventoryRequest's netconfPort.
        type: str
    no_add_new_device:
        description:
        - InventoryRequest's noAddNewDevice.
        type: bool
    parent_discovery_id:
        description:
        - InventoryRequest's parentDiscoveryId.
        type: str
    password_list:
        description:
        - InventoryRequest's passwordList (list of strings).
        type: list
    preferred_mgmt_ipmethod:
        description:
        - InventoryRequest's preferredMgmtIPMethod.
        type: str
    protocol_order:
        description:
        - InventoryRequest's protocolOrder.
        type: str
    re_discovery:
        description:
        - InventoryRequest's reDiscovery.
        type: bool
    retry:
        description:
        - InventoryRequest's retry.
        type: int
    snmp_auth_passphrase:
        description:
        - InventoryRequest's snmpAuthPassphrase.
        type: str
    snmp_auth_protocol:
        description:
        - InventoryRequest's snmpAuthProtocol.
        type: str
    snmp_mode:
        description:
        - InventoryRequest's snmpMode.
        type: str
    snmp_priv_passphrase:
        description:
        - InventoryRequest's snmpPrivPassphrase.
        type: str
    snmp_priv_protocol:
        description:
        - InventoryRequest's snmpPrivProtocol.
        type: str
    snmp_rocommunity:
        description:
        - InventoryRequest's snmpROCommunity.
        type: str
    snmp_rocommunity_desc:
        description:
        - InventoryRequest's snmpROCommunityDesc.
        type: str
    snmp_rwcommunity:
        description:
        - InventoryRequest's snmpRWCommunity.
        type: str
    snmp_rwcommunity_desc:
        description:
        - InventoryRequest's snmpRWCommunityDesc.
        type: str
    snmp_user_name:
        description:
        - InventoryRequest's snmpUserName.
        type: str
    snmp_version:
        description:
        - InventoryRequest's snmpVersion.
        type: str
        required: True
    timeout:
        description:
        - InventoryRequest's timeout.
        type: int
    update_mgmt_ip:
        description:
        - InventoryRequest's updateMgmtIp.
        type: bool
    user_name_list:
        description:
        - InventoryRequest's userNameList (list of strings).
        type: list
    attribute_info:
        description:
        - DiscoveryNIO's attributeInfo.
        type: dict
    cdp_level:
        description:
        - DiscoveryNIO's cdpLevel.
        type: int
    device_ids:
        description:
        - DiscoveryNIO's deviceIds.
        type: str
    discovery_condition:
        description:
        - DiscoveryNIO's DiscoveryCondition.
        type: str
    discovery_status:
        description:
        - DiscoveryNIO's DiscoveryStatus.
        type: str
        required: True
    discovery_type:
        description:
        - DiscoveryNIO's DiscoveryType.
        type: str
    enable_password_list:
        description:
        - DiscoveryNIO's enablePasswordList.
        type: str
    global_credential_id_list:
        description:
        - DiscoveryNIO's globalCredentialIdList (list of strings).
        type: list
    http_read_credential:
        description:
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

    http_write_credential:
        description:
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

    id:
        description:
        - DiscoveryNIO's id.
        type: str
        required: True
    ip_address_list:
        description:
        - DiscoveryNIO's ipAddressList.
        type: str
    ip_filter_list:
        description:
        - DiscoveryNIO's ipFilterList.
        type: str
    is_auto_cdp:
        description:
        - DiscoveryNIO's isAutoCdp.
        type: bool
    lldp_level:
        description:
        - DiscoveryNIO's lldpLevel.
        type: int
    name:
        description:
        - DiscoveryNIO's name.
        type: str
    netconf_port:
        description:
        - DiscoveryNIO's netconfPort.
        type: str
    num_devices:
        description:
        - DiscoveryNIO's numDevices.
        type: int
    parent_discovery_id:
        description:
        - DiscoveryNIO's parentDiscoveryId.
        type: str
    password_list:
        description:
        - DiscoveryNIO's passwordList.
        type: str
    preferred_mgmt_ipmethod:
        description:
        - DiscoveryNIO's preferredMgmtIPMethod.
        type: str
    protocol_order:
        description:
        - DiscoveryNIO's protocolOrder.
        type: str
    retry_count:
        description:
        - DiscoveryNIO's retryCount.
        type: int
    snmp_auth_passphrase:
        description:
        - DiscoveryNIO's snmpAuthPassphrase.
        type: str
    snmp_auth_protocol:
        description:
        - DiscoveryNIO's snmpAuthProtocol.
        type: str
    snmp_mode:
        description:
        - DiscoveryNIO's snmpMode.
        type: str
    snmp_priv_passphrase:
        description:
        - DiscoveryNIO's snmpPrivPassphrase.
        type: str
    snmp_priv_protocol:
        description:
        - DiscoveryNIO's snmpPrivProtocol.
        type: str
    snmp_ro_community:
        description:
        - DiscoveryNIO's snmpRoCommunity.
        type: str
    snmp_ro_community_desc:
        description:
        - DiscoveryNIO's snmpRoCommunityDesc.
        type: str
    snmp_rw_community:
        description:
        - DiscoveryNIO's snmpRwCommunity.
        type: str
    snmp_rw_community_desc:
        description:
        - DiscoveryNIO's snmpRwCommunityDesc.
        type: str
    snmp_user_name:
        description:
        - DiscoveryNIO's snmpUserName.
        type: str
    time_out:
        description:
        - DiscoveryNIO's timeOut.
        type: int
    update_mgmt_ip:
        description:
        - DiscoveryNIO's updateMgmtIp.
        type: bool
    user_name_list:
        description:
        - DiscoveryNIO's userNameList.
        type: str
    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True
    id:
        description:
        - Discovery ID.
        type: str
        required: True
    id:
        description:
        - Discovery ID.
        type: str
        required: True
    records_to_delete:
        description:
        - Number of records to delete.
        type: int
        required: True
    start_index:
        description:
        - Start index.
        type: int
        required: True
    records_to_return:
        description:
        - Number of records to return.
        type: int
        required: True
    start_index:
        description:
        - Start index.
        type: int
        required: True

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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Stops all the discoveries and removes them.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Discovery's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Discovery's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Initiates Discovery with the given parameters.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: InventoryRequest's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Discovery's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Discovery's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: InventoryRequest's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Stops or starts an existing Discovery.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: DiscoveryNIO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Discovery's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Discovery's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: DiscoveryNIO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Returns the count of all available Discovery jobs.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_4:
    description: Stops the Discovery for the given Discovery ID and removes it. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Discovery's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Discovery's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_5:
    description: Returns Discovery by Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                attributeInfo:
                    description: It is the Discovery's attributeInfo.
                    returned: success,changed,always
                    type: dict
                cdpLevel:
                    description: It is the Discovery's cdpLevel.
                    returned: success,changed,always
                    type: int
                    sample: 0
                deviceIds:
                    description: It is the Discovery's deviceIds.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryCondition:
                    description: It is the Discovery's DiscoveryCondition.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryStatus:
                    description: It is the Discovery's DiscoveryStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryType:
                    description: It is the Discovery's DiscoveryType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enablePasswordList:
                    description: It is the Discovery's enablePasswordList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                globalCredentialIdList:
                    description: It is the Discovery's globalCredentialIdList.
                    returned: success,changed,always
                    type: list
                httpReadCredential:
                    description: It is the Discovery's httpReadCredential.
                    returned: success,changed,always
                    type: dict
                    contains:
                        comments:
                            description: It is the Discovery's comments.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        credentialType:
                            description: It is the Discovery's credentialType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the Discovery's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the Discovery's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceTenantId:
                            description: It is the Discovery's instanceTenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceUuid:
                            description: It is the Discovery's instanceUuid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        password:
                            description: It is the Discovery's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        port:
                            description: It is the Discovery's port.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        secure:
                            description: It is the Discovery's secure.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        username:
                            description: It is the Discovery's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                httpWriteCredential:
                    description: It is the Discovery's httpWriteCredential.
                    returned: success,changed,always
                    type: dict
                    contains:
                        comments:
                            description: It is the Discovery's comments.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        credentialType:
                            description: It is the Discovery's credentialType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the Discovery's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the Discovery's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceTenantId:
                            description: It is the Discovery's instanceTenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceUuid:
                            description: It is the Discovery's instanceUuid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        password:
                            description: It is the Discovery's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        port:
                            description: It is the Discovery's port.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        secure:
                            description: It is the Discovery's secure.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        username:
                            description: It is the Discovery's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                id:
                    description: It is the Discovery's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipAddressList:
                    description: It is the Discovery's ipAddressList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipFilterList:
                    description: It is the Discovery's ipFilterList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isAutoCdp:
                    description: It is the Discovery's isAutoCdp.
                    returned: success,changed,always
                    type: bool
                    sample: false
                lldpLevel:
                    description: It is the Discovery's lldpLevel.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the Discovery's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                netconfPort:
                    description: It is the Discovery's netconfPort.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                numDevices:
                    description: It is the Discovery's numDevices.
                    returned: success,changed,always
                    type: int
                    sample: 0
                parentDiscoveryId:
                    description: It is the Discovery's parentDiscoveryId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                passwordList:
                    description: It is the Discovery's passwordList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                preferredMgmtIPMethod:
                    description: It is the Discovery's preferredMgmtIPMethod.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                protocolOrder:
                    description: It is the Discovery's protocolOrder.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                retryCount:
                    description: It is the Discovery's retryCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                snmpAuthPassphrase:
                    description: It is the Discovery's snmpAuthPassphrase.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpAuthProtocol:
                    description: It is the Discovery's snmpAuthProtocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpMode:
                    description: It is the Discovery's snmpMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpPrivPassphrase:
                    description: It is the Discovery's snmpPrivPassphrase.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpPrivProtocol:
                    description: It is the Discovery's snmpPrivProtocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRoCommunity:
                    description: It is the Discovery's snmpRoCommunity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRoCommunityDesc:
                    description: It is the Discovery's snmpRoCommunityDesc.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRwCommunity:
                    description: It is the Discovery's snmpRwCommunity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRwCommunityDesc:
                    description: It is the Discovery's snmpRwCommunityDesc.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpUserName:
                    description: It is the Discovery's snmpUserName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                timeOut:
                    description: It is the Discovery's timeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0
                updateMgmtIp:
                    description: It is the Discovery's updateMgmtIp.
                    returned: success,changed,always
                    type: bool
                    sample: false
                userNameList:
                    description: It is the Discovery's userNameList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_6:
    description: Stops Discovery for the given range and removes them.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the Discovery's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the Discovery's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_7:
    description: Returns the Discovery by specified range.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                attributeInfo:
                    description: It is the Discovery's attributeInfo.
                    returned: success,changed,always
                    type: dict
                cdpLevel:
                    description: It is the Discovery's cdpLevel.
                    returned: success,changed,always
                    type: int
                    sample: 0
                deviceIds:
                    description: It is the Discovery's deviceIds.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryCondition:
                    description: It is the Discovery's DiscoveryCondition.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryStatus:
                    description: It is the Discovery's DiscoveryStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryType:
                    description: It is the Discovery's DiscoveryType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                enablePasswordList:
                    description: It is the Discovery's enablePasswordList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                globalCredentialIdList:
                    description: It is the Discovery's globalCredentialIdList.
                    returned: success,changed,always
                    type: list
                httpReadCredential:
                    description: It is the Discovery's httpReadCredential.
                    returned: success,changed,always
                    type: dict
                    contains:
                        comments:
                            description: It is the Discovery's comments.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        credentialType:
                            description: It is the Discovery's credentialType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the Discovery's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the Discovery's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceTenantId:
                            description: It is the Discovery's instanceTenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceUuid:
                            description: It is the Discovery's instanceUuid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        password:
                            description: It is the Discovery's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        port:
                            description: It is the Discovery's port.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        secure:
                            description: It is the Discovery's secure.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        username:
                            description: It is the Discovery's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                httpWriteCredential:
                    description: It is the Discovery's httpWriteCredential.
                    returned: success,changed,always
                    type: dict
                    contains:
                        comments:
                            description: It is the Discovery's comments.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        credentialType:
                            description: It is the Discovery's credentialType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the Discovery's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the Discovery's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceTenantId:
                            description: It is the Discovery's instanceTenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceUuid:
                            description: It is the Discovery's instanceUuid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        password:
                            description: It is the Discovery's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        port:
                            description: It is the Discovery's port.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        secure:
                            description: It is the Discovery's secure.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        username:
                            description: It is the Discovery's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                id:
                    description: It is the Discovery's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipAddressList:
                    description: It is the Discovery's ipAddressList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipFilterList:
                    description: It is the Discovery's ipFilterList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isAutoCdp:
                    description: It is the Discovery's isAutoCdp.
                    returned: success,changed,always
                    type: bool
                    sample: false
                lldpLevel:
                    description: It is the Discovery's lldpLevel.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the Discovery's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                netconfPort:
                    description: It is the Discovery's netconfPort.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                numDevices:
                    description: It is the Discovery's numDevices.
                    returned: success,changed,always
                    type: int
                    sample: 0
                parentDiscoveryId:
                    description: It is the Discovery's parentDiscoveryId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                passwordList:
                    description: It is the Discovery's passwordList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                preferredMgmtIPMethod:
                    description: It is the Discovery's preferredMgmtIPMethod.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                protocolOrder:
                    description: It is the Discovery's protocolOrder.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                retryCount:
                    description: It is the Discovery's retryCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                snmpAuthPassphrase:
                    description: It is the Discovery's snmpAuthPassphrase.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpAuthProtocol:
                    description: It is the Discovery's snmpAuthProtocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpMode:
                    description: It is the Discovery's snmpMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpPrivPassphrase:
                    description: It is the Discovery's snmpPrivPassphrase.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpPrivProtocol:
                    description: It is the Discovery's snmpPrivProtocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRoCommunity:
                    description: It is the Discovery's snmpRoCommunity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRoCommunityDesc:
                    description: It is the Discovery's snmpRoCommunityDesc.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRwCommunity:
                    description: It is the Discovery's snmpRwCommunity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpRwCommunityDesc:
                    description: It is the Discovery's snmpRwCommunityDesc.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpUserName:
                    description: It is the Discovery's snmpUserName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                timeOut:
                    description: It is the Discovery's timeOut.
                    returned: success,changed,always
                    type: int
                    sample: 0
                updateMgmtIp:
                    description: It is the Discovery's updateMgmtIp.
                    returned: success,changed,always
                    type: bool
                    sample: false
                userNameList:
                    description: It is the Discovery's userNameList.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.discovery import module_definition


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
        dnac.exec("post")

    elif state == "update":
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
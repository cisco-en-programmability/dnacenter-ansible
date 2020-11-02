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
module: discovery_network_device
short_description: Manage DiscoveryNetworkDevice objects of Discovery
description:
- Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the network devices discovered for the given discovery and for the given range. The maximum number of records that can be retrieved is 500. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the count of network devices discovered in the given discovery. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the network devices from a discovery job based on given filters. Discovery ID can be obtained using the "Get Discoveries by range" API.
version_added: '1.0'
author: first last (@GitHubID)
options:
    id:
        description:
        - Discovery ID.
        type: str
        required: True
    task_id:
        description:
        - TaskId query parameter.
        type: str
    id:
        description:
        - Discovery ID.
        type: str
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
    task_id:
        description:
        - TaskId query parameter.
        type: str
    id:
        description:
        - Discovery ID.
        type: str
        required: True
    task_id:
        description:
        - TaskId query parameter.
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
    cli_status:
        description:
        - CliStatus query parameter.
        type: str
    http_status:
        description:
        - HttpStatus query parameter.
        type: str
    ip_address:
        description:
        - IpAddress query parameter.
        type: str
    netconf_status:
        description:
        - NetconfStatus query parameter.
        type: str
    ping_status:
        description:
        - PingStatus query parameter.
        type: str
    snmp_status:
        description:
        - SnmpStatus query parameter.
        type: str
    sort_by:
        description:
        - SortBy query parameter.
        type: str
    sort_order:
        description:
        - SortOrder query parameter.
        type: str
    task_id:
        description:
        - TaskId query parameter.
        type: str
    summary:
        description:
        - If true gets the summary.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.discovery_network_device
# Reference by Internet resource
- name: DiscoveryNetworkDevice reference
  description: Complete reference of the DiscoveryNetworkDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DiscoveryNetworkDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                anchorWlcForAp:
                    description: It is the discovery network device's anchorWlcForAp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authModelId:
                    description: It is the discovery network device's authModelId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                avgUpdateFrequency:
                    description: It is the discovery network device's avgUpdateFrequency.
                    returned: success,changed,always
                    type: int
                    sample: 0
                bootDateTime:
                    description: It is the discovery network device's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cliStatus:
                    description: It is the discovery network device's cliStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplicateDeviceId:
                    description: It is the discovery network device's duplicateDeviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                errorCode:
                    description: It is the discovery network device's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                errorDescription:
                    description: It is the discovery network device's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                family:
                    description: It is the discovery network device's family.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostname:
                    description: It is the discovery network device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpStatus:
                    description: It is the discovery network device's httpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the discovery network device's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageName:
                    description: It is the discovery network device's imageName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ingressQueueConfig:
                    description: It is the discovery network device's ingressQueueConfig.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceCount:
                    description: It is the discovery network device's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryCollectionStatus:
                    description: It is the discovery network device's inventoryCollectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryReachabilityStatus:
                    description: It is the discovery network device's inventoryReachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the discovery network device's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lineCardCount:
                    description: It is the discovery network device's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lineCardId:
                    description: It is the discovery network device's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the discovery network device's location.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                locationName:
                    description: It is the discovery network device's locationName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the discovery network device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                managementIpAddress:
                    description: It is the discovery network device's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                memorySize:
                    description: It is the discovery network device's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                netconfStatus:
                    description: It is the discovery network device's netconfStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                numUpdates:
                    description: It is the discovery network device's numUpdates.
                    returned: success,changed,always
                    type: int
                    sample: 0
                pingStatus:
                    description: It is the discovery network device's pingStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                platformId:
                    description: It is the discovery network device's platformId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portRange:
                    description: It is the discovery network device's portRange.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                qosStatus:
                    description: It is the discovery network device's qosStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                reachabilityFailureReason:
                    description: It is the discovery network device's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                reachabilityStatus:
                    description: It is the discovery network device's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                role:
                    description: It is the discovery network device's role.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                roleSource:
                    description: It is the discovery network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the discovery network device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpContact:
                    description: It is the discovery network device's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpLocation:
                    description: It is the discovery network device's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpStatus:
                    description: It is the discovery network device's snmpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                softwareVersion:
                    description: It is the discovery network device's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                tag:
                    description: It is the discovery network device's tag.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                tagCount:
                    description: It is the discovery network device's tagCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                type:
                    description: It is the discovery network device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                upTime:
                    description: It is the discovery network device's upTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vendor:
                    description: It is the discovery network device's vendor.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wlcApDeviceStatus:
                    description: It is the discovery network device's wlcApDeviceStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Returns the network devices discovered for the given discovery and for the given range. The maximum number of records that can be retrieved is 500. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                anchorWlcForAp:
                    description: It is the discovery network device's anchorWlcForAp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authModelId:
                    description: It is the discovery network device's authModelId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                avgUpdateFrequency:
                    description: It is the discovery network device's avgUpdateFrequency.
                    returned: success,changed,always
                    type: int
                    sample: 0
                bootDateTime:
                    description: It is the discovery network device's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cliStatus:
                    description: It is the discovery network device's cliStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplicateDeviceId:
                    description: It is the discovery network device's duplicateDeviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                errorCode:
                    description: It is the discovery network device's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                errorDescription:
                    description: It is the discovery network device's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                family:
                    description: It is the discovery network device's family.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostname:
                    description: It is the discovery network device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpStatus:
                    description: It is the discovery network device's httpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the discovery network device's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageName:
                    description: It is the discovery network device's imageName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ingressQueueConfig:
                    description: It is the discovery network device's ingressQueueConfig.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceCount:
                    description: It is the discovery network device's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryCollectionStatus:
                    description: It is the discovery network device's inventoryCollectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryReachabilityStatus:
                    description: It is the discovery network device's inventoryReachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the discovery network device's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lineCardCount:
                    description: It is the discovery network device's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lineCardId:
                    description: It is the discovery network device's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the discovery network device's location.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                locationName:
                    description: It is the discovery network device's locationName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the discovery network device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                managementIpAddress:
                    description: It is the discovery network device's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                memorySize:
                    description: It is the discovery network device's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                netconfStatus:
                    description: It is the discovery network device's netconfStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                numUpdates:
                    description: It is the discovery network device's numUpdates.
                    returned: success,changed,always
                    type: int
                    sample: 0
                pingStatus:
                    description: It is the discovery network device's pingStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                platformId:
                    description: It is the discovery network device's platformId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portRange:
                    description: It is the discovery network device's portRange.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                qosStatus:
                    description: It is the discovery network device's qosStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                reachabilityFailureReason:
                    description: It is the discovery network device's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                reachabilityStatus:
                    description: It is the discovery network device's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                role:
                    description: It is the discovery network device's role.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                roleSource:
                    description: It is the discovery network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the discovery network device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpContact:
                    description: It is the discovery network device's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpLocation:
                    description: It is the discovery network device's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpStatus:
                    description: It is the discovery network device's snmpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                softwareVersion:
                    description: It is the discovery network device's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                tag:
                    description: It is the discovery network device's tag.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                tagCount:
                    description: It is the discovery network device's tagCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                type:
                    description: It is the discovery network device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                upTime:
                    description: It is the discovery network device's upTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vendor:
                    description: It is the discovery network device's vendor.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wlcApDeviceStatus:
                    description: It is the discovery network device's wlcApDeviceStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Returns the count of network devices discovered in the given discovery. Discovery ID can be obtained using the "Get Discoveries by range" API.
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

data_3:
    description: Returns the network devices from a discovery job based on given filters. Discovery ID can be obtained using the "Get Discoveries by range" API.
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

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.discovery_network_device import module_definition


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

    dnac.exit_json()


if __name__ == "__main__":
    main()
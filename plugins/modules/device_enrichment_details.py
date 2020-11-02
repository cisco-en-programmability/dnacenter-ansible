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
module: device_enrichment_details
short_description: Manage DeviceEnrichmentDetails objects of Devices
description:
- Enriches a given network device context (device id or device Mac Address or device management IP address) with details about the device and neighbor topology.
version_added: '1.0'
author: first last (@GitHubID)
options:
    headers:
        description:
        - Adds the header parameters.
        type: dict
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_enrichment_details
# Reference by Internet resource
- name: DeviceEnrichmentDetails reference
  description: Complete reference of the DeviceEnrichmentDetails object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceEnrichmentDetails reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Enriches a given network device context (device id or device Mac Address or device management IP address) with details about the device and neighbor topology.
    returned: success,changed,always
    type: list
    contains:
        deviceDetails:
            description: It is the device enrichment details's deviceDetails.
            returned: success,changed,always
            type: dict
            contains:
                family:
                    description: It is the device enrichment details's family.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the device enrichment details's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the device enrichment details's location.
                    returned: success,changed,always
                    type: dict
                errorCode:
                    description: It is the device enrichment details's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the device enrichment details's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                role:
                    description: It is the device enrichment details's role.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                apManagerInterfaceIp:
                    description: It is the device enrichment details's apManagerInterfaceIp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                associatedWlcIp:
                    description: It is the device enrichment details's associatedWlcIp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                bootDateTime:
                    description: It is the device enrichment details's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                collectionStatus:
                    description: It is the device enrichment details's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceCount:
                    description: It is the device enrichment details's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lineCardCount:
                    description: It is the device enrichment details's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lineCardId:
                    description: It is the device enrichment details's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                managementIpAddress:
                    description: It is the device enrichment details's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                memorySize:
                    description: It is the device enrichment details's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                platformId:
                    description: It is the device enrichment details's platformId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                reachabilityFailureReason:
                    description: It is the device enrichment details's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                reachabilityStatus:
                    description: It is the device enrichment details's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpContact:
                    description: It is the device enrichment details's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpLocation:
                    description: It is the device enrichment details's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                tunnelUdpPort:
                    description: It is the device enrichment details's tunnelUdpPort.
                    returned: success,changed,always
                    type: dict
                waasDeviceMode:
                    description: It is the device enrichment details's waasDeviceMode.
                    returned: success,changed,always
                    type: dict
                series:
                    description: It is the device enrichment details's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryStatusDetail:
                    description: It is the device enrichment details's inventoryStatusDetail.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                collectionInterval:
                    description: It is the device enrichment details's collectionInterval.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the device enrichment details's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                softwareVersion:
                    description: It is the device enrichment details's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                roleSource:
                    description: It is the device enrichment details's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostname:
                    description: It is the device enrichment details's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                upTime:
                    description: It is the device enrichment details's upTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdateTime:
                    description: It is the device enrichment details's lastUpdateTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                errorDescription:
                    description: It is the device enrichment details's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                locationName:
                    description: It is the device enrichment details's locationName.
                    returned: success,changed,always
                    type: dict
                tagCount:
                    description: It is the device enrichment details's tagCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the device enrichment details's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the device enrichment details's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the device enrichment details's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                neighborTopology:
                    description: It is the device enrichment details's neighborTopology.
                    returned: success,changed,always
                    type: list
                    contains:
                        nodes:
                            description: It is the device enrichment details's nodes.
                            returned: success,changed,always
                            type: list
                            contains:
                                role:
                                    description: It is the device enrichment details's role.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                name:
                                    description: It is the device enrichment details's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                id:
                                    description: It is the device enrichment details's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                description:
                                    description: It is the device enrichment details's description.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                deviceType:
                                    description: It is the device enrichment details's deviceType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                platformId:
                                    description: It is the device enrichment details's platformId.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                family:
                                    description: It is the device enrichment details's family.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ip:
                                    description: It is the device enrichment details's ip.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                softwareVersion:
                                    description: It is the device enrichment details's softwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                userId:
                                    description: It is the device enrichment details's userId.
                                    returned: success,changed,always
                                    type: dict
                                nodeType:
                                    description: It is the device enrichment details's nodeType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                radioFrequency:
                                    description: It is the device enrichment details's radioFrequency.
                                    returned: success,changed,always
                                    type: dict
                                clients:
                                    description: It is the device enrichment details's clients.
                                    returned: success,changed,always
                                    type: dict
                                count:
                                    description: It is the device enrichment details's count.
                                    returned: success,changed,always
                                    type: dict
                                healthScore:
                                    description: It is the device enrichment details's healthScore.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                level:
                                    description: It is the device enrichment details's level.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                fabricGroup:
                                    description: It is the device enrichment details's fabricGroup.
                                    returned: success,changed,always
                                    type: dict
                                connectedDevice:
                                    description: It is the device enrichment details's connectedDevice.
                                    returned: success,changed,always
                                    type: dict

                        links:
                            description: It is the device enrichment details's links.
                            returned: success,changed,always
                            type: list
                            contains:
                                source:
                                    description: It is the device enrichment details's source.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                linkStatus:
                                    description: It is the device enrichment details's linkStatus.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                label:
                                    description: It is the device enrichment details's label.
                                    returned: success,changed,always
                                    type: list
                                target:
                                    description: It is the device enrichment details's target.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                id:
                                    description: It is the device enrichment details's id.
                                    returned: success,changed,always
                                    type: dict
                                portUtilization:
                                    description: It is the device enrichment details's portUtilization.
                                    returned: success,changed,always
                                    type: dict





'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.device_enrichment_details import module_definition


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
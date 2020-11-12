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
"""

EXAMPLES = r"""
"""

RETURN = r"""
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
                    sample: '<family>'
                type:
                    description: It is the device enrichment details's type.
                    returned: success,changed,always
                    type: str
                    sample: '<type>'
                location:
                    description: It is the device enrichment details's location.
                    returned: success,changed,always
                    type: dict
                errorCode:
                    description: It is the device enrichment details's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                macAddress:
                    description: It is the device enrichment details's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<macaddress>'
                role:
                    description: It is the device enrichment details's role.
                    returned: success,changed,always
                    type: str
                    sample: '<role>'
                apManagerInterfaceIp:
                    description: It is the device enrichment details's apManagerInterfaceIp.
                    returned: success,changed,always
                    type: str
                    sample: '<apmanagerinterfaceip>'
                associatedWlcIp:
                    description: It is the device enrichment details's associatedWlcIp.
                    returned: success,changed,always
                    type: str
                    sample: '<associatedwlcip>'
                bootDateTime:
                    description: It is the device enrichment details's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<bootdatetime>'
                collectionStatus:
                    description: It is the device enrichment details's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<collectionstatus>'
                interfaceCount:
                    description: It is the device enrichment details's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: '<interfacecount>'
                lineCardCount:
                    description: It is the device enrichment details's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardcount>'
                lineCardId:
                    description: It is the device enrichment details's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardid>'
                managementIpAddress:
                    description: It is the device enrichment details's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<managementipaddress>'
                memorySize:
                    description: It is the device enrichment details's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: '<memorysize>'
                platformId:
                    description: It is the device enrichment details's platformId.
                    returned: success,changed,always
                    type: str
                    sample: '<platformid>'
                reachabilityFailureReason:
                    description: It is the device enrichment details's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilityfailurereason>'
                reachabilityStatus:
                    description: It is the device enrichment details's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilitystatus>'
                snmpContact:
                    description: It is the device enrichment details's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: '<snmpcontact>'
                snmpLocation:
                    description: It is the device enrichment details's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: '<snmplocation>'
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
                    sample: '<series>'
                inventoryStatusDetail:
                    description: It is the device enrichment details's inventoryStatusDetail.
                    returned: success,changed,always
                    type: str
                    sample: '<inventorystatusdetail>'
                collectionInterval:
                    description: It is the device enrichment details's collectionInterval.
                    returned: success,changed,always
                    type: str
                    sample: '<collectioninterval>'
                serialNumber:
                    description: It is the device enrichment details's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<serialnumber>'
                softwareVersion:
                    description: It is the device enrichment details's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: '<softwareversion>'
                roleSource:
                    description: It is the device enrichment details's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: '<rolesource>'
                hostname:
                    description: It is the device enrichment details's hostname.
                    returned: success,changed,always
                    type: str
                    sample: '<hostname>'
                upTime:
                    description: It is the device enrichment details's upTime.
                    returned: success,changed,always
                    type: str
                    sample: '<uptime>'
                lastUpdateTime:
                    description: It is the device enrichment details's lastUpdateTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                errorDescription:
                    description: It is the device enrichment details's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: '<errordescription>'
                locationName:
                    description: It is the device enrichment details's locationName.
                    returned: success,changed,always
                    type: dict
                tagCount:
                    description: It is the device enrichment details's tagCount.
                    returned: success,changed,always
                    type: str
                    sample: '<tagcount>'
                lastUpdated:
                    description: It is the device enrichment details's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdated>'
                instanceUuid:
                    description: It is the device enrichment details's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                id:
                    description: It is the device enrichment details's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
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
                                    sample: '<role>'
                                name:
                                    description: It is the device enrichment details's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<name>'
                                id:
                                    description: It is the device enrichment details's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: '478012'
                                description:
                                    description: It is the device enrichment details's description.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<description>'
                                deviceType:
                                    description: It is the device enrichment details's deviceType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<devicetype>'
                                platformId:
                                    description: It is the device enrichment details's platformId.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<platformid>'
                                family:
                                    description: It is the device enrichment details's family.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<family>'
                                ip:
                                    description: It is the device enrichment details's ip.
                                    returned: success,changed,always
                                    type: str
                                    sample: '1.1.1.17'
                                softwareVersion:
                                    description: It is the device enrichment details's softwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<softwareversion>'
                                userId:
                                    description: It is the device enrichment details's userId.
                                    returned: success,changed,always
                                    type: dict
                                nodeType:
                                    description: It is the device enrichment details's nodeType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<nodetype>'
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
                                    sample: '<source>'
                                linkStatus:
                                    description: It is the device enrichment details's linkStatus.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<linkstatus>'
                                label:
                                    description: It is the device enrichment details's label.
                                    returned: success,changed,always
                                    type: list
                                target:
                                    description: It is the device enrichment details's target.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<target>'
                                id:
                                    description: It is the device enrichment details's id.
                                    returned: success,changed,always
                                    type: dict
                                portUtilization:
                                    description: It is the device enrichment details's portUtilization.
                                    returned: success,changed,always
                                    type: dict





"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.device_enrichment_details import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()

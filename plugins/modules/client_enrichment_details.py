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
module: client_enrichment_details
short_description: Manage ClientEnrichmentDetails objects of Clients
description:
- Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details about the user, the devices that the user is connected to and the assurance issues that the user is impacted by.
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
- module: cisco.dnac.plugins.module_utils.definitions.client_enrichment_details
# Reference by Internet resource
- name: ClientEnrichmentDetails reference
  description: Complete reference of the ClientEnrichmentDetails object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ClientEnrichmentDetails reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details about the user, the devices that the user is connected to and the assurance issues that the user is impacted by.
    returned: success,changed,always
    type: list
    contains:
        userDetails:
            description: It is the client enrichment details's userDetails.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the client enrichment details's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                connectionStatus:
                    description: It is the client enrichment details's connectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostType:
                    description: It is the client enrichment details's hostType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                userId:
                    description: It is the client enrichment details's userId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostName:
                    description: It is the client enrichment details's hostName.
                    returned: success,changed,always
                    type: dict
                hostOs:
                    description: It is the client enrichment details's hostOs.
                    returned: success,changed,always
                    type: dict
                hostVersion:
                    description: It is the client enrichment details's hostVersion.
                    returned: success,changed,always
                    type: dict
                subType:
                    description: It is the client enrichment details's subType.
                    returned: success,changed,always
                    type: dict
                lastUpdated:
                    description: It is the client enrichment details's lastUpdated.
                    returned: success,changed,always
                    type: int
                    sample: 0
                healthScore:
                    description: It is the client enrichment details's healthScore.
                    returned: success,changed,always
                    type: list
                    contains:
                        healthType:
                            description: It is the client enrichment details's healthType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        reason:
                            description: It is the client enrichment details's reason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        score:
                            description: It is the client enrichment details's score.
                            returned: success,changed,always
                            type: int
                            sample: 0

                hostMac:
                    description: It is the client enrichment details's hostMac.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostIpV4:
                    description: It is the client enrichment details's hostIpV4.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostIpV6:
                    description: It is the client enrichment details's hostIpV6.
                    returned: success,changed,always
                    type: list
                authType:
                    description: It is the client enrichment details's authType.
                    returned: success,changed,always
                    type: dict
                vlanId:
                    description: It is the client enrichment details's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ssid:
                    description: It is the client enrichment details's ssid.
                    returned: success,changed,always
                    type: dict
                location:
                    description: It is the client enrichment details's location.
                    returned: success,changed,always
                    type: dict
                clientConnection:
                    description: It is the client enrichment details's clientConnection.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                connectedDevice:
                    description: It is the client enrichment details's connectedDevice.
                    returned: success,changed,always
                    type: list
                issueCount:
                    description: It is the client enrichment details's issueCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                rssi:
                    description: It is the client enrichment details's rssi.
                    returned: success,changed,always
                    type: dict
                snr:
                    description: It is the client enrichment details's snr.
                    returned: success,changed,always
                    type: dict
                dataRate:
                    description: It is the client enrichment details's dataRate.
                    returned: success,changed,always
                    type: dict
                port:
                    description: It is the client enrichment details's port.
                    returned: success,changed,always
                    type: dict

        connectedDevice:
            description: It is the client enrichment details's connectedDevice.
            returned: success,changed,always
            type: list
            contains:
                deviceDetails:
                    description: It is the client enrichment details's deviceDetails.
                    returned: success,changed,always
                    type: dict
                    contains:
                        family:
                            description: It is the client enrichment details's family.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the client enrichment details's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        location:
                            description: It is the client enrichment details's location.
                            returned: success,changed,always
                            type: dict
                        errorCode:
                            description: It is the client enrichment details's errorCode.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        macAddress:
                            description: It is the client enrichment details's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        role:
                            description: It is the client enrichment details's role.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        apManagerInterfaceIp:
                            description: It is the client enrichment details's apManagerInterfaceIp.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        associatedWlcIp:
                            description: It is the client enrichment details's associatedWlcIp.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        bootDateTime:
                            description: It is the client enrichment details's bootDateTime.
                            returned: success,changed,always
                            type: dict
                        collectionStatus:
                            description: It is the client enrichment details's collectionStatus.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        interfaceCount:
                            description: It is the client enrichment details's interfaceCount.
                            returned: success,changed,always
                            type: dict
                        lineCardCount:
                            description: It is the client enrichment details's lineCardCount.
                            returned: success,changed,always
                            type: dict
                        lineCardId:
                            description: It is the client enrichment details's lineCardId.
                            returned: success,changed,always
                            type: dict
                        managementIpAddress:
                            description: It is the client enrichment details's managementIpAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        memorySize:
                            description: It is the client enrichment details's memorySize.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        platformId:
                            description: It is the client enrichment details's platformId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        reachabilityFailureReason:
                            description: It is the client enrichment details's reachabilityFailureReason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        reachabilityStatus:
                            description: It is the client enrichment details's reachabilityStatus.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        snmpContact:
                            description: It is the client enrichment details's snmpContact.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        snmpLocation:
                            description: It is the client enrichment details's snmpLocation.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        tunnelUdpPort:
                            description: It is the client enrichment details's tunnelUdpPort.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        waasDeviceMode:
                            description: It is the client enrichment details's waasDeviceMode.
                            returned: success,changed,always
                            type: dict
                        series:
                            description: It is the client enrichment details's series.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        inventoryStatusDetail:
                            description: It is the client enrichment details's inventoryStatusDetail.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        collectionInterval:
                            description: It is the client enrichment details's collectionInterval.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        serialNumber:
                            description: It is the client enrichment details's serialNumber.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        softwareVersion:
                            description: It is the client enrichment details's softwareVersion.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        roleSource:
                            description: It is the client enrichment details's roleSource.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        hostname:
                            description: It is the client enrichment details's hostname.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        upTime:
                            description: It is the client enrichment details's upTime.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        lastUpdateTime:
                            description: It is the client enrichment details's lastUpdateTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        errorDescription:
                            description: It is the client enrichment details's errorDescription.
                            returned: success,changed,always
                            type: dict
                        locationName:
                            description: It is the client enrichment details's locationName.
                            returned: success,changed,always
                            type: dict
                        tagCount:
                            description: It is the client enrichment details's tagCount.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        lastUpdated:
                            description: It is the client enrichment details's lastUpdated.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        instanceUuid:
                            description: It is the client enrichment details's instanceUuid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the client enrichment details's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        neighborTopology:
                            description: It is the client enrichment details's neighborTopology.
                            returned: success,changed,always
                            type: list
                            contains:
                                nodes:
                                    description: It is the client enrichment details's nodes.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        role:
                                            description: It is the client enrichment details's role.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        name:
                                            description: It is the client enrichment details's name.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        id:
                                            description: It is the client enrichment details's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        description:
                                            description: It is the client enrichment details's description.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        deviceType:
                                            description: It is the client enrichment details's deviceType.
                                            returned: success,changed,always
                                            type: dict
                                        platformId:
                                            description: It is the client enrichment details's platformId.
                                            returned: success,changed,always
                                            type: dict
                                        family:
                                            description: It is the client enrichment details's family.
                                            returned: success,changed,always
                                            type: dict
                                        ip:
                                            description: It is the client enrichment details's ip.
                                            returned: success,changed,always
                                            type: dict
                                        softwareVersion:
                                            description: It is the client enrichment details's softwareVersion.
                                            returned: success,changed,always
                                            type: dict
                                        userId:
                                            description: It is the client enrichment details's userId.
                                            returned: success,changed,always
                                            type: dict
                                        nodeType:
                                            description: It is the client enrichment details's nodeType.
                                            returned: success,changed,always
                                            type: dict
                                        radioFrequency:
                                            description: It is the client enrichment details's radioFrequency.
                                            returned: success,changed,always
                                            type: dict
                                        clients:
                                            description: It is the client enrichment details's clients.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        count:
                                            description: It is the client enrichment details's count.
                                            returned: success,changed,always
                                            type: dict
                                        healthScore:
                                            description: It is the client enrichment details's healthScore.
                                            returned: success,changed,always
                                            type: dict
                                        level:
                                            description: It is the client enrichment details's level.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        fabricGroup:
                                            description: It is the client enrichment details's fabricGroup.
                                            returned: success,changed,always
                                            type: dict

                                links:
                                    description: It is the client enrichment details's links.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        source:
                                            description: It is the client enrichment details's source.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        linkStatus:
                                            description: It is the client enrichment details's linkStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        label:
                                            description: It is the client enrichment details's label.
                                            returned: success,changed,always
                                            type: list
                                        target:
                                            description: It is the client enrichment details's target.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        id:
                                            description: It is the client enrichment details's id.
                                            returned: success,changed,always
                                            type: dict
                                        portUtilization:
                                            description: It is the client enrichment details's portUtilization.
                                            returned: success,changed,always
                                            type: dict


                        cisco360view:
                            description: It is the client enrichment details's cisco360view.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        issueDetails:
            description: It is the client enrichment details's issueDetails.
            returned: success,changed,always
            type: dict
            contains:
                issue:
                    description: It is the client enrichment details's issue.
                    returned: success,changed,always
                    type: list
                    contains:
                        issueId:
                            description: It is the client enrichment details's issueId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueSource:
                            description: It is the client enrichment details's issueSource.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueCategory:
                            description: It is the client enrichment details's issueCategory.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueName:
                            description: It is the client enrichment details's issueName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueDescription:
                            description: It is the client enrichment details's issueDescription.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueEntity:
                            description: It is the client enrichment details's issueEntity.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueEntityValue:
                            description: It is the client enrichment details's issueEntityValue.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueSeverity:
                            description: It is the client enrichment details's issueSeverity.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issuePriority:
                            description: It is the client enrichment details's issuePriority.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueSummary:
                            description: It is the client enrichment details's issueSummary.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueTimestamp:
                            description: It is the client enrichment details's issueTimestamp.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        suggestedActions:
                            description: It is the client enrichment details's suggestedActions.
                            returned: success,changed,always
                            type: list
                            contains:
                                message:
                                    description: It is the client enrichment details's message.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                steps:
                                    description: It is the client enrichment details's steps.
                                    returned: success,changed,always
                                    type: list

                        impactedHosts:
                            description: It is the client enrichment details's impactedHosts.
                            returned: success,changed,always
                            type: list
                            contains:
                                hostType:
                                    description: It is the client enrichment details's hostType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                hostName:
                                    description: It is the client enrichment details's hostName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                hostOs:
                                    description: It is the client enrichment details's hostOs.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ssid:
                                    description: It is the client enrichment details's ssid.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                connectedInterface:
                                    description: It is the client enrichment details's connectedInterface.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                macAddress:
                                    description: It is the client enrichment details's macAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                failedAttempts:
                                    description: It is the client enrichment details's failedAttempts.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                location:
                                    description: It is the client enrichment details's location.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        siteId:
                                            description: It is the client enrichment details's siteId.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        siteType:
                                            description: It is the client enrichment details's siteType.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        area:
                                            description: It is the client enrichment details's area.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        building:
                                            description: It is the client enrichment details's building.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        floor:
                                            description: It is the client enrichment details's floor.
                                            returned: success,changed,always
                                            type: dict
                                        apsImpacted:
                                            description: It is the client enrichment details's apsImpacted.
                                            returned: success,changed,always
                                            type: list

                                timestamp:
                                    description: It is the client enrichment details's timestamp.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0





'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.client_enrichment_details import module_definition


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
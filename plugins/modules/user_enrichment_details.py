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
module: user_enrichment_details
short_description: Manage UserEnrichmentDetails objects of Users
description:
- Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details about the user and devices that the user is connected to.
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
- module: cisco.dnac.plugins.module_utils.definitions.user_enrichment_details
# Reference by Internet resource
- name: UserEnrichmentDetails reference
  description: Complete reference of the UserEnrichmentDetails object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: UserEnrichmentDetails reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details about the user and devices that the user is connected to.
    returned: success,changed,always
    type: list
    contains:
        userDetails:
            description: It is the user enrichment details's userDetails.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the user enrichment details's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                connectionStatus:
                    description: It is the user enrichment details's connectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<connectionstatus>'
                hostType:
                    description: It is the user enrichment details's hostType.
                    returned: success,changed,always
                    type: str
                    sample: '<hosttype>'
                userId:
                    description: It is the user enrichment details's userId.
                    returned: success,changed,always
                    type: dict
                hostName:
                    description: It is the user enrichment details's hostName.
                    returned: success,changed,always
                    type: dict
                hostOs:
                    description: It is the user enrichment details's hostOs.
                    returned: success,changed,always
                    type: dict
                hostVersion:
                    description: It is the user enrichment details's hostVersion.
                    returned: success,changed,always
                    type: dict
                subType:
                    description: It is the user enrichment details's subType.
                    returned: success,changed,always
                    type: str
                    sample: '<subtype>'
                lastUpdated:
                    description: It is the user enrichment details's lastUpdated.
                    returned: success,changed,always
                    type: int
                    sample: 0
                healthScore:
                    description: It is the user enrichment details's healthScore.
                    returned: success,changed,always
                    type: list
                    contains:
                        healthType:
                            description: It is the user enrichment details's healthType.
                            returned: success,changed,always
                            type: str
                            sample: '<healthtype>'
                        reason:
                            description: It is the user enrichment details's reason.
                            returned: success,changed,always
                            type: str
                            sample: '<reason>'
                        score:
                            description: It is the user enrichment details's score.
                            returned: success,changed,always
                            type: int
                            sample: 0

                hostMac:
                    description: It is the user enrichment details's hostMac.
                    returned: success,changed,always
                    type: str
                    sample: '<hostmac>'
                hostIpV4:
                    description: It is the user enrichment details's hostIpV4.
                    returned: success,changed,always
                    type: str
                    sample: '<hostipv4>'
                hostIpV6:
                    description: It is the user enrichment details's hostIpV6.
                    returned: success,changed,always
                    type: list
                authType:
                    description: It is the user enrichment details's authType.
                    returned: success,changed,always
                    type: dict
                vlanId:
                    description: It is the user enrichment details's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: '<vlanid>'
                ssid:
                    description: It is the user enrichment details's ssid.
                    returned: success,changed,always
                    type: dict
                frequency:
                    description: It is the user enrichment details's frequency.
                    returned: success,changed,always
                    type: dict
                channel:
                    description: It is the user enrichment details's channel.
                    returned: success,changed,always
                    type: dict
                apGroup:
                    description: It is the user enrichment details's apGroup.
                    returned: success,changed,always
                    type: dict
                location:
                    description: It is the user enrichment details's location.
                    returned: success,changed,always
                    type: dict
                clientConnection:
                    description: It is the user enrichment details's clientConnection.
                    returned: success,changed,always
                    type: str
                    sample: '<clientconnection>'
                connectedDevice:
                    description: It is the user enrichment details's connectedDevice.
                    returned: success,changed,always
                    type: list
                issueCount:
                    description: It is the user enrichment details's issueCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                rssi:
                    description: It is the user enrichment details's rssi.
                    returned: success,changed,always
                    type: dict
                avgRssi:
                    description: It is the user enrichment details's avgRssi.
                    returned: success,changed,always
                    type: dict
                snr:
                    description: It is the user enrichment details's snr.
                    returned: success,changed,always
                    type: dict
                avgSnr:
                    description: It is the user enrichment details's avgSnr.
                    returned: success,changed,always
                    type: dict
                dataRate:
                    description: It is the user enrichment details's dataRate.
                    returned: success,changed,always
                    type: dict
                txBytes:
                    description: It is the user enrichment details's txBytes.
                    returned: success,changed,always
                    type: dict
                rxBytes:
                    description: It is the user enrichment details's rxBytes.
                    returned: success,changed,always
                    type: dict
                dnsSuccess:
                    description: It is the user enrichment details's dnsSuccess.
                    returned: success,changed,always
                    type: dict
                dnsFailure:
                    description: It is the user enrichment details's dnsFailure.
                    returned: success,changed,always
                    type: dict
                onboarding:
                    description: It is the user enrichment details's onboarding.
                    returned: success,changed,always
                    type: dict
                    contains:
                        averageRunDuration:
                            description: It is the user enrichment details's averageRunDuration.
                            returned: success,changed,always
                            type: dict
                        maxRunDuration:
                            description: It is the user enrichment details's maxRunDuration.
                            returned: success,changed,always
                            type: dict
                        averageAssocDuration:
                            description: It is the user enrichment details's averageAssocDuration.
                            returned: success,changed,always
                            type: dict
                        maxAssocDuration:
                            description: It is the user enrichment details's maxAssocDuration.
                            returned: success,changed,always
                            type: dict
                        averageAuthDuration:
                            description: It is the user enrichment details's averageAuthDuration.
                            returned: success,changed,always
                            type: dict
                        maxAuthDuration:
                            description: It is the user enrichment details's maxAuthDuration.
                            returned: success,changed,always
                            type: dict
                        averageDhcpDuration:
                            description: It is the user enrichment details's averageDhcpDuration.
                            returned: success,changed,always
                            type: dict
                        maxDhcpDuration:
                            description: It is the user enrichment details's maxDhcpDuration.
                            returned: success,changed,always
                            type: dict
                        aaaServerIp:
                            description: It is the user enrichment details's aaaServerIp.
                            returned: success,changed,always
                            type: dict
                        dhcpServerIp:
                            description: It is the user enrichment details's dhcpServerIp.
                            returned: success,changed,always
                            type: dict

                onboardingTime:
                    description: It is the user enrichment details's onboardingTime.
                    returned: success,changed,always
                    type: dict
                port:
                    description: It is the user enrichment details's port.
                    returned: success,changed,always
                    type: dict

        connectedDevice:
            description: It is the user enrichment details's connectedDevice.
            returned: success,changed,always
            type: list
            contains:
                deviceDetails:
                    description: It is the user enrichment details's deviceDetails.
                    returned: success,changed,always
                    type: dict
                    contains:
                        family:
                            description: It is the user enrichment details's family.
                            returned: success,changed,always
                            type: str
                            sample: '<family>'
                        type:
                            description: It is the user enrichment details's type.
                            returned: success,changed,always
                            type: str
                            sample: '<type>'
                        location:
                            description: It is the user enrichment details's location.
                            returned: success,changed,always
                            type: dict
                        errorCode:
                            description: It is the user enrichment details's errorCode.
                            returned: success,changed,always
                            type: dict
                        macAddress:
                            description: It is the user enrichment details's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: '<macaddress>'
                        role:
                            description: It is the user enrichment details's role.
                            returned: success,changed,always
                            type: str
                            sample: '<role>'
                        apManagerInterfaceIp:
                            description: It is the user enrichment details's apManagerInterfaceIp.
                            returned: success,changed,always
                            type: str
                            sample: '<apmanagerinterfaceip>'
                        associatedWlcIp:
                            description: It is the user enrichment details's associatedWlcIp.
                            returned: success,changed,always
                            type: str
                            sample: '<associatedwlcip>'
                        bootDateTime:
                            description: It is the user enrichment details's bootDateTime.
                            returned: success,changed,always
                            type: str
                            sample: '<bootdatetime>'
                        collectionStatus:
                            description: It is the user enrichment details's collectionStatus.
                            returned: success,changed,always
                            type: str
                            sample: '<collectionstatus>'
                        interfaceCount:
                            description: It is the user enrichment details's interfaceCount.
                            returned: success,changed,always
                            type: str
                            sample: '<interfacecount>'
                        lineCardCount:
                            description: It is the user enrichment details's lineCardCount.
                            returned: success,changed,always
                            type: str
                            sample: '<linecardcount>'
                        lineCardId:
                            description: It is the user enrichment details's lineCardId.
                            returned: success,changed,always
                            type: str
                            sample: '<linecardid>'
                        managementIpAddress:
                            description: It is the user enrichment details's managementIpAddress.
                            returned: success,changed,always
                            type: str
                            sample: '<managementipaddress>'
                        memorySize:
                            description: It is the user enrichment details's memorySize.
                            returned: success,changed,always
                            type: str
                            sample: '<memorysize>'
                        platformId:
                            description: It is the user enrichment details's platformId.
                            returned: success,changed,always
                            type: str
                            sample: '<platformid>'
                        reachabilityFailureReason:
                            description: It is the user enrichment details's reachabilityFailureReason.
                            returned: success,changed,always
                            type: str
                            sample: '<reachabilityfailurereason>'
                        reachabilityStatus:
                            description: It is the user enrichment details's reachabilityStatus.
                            returned: success,changed,always
                            type: str
                            sample: '<reachabilitystatus>'
                        snmpContact:
                            description: It is the user enrichment details's snmpContact.
                            returned: success,changed,always
                            type: str
                            sample: '<snmpcontact>'
                        snmpLocation:
                            description: It is the user enrichment details's snmpLocation.
                            returned: success,changed,always
                            type: str
                            sample: '<snmplocation>'
                        tunnelUdpPort:
                            description: It is the user enrichment details's tunnelUdpPort.
                            returned: success,changed,always
                            type: dict
                        waasDeviceMode:
                            description: It is the user enrichment details's waasDeviceMode.
                            returned: success,changed,always
                            type: dict
                        series:
                            description: It is the user enrichment details's series.
                            returned: success,changed,always
                            type: str
                            sample: '<series>'
                        inventoryStatusDetail:
                            description: It is the user enrichment details's inventoryStatusDetail.
                            returned: success,changed,always
                            type: str
                            sample: '<inventorystatusdetail>'
                        collectionInterval:
                            description: It is the user enrichment details's collectionInterval.
                            returned: success,changed,always
                            type: str
                            sample: '<collectioninterval>'
                        serialNumber:
                            description: It is the user enrichment details's serialNumber.
                            returned: success,changed,always
                            type: str
                            sample: '<serialnumber>'
                        softwareVersion:
                            description: It is the user enrichment details's softwareVersion.
                            returned: success,changed,always
                            type: str
                            sample: '<softwareversion>'
                        roleSource:
                            description: It is the user enrichment details's roleSource.
                            returned: success,changed,always
                            type: str
                            sample: '<rolesource>'
                        hostname:
                            description: It is the user enrichment details's hostname.
                            returned: success,changed,always
                            type: str
                            sample: '<hostname>'
                        upTime:
                            description: It is the user enrichment details's upTime.
                            returned: success,changed,always
                            type: str
                            sample: '<uptime>'
                        lastUpdateTime:
                            description: It is the user enrichment details's lastUpdateTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        errorDescription:
                            description: It is the user enrichment details's errorDescription.
                            returned: success,changed,always
                            type: dict
                        locationName:
                            description: It is the user enrichment details's locationName.
                            returned: success,changed,always
                            type: dict
                        tagCount:
                            description: It is the user enrichment details's tagCount.
                            returned: success,changed,always
                            type: str
                            sample: '<tagcount>'
                        lastUpdated:
                            description: It is the user enrichment details's lastUpdated.
                            returned: success,changed,always
                            type: str
                            sample: '<lastupdated>'
                        instanceUuid:
                            description: It is the user enrichment details's instanceUuid.
                            returned: success,changed,always
                            type: str
                            sample: '<instanceuuid>'
                        id:
                            description: It is the user enrichment details's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        neighborTopology:
                            description: It is the user enrichment details's neighborTopology.
                            returned: success,changed,always
                            type: list
                            contains:
                                errorCode:
                                    description: It is the user enrichment details's errorCode.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                message:
                                    description: It is the user enrichment details's message.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<message>'
                                detail:
                                    description: It is the user enrichment details's detail.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<detail>'





"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.user_enrichment_details import (
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

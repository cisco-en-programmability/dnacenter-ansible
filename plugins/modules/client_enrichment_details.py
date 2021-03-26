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
module: client_enrichment_details
short_description: Manage ClientEnrichmentDetails objects of Clients
description:
- Enriches a given network End User context (a network user-id or end user's device Mac Address) with details about the user, the devices that the user is connected to and the assurance issues that the user is impacted by.
version_added: '1.0'
author: Rafael Campos (@racampos)
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
"""

EXAMPLES = r"""
- name: get_client_enrichment_details
  cisco.dnac.client_enrichment_details:
    state: query  # required
    headers:  # required
  register: query_result
  """

RETURN = """
get_client_enrichment_details:
    description: Enriches a given network End User context (a network user-id or end user's device Mac Address) with details about the user, the devices that the user is connected to and the assurance issues that the user is impacted by.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the client enrichment details's payload.
      returned: always
      type: list
      contains:
        userDetails:
          description: It is the client enrichment details's userDetails.
          returned: always
          type: dict
          contains:
            id:
              description: It is the client enrichment details's id.
              returned: always
              type: str
              sample: '478012'
            connectionStatus:
              description: It is the client enrichment details's connectionStatus.
              returned: always
              type: str
              sample: '<connectionstatus>'
            hostType:
              description: It is the client enrichment details's hostType.
              returned: always
              type: str
              sample: '<hosttype>'
            userId:
              description: It is the client enrichment details's userId.
              returned: always
              type: str
              sample: '<userid>'
            hostName:
              description: It is the client enrichment details's hostName.
              returned: always
              type: dict
            hostOs:
              description: It is the client enrichment details's hostOs.
              returned: always
              type: dict
            hostVersion:
              description: It is the client enrichment details's hostVersion.
              returned: always
              type: dict
            subType:
              description: It is the client enrichment details's subType.
              returned: always
              type: dict
            lastUpdated:
              description: It is the client enrichment details's lastUpdated.
              returned: always
              type: int
              sample: 0
            healthScore:
              description: It is the client enrichment details's healthScore.
              returned: always
              type: list
              contains:
                healthType:
                  description: It is the client enrichment details's healthType.
                  returned: always
                  type: str
                  sample: '<healthtype>'
                reason:
                  description: It is the client enrichment details's reason.
                  returned: always
                  type: str
                  sample: '<reason>'
                score:
                  description: It is the client enrichment details's score.
                  returned: always
                  type: int
                  sample: 0

            hostMac:
              description: It is the client enrichment details's hostMac.
              returned: always
              type: str
              sample: '<hostmac>'
            hostIpV4:
              description: It is the client enrichment details's hostIpV4.
              returned: always
              type: str
              sample: '<hostipv4>'
            hostIpV6:
              description: It is the client enrichment details's hostIpV6.
              returned: always
              type: list
            authType:
              description: It is the client enrichment details's authType.
              returned: always
              type: dict
            vlanId:
              description: It is the client enrichment details's vlanId.
              returned: always
              type: str
              sample: '<vlanid>'
            ssid:
              description: It is the client enrichment details's ssid.
              returned: always
              type: dict
            location:
              description: It is the client enrichment details's location.
              returned: always
              type: dict
            clientConnection:
              description: It is the client enrichment details's clientConnection.
              returned: always
              type: str
              sample: '<clientconnection>'
            connectedDevice:
              description: It is the client enrichment details's connectedDevice.
              returned: always
              type: list
            issueCount:
              description: It is the client enrichment details's issueCount.
              returned: always
              type: int
              sample: 0
            rssi:
              description: It is the client enrichment details's rssi.
              returned: always
              type: dict
            snr:
              description: It is the client enrichment details's snr.
              returned: always
              type: dict
            dataRate:
              description: It is the client enrichment details's dataRate.
              returned: always
              type: dict
            port:
              description: It is the client enrichment details's port.
              returned: always
              type: dict

        connectedDevice:
          description: It is the client enrichment details's connectedDevice.
          returned: always
          type: list
          contains:
            deviceDetails:
              description: It is the client enrichment details's deviceDetails.
              returned: always
              type: dict
              contains:
                family:
                  description: It is the client enrichment details's family.
                  returned: always
                  type: str
                  sample: '<family>'
                type:
                  description: It is the client enrichment details's type.
                  returned: always
                  type: str
                  sample: '<type>'
                location:
                  description: It is the client enrichment details's location.
                  returned: always
                  type: dict
                errorCode:
                  description: It is the client enrichment details's errorCode.
                  returned: always
                  type: str
                  sample: '<errorcode>'
                macAddress:
                  description: It is the client enrichment details's macAddress.
                  returned: always
                  type: str
                  sample: '<macaddress>'
                role:
                  description: It is the client enrichment details's role.
                  returned: always
                  type: str
                  sample: '<role>'
                apManagerInterfaceIp:
                  description: It is the client enrichment details's apManagerInterfaceIp.
                  returned: always
                  type: str
                  sample: '<apmanagerinterfaceip>'
                associatedWlcIp:
                  description: It is the client enrichment details's associatedWlcIp.
                  returned: always
                  type: str
                  sample: '<associatedwlcip>'
                bootDateTime:
                  description: It is the client enrichment details's bootDateTime.
                  returned: always
                  type: dict
                collectionStatus:
                  description: It is the client enrichment details's collectionStatus.
                  returned: always
                  type: str
                  sample: '<collectionstatus>'
                interfaceCount:
                  description: It is the client enrichment details's interfaceCount.
                  returned: always
                  type: dict
                lineCardCount:
                  description: It is the client enrichment details's lineCardCount.
                  returned: always
                  type: dict
                lineCardId:
                  description: It is the client enrichment details's lineCardId.
                  returned: always
                  type: dict
                managementIpAddress:
                  description: It is the client enrichment details's managementIpAddress.
                  returned: always
                  type: str
                  sample: '<managementipaddress>'
                memorySize:
                  description: It is the client enrichment details's memorySize.
                  returned: always
                  type: str
                  sample: '<memorysize>'
                platformId:
                  description: It is the client enrichment details's platformId.
                  returned: always
                  type: str
                  sample: '<platformid>'
                reachabilityFailureReason:
                  description: It is the client enrichment details's reachabilityFailureReason.
                  returned: always
                  type: str
                  sample: '<reachabilityfailurereason>'
                reachabilityStatus:
                  description: It is the client enrichment details's reachabilityStatus.
                  returned: always
                  type: str
                  sample: '<reachabilitystatus>'
                snmpContact:
                  description: It is the client enrichment details's snmpContact.
                  returned: always
                  type: str
                  sample: '<snmpcontact>'
                snmpLocation:
                  description: It is the client enrichment details's snmpLocation.
                  returned: always
                  type: str
                  sample: '<snmplocation>'
                tunnelUdpPort:
                  description: It is the client enrichment details's tunnelUdpPort.
                  returned: always
                  type: str
                  sample: '<tunneludpport>'
                waasDeviceMode:
                  description: It is the client enrichment details's waasDeviceMode.
                  returned: always
                  type: dict
                series:
                  description: It is the client enrichment details's series.
                  returned: always
                  type: str
                  sample: '<series>'
                inventoryStatusDetail:
                  description: It is the client enrichment details's inventoryStatusDetail.
                  returned: always
                  type: str
                  sample: '<inventorystatusdetail>'
                collectionInterval:
                  description: It is the client enrichment details's collectionInterval.
                  returned: always
                  type: str
                  sample: '<collectioninterval>'
                serialNumber:
                  description: It is the client enrichment details's serialNumber.
                  returned: always
                  type: str
                  sample: '<serialnumber>'
                softwareVersion:
                  description: It is the client enrichment details's softwareVersion.
                  returned: always
                  type: str
                  sample: '<softwareversion>'
                roleSource:
                  description: It is the client enrichment details's roleSource.
                  returned: always
                  type: str
                  sample: '<rolesource>'
                hostname:
                  description: It is the client enrichment details's hostname.
                  returned: always
                  type: str
                  sample: '<hostname>'
                upTime:
                  description: It is the client enrichment details's upTime.
                  returned: always
                  type: str
                  sample: '<uptime>'
                lastUpdateTime:
                  description: It is the client enrichment details's lastUpdateTime.
                  returned: always
                  type: int
                  sample: 0
                errorDescription:
                  description: It is the client enrichment details's errorDescription.
                  returned: always
                  type: dict
                locationName:
                  description: It is the client enrichment details's locationName.
                  returned: always
                  type: dict
                tagCount:
                  description: It is the client enrichment details's tagCount.
                  returned: always
                  type: str
                  sample: '<tagcount>'
                lastUpdated:
                  description: It is the client enrichment details's lastUpdated.
                  returned: always
                  type: str
                  sample: '<lastupdated>'
                instanceUuid:
                  description: It is the client enrichment details's instanceUuid.
                  returned: always
                  type: str
                  sample: '<instanceuuid>'
                id:
                  description: It is the client enrichment details's id.
                  returned: always
                  type: str
                  sample: '478012'
                neighborTopology:
                  description: It is the client enrichment details's neighborTopology.
                  returned: always
                  type: list
                  contains:
                    nodes:
                      description: It is the client enrichment details's nodes.
                      returned: always
                      type: list
                      contains:
                        role:
                          description: It is the client enrichment details's role.
                          returned: always
                          type: str
                          sample: '<role>'
                        name:
                          description: It is the client enrichment details's name.
                          returned: always
                          type: str
                          sample: '<name>'
                        id:
                          description: It is the client enrichment details's id.
                          returned: always
                          type: str
                          sample: '478012'
                        description:
                          description: It is the client enrichment details's description.
                          returned: always
                          type: str
                          sample: '<description>'
                        deviceType:
                          description: It is the client enrichment details's deviceType.
                          returned: always
                          type: dict
                        platformId:
                          description: It is the client enrichment details's platformId.
                          returned: always
                          type: dict
                        family:
                          description: It is the client enrichment details's family.
                          returned: always
                          type: dict
                        ip:
                          description: It is the client enrichment details's ip.
                          returned: always
                          type: dict
                        softwareVersion:
                          description: It is the client enrichment details's softwareVersion.
                          returned: always
                          type: dict
                        userId:
                          description: It is the client enrichment details's userId.
                          returned: always
                          type: dict
                        nodeType:
                          description: It is the client enrichment details's nodeType.
                          returned: always
                          type: dict
                        radioFrequency:
                          description: It is the client enrichment details's radioFrequency.
                          returned: always
                          type: dict
                        clients:
                          description: It is the client enrichment details's clients.
                          returned: always
                          type: int
                          sample: 0
                        count:
                          description: It is the client enrichment details's count.
                          returned: always
                          type: dict
                        healthScore:
                          description: It is the client enrichment details's healthScore.
                          returned: always
                          type: dict
                        level:
                          description: It is the client enrichment details's level.
                          returned: always
                          type: int
                          sample: 0
                        fabricGroup:
                          description: It is the client enrichment details's fabricGroup.
                          returned: always
                          type: dict

                    links:
                      description: It is the client enrichment details's links.
                      returned: always
                      type: list
                      contains:
                        source:
                          description: It is the client enrichment details's source.
                          returned: always
                          type: str
                          sample: '<source>'
                        linkStatus:
                          description: It is the client enrichment details's linkStatus.
                          returned: always
                          type: str
                          sample: '<linkstatus>'
                        label:
                          description: It is the client enrichment details's label.
                          returned: always
                          type: list
                        target:
                          description: It is the client enrichment details's target.
                          returned: always
                          type: str
                          sample: '<target>'
                        id:
                          description: It is the client enrichment details's id.
                          returned: always
                          type: dict
                        portUtilization:
                          description: It is the client enrichment details's portUtilization.
                          returned: always
                          type: dict


                cisco360view:
                  description: It is the client enrichment details's cisco360view.
                  returned: always
                  type: str
                  sample: '<cisco360view>'


        issueDetails:
          description: It is the client enrichment details's issueDetails.
          returned: always
          type: dict
          contains:
            issue:
              description: It is the client enrichment details's issue.
              returned: always
              type: list
              contains:
                issueId:
                  description: It is the client enrichment details's issueId.
                  returned: always
                  type: str
                  sample: '<issueid>'
                issueSource:
                  description: It is the client enrichment details's issueSource.
                  returned: always
                  type: str
                  sample: '<issuesource>'
                issueCategory:
                  description: It is the client enrichment details's issueCategory.
                  returned: always
                  type: str
                  sample: '<issuecategory>'
                issueName:
                  description: It is the client enrichment details's issueName.
                  returned: always
                  type: str
                  sample: '<issuename>'
                issueDescription:
                  description: It is the client enrichment details's issueDescription.
                  returned: always
                  type: str
                  sample: '<issuedescription>'
                issueEntity:
                  description: It is the client enrichment details's issueEntity.
                  returned: always
                  type: str
                  sample: '<issueentity>'
                issueEntityValue:
                  description: It is the client enrichment details's issueEntityValue.
                  returned: always
                  type: str
                  sample: '<issueentityvalue>'
                issueSeverity:
                  description: It is the client enrichment details's issueSeverity.
                  returned: always
                  type: str
                  sample: '<issueseverity>'
                issuePriority:
                  description: It is the client enrichment details's issuePriority.
                  returned: always
                  type: str
                  sample: '<issuepriority>'
                issueSummary:
                  description: It is the client enrichment details's issueSummary.
                  returned: always
                  type: str
                  sample: '<issuesummary>'
                issueTimestamp:
                  description: It is the client enrichment details's issueTimestamp.
                  returned: always
                  type: int
                  sample: 0
                suggestedActions:
                  description: It is the client enrichment details's suggestedActions.
                  returned: always
                  type: list
                  contains:
                    message:
                      description: It is the client enrichment details's message.
                      returned: always
                      type: str
                      sample: '<message>'
                    steps:
                      description: It is the client enrichment details's steps.
                      returned: always
                      type: list

                impactedHosts:
                  description: It is the client enrichment details's impactedHosts.
                  returned: always
                  type: list
                  contains:
                    hostType:
                      description: It is the client enrichment details's hostType.
                      returned: always
                      type: str
                      sample: '<hosttype>'
                    hostName:
                      description: It is the client enrichment details's hostName.
                      returned: always
                      type: str
                      sample: '<hostname>'
                    hostOs:
                      description: It is the client enrichment details's hostOs.
                      returned: always
                      type: str
                      sample: '<hostos>'
                    ssid:
                      description: It is the client enrichment details's ssid.
                      returned: always
                      type: str
                      sample: '<ssid>'
                    connectedInterface:
                      description: It is the client enrichment details's connectedInterface.
                      returned: always
                      type: str
                      sample: '<connectedinterface>'
                    macAddress:
                      description: It is the client enrichment details's macAddress.
                      returned: always
                      type: str
                      sample: '<macaddress>'
                    failedAttempts:
                      description: It is the client enrichment details's failedAttempts.
                      returned: always
                      type: int
                      sample: 0
                    location:
                      description: It is the client enrichment details's location.
                      returned: always
                      type: dict
                      contains:
                        siteId:
                          description: It is the client enrichment details's siteId.
                          returned: always
                          type: str
                          sample: '<siteid>'
                        siteType:
                          description: It is the client enrichment details's siteType.
                          returned: always
                          type: str
                          sample: '<sitetype>'
                        area:
                          description: It is the client enrichment details's area.
                          returned: always
                          type: str
                          sample: '<area>'
                        building:
                          description: It is the client enrichment details's building.
                          returned: always
                          type: str
                          sample: '<building>'
                        floor:
                          description: It is the client enrichment details's floor.
                          returned: always
                          type: dict
                        apsImpacted:
                          description: It is the client enrichment details's apsImpacted.
                          returned: always
                          type: list

                    timestamp:
                      description: It is the client enrichment details's timestamp.
                      returned: always
                      type: int
                      sample: 0





"""

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
- name: get_device_enrichment_details
  cisco.dnac.device_enrichment_details:
    state: query  # required
    headers:  # required
  register: query_result
  
"""

RETURN = """
get_device_enrichment_details:
    description: Enriches a given network device context (device id or device Mac Address or device management IP address) with details about the device and neighbor topology.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the device enrichment details's payload.
      returned: always
      type: list
      contains:
        deviceDetails:
          description: It is the device enrichment details's deviceDetails.
          returned: always
          type: dict
          contains:
            family:
              description: It is the device enrichment details's family.
              returned: always
              type: str
              sample: '<family>'
            type:
              description: It is the device enrichment details's type.
              returned: always
              type: str
              sample: '<type>'
            location:
              description: It is the device enrichment details's location.
              returned: always
              type: dict
            errorCode:
              description: It is the device enrichment details's errorCode.
              returned: always
              type: str
              sample: '<errorcode>'
            macAddress:
              description: It is the device enrichment details's macAddress.
              returned: always
              type: str
              sample: '<macaddress>'
            role:
              description: It is the device enrichment details's role.
              returned: always
              type: str
              sample: '<role>'
            apManagerInterfaceIp:
              description: It is the device enrichment details's apManagerInterfaceIp.
              returned: always
              type: str
              sample: '<apmanagerinterfaceip>'
            associatedWlcIp:
              description: It is the device enrichment details's associatedWlcIp.
              returned: always
              type: str
              sample: '<associatedwlcip>'
            bootDateTime:
              description: It is the device enrichment details's bootDateTime.
              returned: always
              type: str
              sample: '<bootdatetime>'
            collectionStatus:
              description: It is the device enrichment details's collectionStatus.
              returned: always
              type: str
              sample: '<collectionstatus>'
            interfaceCount:
              description: It is the device enrichment details's interfaceCount.
              returned: always
              type: str
              sample: '<interfacecount>'
            lineCardCount:
              description: It is the device enrichment details's lineCardCount.
              returned: always
              type: str
              sample: '<linecardcount>'
            lineCardId:
              description: It is the device enrichment details's lineCardId.
              returned: always
              type: str
              sample: '<linecardid>'
            managementIpAddress:
              description: It is the device enrichment details's managementIpAddress.
              returned: always
              type: str
              sample: '<managementipaddress>'
            memorySize:
              description: It is the device enrichment details's memorySize.
              returned: always
              type: str
              sample: '<memorysize>'
            platformId:
              description: It is the device enrichment details's platformId.
              returned: always
              type: str
              sample: '<platformid>'
            reachabilityFailureReason:
              description: It is the device enrichment details's reachabilityFailureReason.
              returned: always
              type: str
              sample: '<reachabilityfailurereason>'
            reachabilityStatus:
              description: It is the device enrichment details's reachabilityStatus.
              returned: always
              type: str
              sample: '<reachabilitystatus>'
            snmpContact:
              description: It is the device enrichment details's snmpContact.
              returned: always
              type: str
              sample: '<snmpcontact>'
            snmpLocation:
              description: It is the device enrichment details's snmpLocation.
              returned: always
              type: str
              sample: '<snmplocation>'
            tunnelUdpPort:
              description: It is the device enrichment details's tunnelUdpPort.
              returned: always
              type: dict
            waasDeviceMode:
              description: It is the device enrichment details's waasDeviceMode.
              returned: always
              type: dict
            series:
              description: It is the device enrichment details's series.
              returned: always
              type: str
              sample: '<series>'
            inventoryStatusDetail:
              description: It is the device enrichment details's inventoryStatusDetail.
              returned: always
              type: str
              sample: '<inventorystatusdetail>'
            collectionInterval:
              description: It is the device enrichment details's collectionInterval.
              returned: always
              type: str
              sample: '<collectioninterval>'
            serialNumber:
              description: It is the device enrichment details's serialNumber.
              returned: always
              type: str
              sample: '<serialnumber>'
            softwareVersion:
              description: It is the device enrichment details's softwareVersion.
              returned: always
              type: str
              sample: '<softwareversion>'
            roleSource:
              description: It is the device enrichment details's roleSource.
              returned: always
              type: str
              sample: '<rolesource>'
            hostname:
              description: It is the device enrichment details's hostname.
              returned: always
              type: str
              sample: '<hostname>'
            upTime:
              description: It is the device enrichment details's upTime.
              returned: always
              type: str
              sample: '<uptime>'
            lastUpdateTime:
              description: It is the device enrichment details's lastUpdateTime.
              returned: always
              type: int
              sample: 0
            errorDescription:
              description: It is the device enrichment details's errorDescription.
              returned: always
              type: str
              sample: '<errordescription>'
            locationName:
              description: It is the device enrichment details's locationName.
              returned: always
              type: dict
            tagCount:
              description: It is the device enrichment details's tagCount.
              returned: always
              type: str
              sample: '<tagcount>'
            lastUpdated:
              description: It is the device enrichment details's lastUpdated.
              returned: always
              type: str
              sample: '<lastupdated>'
            instanceUuid:
              description: It is the device enrichment details's instanceUuid.
              returned: always
              type: str
              sample: '<instanceuuid>'
            id:
              description: It is the device enrichment details's id.
              returned: always
              type: str
              sample: '478012'
            neighborTopology:
              description: It is the device enrichment details's neighborTopology.
              returned: always
              type: list
              contains:
                nodes:
                  description: It is the device enrichment details's nodes.
                  returned: always
                  type: list
                  contains:
                    role:
                      description: It is the device enrichment details's role.
                      returned: always
                      type: str
                      sample: '<role>'
                    name:
                      description: It is the device enrichment details's name.
                      returned: always
                      type: str
                      sample: '<name>'
                    id:
                      description: It is the device enrichment details's id.
                      returned: always
                      type: str
                      sample: '478012'
                    description:
                      description: It is the device enrichment details's description.
                      returned: always
                      type: str
                      sample: '<description>'
                    deviceType:
                      description: It is the device enrichment details's deviceType.
                      returned: always
                      type: str
                      sample: '<devicetype>'
                    platformId:
                      description: It is the device enrichment details's platformId.
                      returned: always
                      type: str
                      sample: '<platformid>'
                    family:
                      description: It is the device enrichment details's family.
                      returned: always
                      type: str
                      sample: '<family>'
                    ip:
                      description: It is the device enrichment details's ip.
                      returned: always
                      type: str
                      sample: '1.1.1.17'
                    softwareVersion:
                      description: It is the device enrichment details's softwareVersion.
                      returned: always
                      type: str
                      sample: '<softwareversion>'
                    userId:
                      description: It is the device enrichment details's userId.
                      returned: always
                      type: dict
                    nodeType:
                      description: It is the device enrichment details's nodeType.
                      returned: always
                      type: str
                      sample: '<nodetype>'
                    radioFrequency:
                      description: It is the device enrichment details's radioFrequency.
                      returned: always
                      type: dict
                    clients:
                      description: It is the device enrichment details's clients.
                      returned: always
                      type: dict
                    count:
                      description: It is the device enrichment details's count.
                      returned: always
                      type: dict
                    healthScore:
                      description: It is the device enrichment details's healthScore.
                      returned: always
                      type: int
                      sample: 0
                    level:
                      description: It is the device enrichment details's level.
                      returned: always
                      type: int
                      sample: 0
                    fabricGroup:
                      description: It is the device enrichment details's fabricGroup.
                      returned: always
                      type: dict
                    connectedDevice:
                      description: It is the device enrichment details's connectedDevice.
                      returned: always
                      type: dict

                links:
                  description: It is the device enrichment details's links.
                  returned: always
                  type: list
                  contains:
                    source:
                      description: It is the device enrichment details's source.
                      returned: always
                      type: str
                      sample: '<source>'
                    linkStatus:
                      description: It is the device enrichment details's linkStatus.
                      returned: always
                      type: str
                      sample: '<linkstatus>'
                    label:
                      description: It is the device enrichment details's label.
                      returned: always
                      type: list
                    target:
                      description: It is the device enrichment details's target.
                      returned: always
                      type: str
                      sample: '<target>'
                    id:
                      description: It is the device enrichment details's id.
                      returned: always
                      type: dict
                    portUtilization:
                      description: It is the device enrichment details's portUtilization.
                      returned: always
                      type: dict





"""

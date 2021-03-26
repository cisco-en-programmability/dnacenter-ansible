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
module: discovery_network_device
short_description: Manage DiscoveryNetworkDevice objects of Discovery
description:
- Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the network devices discovered for the given discovery and for the given range. The maximum number of records that can be retrieved is 500. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the count of network devices discovered in the given discovery. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the network devices from a discovery job based on given filters. Discovery ID can be obtained using the "Get Discoveries by range" API.
version_added: '1.0'
author: Rafael Campos (@racampos)
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
  count:
    description:
    - If true gets the number of objects.
    type: bool
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
"""

EXAMPLES = r"""
- name: get_discovered_network_devices_by_discovery_id
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    task_id: SomeValue  # string
  register: query_result
  - name: get_discovered_devices_by_range
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    records_to_return: 1  #  integer, required
    start_index: 1  #  integer, required
    task_id: SomeValue  # string
  register: query_result
  - name: get_devices_discovered_by_id
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    count: True  # boolean, required
    task_id: SomeValue  # string
  register: query_result
  - name: get_network_devices_from_discovery
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    summary: True  # boolean, required
    cli_status: SomeValue  # string
    http_status: SomeValue  # string
    ip_address: SomeValue  # string
    netconf_status: SomeValue  # string
    ping_status: SomeValue  # string
    snmp_status: SomeValue  # string
    sort_by: SomeValue  # string
    sort_order: SomeValue  # string
    task_id: SomeValue  # string
  register: query_result
  """

RETURN = """
get_discovered_network_devices_by_discovery_id:
    description: Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        anchorWlcForAp:
          description: It is the discovery network device's anchorWlcForAp.
          returned: always
          type: str
          sample: '<anchorwlcforap>'
        authModelId:
          description: It is the discovery network device's authModelId.
          returned: always
          type: str
          sample: '<authmodelid>'
        avgUpdateFrequency:
          description: It is the discovery network device's avgUpdateFrequency.
          returned: always
          type: int
          sample: 0
        bootDateTime:
          description: It is the discovery network device's bootDateTime.
          returned: always
          type: str
          sample: '<bootdatetime>'
        cliStatus:
          description: It is the discovery network device's cliStatus.
          returned: always
          type: str
          sample: '<clistatus>'
        duplicateDeviceId:
          description: It is the discovery network device's duplicateDeviceId.
          returned: always
          type: str
          sample: '<duplicatedeviceid>'
        errorCode:
          description: It is the discovery network device's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorDescription:
          description: It is the discovery network device's errorDescription.
          returned: always
          type: str
          sample: '<errordescription>'
        family:
          description: It is the discovery network device's family.
          returned: always
          type: str
          sample: '<family>'
        hostname:
          description: It is the discovery network device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        httpStatus:
          description: It is the discovery network device's httpStatus.
          returned: always
          type: str
          sample: '<httpstatus>'
        id:
          description: It is the discovery network device's id.
          returned: always
          type: str
          sample: '478012'
        imageName:
          description: It is the discovery network device's imageName.
          returned: always
          type: str
          sample: '<imagename>'
        ingressQueueConfig:
          description: It is the discovery network device's ingressQueueConfig.
          returned: always
          type: str
          sample: '<ingressqueueconfig>'
        interfaceCount:
          description: It is the discovery network device's interfaceCount.
          returned: always
          type: str
          sample: '<interfacecount>'
        inventoryCollectionStatus:
          description: It is the discovery network device's inventoryCollectionStatus.
          returned: always
          type: str
          sample: '<inventorycollectionstatus>'
        inventoryReachabilityStatus:
          description: It is the discovery network device's inventoryReachabilityStatus.
          returned: always
          type: str
          sample: '<inventoryreachabilitystatus>'
        lastUpdated:
          description: It is the discovery network device's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        lineCardCount:
          description: It is the discovery network device's lineCardCount.
          returned: always
          type: str
          sample: '<linecardcount>'
        lineCardId:
          description: It is the discovery network device's lineCardId.
          returned: always
          type: str
          sample: '<linecardid>'
        location:
          description: It is the discovery network device's location.
          returned: always
          type: str
          sample: '<location>'
        locationName:
          description: It is the discovery network device's locationName.
          returned: always
          type: str
          sample: '<locationname>'
        macAddress:
          description: It is the discovery network device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        managementIpAddress:
          description: It is the discovery network device's managementIpAddress.
          returned: always
          type: str
          sample: '<managementipaddress>'
        memorySize:
          description: It is the discovery network device's memorySize.
          returned: always
          type: str
          sample: '<memorysize>'
        netconfStatus:
          description: It is the discovery network device's netconfStatus.
          returned: always
          type: str
          sample: '<netconfstatus>'
        numUpdates:
          description: It is the discovery network device's numUpdates.
          returned: always
          type: int
          sample: 0
        pingStatus:
          description: It is the discovery network device's pingStatus.
          returned: always
          type: str
          sample: '<pingstatus>'
        platformId:
          description: It is the discovery network device's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        portRange:
          description: It is the discovery network device's portRange.
          returned: always
          type: str
          sample: '<portrange>'
        qosStatus:
          description: It is the discovery network device's qosStatus.
          returned: always
          type: str
          sample: '<qosstatus>'
        reachabilityFailureReason:
          description: It is the discovery network device's reachabilityFailureReason.
          returned: always
          type: str
          sample: '<reachabilityfailurereason>'
        reachabilityStatus:
          description: It is the discovery network device's reachabilityStatus.
          returned: always
          type: str
          sample: '<reachabilitystatus>'
        role:
          description: It is the discovery network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the discovery network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'
        serialNumber:
          description: It is the discovery network device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        snmpContact:
          description: It is the discovery network device's snmpContact.
          returned: always
          type: str
          sample: '<snmpcontact>'
        snmpLocation:
          description: It is the discovery network device's snmpLocation.
          returned: always
          type: str
          sample: '<snmplocation>'
        snmpStatus:
          description: It is the discovery network device's snmpStatus.
          returned: always
          type: str
          sample: '<snmpstatus>'
        softwareVersion:
          description: It is the discovery network device's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        tag:
          description: It is the discovery network device's tag.
          returned: always
          type: str
          sample: '<tag>'
        tagCount:
          description: It is the discovery network device's tagCount.
          returned: always
          type: int
          sample: 0
        type:
          description: It is the discovery network device's type.
          returned: always
          type: str
          sample: '<type>'
        upTime:
          description: It is the discovery network device's upTime.
          returned: always
          type: str
          sample: '<uptime>'
        vendor:
          description: It is the discovery network device's vendor.
          returned: always
          type: str
          sample: '<vendor>'
        wlcApDeviceStatus:
          description: It is the discovery network device's wlcApDeviceStatus.
          returned: always
          type: str
          sample: '<wlcapdevicestatus>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_discovered_devices_by_range:
    description: Returns the network devices discovered for the given discovery and for the given range. The maximum number of records that can be retrieved is 500. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        anchorWlcForAp:
          description: It is the discovery network device's anchorWlcForAp.
          returned: always
          type: str
          sample: '<anchorwlcforap>'
        authModelId:
          description: It is the discovery network device's authModelId.
          returned: always
          type: str
          sample: '<authmodelid>'
        avgUpdateFrequency:
          description: It is the discovery network device's avgUpdateFrequency.
          returned: always
          type: int
          sample: 0
        bootDateTime:
          description: It is the discovery network device's bootDateTime.
          returned: always
          type: str
          sample: '<bootdatetime>'
        cliStatus:
          description: It is the discovery network device's cliStatus.
          returned: always
          type: str
          sample: '<clistatus>'
        duplicateDeviceId:
          description: It is the discovery network device's duplicateDeviceId.
          returned: always
          type: str
          sample: '<duplicatedeviceid>'
        errorCode:
          description: It is the discovery network device's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorDescription:
          description: It is the discovery network device's errorDescription.
          returned: always
          type: str
          sample: '<errordescription>'
        family:
          description: It is the discovery network device's family.
          returned: always
          type: str
          sample: '<family>'
        hostname:
          description: It is the discovery network device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        httpStatus:
          description: It is the discovery network device's httpStatus.
          returned: always
          type: str
          sample: '<httpstatus>'
        id:
          description: It is the discovery network device's id.
          returned: always
          type: str
          sample: '478012'
        imageName:
          description: It is the discovery network device's imageName.
          returned: always
          type: str
          sample: '<imagename>'
        ingressQueueConfig:
          description: It is the discovery network device's ingressQueueConfig.
          returned: always
          type: str
          sample: '<ingressqueueconfig>'
        interfaceCount:
          description: It is the discovery network device's interfaceCount.
          returned: always
          type: str
          sample: '<interfacecount>'
        inventoryCollectionStatus:
          description: It is the discovery network device's inventoryCollectionStatus.
          returned: always
          type: str
          sample: '<inventorycollectionstatus>'
        inventoryReachabilityStatus:
          description: It is the discovery network device's inventoryReachabilityStatus.
          returned: always
          type: str
          sample: '<inventoryreachabilitystatus>'
        lastUpdated:
          description: It is the discovery network device's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        lineCardCount:
          description: It is the discovery network device's lineCardCount.
          returned: always
          type: str
          sample: '<linecardcount>'
        lineCardId:
          description: It is the discovery network device's lineCardId.
          returned: always
          type: str
          sample: '<linecardid>'
        location:
          description: It is the discovery network device's location.
          returned: always
          type: str
          sample: '<location>'
        locationName:
          description: It is the discovery network device's locationName.
          returned: always
          type: str
          sample: '<locationname>'
        macAddress:
          description: It is the discovery network device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        managementIpAddress:
          description: It is the discovery network device's managementIpAddress.
          returned: always
          type: str
          sample: '<managementipaddress>'
        memorySize:
          description: It is the discovery network device's memorySize.
          returned: always
          type: str
          sample: '<memorysize>'
        netconfStatus:
          description: It is the discovery network device's netconfStatus.
          returned: always
          type: str
          sample: '<netconfstatus>'
        numUpdates:
          description: It is the discovery network device's numUpdates.
          returned: always
          type: int
          sample: 0
        pingStatus:
          description: It is the discovery network device's pingStatus.
          returned: always
          type: str
          sample: '<pingstatus>'
        platformId:
          description: It is the discovery network device's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        portRange:
          description: It is the discovery network device's portRange.
          returned: always
          type: str
          sample: '<portrange>'
        qosStatus:
          description: It is the discovery network device's qosStatus.
          returned: always
          type: str
          sample: '<qosstatus>'
        reachabilityFailureReason:
          description: It is the discovery network device's reachabilityFailureReason.
          returned: always
          type: str
          sample: '<reachabilityfailurereason>'
        reachabilityStatus:
          description: It is the discovery network device's reachabilityStatus.
          returned: always
          type: str
          sample: '<reachabilitystatus>'
        role:
          description: It is the discovery network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the discovery network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'
        serialNumber:
          description: It is the discovery network device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        snmpContact:
          description: It is the discovery network device's snmpContact.
          returned: always
          type: str
          sample: '<snmpcontact>'
        snmpLocation:
          description: It is the discovery network device's snmpLocation.
          returned: always
          type: str
          sample: '<snmplocation>'
        snmpStatus:
          description: It is the discovery network device's snmpStatus.
          returned: always
          type: str
          sample: '<snmpstatus>'
        softwareVersion:
          description: It is the discovery network device's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        tag:
          description: It is the discovery network device's tag.
          returned: always
          type: str
          sample: '<tag>'
        tagCount:
          description: It is the discovery network device's tagCount.
          returned: always
          type: int
          sample: 0
        type:
          description: It is the discovery network device's type.
          returned: always
          type: str
          sample: '<type>'
        upTime:
          description: It is the discovery network device's upTime.
          returned: always
          type: str
          sample: '<uptime>'
        vendor:
          description: It is the discovery network device's vendor.
          returned: always
          type: str
          sample: '<vendor>'
        wlcApDeviceStatus:
          description: It is the discovery network device's wlcApDeviceStatus.
          returned: always
          type: str
          sample: '<wlcapdevicestatus>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_devices_discovered_by_id:
    description: Returns the count of network devices discovered in the given discovery. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_network_devices_from_discovery:
    description: Returns the network devices from a discovery job based on given filters. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

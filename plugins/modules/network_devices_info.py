#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_devices_info
short_description: Information module for Network Devices Info
description:
- This module represents an alias of the module network_devices_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description:
    - >
      StartTime query parameter. Start time from which API queries the data set related to the resource. It must
      be specified in UNIX epochtime in milliseconds. Value is inclusive. If `startTime` is not provided, API will
      default to current time.
    type: float
  endTime:
    description:
    - >
      EndTime query parameter. End time to which API queries the data set related to the resource. It must be
      specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  limit:
    description:
    - Limit query parameter. Maximum number of records to return.
    type: float
  offset:
    description:
    - >
      Offset query parameter. Specifies the starting point within all records returned by the API. It's one based
      offset. The starting value is 1.
    type: float
  sortBy:
    description:
    - SortBy query parameter. A field within the response to sort by.
    type: str
  order:
    description:
    - Order query parameter. The sort order of the field ascending or descending.
    type: str
  siteHierarchy:
    description:
    - >
      SiteHierarchy query parameter. The full hierarchical breakdown of the site tree starting from Global site
      name and ending with the specific site name. The Root site is named "Global" (Ex.
      `Global/AreaName/BuildingName/FloorName`) This field supports wildcard asterisk (*) character search
      support. E.g. */San*, */San, /San* Examples `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
      siteHierarchy requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaNam
      e2/BuildingName2/FloorName2` (multiple siteHierarchies requested).
    type: str
  siteHierarchyId:
    description:
    - >
      SiteHierarchyId query parameter. The full hierarchy breakdown of the site tree in id form starting from
      Global site UUID and ending with the specific site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`)
      This field supports wildcard asterisk (*) character search support. E.g. `*uuid*, *uuid, uuid* Examples
      `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId requested) `?siteHiera
      rchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUu
      id2` (multiple siteHierarchyIds requested).
    type: str
  siteId:
    description:
    - >
      SiteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports wildcard asterisk (*)
      character search support. E.g.*flooruuid*, *flooruuid, flooruuid* Examples `?siteId=id1` (single id
      requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested).
    type: str
  id:
    description:
    - >
      Id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples
      id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-4170-8375-
      b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-8aa2-79b233318ba0 (multiple
      entity uuid with '&' separator).
    type: str
  managementIpAddress:
    description:
    - >
      ManagementIpAddress query parameter. The list of entity management IP Address. It can be either Ipv4 or Ipv6
      address or combination of both(Ex. "121.1.1.10") This field supports wildcard (`*`) character-based search.
      Ex `*1.1*` or `1.1*` or `*1.1` Examples managementIpAddresses=121.1.1.10
      managementIpAddresses=121.1.1.10&managementIpAddresses=172.20.1.10&managementIpAddresses=200
      10&=managementIpAddresses172.20.3.4 (multiple entity IP Address with & separator).
    type: str
  macAddress:
    description:
    - >
      MacAddress query parameter. The macAddress of the network device or client This field supports wildcard
      (`*`) character-based search. Ex `*AB AB AB*` or `AB AB AB*` or `*AB AB AB` Examples `macAddress=AB AB AB CD
      CD CD` (single macAddress requested) `macAddress=AB AB AB CD CD DC&macAddress=AB AB AB CD CD FE` (multiple
      macAddress requested).
    type: str
  family:
    description:
    - >
      Family query parameter. The list of network device family names Examples family=Switches and Hubs (single
      network device family name )family=Switches and Hubs&family=Router&family=Wireless Controller (multiple
      Network device family names with & separator). This field is not case sensitive.
    type: str
  type:
    description:
    - >
      Type query parameter. The list of network device type This field supports wildcard (`*`) character-based
      search. Ex `*9407R*` or `*9407R` or `9407R*` Examples type=SwitchesCisco Catalyst 9407R Switch (single
      network device types ) type=Cisco Catalyst 38xx stack-able ethernet switch&type=Cisco 3945 Integrated
      Services Router G2 (multiple Network device types with & separator).
    type: str
  role:
    description:
    - >
      Role query parameter. The list of network device role. Examples role=CORE, role=CORE&role=ACCESS&role=ROUTER
      (multiple Network device roles with & separator). This field is not case sensitive.
    type: str
  serialNumber:
    description:
    - >
      SerialNumber query parameter. The list of network device serial numbers. This field supports wildcard (`*`)
      character-based search. Ex `*MS1SV*` or `MS1SV*` or `*MS1SV` Examples serialNumber=9FUFMS1SVAX
      serialNumber=9FUFMS1SVAX&FCW2333Q0BY&FJC240617JX(multiple Network device serial number with & separator).
    type: str
  maintenanceMode:
    description:
    - MaintenanceMode query parameter. The device maintenanceMode status true or false.
    type: bool
  softwareVersion:
    description:
    - >
      SoftwareVersion query parameter. The list of network device software version This field supports wildcard
      (`*`) character-based search. Ex `*17.8*` or `*17.8` or `17.8*` Examples softwareVersion=2.3.4.0 (single
      network device software version ) softwareVersion=17.9.3.23&softwareVersion=17.7.1.2&softwareVersion=*.17.7
      (multiple Network device software versions with & separator).
    type: str
  healthScore:
    description:
    - >
      HealthScore query parameter. The list of entity health score categories Examples healthScore=good,
      healthScore=good&healthScore=fair (multiple entity healthscore values with & separator). This field is not
      case sensitive.
    type: str
  view:
    description:
    - >
      View query parameter. The List of Network Device model views. Please refer to ```NetworkDeviceView``` for
      the supported list.
    type: str
  attribute:
    description:
    - >
      Attribute query parameter. The List of Network Device model attributes. This is helps to specify the
      interested fields in the request.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetTheDeviceDataForTheGivenDeviceIdUuidV1
  description: Complete reference of the GetTheDeviceDataForTheGivenDeviceIdUuidV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-the-device-data-for-the-given-device-id-uuid
- name: Cisco DNA Center documentation for Devices GetsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParametersV1
  description: Complete reference of the GetsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParametersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-the-network-device-details-based-on-the-provided-query-parameters  # noqa: E501
notes:
  - SDK Method used are
    devices.Devices.get_the_device_data_for_the_given_device_id_uuid_v1,
    devices.Devices.gets_the_network_device_details_based_on_the_provided_query_parameters_v1,

  - Paths used are
    get /dna/data/api/v1/networkDevices,
    get /dna/data/api/v1/networkDevices/{id},
  - It should be noted that this module is an alias of network_devices_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Devices Info
  cisco.dnac.network_devices_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    limit: 0
    offset: 0
    sortBy: string
    order: string
    siteHierarchy: string
    siteHierarchyId: string
    siteId: string
    id: string
    managementIpAddress: string
    macAddress: string
    family: string
    type: string
    role: string
    serialNumber: string
    maintenanceMode: True
    softwareVersion: string
    healthScore: string
    view: string
    attribute: string
  register: result

- name: Get Network Devices Info by id
  cisco.dnac.network_devices_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    view: string
    attribute: string
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "name": "string",
        "managementIpAddress": "string",
        "platformId": "string",
        "deviceFamily": "string",
        "serialNumber": "string",
        "macAddress": "string",
        "deviceSeries": "string",
        "softwareVersion": "string",
        "productVendor": "string",
        "deviceRole": "string",
        "deviceType": "string",
        "communicationState": "string",
        "collectionStatus": "string",
        "haStatus": "string",
        "lastBootTime": 0,
        "siteHierarchyId": "string",
        "siteHierarchy": "string",
        "siteId": "string",
        "deviceGroupHierarchyId": "string",
        "tagNames": [
          "string"
        ],
        "stackType": "string",
        "osType": "string",
        "ringStatus": true,
        "maintenanceModeEnabled": true,
        "upTime": 0,
        "ipv4Address": "string",
        "ipv6Address": "string",
        "redundancyMode": "string",
        "featureFlagList": [
          "string"
        ],
        "haLastResetReason": "string",
        "redundancyPeerStateDerived": "string",
        "redundancyPeerState": "string",
        "redundancyStateDerived": "string",
        "redundancyState": "string",
        "wiredClientCount": 0,
        "wirelessClientCount": 0,
        "portCount": 0,
        "clientCount": 0,
        "apDetails": {
          "connectedWlcName": "string",
          "policyTagName": "string",
          "apOperationalState": "string",
          "powerSaveMode": "string",
          "operationalMode": "string",
          "resetReason": "string",
          "protocol": "string",
          "powerMode": "string",
          "connectedTime": 0,
          "ledFlashEnabled": true,
          "ledFlashSeconds": 0,
          "subMode": "string",
          "homeApEnabled": true,
          "powerType": "string",
          "apType": "string",
          "adminState": "string",
          "icapCapability": "string",
          "regulatoryDomain": "string",
          "ethernetMac": "string",
          "rfTagName": "string",
          "siteTagName": "string",
          "powerSaveModeCapable": "string",
          "powerProfile": "string",
          "flexGroup": "string",
          "powerCalendarProfile": "string",
          "apGroup": "string",
          "radios": [
            {
              "id": "string",
              "band": "string",
              "noise": 0,
              "airQuality": 0,
              "interference": 0,
              "trafficUtil": 0,
              "utilization": 0,
              "clientCount": 0
            }
          ]
        },
        "metricsDetails": {
          "overallHealthScore": 0,
          "overallFabricScore": 0,
          "cpuUtilization": 0,
          "cpuScore": 0,
          "memoryUtilization": 0,
          "memoryScore": 0,
          "avgTemperature": 0,
          "maxTemperature": 0,
          "discardScore": 0,
          "discardInterfaces": [
            "string"
          ],
          "errorScore": 0,
          "errorInterfaces": [
            "string"
          ],
          "interDeviceLinkScore": 0,
          "interDeviceConnectedDownInterfaces": [
            "string"
          ],
          "linkUtilizationScore": 0,
          "highLinkUtilizationInterfaces": [
            "string"
          ],
          "freeTimerScore": 0,
          "freeTimer": 0,
          "packetPoolScore": 0,
          "packetPool": 0,
          "freeMemoryBufferScore": 0,
          "freeMemoryBuffer": 0,
          "wqePoolScore": 0,
          "wqePool": 0,
          "apCount": 0,
          "noiseScore": 0,
          "utilizationScore": 0,
          "interferenceScore": 0,
          "airQualityScore": 0
        },
        "fabricDetails": {
          "fabricRole": [
            "string"
          ],
          "fabricSiteName": "string",
          "transitFabrics": [
            "string"
          ]
        },
        "aggregateAttributes": [
          {
            "name": "string",
            "function": "string",
            "value": 0
          }
        ]
      },
      "version": "string"
    }
"""

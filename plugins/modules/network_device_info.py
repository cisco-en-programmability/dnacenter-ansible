#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_info
short_description: Information module for Network Device
description:
- Get all Network Device.
- Get Network Device by id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  hostname:
    description:
    - Hostname query parameter.
    type: list
  managementIpAddress:
    description:
    - ManagementIpAddress query parameter.
    type: list
  macAddress:
    description:
    - MacAddress query parameter.
    type: list
  locationName:
    description:
    - LocationName query parameter.
    type: list
  serialNumber:
    description:
    - SerialNumber query parameter.
    type: list
  location:
    description:
    - Location query parameter.
    type: list
  family:
    description:
    - Family query parameter.
    type: list
  type:
    description:
    - Type query parameter.
    type: list
  series:
    description:
    - Series query parameter.
    type: list
  collectionStatus:
    description:
    - CollectionStatus query parameter.
    type: list
  collectionInterval:
    description:
    - CollectionInterval query parameter.
    type: list
  notSyncedForMinutes:
    description:
    - NotSyncedForMinutes query parameter.
    type: list
  errorCode:
    description:
    - ErrorCode query parameter.
    type: list
  errorDescription:
    description:
    - ErrorDescription query parameter.
    type: list
  softwareVersion:
    description:
    - SoftwareVersion query parameter.
    type: list
  softwareType:
    description:
    - SoftwareType query parameter.
    type: list
  platformId:
    description:
    - PlatformId query parameter.
    type: list
  role:
    description:
    - Role query parameter.
    type: list
  reachabilityStatus:
    description:
    - ReachabilityStatus query parameter.
    type: list
  upTime:
    description:
    - UpTime query parameter.
    type: list
  associatedWlcIp:
    description:
    - AssociatedWlcIp query parameter.
    type: list
  license_name:
    description:
    - License.name query parameter.
    type: list
  license_type:
    description:
    - License.type query parameter.
    type: list
  license_status:
    description:
    - License.status query parameter.
    type: list
  module_name:
    description:
    - Module+name query parameter.
    type: list
  module_equpimenttype:
    description:
    - Module+equpimenttype query parameter.
    type: list
  module_servicestate:
    description:
    - Module+servicestate query parameter.
    type: list
  module_vendorequipmenttype:
    description:
    - Module+vendorequipmenttype query parameter.
    type: list
  module_partnumber:
    description:
    - Module+partnumber query parameter.
    type: list
  module_operationstatecode:
    description:
    - Module+operationstatecode query parameter.
    type: list
  id:
    description:
    - >
      Id query parameter. Accepts comma separated ids and return list of network-devices for the given ids. If
      invalid or not-found ids are provided, null entry will be returned in the list.
    type: str
  deviceSupportLevel:
    description:
    - DeviceSupportLevel query parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Network Device reference
  description: Complete reference of the Network Device object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Device
  cisco.dnac.network_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    hostname: []
    managementIpAddress: []
    macAddress: []
    locationName: []
    serialNumber: []
    location: []
    family: []
    type: []
    series: []
    collectionStatus: []
    collectionInterval: []
    notSyncedForMinutes: []
    errorCode: []
    errorDescription: []
    softwareVersion: []
    softwareType: []
    platformId: []
    role: []
    reachabilityStatus: []
    upTime: []
    associatedWlcIp: []
    license_name: []
    license_type: []
    license_status: []
    module_name: []
    module_equpimenttype: []
    module_servicestate: []
    module_vendorequipmenttype: []
    module_partnumber: []
    module_operationstatecode: []
    id: string
    deviceSupportLevel: string
  register: result

- name: Get Network Device by id
  cisco.dnac.network_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
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
        "apManagerInterfaceIp": "string",
        "associatedWlcIp": "string",
        "bootDateTime": "string",
        "collectionInterval": "string",
        "collectionStatus": "string",
        "errorCode": "string",
        "errorDescription": "string",
        "family": "string",
        "hostname": "string",
        "id": "string",
        "instanceTenantId": "string",
        "instanceUuid": "string",
        "interfaceCount": "string",
        "inventoryStatusDetail": "string",
        "lastUpdateTime": 0,
        "lastUpdated": "string",
        "lineCardCount": "string",
        "lineCardId": "string",
        "location": "string",
        "locationName": "string",
        "macAddress": "string",
        "managementIpAddress": "string",
        "memorySize": "string",
        "platformId": "string",
        "reachabilityFailureReason": "string",
        "reachabilityStatus": "string",
        "role": "string",
        "roleSource": "string",
        "serialNumber": "string",
        "series": "string",
        "snmpContact": "string",
        "snmpLocation": "string",
        "softwareType": "string",
        "softwareVersion": "string",
        "tagCount": "string",
        "tunnelUdpPort": "string",
        "type": "string",
        "upTime": "string",
        "waasDeviceMode": "string",
        "uptimeSeconds": 0
      },
      "version": "string"
    }
"""

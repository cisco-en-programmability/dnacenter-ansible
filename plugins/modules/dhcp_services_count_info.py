#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: dhcp_services_count_info
short_description: Information module for Dhcp Services Count Info
description:
- This module represents an alias of the module dhcp_services_count_v1_info
version_added: '6.17.0'
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
      be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  endTime:
    description:
    - >
      EndTime query parameter. End time to which API queries the data set related to the resource. It must be
      specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  serverIp:
    description:
    - >
      ServerIp query parameter. IP Address of the DHCP Server. This parameter supports wildcard (`*`) character
      -based search. Example `10.76.81.*` or `*56.78*` or `*50.28` Examples serverIp=10.42.3.31 (single IP Address
      is requested) serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple IP Addresses are requested).
    type: str
  deviceId:
    description:
    - >
      DeviceId query parameter. The device UUID. Examples `deviceId=6bef213c-19ca-4170-8375-b694e251101c` (single
      deviceId is requested)
      `deviceId=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9 (multiple
      networkDeviceIds with & separator).
    type: str
  deviceName:
    description:
    - >
      DeviceName query parameter. Name of the device. This parameter supports wildcard (`*`) character -based
      search. Example `wnbu-sjc*` or `*wnbu-sjc*` or `*wnbu-sjc` Examples deviceName=wnbu-sjc24.cisco.com (single
      device name is requested) deviceName=wnbu-sjc24.cisco.com&deviceName=wnbu-sjc22.cisco.com (multiple device
      names are requested).
    type: str
  deviceSiteHierarchy:
    description:
    - >
      DeviceSiteHierarchy query parameter. The full hierarchical breakdown of the site tree starting from Global
      site name and ending with the specific site name. The Root site is named "Global" (Ex.
      `Global/AreaName/BuildingName/FloorName`) This field supports wildcard asterisk (`*`) character search
      support. E.g. `*/San*, */San, /San*` Examples `?siteHierarchy=Global/AreaName/BuildingName/FloorName`
      (single siteHierarchy requested) `?deviceSiteHierarchy=Global/AreaName/BuildingName/FloorName&deviceSiteHier
      archy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested).
    type: str
  deviceSiteHierarchyId:
    description:
    - >
      DeviceSiteHierarchyId query parameter. The full hierarchy breakdown of the site tree in id form starting
      from Global site UUID and ending with the specific site UUID. (Ex.
      `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk (`*`) character search
      support. E.g. `*uuid*, *uuid, uuid*` Examples
      `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId requested) `?dev
      iceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/bui
      ldingUuid2/floorUuid2` (multiple siteHierarchyIds requested).
    type: str
  deviceSiteId:
    description:
    - >
      DeviceSiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples `?deviceSiteIds=id1` (single
      id requested) `?deviceSiteIds=id1&deviceSiteIds=id2&siteId=id3` (multiple ids requested).
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices RetrievesTheTotalNumberOfDHCPServicesForGivenParametersV1
  description: Complete reference of the RetrievesTheTotalNumberOfDHCPServicesForGivenParametersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-dhcp-services-for-given-parameters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1,

  - Paths used are
    get /dna/data/api/v1/dhcpServices/count,
  - It should be noted that this module is an alias of dhcp_services_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Dhcp Services Count Info
  cisco.dnac.dhcp_services_count_info:
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
    serverIp: string
    deviceId: string
    deviceName: string
    deviceSiteHierarchy: string
    deviceSiteHierarchyId: string
    deviceSiteId: string
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
        "count": 0
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_health_summaries_info
short_description: Information module for Site Health Summaries Info
description:
  - This module represents an alias of the module site_health_summaries_v1_info
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
        StartTime query parameter. Start time from which API queries the data set
        related to the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive. If `startTime`
        is not provided, API will
        default to current time.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related
        to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: float
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned
        by the API. It's one based
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
        SiteHierarchy query parameter. The full hierarchical breakdown of the site
        tree starting from Global site
        name and ending with the specific site name. The Root site is named "Global"
        (Ex.
        `Global/AreaName/BuildingName/FloorName`) This field supports wildcard asterisk
        (`*`) character search
        support. E.g. `*/San*, */San, /San*` Examples `?siteHierarchy=Global/AreaName/BuildingName/FloorName`
        (single siteHierarchy requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global
        /AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested).
    type: str
  siteHierarchyId:
    description:
      - >
        SiteHierarchyId query parameter. The full hierarchy breakdown of the site
        tree in id form starting from
        Global site UUID and ending with the specific site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`)
        This field supports wildcard asterisk (`*`) character search support. E.g.
        `*uuid*, *uuid, uuid*` Examples
        `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
        requested) `?siteHiera
        rchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUu
        id2` (multiple siteHierarchyIds requested).
    type: str
  siteType:
    description:
      - >
        SiteType query parameter. The type of the site. A site can be an area, building,
        or floor. Default when not
        provided will be `floor,building,area` Examples `?siteType=area` (single siteType
        requested)
        `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested).
    type: str
  id:
    description:
      - >
        Id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
        Examples
        id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-4170-8375-
        b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-8aa2-79b233318ba0
        (multiple
        entity uuid with '&' separator).
    type: str
  view:
    description:
      - >
        View query parameter. The specific summary view being requested. This is an
        optional parameter which can be
        passed to get one or more of the specific health data summaries associated
        with sites. ### Response data
        proviced by each view 1. **site** id, siteHierarchy, siteHierarchyId, siteType,
        latitude, longitude 2.
        **network** id, networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
        wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
        coreDeviceCount,
        coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
        routerDeviceCount,
        routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount,
        wlcDeviceGoodHealthCount, switchDeviceCount, switchDeviceGoodHealthCount,
        networkDeviceGoodHealthPercentage,
        accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage, distributionDeviceGoodHealthPercentage,
        routerDeviceGoodHealthPercentage, apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
        switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage 3. **client**
        id, clientCount,
        clientGoodHealthCount, wiredClientCount, wirelessClientCount, wiredClientGoodHealthCount,
        wirelessClientGoodHealthCount, clientGoodHealthPercentage, wiredClientGoodHealthPercentage,
        wirelessClientGoodHealthPercentage, clientDataUsage 4. **issue** id, p1IssueCount,
        p2IssueCount,
        p3IssueCount, p4IssueCount, issueCount When this query parameter is not added
        the default summaries are
        **site,client,network,issue** Examples view=client (single view requested)
        view=client&view=network&view=issue (multiple views requested).
    type: str
  attribute:
    description:
      - >
        Attribute query parameter. Supported Attributes id, siteHierarchy, siteHierarchyId,
        siteType, latitude,
        longitude, networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
        wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
        coreDeviceCount,
        coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
        routerDeviceCount,
        routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount,
        wlcDeviceGoodHealthCount, switchDeviceCount, switchDeviceGoodHealthCount,
        networkDeviceGoodHealthPercentage,
        accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage, distributionDeviceGoodHealthPercentage,
        routerDeviceGoodHealthPercentage, apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
        switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage, clientCount,
        clientGoodHealthCount,
        wiredClientCount, wirelessClientCount, wiredClientGoodHealthCount, wirelessClientGoodHealthCount,
        clientGoodHealthPercentage, wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage,
        clientDataUsage, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount
        If length of attribute
        list is too long, please use 'view' param instead. Examples attribute=siteHierarchy
        (single attribute
        requested) attribute=siteHierarchy&attribute=clientCount (multiple attributes
        requested).
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ReadListOfSiteHealthSummariesV1
    description: Complete reference of the ReadListOfSiteHealthSummariesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!read-list-of-site-health-summaries
  - name: Cisco DNA Center documentation for Sites ReadSiteHealthSummaryDataBySiteIdV1
    description: Complete reference of the ReadSiteHealthSummaryDataBySiteIdV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!read-site-health-summary-data-by-site-id
notes:
  - SDK Method used are sites.Sites.read_list_of_site_health_summaries_v1, sites.Sites.read_site_health_summary_data_by_site_id_v1,
  - Paths used are get /dna/data/api/v1/siteHealthSummaries, get /dna/data/api/v1/siteHealthSummaries/{id},
  - It should be noted that this module is an alias of site_health_summaries_v1_info
"""
EXAMPLES = r"""
- name: Get all Site Health Summaries Info
  cisco.dnac.site_health_summaries_info:
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
    siteType: string
    id: string
    view: string
    attribute: string
  register: result
- name: Get Site Health Summaries Info by id
  cisco.dnac.site_health_summaries_info:
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
        "siteHierarchy": "string",
        "siteHierarchyId": "string",
        "siteType": "string",
        "latitude": 0,
        "longitude": 0,
        "networkDeviceGoodHealthPercentage": 0,
        "networkDeviceGoodHealthCount": 0,
        "clientGoodHealthCount": 0,
        "clientGoodHealthPercentage": 0,
        "wiredClientGoodHealthPercentage": 0,
        "wirelessClientGoodHealthPercentage": 0,
        "clientCount": 0,
        "wiredClientCount": 0,
        "wirelessClientCount": 0,
        "wiredClientGoodHealthCount": 0,
        "wirelessClientGoodHealthCount": 0,
        "networkDeviceCount": 0,
        "accessDeviceCount": 0,
        "accessDeviceGoodHealthCount": 0,
        "coreDeviceCount": 0,
        "coreDeviceGoodHealthCount": 0,
        "distributionDeviceCount": 0,
        "distributionDeviceGoodHealthCount": 0,
        "routerDeviceCount": 0,
        "routerDeviceGoodHealthCount": 0,
        "wirelessDeviceCount": 0,
        "wirelessDeviceGoodHealthCount": 0,
        "apDeviceCount": 0,
        "apDeviceGoodHealthCount": 0,
        "wlcDeviceCount": 0,
        "wlcDeviceGoodHealthCount": 0,
        "switchDeviceCount": 0,
        "switchDeviceGoodHealthCount": 0,
        "accessDeviceGoodHealthPercentage": 0,
        "coreDeviceGoodHealthPercentage": 0,
        "distributionDeviceGoodHealthPercentage": 0,
        "routerDeviceGoodHealthPercentage": 0,
        "apDeviceGoodHealthPercentage": 0,
        "wlcDeviceGoodHealthPercentage": 0,
        "switchDeviceGoodHealthPercentage": 0,
        "wirelessDeviceGoodHealthPercentage": 0,
        "clientDataUsage": 0,
        "p1IssueCount": 0,
        "p2IssueCount": 0,
        "p3IssueCount": 0,
        "p4IssueCount": 0,
        "issueCount": 0
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_health_summaries_count_info
short_description: Information module for Site Health Summaries Count Info
description:
  - This module represents an alias of the module site_health_summaries_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related
        to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
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
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ReadSiteCountV1
    description: Complete reference of the ReadSiteCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!read-site-count
notes:
  - SDK Method used are sites.Sites.read_site_count_v1,
  - Paths used are get /dna/data/api/v1/siteHealthSummaries/count,
  - It should be noted that this module is an alias of site_health_summaries_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Site Health Summaries Count Info
  cisco.dnac.site_health_summaries_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    endTime: 0
    siteHierarchy: string
    siteHierarchyId: string
    siteType: string
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
        "count": 0
      },
      "version": "string"
    }
"""

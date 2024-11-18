#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: site_health_summaries_summary_analytics
short_description: Resource module for Site Health Summaries Summary Analytics
description:
- This module represents an alias of the module site_health_summaries_summary_analytics_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  attributes:
    description: Attributes.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  id:
    description: Id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
      Examples id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested)
      id=6bef213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-8aa2-79...
      (multiple entity uuid with '&' separator).
    type: str
  siteHierarchy:
    description: SiteHierarchy query parameter. The full hierarchical breakdown of the
      site tree starting from Global site name and ending with the specific site name.
      The Root site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`)
      This field supports wildcard asterisk (`*`) character search support. E.g. `*/San*,
      */San, /San*` Examples `?siteHierarchy=Global/AreaName/BuildingName/FloorName`
      (single siteHierarchy requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/...
      (multiple siteHierarchies requested).
    type: str
  siteHierarchyId:
    description: SiteHierarchyId query parameter. The full hierarchy breakdown of the
      site tree in id form starting from Global site UUID and ending with the specific
      site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports
      wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*`
      Examples `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
      siteHierarchyId requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globa...
      (multiple siteHierarchyIds requested).
    type: str
  siteType:
    description: SiteType query parameter. The type of the site. A site can be an area,
      building, or floor. Default when not provided will be `floor,building,area` Examples
      `?siteType=area` (single siteType requested) `?siteType=area&siteType=building&siteType=floor`
      (multiple siteTypes requested).
    type: str
  startTime:
    description: Start Time.
    type: int
  views:
    description: Views.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites QueryAnAggregatedSummaryOfSiteHealthDataV1
  description: Complete reference of the QueryAnAggregatedSummaryOfSiteHealthDataV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!query-an-aggregated-summary-of-site-health-data-v-1
notes:
  - SDK Method used are
    sites.Sites.query_an_aggregated_summary_of_site_health_data_v1,

  - Paths used are
    post /dna/data/api/v1/siteHealthSummaries/summaryAnalytics,
  - It should be noted that this module is an alias of site_health_summaries_summary_analytics_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.site_health_summaries_summary_analytics:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    attributes:
    - string
    endTime: 0
    id: string
    siteHierarchy: string
    siteHierarchyId: string
    siteType: string
    startTime: 0
    views:
    - string

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of site_health_summaries_summary_analytics_v1.
"""

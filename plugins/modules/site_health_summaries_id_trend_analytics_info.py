#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_health_summaries_id_trend_analytics_info
short_description: Information module for Site Health Summaries Id Trend Analytics
  Info
description:
  - This module represents an alias of the module site_health_summaries_id_trend_analytics_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Unique site uuid.
    type: str
  startTime:
    description:
      - >
        StartTime query parameter. Start time from which API queries the data set
        related to the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related
        to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  trendInterval:
    description:
      - >
        TrendInterval query parameter. The time window to aggregate the metrics. Interval
        can be 5 minutes or 10
        minutes or 1 hour or 1 day or 7 days.
    type: str
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
  timeSortOrder:
    description:
      - TimeSortOrder query parameter. The sort order of a time sorted API response.
    type: str
  attribute:
    description:
      - >
        Attribute query parameter. Supported Analytics Attributes networkDeviceCount,
        networkDeviceGoodHealthCount,wirelessDeviceCount, wirelessDeviceGoodHealthCount,
        accessDeviceCount,
        accessDeviceGoodHealthCount, coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
        distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
        apDeviceCount,
        apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount, switchDeviceCount,
        switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage, accessDeviceGoodHealthPercentage,
        coreDeviceGoodHealthPercentage, distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
        apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage, switchDeviceGoodHealthPercentage,
        wirelessDeviceGoodHealthPercentage, clientCount, clientGoodHealthCount, wiredClientCount,
        wirelessClientCount, wiredClientGoodHealthCount, wirelessClientGoodHealthCount,
        clientGoodHealthPercentage,
        wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage,
        p1IssueCount,
        p2IssueCount, p3IssueCount, p4IssueCount, issueCount attribute=networkDeviceCount
        (single attribute
        requested) attribute=networkDeviceCount&attribute=clientCount (multiple attributes
        requested).
    type: str
  taskId:
    description:
      - >
        TaskId query parameter. Used to retrieve asynchronously processed & stored
        data. When this parameter is
        used, the rest of the request params will be ignored.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ReadTrendAnalyticsDataForASpecificSiteInYourNetworkV1
    description: Complete reference of the ReadTrendAnalyticsDataForASpecificSiteInYourNetworkV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!read-trend-analytics-data-for-a-specific-site-in-your-network
notes:
  - SDK Method used are sites.Sites.read_trend_analytics_data_for_a_specific_site_in_your_network_v1,
  - Paths used are get /dna/data/api/v1/siteHealthSummaries/{id}/trendAnalytics,
  - It should be noted that this module is an alias of site_health_summaries_id_trend_analytics_v1_info
"""
EXAMPLES = r"""
- name: Get all Site Health Summaries Id Trend Analytics Info
  cisco.dnac.site_health_summaries_id_trend_analytics_info:
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
    trendInterval: string
    limit: 0
    offset: 0
    timeSortOrder: string
    attribute: string
    taskId: string
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
      "response": [
        {
          "timestamp": 0,
          "attributes": [
            {
              "name": "string",
              "value": 0
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "timeSortOrder": "string"
      },
      "version": "string"
    }
"""

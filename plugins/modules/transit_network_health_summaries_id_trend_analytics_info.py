#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: transit_network_health_summaries_id_trend_analytics_info
short_description: Information module for Transit Network Health Summaries Id Trend
  Analytics Info
description:
  - This module represents an alias of the module transit_network_health_summaries_id_trend_analytics_v1_info
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
      - Id path parameter. The unique transit network id, Ex "1551156a-bc97-3c63-aeda-8a6d3765b5b9".
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
  order:
    description:
      - Order query parameter. The sort order of the field ascending or descending.
    type: str
  attribute:
    description:
      - Attribute query parameter. The interested fields in the request. For valid
        attributes, verify the documentation.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA TheTrendAnalyticsDataForATransitNetworkInTheSpecifiedTimeRangeV1
    description: Complete reference of the TheTrendAnalyticsDataForATransitNetworkInTheSpecifiedTimeRangeV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-a-transit-network-in-the-specified-time-range
notes:
  - SDK Method used are
    sda.Sda.the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1,
  - Paths used are get /dna/data/api/v1/transitNetworkHealthSummaries/{id}/trendAnalytics,
  - It should be noted that this module is an alias of transit_network_health_summaries_id_trend_analytics_v1_info
"""
EXAMPLES = r"""
- name: Get all Transit Network Health Summaries Id Trend Analytics Info
  cisco.dnac.transit_network_health_summaries_id_trend_analytics_info:
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
    order: string
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
        "timeSortOrder": "string"
      },
      "version": 0
    }
"""

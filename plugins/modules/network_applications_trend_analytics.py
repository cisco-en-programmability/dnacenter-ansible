#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_applications_trend_analytics
short_description: Resource module for Network Applications Trend Analytics
description:
  - This module represents an alias of the module network_applications_trend_analytics_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Network Applications Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Function.
        type: str
      name:
        description: Name.
        type: str
    type: list
  attributes:
    description: Attributes.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  filters:
    description: Network Applications Trend Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Key.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: int
    type: list
  groupBy:
    description: Group By.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Network Applications Trend Analytics's page.
    suboptions:
      cursor:
        description: Cursor.
        type: str
      limit:
        description: Limit.
        type: int
      timeSortOrder:
        description: Time Sort Order.
        type: str
    type: dict
  siteIds:
    description: Site Ids.
    elements: str
    type: list
  startTime:
    description: Start Time.
    type: int
  trendInterval:
    description: Trend Interval.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Applications RetrievesTheTrendAnalyticsDataRelatedToNetworkApplicationsV1
    description: Complete reference of the RetrievesTheTrendAnalyticsDataRelatedToNetworkApplicationsV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-data-related-to-network-applications
notes:
  - SDK Method used are
    applications.Applications.retrieves_the_trend_analytics_data_related_to_network_applications_v1,
  - Paths used are post /dna/data/api/v1/networkApplications/trendAnalytics,
  - It should be noted that this module is an alias of network_applications_trend_analytics_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.network_applications_trend_analytics:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    aggregateAttributes:
      - function: string
        name: string
    attributes:
      - string
    endTime: 0
    filters:
      - key: string
        operator: string
        value: 0
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    page:
      cursor: string
      limit: 0
      timeSortOrder: string
    siteIds:
      - string
    startTime: 0
    trendInterval: string
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
              "value": "string"
            }
          ],
          "aggregateAttributes": [
            {
              "name": "string",
              "function": "string",
              "value": "string"
            }
          ],
          "groups": [
            {
              "id": "string",
              "attributes": [
                {
                  "name": "string",
                  "value": "string"
                }
              ],
              "aggregateAttributes": [
                {
                  "name": "string",
                  "function": "string",
                  "value": "string"
                }
              ]
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "cursor": "string",
        "count": 0,
        "timeSortOrder": "string"
      },
      "version": "string"
    }
"""

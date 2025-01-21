#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_devices_trend_analytics
short_description: Resource module for Network Devices Trend Analytics
description:
- This module represents an alias of the module network_devices_trend_analytics_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Aggregate Attributes.
    elements: dict
    type: list
  attributes:
    description: Attributes.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  filters:
    description: Network Devices Trend Analytics's filters.
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
        type: str
    type: list
  groupBy:
    description: Group By.
    elements: dict
    type: list
  page:
    description: Network Devices Trend Analytics's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      timestampOrder:
        description: Timestamp Order.
        type: str
    type: dict
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
- name: Cisco DNA Center documentation for Devices GetsTheTrendAnalyticsDataV1
  description: Complete reference of the GetsTheTrendAnalyticsDataV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-the-trend-analytics-data
notes:
  - SDK Method used are
    devices.Devices.gets_the_trend_analytics_data_v1,

  - Paths used are
    post /dna/data/api/v1/networkDevices/trendAnalytics,
  - It should be noted that this module is an alias of network_devices_trend_analytics_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.network_devices_trend_analytics:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    aggregateAttributes:
    - {}
    attributes:
    - string
    endTime: 0
    filters:
    - key: string
      operator: string
      value: string
    groupBy:
    - {}
    page:
      limit: 0
      offset: 0
      timestampOrder: string
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
              "value": 0
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
                  "value": 0
                }
              ]
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "timestampOrder": "string"
      },
      "version": "string"
    }
"""

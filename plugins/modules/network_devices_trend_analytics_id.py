#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_devices_trend_analytics_id
short_description: Resource module for Network Devices Trend Analytics Id
description:
- This module represents an alias of the module network_devices_trend_analytics_id_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Network Devices Trend Analytics Id's aggregateAttributes.
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
    description: Network Devices Trend Analytics Id's filters.
    elements: dict
    suboptions:
      filters:
        description: Filters.
        elements: str
        type: list
      key:
        description: Key.
        type: str
      logicalOperator:
        description: Logical Operator.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: dict
    type: list
  groupBy:
    description: Group By.
    elements: str
    type: list
  id:
    description: Id path parameter. The device Uuid.
    type: str
  page:
    description: Network Devices Trend Analytics Id's page.
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
  trendIntervalInMinutes:
    description: Trend Interval In Minutes.
    type: int
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices TheTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRangeV1   # noqa: E501
  description: Complete reference of the TheTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRangeV1 API.  # noqa: E501
  link: https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-the-network-device-in-the-specified-time-range  # noqa: E501
notes:
  - SDK Method used are
    devices.Devices.the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1,

  - Paths used are
    post /dna/data/api/v1/networkDevices/{id}/trendAnalytics,
  - It should be noted that this module is an alias of network_devices_trend_analytics_id_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.network_devices_trend_analytics_id:
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
    - filters:
      - string
      key: string
      logicalOperator: string
      operator: string
      value: {}
    groupBy:
    - string
    id: string
    page:
      limit: 0
      offset: 0
      timestampOrder: string
    startTime: 0
    trendIntervalInMinutes: 0

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

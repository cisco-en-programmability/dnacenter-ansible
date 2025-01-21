#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_devices_summary_analytics
short_description: Resource module for Network Devices Summary Analytics
description:
- This module represents an alias of the module network_devices_summary_analytics_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Network Devices Summary Analytics's aggregateAttributes.
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
    description: Network Devices Summary Analytics's filters.
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
    elements: str
    type: list
  page:
    description: Network Devices Summary Analytics's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      sortBy:
        description: Network Devices Summary Analytics's sortBy.
        elements: dict
        suboptions:
          name:
            description: Name.
            type: str
          order:
            description: Order.
            type: str
        type: list
    type: dict
  startTime:
    description: Start Time.
    type: int
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetsTheSummaryAnalyticsDataRelatedToNetworkDevicesV1
  description: Complete reference of the GetsTheSummaryAnalyticsDataRelatedToNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-the-summary-analytics-data-related-to-network-devices
notes:
  - SDK Method used are
    devices.Devices.gets_the_summary_analytics_data_related_to_network_devices_v1,

  - Paths used are
    post /dna/data/api/v1/networkDevices/summaryAnalytics,
  - It should be noted that this module is an alias of network_devices_summary_analytics_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.network_devices_summary_analytics:
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
      value: string
    groupBy:
    - string
    page:
      limit: 0
      offset: 0
      sortBy:
      - name: string
        order: string
    startTime: 0

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "attributes": [
          {}
        ],
        "aggregateAttributes": [
          {}
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
      },
      "page": [
        {
          "limit": 0,
          "offset": 0,
          "count": 0,
          "sortBy": [
            {
              "name": "string",
              "order": "string"
            }
          ]
        }
      ]
    }
"""

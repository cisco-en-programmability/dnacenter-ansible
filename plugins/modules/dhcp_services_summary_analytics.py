#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: dhcp_services_summary_analytics
short_description: Resource module for Dhcp Services Summary Analytics
description:
- This module represents an alias of the module dhcp_services_summary_analytics_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Dhcp Services Summary Analytics's aggregateAttributes.
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
    description: Dhcp Services Summary Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Dhcp Services Summary Analytics's filters.
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
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Dhcp Services Summary Analytics's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      sortBy:
        description: Dhcp Services Summary Analytics's sortBy.
        elements: dict
        suboptions:
          function:
            description: Function.
            type: str
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
- name: Cisco DNA Center documentation for Devices GetSummaryAnalyticsDataOfDHCPServicesForGivenSetOfComplexFiltersV1
  description: Complete reference of the GetSummaryAnalyticsDataOfDHCPServicesForGivenSetOfComplexFiltersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-summary-analytics-data-of-dhcp-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1,

  - Paths used are
    post /dna/data/api/v1/dhcpServices/summaryAnalytics,
  - It should be noted that this module is an alias of dhcp_services_summary_analytics_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.dhcp_services_summary_analytics:
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
      - filters:
        - string
        key: string
        logicalOperator: string
        operator: string
        value: {}
      key: string
      logicalOperator: string
      operator: string
      value: {}
    groupBy:
    - string
    headers: '{{my_headers | from_json}}'
    page:
      limit: 0
      offset: 0
      sortBy:
      - function: string
        name: string
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
      "version": "string",
      "response": {
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
        ],
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
      },
      "page": {
        "limit": 0,
        "offset": 0,
        "count": "string",
        "sortBy": [
          {
            "name": "string",
            "function": "string",
            "order": "string"
          }
        ]
      }
    }
"""

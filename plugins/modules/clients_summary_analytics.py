#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: clients_summary_analytics
short_description: Resource module for Clients Summary Analytics
description:
- This module represents an alias of the module clients_summary_analytics_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Clients Summary Analytics's aggregateAttributes.
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
    description: Clients Summary Analytics's filters.
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
    description: Clients Summary Analytics's page.
    suboptions:
      cursor:
        description: Cursor.
        type: str
      limit:
        description: Limit.
        type: int
      sortBy:
        description: Clients Summary Analytics's sortBy.
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
- name: Cisco DNA Center documentation for Clients RetrievesSummaryAnalyticsDataRelatedToClientsV1
  description: Complete reference of the RetrievesSummaryAnalyticsDataRelatedToClientsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-summary-analytics-data-related-to-clients
notes:
  - SDK Method used are
    clients.Clients.retrieves_summary_analytics_data_related_to_clients_v1,

  - Paths used are
    post /dna/data/api/v1/clients/summaryAnalytics,
  - It should be noted that this module is an alias of clients_summary_analytics_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.clients_summary_analytics:
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
        "groups": [
          {
            "id": "string",
            "attributes": [
              {
                "name": "string",
                "value": 0
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
      "page": {
        "limit": 0,
        "cursor": "string",
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string"
          }
        ]
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: endpoint_analytics_profiling_rules_info
short_description: Information module for Endpoint Analytics Profiling Rules Info
description:
  - This module represents an alias of the module endpoint_analytics_profiling_rules_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  ruleType:
    description:
      - RuleType query parameter. Use comma-separated list of rule types to filter
        the data. Defaults to 'Custom Rule'.
    type: str
  includeDeleted:
    description:
      - IncludeDeleted query parameter. Flag to indicate whether deleted rules should
        be part of the records fetched.
    type: bool
  limit:
    description:
      - >
        Limit query parameter. Maximum number of records to be fetched. If not provided,
        500 records will be fetched
        by default. To fetch all the records in the system, provide a large value
        for this parameter.
    type: float
  offset:
    description:
      - Offset query parameter. Record offset to start data fetch at. Offset starts
        at zero.
    type: float
  sortBy:
    description:
      - >
        SortBy query parameter. Name of the column to sort the results on. Please
        note that fetch might take more
        time if sorting is requested.
    type: str
  order:
    description:
      - Order query parameter. Order to be used for sorting.
    type: str
  ruleId:
    description:
      - RuleId path parameter. Unique rule identifier.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
notes:
  - SDK Method used are
    a_i_endpoint_analytics.AIEndpointAnalytics.get_details_of_a_single_profiling_rule_v1,
    a_i_endpoint_analytics.AIEndpointAnalytics.get_list_of_profiling_rules_v1,
  - Paths used are get /dna/intent/api/v1/endpoint-analytics/profiling-rules, get
    /dna/intent/api/v1/endpoint-analytics/profiling-rules/{ruleId},
  - It should be noted that this module is an alias of endpoint_analytics_profiling_rules_v1_info
"""
EXAMPLES = r"""
- name: Get all Endpoint Analytics Profiling Rules Info
  cisco.dnac.endpoint_analytics_profiling_rules_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    ruleType: string
    includeDeleted: true
    limit: 0
    offset: 0
    sortBy: string
    order: string
  register: result
- name: Get Endpoint Analytics Profiling Rules Info by id
  cisco.dnac.endpoint_analytics_profiling_rules_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    ruleId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "ruleId": "string",
      "ruleName": "string",
      "ruleType": "string",
      "ruleVersion": 0,
      "rulePriority": 0,
      "sourcePriority": 0,
      "isDeleted": true,
      "lastModifiedBy": "string",
      "lastModifiedOn": 0,
      "pluginId": "string",
      "clusterId": "string",
      "rejected": true,
      "result": {
        "deviceType": [
          "string"
        ],
        "hardwareManufacturer": [
          "string"
        ],
        "hardwareModel": [
          "string"
        ],
        "operatingSystem": [
          "string"
        ]
      },
      "conditionGroups": {
        "type": "string",
        "condition": {
          "attribute": "string",
          "operator": "string",
          "value": "string",
          "attributeDictionary": "string"
        },
        "operator": "string",
        "conditionGroup": [
          {}
        ]
      },
      "usedAttributes": [
        "string"
      ]
    }
"""

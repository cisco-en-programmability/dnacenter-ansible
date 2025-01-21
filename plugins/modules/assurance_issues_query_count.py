#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: assurance_issues_query_count
short_description: Resource module for Assurance Issues Query Count
description:
- This module represents an alias of the module assurance_issues_query_count_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  filters:
    description: Assurance Issues Query Count's filters.
    elements: dict
    suboptions:
      filters:
        description: Assurance Issues Query Count's filters.
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
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Start Time.
    type: int
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Issues GetTheTotalNumberOfIssuesForGivenSetOfFiltersV1
  description: Complete reference of the GetTheTotalNumberOfIssuesForGivenSetOfFiltersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-the-total-number-of-issues-for-given-set-of-filters
notes:
  - SDK Method used are
    issues.Issues.get_the_total_number_of_issues_for_given_set_of_filters_v1,

  - Paths used are
    post /dna/data/api/v1/assuranceIssues/query/count,
  - It should be noted that this module is an alias of assurance_issues_query_count_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.assurance_issues_query_count:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    endTime: 0
    filters:
    - filters:
      - key: string
        operator: string
        value: string
      key: string
      logicalOperator: string
      operator: string
      value: string
    headers: '{{my_headers | from_json}}'
    startTime: 0

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "filters": [
        {
          "key": "string",
          "value": "string",
          "operator": "string"
        }
      ]
    }
"""

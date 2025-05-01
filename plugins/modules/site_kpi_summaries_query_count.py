#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_kpi_summaries_query_count
short_description: Resource module for Site Kpi Summaries Query Count
description:
  - This module represents an alias of the module site_kpi_summaries_query_count_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  filters:
    description: Site Kpi Summaries Query Count's filters.
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
  - name: Cisco DNA Center documentation for Sites GetTheTotalNumberOfSiteAnalyticsRecordsAvailableForForGivenSetOfFiltersV1
    description: Complete reference of the GetTheTotalNumberOfSiteAnalyticsRecordsAvailableForForGivenSetOfFiltersV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-the-total-number-of-site-analytics-records-available-for-for-given-set-of-filters
notes:
  - SDK Method used are
    sites.Sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1,
  - Paths used are post /dna/data/api/v1/siteKpiSummaries/query/count,
  - It should be noted that this module is an alias of site_kpi_summaries_query_count_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.site_kpi_summaries_query_count:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    endTime: 0
    filters:
      - key: string
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
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""

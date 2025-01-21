#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: site_kpi_summaries_trend_analytics
short_description: Resource module for Site Kpi Summaries Trend Analytics
description:
- This module represents an alias of the module site_kpi_summaries_trend_analytics_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  attributes:
    description: Attributes.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  filters:
    description: Site Kpi Summaries Trend Analytics's filters.
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
  page:
    description: Site Kpi Summaries Trend Analytics's page.
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
- name: Cisco DNA Center documentation for Sites SubmitRequestForSiteAnalyticsTrendDataV1
  description: Complete reference of the SubmitRequestForSiteAnalyticsTrendDataV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!submit-request-for-site-analytics-trend-data
notes:
  - SDK Method used are
    sites.Sites.submit_request_for_site_analytics_trend_data_v1,

  - Paths used are
    post /dna/data/api/v1/siteKpiSummaries/trendAnalytics,
  - It should be noted that this module is an alias of site_kpi_summaries_trend_analytics_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.site_kpi_summaries_trend_analytics:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    attributes:
    - string
    endTime: 0
    filters:
    - key: string
      operator: string
      value: string
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
      "response": {
        "taskLocation": "string",
        "taskId": "string"
      },
      "version": "string"
    }
"""

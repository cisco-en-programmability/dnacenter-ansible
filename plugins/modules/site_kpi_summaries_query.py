#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: site_kpi_summaries_query
short_description: Resource module for Site Kpi Summaries Query
description:
- This module represents an alias of the module site_kpi_summaries_query_v1
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
    description: Site Kpi Summaries Query's filters.
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
  page:
    description: Site Kpi Summaries Query's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      sortBy:
        description: Site Kpi Summaries Query's sortBy.
        suboptions:
          name:
            description: Name.
            type: str
          order:
            description: Order.
            type: str
        type: dict
    type: dict
  startTime:
    description: Start Time.
    type: int
  views:
    description: Views.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites GetSiteAnalyticsForTheChildSitesOfGivenParentSiteAndOtherFiltersV1
  description: Complete reference of the GetSiteAnalyticsForTheChildSitesOfGivenParentSiteAndOtherFiltersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-analytics-for-the-child-sites-of-given-parent-site-and-other-filters
notes:
  - SDK Method used are
    sites.Sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1,

  - Paths used are
    post /dna/data/api/v1/siteKpiSummaries/query,
  - It should be noted that this module is an alias of site_kpi_summaries_query_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.site_kpi_summaries_query:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    attributes:
    - string
    endTime: 0
    filters:
    - key: string
      operator: string
      value: string
    headers: '{{my_headers | from_json}}'
    page:
      limit: 0
      offset: 0
      sortBy:
        name: string
        order: string
    startTime: 0
    views:
    - string

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

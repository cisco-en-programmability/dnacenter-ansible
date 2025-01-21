#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: site_kpi_summaries_top_n_analytics_info
short_description: Information module for Site Kpi Summaries Top N Analytics Info
description:
- This module represents an alias of the module site_kpi_summaries_top_n_analytics_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
    - >
      TaskId query parameter. Used to retrieve asynchronously processed & stored data. When this parameter is
      used, the rest of the request params will be ignored.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites GetTopNEntitiesRelatedToSiteAnalyticsForTheGivenTaskIdV1
  description: Complete reference of the GetTopNEntitiesRelatedToSiteAnalyticsForTheGivenTaskIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-top-n-entities-related-to-site-analytics-for-the-given-task-id
notes:
  - SDK Method used are
    sites.Sites.get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1,

  - Paths used are
    get /dna/data/api/v1/siteKpiSummaries/topNAnalytics,
  - It should be noted that this module is an alias of site_kpi_summaries_top_n_analytics_v1_info

"""

EXAMPLES = r"""
- name: Get all Site Kpi Summaries Top N Analytics Info
  cisco.dnac.site_kpi_summaries_top_n_analytics_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": [
        {
          "id": "string",
          "attributes": [
            {
              "name": "string",
              "value": 0
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0
      }
    }
"""

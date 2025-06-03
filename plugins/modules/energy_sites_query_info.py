#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: energy_sites_query_info
short_description: Information module for Energy Sites Query Info
description:
  - This module represents an alias of the module energy_sites_query_v1_info
version_added: '6.18.0'
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
        TaskId query parameter. Used to retrieve asynchronously processed & stored
        data. When this parameter is
        used, the rest of the request params will be ignored.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites QuerySitesEnergyForTheGivenTaskIDV1
    description: Complete reference of the QuerySitesEnergyForTheGivenTaskIDV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!query-sites-energy-for-the-given-task-id
notes:
  - SDK Method used are sites.Sites.query_sites_energy_for_the_given_task_id_v1,
  - Paths used are get /dna/data/api/v1/energy/sites/query,
  - It should be noted that this module is an alias of energy_sites_query_v1_info
"""
EXAMPLES = r"""
- name: Get all Energy Sites Query Info
  cisco.dnac.energy_sites_query_info:
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
      "response": [
        {
          "id": "string",
          "siteName": "string",
          "siteHierarchy": "string",
          "siteHierarchyId": "string",
          "siteType": "string",
          "latitude": 0,
          "longitude": 0,
          "deviceCategories": [
            "string"
          ],
          "energyConsumed": 0,
          "estimatedCost": 0,
          "estimatedEmission": 0,
          "carbonIntensity": 0,
          "numberOfDevices": 0,
          "aggregateAttributes": [
            {
              "name": "string",
              "function": "string",
              "value": 0
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string",
            "function": "string"
          }
        ]
      },
      "version": "string"
    }
"""

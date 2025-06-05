#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: endpoint_analytics_tasks_info
short_description: Information module for Endpoint Analytics Tasks Info
description:
  - This module represents an alias of the module endpoint_analytics_tasks_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
      - TaskId path parameter. Unique identifier for the task.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for AI Endpoint Analytics GetTaskDetailsV1
    description: Complete reference of the GetTaskDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-task-details
notes:
  - SDK Method used are a_i_endpoint_analytics.AIEndpointAnalytics.get_task_details_v1,
  - Paths used are get /dna/intent/api/v1/endpoint-analytics/tasks/{taskId},
  - It should be noted that this module is an alias of endpoint_analytics_tasks_v1_info
"""
EXAMPLES = r"""
- name: Get Endpoint Analytics Tasks Info by id
  cisco.dnac.endpoint_analytics_tasks_info:
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
      "id": "string",
      "name": "string",
      "status": "string",
      "errors": [
        {
          "index": 0,
          "code": 0,
          "message": "string",
          "details": "string"
        }
      ],
      "additionalInfo": {},
      "createdBy": "string",
      "createdOn": 0,
      "lastUpdatedOn": 0
    }
"""

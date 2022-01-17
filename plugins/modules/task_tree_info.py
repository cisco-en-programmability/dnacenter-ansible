#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: task_tree_info
short_description: Information module for Task Tree
description:
- Get all Task Tree.
- Returns a task with its children tasks by based on their id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
    - TaskId path parameter. UUID of the Task.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_task_tree used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.task.Task.get_task_tree

notes:
  - Paths used: get /dna/intent/api/v1/task/{taskId}/tree
"""

EXAMPLES = r"""
- name: Get all Task Tree
  cisco.dnac.task_tree_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
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
          "additionalStatusURL": "string",
          "data": "string",
          "endTime": "string",
          "errorCode": "string",
          "errorKey": "string",
          "failureReason": "string",
          "id": "string",
          "instanceTenantId": "string",
          "isError": true,
          "lastUpdate": "string",
          "operationIdList": {},
          "parentId": "string",
          "progress": "string",
          "rootId": "string",
          "serviceType": "string",
          "startTime": "string",
          "username": "string",
          "version": 0
        }
      ],
      "version": "string"
    }
"""

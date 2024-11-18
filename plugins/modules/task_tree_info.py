#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: task_tree_info
short_description: Information module for Task Tree Info
description:
- This module represents an alias of the module task_tree_v1_info
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
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Task GetTaskTreeV1
  description: Complete reference of the GetTaskTreeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-task-tree-v-1
notes:
  - SDK Method used are
    task.Task.get_task_tree_v1,

  - Paths used are
    get /dna/intent/api/v1/task/{taskId}/tree,
  - It should be noted that this module is an alias of task_tree_v1_info

"""

EXAMPLES = r"""
- name: Get all Task Tree Info
  cisco.dnac.task_tree_info:
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
  This alias returns the output of task_tree_v1_info.
"""

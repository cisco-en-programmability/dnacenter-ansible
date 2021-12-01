#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_workflow_info
short_description: Information module for Pnp Workflow
description:
- Get all Pnp Workflow.
- Get Pnp Workflow by id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - Limit query parameter. Limits number of results.
    type: int
  offset:
    description:
    - Offset query parameter. Index of first result.
    type: int
  sort:
    description:
    - Sort query parameter. Comma seperated lost of fields to sort on.
    type: list
  sortOrder:
    description:
    - SortOrder query parameter. Sort Order Ascending (asc) or Descending (des).
    type: str
  type:
    description:
    - Type query parameter. Workflow Type.
    type: list
  name:
    description:
    - Name query parameter. Workflow Name.
    type: list
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Pnp Workflow reference
  description: Complete reference of the Pnp Workflow object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Pnp Workflow
  cisco.dnac.pnp_workflow_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    limit: 0
    offset: 0
    sort: []
    sortOrder: string
    type: []
    name: []
  register: result

- name: Get Pnp Workflow by id
  cisco.dnac.pnp_workflow_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    id: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "_id": "string",
      "state": "string",
      "type": "string",
      "description": "string",
      "lastupdateOn": 0,
      "imageId": "string",
      "currTaskIdx": 0,
      "addedOn": 0,
      "tasks": [
        {
          "state": "string",
          "type": "string",
          "currWorkItemIdx": 0,
          "taskSeqNo": 0,
          "endTime": 0,
          "startTime": 0,
          "workItemList": [
            {
              "state": "string",
              "command": "string",
              "outputStr": "string",
              "endTime": 0,
              "startTime": 0,
              "timeTaken": 0
            }
          ],
          "timeTaken": 0,
          "name": "string"
        }
      ],
      "addToInventory": true,
      "instanceType": "string",
      "endTime": 0,
      "execTime": 0,
      "startTime": 0,
      "useState": "string",
      "configId": "string",
      "name": "string",
      "version": 0,
      "tenantId": "string"
    }
"""

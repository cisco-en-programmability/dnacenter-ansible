#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_config_task_info
short_description: Information module for Network Device Config Task Info
description:
- This module represents an alias of the module network_device_config_task_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  parentTaskId:
    description:
    - ParentTaskId query parameter. Task Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Archive GetConfigTaskDetailsV1
  description: Complete reference of the GetConfigTaskDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-config-task-details
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.get_config_task_details_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device-config/task,
  - It should be noted that this module is an alias of network_device_config_task_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Config Task Info
  cisco.dnac.network_device_config_task_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    parentTaskId: string
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
          "startTime": 0,
          "errorCode": "string",
          "deviceId": "string",
          "taskId": "string",
          "taskStatus": "string",
          "parentTaskId": "string",
          "deviceIpAddress": "string",
          "detailMessage": "string",
          "failureMessage": "string",
          "taskType": "string",
          "completionTime": 0,
          "hostName": "string"
        }
      ]
    }
"""

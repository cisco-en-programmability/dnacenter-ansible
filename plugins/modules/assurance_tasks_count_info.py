#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: assurance_tasks_count_info
short_description: Information module for Assurance Tasks Count Info
description:
  - This module represents an alias of the module assurance_tasks_count_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  status:
    description:
      - Status query parameter. Used to get a subset of tasks by their status.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Task RetrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExistV1
    description: Complete reference of the RetrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExistV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-a-count-of-the-number-of-assurance-tasks-that-currently-exist
notes:
  - SDK Method used are
    task.Task.retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist_v1,
  - Paths used are get /dna/data/api/v1/assuranceTasks/count,
  - It should be noted that this module is an alias of assurance_tasks_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Assurance Tasks Count Info
  cisco.dnac.assurance_tasks_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    status: string
  register: result
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

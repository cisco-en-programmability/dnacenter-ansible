#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: software_management_executions_info
short_description: Information module for Software Management Executions
description:
  - Get Software Management Executions by id.
  - This api is used to get execution status and task details of a specific software management workflows.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The id of the execution detail to be retrieved.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade GetSoftwareManagementExecutionDetails
    description: Complete reference of the GetSoftwareManagementExecutionDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!get-software-management-execution-details
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.get_software_management_execution_details,
  - Paths used are
    get /dna/system/api/v1/softwareManagementExecutions/{id},
"""

EXAMPLES = r"""
---
- name: Get Software Management Executions by id
  cisco.dnac.software_management_executions_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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
      "response": {
        "id": "string",
        "completedPercentage": 0,
        "createdBy": "string",
        "duration": 0,
        "endDate": "string",
        "errorCode": "string",
        "errorMessage": "string",
        "isForceUpdate": true,
        "jobType": "string",
        "localReleaseId": "string",
        "optionalPackages": [
          "string"
        ],
        "releaseDisplayName": "string",
        "releaseDisplayVersion": "string",
        "releaseName": "string",
        "releaseVersion": "string",
        "startDate": "string",
        "status": "string",
        "systemErrorMessage": "string",
        "tasks": [
          {
            "id": "string",
            "endDate": "string",
            "errorCode": "string",
            "message": "string",
            "startDate": "string",
            "status": "string",
            "systemErrorMessage": "string",
            "taskName": "string"
          }
        ],
        "updateMessage": "string"
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: flexible_report_executions_info
short_description: Information module for Flexible Report Executions Info
description:
- This module represents an alias of the module flexible_report_executions_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  reportId:
    description:
    - ReportId path parameter. Id of the report.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Reports GetExecutionIdByReportIdV1
  description: Complete reference of the GetExecutionIdByReportIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-execution-id-by-report-id
notes:
  - SDK Method used are
    reports.Reports.get_execution_id_by_report_id_v1,

  - Paths used are
    get /dna/data/api/v1/flexible-report/report/{reportId}/executions,
  - It should be noted that this module is an alias of flexible_report_executions_v1_info

"""

EXAMPLES = r"""
- name: Get all Flexible Report Executions Info
  cisco.dnac.flexible_report_executions_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    reportId: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "reportId": "string",
      "reportName": "string",
      "executions": [
        {
          "executionId": "string",
          "startTime": 0,
          "endTime": 0,
          "processStatus": "string",
          "requestStatus": "string",
          "errors": [
            "string"
          ],
          "warnings": [
            {}
          ]
        }
      ],
      "executionCount": 0,
      "reportWasExecuted": true
    }
"""

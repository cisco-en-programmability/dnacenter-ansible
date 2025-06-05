#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: flexible_report_schedule
short_description: Resource module for Flexible Report Schedule
description:
  - This module represents an alias of the module flexible_report_schedule_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  reportId:
    description: ReportId path parameter. Id of the report.
    type: str
  schedule:
    description: Schedule information.
    type: dict
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Reports UpdateScheduleOfFlexibleReportV1
    description: Complete reference of the UpdateScheduleOfFlexibleReportV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-schedule-of-flexible-report
notes:
  - SDK Method used are reports.Reports.update_schedule_of_flexible_report_v1,
  - Paths used are put /dna/data/api/v1/flexible-report/schedule/{reportId},
  - It should be noted that this module is an alias of flexible_report_schedule_v1
"""
EXAMPLES = r"""
- name: Update by id
  cisco.dnac.flexible_report_schedule:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    reportId: string
    schedule: {}
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "schedule": {}
    }
"""

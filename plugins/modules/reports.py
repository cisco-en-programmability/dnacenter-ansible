#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: reports
short_description: Resource module for Reports
description:
- This module represents an alias of the module reports_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  dataCategory:
    description: Category of viewgroup for the report.
    type: str
  deliveries:
    description: Array of available delivery channels.
    elements: dict
    type: list
  name:
    description: Report name.
    type: str
  reportId:
    description: ReportId path parameter. ReportId of report.
    type: str
  schedule:
    description: Reports's schedule.
    type: dict
  tags:
    description: Array of tags for report.
    elements: str
    type: list
  view:
    description: Reports's view.
    suboptions:
      fieldGroups:
        description: Reports's fieldGroups.
        elements: dict
        suboptions:
          fieldGroupDisplayName:
            description: Field group label/displayname for user.
            type: str
          fieldGroupName:
            description: Field group name.
            type: str
          fields:
            description: Reports's fields.
            elements: dict
            suboptions:
              displayName:
                description: Field label/displayname.
                type: str
              name:
                description: Field name.
                type: str
            type: list
        type: list
      filters:
        description: Reports's filters.
        elements: dict
        suboptions:
          displayName:
            description: Filter label/displayname.
            type: str
          name:
            description: Filter name.
            type: str
          type:
            description: Filter type.
            type: str
          value:
            description: Value of filter. Data type is based on the filter type. Use
              the filter definitions from the view to fetch the options for a filter.
            type: dict
        type: list
      format:
        description: Reports's format.
        suboptions:
          formatType:
            description: Format type of report.
            type: str
          name:
            description: Format name of report.
            type: str
        type: dict
      name:
        description: View name.
        type: str
      viewId:
        description: View Id.
        type: str
    type: dict
  viewGroupId:
    description: ViewGroupId of the viewgroup for the report.
    type: str
  viewGroupVersion:
    description: Version of viewgroup for the report.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Reports CreateOrScheduleAReportV1
  description: Complete reference of the CreateOrScheduleAReportV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-or-schedule-a-report-v-1
- name: Cisco DNA Center documentation for Reports DeleteAScheduledReportV1
  description: Complete reference of the DeleteAScheduledReportV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-a-scheduled-report-v-1
notes:
  - SDK Method used are
    reports.Reports.create_or_schedule_a_report_v1,
    reports.Reports.delete_a_scheduled_report_v1,

  - Paths used are
    post /dna/intent/api/v1/data/reports,
    delete /dna/intent/api/v1/data/reports/{reportId},
  - It should be noted that this module is an alias of reports_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.reports:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dataCategory: string
    deliveries:
    - {}
    name: string
    schedule: {}
    tags:
    - string
    view:
      fieldGroups:
      - fieldGroupDisplayName: string
        fieldGroupName: string
        fields:
        - displayName: string
          name: string
      filters:
      - displayName: string
        name: string
        type: string
        value: {}
      format:
        formatType: string
        name: string
      name: string
      viewId: string
    viewGroupId: string
    viewGroupVersion: string

- name: Delete by id
  cisco.dnac.reports:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    reportId: string

"""
RETURN = r"""
dnac_response:
  This alias returns the output of reports_v1.
"""

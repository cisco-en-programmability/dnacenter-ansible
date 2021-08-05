#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: reports
short_description: Resource module for Reports
description:
- Manage operations create and delete of the resource Reports.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deliveries:
    description: Reports's deliveries.
    elements: dict
    type: list
  name:
    description: Reports's name.
    type: str
  reportId:
    description: ReportId path parameter. ReportId of report.
    type: str
  schedule:
    description: Reports's schedule.
    type: dict
  tags:
    description: Reports's tags.
    elements: str
    type: list
  view:
    description: Reports's view.
    suboptions:
      fieldGroups:
        description: Reports's fieldGroups.
        suboptions:
          fieldGroupDisplayName:
            description: Reports's fieldGroupDisplayName.
            type: str
          fieldGroupName:
            description: Reports's fieldGroupName.
            type: str
          fields:
            description: Reports's fields.
            suboptions:
              displayName:
                description: Reports's displayName.
                type: str
              name:
                description: Reports's name.
                type: str
            type: list
        type: list
      filters:
        description: Reports's filters.
        suboptions:
          displayName:
            description: Reports's displayName.
            type: str
          name:
            description: Reports's name.
            type: str
          type:
            description: Reports's type.
            type: str
          value:
            description: Reports's value.
            type: dict
        type: list
      format:
        description: Reports's format.
        suboptions:
          formatType:
            description: Reports's formatType.
            type: str
          name:
            description: Reports's name.
            type: str
        type: dict
      name:
        description: Reports's name.
        type: str
      viewId:
        description: Reports's viewId.
        type: str
    type: dict
  viewGroupId:
    description: Reports's viewGroupId.
    type: str
  viewGroupVersion:
    description: Reports's viewGroupVersion.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Reports reference
  description: Complete reference of the Reports object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.reports:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    reportId: string

- name: Create
  cisco.dnac.reports:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
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

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string",
      "status": 0
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: reports_view_group_info
short_description: Information module for Reports View Group
description:
- Get all Reports View Group.
- Get Reports View Group by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  viewGroupId:
    description:
    - ViewGroupId path parameter. ViewGroupId of viewgroup.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Reports View Group reference
  description: Complete reference of the Reports View Group object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Reports View Group
  cisco.dnac.reports_view_group_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
  register: result

- name: Get Reports View Group by id
  cisco.dnac.reports_view_group_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    viewGroupId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "viewGroupId": "string",
      "views": [
        {
          "description": "string",
          "viewId": "string",
          "viewName": "string"
        }
      ]
    }
"""

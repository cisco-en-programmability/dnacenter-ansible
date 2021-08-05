#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_access_point
short_description: Resource module for Wireless Provision Access Point
description:
- Manage operation create of the resource Wireless Provision Access Point.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Wireless Provision Access Point's payload.
    suboptions:
      customApGroupName:
        description: Wireless Provision Access Point's customApGroupName.
        type: str
      customFlexGroupName:
        description: Wireless Provision Access Point's customFlexGroupName.
        elements: str
        type: list
      deviceName:
        description: Wireless Provision Access Point's deviceName.
        type: str
      rfProfile:
        description: Wireless Provision Access Point's rfProfile.
        type: str
      siteId:
        description: Wireless Provision Access Point's siteId.
        type: str
      type:
        description: Wireless Provision Access Point's type.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Provision Access Point reference
  description: Complete reference of the Wireless Provision Access Point object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_provision_access_point:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionUrl": "string",
      "provisionTasks": {
        "success": [
          {
            "taskId": "string",
            "taskUrl": "string"
          }
        ],
        "failure": {
          "taskId": "string",
          "taskUrl": "string",
          "failureReason": "string"
        }
      }
    }
"""

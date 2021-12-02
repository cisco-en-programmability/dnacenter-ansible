#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: disasterrecovery_system_operationstatus_info
short_description: Information module for Disasterrecovery System Operationstatus
description:
- Get all Disasterrecovery System Operationstatus.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Disasterrecovery System Operationstatus reference
  description: Complete reference of the Disasterrecovery System Operationstatus object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Disasterrecovery System Operationstatus
  cisco.dnac.disasterrecovery_system_operationstatus_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "severity": "string",
      "status": "string",
      "initiated_by": "string",
      "ipconfig": [
        {
          "interface": "string",
          "vip": "string",
          "ip": "string"
        }
      ],
      "tasks": [
        {
          "status": "string",
          "ipconfig": [
            {
              "interface": "string",
              "vip": "string",
              "ip": "string"
            }
          ],
          "title": "string",
          "site": "string",
          "startTimestamp": "string",
          "message": "string",
          "endTimestamp": "string"
        }
      ],
      "title": "string",
      "site": "string",
      "startTimestamp": "string",
      "message": "string",
      "endTimestamp": "string"
    }
"""

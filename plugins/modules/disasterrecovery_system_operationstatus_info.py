#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: disasterrecovery_system_operationstatus_info
short_description: Information module for Disasterrecovery System Operationstatus Info
description:
- This module represents an alias of the module disasterrecovery_system_operationstatus_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    disaster_recovery.DisasterRecovery.disaster_recovery_operational_status_v1,

  - Paths used are
    get /dna/intent/api/v1/disasterrecovery/system/operationstatus,
  - It should be noted that this module is an alias of disasterrecovery_system_operationstatus_v1_info

"""

EXAMPLES = r"""
- name: Get all Disasterrecovery System Operationstatus Info
  cisco.dnac.disasterrecovery_system_operationstatus_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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

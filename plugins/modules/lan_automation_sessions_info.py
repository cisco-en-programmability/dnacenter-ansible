#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: lan_automation_sessions_info
short_description: Information module for Lan Automation Sessions Info
description:
- This module represents an alias of the module lan_automation_sessions_v1_info
version_added: '6.14.0'
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
seealso:
- name: Cisco DNA Center documentation for LAN Automation LANAutomationActiveSessionsV1
  description: Complete reference of the LANAutomationActiveSessionsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-active-sessions
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_active_sessions_v1,

  - Paths used are
    get /dna/intent/api/v1/lan-automation/sessions,
  - It should be noted that this module is an alias of lan_automation_sessions_v1_info

"""

EXAMPLES = r"""
- name: Get all Lan Automation Sessions Info
  cisco.dnac.lan_automation_sessions_info:
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
      "response": {
        "maxSupportedCount": "string",
        "activeSessions": "string",
        "activeSessionIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""

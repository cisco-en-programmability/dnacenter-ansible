#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: execute_suggested_actions_commands
short_description: Resource module for Execute Suggested Actions Commands
description:
- This module represents an alias of the module execute_suggested_actions_commands_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  entity_type:
    description: Commands provided as part of the suggested actions for an issue can
      be executed based on issue id. The value here must be issue_id.
    type: str
  entity_value:
    description: Contains the actual value for the entity type that has been defined.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Issues ExecuteSuggestedActionsCommandsV1
  description: Complete reference of the ExecuteSuggestedActionsCommandsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!execute-suggested-actions-commands
notes:
  - SDK Method used are
    issues.Issues.execute_suggested_actions_commands_v1,

  - Paths used are
    post /dna/intent/api/v1/execute-suggested-actions-commands,
  - It should be noted that this module is an alias of execute_suggested_actions_commands_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.execute_suggested_actions_commands:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    entity_type: string
    entity_value: string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  sample: >
    [
      {
        "actionInfo": "string",
        "stepsCount": 0,
        "entityId": "string",
        "hostname": "string",
        "stepsDescription": "string",
        "command": "string",
        "commandOutput": {}
      }
    ]
"""

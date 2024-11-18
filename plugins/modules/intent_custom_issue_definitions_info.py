#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: intent_custom_issue_definitions_info
short_description: Information module for Intent Custom Issue Definitions Info
description:
- This module represents an alias of the module intent_custom_issue_definitions_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Get the custom issue definition for the given custom issue definition Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Issues GetTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionIdV1
  description: Complete reference of the GetTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-the-custom-issue-definition-for-the-given-custom-issue-definition-id
notes:
  - SDK Method used are
    issues.Issues.get_the_custom_issue_definition_for_the_given_custom_issue_definition_id_v1,

  - Paths used are
    get /intent/api/v1/customIssueDefinitions/{id},
  - It should be noted that this module is an alias of intent_custom_issue_definitions_v1_info

"""

EXAMPLES = r"""
- name: Get Intent Custom Issue Definitions Info by id
  cisco.dnac.intent_custom_issue_definitions_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "id": "string",
        "name": "string",
        "description": "string",
        "profileId": "string",
        "triggerId": "string",
        "rules": [
          {
            "type": "string",
            "severity": 0,
            "facility": "string",
            "mnemonic": "string",
            "pattern": "string",
            "occurrences": 0,
            "durationInMinutes": 0
          }
        ],
        "isEnabled": true,
        "priority": "string",
        "isDeletable": true,
        "isNotificationEnabled": true,
        "createdTime": 0,
        "lastUpdatedTime": 0
      }
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: system_issue_definitions_id
short_description: Resource module for System Issue Definitions Id
description:
  - This module represents an alias of the module system_issue_definitions_id_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Issue trigger definition id.
    type: str
  issueEnabled:
    description: Issue Enabled.
    type: bool
  priority:
    description: Priority.
    type: str
  synchronizeToHealthThreshold:
    description: Synchronize To Health Threshold.
    type: bool
  thresholdValue:
    description: Threshold Value.
    type: float
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Issues IssueTriggerDefinitionUpdateV1
    description: Complete reference of the IssueTriggerDefinitionUpdateV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!issue-trigger-definition-update
notes:
  - SDK Method used are issues.Issues.issue_trigger_definition_update_v1,
  - Paths used are put /dna/intent/api/v1/systemIssueDefinitions/{id},
  - It should be noted that this module is an alias of system_issue_definitions_id_v1
"""
EXAMPLES = r"""
- name: Update by id
  cisco.dnac.system_issue_definitions_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
    issueEnabled: true
    priority: string
    synchronizeToHealthThreshold: true
    thresholdValue: 0
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
        "displayName": "string",
        "description": "string",
        "priority": "string",
        "defaultPriority": "string",
        "deviceType": "string",
        "issueEnabled": true,
        "profileId": "string",
        "definitionStatus": "string",
        "categoryName": "string",
        "synchronizeToHealthThreshold": true,
        "thresholdValue": 0,
        "lastModified": "string"
      },
      "version": "string"
    }
"""

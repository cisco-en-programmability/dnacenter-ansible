#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assuranceIssues_update
short_description: Resource module for Assuranceissues Update
description:
- Manage operation create of the resource Assuranceissues Update.
- >
   Updates selected fields in the given issue. Currently the only field that can be updated is 'notes' field. For
   detailed information about the usage of the API, please refer to the Open API specification document - https
   //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
   IssuesLifecycle-1.0.0-resolved.yaml.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. The issue Uuid.
    type: str
  notes:
    description: Notes.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Issues UpdateTheGivenIssueByUpdatingSelectedFields
  description: Complete reference of the UpdateTheGivenIssueByUpdatingSelectedFields API.
  link: https://developer.cisco.com/docs/dna-center/#!update-the-given-issue-by-updating-selected-fields
notes:
  - SDK Method used are
    issues.Issues.update_the_given_issue_by_updating_selected_fields,

  - Paths used are
    post /dna/intent/api/v1/assuranceIssues/{id}/update,

"""

EXAMPLES = r"""
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "issueId": "string",
        "name": "string",
        "description": "string",
        "summary": "string",
        "priority": "string",
        "severity": "string",
        "deviceType": "string",
        "category": "string",
        "entityType": "string",
        "entityId": "string",
        "firstOccurredTime": 0,
        "mostRecentOccurredTime": 0,
        "status": "string",
        "isGlobal": true,
        "updatedBy": "string",
        "updatedTime": 0,
        "notes": "string",
        "siteId": "string",
        "siteHierarchyId": "string",
        "siteName": "string",
        "siteHierarchy": "string",
        "suggestedActions": [
          {
            "message": "string"
          }
        ],
        "additionalAttributes": [
          {
            "key": "string",
            "value": "string"
          }
        ]
      },
      "version": "string"
    }
"""

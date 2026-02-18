#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: issue_enrichment_details_info
short_description: Information module for Issue Enrichment Details
description:
  - Get all Issue Enrichment Details.
  - Enriches a given network issue context an issue id or end user's Mac Address with details about the issues.
  - Includes impacted hosts and suggested actions for remediation.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Issues GetIssueEnrichmentDetailsV2
    description: Complete reference of the GetIssueEnrichmentDetailsV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-issue-enrichment-details-v-2
notes:
  - SDK Method used are
    issues.Issues.get_issue_enrichment_details_v2,
  - Paths used are
    get /dna/intent/api/v2/issue-enrichment-details,
"""

EXAMPLES = r"""
---
- name: Get all Issue Enrichment Details
  cisco.dnac.issue_enrichment_details_info:
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
      "issue": [
        {
          "issueId": "string",
          "issueSource": "string",
          "issueCategory": "string",
          "issueName": "string",
          "issueDescription": "string",
          "issueEntity": "string",
          "issueEntityValue": "string",
          "issueSeverity": "string",
          "issuePriority": "string",
          "issueSummary": "string",
          "issueTimestamp": 0,
          "suggestedActions": [
            {
              "message": "string",
              "steps": [
                "string"
              ]
            }
          ],
          "impactedHosts": [
            "string"
          ]
        }
      ]
    }
"""

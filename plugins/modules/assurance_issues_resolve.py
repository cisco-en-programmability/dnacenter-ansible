#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: assurance_issues_resolve
short_description: Resource module for Assurance Issues Resolve
description:
  - This module represents an alias of the module assurance_issues_resolve_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  issueIds:
    description: Issue Ids.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Issues ResolveTheGivenListsOfIssuesV1
    description: Complete reference of the ResolveTheGivenListsOfIssuesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!resolve-the-given-lists-of-issues
notes:
  - SDK Method used are issues.Issues.resolve_the_given_lists_of_issues_v1,
  - Paths used are post /dna/intent/api/v1/assuranceIssues/resolve,
  - It should be noted that this module is an alias of assurance_issues_resolve_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.assurance_issues_resolve:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: '{{my_headers | from_json}}'
    issueIds:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "successfulIssueIds": [
          "string"
        ],
        "failureIssueIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""

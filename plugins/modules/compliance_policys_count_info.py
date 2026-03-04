#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_count_info
short_description: Information module for Compliance Policys Count
description:
  - Get all Compliance Policys Count.
  - Retrieves the count of compliance policies.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  policyId:
    description:
      - PolicyId query parameter. The IDs of the compliance policies.The number of policyId(s) must not exceed 25.
    type: str
  name:
    description:
      - Name query parameter. Filter with policy name. Supports partial case-insensitive search.
    type: str
  siteId:
    description:
      - SiteId query parameter. The `id` of the site to which compliance policies are associated.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance RetrieveTheCountOfPolicies
    description: Complete reference of the RetrieveTheCountOfPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-policies
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_count_of_policies,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/count,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Count
  cisco.dnac.compliance_policys_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    policyId: string
    name: string
    siteId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "runStatus": "string",
          "submitTime": 0,
          "startTime": 0,
          "endTime": 0,
          "validationStatus": "string",
          "validationSetIds": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""

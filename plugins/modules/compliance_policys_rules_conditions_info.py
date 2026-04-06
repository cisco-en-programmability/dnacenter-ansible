#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_conditions_info
short_description: Information module for Compliance Policys Rules Conditions
description:
  - Get all Compliance Policys Rules Conditions.
  - Get Compliance Policys Rules Conditions by id.
  - Retrieves a specific condition within the specified compliance policy and rule.
  - Retrieves the list of all conditions within the specified compliance policy and rule.
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
      - PolicyId path parameter. The `id` of the compliance policy.
    type: str
  ruleId:
    description:
      - RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default is 500 if not specified.
        Maximum allowed limit is 500.
    type: int
  id:
    description:
      - Id path parameter. The `id` of the condition.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance RetrieveASpecificCondition
    description: Complete reference of the RetrieveASpecificCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-condition
  - name: Cisco DNA Center documentation for Compliance RetrieveTheConditions
    description: Complete reference of the RetrieveTheConditions API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-conditions
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_specific_condition,
    compliance.Compliance.retrieve_the_conditions,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions,
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions/{id},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Rules Conditions
  cisco.dnac.compliance_policys_rules_conditions_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    policyId: string
    ruleId: string
  register: result
- name: Get Compliance Policys Rules Conditions by id
  cisco.dnac.compliance_policys_rules_conditions_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    policyId: string
    ruleId: string
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
        "name": "string",
        "description": "string"
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_variables_info
short_description: Information module for Compliance Policys Rules Variables
description:
  - Get all Compliance Policys Rules Variables.
  - Get Compliance Policys Rules Variables by id.
  - Retrieves a specific variable within the specified compliance policy and rule.
  - Retrieves the list of all variables within the specified compliance policy and rule.
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
      - Id path parameter. The `id` of the variable.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance RetrieveASpecificVariable
    description: Complete reference of the RetrieveASpecificVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-variable
  - name: Cisco DNA Center documentation for Compliance RetrieveTheVariables
    description: Complete reference of the RetrieveTheVariables API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-variables
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_specific_variable,
    compliance.Compliance.retrieve_the_variables,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables,
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables/{id},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Rules Variables
  cisco.dnac.compliance_policys_rules_variables_info:
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
- name: Get Compliance Policys Rules Variables by id
  cisco.dnac.compliance_policys_rules_variables_info:
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
      "response": [
        {
          "id": "string",
          "sequenceNumber": 0,
          "name": "string",
          "description": "string",
          "dataType": "string",
          "mandatory": true,
          "inputType": "string",
          "selectionList": [
            {
              "key": "string",
              "value": "string",
              "default": true
            }
          ],
          "defaultValue": "string",
          "maxLength": 0,
          "validationRegex": "string",
          "minValue": 0,
          "maxValue": 0,
          "identifier": "string",
          "usedByConditions": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""

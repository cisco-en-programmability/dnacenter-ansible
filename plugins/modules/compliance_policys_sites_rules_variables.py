#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_sites_rules_variables
short_description: Resource module for Compliance Policys Sites Rules Variables
description:
  - Manage operation update of the resource Compliance Policys Sites Rules Variables.
  - Set site variable values for the specified rule within the compliance policy.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  ruleId:
    description: RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  siteId:
    description: SiteId path parameter. The `id` of the site to which compliance policy is associated.
    type: str
  variableValues:
    description: Compliance Policys Sites Rules Variables's variableValues.
    elements: dict
    suboptions:
      id:
        description: The `id` of the variable.
        type: str
      values:
        description: List of variable values. The order of the list is preserved for compliance checks. The variable value
          is formatted as a string. It must be a valid string representation of the data and conform to the specified type.
          For variables with an input type of `SINGLE_SELECT` or `MULTI_SELECT`, pass the actual value, not the key.
        elements: str
        type: list
    type: list
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance SetSiteVariables
    description: Complete reference of the SetSiteVariables API.
    link: https://developer.cisco.com/docs/dna-center/#!set-site-variables
notes:
  - SDK Method used are
    compliance.Compliance.set_site_variables,
  - Paths used are
    put /dna/intent/api/v1/compliancePolicys/{policyId}/sites/{siteId}/rules/{ruleId}/variables,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.dnac.compliance_policys_sites_rules_variables:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    policyId: string
    ruleId: string
    siteId: string
    variableValues:
      - id: string
        values:
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

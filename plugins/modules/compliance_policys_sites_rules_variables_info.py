#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_sites_rules_variables_info
short_description: Information module for Compliance Policys Sites Rules Variables
description:
  - Get all Compliance Policys Sites Rules Variables.
  - Retrieve the site variables for the specified rule within the compliance policy.
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
  siteId:
    description:
      - SiteId path parameter. The `id` of the site to which compliance policy is associated.
    type: str
  ruleId:
    description:
      - RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  _inherited:
    description:
      - >
        _inherited query parameter. Include values explicitly set for this site; when false, null values
        indicate that the site inherits these values from the parent site or a higher level in the site
        hierarchy.
    type: bool
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance RetrieveSiteVariables
    description: Complete reference of the RetrieveSiteVariables API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-site-variables
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_site_variables,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/{policyId}/sites/{siteId}/rules/{ruleId}/variables,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Sites Rules Variables
  cisco.dnac.compliance_policys_sites_rules_variables_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: true
    policyId: string
    siteId: string
    ruleId: string
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
        "variableValues": [
          {
            "id": "string",
            "values": [
              "string"
            ]
          }
        ],
        "inheritedSiteId": "string",
        "inheritedSiteName": "string"
      },
      "version": "string"
    }
"""

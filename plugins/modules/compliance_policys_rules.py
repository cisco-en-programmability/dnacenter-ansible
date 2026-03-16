#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules
short_description: Resource module for Compliance Policys Rules
description:
  - Manage operations create, update and delete of the resource Compliance Policys Rules.
  - This API operation creates a new rule within the specified compliance policy.
  - Deletes the rule within the specified compliance policy.
  - Updates the details of an existing rule within the specified compliance policy.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  description:
    description: A comprehensive description of the rule. This should provide detailed information about what the rule does,
      its scope, and any other pertinent details that explain its function and purpose.
    type: str
  deviceTypes:
    description: Compliance Policys Rules's deviceTypes.
    elements: dict
    suboptions:
      deviceFamily:
        description: The device family.
        type: str
      deviceModel:
        description: The device model. When a device model is specified, `deviceSeries` is required.
        type: str
      deviceSeries:
        description: The device series.
        type: str
    type: list
  id:
    description: Id path parameter. The `id` of the rule within the compliance policy.
    type: str
  impact:
    description: This describes the potential impact when the conditions of this rule are violated.
    type: str
  name:
    description: This is the name of the rule. It should be a concise and descriptive title that clearly identifies the rule's
      purpose or function. The name must be unique within the specified policy.
    type: str
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  softwareType:
    description: Specifies the software type applicable to the rule. For detailed enum descriptions, refer to the `Features`
      tab.
    type: str
  suggestedFix:
    description: Suggestions on how to fix the issues detected by this rule.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance CreateANewRule
    description: Complete reference of the CreateANewRule API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-rule
  - name: Cisco DNA Center documentation for Compliance DeleteASpecificRule
    description: Complete reference of the DeleteASpecificRule API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-specific-rule
  - name: Cisco DNA Center documentation for Compliance UpdateAnExistingRule
    description: Complete reference of the UpdateAnExistingRule API.
    link: https://developer.cisco.com/docs/dna-center/#!update-an-existing-rule
notes:
  - SDK Method used are
    compliance.Compliance.create_a_new_rule,
    compliance.Compliance.delete_a_specific_rule,
    compliance.Compliance.update_an_existing_rule,
  - Paths used are
    post /dna/intent/api/v1/compliancePolicys/{policyId}/rules,
    delete /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{id},
    put /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.compliance_policys_rules:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    deviceTypes:
      - deviceFamily: string
        deviceModel: string
        deviceSeries: string
    impact: string
    name: string
    policyId: string
    softwareType: string
    suggestedFix: string
- name: Delete by id
  cisco.dnac.compliance_policys_rules:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
    policyId: string
- name: Update by id
  cisco.dnac.compliance_policys_rules:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    deviceTypes:
      - deviceFamily: string
        deviceModel: string
        deviceSeries: string
    id: string
    impact: string
    name: string
    policyId: string
    softwareType: string
    suggestedFix: string
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

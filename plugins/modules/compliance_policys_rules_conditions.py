#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_conditions
short_description: Resource module for Compliance Policys Rules Conditions
description:
  - Manage operations create, update and delete of the resource Compliance Policys Rules Conditions.
  - This API operation creates a new condition within the specified compliance policy and rule.
  - Deletes a specific condition within the specified compliance policy and rule.
  - Updates an existing compliance condition within the specified compliance policy and rule.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  action:
    description: Compliance Policys Rules Conditions's action.
    suboptions:
      doesNotMatchAction:
        description: Action to take when the condition does not match. The choice of action influences whether a violation
          is logged and whether further conditions are evaluated. For detailed enum descriptions, refer to the `Features`
          tab.
        type: str
      doesNotMatchViolationMessage:
        description: Specify the custom violation message to be used to report violations when the condition does not match
          and raises violation. This field is applicable and required when `doesNotMatchViolationMessageType` is `CUSTOM_MESSAGE`.
          Custom variables and automatically generated regular expression group variables can both be used in this field,
          similar to how they are used in the `value` field.
        type: str
      doesNotMatchViolationMessageType:
        description: The type of message to display when the condition does not match and results in a violation. This provides
          context about the violation. This field is applicable and required when `doesNotMatchAction` is either `RAISE_VIOLATION_AND_CONTINUE`
          or `RAISE_VIOLATION_AND_STOP`. For detailed enum descriptions, refer to the `Features` tab.
        type: str
      doesNotMatchViolationSeverity:
        description: The severity level of the violation when the condition does not match. This field is applicable and required
          when `doesNotMatchAction` is either `RAISE_VIOLATION_AND_CONTINUE` or `RAISE_VIOLATION_AND_STOP`.
        type: str
      matchAction:
        description: Action to take when the condition matches. The choice of action influences whether a violation is logged
          and whether further conditions are evaluated. For detailed enum descriptions, refer to the `Features` tab.
        type: str
      matchViolationMessage:
        description: Specify the custom violation message to be used to report violations when the condition matches and raises
          violation. This field is applicable and required when `matchViolationMessageType` is `CUSTOM_MESSAGE`. Custom variables
          and automatically generated regular expression group variables can both be used in this field, similar to how they
          are used in the `value` field.
        type: str
      matchViolationMessageType:
        description: The type of message to display when the condition matches and results in a violation. This provides context
          about the violation. This field is applicable and required when `matchAction` is either `RAISE_VIOLATION_AND_CONTINUE`
          or `RAISE_VIOLATION_AND_STOP`. For detailed enum descriptions, refer to the `Features` tab.
        type: str
      matchViolationSeverity:
        description: The severity level of the violation when the condition matches. This field is applicable and required
          when `matchAction` is either `RAISE_VIOLATION_AND_CONTINUE` or `RAISE_VIOLATION_AND_STOP`.
        type: str
    type: dict
  blockEndExpression:
    description: The regular expression defining the end of a block. If not specified, block parsing will continue until new
      section starts in the configuration. This is applicable only when `parseAsBlocks` is set. This is an optional field.
      The value, when provided, must be a valid regular expression.
    type: str
  blockStartExpression:
    description: The regular expression defining the start of a block. This is used to identify the beginning of relevant
      configuration sections. This is applicable and required only when `parseAsBlocks` is set. The value must be a valid
      regular expression.
    type: str
  blockViolationCriteria:
    description: Criteria determining when a violation is raised based on block evaluation results. This allows for flexible
      compliance checks depending on whether a single failure or all failures should trigger a violation. For detailed enum
      descriptions, refer to the `Features` tab.
    type: str
  deviceProperty:
    description: The specific device property to consider as source for the condition. For detailed enum descriptions, refer
      to the `Features` tab.
    type: str
  id:
    description: Id path parameter. The `id` of the condition.
    type: str
  operator:
    description: The operation used to evaluate the condition. String, regular expression, and expressions required for the
      operator to work are provided in `value` attribute. For detailed enum descriptions, refer to the `Features` tab.
    type: str
  parseAsBlocks:
    description: An optional param that indicates whether to parse the configuration as discrete blocks for evaluation. Useful
      for conditions that apply to specific sections of a configuration file. This is applicable for all condition scopes
      except `DEVICE_PROPERTIES`. When scope is `PREVIOUSLY_MATCHED_BLOCKS`, this helps extract sub-blocks or portion of the
      blocks. When this is set, `blockStartExpression` must be provided. Optionally, `blockEndExpression` can be provided
      to customise blocks further.
    type: bool
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  regexViolationCriteria:
    description: Criteria determining when a violation is raised based on regular expression evaluation results. This allows
      for flexible compliance checks depending on whether a single failure or all failures should trigger a violation. For
      detailed enum descriptions, refer to the `Features` tab.
    type: str
  ruleId:
    description: RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  scope:
    description: The source of data for the evaluation of the condition. For detailed enum descriptions, refer to the `Features`
      tab.
    type: str
  showCommand:
    description: "The command executed on the device to retrieve output for evaluation. Pattern ^((S|s)(H|h)(O|o)(W|w))\\s+.+$
      — The string must start with `show` (case-insensitive), followed by at least one space, and then any sequence of characters.
      For detailed information on using `show` command, refer to the `Features` tab."
    type: str
  value:
    description: The value or pattern used in the condition evaluation. Custom variables and automatically generated regular
      expression group variables can both be used in this field. For detailed information on using variables, refer to the
      `Features` tab.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance CreateANewCondition
    description: Complete reference of the CreateANewCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-condition
  - name: Cisco DNA Center documentation for Compliance DeleteASpecificCondition
    description: Complete reference of the DeleteASpecificCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-specific-condition
  - name: Cisco DNA Center documentation for Compliance UpdateAnExistingCondition
    description: Complete reference of the UpdateAnExistingCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!update-an-existing-condition
notes:
  - SDK Method used are
    compliance.Compliance.create_a_new_condition,
    compliance.Compliance.delete_a_specific_condition,
    compliance.Compliance.update_an_existing_condition,
  - Paths used are
    post /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions,
    delete /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions/{id},
    put /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.compliance_policys_rules_conditions:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    action:
      doesNotMatchAction: string
      doesNotMatchViolationMessage: string
      doesNotMatchViolationMessageType: string
      doesNotMatchViolationSeverity: string
      matchAction: string
      matchViolationMessage: string
      matchViolationMessageType: string
      matchViolationSeverity: string
    blockEndExpression: string
    blockStartExpression: string
    blockViolationCriteria: string
    deviceProperty: string
    operator: string
    parseAsBlocks: true
    policyId: string
    regexViolationCriteria: string
    ruleId: string
    scope: string
    showCommand: string
    value: string
- name: Delete by id
  cisco.dnac.compliance_policys_rules_conditions:
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
    ruleId: string
- name: Update by id
  cisco.dnac.compliance_policys_rules_conditions:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    action:
      doesNotMatchAction: string
      doesNotMatchViolationMessage: string
      doesNotMatchViolationMessageType: string
      doesNotMatchViolationSeverity: string
      matchAction: string
      matchViolationMessage: string
      matchViolationMessageType: string
      matchViolationSeverity: string
    blockEndExpression: string
    blockStartExpression: string
    blockViolationCriteria: string
    deviceProperty: string
    id: string
    operator: string
    parseAsBlocks: true
    policyId: string
    regexViolationCriteria: string
    ruleId: string
    scope: string
    showCommand: string
    value: string
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

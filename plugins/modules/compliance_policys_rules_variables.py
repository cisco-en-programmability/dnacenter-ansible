#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_variables
short_description: Resource module for Compliance Policys Rules Variables
description:
  - Manage operations create, update and delete of the resource Compliance Policys Rules Variables.
  - This API operation creates a new variable within the specified compliance policy and rule.
  - Deletes a specific variable within the specified compliance policy and rule.
  - Updates an existing compliance variable within the specified compliance policy and rule.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  dataType:
    description: The data type of the variable. IP mask is supported in IP address form (e.g., 255.255.255.0) only. Interface
      names must be provided in their full form, such as GigabitEthernet1/0/1.
    type: str
  defaultValue:
    description: The default value for the variable. This is applicable when `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
      Ensure that any type of data is formatted as a string, but it must match the required format for the data type and adhere
      to any provided constraints.
    type: str
  description:
    description: A brief description of the variable.
    type: str
  id:
    description: Id path parameter. The `id` of the variable.
    type: str
  identifier:
    description: This is the identifier of the variable. Variables are referenced using the identifier enclosed in angle brackets.
      Update operation cannot be used to change the identifier.
    type: str
  inputType:
    description: The input type of the variable. For detailed enum descriptions, refer to the `Features` tab.
    type: str
  mandatory:
    description: Indicates if the variable is mandatory.
    type: bool
  maxLength:
    description: The maximum length constraint for the `STRING` values. This is only applicable when the `inputType` is `SINGLE_TEXT`
      or `MULTI_TEXT`. Max length must be between 1 and 255, both inclusive.
    type: int
  maxValue:
    description: The maximum value constraint for the `INTEGER` variable. This is only applicable when the `inputType` is
      `SINGLE_TEXT` or `MULTI_TEXT`.
    type: int
  minValue:
    description: The minimum value constraint for the `INTEGER` variable. This is only applicable when the `inputType` is
      `SINGLE_TEXT` or `MULTI_TEXT`.
    type: int
  name:
    description: This is the name of the variable. It should be a concise and descriptive title that clearly identifies the
      variable. The name must be unique within the specified rule. Pattern ^\w\ \-\(\)+$.
    type: str
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  ruleId:
    description: RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  selectionList:
    description: Compliance Policys Rules Variables's selectionList.
    elements: dict
    suboptions:
      default:
        description: Indicates whether this selection option is the default. Depending on the `inputType`, either only one
          or multiple selection options can be set as default.
        type: bool
      key:
        description: The key for the selection option, which uniquely identifies the value.
        type: str
      value:
        description: This is the value for the selection option. Ensure that any type of data is formatted as a string, but
          it must match the required format for the data type and adhere to any provided constraints.
        type: str
    type: list
  validationRegex:
    description: A regular expression pattern for constraining `STRING` values. This is only applicable when the `inputType`
      is `SINGLE_TEXT` or `MULTI_TEXT`.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance CreateANewVariable
    description: Complete reference of the CreateANewVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-variable
  - name: Cisco DNA Center documentation for Compliance DeleteASpecificVariable
    description: Complete reference of the DeleteASpecificVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-specific-variable
  - name: Cisco DNA Center documentation for Compliance UpdateAnExistingVariable
    description: Complete reference of the UpdateAnExistingVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!update-an-existing-variable
notes:
  - SDK Method used are
    compliance.Compliance.create_a_new_variable,
    compliance.Compliance.delete_a_specific_variable,
    compliance.Compliance.update_an_existing_variable,
  - Paths used are
    post /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables,
    delete /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables/{id},
    put /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.compliance_policys_rules_variables:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    dataType: string
    defaultValue: string
    description: string
    identifier: string
    inputType: string
    mandatory: true
    maxLength: 0
    maxValue: 0
    minValue: 0
    name: string
    policyId: string
    ruleId: string
    selectionList:
      - default: true
        key: string
        value: string
    validationRegex: string
- name: Delete by id
  cisco.dnac.compliance_policys_rules_variables:
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
  cisco.dnac.compliance_policys_rules_variables:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    dataType: string
    defaultValue: string
    description: string
    id: string
    inputType: string
    mandatory: true
    maxLength: 0
    maxValue: 0
    minValue: 0
    name: string
    policyId: string
    ruleId: string
    selectionList:
      - default: true
        key: string
        value: string
    validationRegex: string
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

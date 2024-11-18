#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: diagnostic_validation_workflows
short_description: Resource module for Diagnostic Validation Workflows
description:
- This module represents an alias of the module diagnostic_validation_workflows_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of the workflow to run.
    type: str
  id:
    description: Id path parameter. Workflow id.
    type: str
  name:
    description: Name of the workflow to run. It must be unique.
    type: str
  validationSetIds:
    description: List of validation set ids.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Health and Performance SubmitsTheWorkflowForExecutingValidationsV1
  description: Complete reference of the SubmitsTheWorkflowForExecutingValidationsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!submits-the-workflow-for-executing-validations-v-1
- name: Cisco DNA Center documentation for Health and Performance DeletesAValidationWorkflowV1
  description: Complete reference of the DeletesAValidationWorkflowV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!deletes-a-validation-workflow-v-1
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.deletes_a_validation_workflow_v1,
    health_and_performance.HealthAndPerformance.submits_the_workflow_for_executing_validations_v1,

  - Paths used are
    post /dna/intent/api/v1/diagnosticValidationWorkflows,
    delete /dna/intent/api/v1/diagnosticValidationWorkflows/{id},
  - It should be noted that this module is an alias of diagnostic_validation_workflows_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.diagnostic_validation_workflows:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    description: string
    name: string
    validationSetIds:
    - string

- name: Delete by id
  cisco.dnac.diagnostic_validation_workflows:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of diagnostic_validation_workflows_v1.
"""
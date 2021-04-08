#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_api_status
short_description: Manage EventApiStatus objects of EventManagement
description:
- Get the Status of events API calls with provided executionId as mandatory path parameter.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  execution_id:
    description:
    - Execution ID.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.event_api_status
# Reference by Internet resource
- name: EventApiStatus reference
  description: Complete reference of the EventApiStatus object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EventApiStatus reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_status_api_for_events
  cisco.dnac.event_api_status:
    state: query  # required
    execution_id: SomeValue  # string, required
  register: nm_get_status_api_for_events

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: event_management.get_status_api_for_events
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

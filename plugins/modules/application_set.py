#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: application_set
short_description: Manage ApplicationSet objects of ApplicationPolicy
description:
- Delete existing application-set by it's id.
- Get appllication-sets by offset/limit or by name.
- Create new custom application-set/s.
- Get the number of existing application-sets.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id query parameter.
    - Required for state delete.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: int
  name:
    description:
    - Name query parameter.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: int
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - It is the application set's name.
        type: str

  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.application_set
# Reference by Internet resource
- name: ApplicationSet reference
  description: Complete reference of the ApplicationSet object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ApplicationSet reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_application_set
  cisco.dnac.application_set:
    state: delete  # required
    id: SomeValue  # string, required

- name: get_application_sets
  cisco.dnac.application_set:
    state: query  # required
    limit: 1  #  number
    name: SomeValue  # string
    offset: 1  #  number
  register: nm_get_application_sets

- name: create_application_set
  cisco.dnac.application_set:
    state: create  # required
    payload:  # required
    - name: SomeValue  # string

- name: get_application_sets_count
  cisco.dnac.application_set:
    state: query  # required
    count: True  # boolean, required
  register: nm_get_application_sets_count

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
  sample: application_policy.create_application_set
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

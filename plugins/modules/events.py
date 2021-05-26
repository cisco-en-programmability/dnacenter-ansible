#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: events
short_description: Manage Events objects of EventManagement
description:
- Gets the list of registered Events with provided eventIds or tags as mandatory.
- Get the count of registered Events with provided eventIds or tags as mandatory.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  tags:
    description:
    - The registered Tags should be provided.
    type: str
    required: True
  event_id:
    description:
    - The registered EventId should be provided.
    type: str
  limit:
    description:
    - The number of Registries to limit in the resultset whose default value 10.
    type: int
  offset:
    description:
    - The number of Registries to offset in the resultset whose default value 0.
    type: int
  order:
    description:
    - Order query parameter.
    type: str
  sort_by:
    description:
    - SortBy field name.
    type: str
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.events
# Reference by Internet resource
- name: Events reference
  description: Complete reference of the Events object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Events reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_events
  cisco.dnac.events:
    state: query  # required
    tags: SomeValue  # string, required
    event_id: SomeValue  # string
    limit: 1  #  number
    offset: 1  #  number
    order: SomeValue  # string
    sort_by: SomeValue  # string
  register: nm_get_events

- name: count_of_events
  cisco.dnac.events:
    state: query  # required
    tags: SomeValue  # string, required
    count: True  # boolean, required
    event_id: SomeValue  # string
  register: nm_count_of_events

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
  sample: event_management.count_of_events
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

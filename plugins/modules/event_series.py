#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: event_series
short_description: Manage EventSeries objects of EventManagement
description:
- Get the list of Published Notifications.
- Get the Count of Published Notifications.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  category:
    description:
    - Category .
    type: str
  domain:
    description:
    - Domain .
    type: str
  end_time:
    description:
    - EndTime .
    type: str
  event_ids:
    description:
    - The registered EventIds should be provided.
    type: str
  limit:
    description:
    - Limit whose default value 10.
    type: int
  offset:
    description:
    - Offset whose default value 0.
    type: int
  order:
    description:
    - Order query parameter.
    type: str
  severity:
    description:
    - Severity .
    type: str
  sort_by:
    description:
    - SortBy field name.
    type: str
  source:
    description:
    - Source .
    type: str
  start_time:
    description:
    - StartTime .
    type: str
  sub_domain:
    description:
    - SubDomain .
    type: str
  type:
    description:
    - Type .
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
- module: cisco.dnac.plugins.module_utils.definitions.event_series
# Reference by Internet resource
- name: EventSeries reference
  description: Complete reference of the EventSeries object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EventSeries reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_notifications
  cisco.dnac.event_series:
    state: query  # required
    category: SomeValue  # string
    domain: SomeValue  # string
    end_time: SomeValue  # string
    event_ids: SomeValue  # string
    limit: 1  #  number
    offset: 1  #  number
    order: SomeValue  # string
    severity: SomeValue  # string
    sort_by: SomeValue  # string
    source: SomeValue  # string
    start_time: SomeValue  # string
    sub_domain: SomeValue  # string
    type: SomeValue  # string
  register: nm_get_notifications

- name: count_of_notifications
  cisco.dnac.event_series:
    state: query  # required
    count: True  # boolean, required
    category: SomeValue  # string
    domain: SomeValue  # string
    end_time: SomeValue  # string
    event_ids: SomeValue  # string
    severity: SomeValue  # string
    source: SomeValue  # string
    start_time: SomeValue  # string
    sub_domain: SomeValue  # string
    type: SomeValue  # string
  register: nm_count_of_notifications

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
  sample: event_management.count_of_notifications
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

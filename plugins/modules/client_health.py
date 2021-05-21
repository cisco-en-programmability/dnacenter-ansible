#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: client_health
short_description: Manage ClientHealth objects of Clients
description:
- Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  timestamp:
    description:
    - Epoch time(in milliseconds) when the Client health data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.client_health
# Reference by Internet resource
- name: ClientHealth reference
  description: Complete reference of the ClientHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ClientHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_overall_client_health
  cisco.dnac.client_health:
    state: query  # required
    timestamp: 1  #  integer
  register: nm_get_overall_client_health

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
  sample: clients.get_overall_client_health
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

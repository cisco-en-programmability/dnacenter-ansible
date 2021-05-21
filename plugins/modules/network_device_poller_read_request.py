#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_device_poller_read_request
short_description: Manage NetworkDevicePollerReadRequest objects of CommandRunner
description:
- Submit request for read-only CLIs.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  commands:
    description:
    - CommandRunnerDTO's commands (list of strings).
    type: list
    required: True
  description:
    description:
    - CommandRunnerDTO's description.
    type: str
  deviceUuids:
    description:
    - CommandRunnerDTO's deviceUuids (list of strings).
    type: list
    required: True
  name:
    description:
    - CommandRunnerDTO's name.
    type: str
  timeout:
    description:
    - CommandRunnerDTO's timeout.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_poller_read_request
# Reference by Internet resource
- name: NetworkDevicePollerReadRequest reference
  description: Complete reference of the NetworkDevicePollerReadRequest object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDevicePollerReadRequest reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: run_read_only_commands_on_devices
  cisco.dnac.network_device_poller_read_request:
    state: create  # required
    commands:  # required
    - SomeValue  # string
    deviceUuids:  # required
    - SomeValue  # string
    description: SomeValue  # string
    name: SomeValue  # string
    timeout: 1  #  integer

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
  sample: command_runner.run_read_only_commands_on_devices
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

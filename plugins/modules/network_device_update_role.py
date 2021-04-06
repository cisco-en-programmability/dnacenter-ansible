#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_update_role
short_description: Manage NetworkDeviceUpdateRole objects of Devices
description:
- Updates the role of the device as access, core, distribution, border router.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - NetworkDeviceBriefNIO's id.
    type: str
    required: True
  role:
    description:
    - NetworkDeviceBriefNIO's role.
    type: str
    required: True
  roleSource:
    description:
    - NetworkDeviceBriefNIO's roleSource.
    type: str
    required: True
  summary:
    description:
    - If true gets the summary.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_update_role
# Reference by Internet resource
- name: NetworkDeviceUpdateRole reference
  description: Complete reference of the NetworkDeviceUpdateRole object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceUpdateRole reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: update_device_role
  cisco.dnac.network_device_update_role:
    state: update  # required
    id: SomeValue  # string, required
    role: SomeValue  # string, required
    roleSource: SomeValue  # string, required
    summary: True  # boolean, required

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
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_config
short_description: Manage NetworkDeviceConfig objects of Devices
description:
- Returns the config for all devices.
- Returns the count of device configs.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_config
# Reference by Internet resource
- name: NetworkDeviceConfig reference
  description: Complete reference of the NetworkDeviceConfig object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceConfig reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_config_for_all_devices
  cisco.dnac.network_device_config:
    state: query  # required
  register: nm_get_device_config_for_all_devices

- name: get_device_config_count
  cisco.dnac.network_device_config:
    state: query  # required
    count: True  # boolean, required
  register: nm_get_device_config_count

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
  sample: devices.get_device_config_count
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_polling_interval
short_description: Manage NetworkDevicePollingInterval objects of Devices
description:
- Returns polling interval by device id.
- Returns polling interval of all devices.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Device ID.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_polling_interval
# Reference by Internet resource
- name: NetworkDevicePollingInterval reference
  description: Complete reference of the NetworkDevicePollingInterval object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDevicePollingInterval reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_polling_interval_by_id
  cisco.dnac.network_device_polling_interval:
    state: query  # required
    id: SomeValue  # string, required
  register: nm_get_polling_interval_by_id

- name: get_polling_interval_for_all_devices
  cisco.dnac.network_device_polling_interval:
    state: query  # required
  register: nm_get_polling_interval_for_all_devices

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
  sample: devices.get_polling_interval_by_id
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

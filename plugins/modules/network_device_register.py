#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_register
short_description: Manage NetworkDeviceRegister objects of Devices
description:
- Registers a device for WSA notification.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  macaddress:
    description:
    - Mac addres of the device.
    type: str
  serial_number:
    description:
    - Serial number of the device.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_register
# Reference by Internet resource
- name: NetworkDeviceRegister reference
  description: Complete reference of the NetworkDeviceRegister object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceRegister reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: register_device_for_wsa
  cisco.dnac.network_device_register:
    state: query  # required
    macaddress: SomeValue  # string
    serial_number: SomeValue  # string
  register: nm_register_device_for_wsa

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
  sample: devices.register_device_for_wsa
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

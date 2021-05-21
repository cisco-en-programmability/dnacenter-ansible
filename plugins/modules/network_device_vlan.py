#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_device_vlan
short_description: Manage NetworkDeviceVlan objects of Devices
description:
- Returns Device Interface VLANs.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
    required: True
  interface_type:
    description:
    - Vlan assocaited with sub-interface.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_vlan
# Reference by Internet resource
- name: NetworkDeviceVlan reference
  description: Complete reference of the NetworkDeviceVlan object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceVlan reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_interface_vlans
  cisco.dnac.network_device_vlan:
    state: query  # required
    id: SomeValue  # string, required
    interface_type: SomeValue  # string
  register: nm_get_device_interface_vlans

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
  sample: devices.get_device_interface_vlans
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface
short_description: Manage Interface objects of Devices
description:
- Returns all available Interfaces. This endpoint can return a maximum of 500 Interfaces.
- Returns the Interface for the given Interface ID.
- Returns the count of Interfaces for all devices.
- Returns list of Interfaces by specified IP address.
- Returns list of Interfaces by specified device.
- Returns the list of Interfaces for the device for the specified range.
- Returns the Interface count for the given device.
- Returns Interface by specified device Id and Interface name.
- Returns the Interfaces that has ISIS enabled.
- Returns the Interfaces that has OSPF enabled.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  limit:
    description:
    - Limit query parameter.
    type: int
  offset:
    description:
    - Offset query parameter.
    type: int
  id:
    description:
    - Interface ID.
    type: str
    required: True
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True
  ip_address:
    description:
    - IP address of the Interface.
    type: str
    required: True
  device_id:
    description:
    - Device ID.
    type: str
    required: True
  records_to_return:
    description:
    - Number of records to return.
    type: int
    required: True
  start_index:
    description:
    - Start index.
    type: int
    required: True
  name:
    description:
    - Interface name.
    type: str
    required: True
  isis:
    description:
    - Specifies that the Interface is isis.
    type: bool
    required: True
  ospf:
    description:
    - Specifies that the Interface is ospf.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.interface
# Reference by Internet resource
- name: Interface reference
  description: Complete reference of the Interface object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Interface reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_all_interfaces
  cisco.dnac.interface:
    state: query  # required
    limit: 1  #  number
    offset: 1  #  number
  register: query_result

- name: get_interface_by_id
  cisco.dnac.interface:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result

- name: get_device_interface_count
  cisco.dnac.interface:
    state: query  # required
    count: True  # boolean, required
  register: query_result

- name: get_interface_by_ip
  cisco.dnac.interface:
    state: query  # required
    ip_address: SomeValue  # string, required
  register: query_result

- name: get_interface_info_by_id
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
  register: query_result

- name: get_device_interfaces_by_specified_range
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
    records_to_return: 1  #  integer, required
    start_index: 1  #  integer, required
  register: query_result

- name: get_device_interface_count_by_id
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
    count: True  # boolean, required
  register: query_result

- name: get_interface_details
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
    name: SomeValue  # string, required
  register: query_result

- name: get_isis_interfaces
  cisco.dnac.interface:
    state: query  # required
    isis: True  # boolean, required
  register: query_result

- name: get_ospf_interfaces
  cisco.dnac.interface:
    state: query  # required
    ospf: True  # boolean, required
  register: query_result

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
  type: array
  sample:
"""

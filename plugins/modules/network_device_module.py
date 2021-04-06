#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_module
short_description: Manage NetworkDeviceModule objects of Devices
description:
- Returns modules by specified device id.
- Returns Module info by id.
- Returns Module Count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_id:
    description:
    - DeviceId query parameter.
    type: str
    required: True
  limit:
    description:
    - Limit query parameter.
    type: str
  name_list:
    description:
    - NameList query parameter.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: str
  operational_state_code_list:
    description:
    - OperationalStateCodeList query parameter.
    type: str
  part_number_list:
    description:
    - PartNumberList query parameter.
    type: str
  vendor_equipment_type_list:
    description:
    - VendorEquipmentTypeList query parameter.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
    required: True
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_module
# Reference by Internet resource
- name: NetworkDeviceModule reference
  description: Complete reference of the NetworkDeviceModule object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceModule reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_modules
  cisco.dnac.network_device_module:
    state: query  # required
    device_id: SomeValue  # string, required
    limit: SomeValue  # string
    name_list: SomeValue  # string
    offset: SomeValue  # string
    operational_state_code_list: SomeValue  # string
    part_number_list: SomeValue  # string
    vendor_equipment_type_list: SomeValue  # string
  register: query_result

- name: get_module_info_by_id
  cisco.dnac.network_device_module:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result

- name: get_module_count
  cisco.dnac.network_device_module:
    state: query  # required
    device_id: SomeValue  # string, required
    count: True  # boolean, required
    name_list: SomeValue  # string
    operational_state_code_list: SomeValue  # string
    part_number_list: SomeValue  # string
    vendor_equipment_type_list: SomeValue  # string
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

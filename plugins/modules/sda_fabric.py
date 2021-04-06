#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric
short_description: Manage SdaFabric objects of Sda
description:
- Get SDA Fabric Info.
- Delete SDA Fabric.
- Add SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  fabric_name:
    description:
    - Fabric Name.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      fabricName:
        description:
        - It is the sda fabric's fabricName.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_fabric
# Reference by Internet resource
- name: SdaFabric reference
  description: Complete reference of the SdaFabric object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaFabric reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_sda_fabric_info
  cisco.dnac.sda_fabric:
    state: query  # required
    fabric_name: SomeValue  # string, required
  register: query_result

- name: delete_sda_fabric
  cisco.dnac.sda_fabric:
    state: delete  # required
    fabric_name: SomeValue  # string, required

- name: add_fabric
  cisco.dnac.sda_fabric:
    state: create  # required
    payload:  # required
    - fabricName: SomeValue  # string

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

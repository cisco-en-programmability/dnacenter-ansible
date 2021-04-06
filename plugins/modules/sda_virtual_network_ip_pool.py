#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_virtual_network_ip_pool
short_description: Manage SdaVirtualNetworkIpPool objects of Sda
description:
- Delete IP Pool from SDA Virtual Network.
- Get IP Pool from SDA Virtual Network.
- Add IP Pool in SDA Virtual Network.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  ip_pool_name:
    description:
    - IpPoolName query parameter.
    type: str
    required: True
  virtual_network_name:
    description:
    - VirtualNetworkName query parameter.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      virtualNetworkName:
        description:
        - It is the sda virtual network ip pool's virtualNetworkName.
        type: str
      ipPoolName:
        description:
        - It is the sda virtual network ip pool's ipPoolName.
        type: str
      trafficType:
        description:
        - It is the sda virtual network ip pool's trafficType.
        type: str
      authenticationPolicyName:
        description:
        - It is the sda virtual network ip pool's authenticationPolicyName.
        type: str
      scalableGroupName:
        description:
        - It is the sda virtual network ip pool's scalableGroupName.
        type: str
      isL2FloodingEnabled:
        description:
        - It is the sda virtual network ip pool's isL2FloodingEnabled.
        type: bool
      isThisCriticalPool:
        description:
        - It is the sda virtual network ip pool's isThisCriticalPool.
        type: bool
      poolType:
        description:
        - It is the sda virtual network ip pool's poolType.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_virtual_network_ip_pool
# Reference by Internet resource
- name: SdaVirtualNetworkIpPool reference
  description: Complete reference of the SdaVirtualNetworkIpPool object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaVirtualNetworkIpPool reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_ip_pool_from_sda_virtual_network
  cisco.dnac.sda_virtual_network_ip_pool:
    state: delete  # required
    ip_pool_name: SomeValue  # string, required
    virtual_network_name: SomeValue  # string, required

- name: get_ip_pool_from_sda_virtual_network
  cisco.dnac.sda_virtual_network_ip_pool:
    state: query  # required
    ip_pool_name: SomeValue  # string, required
    virtual_network_name: SomeValue  # string, required
  register: query_result

- name: add_ip_pool_in_sda_virtual_network
  cisco.dnac.sda_virtual_network_ip_pool:
    state: create  # required
    payload:  # required
    - virtualNetworkName: SomeValue  # string
      ipPoolName: SomeValue  # string
      trafficType: SomeValue  # string
      authenticationPolicyName: SomeValue  # string
      scalableGroupName: SomeValue  # string
      isL2FloodingEnabled: True  # boolean
      isThisCriticalPool: True  # boolean
      poolType: SomeValue  # string

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

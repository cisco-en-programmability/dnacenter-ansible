#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_unclaim
short_description: Manage PnpDeviceUnclaim objects of DeviceOnboardingPnp
description:
- Un-Claims one of more devices with specified workflow.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceIdList:
    description:
    - UnclaimRequest's deviceIdList (list of strings).
    type: list

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_unclaim
# Reference by Internet resource
- name: PnpDeviceUnclaim reference
  description: Complete reference of the PnpDeviceUnclaim object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceUnclaim reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: un_claim_device
  cisco.dnac.pnp_device_unclaim:
    state: create  # required
    deviceIdList:
    - SomeValue  # string

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
  sample: device_onboarding_pnp.un_claim_device
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

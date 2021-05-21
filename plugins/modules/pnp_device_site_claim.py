#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: pnp_device_site_claim
short_description: Manage PnpDeviceSiteClaim objects of DeviceOnboardingPnp
description:
- >
   Claim a device based on DNA-C Site based design process. Different parameters are required for different device
   platforms.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceId:
    description:
    - SiteProvisionRequest's deviceId.
    type: str
  siteId:
    description:
    - SiteProvisionRequest's siteId.
    type: str
  type:
    description:
    - SiteProvisionRequest's type.
    - Available values are 'Default', 'AccessPoint', 'StackSwitch', 'Sensor' and 'MobilityExpress'.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_site_claim
# Reference by Internet resource
- name: PnpDeviceSiteClaim reference
  description: Complete reference of the PnpDeviceSiteClaim object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceSiteClaim reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: claim_a_device_to_a_site
  cisco.dnac.pnp_device_site_claim:
    state: create  # required
    deviceId: SomeValue  # string
    siteId: SomeValue  # string
    type: # valid values are 'Default',
      # 'AccessPoint',
      # 'StackSwitch',
      # 'Sensor',
      # 'MobilityExpress'.
      SomeValue  # string

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
  sample: device_onboarding_pnp.claim_a_device_to_a_site
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

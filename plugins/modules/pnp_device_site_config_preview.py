#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_site_config_preview
short_description: Manage PnpDeviceSiteConfigPreview objects of DeviceOnboardingPnp
description:
- Triggers a preview for site-based Day 0 Configuration.
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
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_site_config_preview
# Reference by Internet resource
- name: PnpDeviceSiteConfigPreview reference
  description: Complete reference of the PnpDeviceSiteConfigPreview object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceSiteConfigPreview reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: preview_config
  cisco.dnac.pnp_device_site_config_preview:
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
  sample: device_onboarding_pnp.preview_config
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

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

RETURN = """
un_claim_device:
    description: Un-Claims one of more devices with specified workflow.
    returned: success
    type: dict
    contains:
    jsonArrayResponse:
      description: UnclaimRequest's Json Array Response (list of any objects).
      returned: success
      type: list
    jsonResponse:
      description: UnclaimRequest's Json Response.
      returned: success
      type: dict
    message:
      description: UnclaimRequest's Message.
      returned: success
      type: str
      sample: '<message>'
    statusCode:
      description: UnclaimRequest's statusCode.
      returned: success
      type: int
      sample: 0

"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: pnp_device_reset
short_description: Manage PnpDeviceReset objects of DeviceOnboardingPnp
description:
- Recovers a device from a Workflow Execution Error state.
version_added: '1.0'
author: first last (@GitHubID)
options:
  deviceResetList:
    description:
    - ResetRequest's deviceResetList (list of objects).
    type: list
    elements: dict
    suboptions:
      configList:
        description:
        - It is the pnp device reset's configList.
        type: list
        elements: dict
        suboptions:
          configId:
            description:
            - It is the pnp device reset's configId.
            type: str
          configParameters:
            description:
            - It is the pnp device reset's configParameters.
            type: list
            elements: dict
            suboptions:
              key:
                description:
                - It is the pnp device reset's key.
                type: str
              value:
                description:
                - It is the pnp device reset's value.
                type: str


      deviceId:
        description:
        - It is the pnp device reset's deviceId.
        type: str
      licenseLevel:
        description:
        - It is the pnp device reset's licenseLevel.
        type: str
      licenseType:
        description:
        - It is the pnp device reset's licenseType.
        type: str
      topOfStackSerialNumber:
        description:
        - It is the pnp device reset's topOfStackSerialNumber.
        type: str

  projectId:
    description:
    - ResetRequest's projectId.
    type: str
  workflowId:
    description:
    - ResetRequest's workflowId.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_reset
# Reference by Internet resource
- name: PnpDeviceReset reference
  description: Complete reference of the PnpDeviceReset object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceReset reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: reset_device
  cisco.dnac.pnp_device_reset:
    state: create  # required
    deviceResetList:
    - configList:
      - configId: SomeValue  # string
        configParameters:
        - key: SomeValue  # string
          value: SomeValue  # string
      deviceId: SomeValue  # string
      licenseLevel: SomeValue  # string
      licenseType: SomeValue  # string
      topOfStackSerialNumber: SomeValue  # string
    projectId: SomeValue  # string
    workflowId: SomeValue  # string
  
"""

RETURN = """
reset_device:
    description: Recovers a device from a Workflow Execution Error state.
    returned: success
    type: dict
    contains:
    jsonArrayResponse:
      description: ResetRequest's Json Array Response (list of any objects).
      returned: success
      type: list
    jsonResponse:
      description: ResetRequest's Json Response.
      returned: success
      type: dict
    message:
      description: ResetRequest's Message.
      returned: success
      type: str
      sample: '<message>'
    statusCode:
      description: ResetRequest's statusCode.
      returned: success
      type: int
      sample: 0

"""

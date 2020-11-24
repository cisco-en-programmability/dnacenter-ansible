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
module: pnp_device_claim
short_description: Manage PnpDeviceClaim objects of DeviceOnboardingPnp
description:
- Claims one of more devices with specified workflow.
version_added: '1.0'
author: first last (@GitHubID)
options:
  configFileUrl:
    description:
    - ClaimDeviceRequest's configFileUrl.
    type: str
  configId:
    description:
    - ClaimDeviceRequest's configId.
    type: str
  deviceClaimList:
    description:
    - ClaimDeviceRequest's deviceClaimList (list of objects).
    type: list
    elements: dict
    suboptions:
      configList:
        description:
        - It is the pnp device claim's configList.
        type: list
        elements: dict
        suboptions:
          configId:
            description:
            - It is the pnp device claim's configId.
            type: str
          configParameters:
            description:
            - It is the pnp device claim's configParameters.
            type: list
            elements: dict
            suboptions:
              key:
                description:
                - It is the pnp device claim's key.
                type: str
              value:
                description:
                - It is the pnp device claim's value.
                type: str


      deviceId:
        description:
        - It is the pnp device claim's deviceId.
        type: str
      licenseLevel:
        description:
        - It is the pnp device claim's licenseLevel.
        type: str
      licenseType:
        description:
        - It is the pnp device claim's licenseType.
        type: str
      topOfStackSerialNumber:
        description:
        - It is the pnp device claim's topOfStackSerialNumber.
        type: str

  fileServiceId:
    description:
    - ClaimDeviceRequest's fileServiceId.
    type: str
  imageId:
    description:
    - ClaimDeviceRequest's imageId.
    type: str
  imageUrl:
    description:
    - ClaimDeviceRequest's imageUrl.
    type: str
  populateInventory:
    description:
    - ClaimDeviceRequest's populateInventory.
    type: bool
  projectId:
    description:
    - ClaimDeviceRequest's projectId.
    type: str
  workflowId:
    description:
    - ClaimDeviceRequest's workflowId.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_claim
# Reference by Internet resource
- name: PnpDeviceClaim reference
  description: Complete reference of the PnpDeviceClaim object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceClaim reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: claim_device
  cisco.dnac.pnp_device_claim
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    configFileUrl: SomeValue  # string
    configId: SomeValue  # string
    deviceClaimList:
    - configList:
      - configId: SomeValue  # string
        configParameters:
        - key: SomeValue  # string
          value: SomeValue  # string
      deviceId: SomeValue  # string
      licenseLevel: SomeValue  # string
      licenseType: SomeValue  # string
      topOfStackSerialNumber: SomeValue  # string
    fileServiceId: SomeValue  # string
    imageId: SomeValue  # string
    imageUrl: SomeValue  # string
    populateInventory: True  # boolean
    projectId: SomeValue  # string
    workflowId: SomeValue  # string
  delegate_to: localhost
  
"""

RETURN = """
claim_device:
    description: Claims one of more devices with specified workflow.
    returned: success
    type: dict
    contains:
    jsonArrayResponse:
      description: ClaimDeviceRequest's Json Array Response (list of any objects).
      returned: success
      type: list
    jsonResponse:
      description: ClaimDeviceRequest's Json Response.
      returned: success
      type: dict
    message:
      description: ClaimDeviceRequest's Message.
      returned: success
      type: str
      sample: '<message>'
    statusCode:
      description: ClaimDeviceRequest's statusCode.
      returned: success
      type: int
      sample: 0

"""

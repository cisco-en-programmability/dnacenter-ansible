#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_device_create
short_description: Resource module for Wireless Provision Device Create
description:
- Manage operation create of the resource Wireless Provision Device Create.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Wireless Provision Device Create's payload.
    suboptions:
      deviceName:
        description: Wireless Provision Device Create's deviceName.
        type: str
      dynamicInterfaces:
        description: Wireless Provision Device Create's dynamicInterfaces.
        suboptions:
          interfaceGateway:
            description: Wireless Provision Device Create's interfaceGateway.
            type: str
          interfaceIPAddress:
            description: Wireless Provision Device Create's interfaceIPAddress.
            type: str
          interfaceName:
            description: Wireless Provision Device Create's interfaceName.
            type: str
          interfaceNetmaskInCIDR:
            description: Wireless Provision Device Create's interfaceNetmaskInCIDR.
            type: int
          lagOrPortNumber:
            description: Wireless Provision Device Create's lagOrPortNumber.
            type: int
          vlanId:
            description: Wireless Provision Device Create's vlanId.
            type: int
        type: list
      managedAPLocations:
        description: Wireless Provision Device Create's managedAPLocations.
        elements: str
        type: list
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Provision Device Create reference
  description: Complete reference of the Wireless Provision Device Create object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.wireless_provision_device_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"

- name: Create
  cisco.dnac.wireless_provision_device_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionUrl": "string",
      "provisioningTasks": {
        "success": [
          "string"
        ],
        "failed": [
          "string"
        ]
      }
    }
"""

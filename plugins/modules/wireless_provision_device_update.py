#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_device_update
short_description: Resource module for Wireless Provision Device Update
description:
- Manage operation update of the resource Wireless Provision Device Update.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Wireless Provision Device Update's payload.
    suboptions:
      deviceName:
        description: Wireless Provision Device Update's deviceName.
        type: str
      dynamicInterfaces:
        description: Wireless Provision Device Update's dynamicInterfaces.
        suboptions:
          interfaceGateway:
            description: Wireless Provision Device Update's interfaceGateway.
            type: str
          interfaceIPAddress:
            description: Wireless Provision Device Update's interfaceIPAddress.
            type: str
          interfaceName:
            description: Wireless Provision Device Update's interfaceName.
            type: str
          interfaceNetmaskInCIDR:
            description: Wireless Provision Device Update's interfaceNetmaskInCIDR.
            type: int
          lagOrPortNumber:
            description: Wireless Provision Device Update's lagOrPortNumber.
            type: int
          vlanId:
            description: Wireless Provision Device Update's vlanId.
            type: int
        type: list
      managedAPLocations:
        description: Wireless Provision Device Update's managedAPLocations.
        elements: str
        type: list
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Provision Device Update reference
  description: Complete reference of the Wireless Provision Device Update object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.wireless_provision_device_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"

- name: Create
  cisco.dnac.wireless_provision_device_update:
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

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
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Wireless Provision Device Create's payload.
    suboptions:
      deviceName:
        description: Device Name.
        type: str
      dynamicInterfaces:
        description: Wireless Provision Device Create's dynamicInterfaces.
        suboptions:
          interfaceGateway:
            description: Interface Gateway.
            type: str
          interfaceIPAddress:
            description: Interface IPAddress.
            type: str
          interfaceName:
            description: Interface Name.
            type: str
          interfaceNetmaskInCIDR:
            description: Interface Netmask In CIDR.
            type: int
          lagOrPortNumber:
            description: Lag Or Port Number.
            type: int
          vlanId:
            description: Vlan Id.
            type: int
        type: list
      managedAPLocations:
        description: Managed APLocations.
        elements: str
        type: list
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Wireless Provision Device Create reference
  description: Complete reference of the Wireless Provision Device Create object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
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

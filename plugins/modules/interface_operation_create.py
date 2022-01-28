#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface_operation_create
short_description: Resource module for Interface Operation Create
description:
- Manage operation create of the resource Interface Operation Create.
version_added: '4.4.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deployementMode:
    description: DeployementMode query parameter. Preview/Deploy 'Preview' means the
      configuration is not pushed to the device. 'Deploy' makes the configuration pushed
      to the device.
    type: str
  interfaceUuid:
    description: InterfaceUuid path parameter. Interface Id.
    type: str
  operation:
    description: Operation.
    type: str
  payload:
    description: Payload.
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Interface Operation Create reference
  description: Complete reference of the Interface Operation Create object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.interface_operation_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deployementMode: string
    interfaceUuid: string
    operation: string
    payload: {}

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

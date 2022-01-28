#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface_update
short_description: Resource module for Interface Update
description:
- Manage operation update of the resource Interface Update.
version_added: '4.4.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  adminStatus:
    description: Interface Update's adminStatus.
    suboptions:
      type:
        description: Type.
        type: str
    type: dict
  deploymentMode:
    description: DeploymentMode query parameter. Preview/Deploy 'Preview' means the
      configuration is not pushed to the device. 'Deploy' makes the configuration pushed
      to the device.
    type: str
  description:
    description: Interface Update's description.
    suboptions:
      type:
        description: Type.
        type: str
    type: dict
  interfaceUuid:
    description: InterfaceUuid path parameter. Interface ID.
    type: str
  vlanId:
    description: Interface Update's vlanId.
    suboptions:
      type:
        description: Type.
        type: str
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Interface Update reference
  description: Complete reference of the Interface Update object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.dnac.interface_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    adminStatus:
      type: string
    deploymentMode: string
    description:
      type: string
    interfaceUuid: string
    vlanId:
      type: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "type": "string",
        "properties": {
          "taskId": "string",
          "url": {
            "type": "string"
          }
        },
        "required": [
          "string"
        ]
      },
      "version": {
        "type": "string"
      }
    }
"""

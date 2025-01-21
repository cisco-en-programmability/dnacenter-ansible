#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: interface_update
short_description: Resource module for Interface Update
description:
- This module represents an alias of the module interface_update_v1
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  adminStatus:
    description: Admin status as ('UP'/'DOWN').
    type: str
  deploymentMode:
    description: DeploymentMode query parameter. Preview/Deploy 'Preview' means the
      configuration is not pushed to the device. 'Deploy' makes the configuration pushed
      to the device.
    type: str
  description:
    description: Description for the Interface.
    type: str
  interfaceUuid:
    description: InterfaceUuid path parameter. Interface ID.
    type: str
  vlanId:
    description: VLAN Id to be Updated.
    type: int
  voiceVlanId:
    description: Voice Vlan Id to be Updated.
    type: int
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices UpdateInterfaceDetailsV1
  description: Complete reference of the UpdateInterfaceDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-interface-details
notes:
  - SDK Method used are
    devices.Devices.update_interface_details_v1,

  - Paths used are
    put /dna/intent/api/v1/interface/{interfaceUuid},
  - It should be noted that this module is an alias of interface_update_v1

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
    adminStatus: string
    deploymentMode: string
    description: string
    interfaceUuid: string
    vlanId: 0
    voiceVlanId: 0

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
          "taskId": {
            "type": "string"
          },
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

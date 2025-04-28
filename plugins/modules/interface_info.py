#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: interface_info
short_description: Information module for Interface Info
description:
  - This module represents an alias of the module interface_v1_info
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  interfaceUuid:
    description:
      - InterfaceUuid path parameter. Interface ID.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices LegitOperationsForInterfaceV1
    description: Complete reference of the LegitOperationsForInterfaceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!legit-operations-for-interface
notes:
  - SDK Method used are devices.Devices.legit_operations_for_interface_v1,
  - Paths used are get /dna/intent/api/v1/interface/{interfaceUuid}/legit-operation,
  - It should be noted that this module is an alias of interface_v1_info
"""
EXAMPLES = r"""
- name: Get all Interface Info
  cisco.dnac.interface_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    interfaceUuid: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "interfaceUuid": "string",
        "properties": [
          {
            "name": "string",
            "applicable": "string",
            "failureReason": "string"
          }
        ],
        "operations": [
          {
            "name": "string",
            "applicable": "string",
            "failureReason": "string"
          }
        ]
      },
      "version": "string"
    }
"""

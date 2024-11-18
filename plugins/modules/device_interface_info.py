#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: device_interface_info
short_description: Information module for Device Interface Info
description:
- This module represents an alias of the module device_interface_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter.
    type: int
  limit:
    description:
    - Limit query parameter.
    type: int
  lastInputTime:
    description:
    - LastInputTime query parameter. Last Input Time.
    type: str
  lastOutputTime:
    description:
    - LastOutputTime query parameter. Last Output Time.
    type: str
  id:
    description:
    - Id path parameter. Interface ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetAllInterfacesV1
  description: Complete reference of the GetAllInterfacesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-interfaces-v-1
- name: Cisco DNA Center documentation for Devices GetInterfaceByIdV1
  description: Complete reference of the GetInterfaceByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-interface-by-id-v-1
notes:
  - SDK Method used are
    devices.Devices.get_all_interfaces_v1,
    devices.Devices.get_interface_by_id_v1,

  - Paths used are
    get /dna/intent/api/v1/interface,
    get /dna/intent/api/v1/interface/{id},
  - It should be noted that this module is an alias of device_interface_v1_info

"""

EXAMPLES = r"""
- name: Get all Device Interface Info
  cisco.dnac.device_interface_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    lastInputTime: string
    lastOutputTime: string
  register: result

- name: Get Device Interface Info by id
  cisco.dnac.device_interface_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of device_interface_v1_info.
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessSettings_interfaces_info
short_description: Information module for Wirelesssettings Interfaces
description:
- Get all Wirelesssettings Interfaces.
- Get Wirelesssettings Interfaces by id.
- This API allows the user to get all Interfaces.
- This API allows the user to get an interface by ID.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - Limit query parameter.
    type: float
  offset:
    description:
    - Offset query parameter.
    type: float
  id:
    description:
    - Id path parameter. Interface ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetInterfaceByID
  description: Complete reference of the GetInterfaceByID API.
  link: https://developer.cisco.com/docs/dna-center/#!get-interface-by-id
- name: Cisco DNA Center documentation for Wireless GetInterfaces
  description: Complete reference of the GetInterfaces API.
  link: https://developer.cisco.com/docs/dna-center/#!get-interfaces
notes:
  - SDK Method used are
    wireless.Wireless.get_interface_by_id,
    wireless.Wireless.get_interfaces,

  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/interfaces,
    get /dna/intent/api/v1/wirelessSettings/interfaces/{id},

"""

EXAMPLES = r"""
- name: Get all Wirelesssettings Interfaces
  cisco.dnac.wirelessSettings_interfaces_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
  register: result

- name: Get Wirelesssettings Interfaces by id
  cisco.dnac.wirelessSettings_interfaces_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "interfaceName": "string",
        "vlanId": 0,
        "id": "string"
      },
      "version": "string"
    }
"""

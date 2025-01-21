#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_dynamic_interface_info
short_description: Information module for Wireless Dynamic Interface Info
description:
- This module represents an alias of the module wireless_dynamic_interface_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  interface_name:
    description:
    - >
      Interface-name query parameter. Dynamic-interface name, if not specified all the existing dynamic interfaces
      will be retrieved.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetDynamicInterfaceV1
  description: Complete reference of the GetDynamicInterfaceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-dynamic-interface
notes:
  - SDK Method used are
    wireless.Wireless.get_dynamic_interface_v1,

  - Paths used are
    get /dna/intent/api/v1/wireless/dynamic-interface,
  - It should be noted that this module is an alias of wireless_dynamic_interface_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Dynamic Interface Info
  cisco.dnac.wireless_dynamic_interface_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    interface_name: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "interfaceName": "string",
        "vlanId": 0
      }
    ]
"""

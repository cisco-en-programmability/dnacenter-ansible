#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: client_detail_info
short_description: Information module for Client Detail Info
description:
- This module represents an alias of the module client_detail_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  macAddress:
    description:
    - MacAddress query parameter. MAC Address of the client.
    type: str
  timestamp:
    description:
    - Timestamp query parameter. Epoch time(in milliseconds) when the Client health data is required.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Clients GetClientDetailV1
  description: Complete reference of the GetClientDetailV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-client-detail-v-1
notes:
  - SDK Method used are
    clients.Clients.get_client_detail_v1,

  - Paths used are
    get /dna/intent/api/v1/client-detail,
  - It should be noted that this module is an alias of client_detail_v1_info

"""

EXAMPLES = r"""
- name: Get all Client Detail Info
  cisco.dnac.client_detail_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    macAddress: string
    timestamp: 0
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of client_detail_v1_info.
"""

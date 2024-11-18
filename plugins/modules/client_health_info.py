#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: client_health_info
short_description: Information module for Client Health Info
description:
- This module represents an alias of the module client_health_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  timestamp:
    description:
    - Timestamp query parameter. Epoch time(in milliseconds) when the Client health data is required.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Clients GetOverallClientHealthV1
  description: Complete reference of the GetOverallClientHealthV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-overall-client-health-v-1
notes:
  - SDK Method used are
    clients.Clients.get_overall_client_health_v1,

  - Paths used are
    get /dna/intent/api/v1/client-health,
  - It should be noted that this module is an alias of client_health_v1_info

"""

EXAMPLES = r"""
- name: Get all Client Health Info
  cisco.dnac.client_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    timestamp: 0
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of client_health_v1_info.
"""

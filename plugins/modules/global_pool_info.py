#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: global_pool_info
short_description: Information module for Global Pool Info
description:
- This module represents an alias of the module global_pool_v1_info
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
    - Offset query parameter. Offset/starting row. Indexed from 1. Default value of 1.
    type: float
  limit:
    description:
    - Limit query parameter. Number of Global Pools to be retrieved. Default is 25 if not specified.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings GetGlobalPoolV1
  description: Complete reference of the GetGlobalPoolV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-global-pool-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_global_pool_v1,

  - Paths used are
    get /dna/intent/api/v1/global-pool,
  - It should be noted that this module is an alias of global_pool_v1_info

"""

EXAMPLES = r"""
- name: Get all Global Pool Info
  cisco.dnac.global_pool_info:
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
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of global_pool_v1_info.
"""

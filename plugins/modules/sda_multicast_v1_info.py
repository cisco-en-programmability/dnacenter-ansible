#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_multicast_v1_info
short_description: Information module for Sda Multicast V1
description:
  - Get all Sda Multicast V1.
  - Returns a list of multicast configurations at a fabric site level that match the provided query parameters.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
      - FabricId query parameter. ID of the fabric site where multicast is configured.
    type: str
  offset:
    description:
      - Offset query parameter. Starting record for pagination.
    type: int
  limit:
    description:
      - >
        Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
        single request is 500.
    type: int
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for SDA GetMulticast
    description: Complete reference of the GetMulticast API.
    link: https://developer.cisco.com/docs/dna-center/#!get-multicast
notes:
  - SDK Method used are
    sda.Sda.get_multicast,
  - Paths used are
    get /dna/intent/api/v1/sda/multicast,
"""

EXAMPLES = r"""
---
- name: Get all Sda Multicast V1
  cisco.dnac.sda_multicast_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "fabricId": "string",
          "replicationMode": "string"
        }
      ],
      "version": "string"
    }
"""

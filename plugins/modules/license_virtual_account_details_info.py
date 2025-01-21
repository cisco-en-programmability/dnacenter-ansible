#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: license_virtual_account_details_info
short_description: Information module for License Virtual Account Details Info
description:
- This module represents an alias of the module license_virtual_account_details_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  smart_account_id:
    description:
    - Smart_account_id path parameter. Id of smart account.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses VirtualAccountDetailsV1
  description: Complete reference of the VirtualAccountDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!virtual-account-details
notes:
  - SDK Method used are
    licenses.Licenses.virtual_account_details_v1,

  - Paths used are
    get /dna/intent/api/v1/licenses/smartAccount/{smart_account_id}/virtualAccounts,
  - It should be noted that this module is an alias of license_virtual_account_details_v1_info

"""

EXAMPLES = r"""
- name: Get all License Virtual Account Details Info
  cisco.dnac.license_virtual_account_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    smart_account_id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "smart_account_id": "string",
      "smart_account_name": "string",
      "virtual_account_details": [
        {
          "virtual_account_id": "string",
          "virtual_account_name": "string"
        }
      ]
    }
"""

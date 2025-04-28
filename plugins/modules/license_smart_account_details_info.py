#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_smart_account_details_info
short_description: Information module for License Smart Account Details Info
description:
  - This module represents an alias of the module license_smart_account_details_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses SmartAccountDetailsV1
    description: Complete reference of the SmartAccountDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!smart-account-details
notes:
  - SDK Method used are licenses.Licenses.smart_account_details_v1,
  - Paths used are get /dna/intent/api/v1/licenses/smartAccounts,
  - It should be noted that this module is an alias of license_smart_account_details_v1_info
"""
EXAMPLES = r"""
- name: Get all License Smart Account Details Info
  cisco.dnac.license_smart_account_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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
          "name": "string",
          "id": "string",
          "domain": "string",
          "is_active_smart_account": true
        }
      ],
      "version": "string"
    }
"""

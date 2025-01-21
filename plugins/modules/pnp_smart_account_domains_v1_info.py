#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_smart_account_domains_v1_info
short_description: Information module for Pnp Smart Account Domains V1
description:
- Get all Pnp Smart Account Domains V1.
- Returns the list of Smart Account domains.
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
- name: Cisco DNA Center documentation for Device Onboarding (PnP) GetSmartAccountListV1
  description: Complete reference of the GetSmartAccountListV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-smart-account-list
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_smart_account_list_v1,

  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-settings/sacct,

"""

EXAMPLES = r"""
- name: Get all Pnp Smart Account Domains V1
  cisco.dnac.pnp_smart_account_domains_v1_info:
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
  type: list
  elements: str
  sample: >
    [
      "string"
    ]
"""

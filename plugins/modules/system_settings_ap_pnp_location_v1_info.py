#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: system_settings_ap_pnp_location_v1_info
short_description: Information module for System Settings Ap Pnp Location V1
description:
  - Get all System Settings Ap Pnp Location V1.
  - >
    Retrieve the current AP PnP Location setting from the system.Once the AP PnP Location
    Setting is enabled, the
    Access Point's assigned Site name will be configured as the AP Location during
    the PnP Claim process. This applies
    only during the PnP onboarding process and not during any subsequent provisioning
    dayN .
version_added: '6.18.0'
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
  - name: Cisco DNA Center documentation for Wireless GetAPPnPLocationSettingV1
    description: Complete reference of the GetAPPnPLocationSettingV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ap-pn-p-location-setting
notes:
  - SDK Method used are wireless.Wireless.get_ap_pnp_location_setting_v1,
  - Paths used are get /dna/intent/api/v1/systemSettings/apPnpLocation,
"""
EXAMPLES = r"""
- name: Get all System Settings Ap Pnp Location V1
  cisco.dnac.system_settings_ap_pnp_location_v1_info:
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
  type: str
  sample: >
    "string"
"""

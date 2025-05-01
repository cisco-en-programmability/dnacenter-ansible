#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: floors_settings_info
short_description: Information module for Floors Settings Info
description:
  - This module represents an alias of the module floors_settings_v2_info
version_added: '6.15.0'
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
  - name: Cisco DNA Center documentation for Site Design GetFloorSettingsV2
    description: Complete reference of the GetFloorSettingsV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-floor-settings
notes:
  - SDK Method used are site_design.SiteDesign.get_floor_settings_v2,
  - Paths used are get /dna/intent/api/v2/floors/settings,
  - It should be noted that this module is an alias of floors_settings_v2_info
"""
EXAMPLES = r"""
- name: Get all Floors Settings Info
  cisco.dnac.floors_settings_info:
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
      "response": {
        "unitsOfMeasure": "string"
      },
      "version": "string"
    }
"""

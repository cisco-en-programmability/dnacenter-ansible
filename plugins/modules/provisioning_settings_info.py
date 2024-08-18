#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: provisioningSettings_info
short_description: Information module for Provisioningsettings
description:
- Get all Provisioningsettings.
- Returns provisioning settings.
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
- name: Cisco DNA Center documentation for System Settings GetProvisioningSettings
  description: Complete reference of the GetProvisioningSettings API.
  link: https://developer.cisco.com/docs/dna-center/#!get-provisioning-settings
notes:
  - SDK Method used are
    system_settings.SystemSettings.get_provisioning_settings,

  - Paths used are
    get /dna/intent/api/v1/provisioningSettings,

"""

EXAMPLES = r"""
- name: Get all Provisioningsettings
  cisco.dnac.provisioningSettings_info:
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
        "requireItsmApproval": true,
        "requirePreview": true
      },
      "version": "string"
    }
"""

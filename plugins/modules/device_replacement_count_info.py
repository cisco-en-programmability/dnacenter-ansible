#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: device_replacement_count_info
short_description: Information module for Device Replacement Count Info
description:
  - This module represents an alias of the module device_replacement_count_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  replacementStatus:
    description:
      - >
        ReplacementStatus query parameter. Device Replacement status listREADY-FOR-REPLACEMENT,
        REPLACEMENT-IN-
        PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Replacement ReturnReplacementDevicesCountV1
    description: Complete reference of the ReturnReplacementDevicesCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!return-replacement-devices-count
notes:
  - SDK Method used are device_replacement.DeviceReplacement.return_replacement_devices_count_v1,
  - Paths used are get /dna/intent/api/v1/device-replacement/count,
  - It should be noted that this module is an alias of device_replacement_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Device Replacement Count Info
  cisco.dnac.device_replacement_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    replacementStatus: []
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""

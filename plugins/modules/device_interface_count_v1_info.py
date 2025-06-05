#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: device_interface_count_v1_info
short_description: Information module for Device Interface Count V1
description:
  - Get all Device Interface Count V1.
  - Returns the count of interfaces for all devices.
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
  - name: Cisco DNA Center documentation for Devices GetDeviceInterfaceCountForMultipleDevicesV1
    description: Complete reference of the GetDeviceInterfaceCountForMultipleDevicesV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-device-interface-count-for-multiple-devices
notes:
  - SDK Method used are devices.Devices.get_device_interface_count,
  - Paths used are get /dna/intent/api/v1/interface/count,
"""
EXAMPLES = r"""
- name: Get all Device Interface Count V1
  cisco.dnac.device_interface_count_v1_info:
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
      "response": 0,
      "version": "string"
    }
"""

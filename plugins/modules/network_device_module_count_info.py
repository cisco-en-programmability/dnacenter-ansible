#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_module_count_info
short_description: Information module for Network Device Module Count Info
description:
  - This module represents an alias of the module network_device_module_count_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
      - DeviceId query parameter.
    type: str
  nameList:
    description:
      - NameList query parameter.
    elements: str
    type: list
  vendorEquipmentTypeList:
    description:
      - VendorEquipmentTypeList query parameter.
    elements: str
    type: list
  partNumberList:
    description:
      - PartNumberList query parameter.
    elements: str
    type: list
  operationalStateCodeList:
    description:
      - OperationalStateCodeList query parameter.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetModuleCountV1
    description: Complete reference of the GetModuleCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-module-count
notes:
  - SDK Method used are devices.Devices.get_module_count_v1,
  - Paths used are get /dna/intent/api/v1/network-device/module/count,
  - It should be noted that this module is an alias of network_device_module_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Device Module Count Info
  cisco.dnac.network_device_module_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
    nameList: []
    vendorEquipmentTypeList: []
    partNumberList: []
    operationalStateCodeList: []
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

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabric_devices_layer2_handoffs_count_info
short_description: Information module for Sda Fabric Devices Layer2 Handoffs Count
  Info
description:
  - This module represents an alias of the module sda_fabric_devices_layer2_handoffs_count_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
      - FabricId query parameter. ID of the fabric this device belongs to.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId query parameter. Network device ID of the fabric device.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetFabricDevicesLayer2HandoffsCountV1
    description: Complete reference of the GetFabricDevicesLayer2HandoffsCountV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer-2-handoffs-count
notes:
  - SDK Method used are sda.Sda.get_fabric_devices_layer2_handoffs_count_v1,
  - Paths used are get /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/count,
  - It should be noted that this module is an alias of sda_fabric_devices_layer2_handoffs_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Sda Fabric Devices Layer2 Handoffs Count Info
  cisco.dnac.sda_fabric_devices_layer2_handoffs_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    networkDeviceId: string
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
        "count": 0
      },
      "version": "string"
    }
"""

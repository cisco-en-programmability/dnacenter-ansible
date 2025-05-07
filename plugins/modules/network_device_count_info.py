#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_count_info
short_description: Information module for Network Device Count Info
description:
  - This module represents an alias of the module network_device_count_v1_info
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
      - DeviceId path parameter. Device ID.
    type: str
  hostname:
    description:
      - Hostname query parameter.
    elements: str
    type: list
  managementIpAddress:
    description:
      - ManagementIpAddress query parameter.
    elements: str
    type: list
  macAddress:
    description:
      - MacAddress query parameter.
    elements: str
    type: list
  locationName:
    description:
      - LocationName query parameter.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetDeviceCountKnowYourNetworkV1
    description: Complete reference of the GetDeviceCountKnowYourNetworkV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-count-know-your-network
  - name: Cisco DNA Center documentation for Devices GetDeviceInterfaceCountV1
    description: Complete reference of the GetDeviceInterfaceCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-interface-count
notes:
  - SDK Method used are devices.Devices.get_device_count, devices.Devices.get_device_interface_count_by_id,
  - Paths used are get /dna/intent/api/v1/interface/network-device/{deviceId}/count,
    get /dna/intent/api/v1/network-device/count,
  - It should be noted that this module is an alias of network_device_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Device Count Info
  cisco.dnac.network_device_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    hostname: []
    managementIpAddress: []
    macAddress: []
    locationName: []
  register: result
- name: Get Network Device Count Info by id
  cisco.dnac.network_device_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
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

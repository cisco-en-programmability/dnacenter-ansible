#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_module_v1_info
short_description: Information module for Network Device Module V1
description:
  - Get all Network Device Module V1.
  - Get Network Device Module V1 by id.
  - Returns Module info by 'module id'.
  - Returns modules by specified device id.
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
  limit:
    description:
      - Limit query parameter. The number of records to show for this page. Min 1,
        Max 500.
    type: int
  offset:
    description:
      - Offset query parameter.
    type: int
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
  id:
    description:
      - Id path parameter. Module id.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetModuleInfoByIdV1
    description: Complete reference of the GetModuleInfoByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-module-info-by-id
  - name: Cisco DNA Center documentation for Devices GetModulesV1
    description: Complete reference of the GetModulesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-modules
notes:
  - SDK Method used are devices.Devices.get_module_info_by_id_v1, devices.Devices.get_modules_v1,
  - Paths used are get /dna/intent/api/v1/network-device/module, get /dna/intent/api/v1/network-device/module/{id},
"""
EXAMPLES = r"""
- name: Get all Network Device Module V1
  cisco.dnac.network_device_module_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
    limit: 0
    offset: 0
    nameList: []
    vendorEquipmentTypeList: []
    partNumberList: []
    operationalStateCodeList: []
  register: result
- name: Get Network Device Module V1 by id
  cisco.dnac.network_device_module_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "assemblyNumber": "string",
        "assemblyRevision": "string",
        "attributeInfo": {},
        "containmentEntity": "string",
        "description": "string",
        "entityPhysicalIndex": "string",
        "id": "string",
        "isFieldReplaceable": "string",
        "isReportingAlarmsAllowed": "string",
        "manufacturer": "string",
        "moduleIndex": 0,
        "name": "string",
        "operationalStateCode": "string",
        "partNumber": "string",
        "serialNumber": "string",
        "vendorEquipmentType": "string"
      },
      "version": "string"
    }
"""

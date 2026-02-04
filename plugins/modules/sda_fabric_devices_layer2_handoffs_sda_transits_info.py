#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_devices_layer2_handoffs_sda_transits_info
short_description: Information module for Sda Fabric Devices Layer2 Handoffs Sda Transits
description:
  - Get all Sda Fabric Devices Layer2 Handoffs Sda Transits.
  - Returns a list of layer 3 handoffs with sda transit of fabric devices that match the provided query parameters.
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
  offset:
    description:
      - Offset query parameter. Starting record for pagination.
    type: int
  limit:
    description:
      - >
        Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
        single request is 500.
    type: int
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for SDA GetFabricDevicesLayer3HandoffsWithSdaTransit
    description: Complete reference of the GetFabricDevicesLayer3HandoffsWithSdaTransit API.
    link: https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer-3-handoffs-with-sda-transit
notes:
  - SDK Method used are
    sda.Sda.get_fabric_devices_layer3_handoffs_with_sda_transit,
  - Paths used are
    get /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits,
"""

EXAMPLES = r"""
---
- name: Get all Sda Fabric Devices Layer2 Handoffs Sda Transits
  cisco.dnac.sda_fabric_devices_layer2_handoffs_sda_transits_info:
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
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "siteId": "string",
          "type": "string",
          "ipTransitSettings": {
            "routingProtocolName": "string",
            "autonomousSystemNumber": "string"
          },
          "sdaTransitSettings": {
            "isMulticastOverTransitEnabled": true,
            "controlPlaneNetworkDeviceIds": [
              "string"
            ]
          }
        }
      ],
      "version": "string"
    }
"""

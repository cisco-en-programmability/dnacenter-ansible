#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_images_validations_info
short_description: Information module for Network Device Images Validations Info
description:
  - This module represents an alias of the module network_device_images_validations_v1_info
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  productSeriesOrdinal:
    description:
      - ProductSeriesOrdinal query parameter. Unique identifier of product series.
    type: float
  operationType:
    description:
      - >
        OperationType query parameter. The operation type, as part of which this validation
        will get triggered.
        Available values DISTRIBUTION, ACTIVATION.
    type: str
  type:
    description:
      - Type query parameter. Type of the validation. Available values PRE_VALIDATION,
        POST_VALIDATION.
    type: str
  order:
    description:
      - >
        Order query parameter. Whether ascending or descending order should be used
        to sort the response. Available
        values asc, desc.
    type: str
  offset:
    description:
      - >
        Offset query parameter. The first record to show for this page; the first
        record is numbered 1. The minimum
        value is 1.
    type: float
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. The minimum
        and maximum values are 1 and
        500, respectively.
    type: float
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) GetTheListOfCustomNetworkDeviceValidationsV1
    description: Complete reference of the GetTheListOfCustomNetworkDeviceValidationsV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-the-list-of-custom-network-device-validations
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.get_the_list_of_custom_network_device_validations_v1,
  - Paths used are get /dna/intent/api/v1/networkDeviceImages/validations,
  - It should be noted that this module is an alias of network_device_images_validations_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Device Images Validations Info
  cisco.dnac.network_device_images_validations_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    productSeriesOrdinal: 0
    operationType: string
    type: string
    order: string
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
          "type": "string",
          "operationType": "string",
          "description": "string",
          "category": "string",
          "cli": "string",
          "productSeriesOrdinals": [
            0
          ]
        }
      ],
      "version": "string"
    }
"""

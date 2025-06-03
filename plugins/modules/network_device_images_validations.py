#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_images_validations
short_description: Resource module for Network Device Images Validations
description:
  - This module represents an alias of the module network_device_images_validations_v1
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  cli:
    description: Show commands that will be executed. Validate the CLI - Cisco DevNet
      https
      //developer.cisco.com/docs/dna-center/2-3-7/run-read-only-commands-on-devices-to-get-their-real-time-co...
    type: str
  description:
    description: Details of the network device validation.
    type: str
  name:
    description: Name of the network device validation.
    type: str
  operationType:
    description: The operation type, as part of which this validation will get triggered.
    type: str
  productSeriesOrdinals:
    description: The custom check will be mapped to the product series and devices
      that belong to this series. These devices will consume this check when triggered.
      Fetch productSeriesOrdinal from API `/dna/intent/api/v1/productSeries`.
    elements: float
    type: list
  type:
    description: The type of network device validation determines whether this validation
      runs before or after the operation.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) CreateCustomNetworkDeviceValidationV1
    description: Complete reference of the CreateCustomNetworkDeviceValidationV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!create-custom-network-device-validation
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.create_custom_network_device_validation_v1,
  - Paths used are post /dna/intent/api/v1/networkDeviceImages/validations,
  - It should be noted that this module is an alias of network_device_images_validations_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.network_device_images_validations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cli: string
    description: string
    name: string
    operationType: string
    productSeriesOrdinals:
      - 0
    type: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

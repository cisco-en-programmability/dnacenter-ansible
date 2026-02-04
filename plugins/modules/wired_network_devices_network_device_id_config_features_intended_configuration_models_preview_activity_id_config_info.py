#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wired_network_devices_network_device_id_config_features_intended_configuration_models_preview_activity_id_config_info
short_description: Information module for Wired Network Devices Network Device Id Config Features Intended Configuration Models
  Preview Activity Id Config
description:
  - Get Wired Network Devices Network Device Id Config Features Intended Configuration Models Preview Config by id.
  - Gets the device config for the configuration model. This API is 'Step 3' in the workflow.
  - Step 1 Use POST configurationModels to start provision, response has taskId as previewActivityId.
  - Step 2 Use POST config to generate device CLIs for preview.
  - Step 3 Use GET config to view the CLIs that will be applied to the device.
  - Step 4 Use POST deploy to deploy the intent to the device.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Network device ID of the wired device to provision. The API
        /intent/api/v1/network-device can be used to get the network device ID.
    type: str
  previewActivityId:
    description:
      - >
        PreviewActivityId path parameter. Activity id is the taskId from Step 2- 'POST /intent/api/v1/wired/netw
        orkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}/networkDevi
        ces/{networkDeviceId}/config.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wired GetsTheDeviceConfigForTheConfigurationModel
    description: Complete reference of the GetsTheDeviceConfigForTheConfigurationModel API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-the-device-config-for-the-configuration-model
notes:
  - SDK Method used are
    wired.Wired.gets_the_device_config_for_the_configuration_model,
  - Paths used are
    get /dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}/config,
"""

EXAMPLES = r"""
---
- name: Get Wired Network Devices Network Device Id Config Features Intended Configuration Models Preview Activity Id Config
    by id
  cisco.dnac.wired_network_devices_network_device_id_config_features_intended_configuration_models_preview_activity_id_config_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
    previewActivityId: string
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
        "networkDeviceId": "string",
        "status": "string",
        "previewItems": [
          {
            "name": "string",
            "configType": "string",
            "configPreview": "string",
            "errorMessages": [
              "string"
            ]
          }
        ]
      },
      "version": "string"
    }
"""

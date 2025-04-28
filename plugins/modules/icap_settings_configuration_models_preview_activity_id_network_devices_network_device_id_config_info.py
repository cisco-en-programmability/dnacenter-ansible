#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module:
  icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_info
short_description: Information module for Icap Settings Configuration Models Preview
  Activity Id Network Devices Network Device Id Config Info                                                                                     # noqa: E501
description:
  - This module represents an alias of the module
    icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1_info                                              # noqa: E501
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  previewActivityId:
    description:
      - PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels
        task response.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Device id from intent/api/v1/network-device.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors RetrievesTheDevice'sCLIsOfTheICAPIntentV1
    description: Complete reference of the RetrievesTheDevice'sCLIsOfTheICAPIntentV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-device's-cl-is-of-the-icap-intent
notes:
  - SDK Method used are sensors.Sensors.retrieves_the_devices_clis_of_the_i_capintent_v1,
  - Paths used are get
    /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
  - It should be noted that this module is an alias of
    icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1_info                                                     # noqa: E501
"""
EXAMPLES = r"""
- name: Get Icap Settings Configuration Models Preview Activity Id Network Devices
    Network Device Id Config Info by id
  cisco.dnac.icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    previewActivityId: string
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
        "networkDeviceId": "string",
        "previewItems": [
          {
            "configPreview": "string",
            "configType": "string",
            "errorMessages": [
              "string"
            ],
            "name": "string"
          }
        ],
        "status": "string"
      },
      "version": "string"
    }
"""

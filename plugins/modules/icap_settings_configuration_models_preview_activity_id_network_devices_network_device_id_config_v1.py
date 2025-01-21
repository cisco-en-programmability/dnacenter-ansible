#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1
short_description: Resource module for Icap Settings Configuration Models Preview Activity Id Network Devices Network Device Id Config V1
description:
- Manage operation create of the resource Icap Settings Configuration Models Preview Activity Id Network Devices Network Device Id Config V1.  # noqa: E501
- >
   Generates the device's CLIs of the ICAP intent for preview and approve prior to deploying the ICAP configuration
   intent to the device. After deploying the configuration intent, generating intent CLIs will not be available for
   preview.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  networkDeviceId:
    description: NetworkDeviceId path parameter. Device id from intent/api/v1/network-device.
    type: str
  object:
    description: Object.
    type: str
  previewActivityId:
    description: PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels
      task response.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors GeneratesTheDevice'sCLIsOfTheICAPConfigurationIntentV1
  description: Complete reference of the GeneratesTheDevice'sCLIsOfTheICAPConfigurationIntentV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!generates-the-device's-cl-is-of-the-icap-configuration-intent
notes:
  - SDK Method used are
    sensors.Sensors.generates_the_devices_clis_of_the_i_cap_configuration_intent_v1,

  - Paths used are
    post /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    networkDeviceId: string
    object: string
    previewActivityId: string

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

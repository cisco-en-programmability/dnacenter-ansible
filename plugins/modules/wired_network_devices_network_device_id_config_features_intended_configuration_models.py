#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wired_network_devices_network_device_id_config_features_intended_configuration_models
short_description: Resource module for Wired Network Devices Network Device Id Config Features Intended Configuration Models
description:
  - Manage operation create of the resource Wired Network Devices Configuration Models.
  - Create a configuration model for the intended configs for a wired device.
  - This is a pre-requisite to preview the generated device config for the provisioning intent.
  - This is mandatory if the provisioning settings require Preview or ITSM Approval before deploying.
  - This API is 'Step 1' in the workflow.
  - Step 1 Use POST configurationModels to start provision, response has taskId as previewActivityId.
  - Step 2 Use POST config to generate device CLIs for preview.
  - Step 3 Use GET config to view the CLIs that will be applied to the device.
  - Step 4 Use POST deploy to deploy the intent to the device.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wired device to provision. The API /intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wired CreateAConfigurationModelForTheIntendedConfigsForAWiredDevice
    description: Complete reference of the CreateAConfigurationModelForTheIntendedConfigsForAWiredDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-configuration-model-for-the-intended-configs-for-a-wired-device
notes:
  - SDK Method used are
    wired.Wired.create_a_configuration_model_for_the_intended_configs_for_a_wired_device,
  - Paths used are
    post /dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.wired_network_devices_network_device_id_config_features_intended_configuration_models:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    networkDeviceId: string
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

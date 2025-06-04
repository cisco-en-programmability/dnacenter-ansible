#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: create_wired_network_devices_id_config_features_intended_layer2
short_description: Resource module for Create Wired Network Devices Id Config Features
  Intended Layer2
description:
  - This module represents an alias of the module create_wired_network_devices_id_config_features_intended_layer2_v1
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Network device ID of the wired device to configure.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wired CreateConfigurationsForIntendedLayer2FeaturesOnAWiredDeviceV1
    description: Complete reference of the CreateConfigurationsForIntendedLayer2FeaturesOnAWiredDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!create-configurations-for-intended-layer-2-features-on-a-wired-device
notes:
  - SDK Method used are
    wired.Wired.create_configurations_for_intended_layer2_features_on_a_wired_device_v1,
  - Paths used are post /dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2,
  - It should be noted that this module is an alias of create_wired_network_devices_id_config_features_intended_layer2_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.create_wired_network_devices_id_config_features_intended_layer2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string
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

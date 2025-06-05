#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_device_controllability_settings
short_description: Resource module for Network Devices Device Controllability Settings
description:
  - This module represents an alias of the module network_devices_device_controllability_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  autocorrectTelemetryConfig:
    description: If it is true, autocorrect telemetry config is enabled. If it is
      false, autocorrect telemetry config is disabled. The autocorrect telemetry config
      feature is supported only when device controllability is enabled.
    type: bool
  deviceControllability:
    description: If it is true, device controllability is enabled. If it is false,
      device controllability is disabled.
    type: bool
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design UpdateDeviceControllabilitySettingsV1
    description: Complete reference of the UpdateDeviceControllabilitySettingsV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-device-controllability-settings
notes:
  - SDK Method used are site_design.SiteDesign.update_device_controllability_settings_v1,
  - Paths used are put /dna/intent/api/v1/networkDevices/deviceControllability/settings,
  - It should be noted that this module is an alias of network_devices_device_controllability_settings_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.dnac.network_devices_device_controllability_settings:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    autocorrectTelemetryConfig: true
    deviceControllability: true
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: telemetry_settings_apply_v1
short_description: Resource module for Telemetry Settings Apply V1
description:
  - Manage operation create of the resource Telemetry Settings Apply V1.
  - >
    Update a devices telemetry settings to conform to the telemetry settings for its
    site. One Task is created to
    track the update, for more granular status tracking, split your devices into multiple
    requests.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIds:
    description: The list of device Ids to perform the provisioning against.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings UpdateADevicesTelemetrySettingsToConformToTheTelemetrySettingsForItsSiteV1
    description: Complete reference of the UpdateADevicesTelemetrySettingsToConformToTheTelemetrySettingsForItsSiteV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-a-devices-telemetry-settings-to-conform-to-the-telemetry-settings-for-its-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1,
  - Paths used are post /dna/intent/api/v1/telemetrySettings/apply,
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.telemetry_settings_apply_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceIds:
      - string
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

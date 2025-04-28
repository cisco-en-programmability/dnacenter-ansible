#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_resync_interval_settings_override
short_description: Resource module for Network Devices Resync Interval Settings Override
description:
  - This module represents an alias of the module network_devices_resync_interval_settings_override_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices OverrideResyncIntervalV1
    description: Complete reference of the OverrideResyncIntervalV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!override-resync-interval
notes:
  - SDK Method used are devices.Devices.override_resync_interval_v1,
  - Paths used are post /dna/intent/api/v1/networkDevices/resyncIntervalSettings/override,
  - It should be noted that this module is an alias of network_devices_resync_interval_settings_override_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.network_devices_resync_interval_settings_override:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
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

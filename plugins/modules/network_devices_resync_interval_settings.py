#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_resync_interval_settings
short_description: Resource module for Network Devices Resync Interval Settings
description:
  - This module represents an alias of the module network_devices_resync_interval_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  interval:
    description: Resync Interval should be between 25 to 1440 minutes.
    type: int
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices UpdateGlobalResyncIntervalV1
    description: Complete reference of the UpdateGlobalResyncIntervalV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-global-resync-interval
notes:
  - SDK Method used are devices.Devices.update_global_resync_interval_v1,
  - Paths used are put /dna/intent/api/v1/networkDevices/resyncIntervalSettings,
  - It should be noted that this module is an alias of network_devices_resync_interval_settings_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.dnac.network_devices_resync_interval_settings:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    interval: 0
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

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: pnp_device_config_preview
short_description: Resource module for Pnp Device Config Preview
description:
  - This module represents an alias of the module pnp_device_config_preview_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceId:
    description: Pnp Device Config Preview's deviceId.
    type: str
  siteId:
    description: Pnp Device Config Preview's siteId.
    type: str
  type:
    description: Pnp Device Config Preview's type.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) PreviewConfigV1
    description: Complete reference of the PreviewConfigV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!preview-config
notes:
  - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.preview_config_v1,
  - Paths used are post /dna/intent/api/v1/onboarding/pnp-device/site-config-preview,
  - It should be noted that this module is an alias of pnp_device_config_preview_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.pnp_device_config_preview:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    siteId: string
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
        "complete": true,
        "config": "string",
        "error": true,
        "errorMessage": "string",
        "expiredTime": 0,
        "rfProfile": "string",
        "sensorProfile": "string",
        "siteId": "string",
        "startTime": 0,
        "taskId": "string"
      },
      "version": "string"
    }
"""

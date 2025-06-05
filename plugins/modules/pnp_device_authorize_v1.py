#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: pnp_device_authorize_v1
short_description: Resource module for Pnp Device Authorize V1
description:
  - Manage operation create of the resource Pnp Device Authorize V1.
  - Authorizes one of more devices. A device can only be authorized if Authorization
    is set in Device Settings.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIdList:
    description: Device Id List.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) AuthorizeDeviceV1
    description: Complete reference of the AuthorizeDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!authorize-device
notes:
  - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.authorize_device_v1,
  - Paths used are post /api/v1/onboarding/pnp-device/authorize,
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.pnp_device_authorize_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceIdList:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "jsonResponse": {
        "empty": true
      },
      "message": "string",
      "statusCode": 0,
      "jsonArrayResponse": [
        "string"
      ]
    }
"""

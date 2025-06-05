#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: pnp_device_reset_v1
short_description: Resource module for Pnp Device Reset V1
description:
  - Manage operation create of the resource Pnp Device Reset V1.
  - Recovers a device from a Workflow Execution Error state.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceResetList:
    description: Pnp Device Reset's deviceResetList.
    elements: dict
    suboptions:
      configList:
        description: Pnp Device Reset's configList.
        elements: dict
        suboptions:
          configId:
            description: Pnp Device Reset's configId.
            type: str
          configParameters:
            description: Pnp Device Reset's configParameters.
            elements: dict
            suboptions:
              key:
                description: Pnp Device Reset's key.
                type: str
              value:
                description: Pnp Device Reset's value.
                type: str
            type: list
        type: list
      deviceId:
        description: Pnp Device Reset's deviceId.
        type: str
      licenseLevel:
        description: Pnp Device Reset's licenseLevel.
        type: str
      licenseType:
        description: Pnp Device Reset's licenseType.
        type: str
      topOfStackSerialNumber:
        description: Pnp Device Reset's topOfStackSerialNumber.
        type: str
    type: list
  projectId:
    description: Pnp Device Reset's projectId.
    type: str
  workflowId:
    description: Pnp Device Reset's workflowId.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) ResetDeviceV1
    description: Complete reference of the ResetDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!reset-device
notes:
  - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.reset_device_v1,
  - Paths used are post /dna/intent/api/v1/onboarding/pnp-device/reset,
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.pnp_device_reset_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceResetList:
      - configList:
          - configId: string
            configParameters:
              - key: string
                value: string
        deviceId: string
        licenseLevel: string
        licenseType: string
        topOfStackSerialNumber: string
    projectId: string
    workflowId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "jsonArrayResponse": [
        {}
      ],
      "jsonResponse": {},
      "message": "string",
      "statusCode": 0
    }
"""

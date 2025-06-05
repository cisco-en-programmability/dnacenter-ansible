#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: pnp_global_settings_info
short_description: Information module for Pnp Global Settings Info
description:
  - This module represents an alias of the module pnp_global_settings_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) GetPnPGlobalSettingsV1
    description: Complete reference of the GetPnPGlobalSettingsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-pn-p-global-settings
notes:
  - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.get_pnp_global_settings_v1,
  - Paths used are get /dna/intent/api/v1/onboarding/pnp-settings,
  - It should be noted that this module is an alias of pnp_global_settings_v1_info
"""
EXAMPLES = r"""
- name: Get all Pnp Global Settings Info
  cisco.dnac.pnp_global_settings_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "savaMappingList": [
        {
          "syncStatus": "string",
          "syncStartTime": 0,
          "syncResult": {
            "syncList": [
              {
                "syncType": "string",
                "deviceSnList": [
                  "string"
                ]
              }
            ],
            "syncMsg": "string"
          },
          "lastSync": 0,
          "tenantId": "string",
          "profile": {
            "port": 0,
            "addressIpV4": "string",
            "addressFqdn": "string",
            "profileId": "string",
            "proxy": true,
            "makeDefault": true,
            "cert": "string",
            "name": "string"
          },
          "token": "string",
          "expiry": 0,
          "ccoUser": "string",
          "smartAccountId": "string",
          "virtualAccountId": "string",
          "autoSyncPeriod": 0,
          "syncResultStr": "string"
        }
      ],
      "taskTimeOuts": {
        "imageDownloadTimeOut": 0,
        "configTimeOut": 0,
        "generalTimeOut": 0
      },
      "tenantId": "string",
      "aaaCredentials": {
        "password": "string",
        "username": "string"
      },
      "defaultProfile": {
        "fqdnAddresses": [
          "string"
        ],
        "proxy": true,
        "cert": "string",
        "ipAddresses": [
          "string"
        ],
        "port": 0
      },
      "acceptEula": true,
      "id": "string",
      "version": 0
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_rf_profile_info
short_description: Information module for Wireless Rf Profile
description:
- Get all Wireless Rf Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  rf_profile_name:
    description:
    - Rf-profile-name query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Rf Profile reference
  description: Complete reference of the Wireless Rf Profile object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Wireless Rf Profile
  cisco.dnac.wireless_rf_profile_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    rf_profile_name: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "name": "string",
        "parentProfileA": "string",
        "parentProfileB": "string",
        "enableARadioType": true,
        "enableBRadioType": true,
        "channelWidth": "string",
        "aRadioChannels": "string",
        "bRadioChannels": "string",
        "dataRatesA": "string",
        "dataRatesB": "string",
        "mandatoryDataRatesA": "string",
        "mandatoryDataRatesB": "string",
        "enableCustom": true,
        "minPowerLevelA": "string",
        "minPowerLevelB": "string",
        "maxPowerLevelA": "string",
        "maxPowerLevelB": "string",
        "powerThresholdV1A": 0,
        "powerThresholdV1B": 0,
        "rxSopThresholdA": "string",
        "rxSopThresholdB": "string",
        "defaultRfProfile": true,
        "enableBrownField": true
      }
    ]
"""

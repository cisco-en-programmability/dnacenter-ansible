#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: enterprise_ssid
short_description: Manage EnterpriseSsid objects of Wireless
description:
- Gets either one or all the enterprise SSID.
- Creates enterprise SSID.
- Deletes given enterprise SSID.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  ssid_name:
    description:
    - >
       Enter the enterprise SSID name that needs to be retrieved. If not entered, all the enterprise SSIDs will
       be retrieved.
    - Enter the SSID name to be deleted.
    - Required for state delete.
    type: str
  enableBroadcastSSID:
    description:
    - EnableBroadcastSSID, property of the request body.
    type: bool
  enableFastLane:
    description:
    - EnableFastLane, property of the request body.
    type: bool
  enableMACFiltering:
    description:
    - EnableMACFiltering, property of the request body.
    type: bool
  fastTransition:
    description:
    - Fast Transition, property of the request body.
    - Available values are 'Adaptive', 'Enable' and 'Disable'.
    type: str
  name:
    description:
    - Enter SSID Name, property of the request body. Constraint is maxLength set to 32.
    - Required for state create.
    type: str
  passphrase:
    description:
    - >
       Pass Phrase (Only applicable for SSID with PERSONAL security level), property of the request body.
       Constraints are maxLength set to 63 and minLength set to 8.
    type: str
  radioPolicy:
    description:
    - Radio Policy, property of the request body.
    - >
       Available values are 'Dual band operation (2.4GHz and 5GHz)', 'Dual band operation with band select',
       '5GHz only' and '2.4GHz only'.
    type: str
  securityLevel:
    description:
    - Security Level, property of the request body.
    - Available values are 'WPA2_ENTERPRISE', 'WPA2_PERSONAL' and 'OPEN'.
    - Required for state create.
    type: str
  trafficType:
    description:
    - Traffic Type, property of the request body.
    - Available values are 'voicedata' and 'data'.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.enterprise_ssid
# Reference by Internet resource
- name: EnterpriseSsid reference
  description: Complete reference of the EnterpriseSsid object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EnterpriseSsid reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_enterprise_ssid
  cisco.dnac.enterprise_ssid:
    state: query  # required
    ssid_name: SomeValue  # string
  register: nm_get_enterprise_ssid

- name: create_enterprise_ssid
  cisco.dnac.enterprise_ssid:
    state: create  # required
    name: SomeValue  # string, required
    securityLevel: # valid values are 'WPA2_ENTERPRISE',
      # 'WPA2_PERSONAL',
      # 'OPEN'.
      SomeValue  # string, required
    enableBroadcastSSID: True  # boolean
    enableFastLane: True  # boolean
    enableMACFiltering: True  # boolean
    fastTransition: # valid values are 'Adaptive',
      # 'Enable',
      # 'Disable'.
      SomeValue  # string
    passphrase: SomeValue  # string
    radioPolicy: # valid values are 'Dual band operation (2.4GHz and 5GHz)',
      # 'Dual band operation with band select',
      # '5GHz only',
      # '2.4GHz only'.
      SomeValue  # string
    trafficType: # valid values are 'voicedata',
      # 'data'.
      SomeValue  # string

- name: delete_enterprise_ssid
  cisco.dnac.enterprise_ssid:
    state: delete  # required
    ssid_name: SomeValue  # string, required

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: wireless.create_enterprise_ssid
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

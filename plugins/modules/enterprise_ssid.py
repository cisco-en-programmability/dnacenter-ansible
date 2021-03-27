#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

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
    - Enter the enterprise SSID name that needs to be retrieved. If not entered, all the enterprise SSIDs will be retrieved.
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
    - Enter SSID Name, property of the request body. Constraints: maxLength set to 32.
    - Required for state create.
    type: str
  passphrase:
    description:
    - Pass Phrase (Only applicable for SSID with PERSONAL security level), property of the request body. Constraints: maxLength set to 63 and minLength set to 8.
    type: str
  radioPolicy:
    description:
    - Radio Policy, property of the request body.
    - Available values are 'Dual band operation (2.4GHz and 5GHz)', 'Dual band operation with band select', '5GHz only' and '2.4GHz only'.
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
  register: query_result

- name: create_enterprise_ssid
  cisco.dnac.enterprise_ssid:
    state: create  # required
    name: SomeValue  # string, required
    securityLevel: SomeValue  # string, required, valid values: 'WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN'.
    enableBroadcastSSID: True  # boolean
    enableFastLane: True  # boolean
    enableMACFiltering: True  # boolean
    fastTransition: SomeValue  # string, valid values: 'Adaptive', 'Enable', 'Disable'.
    passphrase: SomeValue  # string
    radioPolicy: SomeValue  # string, valid values: 'Dual band operation (2.4GHz and 5GHz)', 'Dual band operation with band select', '5GHz only', '2.4GHz only'.
    trafficType: SomeValue  # string, valid values: 'voicedata', 'data'.

- name: delete_enterprise_ssid
  cisco.dnac.enterprise_ssid:
    state: delete  # required
    ssid_name: SomeValue  # string, required

"""

RETURN = """
"""

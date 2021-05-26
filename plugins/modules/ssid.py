#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ssid
short_description: Manage Ssid objects of Wireless
description:
- >
   Creates SSID, updates the SSID to the corresponding site profiles and provision it to the devices matching the
   given sites.
- Removes SSID or WLAN from the network profile, reprovision the device(s) and deletes the SSID or WLAN from DNA Center.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  enableFabric:
    description:
    - EnableFabric, property of the request body.
    - Required for state create.
    type: bool
  flexConnect:
    description:
    - Flex Connect - Applicable for non fabric profile, property of the request body.
    type: dict
    suboptions:
      enableFlexConnect:
        description:
        - It is the Ssid's enableFlexConnect.
        type: bool
      localToVlan:
        description:
        - It is the Ssid's localToVlan.
        type: int

  managedAPLocations:
    description:
    - Managed AP Locations (Enter entire Site(s) hierarchy), property of the request body (list of strings).
    - Required for state create.
    type: list
  ssidDetails:
    description:
    - SsidDetails, property of the request body.
    - Required for state create.
    type: dict
    suboptions:
      name:
        description:
        - It is the Ssid's name.
        type: str
      securityLevel:
        description:
        - It is the Ssid's securityLevel.
        type: str
      enableFastLane:
        description:
        - It is the Ssid's enableFastLane.
        type: bool
      passphrase:
        description:
        - It is the Ssid's passphrase.
        type: str
      trafficType:
        description:
        - It is the Ssid's trafficType.
        type: str
      enableBroadcastSSID:
        description:
        - It is the Ssid's enableBroadcastSSID.
        type: bool
      radioPolicy:
        description:
        - It is the Ssid's radioPolicy.
        type: str
      enableMACFiltering:
        description:
        - It is the Ssid's enableMACFiltering.
        type: bool
      fastTransition:
        description:
        - It is the Ssid's fastTransition.
        type: str
      webAuthURL:
        description:
        - It is the Ssid's webAuthURL.
        type: str

  ssidType:
    description:
    - SSID Type, property of the request body.
    - Available values are 'Guest' and 'Enterprise'.
    - Required for state create.
    type: str
  managed_aplocations:
    description:
    - ManagedAPLocations path parameter.
    - Required for state delete.
    type: str
  ssid_name:
    description:
    - SsidName path parameter.
    - Required for state delete.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.ssid
# Reference by Internet resource
- name: Ssid reference
  description: Complete reference of the Ssid object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Ssid reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_and_provision_ssid
  cisco.dnac.ssid:
    state: create  # required
    enableFabric: True  # boolean, required
    managedAPLocations:  # required
    - SomeValue  # string
    ssidDetails:  # required
      name: SomeValue  # string
      securityLevel: SomeValue  # string
      enableFastLane: True  # boolean
      passphrase: SomeValue  # string
      trafficType: SomeValue  # string
      enableBroadcastSSID: True  # boolean
      radioPolicy: SomeValue  # string
      enableMACFiltering: True  # boolean
      fastTransition: SomeValue  # string
      webAuthURL: SomeValue  # string
    ssidType: # valid values are 'Guest',
      # 'Enterprise'.
      SomeValue  # string, required
    flexConnect:
      enableFlexConnect: True  # boolean
      localToVlan: 1  #  integer

- name: delete_ssid_and_provision_it_to_devices
  cisco.dnac.ssid:
    state: delete  # required
    managed_aplocations: SomeValue  # string, required
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
  sample: wireless.create_and_provision_ssid
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

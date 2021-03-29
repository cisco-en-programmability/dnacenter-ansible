#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profile
short_description: Manage WirelessProfile objects of Wireless
description:
- Gets either one or all the wireless network profiles if no name is provided for network-profile.
- Creates Wireless Network Profile on DNAC and associates sites and SSIDs to it.
- Updates the wireless Network Profile with updated details provided. All sites to be present in the network profile should be provided.
- Delete the Wireless Profile from DNAC whose name is provided.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  profile_name:
    description:
    - ProfileName query parameter.
    type: str
  profileDetails:
    description:
    - Profile Details, property of the request body.
    type: dict
    required: True
    suboptions:
      name:
        description:
        - It is the wireless profile's name.
        type: str
      sites:
        description:
        - It is the wireless profile's sites.
        type: list
      ssidDetails:
        description:
        - It is the wireless profile's ssidDetails.
        type: list
        elements: dict
        suboptions:
          enableFabric:
            description:
            - It is the wireless profile's enableFabric.
            type: bool
          flexConnect:
            description:
            - It is the wireless profile's flexConnect.
            type: dict
            suboptions:
              enableFlexConnect:
                description:
                - It is the wireless profile's enableFlexConnect.
                type: bool
              localToVlan:
                description:
                - It is the wireless profile's localToVlan.
                type: int

          interfaceName:
            description:
            - It is the wireless profile's interfaceName.
            type: str
          name:
            description:
            - It is the wireless profile's name.
            type: str
          type:
            description:
            - It is the wireless profile's type.
            type: str


  wireless_profile_name:
    description:
    - WirelessProfileName path parameter.
    - Required for state delete.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.wireless_profile
# Reference by Internet resource
- name: WirelessProfile reference
  description: Complete reference of the WirelessProfile object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: WirelessProfile reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_wireless_profile
  cisco.dnac.wireless_profile:
    state: query  # required
    profile_name: SomeValue  # string
  register: query_result

- name: create_wireless_profile
  cisco.dnac.wireless_profile:
    state: create  # required
    profileDetails:  # required
      name: SomeValue  # string
      sites:
      - SomeValue  # string
      ssidDetails:
      - name: SomeValue  # string
        type: SomeValue  # string
        enableFabric: True  # boolean
        flexConnect:
          enableFlexConnect: True  # boolean
          localToVlan: 1  #  integer
        interfaceName: SomeValue  # string

- name: update_wireless_profile
  cisco.dnac.wireless_profile:
    state: update  # required
    profileDetails:  # required
      name: SomeValue  # string
      sites:
      - SomeValue  # string
      ssidDetails:
      - name: SomeValue  # string
        type: SomeValue  # string
        enableFabric: True  # boolean
        flexConnect:
          enableFlexConnect: True  # boolean
          localToVlan: 1  #  integer
        interfaceName: SomeValue  # string

- name: delete_wireless_profile
  cisco.dnac.wireless_profile:
    state: delete  # required
    wireless_profile_name: SomeValue  # string, required

"""

RETURN = """
"""

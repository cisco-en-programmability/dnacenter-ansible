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
module: wireless_profile
short_description: Manage WirelessProfile objects of Wireless
description:
- Gets either one or all the wireless network profiles if no name is provided for network-profile.
- Creates Wireless Network Profile on DNAC and associates sites and SSIDs to it.
- Updates the wireless Network Profile with updated details provided. All sites to be present in the network profile should be provided.
- Delete the Wireless Profile from DNAC whose name is provided.
version_added: '1.0'
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
get_wireless_profile:
    description: Gets either one or all the wireless network profiles if no name is provided for network-profile.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the wireless profile's payload.
      returned: always
      type: list
      contains:
        profileDetails:
          description: It is the wireless profile's profileDetails.
          returned: always
          type: dict
          contains:
            name:
              description: It is the wireless profile's name.
              returned: always
              type: str
              sample: '<name>'
            sites:
              description: It is the wireless profile's sites.
              returned: always
              type: list
            ssidDetails:
              description: It is the wireless profile's ssidDetails.
              returned: always
              type: list
              contains:
                name:
                  description: It is the wireless profile's name.
                  returned: always
                  type: str
                  sample: '<name>'
                type:
                  description: It is the wireless profile's type.
                  returned: always
                  type: str
                  sample: '<type>'
                enableFabric:
                  description: It is the wireless profile's enableFabric.
                  returned: always
                  type: bool
                  sample: false
                flexConnect:
                  description: It is the wireless profile's flexConnect.
                  returned: always
                  type: dict
                  contains:
                    enableFlexConnect:
                      description: It is the wireless profile's enableFlexConnect.
                      returned: always
                      type: bool
                      sample: false
                    localToVlan:
                      description: It is the wireless profile's localToVlan.
                      returned: always
                      type: int
                      sample: 0

                interfaceName:
                  description: It is the wireless profile's interfaceName.
                  returned: always
                  type: str
                  sample: '<interfacename>'




create_wireless_profile:
    description: Creates Wireless Network Profile on DNAC and associates sites and SSIDs to it.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

update_wireless_profile:
    description: Updates the wireless Network Profile with updated details provided. All sites to be present in the network profile should be provided.
    returned: changed
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: changed
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: changed
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: changed
      type: str
      sample: '<message>'

delete_wireless_profile:
    description: Delete the Wireless Profile from DNAC whose name is provided.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

"""

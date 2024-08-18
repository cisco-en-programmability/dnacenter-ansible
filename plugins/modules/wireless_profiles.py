#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessProfiles
short_description: Resource module for Wirelessprofiles
description:
- Manage operations create, update and delete of the resource Wirelessprofiles.
- This API allows the user to create a Wireless Network Profile.
- This API allows the user to delete Wireless Network Profile by ID.
- This API allows the user to update a Wireless Network Profile by ID.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Wireless Profile Id.
    type: str
  ssidDetails:
    description: Wireless Profiles's ssidDetails.
    elements: dict
    suboptions:
      dot11beProfileId:
        description: 802.11be Profile Id. Applicable to IOS controllers with version
          17.15 and higher. 802.11be Profiles if passed, should be same across all SSIDs
          in network profile being configured.
        type: str
      enableFabric:
        description: True if fabric is enabled, else False. Flex and fabric cannot be
          enabled simultaneously and a profile can only contain either flex SSIDs or
          fabric SSIDs and not both at the same time.
        type: bool
      flexConnect:
        description: Wireless Profiles's flexConnect.
        suboptions:
          enableFlexConnect:
            description: True if flex connect is enabled, else False. Flex and fabric
              cannot be enabled simultaneously and a profile can only contain either
              flex SSIDs or fabric SSIDs and not both at the same time.
            type: bool
          localToVlan:
            description: Local to VLAN ID.
            type: int
        type: dict
      interfaceName:
        description: Interface Name. Default Value management.
        type: str
      ssidName:
        description: SSID Name.
        type: str
      wlanProfileName:
        description: WLAN Profile Name.
        type: str
    type: list
  wirelessProfileName:
    description: Wireless Network Profile Name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless CreateWirelessProfile2
  description: Complete reference of the CreateWirelessProfile2 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-wireless-profile-2
- name: Cisco DNA Center documentation for Wireless DeleteWirelessProfile2
  description: Complete reference of the DeleteWirelessProfile2 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-wireless-profile-2
- name: Cisco DNA Center documentation for Wireless UpdateWirelessProfile2
  description: Complete reference of the UpdateWirelessProfile2 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-wireless-profile-2
notes:
  - SDK Method used are
    wireless.Wireless.create_wireless_profile2,
    wireless.Wireless.delete_wireless_profile2,
    wireless.Wireless.update_wireless_profile2,

  - Paths used are
    post /dna/intent/api/v1/wirelessProfiles,
    delete /dna/intent/api/v1/wirelessProfiles/{id},
    put /dna/intent/api/v1/wirelessProfiles/{id},

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wirelessProfiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    ssidDetails:
    - dot11beProfileId: string
      enableFabric: true
      flexConnect:
        enableFlexConnect: true
        localToVlan: 0
      interfaceName: string
      ssidName: string
      wlanProfileName: string
    wirelessProfileName: string

- name: Update by id
  cisco.dnac.wirelessProfiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
    ssidDetails:
    - dot11beProfileId: string
      enableFabric: true
      flexConnect:
        enableFlexConnect: true
        localToVlan: 0
      interfaceName: string
      ssidName: string
      wlanProfileName: string
    wirelessProfileName: string

- name: Delete by id
  cisco.dnac.wirelessProfiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

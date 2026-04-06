#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_dot11be_profiles
short_description: Resource module for Wireless Settings Dot11be Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Settings Dot11be Profiles. - > This API allows the
    user to create a 802.11be Profile.Catalyst Center will push this profile to device's "default-dot11be-profile".Also please
    note , 802.11be Profile is supported only on IOS-XE controllers since device version 17.15. - > This API allows the user
    to delete a 802.11be Profile,if the 802.11be Profile is not mapped to any Wireless Network Profile.
  - This API allows the user to update a 802.11be Profile.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  default:
    description: Specifies whether this 802.11be profile's properties should be set to system default profile on device(default-dot11be-profile)
      or not.When a profile is marked with default as true ,configuration is pushed to device's 'default-dot11be-profile'.
      Note Setting a profile as custom (default=false) on devices with IOS-XE versions below 17.18.1 will result in a provisioning
      failure.
    type: bool
  id:
    description: Id path parameter. 802.11be Profile ID.
    type: str
  mloGroup:
    description: Wireless Settings Dot11be Profiles's mloGroup.
    suboptions:
      primary24GhzEnable:
        description: Indicates if primary 2.4GHz MLO link is enabled.(Default true).
        type: bool
      primary5GhzEnable:
        description: Indicates if primary 5GHz MLO link is enabled.(Default true).
        type: bool
      primary6GhzEnable:
        description: Indicates if primary 6GHz MLO link is enabled.(Default true).
        type: bool
      secondary5GhzEnable:
        description: Indicates if secondary 5GHz MLO link is enabled.(Default true).
        type: bool
    type: dict
  muMimoDownLink:
    description: MU-MIMO Downlink (Default false). This parameter is deprecated in IOS-XE versions 17.18.2 and above and will
      be ignored during provisioning. For IOS-XE version above 17.18.2, use the 802.11ax properties in Advanced SSID Feature
      Template.
    type: bool
  muMimoUpLink:
    description: MU-MIMO Uplink (Default false). This parameter is deprecated in IOS-XE versions 17.18.2 and above and will
      be ignored during provisioning. For IOS-XE version above 17.18.2, use the 802.11ax properties in Advanced SSID Feature
      Template.
    type: bool
  ofdmaDownLink:
    description: OFDMA Downlink (Default true). This parameter is deprecated in IOS-XE versions 17.18.2 and above and will
      be ignored during provisioning. For IOS-XE version above 17.18.2, use the 802.11ax properties in Advanced SSID Feature
      Template.
    type: bool
  ofdmaMultiRu:
    description: OFDMA Multi-RU (Default false).
    type: bool
  ofdmaUpLink:
    description: OFDMA Uplink (Default true). This parameter is deprecated in IOS-XE versions 17.18.2 and above and will be
      ignored during provisioning. For IOS-XE version above 17.18.2, use the 802.11ax properties in Advanced SSID Feature
      Template.
    type: bool
  profileName:
    description: 802.11be Profile Name.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateA80211beProfile
    description: Complete reference of the CreateA80211beProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-80-21-1be-profile
  - name: Cisco DNA Center documentation for Wireless DeleteA80211beProfile
    description: Complete reference of the DeleteA80211beProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-80-21-1be-profile
  - name: Cisco DNA Center documentation for Wireless Update80211beProfile
    description: Complete reference of the Update80211beProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!update-80-21-1be-profile
notes:
  - SDK Method used are
    wireless.Wireless.create_a80211be_profile,
    wireless.Wireless.delete_a80211be_profile,
    wireless.Wireless.update80211be_profile,
  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/dot11beProfiles,
    delete /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
    put /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.wireless_settings_dot11be_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    default: true
    mloGroup:
      primary24GhzEnable: true
      primary5GhzEnable: true
      primary6GhzEnable: true
      secondary5GhzEnable: true
    muMimoDownLink: true
    muMimoUpLink: true
    ofdmaDownLink: true
    ofdmaMultiRu: true
    ofdmaUpLink: true
    profileName: string
- name: Delete by id
  cisco.dnac.wireless_settings_dot11be_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.dnac.wireless_settings_dot11be_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    default: true
    id: string
    mloGroup:
      primary24GhzEnable: true
      primary5GhzEnable: true
      primary6GhzEnable: true
      secondary5GhzEnable: true
    muMimoDownLink: true
    muMimoUpLink: true
    ofdmaDownLink: true
    ofdmaMultiRu: true
    ofdmaUpLink: true
    profileName: string
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

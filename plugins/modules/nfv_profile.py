#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: nfv_profile
short_description: Resource module for Nfv Profile
description:
- Manage operations create, update and delete of the resource Nfv Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device:
    description: Nfv Profile's device.
    suboptions:
      currentDeviceTag:
        description: Nfv Profile's currentDeviceTag.
        type: str
      customNetworks:
        description: Nfv Profile's customNetworks.
        suboptions:
          connectionType:
            description: Nfv Profile's connectionType.
            type: str
          networkName:
            description: Nfv Profile's networkName.
            type: str
          servicesToConnect:
            description: Nfv Profile's servicesToConnect.
            suboptions:
              serviceName:
                description: Nfv Profile's serviceName.
                type: str
            type: list
          vlanId:
            description: Nfv Profile's vlanId.
            type: int
          vlanMode:
            description: Nfv Profile's vlanMode.
            type: str
        type: list
      customTemplate:
        description: Nfv Profile's customTemplate.
        suboptions:
          deviceType:
            description: Nfv Profile's deviceType.
            type: str
          template:
            description: Nfv Profile's template.
            type: str
          templateType:
            description: Nfv Profile's templateType.
            type: str
        type: list
      deviceTag:
        description: Nfv Profile's deviceTag.
        type: str
      directInternetAccessForFirewall:
        description: DirectInternetAccessForFirewall flag.
        type: bool
      services:
        description: Nfv Profile's services.
        suboptions:
          firewallMode:
            description: Nfv Profile's firewallMode.
            type: str
          imageName:
            description: Nfv Profile's imageName.
            type: str
          profileType:
            description: Nfv Profile's profileType.
            type: str
          serviceName:
            description: Nfv Profile's serviceName.
            type: str
          serviceType:
            description: Nfv Profile's serviceType.
            type: str
          vNicMapping:
            description: Nfv Profile's vNicMapping.
            suboptions:
              assignIpAddressToNetwork:
                description: Nfv Profile's assignIpAddressToNetwork.
                type: str
              networkType:
                description: Nfv Profile's networkType.
                type: str
            type: list
        type: list
      vlanForL2:
        description: Nfv Profile's vlanForL2.
        suboptions:
          vlanDescription:
            description: Nfv Profile's vlanDescription.
            type: str
          vlanId:
            description: Nfv Profile's vlanId.
            type: int
          vlanType:
            description: Nfv Profile's vlanType.
            type: str
        type: list
    type: list
  id:
    description: Id path parameter. Id of the NFV profile to be updated.
    type: str
  name:
    description: Name query parameter. Name of the profile to be updated.
    type: str
  profileName:
    description: Nfv Profile's profileName.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Nfv Profile reference
  description: Complete reference of the Nfv Profile object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.dnac.nfv_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    device:
    - currentDeviceTag: string
      customNetworks:
      - connectionType: string
        networkName: string
        servicesToConnect:
        - serviceName: string
        vlanId: 0
        vlanMode: string
      customTemplate:
      - deviceType: string
        template: string
        templateType: string
      deviceTag: string
      directInternetAccessForFirewall: true
      services:
      - firewallMode: string
        imageName: string
        profileType: string
        serviceName: string
        serviceType: string
        vNicMapping:
        - assignIpAddressToNetwork: string
          networkType: string
      vlanForL2:
      - vlanDescription: string
        vlanId: 0
        vlanType: string
    id: string
    name: string

- name: Delete by id
  cisco.dnac.nfv_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
    name: string

- name: Create
  cisco.dnac.nfv_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    device:
    - customNetworks:
      - connectionType: string
        networkName: string
        servicesToConnect:
        - serviceName: string
        vlanId: 0
        vlanMode: string
      customTemplate:
      - deviceType: string
        template: string
        templateType: string
      deviceTag: string
      deviceType: string
      directInternetAccessForFirewall: true
      serviceProviderProfile:
      - connect: true
        connectDefaultGatewayOnWan: true
        linkType: string
        serviceProvider: string
      services:
      - firewallMode: string
        imageName: string
        profileType: string
        serviceName: string
        serviceType: string
        vNicMapping:
        - assignIpAddressToNetwork: string
          networkType: string
      vlanForL2:
      - vlanDescription: string
        vlanId: 0
        vlanType: string
    profileName: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

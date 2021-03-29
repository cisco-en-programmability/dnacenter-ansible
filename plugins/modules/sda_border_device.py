#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_border_device
short_description: Manage SdaBorderDevice objects of Sda
description:
- Gets border device detail from SDA Fabric.
- Deletes border device from SDA Fabric.
- Adds border device in SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_ipaddress:
    description:
    - Device IP Address.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      deviceManagementIpAddress:
        description:
        - It is the sda border device's deviceManagementIpAddress.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda border device's siteNameHierarchy.
        type: str
      externalDomainRoutingProtocolName:
        description:
        - It is the sda border device's externalDomainRoutingProtocolName.
        type: str
      externalConnectivityIpPoolName:
        description:
        - It is the sda border device's externalConnectivityIpPoolName.
        type: str
      internalAutonomouSystemNumber:
        description:
        - It is the sda border device's internalAutonomouSystemNumber.
        type: str
      borderSessionType:
        description:
        - It is the sda border device's borderSessionType.
        type: str
      connectedToInternet:
        description:
        - It is the sda border device's connectedToInternet.
        type: bool
      externalConnectivitySettings:
        description:
        - It is the sda border device's externalConnectivitySettings.
        type: list
        elements: dict
        suboptions:
          interfaceName:
            description:
            - It is the sda border device's interfaceName.
            type: str
          externalAutonomouSystemNumber:
            description:
            - It is the sda border device's externalAutonomouSystemNumber.
            type: str
          l3Handoff:
            description:
            - It is the sda border device's l3Handoff.
            type: list
            elements: dict
            suboptions:
              virtualNetwork:
                description:
                - It is the sda border device's virtualNetwork.
                type: dict
                suboptions:
                  virtualNetworkName:
                    description:
                    - It is the sda border device's virtualNetworkName.
                    type: str





requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_border_device
# Reference by Internet resource
- name: SdaBorderDevice reference
  description: Complete reference of the SdaBorderDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaBorderDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: gets_border_device_detail
  cisco.dnac.sda_border_device:
    state: query  # required
    device_ipaddress: SomeValue  # string, required
  register: query_result

- name: deletes_border_device
  cisco.dnac.sda_border_device:
    state: delete  # required
    device_ipaddress: SomeValue  # string, required

- name: adds_border_device
  cisco.dnac.sda_border_device:
    state: create  # required
    payload:  # required
    - deviceManagementIpAddress: SomeValue  # string
      siteNameHierarchy: SomeValue  # string
      externalDomainRoutingProtocolName: SomeValue  # string
      externalConnectivityIpPoolName: SomeValue  # string
      internalAutonomouSystemNumber: SomeValue  # string
      borderSessionType: SomeValue  # string
      connectedToInternet: True  # boolean
      externalConnectivitySettings:
      - interfaceName: SomeValue  # string
        externalAutonomouSystemNumber: SomeValue  # string
        l3Handoff:
        - virtualNetwork:
            virtualNetworkName: SomeValue  # string

"""

RETURN = """
"""

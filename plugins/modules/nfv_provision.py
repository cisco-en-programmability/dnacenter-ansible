#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: nfv_provision
short_description: Resource module for Nfv Provision
description:
- Manage operation create of the resource Nfv Provision.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  provisioning:
    description: Nfv Provision's provisioning.
    suboptions:
      device:
        description: Nfv Provision's device.
        suboptions:
          customNetworks:
            description: Nfv Provision's customNetworks.
            suboptions:
              ipAddressPool:
                description: Nfv Provision's ipAddressPool.
                type: str
              name:
                description: Nfv Provision's name.
                type: str
              port:
                description: Nfv Provision's port.
                type: str
            type: list
          deviceSerialNumber:
            description: Nfv Provision's deviceSerialNumber.
            type: str
          ip:
            description: Nfv Provision's ip.
            type: str
          serviceProviders:
            description: Nfv Provision's serviceProviders.
            suboptions:
              serviceProvider:
                description: Nfv Provision's serviceProvider.
                type: str
              wanInterface:
                description: Nfv Provision's wanInterface.
                suboptions:
                  bandwidth:
                    description: Nfv Provision's bandwidth.
                    type: str
                  gateway:
                    description: Nfv Provision's gateway.
                    type: str
                  interfaceName:
                    description: Nfv Provision's interfaceName.
                    type: str
                  ipAddress:
                    description: Nfv Provision's ipAddress.
                    type: str
                  subnetmask:
                    description: Nfv Provision's subnetmask.
                    type: str
                type: dict
            type: list
          services:
            description: Nfv Provision's services.
            suboptions:
              adminPasswordHash:
                description: Nfv Provision's adminPasswordHash.
                type: str
              centralManagerIP:
                description: Nfv Provision's centralManagerIP.
                type: str
              centralRegistrationKey:
                description: Nfv Provision's centralRegistrationKey.
                type: str
              commonKey:
                description: Nfv Provision's commonKey.
                type: str
              disk:
                description: Nfv Provision's disk.
                type: str
              mode:
                description: Nfv Provision's mode.
                type: str
              systemIp:
                description: Nfv Provision's systemIp.
                type: str
              type:
                description: Nfv Provision's type.
                type: str
            type: list
          subPools:
            description: Nfv Provision's subPools.
            suboptions:
              gateway:
                description: Nfv Provision's gateway.
                type: str
              ipSubnet:
                description: Nfv Provision's ipSubnet.
                type: str
              name:
                description: Nfv Provision's name.
                type: str
              parentPoolName:
                description: Nfv Provision's parentPoolName.
                type: str
              type:
                description: Nfv Provision's type.
                type: str
            type: list
          tagName:
            description: Nfv Provision's tagName.
            type: str
          templateParam:
            description: Nfv Provision's templateParam.
            suboptions:
              asav:
                description: Nfv Provision's asav.
                suboptions:
                  var1:
                    description: Nfv Provision's var1.
                    type: str
                type: dict
              nfvis:
                description: Nfv Provision's nfvis.
                suboptions:
                  var1:
                    description: Nfv Provision's var1.
                    type: str
                type: dict
            type: dict
          vlan:
            description: Nfv Provision's vlan.
            suboptions:
              id:
                description: Nfv Provision's id.
                type: str
              interfaces:
                description: Nfv Provision's interfaces.
                type: str
              network:
                description: Nfv Provision's network.
                type: str
              type:
                description: Nfv Provision's type.
                type: str
            type: list
        type: list
      site:
        description: Nfv Provision's site.
        suboptions:
          area:
            description: Nfv Provision's area.
            suboptions:
              name:
                description: Nfv Provision's name.
                type: str
              parentName:
                description: Nfv Provision's parentName.
                type: str
            type: dict
          building:
            description: Nfv Provision's building.
            suboptions:
              address:
                description: Nfv Provision's address.
                type: str
              latitude:
                description: Nfv Provision's latitude.
                type: int
              longitude:
                description: Nfv Provision's longitude.
                type: int
              name:
                description: Nfv Provision's name.
                type: str
              parentName:
                description: Nfv Provision's parentName.
                type: str
            type: dict
          floor:
            description: Nfv Provision's floor.
            suboptions:
              height:
                description: Nfv Provision's height.
                type: int
              length:
                description: Nfv Provision's length.
                type: int
              name:
                description: Nfv Provision's name.
                type: str
              parentName:
                description: Nfv Provision's parentName.
                type: str
              rfModel:
                description: Nfv Provision's rfModel.
                type: str
              width:
                description: Nfv Provision's width.
                type: int
            type: dict
          siteProfileName:
            description: Nfv Provision's siteProfileName.
            type: str
        type: dict
    type: list
  siteProfile:
    description: Nfv Provision's siteProfile.
    suboptions:
      device:
        description: Nfv Provision's device.
        suboptions:
          customNetworks:
            description: Nfv Provision's customNetworks.
            suboptions:
              connectionType:
                description: Nfv Provision's connectionType.
                type: str
              name:
                description: Nfv Provision's name.
                type: str
              networkMode:
                description: Nfv Provision's networkMode.
                type: str
              servicesToConnect:
                description: Nfv Provision's servicesToConnect.
                suboptions:
                  service:
                    description: Nfv Provision's service.
                    type: str
                type: list
              vlan:
                description: Nfv Provision's vlan.
                type: str
            type: list
          customServices:
            description: Nfv Provision's customServices.
            suboptions:
              applicationType:
                description: Nfv Provision's applicationType.
                type: str
              imageName:
                description: Nfv Provision's imageName.
                type: str
              name:
                description: Nfv Provision's name.
                type: str
              profile:
                description: Nfv Provision's profile.
                type: str
              topology:
                description: Nfv Provision's topology.
                suboptions:
                  assignIp:
                    description: Nfv Provision's assignIp.
                    type: str
                  name:
                    description: Nfv Provision's name.
                    type: str
                  type:
                    description: Nfv Provision's type.
                    type: str
                type: dict
            type: list
          customTemplate:
            description: Nfv Provision's customTemplate.
            suboptions:
              deviceType:
                description: Nfv Provision's deviceType.
                type: str
              template:
                description: Nfv Provision's template.
                type: str
            type: list
          deviceType:
            description: Nfv Provision's deviceType.
            type: str
          dia:
            description: Dia flag.
            type: bool
          serviceProviders:
            description: Nfv Provision's serviceProviders.
            suboptions:
              connect:
                description: Connect flag.
                type: bool
              defaultGateway:
                description: DefaultGateway flag.
                type: bool
              linkType:
                description: Nfv Provision's linkType.
                type: str
              serviceProvider:
                description: Nfv Provision's serviceProvider.
                type: str
            type: list
          services:
            description: Nfv Provision's services.
            suboptions:
              imageName:
                description: Nfv Provision's imageName.
                type: str
              mode:
                description: Nfv Provision's mode.
                type: str
              name:
                description: Nfv Provision's name.
                type: str
              profile:
                description: Nfv Provision's profile.
                type: str
              topology:
                description: Nfv Provision's topology.
                suboptions:
                  assignIp:
                    description: Nfv Provision's assignIp.
                    type: str
                  name:
                    description: Nfv Provision's name.
                    type: str
                  type:
                    description: Nfv Provision's type.
                    type: str
                type: dict
              type:
                description: Nfv Provision's type.
                type: str
            type: list
          tagName:
            description: Nfv Provision's tagName.
            type: str
          vlan:
            description: Nfv Provision's vlan.
            suboptions:
              id:
                description: Nfv Provision's id.
                type: str
              type:
                description: Nfv Provision's type.
                type: str
            type: list
        type: list
      siteProfileName:
        description: Nfv Provision's siteProfileName.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Nfv Provision reference
  description: Complete reference of the Nfv Provision object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.nfv_provision:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    provisioning:
    - device:
      - customNetworks:
        - ipAddressPool: string
          name: string
          port: string
        deviceSerialNumber: string
        ip: string
        serviceProviders:
        - serviceProvider: string
          wanInterface:
            bandwidth: string
            gateway: string
            interfaceName: string
            ipAddress: string
            subnetmask: string
        services:
        - adminPasswordHash: string
          centralManagerIP: string
          centralRegistrationKey: string
          commonKey: string
          disk: string
          mode: string
          systemIp: string
          type: string
        subPools:
        - gateway: string
          ipSubnet: string
          name: string
          parentPoolName: string
          type: string
        tagName: string
        templateParam:
          asav:
            var1: string
          nfvis:
            var1: string
        vlan:
        - id: string
          interfaces: string
          network: string
          type: string
      site:
        area:
          name: string
          parentName: string
        building:
          address: string
          latitude: 0
          longitude: 0
          name: string
          parentName: string
        floor:
          height: 0
          length: 0
          name: string
          parentName: string
          rfModel: string
          width: 0
        siteProfileName: string
    siteProfile:
    - device:
      - customNetworks:
        - connectionType: string
          name: string
          networkMode: string
          servicesToConnect:
          - service: string
          vlan: string
        customServices:
        - applicationType: string
          imageName: string
          name: string
          profile: string
          topology:
            assignIp: string
            name: string
            type: string
        customTemplate:
        - deviceType: string
          template: string
        deviceType: string
        dia: true
        serviceProviders:
        - connect: true
          defaultGateway: true
          linkType: string
          serviceProvider: string
        services:
        - imageName: string
          mode: string
          name: string
          profile: string
          topology:
            assignIp: string
            name: string
            type: string
          type: string
        tagName: string
        vlan:
        - id: string
          type: string
      siteProfileName: string

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

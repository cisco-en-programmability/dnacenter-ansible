#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: nfv_provision
short_description: Manage NfvProvision objects of SiteDesign
description:
- Design and Provision single/multi NFV device with given site/area/building/floor .
- Returns provisioning device information for the specified IP address.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  provisioning:
    description:
    - Provisioning, property of the request body (list of objects).
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      site:
        description:
        - It is the nfv provision's site.
        type: dict
        required: True
        suboptions:
          siteProfileName:
            description:
            - It is the nfv provision's siteProfileName.
            type: str
          area:
            description:
            - It is the nfv provision's area.
            type: dict
            suboptions:
              name:
                description:
                - It is the nfv provision's name.
                type: str
              parentName:
                description:
                - It is the nfv provision's parentName.
                type: str

          building:
            description:
            - It is the nfv provision's building.
            type: dict
            suboptions:
              name:
                description:
                - It is the nfv provision's name.
                type: str
              address:
                description:
                - It is the nfv provision's address.
                type: str
              latitude:
                description:
                - It is the nfv provision's latitude.
                type: int
              longitude:
                description:
                - It is the nfv provision's longitude.
                type: int
              parentName:
                description:
                - It is the nfv provision's parentName.
                type: str

          floor:
            description:
            - It is the nfv provision's floor.
            type: dict
            suboptions:
              name:
                description:
                - It is the nfv provision's name.
                type: str
              parentName:
                description:
                - It is the nfv provision's parentName.
                type: str
              rfModel:
                description:
                - It is the nfv provision's rfModel.
                type: str
              width:
                description:
                - It is the nfv provision's width.
                type: int
              length:
                description:
                - It is the nfv provision's length.
                type: int
              height:
                description:
                - It is the nfv provision's height.
                type: int


      device:
        description:
        - It is the nfv provision's device.
        type: list
        required: True
        elements: dict
        suboptions:
          ip:
            description:
            - It is the nfv provision's ip.
            type: str
          deviceSerialNumber:
            description:
            - It is the nfv provision's deviceSerialNumber.
            type: str
          tagName:
            description:
            - It is the nfv provision's tagName.
            type: str
            required: True
          serviceProviders:
            description:
            - It is the nfv provision's serviceProviders.
            type: list
            required: True
            elements: dict
            suboptions:
              serviceProvider:
                description:
                - It is the nfv provision's serviceProvider.
                type: str
                required: True
              wanInterface:
                description:
                - It is the nfv provision's wanInterface.
                type: dict
                suboptions:
                  ipAddress:
                    description:
                    - It is the nfv provision's ipAddress.
                    type: str
                  interfaceName:
                    description:
                    - It is the nfv provision's interfaceName.
                    type: str
                  subnetmask:
                    description:
                    - It is the nfv provision's subnetmask.
                    type: str
                  bandwidth:
                    description:
                    - It is the nfv provision's bandwidth.
                    type: str
                  gateway:
                    description:
                    - It is the nfv provision's gateway.
                    type: str


          services:
            description:
            - It is the nfv provision's services.
            type: list
            required: True
            elements: dict
            suboptions:
              type:
                description:
                - It is the nfv provision's type.
                type: str
                required: True
              mode:
                description:
                - It is the nfv provision's mode.
                type: str
              systemIp:
                description:
                - It is the nfv provision's systemIp.
                type: str
              centralManagerIP:
                description:
                - It is the nfv provision's centralManagerIP.
                type: str
              centralRegistrationKey:
                description:
                - It is the nfv provision's centralRegistrationKey.
                type: str
              commonKey:
                description:
                - It is the nfv provision's commonKey.
                type: str
              adminPasswordHash:
                description:
                - It is the nfv provision's adminPasswordHash.
                type: str
              disk:
                description:
                - It is the nfv provision's disk.
                type: str

          vlan:
            description:
            - It is the nfv provision's vlan.
            type: list
            elements: dict
            suboptions:
              type:
                description:
                - It is the nfv provision's type.
                type: str
                required: True
              id:
                description:
                - It is the nfv provision's id.
                type: str
                required: True
              interfaces:
                description:
                - It is the nfv provision's interfaces.
                type: str
                required: True
              network:
                description:
                - It is the nfv provision's network.
                type: str

          subPools:
            description:
            - It is the nfv provision's subPools.
            type: list
            required: True
            elements: dict
            suboptions:
              type:
                description:
                - It is the nfv provision's type.
                type: str
                required: True
              name:
                description:
                - It is the nfv provision's name.
                type: str
                required: True
              ipSubnet:
                description:
                - It is the nfv provision's ipSubnet.
                type: str
                required: True
              gateway:
                description:
                - It is the nfv provision's gateway.
                type: str
                required: True
              parentPoolName:
                description:
                - It is the nfv provision's parentPoolName.
                type: str

          customNetworks:
            description:
            - It is the nfv provision's customNetworks.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                - It is the nfv provision's name.
                type: str
                required: True
              port:
                description:
                - It is the nfv provision's port.
                type: str
              ipAddressPool:
                description:
                - It is the nfv provision's ipAddressPool.
                type: str

          templateParam:
            description:
            - It is the nfv provision's templateParam.
            type: dict
            suboptions:
              nfvis:
                description:
                - It is the nfv provision's nfvis.
                type: dict
                suboptions:
                  var1:
                    description:
                    - It is the nfv provision's var1.
                    type: str

              asav:
                description:
                - It is the nfv provision's asav.
                type: dict
                suboptions:
                  var1:
                    description:
                    - It is the nfv provision's var1.
                    type: str




  siteProfile:
    description:
    - Site Profile, property of the request body (list of objects).
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      siteProfileName:
        description:
        - It is the nfv provision's siteProfileName.
        type: str
        required: True
      device:
        description:
        - It is the nfv provision's device.
        type: list
        required: True
        elements: dict
        suboptions:
          deviceType:
            description:
            - It is the nfv provision's deviceType.
            type: str
            required: True
          tagName:
            description:
            - It is the nfv provision's tagName.
            type: str
            required: True
          serviceProviders:
            description:
            - It is the nfv provision's serviceProviders.
            type: list
            required: True
            elements: dict
            suboptions:
              serviceProvider:
                description:
                - It is the nfv provision's serviceProvider.
                type: str
                required: True
              linkType:
                description:
                - It is the nfv provision's linkType.
                type: str
                required: True
              connect:
                description:
                - It is the nfv provision's connect.
                type: bool
                required: True
              defaultGateway:
                description:
                - It is the nfv provision's defaultGateway.
                type: bool
                required: True

          dia:
            description:
            - It is the nfv provision's dia.
            type: bool
            required: True
          services:
            description:
            - It is the nfv provision's services.
            type: list
            required: True
            elements: dict
            suboptions:
              type:
                description:
                - It is the nfv provision's type.
                type: str
                required: True
              profile:
                description:
                - It is the nfv provision's profile.
                type: str
                required: True
              mode:
                description:
                - It is the nfv provision's mode.
                type: str
              name:
                description:
                - It is the nfv provision's name.
                type: str
                required: True
              imageName:
                description:
                - It is the nfv provision's imageName.
                type: str
                required: True
              topology:
                description:
                - It is the nfv provision's topology.
                type: dict
                required: True
                suboptions:
                  type:
                    description:
                    - It is the nfv provision's type.
                    type: str
                  name:
                    description:
                    - It is the nfv provision's name.
                    type: str
                  assignIp:
                    description:
                    - It is the nfv provision's assignIp.
                    type: str


          customServices:
            description:
            - It is the nfv provision's customServices.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                - It is the nfv provision's name.
                type: str
                required: True
              applicationType:
                description:
                - It is the nfv provision's applicationType.
                type: str
                required: True
              profile:
                description:
                - It is the nfv provision's profile.
                type: str
                required: True
              topology:
                description:
                - It is the nfv provision's topology.
                type: dict
                required: True
                suboptions:
                  type:
                    description:
                    - It is the nfv provision's type.
                    type: str
                  name:
                    description:
                    - It is the nfv provision's name.
                    type: str
                  assignIp:
                    description:
                    - It is the nfv provision's assignIp.
                    type: str

              imageName:
                description:
                - It is the nfv provision's imageName.
                type: str

          customNetworks:
            description:
            - It is the nfv provision's customNetworks.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                - It is the nfv provision's name.
                type: str
                required: True
              servicesToConnect:
                description:
                - It is the nfv provision's servicesToConnect.
                type: list
                required: True
                elements: dict
                suboptions:
                  service:
                    description:
                    - It is the nfv provision's service.
                    type: str
                    required: True

              connectionType:
                description:
                - It is the nfv provision's connectionType.
                type: str
                required: True
              networkMode:
                description:
                - It is the nfv provision's networkMode.
                type: str
                required: True
              vlan:
                description:
                - It is the nfv provision's vlan.
                type: str

          vlan:
            description:
            - It is the nfv provision's vlan.
            type: list
            elements: dict
            suboptions:
              type:
                description:
                - It is the nfv provision's type.
                type: str
                required: True
              id:
                description:
                - It is the nfv provision's id.
                type: str
                required: True

          customTemplate:
            description:
            - It is the nfv provision's customTemplate.
            type: list
            elements: dict
            suboptions:
              deviceType:
                description:
                - It is the nfv provision's deviceType.
                type: str
                required: True
              template:
                description:
                - It is the nfv provision's template.
                type: str
                required: True



  device_ip:
    description:
    - Device to which the provisioning detail has to be retrieved.
    - Required for state query.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.nfv_provision
# Reference by Internet resource
- name: NfvProvision reference
  description: Complete reference of the NfvProvision object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NfvProvision reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: provision_nfv
  cisco.dnac.nfv_provision:
    state: create  # required
    provisioning:  # required
    - site:  # required
        siteProfileName: SomeValue  # string
        area:
          name: SomeValue  # string
          parentName: SomeValue  # string
        building:
          name: SomeValue  # string
          address: SomeValue  # string
          latitude: 1  #  number
          longitude: 1  #  number
          parentName: SomeValue  # string
        floor:
          name: SomeValue  # string
          parentName: SomeValue  # string
          rfModel: SomeValue  # string
          width: 1  #  number
          length: 1  #  number
          height: 1  #  number
      device:  # required
      - tagName: SomeValue  # string, required
        serviceProviders:  # required
        - serviceProvider: SomeValue  # string, required
          wanInterface:
            ipAddress: SomeValue  # string
            interfaceName: SomeValue  # string
            subnetmask: SomeValue  # string
            bandwidth: SomeValue  # string
            gateway: SomeValue  # string
        services:  # required
        - type: SomeValue  # string, required
          mode: SomeValue  # string
          systemIp: SomeValue  # string
          centralManagerIP: SomeValue  # string
          centralRegistrationKey: SomeValue  # string
          commonKey: SomeValue  # string
          adminPasswordHash: SomeValue  # string
          disk: SomeValue  # string
        subPools:  # required
        - type: SomeValue  # string, required
          name: SomeValue  # string, required
          ipSubnet: SomeValue  # string, required
          gateway: SomeValue  # string, required
          parentPoolName: SomeValue  # string
        ip: SomeValue  # string
        deviceSerialNumber: SomeValue  # string
        vlan:
        - type: SomeValue  # string, required
          id: SomeValue  # string, required
          interfaces: SomeValue  # string, required
          network: SomeValue  # string
        customNetworks:
        - name: SomeValue  # string, required
          port: SomeValue  # string
          ipAddressPool: SomeValue  # string
        templateParam:
          nfvis:
            var1: SomeValue  # string
          asav:
            var1: SomeValue  # string
    siteProfile:  # required
    - siteProfileName: SomeValue  # string, required
      device:  # required
      - deviceType: SomeValue  # string, required
        tagName: SomeValue  # string, required
        serviceProviders:  # required
        - serviceProvider: SomeValue  # string, required
          linkType: SomeValue  # string, required
          connect: True  # boolean, required
          defaultGateway: True  # boolean, required
        dia: True  # boolean, required
        services:  # required
        - type: SomeValue  # string, required
          profile: SomeValue  # string, required
          name: SomeValue  # string, required
          imageName: SomeValue  # string, required
          topology:  # required
            type: SomeValue  # string
            name: SomeValue  # string
            assignIp: SomeValue  # string
          mode: SomeValue  # string
        customServices:
        - name: SomeValue  # string, required
          applicationType: SomeValue  # string, required
          profile: SomeValue  # string, required
          topology:  # required
            type: SomeValue  # string
            name: SomeValue  # string
            assignIp: SomeValue  # string
          imageName: SomeValue  # string
        customNetworks:
        - name: SomeValue  # string, required
          servicesToConnect:  # required
          - service: SomeValue  # string, required
          connectionType: SomeValue  # string, required
          networkMode: SomeValue  # string, required
          vlan: SomeValue  # string
        vlan:
        - type: SomeValue  # string, required
          id: SomeValue  # string, required
        customTemplate:
        - deviceType: SomeValue  # string, required
          template: SomeValue  # string, required

- name: get_device_details_by_ip
  cisco.dnac.nfv_provision:
    state: query  # required
    device_ip: SomeValue  # string, required
  register: nm_get_device_details_by_ip

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
  sample: site_design.get_device_details_by_ip
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

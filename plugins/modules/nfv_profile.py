#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: nfv_profile
short_description: Manage NfvProfile objects of SiteDesign
description:
- API to create network profile for different NFV topologies.
- API to get NFV network profile.
- API to delete nfv network profile.
- API to update a NFV Network profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device:
    description:
    - Device, property of the request body (list of objects).
    type: list
    required: True
    elements: dict
    suboptions:
      currentDeviceTag:
        description:
        - It is the nfv profile's currentDeviceTag.
        type: str
        required: True
      customNetworks:
        description:
        - It is the nfv profile's customNetworks.
        type: list
        elements: dict
        suboptions:
          connectionType:
            description:
            - It is the nfv profile's connectionType.
            - Required for states create and update.
            type: str
          networkName:
            description:
            - It is the nfv profile's networkName.
            - Required for states create and update.
            type: str
          servicesToConnect:
            description:
            - It is the nfv profile's servicesToConnect.
            type: list
            required: True
            elements: dict
            suboptions:
              serviceName:
                description:
                - It is the nfv profile's serviceName.
                - Required for states create and update.
                type: str

          vlanId:
            description:
            - It is the nfv profile's vlanId.
            - Required for states create and update.
            type: int
          vlanMode:
            description:
            - It is the nfv profile's vlanMode.
            - Required for states create and update.
            type: str

      customTemplate:
        description:
        - It is the nfv profile's customTemplate.
        type: list
        elements: dict
        suboptions:
          deviceType:
            description:
            - It is the nfv profile's deviceType.
            - Required for states create and update.
            type: str
          template:
            description:
            - It is the nfv profile's template.
            - Required for states create and update.
            type: str
          templateType:
            description:
            - It is the nfv profile's templateType.
            - Required for states create and update.
            type: str

      deviceTag:
        description:
        - It is the nfv profile's deviceTag.
        - Required for states create and update.
        type: str
      deviceType:
        description:
        - It is the nfv profile's deviceType.
        type: str
        required: True
      directInternetAccessForFirewall:
        description:
        - It is the nfv profile's directInternetAccessForFirewall.
        - Required for states create and update.
        type: bool
      serviceProviderProfile:
        description:
        - It is the nfv profile's serviceProviderProfile.
        type: list
        required: True
        elements: dict
        suboptions:
          serviceProvider:
            description:
            - It is the nfv profile's serviceProvider.
            type: str
            required: True
          linkType:
            description:
            - It is the nfv profile's linkType.
            type: str
            required: True
          connect:
            description:
            - It is the nfv profile's connect.
            type: bool
            required: True
          connectDefaultGatewayOnWan:
            description:
            - It is the nfv profile's connectDefaultGatewayOnWan.
            type: bool
            required: True

      services:
        description:
        - It is the nfv profile's services.
        type: list
        required: True
        elements: dict
        suboptions:
          firewallMode:
            description:
            - It is the nfv profile's firewallMode.
            type: str
          imageName:
            description:
            - It is the nfv profile's imageName.
            - Required for states create and update.
            type: str
          profileType:
            description:
            - It is the nfv profile's profileType.
            - Required for states create and update.
            type: str
          serviceName:
            description:
            - It is the nfv profile's serviceName.
            - Required for states create and update.
            type: str
          serviceType:
            description:
            - It is the nfv profile's serviceType.
            - Required for states create and update.
            type: str
          vNicMapping:
            description:
            - It is the nfv profile's vNicMapping.
            type: list
            required: True
            elements: dict
            suboptions:
              assignIpAddressToNetwork:
                description:
                - It is the nfv profile's assignIpAddressToNetwork.
                type: str
              networkType:
                description:
                - It is the nfv profile's networkType.
                - Required for states create and update.
                type: str


      vlanForL2:
        description:
        - It is the nfv profile's vlanForL2.
        type: list
        elements: dict
        suboptions:
          vlanDescription:
            description:
            - It is the nfv profile's vlanDescription.
            - Required for states create and update.
            type: str
          vlanId:
            description:
            - It is the nfv profile's vlanId.
            - Required for states create and update.
            type: int
          vlanType:
            description:
            - It is the nfv profile's vlanType.
            - Required for states create and update.
            type: str


  profileName:
    description:
    - Site Profile Name, property of the request body.
    - Required for state create.
    type: str
  id:
    description:
    - ID of network profile to retrieve.
    - Id of nfv network profile to delete. .
    - Id of the NFV profile to be updated.
    type: str
    required: True
  limit:
    description:
    - Number of profile to be retrieved.
    type: str
  name:
    description:
    - Name of network profile to be retrieved.
    - Nameof nfv network profile to delete. .
    - Name of the profile to be updated.
    type: str
  offset:
    description:
    - Offset/starting row.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.nfv_profile
# Reference by Internet resource
- name: NfvProfile reference
  description: Complete reference of the NfvProfile object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NfvProfile reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_nfv_profile
  cisco.dnac.nfv_profile:
    state: create  # required
    device:  # required
    - deviceType: SomeValue  # string, required
      deviceTag: SomeValue  # string, required
      serviceProviderProfile:  # required
      - serviceProvider: SomeValue  # string, required
        linkType: SomeValue  # string, required
        connect: True  # boolean, required
        connectDefaultGatewayOnWan: True  # boolean, required
      directInternetAccessForFirewall: True  # boolean, required
      services:  # required
      - serviceType: SomeValue  # string, required
        profileType: SomeValue  # string, required
        serviceName: SomeValue  # string, required
        imageName: SomeValue  # string, required
        vNicMapping:  # required
        - networkType: SomeValue  # string, required
          assignIpAddressToNetwork: SomeValue  # string
        firewallMode: SomeValue  # string
      customNetworks:
      - networkName: SomeValue  # string, required
        servicesToConnect:  # required
        - serviceName: SomeValue  # string, required
        connectionType: SomeValue  # string, required
        vlanMode: SomeValue  # string, required
        vlanId: 1  #  number, required
      vlanForL2:
      - vlanType: SomeValue  # string, required
        vlanId: 1  #  number, required
        vlanDescription: SomeValue  # string, required
      customTemplate:
      - deviceType: SomeValue  # string, required
        template: SomeValue  # string, required
        templateType: SomeValue  # string, required
    profileName: SomeValue  # string, required

- name: get_nfv_profile
  cisco.dnac.nfv_profile:
    state: query  # required
    id: SomeValue  # string, required
    limit: SomeValue  # string
    name: SomeValue  # string
    offset: SomeValue  # string
  register: query_result

- name: delete_nfv_profile
  cisco.dnac.nfv_profile:
    state: delete  # required
    id: SomeValue  # string, required
    name: SomeValue  # string

- name: update_nfv_profile
  cisco.dnac.nfv_profile:
    state: update  # required
    id: SomeValue  # string, required
    device:  # required
    - deviceTag: SomeValue  # string, required
      directInternetAccessForFirewall: True  # boolean, required
      currentDeviceTag: SomeValue  # string, required
      services:
      - serviceType: SomeValue  # string, required
        profileType: SomeValue  # string, required
        serviceName: SomeValue  # string, required
        imageName: SomeValue  # string, required
        vNicMapping:  # required
        - networkType: SomeValue  # string, required
          assignIpAddressToNetwork: SomeValue  # string
        firewallMode: SomeValue  # string
      customNetworks:
      - networkName: SomeValue  # string, required
        servicesToConnect:  # required
        - serviceName: SomeValue  # string, required
        connectionType: SomeValue  # string, required
        vlanMode: SomeValue  # string, required
        vlanId: 1  #  number, required
      vlanForL2:
      - vlanType: SomeValue  # string, required
        vlanId: 1  #  number, required
        vlanDescription: SomeValue  # string, required
      customTemplate:
      - deviceType: SomeValue  # string, required
        template: SomeValue  # string, required
        templateType: SomeValue  # string, required
    name: SomeValue  # string

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
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: array
  sample:
"""

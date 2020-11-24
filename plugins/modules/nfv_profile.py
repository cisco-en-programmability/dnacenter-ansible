#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: nfv_profile
short_description: Manage NfvProfile objects of SiteDesign
description:
- API to create network profile for different NFV topologies.
- API to get NFV network profile.
- API to delete nfv network profile.
- API to update a NFV Network profile.
version_added: '1.0'
author: first last (@GitHubID)
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
  cisco.dnac.nfv_profile
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
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
  delegate_to: localhost
  
- name: get_nfv_profile
  cisco.dnac.nfv_profile
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    id: SomeValue  # string, required
    limit: SomeValue  # string
    name: SomeValue  # string
    offset: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
- name: delete_nfv_profile
  cisco.dnac.nfv_profile
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: delete  # required
    id: SomeValue  # string, required
    name: SomeValue  # string
  delegate_to: localhost
  
- name: update_nfv_profile
  cisco.dnac.nfv_profile
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
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
  delegate_to: localhost
  
"""

RETURN = """
create_nfv_profile:
    description: API to create network profile for different NFV topologies.
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

get_nfv_profile:
    description: API to get NFV network profile.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        profileName:
          description: It is the nfv profile's profileName.
          returned: always
          type: str
          sample: '<profilename>'
        id:
          description: It is the nfv profile's id.
          returned: always
          type: str
          sample: '478012'
        device:
          description: It is the nfv profile's device.
          returned: always
          type: list
          contains:
            deviceType:
              description: It is the nfv profile's deviceType.
              returned: always
              type: str
              sample: '<devicetype>'
            deviceTag:
              description: It is the nfv profile's deviceTag.
              returned: always
              type: str
              sample: '<devicetag>'
            serviceProviderProfile:
              description: It is the nfv profile's serviceProviderProfile.
              returned: always
              type: list
              contains:
                linkType:
                  description: It is the nfv profile's linkType.
                  returned: always
                  type: str
                  sample: '<linktype>'
                connect:
                  description: It is the nfv profile's connect.
                  returned: always
                  type: bool
                  sample: false
                connectDefaultGatewayOnWan:
                  description: It is the nfv profile's connectDefaultGatewayOnWan.
                  returned: always
                  type: bool
                  sample: false
                serviceProvider:
                  description: It is the nfv profile's serviceProvider.
                  returned: always
                  type: str
                  sample: '<serviceprovider>'

            directInternetAccessForFirewall:
              description: It is the nfv profile's directInternetAccessForFirewall.
              returned: always
              type: bool
              sample: false
            services:
              description: It is the nfv profile's services.
              returned: always
              type: list
              contains:
                serviceType:
                  description: It is the nfv profile's serviceType.
                  returned: always
                  type: str
                  sample: '<servicetype>'
                profileType:
                  description: It is the nfv profile's profileType.
                  returned: always
                  type: str
                  sample: '<profiletype>'
                serviceName:
                  description: It is the nfv profile's serviceName.
                  returned: always
                  type: str
                  sample: '<servicename>'
                imageName:
                  description: It is the nfv profile's imageName.
                  returned: always
                  type: str
                  sample: '<imagename>'
                vNicMapping:
                  description: It is the nfv profile's vNicMapping.
                  returned: always
                  type: list
                  contains:
                    networkType:
                      description: It is the nfv profile's networkType.
                      returned: always
                      type: str
                      sample: '<networktype>'
                    assignIpAddressToNetwork:
                      description: It is the nfv profile's assignIpAddressToNetwork.
                      returned: always
                      type: bool
                      sample: false

                firewallMode:
                  description: It is the nfv profile's firewallMode.
                  returned: always
                  type: str
                  sample: '<firewallmode>'

            customNetworks:
              description: It is the nfv profile's customNetworks.
              returned: always
              type: list
              contains:
                networkName:
                  description: It is the nfv profile's networkName.
                  returned: always
                  type: str
                  sample: '<networkname>'
                servicesToConnect:
                  description: It is the nfv profile's servicesToConnect.
                  returned: always
                  type: list
                  contains:
                    serviceName:
                      description: It is the nfv profile's serviceName.
                      returned: always
                      type: str
                      sample: '<servicename>'

                connectionType:
                  description: It is the nfv profile's connectionType.
                  returned: always
                  type: str
                  sample: '<connectiontype>'
                vlanMode:
                  description: It is the nfv profile's vlanMode.
                  returned: always
                  type: str
                  sample: '<vlanmode>'
                vlanId:
                  description: It is the nfv profile's vlanId.
                  returned: always
                  type: str
                  sample: '<vlanid>'

            vlanForL2:
              description: It is the nfv profile's vlanForL2.
              returned: always
              type: list
              contains:
                vlanType:
                  description: It is the nfv profile's vlanType.
                  returned: always
                  type: str
                  sample: '<vlantype>'
                vlanId:
                  description: It is the nfv profile's vlanId.
                  returned: always
                  type: str
                  sample: '<vlanid>'
                vlanDescription:
                  description: It is the nfv profile's vlanDescription.
                  returned: always
                  type: str
                  sample: '<vlandescription>'

            customTemplate:
              description: It is the nfv profile's customTemplate.
              returned: always
              type: list
              contains:
                deviceType:
                  description: It is the nfv profile's deviceType.
                  returned: always
                  type: str
                  sample: '<devicetype>'
                template:
                  description: It is the nfv profile's template.
                  returned: always
                  type: str
                  sample: '<template>'
                templateType:
                  description: It is the nfv profile's templateType.
                  returned: always
                  type: str
                  sample: '<templatetype>'




delete_nfv_profile:
    description: API to delete nfv network profile.
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

update_nfv_profile:
    description: API to update a NFV Network profile.
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

"""

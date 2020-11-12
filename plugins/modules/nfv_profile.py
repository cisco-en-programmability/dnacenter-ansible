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
                        type: str
                        required: True
                    networkName:
                        description:
                        - It is the nfv profile's networkName.
                        type: str
                        required: True
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
                                type: str
                                required: True

                    vlanId:
                        description:
                        - It is the nfv profile's vlanId.
                        type: int
                        required: True
                    vlanMode:
                        description:
                        - It is the nfv profile's vlanMode.
                        type: str
                        required: True

            customTemplate:
                description:
                - It is the nfv profile's customTemplate.
                type: list
                elements: dict
                suboptions:
                    deviceType:
                        description:
                        - It is the nfv profile's deviceType.
                        type: str
                        required: True
                    template:
                        description:
                        - It is the nfv profile's template.
                        type: str
                        required: True
                    templateType:
                        description:
                        - It is the nfv profile's templateType.
                        type: str
                        required: True

            deviceTag:
                description:
                - It is the nfv profile's deviceTag.
                type: str
                required: True
            deviceType:
                description:
                - It is the nfv profile's deviceType.
                type: str
                required: True
            directInternetAccessForFirewall:
                description:
                - It is the nfv profile's directInternetAccessForFirewall.
                type: bool
                required: True
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
                        type: str
                        required: True
                    profileType:
                        description:
                        - It is the nfv profile's profileType.
                        type: str
                        required: True
                    serviceName:
                        description:
                        - It is the nfv profile's serviceName.
                        type: str
                        required: True
                    serviceType:
                        description:
                        - It is the nfv profile's serviceType.
                        type: str
                        required: True
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
                                type: str
                                required: True


            vlanForL2:
                description:
                - It is the nfv profile's vlanForL2.
                type: list
                elements: dict
                suboptions:
                    vlanDescription:
                        description:
                        - It is the nfv profile's vlanDescription.
                        type: str
                        required: True
                    vlanId:
                        description:
                        - It is the nfv profile's vlanId.
                        type: int
                        required: True
                    vlanType:
                        description:
                        - It is the nfv profile's vlanType.
                        type: str
                        required: True


    profileName:
        description:
        - Site Profile Name, property of the request body.
        type: str
        required: True
    id:
        description:
        - ID of network profile to retrieve.
        type: str
        required: True
    limit:
        description:
        - Number of profile to be retrieved.
        type: str
    name:
        description:
        - Name of network profile to be retrieved.
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
"""

RETURN = r"""
data_0:
    description: API to create network profile for different NFV topologies.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionstatusurl>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

data_1:
    description: API to get NFV network profile.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                profileName:
                    description: It is the nfv profile's profileName.
                    returned: success,changed,always
                    type: str
                    sample: '<profilename>'
                id:
                    description: It is the nfv profile's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                device:
                    description: It is the nfv profile's device.
                    returned: success,changed,always
                    type: list
                    contains:
                        deviceType:
                            description: It is the nfv profile's deviceType.
                            returned: success,changed,always
                            type: str
                            sample: '<devicetype>'
                        deviceTag:
                            description: It is the nfv profile's deviceTag.
                            returned: success,changed,always
                            type: str
                            sample: '<devicetag>'
                        serviceProviderProfile:
                            description: It is the nfv profile's serviceProviderProfile.
                            returned: success,changed,always
                            type: list
                            contains:
                                linkType:
                                    description: It is the nfv profile's linkType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<linktype>'
                                connect:
                                    description: It is the nfv profile's connect.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                connectDefaultGatewayOnWan:
                                    description: It is the nfv profile's connectDefaultGatewayOnWan.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                serviceProvider:
                                    description: It is the nfv profile's serviceProvider.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<serviceprovider>'

                        directInternetAccessForFirewall:
                            description: It is the nfv profile's directInternetAccessForFirewall.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        services:
                            description: It is the nfv profile's services.
                            returned: success,changed,always
                            type: list
                            contains:
                                serviceType:
                                    description: It is the nfv profile's serviceType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<servicetype>'
                                profileType:
                                    description: It is the nfv profile's profileType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<profiletype>'
                                serviceName:
                                    description: It is the nfv profile's serviceName.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<servicename>'
                                imageName:
                                    description: It is the nfv profile's imageName.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<imagename>'
                                vNicMapping:
                                    description: It is the nfv profile's vNicMapping.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        networkType:
                                            description: It is the nfv profile's networkType.
                                            returned: success,changed,always
                                            type: str
                                            sample: '<networktype>'
                                        assignIpAddressToNetwork:
                                            description: It is the nfv profile's assignIpAddressToNetwork.
                                            returned: success,changed,always
                                            type: bool
                                            sample: false

                                firewallMode:
                                    description: It is the nfv profile's firewallMode.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<firewallmode>'

                        customNetworks:
                            description: It is the nfv profile's customNetworks.
                            returned: success,changed,always
                            type: list
                            contains:
                                networkName:
                                    description: It is the nfv profile's networkName.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<networkname>'
                                servicesToConnect:
                                    description: It is the nfv profile's servicesToConnect.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        serviceName:
                                            description: It is the nfv profile's serviceName.
                                            returned: success,changed,always
                                            type: str
                                            sample: '<servicename>'

                                connectionType:
                                    description: It is the nfv profile's connectionType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<connectiontype>'
                                vlanMode:
                                    description: It is the nfv profile's vlanMode.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<vlanmode>'
                                vlanId:
                                    description: It is the nfv profile's vlanId.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<vlanid>'

                        vlanForL2:
                            description: It is the nfv profile's vlanForL2.
                            returned: success,changed,always
                            type: list
                            contains:
                                vlanType:
                                    description: It is the nfv profile's vlanType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<vlantype>'
                                vlanId:
                                    description: It is the nfv profile's vlanId.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<vlanid>'
                                vlanDescription:
                                    description: It is the nfv profile's vlanDescription.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<vlandescription>'

                        customTemplate:
                            description: It is the nfv profile's customTemplate.
                            returned: success,changed,always
                            type: list
                            contains:
                                deviceType:
                                    description: It is the nfv profile's deviceType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<devicetype>'
                                template:
                                    description: It is the nfv profile's template.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<template>'
                                templateType:
                                    description: It is the nfv profile's templateType.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<templatetype>'




data_2:
    description: API to delete nfv network profile.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionstatusurl>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

data_3:
    description: API to update a NFV Network profile.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionstatusurl>'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<message>'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.nfv_profile import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()

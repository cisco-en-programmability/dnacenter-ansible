#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: nfv_provision
short_description: Manage NfvProvision objects of SiteDesign
description:
- Design and Provision single/multi NFV device with given site/area/building/floor .
- Returns provisioning device information for the specified IP address.
version_added: '1.0'
author: first last (@GitHubID)
options:
    provisioning:
        description:
        - Provisioning, property of the request body (list of objects).
        type: list
        required: True
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
        type: list
        required: True
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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Design and Provision single/multi NFV device with given site/area/building/floor .
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Returns provisioning device information for the specified IP address.
    returned: success,changed,always
    type: dict
    contains:
        provisionDetails:
            description: Provision Details, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                startTime:
                    description: It is the nfv provision's startTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the nfv provision's endTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duration:
                    description: It is the nfv provision's duration.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                statusMessage:
                    description: It is the nfv provision's statusMessage.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the nfv provision's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                taskNodes:
                    description: It is the nfv provision's taskNodes.
                    returned: success,changed,always
                    type: list
                    contains:
                        startTime:
                            description: It is the nfv provision's startTime.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the nfv provision's endTime.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        duration:
                            description: It is the nfv provision's duration.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        status:
                            description: It is the nfv provision's status.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        nextTask:
                            description: It is the nfv provision's nextTask.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the nfv provision's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        target:
                            description: It is the nfv provision's target.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        statusMessage:
                            description: It is the nfv provision's statusMessage.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        payload:
                            description: It is the nfv provision's payload.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        provisionedNames:
                            description: It is the nfv provision's provisionedNames.
                            returned: success,changed,always
                            type: dict
                        errorPayload:
                            description: It is the nfv provision's errorPayload.
                            returned: success,changed,always
                            type: dict
                        parentTask:
                            description: It is the nfv provision's parentTask.
                            returned: success,changed,always
                            type: dict
                        cliTemplateUserMessageDTO:
                            description: It is the nfv provision's cliTemplateUserMessageDTO.
                            returned: success,changed,always
                            type: dict
                        stepRan:
                            description: It is the nfv provision's stepRan.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                topology:
                    description: It is the nfv provision's topology.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                beginStep:
                    description: It is the nfv provision's beginStep.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.nfv_provision import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
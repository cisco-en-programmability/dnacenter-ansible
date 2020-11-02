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
module: wireless_provision
short_description: Manage WirelessProvision objects of Wireless
description:
- Provision wireless devices.
- Updates wireless provisioning.
version_added: '1.0'
author: first last (@GitHubID)
options:
    payload:
        description:
        - A JSON serializable Python object to send in the body of the Request.
        type: list
        required: True
        elements: dict
        suboptions:
            deviceName:
                description:
                - It is the wireless provision's deviceName.
                type: str
                required: True
            site:
                description:
                - It is the wireless provision's site.
                type: str
                required: True
            managedAPLocations:
                description:
                - It is the wireless provision's managedAPLocations.
                type: list
            dynamicInterfaces:
                description:
                - It is the wireless provision's dynamicInterfaces.
                type: list
                elements: dict
                suboptions:
                    interfaceIPAddress:
                        description:
                        - It is the wireless provision's interfaceIPAddress.
                        type: str
                    interfaceNetmaskInCIDR:
                        description:
                        - It is the wireless provision's interfaceNetmaskInCIDR.
                        type: int
                    interfaceGateway:
                        description:
                        - It is the wireless provision's interfaceGateway.
                        type: str
                    lagOrPortNumber:
                        description:
                        - It is the wireless provision's lagOrPortNumber.
                        type: int
                    vlanId:
                        description:
                        - It is the wireless provision's vlanId.
                        type: int
                    interfaceName:
                        description:
                        - It is the wireless provision's interfaceName.
                        type: str


    payload:
        description:
        - A JSON serializable Python object to send in the body of the Request.
        type: list
        required: True
        elements: dict
        suboptions:
            deviceName:
                description:
                - It is the wireless provision's deviceName.
                type: str
                required: True
            managedAPLocations:
                description:
                - It is the wireless provision's managedAPLocations.
                type: list
            dynamicInterfaces:
                description:
                - It is the wireless provision's dynamicInterfaces.
                type: list
                elements: dict
                suboptions:
                    interfaceIPAddress:
                        description:
                        - It is the wireless provision's interfaceIPAddress.
                        type: str
                    interfaceNetmaskInCIDR:
                        description:
                        - It is the wireless provision's interfaceNetmaskInCIDR.
                        type: int
                    interfaceGateway:
                        description:
                        - It is the wireless provision's interfaceGateway.
                        type: str
                    lagOrPortNumber:
                        description:
                        - It is the wireless provision's lagOrPortNumber.
                        type: int
                    vlanId:
                        description:
                        - It is the wireless provision's vlanId.
                        type: int
                    interfaceName:
                        description:
                        - It is the wireless provision's interfaceName.
                        type: str



requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.wireless_provision
# Reference by Internet resource
- name: WirelessProvision reference
  description: Complete reference of the WirelessProvision object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: WirelessProvision reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Provision wireless devices.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionUrl:
            description: Execution Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        provisioningTasks:
            description: Provisioning Tasks, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                success:
                    description: It is the wireless provision's success.
                    returned: success,changed,always
                    type: list
                failed:
                    description: It is the wireless provision's failed.
                    returned: success,changed,always
                    type: list


data_1:
    description: Updates wireless provisioning.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionUrl:
            description: Execution Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        provisioningTasks:
            description: Provisioning Tasks, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                success:
                    description: It is the wireless provision's success.
                    returned: success,changed,always
                    type: list
                failed:
                    description: It is the wireless provision's failed.
                    returned: success,changed,always
                    type: list


'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.wireless_provision import module_definition


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

    if state == "create":
        dnac.exec("post")

    elif state == "update":
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
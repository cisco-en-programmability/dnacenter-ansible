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
module: sda_virtual_network_ip_pool
short_description: Manage SdaVirtualNetworkIpPool objects of Sda
description:
- Delete IP Pool from SDA Virtual Network.
- Get IP Pool from SDA Virtual Network.
- Add IP Pool in SDA Virtual Network.
version_added: '1.0'
author: first last (@GitHubID)
options:
    ip_pool_name:
        description:
        - IpPoolName query parameter.
        type: str
    virtual_network_name:
        description:
        - VirtualNetworkName query parameter.
        type: str
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            virtualNetworkName:
                description:
                - It is the sda virtual network ip pool's virtualNetworkName.
                type: str
            ipPoolName:
                description:
                - It is the sda virtual network ip pool's ipPoolName.
                type: str
            trafficType:
                description:
                - It is the sda virtual network ip pool's trafficType.
                type: str
            authenticationPolicyName:
                description:
                - It is the sda virtual network ip pool's authenticationPolicyName.
                type: str
            scalableGroupName:
                description:
                - It is the sda virtual network ip pool's scalableGroupName.
                type: str
            isL2FloodingEnabled:
                description:
                - It is the sda virtual network ip pool's isL2FloodingEnabled.
                type: bool
            isThisCriticalPool:
                description:
                - It is the sda virtual network ip pool's isThisCriticalPool.
                type: bool
            poolType:
                description:
                - It is the sda virtual network ip pool's poolType.
                type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_virtual_network_ip_pool
# Reference by Internet resource
- name: SdaVirtualNetworkIpPool reference
  description: Complete reference of the SdaVirtualNetworkIpPool object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaVirtualNetworkIpPool reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Delete IP Pool from SDA Virtual Network.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Get IP Pool from SDA Virtual Network.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        virtualNetworkName:
            description: Virtual Network Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        ipPoolName:
            description: Ip Pool Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        authenticationPolicyName:
            description: Authentication Policy Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        trafficType:
            description: Traffic Type, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        scalableGroupName:
            description: Scalable Group Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        isL2FloodingEnabled:
            description: IsL2FloodingEnabled, property of the response body.
            returned: success,changed,always
            type: bool
            sample: false
        isThisCriticalPool:
            description: IsThisCriticalPool, property of the response body.
            returned: success,changed,always
            type: bool
            sample: false

data_2:
    description: Add IP Pool in SDA Virtual Network.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.sda_virtual_network_ip_pool import module_definition


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

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
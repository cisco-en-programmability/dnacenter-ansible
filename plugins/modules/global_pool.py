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
module: global_pool
short_description: Manage GlobalPool objects of NetworkSettings
description:
- API to get global pool.
- API to create global pool.
- API to update global pool.
- API to delete global IP pool.
version_added: '1.0'
author: first last (@GitHubID)
options:
    limit:
        description:
        - No of Global Pools to be retrieved.
        type: str
    offset:
        description:
        - Offset/starting row.
        type: str
    settings:
        description:
        - Settings, property of the request body.
        type: dict
        required: True
        suboptions:
            ippool:
                description:
                - It is the global pool's ippool.
                type: list
                elements: dict
                suboptions:
                    ipPoolName:
                        description:
                        - It is the global pool's ipPoolName.
                        type: str
                        required: True
                    type:
                        description:
                        - It is the global pool's type.
                        type: str
                        required: True
                    ipPoolCidr:
                        description:
                        - It is the global pool's ipPoolCidr.
                        type: str
                        required: True
                    gateway:
                        description:
                        - It is the global pool's gateway.
                        type: str
                    dhcpServerIps:
                        description:
                        - It is the global pool's dhcpServerIps.
                        type: list
                    dnsServerIps:
                        description:
                        - It is the global pool's dnsServerIps.
                        type: list
                    IpAddressSpace:
                        description:
                        - It is the global pool's IpAddressSpace.
                        type: str


    settings:
        description:
        - Settings, property of the request body.
        type: dict
        required: True
        suboptions:
            ippool:
                description:
                - It is the global pool's ippool.
                type: list
                elements: dict
                suboptions:
                    ipPoolName:
                        description:
                        - It is the global pool's ipPoolName.
                        type: str
                    gateway:
                        description:
                        - It is the global pool's gateway.
                        type: str
                    dhcpServerIps:
                        description:
                        - It is the global pool's dhcpServerIps.
                        type: list
                    dnsServerIps:
                        description:
                        - It is the global pool's dnsServerIps.
                        type: list
                    id:
                        description:
                        - It is the global pool's id.
                        type: str
                        required: True


    id:
        description:
        - Global pool id.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_pool
# Reference by Internet resource
- name: GlobalPool reference
  description: Complete reference of the GlobalPool object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalPool reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: API to get global pool.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                ipPoolName:
                    description: It is the global pool's ipPoolName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                dhcpServerIps:
                    description: It is the global pool's dhcpServerIps.
                    returned: success,changed,always
                    type: list
                gateways:
                    description: It is the global pool's gateways.
                    returned: success,changed,always
                    type: list
                createTime:
                    description: It is the global pool's createTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdateTime:
                    description: It is the global pool's lastUpdateTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                totalIpAddressCount:
                    description: It is the global pool's totalIpAddressCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                usedIpAddressCount:
                    description: It is the global pool's usedIpAddressCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                parentUuid:
                    description: It is the global pool's parentUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                owner:
                    description: It is the global pool's owner.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                shared:
                    description: It is the global pool's shared.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                overlapping:
                    description: It is the global pool's overlapping.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configureExternalDhcp:
                    description: It is the global pool's configureExternalDhcp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                usedPercentage:
                    description: It is the global pool's usedPercentage.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                clientOptions:
                    description: It is the global pool's clientOptions.
                    returned: success,changed,always
                    type: dict
                dnsServerIps:
                    description: It is the global pool's dnsServerIps.
                    returned: success,changed,always
                    type: list
                context:
                    description: It is the global pool's context.
                    returned: success,changed,always
                    type: list
                    contains:
                        owner:
                            description: It is the global pool's owner.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        contextKey:
                            description: It is the global pool's contextKey.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        contextValue:
                            description: It is the global pool's contextValue.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                ipv6:
                    description: It is the global pool's ipv6.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the global pool's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipPoolCidr:
                    description: It is the global pool's ipPoolCidr.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: API to create global pool.
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

data_2:
    description: API to update global pool.
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

data_3:
    description: API to delete global IP pool.
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

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.global_pool import module_definition


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
        dnac.exec("post")

    elif state == "update":
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
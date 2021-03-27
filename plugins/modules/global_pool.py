#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: global_pool
short_description: Manage GlobalPool objects of NetworkSettings
description:
- API to get global pool.
- API to create global pool.
- API to update global pool.
- API to delete global IP pool.
version_added: '1.0'
author: Rafael Campos (@racampos)
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
          IpAddressSpace:
            description:
            - It is the global pool's IpAddressSpace.
            type: str
          dhcpServerIps:
            description:
            - It is the global pool's dhcpServerIps.
            type: list
          dnsServerIps:
            description:
            - It is the global pool's dnsServerIps.
            type: list
          gateway:
            description:
            - It is the global pool's gateway.
            type: str
          id:
            description:
            - It is the global pool's id.
            type: str
            required: True
          ipPoolCidr:
            description:
            - It is the global pool's ipPoolCidr.
            type: str
            required: True
          ipPoolName:
            description:
            - It is the global pool's ipPoolName.
            - Required for state create.
            type: str
          type:
            description:
            - It is the global pool's type.
            type: str
            required: True


  id:
    description:
    - Global pool id.
    - Required for state delete.
    type: str

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
"""

EXAMPLES = r"""
- name: get_global_pool
  cisco.dnac.global_pool:
    state: query  # required
    limit: SomeValue  # string
    offset: SomeValue  # string
  register: query_result
  
- name: create_global_pool
  cisco.dnac.global_pool:
    state: create  # required
    settings:  # required
      ippool:
      - ipPoolName: SomeValue  # string, required
        type: SomeValue  # string, required
        ipPoolCidr: SomeValue  # string, required
        gateway: SomeValue  # string
        dhcpServerIps:
        - SomeValue  # string
        dnsServerIps:
        - SomeValue  # string
        IpAddressSpace: SomeValue  # string
  
- name: update_global_pool
  cisco.dnac.global_pool:
    state: update  # required
    settings:  # required
      ippool:
      - id: SomeValue  # string, required
        ipPoolName: SomeValue  # string
        gateway: SomeValue  # string
        dhcpServerIps:
        - SomeValue  # string
        dnsServerIps:
        - SomeValue  # string
  
- name: delete_global_ip_pool
  cisco.dnac.global_pool:
    state: delete  # required
    id: SomeValue  # string, required
  
"""

RETURN = """
get_global_pool:
    description: API to get global pool.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        ipPoolName:
          description: It is the global pool's ipPoolName.
          returned: always
          type: str
          sample: '<ippoolname>'
        dhcpServerIps:
          description: It is the global pool's dhcpServerIps.
          returned: always
          type: list
        gateways:
          description: It is the global pool's gateways.
          returned: always
          type: list
        createTime:
          description: It is the global pool's createTime.
          returned: always
          type: str
          sample: '<createtime>'
        lastUpdateTime:
          description: It is the global pool's lastUpdateTime.
          returned: always
          type: str
          sample: '<lastupdatetime>'
        totalIpAddressCount:
          description: It is the global pool's totalIpAddressCount.
          returned: always
          type: str
          sample: '<totalipaddresscount>'
        usedIpAddressCount:
          description: It is the global pool's usedIpAddressCount.
          returned: always
          type: str
          sample: '<usedipaddresscount>'
        parentUuid:
          description: It is the global pool's parentUuid.
          returned: always
          type: str
          sample: '<parentuuid>'
        owner:
          description: It is the global pool's owner.
          returned: always
          type: str
          sample: '<owner>'
        shared:
          description: It is the global pool's shared.
          returned: always
          type: str
          sample: '<shared>'
        overlapping:
          description: It is the global pool's overlapping.
          returned: always
          type: str
          sample: '<overlapping>'
        configureExternalDhcp:
          description: It is the global pool's configureExternalDhcp.
          returned: always
          type: str
          sample: '<configureexternaldhcp>'
        usedPercentage:
          description: It is the global pool's usedPercentage.
          returned: always
          type: str
          sample: '<usedpercentage>'
        clientOptions:
          description: It is the global pool's clientOptions.
          returned: always
          type: dict
        dnsServerIps:
          description: It is the global pool's dnsServerIps.
          returned: always
          type: list
        context:
          description: It is the global pool's context.
          returned: always
          type: list
          contains:
            owner:
              description: It is the global pool's owner.
              returned: always
              type: str
              sample: '<owner>'
            contextKey:
              description: It is the global pool's contextKey.
              returned: always
              type: str
              sample: '<contextkey>'
            contextValue:
              description: It is the global pool's contextValue.
              returned: always
              type: str
              sample: '<contextvalue>'

        ipv6:
          description: It is the global pool's ipv6.
          returned: always
          type: str
          sample: '<ipv6>'
        id:
          description: It is the global pool's id.
          returned: always
          type: str
          sample: '478012'
        ipPoolCidr:
          description: It is the global pool's ipPoolCidr.
          returned: always
          type: str
          sample: '<ippoolcidr>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

create_global_pool:
    description: API to create global pool.
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

update_global_pool:
    description: API to update global pool.
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

delete_global_ip_pool:
    description: API to delete global IP pool.
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

"""

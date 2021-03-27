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
version_added: '1.0.0'
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
"""

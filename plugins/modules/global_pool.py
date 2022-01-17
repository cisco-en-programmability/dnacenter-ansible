#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_pool
short_description: Resource module for Global Pool
description:
- Manage operations create, update and delete of the resource Global Pool.
- API to update global pool.
- API to create global pool.
- API to delete global IP pool.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Global pool id.
    type: str
  settings:
    description: Global Pool's settings.
    suboptions:
      ippool:
        description: Global Pool's ippool.
        suboptions:
          dhcpServerIps:
            description: Dhcp Server Ips.
            elements: str
            type: list
          dnsServerIps:
            description: Dns Server Ips.
            elements: str
            type: list
          gateway:
            description: Gateway.
            type: str
          id:
            description: Id.
            type: str
          ipPoolName:
            description: Ip Pool Name.
            type: str
        type: list
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function delete_global_ip_pool used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    network_settings.NetworkSettings.delete_global_ip_pool

- name: SDK function create_global_pool used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    network_settings.NetworkSettings.create_global_pool

- name: SDK function update_global_pool used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    network_settings.NetworkSettings.update_global_pool

notes:
  - Paths used are put /dna/intent/api/v1/global-pool,
    post /dna/intent/api/v1/global-pool,
    delete /dna/intent/api/v1/global-pool/{id}
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.global_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    settings:
      ippool:
      - dhcpServerIps:
        - string
        dnsServerIps:
        - string
        gateway: string
        id: string
        ipPoolName: string

- name: Create
  cisco.dnac.global_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    settings:
      ippool:
      - IpAddressSpace: string
        dhcpServerIps:
        - string
        dnsServerIps:
        - string
        gateway: string
        ipPoolCidr: string
        ipPoolName: string
        type: string

- name: Delete by id
  cisco.dnac.global_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

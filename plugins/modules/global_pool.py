#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: global_pool
short_description: Resource module for Global Pool
description:
  - This module represents an alias of the module global_pool_v1
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
        elements: dict
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
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings CreateGlobalPoolV1
    description: Complete reference of the CreateGlobalPoolV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-global-pool
  - name: Cisco DNA Center documentation for Network Settings DeleteGlobalIPPoolV1
    description: Complete reference of the DeleteGlobalIPPoolV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-global-ip-pool
  - name: Cisco DNA Center documentation for Network Settings UpdateGlobalPoolV1
    description: Complete reference of the UpdateGlobalPoolV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-global-pool
notes:
  - SDK Method used are network_settings.NetworkSettings.create_global_pool_v1, network_settings.NetworkSettings.delete_global_ip_pool_v1,
    network_settings.NetworkSettings.update_global_pool_v1,
  - Paths used are post /dna/intent/api/v1/global-pool, delete /dna/intent/api/v1/global-pool/{id},
    put /dna/intent/api/v1/global-pool,
  - It should be noted that this module is an alias of global_pool_v1
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

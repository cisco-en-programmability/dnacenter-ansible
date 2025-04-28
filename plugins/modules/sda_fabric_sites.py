#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabric_sites
short_description: Resource module for Sda Fabric Sites
description:
  - This module represents an alias of the module sda_fabric_sites_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the fabric site.
    type: str
  payload:
    description: Sda Fabric Sites's payload.
    elements: dict
    suboptions:
      authenticationProfileName:
        description: Authentication profile used for this fabric.
        type: str
      isPubSubEnabled:
        description: Specifies whether this fabric site will use pub/sub for control
          nodes.
        type: bool
      siteId:
        description: ID of the network hierarchy.
        type: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA AddFabricSiteV1
    description: Complete reference of the AddFabricSiteV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-fabric-site
  - name: Cisco DNA Center documentation for SDA DeleteFabricSiteByIdV1
    description: Complete reference of the DeleteFabricSiteByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-fabric-site-by-id
  - name: Cisco DNA Center documentation for SDA UpdateFabricSiteV1
    description: Complete reference of the UpdateFabricSiteV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-fabric-site
notes:
  - SDK Method used are sda.Sda.add_fabric_site_v1, sda.Sda.delete_fabric_site_by_id_v1,
    sda.Sda.update_fabric_site_v1,
  - Paths used are post /dna/intent/api/v1/sda/fabricSites, delete /dna/intent/api/v1/sda/fabricSites/{id},
    put /dna/intent/api/v1/sda/fabricSites,
  - It should be noted that this module is an alias of sda_fabric_sites_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_fabric_sites:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - authenticationProfileName: string
        isPubSubEnabled: true
        siteId: string
- name: Update all
  cisco.dnac.sda_fabric_sites:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - authenticationProfileName: string
        id: string
        isPubSubEnabled: true
        siteId: string
- name: Delete by id
  cisco.dnac.sda_fabric_sites:
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
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

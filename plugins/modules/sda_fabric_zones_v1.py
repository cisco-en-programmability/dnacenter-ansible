#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_zones_v1
short_description: Resource module for Sda Fabric Zones V1
description:
- Manage operations create, update and delete of the resource Sda Fabric Zones V1.
- Adds a fabric zone based on user input.
- Deletes a fabric zone based on id.
- Updates a fabric zone based on user input.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the fabric zone.
    type: str
  payload:
    description: Sda Fabric Zones's payload.
    elements: dict
    suboptions:
      authenticationProfileName:
        description: Authentication profile used for this fabric.
        type: str
      id:
        description: ID of the fabric zone (updating this field is not allowed).
        type: str
      siteId:
        description: ID of the network hierarchy (updating this field is not allowed).
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA AddFabricZoneV1
  description: Complete reference of the AddFabricZoneV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-fabric-zone
- name: Cisco DNA Center documentation for SDA DeleteFabricZoneByIdV1
  description: Complete reference of the DeleteFabricZoneByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-fabric-zone-by-id
- name: Cisco DNA Center documentation for SDA UpdateFabricZoneV1
  description: Complete reference of the UpdateFabricZoneV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-fabric-zone
notes:
  - SDK Method used are
    sda.Sda.add_fabric_zone_v1,
    sda.Sda.delete_fabric_zone_by_id_v1,
    sda.Sda.update_fabric_zone_v1,

  - Paths used are
    post /dna/intent/api/v1/sda/fabricZones,
    delete /dna/intent/api/v1/sda/fabricZones/{id},
    put /dna/intent/api/v1/sda/fabricZones,

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sda_fabric_zones_v1:
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
      siteId: string

- name: Create
  cisco.dnac.sda_fabric_zones_v1:
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
      siteId: string

- name: Delete by id
  cisco.dnac.sda_fabric_zones_v1:
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

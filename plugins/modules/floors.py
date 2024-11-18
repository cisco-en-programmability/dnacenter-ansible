#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: floors
short_description: Resource module for Floors
description:
- This module represents an alias of the module floors_v2
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  floorNumber:
    description: Floor number.
    type: int
  height:
    description: Floor height. Example 10.1.
    type: float
  id:
    description: Id path parameter. Floor Id.
    type: str
  length:
    description: Floor length. Example 110.3.
    type: float
  name:
    description: Floor name.
    type: str
  parentId:
    description: Parent Id.
    type: str
  rfModel:
    description: RF Model.
    type: str
  unitsOfMeasure:
    description: Units Of Measure.
    type: str
  width:
    description: Floor width. Example 100.5.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design CreatesAFloorV2
  description: Complete reference of the CreatesAFloorV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!creates-a-floor-v-2
- name: Cisco DNA Center documentation for Site Design DeletesAFloorV2
  description: Complete reference of the DeletesAFloorV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!deletes-a-floor-v-2
- name: Cisco DNA Center documentation for Site Design UpdatesAFloorV2
  description: Complete reference of the UpdatesAFloorV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!updates-a-floor-v-2
notes:
  - SDK Method used are
    site_design.SiteDesign.creates_a_floor_v2,
    site_design.SiteDesign.deletes_a_floor_v2,
    site_design.SiteDesign.updates_a_floor_v2,

  - Paths used are
    post /dna/intent/api/v2/floors,
    delete /dna/intent/api/v2/floors/{id},
    put /dna/intent/api/v2/floors/{id},
  - It should be noted that this module is an alias of floors_v2

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.floors:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    floorNumber: 0
    height: 0
    length: 0
    name: string
    parentId: string
    rfModel: string
    unitsOfMeasure: string
    width: 0

- name: Update by id
  cisco.dnac.floors:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    floorNumber: 0
    height: 0
    id: string
    length: 0
    name: string
    parentId: string
    rfModel: string
    unitsOfMeasure: string
    width: 0

- name: Delete by id
  cisco.dnac.floors:
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
  description:
    - This alias returns the output of floors_v2.
"""
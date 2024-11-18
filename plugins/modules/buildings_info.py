#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: buildings_info
short_description: Information module for Buildings Info
description:
- This module represents an alias of the module buildings_v2_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Building Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetsABuildingV2
  description: Complete reference of the GetsABuildingV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-a-building-v-2
notes:
  - SDK Method used are
    site_design.SiteDesign.gets_a_building_v2,

  - Paths used are
    get /dna/intent/api/v2/buildings/{id},
  - It should be noted that this module is an alias of buildings_v2_info

"""

EXAMPLES = r"""
- name: Get Buildings Info by id
  cisco.dnac.buildings_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of buildings_v2_info.
"""
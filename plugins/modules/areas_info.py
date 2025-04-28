#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: areas_info
short_description: Information module for Areas Info
description:
  - This module represents an alias of the module areas_v1_info
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
      - Id path parameter. Area Id.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design GetsAnAreaV1
    description: Complete reference of the GetsAnAreaV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-an-area
notes:
  - SDK Method used are site_design.SiteDesign.gets_an_area_v1,
  - Paths used are get /dna/intent/api/v1/areas/{id},
  - It should be noted that this module is an alias of areas_v1_info
"""
EXAMPLES = r"""
- name: Get Areas Info by id
  cisco.dnac.areas_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "name": "string",
        "nameHierarchy": "string",
        "parentId": "string",
        "type": "string"
      },
      "version": "string"
    }
"""

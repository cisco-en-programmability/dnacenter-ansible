#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_count_info
short_description: Information module for Sites Count Info
description:
- This module represents an alias of the module sites_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
    - Name query parameter. Site name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetSitesCountV1
  description: Complete reference of the GetSitesCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-sites-count
notes:
  - SDK Method used are
    site_design.SiteDesign.get_sites_count_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/count,
  - It should be noted that this module is an alias of sites_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Sites Count Info
  cisco.dnac.sites_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "response": {
          "count": 0
        },
        "version": "string"
      }
    ]
"""

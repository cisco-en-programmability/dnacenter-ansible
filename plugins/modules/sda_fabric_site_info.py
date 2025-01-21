#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_fabric_site_info
short_description: Information module for Sda Fabric Site Info
description:
- This module represents an alias of the module sda_fabric_site_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteNameHierarchy:
    description:
    - SiteNameHierarchy query parameter. Site Name Hierarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetSiteFromSDAFabricV1
  description: Complete reference of the GetSiteFromSDAFabricV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_site,

  - Paths used are
    get /dna/intent/api/v1/business/sda/fabric-site,
  - It should be noted that this module is an alias of sda_fabric_site_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Fabric Site Info
  cisco.dnac.sda_fabric_site_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "siteNameHierarchy": "string",
      "fabricName": "string",
      "fabricType": "string",
      "fabricDomainType": "string",
      "status": "string",
      "description": "string"
    }
"""

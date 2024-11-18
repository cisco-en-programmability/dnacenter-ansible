#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_wireless_settings_ssids_info
short_description: Information module for Sites Wireless Settings Ssids Info
description:
- This module represents an alias of the module sites_wireless_settings_ssids_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId path parameter. Site UUID.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: float
  offset:
    description:
    - Offset query parameter.
    type: float
  id:
    description:
    - Id path parameter. SSID ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetSSIDByIDV1
  description: Complete reference of the GetSSIDByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-by-id-v-1
- name: Cisco DNA Center documentation for Wireless GetSSIDBySiteV1
  description: Complete reference of the GetSSIDBySiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-by-site-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_by_id_v1,
    wireless.Wireless.get_ssid_by_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids,
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/{id},
  - It should be noted that this module is an alias of sites_wireless_settings_ssids_v1_info

"""

EXAMPLES = r"""
- name: Get all Sites Wireless Settings Ssids Info
  cisco.dnac.sites_wireless_settings_ssids_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    siteId: string
  register: result

- name: Get Sites Wireless Settings Ssids Info by id
  cisco.dnac.sites_wireless_settings_ssids_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of sites_wireless_settings_ssids_v1_info.
"""

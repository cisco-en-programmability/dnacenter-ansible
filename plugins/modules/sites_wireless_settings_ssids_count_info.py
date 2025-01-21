#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_wireless_settings_ssids_count_info
short_description: Information module for Sites Wireless Settings Ssids Count Info
description:
- This module represents an alias of the module sites_wireless_settings_ssids_count_v1_info
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
  _inherited:
    description:
    - >
      _inherited query parameter. This query parameter indicates whether the current SSID count at the given
      'siteId' is of the SSID(s) it is inheriting or count of non-inheriting SSID(s).
    type: bool
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetSSIDCountBySiteV1
  description: Complete reference of the GetSSIDCountBySiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-count-by-site
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_count_by_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/count,
  - It should be noted that this module is an alias of sites_wireless_settings_ssids_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Sites Wireless Settings Ssids Count Info
  cisco.dnac.sites_wireless_settings_ssids_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: True
    siteId: string
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
        "count": 0
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_wirelessSettings_ssids_count_info
short_description: Information module for Sites Wirelesssettings Ssids Count
description:
- Get all Sites Wirelesssettings Ssids Count.
- This API allows the user to get count of all SSIDs Service Set Identifier present at global site.
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
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetSSIDCountBySite
  description: Complete reference of the GetSSIDCountBySite API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-count-by-site
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_count_by_site,

  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/count,

"""

EXAMPLES = r"""
- name: Get all Sites Wirelesssettings Ssids Count
  cisco.dnac.sites_wirelessSettings_ssids_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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

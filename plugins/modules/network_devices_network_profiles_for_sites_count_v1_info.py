#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_network_profiles_for_sites_count_v1_info
short_description: Information module for Network Devices Network Profiles For Sites Count V1
description:
- Get all Network Devices Network Profiles For Sites Count V1.
- Retrieves the count of network profiles for sites.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  type:
    description:
    - Type query parameter. Filter the response to only count profiles of a given type.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design RetrievesTheCountOfNetworkProfilesForSitesV1
  description: Complete reference of the RetrievesTheCountOfNetworkProfilesForSitesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-network-profiles-for-sites
notes:
  - SDK Method used are
    site_design.SiteDesign.retrieves_the_count_of_network_profiles_for_sites_v1,

  - Paths used are
    get /dna/intent/api/v1/networkProfilesForSites/count,

"""

EXAMPLES = r"""
- name: Get all Network Devices Network Profiles For Sites Count V1
  cisco.dnac.network_devices_network_profiles_for_sites_count_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    type: string
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

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: business_sda_hostonboarding_ssid_ippool_info
short_description: Information module for Business Sda Hostonboarding Ssid Ippool Info
description:
- This module represents an alias of the module business_sda_hostonboarding_ssid_ippool_v1_info
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  vlanName:
    description:
    - VlanName query parameter. VLAN Name.
    type: str
  siteNameHierarchy:
    description:
    - SiteNameHierarchy query parameter. Site Name Heirarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Fabric Wireless GetSSIDToIPPoolMappingV1
  description: Complete reference of the GetSSIDToIPPoolMappingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-to-ip-pool-mapping
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.get_ssid_to_ip_pool_mapping_v1,

  - Paths used are
    get /dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool,
  - It should be noted that this module is an alias of business_sda_hostonboarding_ssid_ippool_v1_info

"""

EXAMPLES = r"""
- name: Get all Business Sda Hostonboarding Ssid Ippool Info
  cisco.dnac.business_sda_hostonboarding_ssid_ippool_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    vlanName: string
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
      "vlanName": "string",
      "ssidDetails": [
        {
          "name": "string",
          "scalableGroupName": "string"
        }
      ]
    }
"""

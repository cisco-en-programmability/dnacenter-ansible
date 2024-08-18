#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: siteWiseProductNames_count_info
short_description: Information module for Sitewiseproductnames Count
description:
- Get all Sitewiseproductnames Count.
- Returns the count of network device product names for given filters. The default value of `siteId` is global.
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
    - >
      SiteId query parameter. Site identifier to get the list of all available products under the site. The
      default value is global site id. See https //developer.cisco.com/docs/dna-center/get-site/ for siteId.
    type: str
  productName:
    description:
    - >
      ProductName query parameter. Filter with network device product name. Supports partial case-insensitive
      search. A minimum of 3 characters are required for search.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) ReturnsTheCountOfNetworkDeviceProductNamesForASite
  description: Complete reference of the ReturnsTheCountOfNetworkDeviceProductNamesForASite API.
  link: https://developer.cisco.com/docs/dna-center/#!returns-the-count-of-network-device-product-names-for-a-site
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.returns_the_count_of_network_device_product_names_for_a_site,

  - Paths used are
    get /dna/intent/api/v1/siteWiseProductNames/count,

"""

EXAMPLES = r"""
- name: Get all Sitewiseproductnames Count
  cisco.dnac.siteWiseProductNames_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    productName: string
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

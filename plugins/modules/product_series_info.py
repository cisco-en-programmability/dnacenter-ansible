#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: product_series_info
short_description: Information module for Product Series
description:
  - Get all Product Series.
  - Get Product Series by id.
  - Get the list of network device product series and their ordinal on filter criteria.
  - Get the network device product series, its ordinal.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
      - >
        Name query parameter. Product series name. Supports partial case-insensitive search. A minimum of 3
        characters is required for the search.
    type: str
  offset:
    description:
      - >
        Offset query parameter. The first record to show for this page; the first record is numbered 1. The
        minimum value is 1.
    type: int
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. The minimum and maximum values are 1
        and 500, respectively.
    type: int
  productSeriesOrdinal:
    description:
      - ProductSeriesOrdinal path parameter. Unique identifier of product series.
    type: float
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) RetrieveNetworkDeviceProductSeries
    description: Complete reference of the RetrieveNetworkDeviceProductSeries API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-network-device-product-series
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) RetrievesTheListOfNetworkDeviceProductSeries
    description: Complete reference of the RetrievesTheListOfNetworkDeviceProductSeries API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-device-product-series
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.retrieve_network_device_product_series,
    software_image_management_swim.SoftwareImageManagementSwim.retrieves_the_list_of_network_device_product_series,
  - Paths used are
    get /dna/intent/api/v1/productSeries,
    get /dna/intent/api/v1/productSeries/{productSeriesOrdinal},
"""

EXAMPLES = r"""
---
- name: Get all Product Series
  cisco.dnac.product_series_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    offset: 0
    limit: 0
  register: result
- name: Get Product Series by id
  cisco.dnac.product_series_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    productSeriesOrdinal: 0
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

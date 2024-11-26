#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_query_count_v1
short_description: Resource module for Network Devices Query Count V1
description:
- Manage operation create of the resource Network Devices Query Count V1.
- >
   Gets the total number Network Devices based on the provided complex filters and aggregation functions. For
   detailed information about the usage of the API, please refer to the Open API specification document - https
   //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
   AssuranceNetworkDevices-1.0.2-resolved.yaml.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Network Devices Query Count's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Function.
        type: str
      name:
        description: Name.
        type: str
    type: list
  attributes:
    description: Attributes.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  filters:
    description: Network Devices Query Count's filters.
    elements: dict
    suboptions:
      key:
        description: Key.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: str
    type: list
  page:
    description: Network Devices Query Count's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      sortBy:
        description: Network Devices Query Count's sortBy.
        elements: dict
        suboptions:
          name:
            description: Name.
            type: str
          order:
            description: Order.
            type: str
        type: list
    type: dict
  startTime:
    description: Start Time.
    type: int
  views:
    description: Views.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctionsV1  # noqa: E501
  description: Complete reference of the GetsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctionsV1 API.  # noqa: E501
  link: https://developer.cisco.com/docs/dna-center/#!gets-the-total-number-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions  # noqa: E501
notes:
  - SDK Method used are
    devices.Devices.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1,  # noqa: E501

  - Paths used are
    post /data/api/v1/networkDevices/query/count,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.network_devices_query_count_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    aggregateAttributes:
    - function: string
      name: string
    attributes:
    - string
    endTime: 0
    filters:
    - key: string
      operator: string
      value: string
    page:
      limit: 0
      offset: 0
      sortBy:
      - name: string
        order: string
    startTime: 0
    views:
    - string

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

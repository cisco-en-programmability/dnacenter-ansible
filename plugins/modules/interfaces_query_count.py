#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: interfaces_query_count
short_description: Resource module for Interfaces Query Count
description:
- This module represents an alias of the module interfaces_query_count_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Interfaces Query Count's aggregateAttributes.
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
    description: Interfaces Query Count's filters.
    elements: dict
    suboptions:
      filters:
        description: Filters.
        elements: str
        type: list
      key:
        description: Key.
        type: str
      logicalOperator:
        description: Logical Operator.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: dict
    type: list
  page:
    description: Interfaces Query Count's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      sortBy:
        description: Interfaces Query Count's sortBy.
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
- name: Cisco DNA Center documentation for Devices TheTotalInterfacesCountAcrossTheNetworkDevicesV1
  description: Complete reference of the TheTotalInterfacesCountAcrossTheNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!the-total-interfaces-count-across-the-network-devices
notes:
  - SDK Method used are
    devices.Devices.the_total_interfaces_count_across_the_network_devices_v1,

  - Paths used are
    post /dna/data/api/v1/interfaces/query/count,
  - It should be noted that this module is an alias of interfaces_query_count_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.interfaces_query_count:
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
    - filters:
      - string
      key: string
      logicalOperator: string
      operator: string
      value: {}
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

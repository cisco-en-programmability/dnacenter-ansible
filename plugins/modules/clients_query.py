#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: clients_query
short_description: Resource module for Clients Query
description:
- This module represents an alias of the module clients_query_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Clients Query's aggregateAttributes.
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
    description: Clients Query's filters.
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
        type: int
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Clients Query's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      sortBy:
        description: Clients Query's sortBy.
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
- name: Cisco DNA Center documentation for Clients RetrievesTheListOfClientsByApplyingComplexFiltersWhileAlsoSupportingAggregateAttributesV1
  description: Complete reference of the RetrievesTheListOfClientsByApplyingComplexFiltersWhileAlsoSupportingAggregateAttributesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-clients-by-applying-complex-filters-while-also-supporting-aggregate-attributes-v-1
notes:
  - SDK Method used are
    clients.Clients.retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1,

  - Paths used are
    post /dna/data/api/v1/clients/query,
  - It should be noted that this module is an alias of clients_query_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.clients_query:
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
      value: 0
    headers: '{{my_headers | from_json}}'
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
  This alias returns the output of clients_query_v1.
"""

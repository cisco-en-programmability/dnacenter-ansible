#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dns_services_query_count
short_description: Resource module for Dns Services Query Count
description:
  - This module represents an alias of the module dns_services_query_count_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  filters:
    description: Dns Services Query Count's filters.
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
        elements: str
        type: list
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Start Time.
    type: int
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices RetrievesTheTotalNumberOfDNSServicesForGivenSetOfComplexFiltersV1
    description: Complete reference of the RetrievesTheTotalNumberOfDNSServicesForGivenSetOfComplexFiltersV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-dns-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1,
  - Paths used are post /dna/data/api/v1/dnsServices/query/count,
  - It should be noted that this module is an alias of dns_services_query_count_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.dns_services_query_count:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    endTime: 0
    filters:
      - key: string
        operator: string
        value:
          - string
    headers: '{{my_headers | from_json}}'
    startTime: 0
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

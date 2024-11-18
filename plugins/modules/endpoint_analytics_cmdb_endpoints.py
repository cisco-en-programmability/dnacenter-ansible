#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: endpoint_analytics_cmdb_endpoints
short_description: Resource module for Endpoint Analytics Cmdb Endpoints
description:
- This module represents an alias of the module endpoint_analytics_cmdb_endpoints_v1
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Endpoint Analytics Cmdb Endpoints's payload.
    elements: dict
    suboptions:
      assetTag:
        description: Asset tag.
        type: str
      department:
        description: Department that asset belongs to.
        type: str
      displayName:
        description: Display name of the asset.
        type: str
      lastUpdateTimestamp:
        description: Last update timestamp in epoch milliseconds.
        type: int
      location:
        description: Location of the asset.
        type: str
      macAddress:
        description: MAC address of the endpoint.
        type: str
      managedBy:
        description: Asset managed by.
        type: str
      model:
        description: Asset model.
        type: str
      modelCategory:
        description: Category of the model.
        type: str
      serialNumber:
        description: Serial number of the endpoint.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for AI Endpoint Analytics ProcessCMDBEndpointsV1
  description: Complete reference of the ProcessCMDBEndpointsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!process-cmdb-endpoints-v-1
notes:
  - SDK Method used are
    ai_endpoint_analytics.AIEndpointAnalytics.process_cmdb_endpoints_v1,

  - Paths used are
    post /dna/intent/api/v1/endpoint-analytics/cmdb/endpoints,
  - It should be noted that this module is an alias of endpoint_analytics_cmdb_endpoints_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.endpoint_analytics_cmdb_endpoints:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - assetTag: string
      department: string
      displayName: string
      lastUpdateTimestamp: 0
      location: string
      macAddress: string
      managedBy: string
      model: string
      modelCategory: string
      serialNumber: string

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of endpoint_analytics_cmdb_endpoints_v1.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: endpoint_analytics_endpoints
short_description: Resource module for Endpoint Analytics Endpoints
description:
  - This module represents an alias of the module endpoint_analytics_endpoints_v1
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceType:
    description: Type of the device represented by this endpoint.
    type: str
  epId:
    description: EpId path parameter. Unique identifier for the endpoint.
    type: str
  hardwareManufacturer:
    description: Hardware manufacturer for the endpoint.
    type: str
  hardwareModel:
    description: Hardware model of the endpoint.
    type: str
  macAddress:
    description: MAC address of the endpoint.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for AI Endpoint Analytics RegisterAnEndpointV1
    description: Complete reference of the RegisterAnEndpointV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!register-an-endpoint
  - name: Cisco DNA Center documentation for AI Endpoint Analytics DeleteAnEndpointV1
    description: Complete reference of the DeleteAnEndpointV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-an-endpoint
  - name: Cisco DNA Center documentation for AI Endpoint Analytics UpdateARegisteredEndpointV1
    description: Complete reference of the UpdateARegisteredEndpointV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-a-registered-endpoint
notes:
  - SDK Method used are a_i_endpoint_analytics.AIEndpointAnalytics.delete_an_endpoint_v1,
    a_i_endpoint_analytics.AIEndpointAnalytics.register_an_endpoint_v1, a_i_endpoint_analytics.AIEndpointAnalytics.update_a_registered_endpoint_v1,
  - Paths used are post /dna/intent/api/v1/endpoint-analytics/endpoints, delete /dna/intent/api/v1/endpoint-analytics/endpoints/{epId},
    put /dna/intent/api/v1/endpoint-analytics/endpoints/{epId},
  - It should be noted that this module is an alias of endpoint_analytics_endpoints_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.endpoint_analytics_endpoints:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    deviceType: string
    hardwareManufacturer: string
    hardwareModel: string
    macAddress: string
- name: Update by id
  cisco.dnac.endpoint_analytics_endpoints:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    deviceType: string
    epId: string
    hardwareManufacturer: string
    hardwareModel: string
- name: Delete by id
  cisco.dnac.endpoint_analytics_endpoints:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    epId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""

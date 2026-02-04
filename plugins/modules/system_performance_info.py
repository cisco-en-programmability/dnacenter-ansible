#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_performance_info
short_description: Information module for System Performance
description:
  - Get all System Performance. - > Retrieves the average values of cluster key performance indicators KPIs , such as CPU
    utilization, memory utilization or network rates over the past 15 minutes. Query parameters 'function', 'startTime' and
    'endTime' are no longer supported.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  kpi:
    description:
      - Kpi query parameter. Valid values cpu,memory,network.
    type: str
  function:
    description:
      - >
        Function query parameter. In this release this field has been deprecated and no longer supported.
        Previously supported functions were 'sum', 'average', and 'max'. Now, only the last 15 minutes average
        of cluster key performance indicators (KPIs) is returned, regardless of the specified function. For
        example, if 'sum', 'average', or 'max' is provided, it will be ignored and the 'average' of the last 15
        minutes will be returned.
    type: str
  startTime:
    description:
      - >
        StartTime query parameter. In this release this field has been deprecated and no longer supported. Only
        the last 15 minutes average of cluster key performance indicators (KPIs) is returned, regardless of the
        provided epoch time. For example, if any epoch time is specified for this field, it will be ignored and
        15 minutes before the current time will be considered.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. In this release this field has been deprecated and no longer supported. Only
        the last 15 minutes average of cluster key performance indicators (KPIs) is returned, regardless of the
        provided epoch time. For example, if any epoch time is specified for this field, it will be ignored and
        the current time will be considered.
    type: float
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Health and Performance SystemPerformanceAPI
    description: Complete reference of the SystemPerformanceAPI API.
    link: https://developer.cisco.com/docs/dna-center/#!system-performance-api
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.system_performance,
  - Paths used are
    get /dna/intent/api/v1/diagnostics/system/performance,
"""

EXAMPLES = r"""
---
- name: Get all System Performance
  cisco.dnac.system_performance_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    kpi: string
    function: string
    startTime: 0
    endTime: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "hostName": "string",
      "version": "string",
      "kpis": {
        "cpu": {
          "units": "string",
          "utilization": "string"
        },
        "memory": {
          "units": "string",
          "utilization": "string"
        },
        "network tx_rate": {
          "units": "string",
          "utilization": "string"
        },
        "network rx_rate": {
          "units": "string",
          "utilization": "string"
        }
      }
    }
"""

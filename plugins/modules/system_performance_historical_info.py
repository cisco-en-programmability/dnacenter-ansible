#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_performance_historical_info
short_description: Information module for System Performance Historical
description:
  - Get all System Performance Historical. - > Retrieves hourly data of cluster key performance indicators KPIs , like CPU
    utilization, memory utilization or network rates for the past 24 hours. Query parameters 'startTime' and 'endTime' are
    no longer supported.
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
      - Kpi query parameter. Fetch historical data for this kpi. Valid values cpu,memory,network.
    type: str
  startTime:
    description:
      - >
        StartTime query parameter. In this release this field has been deprecated and no longer supported. This
        is restricted to a 24-hour time range with hourly samples, regardless of the provided epoch time. For
        example, if any epoch time is specified for this field, it will be ignored and 24 hours before the
        current time will be considered.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. In this release this field has been deprecated and no longer supported. This is
        restricted to a 24-hour time range with hourly samples, regardless of the provided epoch time. For
        example, if any epoch time is specified for this field, it will be ignored and the current time will be
        considered.
    type: float
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Health and Performance SystemPerformanceHistoricalAPI
    description: Complete reference of the SystemPerformanceHistoricalAPI API.
    link: https://developer.cisco.com/docs/dna-center/#!system-performance-historical-api
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.system_performance_historical,
  - Paths used are
    get /dna/intent/api/v1/diagnostics/system/performance/history,
"""

EXAMPLES = r"""
---
- name: Get all System Performance Historical
  cisco.dnac.system_performance_historical_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    kpi: string
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

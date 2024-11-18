#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_sensor_test_results_info
short_description: Information module for Wireless Sensor Test Results Info
description:
- This module represents an alias of the module wireless_sensor_test_results_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId query parameter. Assurance site UUID.
    type: str
  startTime:
    description:
    - StartTime query parameter. The epoch time in milliseconds.
    type: float
  endTime:
    description:
    - EndTime query parameter. The epoch time in milliseconds.
    type: float
  testFailureBy:
    description:
    - >
      TestFailureBy query parameter. Obtain failure statistics group by "area", "building", or "floor" (case
      insensitive).
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless SensorTestResultsV1
  description: Complete reference of the SensorTestResultsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!sensor-test-results-v-1
notes:
  - SDK Method used are
    wireless.Wireless.sensor_test_results_v1,

  - Paths used are
    get /dna/intent/api/v1/AssuranceGetSensorTestResults,
  - It should be noted that this module is an alias of wireless_sensor_test_results_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Sensor Test Results Info
  cisco.dnac.wireless_sensor_test_results_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    startTime: 0
    endTime: 0
    testFailureBy: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of wireless_sensor_test_results_v1_info.
"""

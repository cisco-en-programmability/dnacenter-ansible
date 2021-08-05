#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: applications_health_info
short_description: Information module for Applications Health
description:
- Get all Applications Health.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  siteId:
    description:
    - SiteId query parameter. Assurance site UUID value (Cannot be submitted together with deviceId and clientMac).
    type: str
  deviceId:
    description:
    - DeviceId query parameter. Assurance device UUID value (Cannot be submitted together with siteId and clientMac).
    type: str
  macAddress:
    description:
    - MacAddress query parameter. Client device's MAC address (Cannot be submitted together with siteId and deviceId).
    type: str
  startTime:
    description:
    - StartTime query parameter. Starting epoch time in milliseconds of time window.
    type: int
  endTime:
    description:
    - EndTime query parameter. Ending epoch time in milliseconds of time window.
    type: int
  applicationHealth:
    description:
    - >
      ApplicationHealth query parameter. Application health category (POOR, FAIR, or GOOD. Optionally use with
      siteId only).
    type: str
  offset:
    description:
    - >
      Offset query parameter. The offset of the first application in the returned data (optionally used with
      siteId only).
    type: int
  limit:
    description:
    - >
      Limit query parameter. The max number of application entries in returned data 1, 1000 (optionally used with
      siteId only).
    type: int
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Applications Health reference
  description: Complete reference of the Applications Health object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Applications Health
  cisco.dnac.applications_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    siteId: string
    deviceId: string
    macAddress: string
    startTime: 0
    endTime: 0
    applicationHealth: string
    offset: 0
    limit: 0
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "totalCount": 0,
      "response": [
        {
          "name": "string",
          "health": {},
          "businessRelevance": "string",
          "trafficClass": "string",
          "usageBytes": 0,
          "averageThroughput": 0,
          "packetLossPercent": {},
          "networkLatency": {},
          "jitter": {},
          "applicationServerLatency": {},
          "clientNetworkLatency": {},
          "serverNetworkLatency": {}
        }
      ]
    }
"""

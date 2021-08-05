#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_health_info
short_description: Information module for Site Health
description:
- Get all Site Health.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  timestamp:
    description:
    - Timestamp query parameter. Epoch time(in milliseconds) when the Site Hierarchy data is required.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Site Health reference
  description: Complete reference of the Site Health object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Site Health
  cisco.dnac.site_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    timestamp: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "siteName": "string",
        "siteId": "string",
        "parentSiteId": "string",
        "parentSiteName": "string",
        "siteType": "string",
        "latitude": 0,
        "longitude": 0,
        "healthyNetworkDevicePercentage": {},
        "healthyClientsPercentage": {},
        "clientHealthWired": {},
        "clientHealthWireless": {},
        "numberOfClients": {},
        "numberOfNetworkDevice": {},
        "networkHealthAverage": {},
        "networkHealthAccess": {},
        "networkHealthCore": {},
        "networkHealthDistribution": {},
        "networkHealthRouter": {},
        "networkHealthWireless": {},
        "networkHealthOthers": {},
        "numberOfWiredClients": {},
        "numberOfWirelessClients": {},
        "totalNumberOfConnectedWiredClients": {},
        "totalNumberOfActiveWirelessClients": {},
        "wiredGoodClients": {},
        "wirelessGoodClients": {},
        "overallGoodDevices": {},
        "accessGoodCount": {},
        "accessTotalCount": {},
        "coreGoodCount": {},
        "coreTotalCount": {},
        "distributionGoodCount": {},
        "distributionTotalCount": {},
        "routerGoodCount": {},
        "routerTotalCount": {},
        "wirelessDeviceGoodCount": {},
        "wirelessDeviceTotalCount": {},
        "applicationHealth": {},
        "applicationGoodCount": {},
        "applicationTotalCount": {},
        "applicationBytesTotalCount": {},
        "dnacInfo": {},
        "applicationHealthStats": {
          "appTotalCount": 0,
          "businessRelevantAppCount": {
            "poor": 0,
            "fair": 0,
            "good": 0
          },
          "businessIrrelevantAppCount": {
            "poor": 0,
            "fair": 0,
            "good": 0
          },
          "defaultHealthAppCount": {
            "poor": 0,
            "fair": 0,
            "good": 0
          }
        }
      }
    ]
"""

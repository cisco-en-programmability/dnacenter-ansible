#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: user_enrichment_details_info
short_description: Information module for User Enrichment Details
description:
- Get all User Enrichment Details.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: User Enrichment Details reference
  description: Complete reference of the User Enrichment Details object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all User Enrichment Details
  cisco.dnac.user_enrichment_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
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
        "userDetails": {
          "id": "string",
          "connectionStatus": "string",
          "hostType": "string",
          "userId": {},
          "hostName": {},
          "hostOs": {},
          "hostVersion": {},
          "subType": "string",
          "lastUpdated": 0,
          "healthScore": [
            {
              "healthType": "string",
              "reason": "string",
              "score": 0
            }
          ],
          "hostMac": "string",
          "hostIpV4": "string",
          "hostIpV6": [
            {}
          ],
          "authType": {},
          "vlanId": "string",
          "ssid": {},
          "frequency": {},
          "channel": {},
          "apGroup": {},
          "location": {},
          "clientConnection": "string",
          "connectedDevice": [
            {}
          ],
          "issueCount": 0,
          "rssi": {},
          "avgRssi": {},
          "snr": {},
          "avgSnr": {},
          "dataRate": {},
          "txBytes": {},
          "rxBytes": {},
          "dnsSuccess": {},
          "dnsFailure": {},
          "onboarding": {
            "averageRunDuration": {},
            "maxRunDuration": {},
            "averageAssocDuration": {},
            "maxAssocDuration": {},
            "averageAuthDuration": {},
            "maxAuthDuration": {},
            "averageDhcpDuration": {},
            "maxDhcpDuration": {},
            "aaaServerIp": {},
            "dhcpServerIp": {}
          },
          "onboardingTime": {},
          "port": {}
        },
        "connectedDevice": [
          {
            "deviceDetails": {
              "family": "string",
              "type": "string",
              "location": {},
              "errorCode": {},
              "macAddress": "string",
              "role": "string",
              "apManagerInterfaceIp": "string",
              "associatedWlcIp": "string",
              "bootDateTime": "string",
              "collectionStatus": "string",
              "interfaceCount": "string",
              "lineCardCount": "string",
              "lineCardId": "string",
              "managementIpAddress": "string",
              "memorySize": "string",
              "platformId": "string",
              "reachabilityFailureReason": "string",
              "reachabilityStatus": "string",
              "snmpContact": "string",
              "snmpLocation": "string",
              "tunnelUdpPort": {},
              "waasDeviceMode": {},
              "series": "string",
              "inventoryStatusDetail": "string",
              "collectionInterval": "string",
              "serialNumber": "string",
              "softwareVersion": "string",
              "roleSource": "string",
              "hostname": "string",
              "upTime": "string",
              "lastUpdateTime": 0,
              "errorDescription": {},
              "locationName": {},
              "tagCount": "string",
              "lastUpdated": "string",
              "instanceUuid": "string",
              "id": "string",
              "neighborTopology": [
                {
                  "errorCode": 0,
                  "message": "string",
                  "detail": "string"
                }
              ]
            }
          }
        ]
      }
    ]
"""

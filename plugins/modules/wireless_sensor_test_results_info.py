#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_sensor_test_results_info
short_description: Information module for Wireless Sensor Test Results
description:
  - Get all Wireless Sensor Test Results.
  - Intent API to get SENSOR test result summary.
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
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless SensorTestResults
    description: Complete reference of the SensorTestResults API.
    link: https://developer.cisco.com/docs/dna-center/#!sensor-test-results
notes:
  - SDK Method used are
    wireless.Wireless.sensor_test_results,
  - Paths used are
    get /dna/intent/api/v1/AssuranceGetSensorTestResults,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Sensor Test Results
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "name": "string",
        "_id": "string",
        "version": 0,
        "modelVersion": 0,
        "startTime": 0,
        "lastModifiedTime": 0,
        "numAssociatedSensor": 0,
        "location": "string",
        "siteHierarchy": "string",
        "status": "string",
        "connection": "string",
        "actionInProgress": "string",
        "frequency": {
          "value": 0,
          "unit": "string"
        },
        "rssiThreshold": 0,
        "numNeighborAPThreshold": 0,
        "scheduleInDays": 0,
        "wlans": [
          "string"
        ],
        "ssids": [
          {
            "bands": "string",
            "ssid": "string",
            "profileName": "string",
            "numAps": 0,
            "numSensors": 0,
            "layer3webAuthsecurity": "string",
            "layer3webAuthuserName": "string",
            "layer3webAuthpassword": "string",
            "layer3webAuthEmailAddress": "string",
            "thirdParty": {
              "selected": true
            },
            "id": 0,
            "wlanId": 0,
            "wlc": "string",
            "validFrom": 0,
            "validTo": 0,
            "status": "string",
            "proxyServer": "string",
            "proxyPort": "string",
            "proxyUserName": "string",
            "proxyPassword": "string",
            "authType": "string",
            "psk": "string",
            "username": "string",
            "password": "string",
            "passwordType": "string",
            "eapMethod": "string",
            "scep": true,
            "authProtocol": "string",
            "certfilename": "string",
            "certxferprotocol": "string",
            "certstatus": "string",
            "certpassphrase": "string",
            "certdownloadurl": "string",
            "extWebAuthVirtualIp": "string",
            "extWebAuth": true,
            "whiteList": true,
            "extWebAuthPortal": "string",
            "extWebAuthAccessUrl": "string",
            "extWebAuthHtmlTag": [
              {
                "label": "string",
                "tag": "string",
                "value": "string"
              }
            ],
            "qosPolicy": "string",
            "tests": [
              {
                "name": "string",
                "config": [
                  {
                    "domains": [
                      "string"
                    ],
                    "server": "string",
                    "userName": "string",
                    "password": "string",
                    "url": "string",
                    "port": 0,
                    "protocol": "string",
                    "servers": [
                      "string"
                    ],
                    "direction": "string",
                    "startPort": 0,
                    "endPort": 0,
                    "udpBandwidth": 0,
                    "probeType": "string",
                    "numPackets": "string",
                    "pathToDownload": "string",
                    "transferType": "string",
                    "sharedSecret": "string",
                    "ndtServer": "string",
                    "ndtServerPort": "string",
                    "ndtServerPath": "string",
                    "uplinkTest": true,
                    "downlinkTest": true,
                    "proxyServer": "string",
                    "proxyPort": "string",
                    "proxyUserName": "string",
                    "proxyPassword": "string",
                    "userNamePrompt": "string",
                    "passwordPrompt": "string",
                    "exitCommand": "string",
                    "finalPrompt": "string"
                  }
                ]
              }
            ]
          }
        ],
        "profiles": [
          {
            "authType": "string",
            "psk": "string",
            "username": "string",
            "password": "string",
            "passwordType": "string",
            "eapMethod": "string",
            "scep": true,
            "authProtocol": "string",
            "certfilename": "string",
            "certxferprotocol": "string",
            "certstatus": "string",
            "certpassphrase": "string",
            "certdownloadurl": "string",
            "extWebAuthVirtualIp": "string",
            "extWebAuth": true,
            "whiteList": true,
            "extWebAuthPortal": "string",
            "extWebAuthAccessUrl": "string",
            "extWebAuthHtmlTag": [
              {
                "label": "string",
                "tag": "string",
                "value": "string"
              }
            ],
            "qosPolicy": "string",
            "tests": [
              {
                "name": "string",
                "config": [
                  {
                    "domains": [
                      "string"
                    ],
                    "server": "string",
                    "userName": "string",
                    "password": "string",
                    "url": "string",
                    "port": 0,
                    "protocol": "string",
                    "servers": [
                      "string"
                    ],
                    "direction": "string",
                    "startPort": 0,
                    "endPort": 0,
                    "udpBandwidth": 0,
                    "probeType": "string",
                    "numPackets": "string",
                    "pathToDownload": "string",
                    "transferType": "string",
                    "sharedSecret": "string",
                    "ndtServer": "string",
                    "ndtServerPort": "string",
                    "ndtServerPath": "string",
                    "uplinkTest": true,
                    "downlinkTest": true,
                    "proxyServer": "string",
                    "proxyPort": "string",
                    "proxyUserName": "string",
                    "proxyPassword": "string",
                    "userNamePrompt": "string",
                    "passwordPrompt": "string",
                    "exitCommand": "string",
                    "finalPrompt": "string"
                  }
                ]
              }
            ],
            "profileName": "string",
            "deviceType": "string",
            "vlan": "string",
            "locationVlanList": [
              {
                "locationId": "string",
                "vlans": [
                  "string"
                ]
              }
            ]
          }
        ],
        "testScheduleMode": "string",
        "showWlcUpgradeBanner": true,
        "radioAsSensorRemoved": true,
        "encryptionMode": "string",
        "runNow": "string",
        "locationInfoList": [
          {
            "locationId": "string",
            "locationType": "string",
            "allSensors": true,
            "siteHierarchy": "string",
            "macAddressList": [
              "string"
            ],
            "managementVlan": "string",
            "customManagementVlan": true
          }
        ],
        "sensors": [
          {
            "name": "string",
            "macAddress": "string",
            "switchMac": "string",
            "switchUuid": "string",
            "switchSerialNumber": "string",
            "markedForUninstall": true,
            "ipAddress": "string",
            "hostName": "string",
            "wiredApplicationStatus": "string",
            "wiredApplicationMessage": "string",
            "assigned": true,
            "status": "string",
            "xorSensor": true,
            "targetAPs": [
              "string"
            ],
            "runNow": "string",
            "locationId": "string",
            "allSensorAddition": true,
            "configUpdated": "string",
            "sensorType": "string",
            "testMacAddresses": {},
            "id": "string",
            "servicePolicy": "string",
            "iPerfInfo": {}
          }
        ],
        "apCoverage": [
          {
            "bands": "string",
            "numberOfApsToTest": 0,
            "rssiThreshold": 0
          }
        ]
      }
    }
"""

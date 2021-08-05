#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sensor
short_description: Resource module for Sensor
description:
- Manage operations create and delete of the resource Sensor.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  apCoverage:
    description: Sensor's apCoverage.
    suboptions:
      bands:
        description: Sensor's bands.
        type: str
      numberOfApsToTest:
        description: Sensor's numberOfApsToTest.
        type: str
      rssiThreshold:
        description: Sensor's rssiThreshold.
        type: str
    type: list
  connection:
    description: Sensor's connection.
    type: str
  modelVersion:
    description: Sensor's modelVersion.
    type: int
  name:
    description: Sensor's name.
    type: str
  ssids:
    description: Sensor's ssids.
    suboptions:
      authType:
        description: Sensor's authType.
        type: str
      categories:
        description: Sensor's categories.
        elements: str
        type: list
      profileName:
        description: Sensor's profileName.
        type: str
      psk:
        description: Sensor's psk.
        type: str
      qosPolicy:
        description: Sensor's qosPolicy.
        type: str
      ssid:
        description: Sensor's ssid.
        type: str
      tests:
        description: Sensor's tests.
        suboptions:
          config:
            description: Sensor's config.
            elements: dict
            type: list
          name:
            description: Sensor's name.
            type: str
        type: list
      thirdParty:
        description: Sensor's thirdParty.
        suboptions:
          selected:
            description: Selected flag.
            type: bool
        type: dict
    type: list
  templateName:
    description: TemplateName query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sensor reference
  description: Complete reference of the Sensor object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sensor:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    apCoverage:
    - bands: string
      numberOfApsToTest: string
      rssiThreshold: string
    connection: string
    modelVersion: 0
    name: string
    ssids:
    - authType: string
      categories:
      - string
      profileName: string
      psk: string
      qosPolicy: string
      ssid: string
      tests:
      - config:
        - {}
        name: string
      thirdParty:
        selected: true

- name: Delete all
  cisco.dnac.sensor:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    templateName: string

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
        "_id": "string",
        "name": "string",
        "version": 0,
        "modelVersion": 0,
        "startTime": 0,
        "lastModifiedTime": 0,
        "numAssociatedSensor": 0,
        "location": {},
        "siteHierarchy": {},
        "status": "string",
        "connection": "string",
        "frequency": {},
        "rssiThreshold": 0,
        "numNeighborAPThreshold": 0,
        "scheduleInDays": 0,
        "wlans": [
          {}
        ],
        "ssids": [
          {
            "bands": {},
            "ssid": "string",
            "profileName": "string",
            "authType": "string",
            "authTypeRcvd": {},
            "psk": "string",
            "username": {},
            "password": {},
            "eapMethod": {},
            "scep": true,
            "authProtocol": {},
            "certfilename": {},
            "certxferprotocol": "string",
            "certstatus": "string",
            "certpassphrase": {},
            "certdownloadurl": {},
            "numAps": 0,
            "numSensors": 0,
            "layer3webAuthsecurity": {},
            "layer3webAuthuserName": {},
            "layer3webAuthpassword": {},
            "extWebAuthVirtualIp": {},
            "layer3webAuthEmailAddress": {},
            "qosPolicy": "string",
            "extWebAuth": true,
            "whiteList": true,
            "extWebAuthPortal": {},
            "extWebAuthAccessUrl": {},
            "extWebAuthHtmlTag": [
              {}
            ],
            "thirdParty": {
              "selected": true
            },
            "id": 0,
            "wlanId": 0,
            "wlc": {},
            "validFrom": 0,
            "validTo": 0,
            "status": "string",
            "tests": [
              {
                "name": "string",
                "config": [
                  {}
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
          {}
        ],
        "schedule": {},
        "tests": {},
        "sensors": [
          {}
        ],
        "apCoverage": [
          {
            "bands": "string",
            "numberOfApsToTest": 0,
            "rssiThreshold": 0
          }
        ],
        "testDurationEstimate": 0,
        "testTemplate": true,
        "legacyTestSuite": true,
        "tenantId": {}
      }
    }
"""

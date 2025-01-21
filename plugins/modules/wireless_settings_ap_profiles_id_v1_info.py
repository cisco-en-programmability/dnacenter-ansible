#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_ap_profiles_id_v1_info
short_description: Information module for Wireless Settings Ap Profiles Id V1
description:
- Get Wireless Settings Ap Profiles Id V1 by id.
- This API allows the user to get a AP Profile by AP Profile ID that captured in wireless settings design.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Ap Profile ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetAPProfileByIDV1
  description: Complete reference of the GetAPProfileByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ap-profile-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_ap_profile_by_id_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/apProfiles/{id},

"""

EXAMPLES = r"""
- name: Get Wireless Settings Ap Profiles Id V1 by id
  cisco.dnac.wireless_settings_ap_profiles_id_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "apProfileName": "string",
          "description": "string",
          "remoteWorkerEnabled": true,
          "managementSetting": {
            "authType": "string",
            "dot1xUsername": "string",
            "dot1xPassword": "string",
            "sshEnabled": true,
            "telnetEnabled": true,
            "managementUserName": "string",
            "managementPassword": "string",
            "managementEnablePassword": "string",
            "cdpState": true
          },
          "awipsEnabled": true,
          "awipsForensicEnabled": true,
          "rogueDetectionSetting": {
            "rogueDetection": true,
            "rogueDetectionMinRssi": 0,
            "rogueDetectionTransientInterval": 0,
            "rogueDetectionReportInterval": 0
          },
          "pmfDenialEnabled": true,
          "meshEnabled": true,
          "meshSetting": {
            "bridgeGroupName": "string",
            "backhaulClientAccess": true,
            "range": 0,
            "ghz5BackhaulDataRates": "string",
            "ghz24BackhaulDataRates": "string",
            "rapDownlinkBackhaul": "string"
          },
          "apPowerProfileName": "string",
          "calendarPowerProfiles": {
            "powerProfileName": "string",
            "schedulerType": "string",
            "duration": {
              "schedulerStartTime": "string",
              "schedulerEndTime": "string",
              "schedulerDay": "string",
              "schedulerDate": "string"
            }
          },
          "countryCode": "string",
          "timeZone": "string",
          "timeZoneOffsetHour": 0,
          "timeZoneOffsetMinutes": 0,
          "clientLimit": 0
        }
      ],
      "version": "string"
    }
"""

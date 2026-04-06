#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_summarys_info
short_description: Information module for Discoverys Jobs Summarys
description:
  - Get all Discoverys Jobs Summarys. - > API to fetch the summary of all discoveries. The response includes the basic details
    of all discoveries, latest job status and the number of reachable devices.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices FetchesTheSummaryOfAllDiscoveriesWithLatestJobs
    description: Complete reference of the FetchesTheSummaryOfAllDiscoveriesWithLatestJobs API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-the-summary-of-all-discoveries-with-latest-jobs
notes:
  - SDK Method used are
    devices.Devices.fetches_the_summary_of_all_discoveries_with_latest_jobs,
  - Paths used are
    get /dna/intent/api/v1/discoverys/jobs/summarys,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Jobs Summarys
  cisco.dnac.discoverys_jobs_summarys_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "name": "string",
        "managementIpSelectionMethod": "string",
        "discoveryTypeDetails": {
          "type": "string",
          "ipAddress": "string",
          "range": [
            {
              "ipAddressStart": "string",
              "ipAddressEnd": "string"
            }
          ],
          "cidrAddress": {
            "cidrPrefix": "string",
            "cidrSuffix": 0
          },
          "subnetFilter": {
            "ipAddress": "string",
            "cidrAddress": {
              "cidrPrefix": "string",
              "cidrSuffix": 0
            }
          },
          "hopCount": 0
        },
        "onlyNewDevice": true,
        "updateManagementIp": true,
        "credentials": {
          "cli": {
            "description": "string",
            "username": "string",
            "globalCredentialIdList": [
              "string"
            ],
            "protocolOrder": "string"
          },
          "snmp": {
            "snmpV2Read": {
              "description": "string",
              "globalCredentialIdList": [
                "string"
              ]
            },
            "snmpV2Write": {
              "description": "string",
              "globalCredentialIdList": [
                "string"
              ]
            },
            "snmpV3": {
              "description": "string",
              "mode": "string",
              "username": "string",
              "authType": "string",
              "privacyType": "string",
              "globalCredentialIdList": [
                "string"
              ]
            },
            "retries": 0,
            "timeout": 0
          },
          "httpRead": {
            "description": "string",
            "username": "string",
            "port": 0,
            "protocol": "string",
            "globalCredentialIdList": [
              "string"
            ]
          },
          "httpWrite": {
            "description": "string",
            "username": "string",
            "port": 0,
            "protocol": "string",
            "globalCredentialIdList": [
              "string"
            ]
          },
          "netconf": {
            "port": 0,
            "description": "string",
            "globalCredentialIdList": [
              "string"
            ]
          }
        }
      },
      "version": "string"
    }
"""

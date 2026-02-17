#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_info
short_description: Information module for Discoverys
description:
  - Get all Discoverys.
  - Get Discoverys by id.
  - API to fetch the discovery details using basic filters.
  - API to get discovery details for the given discovery id.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. Optional list of the discovery ids to filter by.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  name:
    description:
      - >
        Name query parameter. Optional name of the discovery to filter by. This supports partial search. For
        example, searching for "Disc" will match "Discovery1", "Discovery2", etc.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices FetchesAllDiscoveryDetails
    description: Complete reference of the FetchesAllDiscoveryDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-all-discovery-details
  - name: Cisco DNA Center documentation for Devices FetchesDiscoveryDetailsById
    description: Complete reference of the FetchesDiscoveryDetailsById API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-discovery-details-by-id
notes:
  - SDK Method used are
    devices.Devices.fetches_all_discovery_details,
    devices.Devices.fetches_discovery_details_by_id,
  - Paths used are
    get /dna/intent/api/v1/discoverys,
    get /dna/intent/api/v1/discoverys/{id},
"""

EXAMPLES = r"""
---
- name: Get all Discoverys
  cisco.dnac.discoverys_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    limit: 0
    name: string
    offset: 0
  register: result
- name: Get Discoverys by id
  cisco.dnac.discoverys_info:
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

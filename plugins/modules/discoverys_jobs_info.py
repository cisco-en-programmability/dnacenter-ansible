#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_info
short_description: Information module for Discoverys Jobs
description:
  - Get all Discoverys Jobs.
  - Get Discoverys Jobs by id. - > API to get all the discovery job details by discovery id. A discovery can have multiple
    discovery jobs, created against the same discovery id.
  - This API retrieves the details of a specific discovery job using the given job id and discovery id.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  discoveryId:
    description:
      - DiscoveryId path parameter. The id of the discovery.
    type: str
  jobId:
    description:
      - JobId path parameter. The id of the discovery job.
    type: str
  id:
    description:
      - Id path parameter. The id of the discovery.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  orderBy:
    description:
      - >
        OrderBy query parameter. To fetch the latest discovery job. Use the orderBy query parameter with values
        such as startTime or endTime. By default, jobs are ordered by startTime in descending order to display
        the most recent entries first.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices FetchesAllTheDiscoveryJobDetailsByDiscoveryId
    description: Complete reference of the FetchesAllTheDiscoveryJobDetailsByDiscoveryId API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-all-the-discovery-job-details-by-discovery-id
  - name: Cisco DNA Center documentation for Devices FetchesTheDiscoveryJobDetailsForTheGivenJobId
    description: Complete reference of the FetchesTheDiscoveryJobDetailsForTheGivenJobId API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-the-discovery-job-details-for-the-given-job-id
notes:
  - SDK Method used are
    devices.Devices.fetches_all_the_discovery_job_details_by_discovery_id,
    devices.Devices.fetches_the_discovery_job_details_for_the_given_job_id,
  - Paths used are
    get /dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId},
    get /dna/intent/api/v1/discoverys/{id}/jobs,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Jobs
  cisco.dnac.discoverys_jobs_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    jobId: string
    limit: 0
    offset: 0
    orderBy: string
    id: string
  register: result
- name: Get Discoverys Jobs by id
  cisco.dnac.discoverys_jobs_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    discoveryId: string
    jobId: string
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

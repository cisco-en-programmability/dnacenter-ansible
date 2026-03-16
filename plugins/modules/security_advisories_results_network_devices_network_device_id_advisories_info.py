#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_results_network_devices_network_device_id_advisories_info
short_description: Information module for Security Advisories Results Network Devices Network Device Id Advisories
description:
  - Get all Security Advisories Results Network Devices Network Device Id Advisories.
  - Get Security Advisories Results Network Devices Network Device Id Advisories by id.
  - Get security advisories affecting the network device.
  - Get security advisory affecting the network device by device Id and advisory id.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Id of the network device.
    type: str
  id:
    description:
      - Id query parameter. Id of the security advisory.
    type: str
  cvssBaseScore:
    description:
      - CvssBaseScore query parameter. Return advisories with cvssBaseScore greater than this cvssBaseScore. E.g. 8.5.
    type: str
  securityImpactRating:
    description:
      - >
        SecurityImpactRating query parameter. Return advisories with this securityImpactRating. Available values
        CRITICAL, HIGH.
    type: str
  offset:
    description:
      - >
        Offset query parameter. The first record to show for this page; the first record is numbered 1. Default
        value is 1.
    type: int
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Minimum value is 1. Maximum value is
        500. Default value is 500.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - >
        Order query parameter. Whether ascending or descending order should be used to sort the response.
        Available values asc, desc. Default value is asc.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance GetSecurityAdvisoriesAffectingTheNetworkDevice
    description: Complete reference of the GetSecurityAdvisoriesAffectingTheNetworkDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!get-security-advisories-affecting-the-network-device
  - name: Cisco DNA Center documentation for Compliance GetSecurityAdvisoryAffectingTheNetworkDeviceByDeviceIdAndAdvisoryId
    description: Complete reference of the GetSecurityAdvisoryAffectingTheNetworkDeviceByDeviceIdAndAdvisoryId API.
    link: https://developer.cisco.com/docs/dna-center/#!get-security-advisory-affecting-the-network-device-by-device-id-and-advisory-id
notes:
  - SDK Method used are
    compliance.Compliance.get_security_advisories_affecting_the_network_device,
    compliance.Compliance.get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id,
  - Paths used are
    get /dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories,
    get /dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories/{id},
"""

EXAMPLES = r"""
---
- name: Get all Security Advisories Results Network Devices Network Device Id Advisories
  cisco.dnac.security_advisories_results_network_devices_network_device_id_advisories_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    cvssBaseScore: string
    securityImpactRating: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
    networkDeviceId: string
  register: result
- name: Get Security Advisories Results Network Devices Network Device Id Advisories by id
  cisco.dnac.security_advisories_results_network_devices_network_device_id_advisories_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
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
        "id": "string",
        "deviceCount": 0,
        "cveIds": [
          "string"
        ],
        "publicationUrl": "string",
        "cvssBaseScore": 0,
        "securityImpactRating": "string",
        "firstFixedVersionsList": [
          {
            "vulnerableVersion": "string",
            "fixedVersions": [
              "string"
            ]
          }
        ]
      },
      "version": "string"
    }
"""

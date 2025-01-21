#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_results_network_devices_network_device_id_advisories_id_v1_info
short_description: Information module for Security Advisories Results Network Devices Network Device Id Advisories Id V1
description:
- Get Security Advisories Results Network Devices Network Device Id Advisories Id V1 by id.
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
    - Id path parameter. Id of the security advisory.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance GetSecurityAdvisoryAffectingTheNetworkDeviceByDeviceIdAndAdvisoryIdV1
  description: Complete reference of the GetSecurityAdvisoryAffectingTheNetworkDeviceByDeviceIdAndAdvisoryIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-security-advisory-affecting-the-network-device-by-device-id-and-advisory-id
notes:
  - SDK Method used are
    compliance.Compliance.get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id_v1,

  - Paths used are
    get /dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories/{id},

"""

EXAMPLES = r"""
- name: Get Security Advisories Results Network Devices Network Device Id Advisories Id V1 by id
  cisco.dnac.security_advisories_results_network_devices_network_device_id_advisories_id_v1_info:
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

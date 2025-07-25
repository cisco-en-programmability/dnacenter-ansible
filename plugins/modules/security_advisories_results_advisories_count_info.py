#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_results_advisories_count_info
short_description: Information module for Security Advisories
  Results Advisories Count
description:
  - Get all Security Advisories Results Advisories Count.
  - Get count of security advisories affecting the network
    devices.
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
      - Id query parameter. Id of the security advisory.
    type: str
  deviceCount:
    description:
      - DeviceCount query parameter. Return advisories
        with deviceCount greater than this deviceCount.
    type: float
  cvssBaseScore:
    description:
      - CvssBaseScore query parameter. Return advisories
        with cvssBaseScore greater than this cvssBaseScore.
        E.g. 8.5.
    type: str
  securityImpactRating:
    description:
      - >
        SecurityImpactRating query parameter. Return
        advisories with this securityImpactRating. Available
        values CRITICAL, HIGH.
    type: str
requirements:
  - dnacentersdk >= 2.10.1
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance
      GetCountOfSecurityAdvisoriesAffectingTheNetworkDevices
    description: Complete reference of the GetCountOfSecurityAdvisoriesAffectingTheNetworkDevices
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisories-affecting-the-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.get_count_of_security_advisories_affecting_the_network_devices,
  - Paths used are
    get /dna/intent/api/v1/securityAdvisories/results/advisories/count,
"""

EXAMPLES = r"""
---
- name: Get all Security Advisories Results Advisories
    Count
  cisco.dnac.security_advisories_results_advisories_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    deviceCount: 0
    cvssBaseScore: string
    securityImpactRating: string
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
        "count": 0
      }
    }
"""

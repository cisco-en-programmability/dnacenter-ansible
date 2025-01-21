#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_summary_v1_info
short_description: Information module for Security Advisories Summary V1
description:
- Get all Security Advisories Summary V1.
- Retrieves summary of advisories on the network.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Security Advisories GetAdvisoriesSummaryV1
  description: Complete reference of the GetAdvisoriesSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-advisories-summary
notes:
  - SDK Method used are
    security_advisories.SecurityAdvisories.get_advisories_summary_v1,

  - Paths used are
    get /dna/intent/api/v1/security-advisory/advisory/aggregate,

"""

EXAMPLES = r"""
- name: Get all Security Advisories Summary V1
  cisco.dnac.security_advisories_summary_v1_info:
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
        "INFORMATIONAL": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "LOW": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "MEDIUM": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "HIGH": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "CRITICAL": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "NA": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        }
      },
      "version": "string"
    }
"""

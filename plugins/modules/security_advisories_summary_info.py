#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_summary_info
short_description: Information module for Security Advisories Summary
description:
- Get all Security Advisories Summary.
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
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_advisories_summary used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.security_advisories.SecurityAdvisories.get_advisories_summary

- name: Paths used on the module Security Advisories Summary
  description: |-
    get /dna/intent/api/v1/security-advisory/advisory/aggregate
"""

EXAMPLES = r"""
- name: Get all Security Advisories Summary
  cisco.dnac.security_advisories_summary_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
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
        "NA": {
          "CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "INFORMATIONAL": {
          "CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "LOW": {
          "CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "MEDIUM": {
          "CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "HIGH": {
          "CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "CRITICAL": {
          "CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        }
      },
      "version": "string"
    }
"""

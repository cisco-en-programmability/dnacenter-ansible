#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_device_details_count_info
short_description: Information module for Compliance Device Details Count
description:
- Get all Compliance Device Details Count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  complianceType:
    description:
    - >
      ComplianceType query parameter. ComplianceType can have any value among 'NETWORK_PROFILE', 'IMAGE',
      'APPLICATION_VISIBILITY', 'FABRIC', 'PSIRT', 'RUNNING_CONFIG', 'WORKFLOW'.
    type: str
  complianceStatus:
    description:
    - >
      ComplianceStatus query parameter. Compliance status can have value among 'COMPLIANT', 'NON_COMPLIANT',
      'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Compliance Device Details Count reference
  description: Complete reference of the Compliance Device Details Count object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Compliance Device Details Count
  cisco.dnac.compliance_device_details_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    complianceType: string
    complianceStatus: string
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
      "response": 0
    }
"""

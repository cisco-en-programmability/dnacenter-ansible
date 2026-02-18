#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_network_devices_detail_policys_violations_info
short_description: Information module for Compliance Network Devices Detail Policys Violations
description:
  - Get all Compliance Network Devices Detail Policys Violations.
  - Retrieve the violation details of the compliance policy for the network device.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. The `id` of the network device.
    type: str
  policyId:
    description:
      - PolicyId path parameter. The `id` of the compliance policy.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default is 500 if not specified.
        Maximum allowed limit is 500.
    type: int
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance RetrieveThePolicyViolations
    description: Complete reference of the RetrieveThePolicyViolations API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-policy-violations
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_policy_violations,
  - Paths used are
    get /dna/intent/api/v1/compliance/networkDevices/{networkDeviceId}/detail/policys/{policyId}/violations,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Network Devices Detail Policys Violations
  cisco.dnac.compliance_network_devices_detail_policys_violations_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    networkDeviceId: string
    policyId: string
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
          "policyId": "string",
          "policyName": "string",
          "policyDescription": "string",
          "maxSeverity": "string",
          "violationsCount": 0,
          "errorCount": 0,
          "lastComplianceRunTime": 0
        }
      ],
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_device_details_v1_info
short_description: Information module for Compliance Device Details V1
description:
- Get all Compliance Device Details V1.
- Return Compliance Detail.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  complianceType:
    description:
    - >
      ComplianceType query parameter. Specify "Compliance type(s)" in commas. The Compliance type can be
      'NETWORK_PROFILE', 'IMAGE', 'FABRIC', 'APPLICATION_VISIBILITY', 'FABRIC', RUNNING_CONFIG',
      'NETWORK_SETTINGS', 'WORKFLOW' , 'EOX'.
    type: str
  complianceStatus:
    description:
    - >
      ComplianceStatus query parameter. Specify "Compliance status(es)" in commas. The Compliance status can be
      'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
    type: str
  deviceUuid:
    description:
    - DeviceUuid query parameter. Comma separated "Device Id(s)".
    type: str
  offset:
    description:
    - Offset query parameter. Offset starting row.
    type: float
  limit:
    description:
    - >
      Limit query parameter. The number of records to be retrieved defaults to 500 if not specified, with a
      maximum allowed limit of 500.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance GetComplianceDetailV1
  description: Complete reference of the GetComplianceDetailV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-compliance-detail
notes:
  - SDK Method used are
    compliance.Compliance.get_compliance_detail_v1,

  - Paths used are
    get /dna/intent/api/v1/compliance/detail,

"""

EXAMPLES = r"""
- name: Get all Compliance Device Details V1
  cisco.dnac.compliance_device_details_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    complianceType: string
    complianceStatus: string
    deviceUuid: string
    offset: 0
    limit: 0
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
      "response": [
        {
          "complianceType": "string",
          "lastSyncTime": 0,
          "deviceUuid": "string",
          "displayName": "string",
          "status": "string",
          "category": "string",
          "lastUpdateTime": 0,
          "state": "string",
          "remediationSupported": true
        }
      ]
    }
"""

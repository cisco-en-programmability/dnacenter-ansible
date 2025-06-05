#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: compliance_device_id_v1_info
short_description: Information module for Compliance Device Id V1
description:
  - Get Compliance Device Id V1 by id.
  - Return compliance status of a device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceUuid:
    description:
      - DeviceUuid path parameter. Device Id.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance DeviceComplianceStatusV1
    description: Complete reference of the DeviceComplianceStatusV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!device-compliance-status
notes:
  - SDK Method used are compliance.Compliance.device_compliance_status_v1,
  - Paths used are get /dna/intent/api/v1/compliance/{deviceUuid},
"""
EXAMPLES = r"""
- name: Get Compliance Device Id V1 by id
  cisco.dnac.compliance_device_id_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceUuid: string
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
        "deviceUuid": "string",
        "complianceStatus": "string",
        "lastUpdateTime": 0,
        "scheduleTime": "string"
      },
      "version": "string"
    }
"""

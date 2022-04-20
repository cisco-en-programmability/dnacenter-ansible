#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: nfv_provision_detail_info
short_description: Information module for Nfv Provision Detail
description:
- Get all Nfv Provision Detail.
- Returns provisioning device information for the specified IP address.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceIp:
    description:
    - DeviceIp query parameter. Device to which the provisioning detail has to be retrieved.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    site_design.SiteDesign.get_device_details_by_ip,

  - Paths used are
    get /dna/intent/api/v1/business/nfv/provisioningDetail,

"""

EXAMPLES = r"""
- name: Get all Nfv Provision Detail
  cisco.dnac.nfv_provision_detail_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    deviceIp: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "startTime": "string",
      "endTime": "string",
      "duration": "string",
      "statusMessage": "string",
      "status": "string",
      "taskNodes": [
        {
          "startTime": "string",
          "endTime": "string",
          "duration": "string",
          "status": "string",
          "nextTask": "string",
          "name": "string",
          "target": "string",
          "statusMessage": "string",
          "payload": "string",
          "provisionedNames": {},
          "errorPayload": {},
          "parentTask": {},
          "cliTemplateUserMessageDTO": {},
          "stepRan": "string"
        }
      ],
      "topology": "string",
      "beginStep": "string"
    }
"""

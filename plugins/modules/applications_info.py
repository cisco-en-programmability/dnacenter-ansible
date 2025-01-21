#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: applications_info
short_description: Information module for Applications Info
description:
- This module represents an alias of the module applications_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter. The offset of the first application to be returned.
    type: float
  limit:
    description:
    - Limit query parameter. The maximum number of applications to be returned.
    type: float
  name:
    description:
    - Name query parameter. Application's name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Application Policy GetApplicationsV1
  description: Complete reference of the GetApplicationsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-applications
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_applications_v1,

  - Paths used are
    get /dna/intent/api/v1/applications,
  - It should be noted that this module is an alias of applications_v1_info

"""

EXAMPLES = r"""
- name: Get all Applications Info
  cisco.dnac.applications_info:
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
    name: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "networkApplications": [
          {
            "id": "string",
            "appProtocol": "string",
            "applicationSubType": "string",
            "applicationType": "string",
            "categoryId": "string",
            "displayName": "string",
            "engineId": "string",
            "helpString": "string",
            "longDescription": "string",
            "name": "string",
            "popularity": "string",
            "rank": "string",
            "trafficClass": "string",
            "serverName": "string",
            "url": "string",
            "dscp": "string",
            "ignoreConflict": "string"
          }
        ],
        "networkIdentity": [
          {
            "id": "string",
            "displayName": "string",
            "lowerPort": "string",
            "ports": "string",
            "protocol": "string",
            "upperPort": "string"
          }
        ],
        "applicationSet": {
          "idRef": "string"
        }
      }
    ]
"""

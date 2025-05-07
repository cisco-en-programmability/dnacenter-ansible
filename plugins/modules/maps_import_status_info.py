#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: maps_import_status_info
short_description: Information module for Maps Import Status Info
description:
  - This module represents an alias of the module maps_import_status_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  importContextUuid:
    description:
      - >
        ImportContextUuid path parameter. The unique import context UUID given by
        a previous and recent call to
        maps/import start API.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ImportMapArchiveImportStatusV1
    description: Complete reference of the ImportMapArchiveImportStatusV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!import-map-archive-import-status
notes:
  - SDK Method used are sites.Sites.import_map_archive_import_status_v1,
  - Paths used are get /dna/intent/api/v1/maps/import/{importContextUuid}/status,
  - It should be noted that this module is an alias of maps_import_status_v1_info
"""
EXAMPLES = r"""
- name: Get all Maps Import Status Info
  cisco.dnac.maps_import_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    importContextUuid: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "auditLog": {
        "children": [
          "string"
        ],
        "entitiesCount": [
          {
            "key": 0
          }
        ],
        "entityName": "string",
        "entityType": "string",
        "errorEntitiesCount": [
          {
            "key": 0
          }
        ],
        "errors": [
          {
            "message": "string"
          }
        ],
        "infos": [
          {
            "message": "string"
          }
        ],
        "matchingEntitiesCount": [
          {
            "key": 0
          }
        ],
        "subTasksRootTaskId": "string",
        "successfullyImportedFloors": [
          "string"
        ],
        "warnings": [
          {
            "message": "string"
          }
        ]
      },
      "status": "string",
      "uuid": {
        "leastSignificantBits": 0,
        "mostSignificantBits": 0
      }
    }
"""

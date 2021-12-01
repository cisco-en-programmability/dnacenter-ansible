#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_artifact_info
short_description: Information module for Event Artifact
description:
- Get all Event Artifact.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  eventIds:
    description:
    - EventIds query parameter. List of eventIds.
    type: str
  tags:
    description:
    - Tags query parameter. Tags defined.
    type: str
  offset:
    description:
    - Offset query parameter. Record start offset.
    type: int
  limit:
    description:
    - Limit query parameter. # of records to return in result set.
    type: int
  sortBy:
    description:
    - SortBy query parameter. Sort by field.
    type: str
  order:
    description:
    - Order query parameter. Sorting order (asc/desc).
    type: str
  search:
    description:
    - Search query parameter. Findd matches in name, description, eventId, type, category.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Event Artifact reference
  description: Complete reference of the Event Artifact object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Event Artifact
  cisco.dnac.event_artifact_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    eventIds: string
    tags: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
    search: string
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
        "version": "string",
        "artifactId": "string",
        "namespace": "string",
        "name": "string",
        "description": "string",
        "domain": "string",
        "subDomain": "string",
        "tags": [
          "string"
        ],
        "isTemplateEnabled": "string",
        "ciscoDNAEventLink": "string",
        "note": "string",
        "isPrivate": "string",
        "eventPayload": {
          "eventId": "string",
          "version": "string",
          "category": "string",
          "type": "string",
          "source": "string",
          "severity": "string",
          "details": {
            "device_ip": "string",
            "message": "string"
          },
          "additionalDetails": {}
        },
        "eventTemplates": [
          {}
        ],
        "isTenantAware": "string",
        "supportedConnectorTypes": [
          "string"
        ],
        "tenantId": "string"
      }
    ]
"""

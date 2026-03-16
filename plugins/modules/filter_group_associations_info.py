#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_group_associations_info
short_description: Information module for Filter Group Associations
description:
  - Get all Filter Group Associations. - > Returns the details of filter group associations for the given parameters. For
    detailed information about the usage of the API, please refer to the Open API specification document - https //github.com/cisco-en-
    programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org- FilterGroups-1.0.0-resolved.yaml.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  filterGroupId:
    description:
      - >
        FilterGroupId query parameter. Filter Group id. Examples
        `?filterGroupId=2ee1b9f0-8036-443b-bad0-7692760af1b5`(single id requested)
        `?filterGroupId=2ee1b9f0-8036-443b-bad0-7692760af1b5&filterGroupId=ae368f0b-f4e3-4e8f-a914-011cbd19bb51`
        (multiple ids requested).
    type: str
  entityId:
    description:
      - >
        EntityId query parameter. Entity id with which the filter group is associated. Examples
        `?entityId=2ee1b9f0-8036-443b-bad0-7692760af1b5`(single id requested)
        `?entityId=2ee1b9f0-8036-443b-bad0-7692760af1b5&entityId=ae368f0b-f4e3-4e8f-a914-011cbd19bb51` (multiple
        ids requested).
    type: str
  entityType:
    description:
      - >
        EntityType query parameter. Type of the entity with which the filter group is associated. Examples
        `?entityType=Issue Settings`(single type requested) `?entityType=Custom Dashboard&entityType=Issue
        Settings` (multiple types requested).
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices GetTheFilterGroupAssociations
    description: Complete reference of the GetTheFilterGroupAssociations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-filter-group-associations
notes:
  - SDK Method used are
    devices.Devices.get_the_filter_group_associations,
  - Paths used are
    get /dna/intent/api/v1/filterGroupAssociations,
"""

EXAMPLES = r"""
---
- name: Get all Filter Group Associations
  cisco.dnac.filter_group_associations_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    filterGroupId: string
    entityId: string
    entityType: string
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
          "id": "string",
          "filterGroupId": "string",
          "entityId": "string",
          "entityName": "string",
          "entityType": "string"
        }
      ],
      "version": "string"
    }
"""

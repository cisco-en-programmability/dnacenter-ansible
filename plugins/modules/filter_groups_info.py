#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_groups_info
short_description: Information module for Filter Groups
description:
  - Get all Filter Groups.
  - Get Filter Groups by id. - > Returns the details of filter group for the given id. For detailed information about the
    usage of the API, please refer to the Open API specification document - https //github.com/cisco-en-programmability/catalyst-
    center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-FilterGroups-1.0.0-resolved.yaml. - > Returns the details of filter
    groups for given search criteria specified in query parameters. For detailed information about the usage of the API, please
    refer to the Open API specification document - https //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
    FilterGroups-1.0.0-resolved.yaml.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - >
        Id query parameter. Filter Group id. Examples `?id=2ee1b9f0-8036-443b-bad0-7692760af1b5`(single id
        requested) `?id=2ee1b9f0-8036-443b-bad0-7692760af1b5&id=ae368f0b-f4e3-4e8f-a914-011cbd19bb51` (multiple
        ids requested).
    type: str
  name:
    description:
      - >
        Name query parameter. Filter Group name. Examples `?name=SJC Wireless`(single name requested) `?name=SJC
        Wireless&name=Global Wired` (multiple names requested).
    type: str
  type:
    description:
      - >
        Type query parameter. Type of the filter group. Examples type=Generic (single Filter Group type
        requested) type=Generic&type=Site (multiple Filter Group types requested).
    type: str
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned by the API. It's one
        based offset. The starting value is 1.
    type: int
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: int
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices GetTheFilterGroupDetailsForTheGivenId
    description: Complete reference of the GetTheFilterGroupDetailsForTheGivenId API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-filter-group-details-for-the-given-id
  - name: Cisco DNA Center documentation for Devices GetTheFilterGroupsForGivenSearchCriteria
    description: Complete reference of the GetTheFilterGroupsForGivenSearchCriteria API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-filter-groups-for-given-search-criteria
notes:
  - SDK Method used are
    devices.Devices.get_the_filter_group_details_for_the_given_id,
    devices.Devices.get_the_filter_groups_for_given_search_criteria,
  - Paths used are
    get /dna/intent/api/v1/filterGroups,
    get /dna/intent/api/v1/filterGroups/{id},
"""

EXAMPLES = r"""
---
- name: Get all Filter Groups
  cisco.dnac.filter_groups_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    name: string
    type: string
    offset: 0
    limit: 0
  register: result
- name: Get Filter Groups by id
  cisco.dnac.filter_groups_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "id": "string",
        "name": "string",
        "type": "string",
        "filters": [
          {
            "key": "string",
            "operator": "string",
            "value": "string",
            "displayValue": "string"
          }
        ]
      }
    }
"""

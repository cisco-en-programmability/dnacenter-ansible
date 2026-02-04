#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credentials_info
short_description: Information module for Global Credentials
description:
  - Get all Global Credentials.
  - Get Global Credentials by id.
  - API to get global credentials based on the given filters.
  - API to retrieve the global credential details by its unique identifier.
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
      - Id query parameter. List of unique identifiers of the global credentials. Accepts comma separated values.
    type: str
  type:
    description:
      - Type query parameter. Returns global credentials for the given credential type.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Network Settings GetDetailsOfASingleGlobalCredential
    description: Complete reference of the GetDetailsOfASingleGlobalCredential API.
    link: https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-global-credential
  - name: Cisco DNA Center documentation for Network Settings RetrievesGlobalCredentials
    description: Complete reference of the RetrievesGlobalCredentials API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-global-credentials
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_details_of_a_single_global_credential,
    network_settings.NetworkSettings.retrieves_global_credentials,
  - Paths used are
    get /dna/intent/api/v1/globalCredentials,
    get /dna/intent/api/v1/globalCredentials/{id},
"""

EXAMPLES = r"""
---
- name: Get all Global Credentials
  cisco.dnac.global_credentials_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    type: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
  register: result
- name: Get Global Credentials by id
  cisco.dnac.global_credentials_info:
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

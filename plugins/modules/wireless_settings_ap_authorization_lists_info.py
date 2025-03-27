#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_settings_ap_authorization_lists_info
short_description: Information module for Wireless Settings Ap Authorization Lists
  Info
description:
  - This module represents an alias of the module wireless_settings_ap_authorization_lists_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  apAuthorizationListName:
    description:
      - >
        ApAuthorizationListName query parameter. Employ this query parameter to obtain
        the details of the AP
        Authorization List corresponding to the provided apAuthorizationListName.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page. The first
        record is numbered 1.
    type: str
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetAPAuthorizationListsV1
    description: Complete reference of the GetAPAuthorizationListsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ap-authorization-lists
notes:
  - SDK Method used are wireless.Wireless.get_ap_authorization_lists_v1,
  - Paths used are get /dna/intent/api/v1/wirelessSettings/apAuthorizationLists,
  - It should be noted that this module is an alias of wireless_settings_ap_authorization_lists_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Settings Ap Authorization Lists Info
  cisco.dnac.wireless_settings_ap_authorization_lists_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    apAuthorizationListName: string
    offset: string
    limit: string
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
        "apAuthorizationListName": "string",
        "localAuthorization": {
          "apMacEntries": [
            "string"
          ],
          "apSerialNumberEntries": [
            "string"
          ]
        },
        "remoteAuthorization": {
          "aaaServers": [
            "string"
          ],
          "authorizeApWithMac": true,
          "authorizeApWithSerialNumber": true
        }
      },
      "version": "string"
    }
"""

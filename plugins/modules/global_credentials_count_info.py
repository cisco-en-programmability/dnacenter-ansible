#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credentials_count_info
short_description: Information module for Global Credentials Count
description:
  - Get all Global Credentials Count.
  - API to get count of the global credentials based on the given filter.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  type:
    description:
      - Type query parameter. Returns count of global credentials for the given credential type.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Network Settings GetCountOfTheGlobalCredentials
    description: Complete reference of the GetCountOfTheGlobalCredentials API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-the-global-credentials
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_count_of_the_global_credentials,
  - Paths used are
    get /dna/intent/api/v1/globalCredentials/count,
"""

EXAMPLES = r"""
---
- name: Get all Global Credentials Count
  cisco.dnac.global_credentials_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    type: string
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

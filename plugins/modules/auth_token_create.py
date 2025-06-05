#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: auth_token_create
short_description: Resource module for Auth Token Create
description:
  - This module represents an alias of the module auth_token_create_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Authentication AuthenticationAPIV1
    description: Complete reference of the AuthenticationAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!authentication-api
notes:
  - SDK Method used are authentication.Authentication.authentication_api_v1,
  - Paths used are post /dna/system/api/v1/auth/token,
  - It should be noted that this module is an alias of auth_token_create_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.auth_token_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "Token": "string"
    }
"""

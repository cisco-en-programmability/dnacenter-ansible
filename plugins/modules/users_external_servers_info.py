#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: users_external_servers_info
short_description: Information module for Users External Servers Info
description:
- This module represents an alias of the module users_external_servers_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  invokeSource:
    description:
    - >
      InvokeSource query parameter. The source that invokes this API. The value of this query parameter must be
      set to "external".
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for User and Roles GetExternalAuthenticationServersAPIV1
  description: Complete reference of the GetExternalAuthenticationServersAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-external-authentication-servers-api
notes:
  - SDK Method used are
    user_and_roles.UserandRoles.get_external_authentication_servers_api_v1,

  - Paths used are
    get /dna/system/api/v1/users/external-servers,
  - It should be noted that this module is an alias of users_external_servers_v1_info

"""

EXAMPLES = r"""
- name: Get all Users External Servers Info
  cisco.dnac.users_external_servers_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    invokeSource: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "aaa-servers": [
        {
          "accountingPort": 0,
          "retries": 0,
          "protocol": "string",
          "socketTimeout": 0,
          "serverIp": "string",
          "sharedSecret": "string",
          "serverId": "string",
          "authenticationPort": 0,
          "aaaAttribute": "string",
          "role": "string"
        }
      ]
    }
"""

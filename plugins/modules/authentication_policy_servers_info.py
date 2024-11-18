#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: authentication_policy_servers_info
short_description: Information module for Authentication Policy Servers Info
description:
- This module represents an alias of the module authentication_policy_servers_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  isIseEnabled:
    description:
    - IsIseEnabled query parameter. Valid values are true, false.
    type: bool
  state_:
    description:
    - State query parameter. Valid values are ACTIVE, INACTIVE, RBAC_SUCCESS, RBAC_FAILURE, DELETED, FAILED, INPROGRESS.
    type: str
  role:
    description:
    - Role query parameter. Authentication and Policy Server Role (Example primary, secondary).
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for System Settings GetAuthenticationAndPolicyServersV1
  description: Complete reference of the GetAuthenticationAndPolicyServersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-authentication-and-policy-servers-v-1
notes:
  - SDK Method used are
    system_settings.SystemSettings.get_authentication_and_policy_servers_v1,

  - Paths used are
    get /dna/intent/api/v1/authentication-policy-servers,
  - It should be noted that this module is an alias of authentication_policy_servers_v1_info

"""

EXAMPLES = r"""
- name: Get all Authentication Policy Servers Info
  cisco.dnac.authentication_policy_servers_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    isIseEnabled: True
    state_: string
    role: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of authentication_policy_servers_v1_info.
"""

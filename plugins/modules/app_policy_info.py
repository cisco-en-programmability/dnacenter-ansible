#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: app_policy_info
short_description: Information module for App Policy Info
description:
- This module represents an alias of the module app_policy_v1_info
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  policyScope:
    description:
    - PolicyScope query parameter. Policy scope name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Application Policy GetApplicationPolicyV1
  description: Complete reference of the GetApplicationPolicyV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-application-policy-v-1
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_policy_v1,

  - Paths used are
    get /dna/intent/api/v1/app-policy,
  - It should be noted that this module is an alias of app_policy_v1_info

"""

EXAMPLES = r"""
- name: Get all App Policy Info
  cisco.dnac.app_policy_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    policyScope: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of app_policy_v1_info.
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_authentication_profiles_info
short_description: Information module for Sda Authentication Profiles Info
description:
- This module represents an alias of the module sda_authentication_profiles_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
    - FabricId query parameter. ID of the fabric the authentication profile is assigned to.
    type: str
  authenticationProfileName:
    description:
    - >
      AuthenticationProfileName query parameter. Return only the authentication profiles with this specified name.
      Note that 'No Authentication' is not a valid option for this parameter.
    type: str
  offset:
    description:
    - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
    - Limit query parameter. Maximum number of records to return.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetAuthenticationProfilesV1
  description: Complete reference of the GetAuthenticationProfilesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-authentication-profiles-v-1
notes:
  - SDK Method used are
    sda.Sda.get_authentication_profiles_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/authenticationProfiles,
  - It should be noted that this module is an alias of sda_authentication_profiles_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Authentication Profiles Info
  cisco.dnac.sda_authentication_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    authenticationProfileName: string
    offset: 0
    limit: 0
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of sda_authentication_profiles_v1_info.
"""
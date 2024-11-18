#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_rf_profile_info
short_description: Information module for Wireless Rf Profile Info
description:
- This module represents an alias of the module wireless_rf_profile_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  rf_profile_name:
    description:
    - Rf-profile-name query parameter. RF Profile Name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless RetrieveRFProfilesV1
  description: Complete reference of the RetrieveRFProfilesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-rf-profiles-v-1
notes:
  - SDK Method used are
    wireless.Wireless.retrieve_rf_profiles_v1,

  - Paths used are
    get /dna/intent/api/v1/wireless/rf-profile,
  - It should be noted that this module is an alias of wireless_rf_profile_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Rf Profile Info
  cisco.dnac.wireless_rf_profile_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    rf_profile_name: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of wireless_rf_profile_v1_info.
"""

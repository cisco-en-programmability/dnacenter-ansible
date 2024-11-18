#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: user_enrichment_details_info
short_description: Information module for User Enrichment Details Info
description:
- This module represents an alias of the module user_enrichment_details_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Users GetUserEnrichmentDetailsV1
  description: Complete reference of the GetUserEnrichmentDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-user-enrichment-details-v-1
notes:
  - SDK Method used are
    users.Users.get_user_enrichment_details_v1,

  - Paths used are
    get /dna/intent/api/v1/user-enrichment-details,
  - It should be noted that this module is an alias of user_enrichment_details_v1_info

"""

EXAMPLES = r"""
- name: Get all User Enrichment Details Info
  cisco.dnac.user_enrichment_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of user_enrichment_details_v1_info.
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: applications_count_v1_info
short_description: Information module for Applications Count V1
description:
  - Get all Applications Count V1.
  - Get the number of all existing applications.
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
  - name: Cisco DNA Center documentation for Application Policy GetApplicationsCountV1
    description: Complete reference of the GetApplicationsCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-applications-count
notes:
  - SDK Method used are application_policy.ApplicationPolicy.get_applications_count_v1,
  - Paths used are get /dna/intent/api/v1/applications-count,
"""
EXAMPLES = r"""
- name: Get all Applications Count V1
  cisco.dnac.applications_count_v1_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "string",
      "version": "string"
    }
"""

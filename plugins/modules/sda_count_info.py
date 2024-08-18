#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_count_info
short_description: Information module for Sda Count
description:
- Get all Sda Count.
- Get SDA Fabric Count.
deprecated:
  removed_in: '6.19.0'
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
  - SDK Method used are
    sda.Sda.get_sda_fabric_count,

  - Paths used are
    get /dna/intent/api/v1/business/sda/fabric/count,

"""

EXAMPLES = r"""
- name: Get all Sda Count
  cisco.dnac.sda_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
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
        "status": "string",
        "description": "string",
        "fabricCount": "string"
      },
      "version": "string"
    }
"""

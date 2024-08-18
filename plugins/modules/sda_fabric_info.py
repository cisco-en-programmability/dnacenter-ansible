#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_info
short_description: Information module for Sda Fabric
description:
- Get all Sda Fabric.
- Get SDA Fabric Info.
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
  fabricName:
    description:
    - FabricName query parameter. Fabric Name.
    type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
  - SDK Method used are
    sda.Sda.get_sda_fabric_info,

  - Paths used are
    get /dna/intent/api/v1/business/sda/fabric,

"""

EXAMPLES = r"""
- name: Get all Sda Fabric
  cisco.dnac.sda_fabric_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    fabricName: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "executionId": "string",
      "fabricName": "string",
      "fabricType": "string",
      "fabricDomainType": "string"
    }
"""

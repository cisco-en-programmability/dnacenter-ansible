#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_deregister
short_description: Resource module for License Deregister
description:
  - This module represents an alias of the module license_deregister_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses SmartLicensingDeregistrationV1
    description: Complete reference of the SmartLicensingDeregistrationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!smart-licensing-deregistration
notes:
  - SDK Method used are licenses.Licenses.smart_licensing_deregistration_v1,
  - Paths used are post /dna/system/api/v1/license/deregister,
  - It should be noted that this module is an alias of license_deregister_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.license_deregister:
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
      "response": {
        "url": "string"
      },
      "version": "string"
    }
"""

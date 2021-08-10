#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_devices_info
short_description: Information module for Security Advisories Devices
description:
- Get all Security Advisories Devices.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  advisoryId:
    description:
    - AdvisoryId path parameter. Advisory ID.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Security Advisories Devices reference
  description: Complete reference of the Security Advisories Devices object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Security Advisories Devices
  cisco.dnac.security_advisories_devices_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    advisoryId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        "string"
      ],
      "version": "string"
    }
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_device_count_info
short_description: Information module for License Device Count
description:
- Get all License Device Count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_type:
    description:
    - Device_type query parameter. Type of device.
    type: str
  registration_status:
    description:
    - Registration_status query parameter. Smart license registration status of device.
    type: str
  dna_level:
    description:
    - Dna_level query parameter. Device Cisco DNA license level.
    type: str
  virtual_account_name:
    description:
    - Virtual_account_name query parameter. Name of virtual account.
    type: str
  smart_account_id:
    description:
    - Smart_account_id query parameter. Id of smart account.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: License Device Count reference
  description: Complete reference of the License Device Count object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all License Device Count
  cisco.dnac.license_device_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    device_type: string
    registration_status: string
    dna_level: string
    virtual_account_name: string
    smart_account_id: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""

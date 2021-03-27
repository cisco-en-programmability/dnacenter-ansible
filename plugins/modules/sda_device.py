#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: sda_device
short_description: Manage SdaDevice objects of Sda
description:
- Get device info from SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_ipaddress:
    description:
    - Device IP Address.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_device
# Reference by Internet resource
- name: SdaDevice reference
  description: Complete reference of the SdaDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_info
  cisco.dnac.sda_device:
    state: query  # required
    device_ipaddress: SomeValue  # string, required
  register: query_result

"""

RETURN = """
"""

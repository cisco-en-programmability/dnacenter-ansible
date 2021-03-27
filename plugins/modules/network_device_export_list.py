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
module: network_device_export_list
short_description: Manage NetworkDeviceExportList objects of Devices
description:
- Exports the selected network device to a file.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceUuids:
    description:
    - ExportDeviceDTO's deviceUuids (list of strings).
    type: list
    required: True
  id:
    description:
    - ExportDeviceDTO's id.
    type: str
  operationEnum:
    description:
    - ExportDeviceDTO's operationEnum.
    - Available values are 'CREDENTIALDETAILS' and 'DEVICEDETAILS'.
    type: str
  parameters:
    description:
    - ExportDeviceDTO's parameters (list of strings).
    type: list
  password:
    description:
    - ExportDeviceDTO's password.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_export_list
# Reference by Internet resource
- name: NetworkDeviceExportList reference
  description: Complete reference of the NetworkDeviceExportList object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceExportList reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: export_device_list
  cisco.dnac.network_device_export_list:
    state: create  # required
    deviceUuids:  # required
    - SomeValue  # string
    id: SomeValue  # string
    operationEnum: SomeValue  # string, valid values: 'CREDENTIALDETAILS', 'DEVICEDETAILS'.
    parameters:
    - SomeValue  # string
    password: SomeValue  # string
  
"""

RETURN = """
"""

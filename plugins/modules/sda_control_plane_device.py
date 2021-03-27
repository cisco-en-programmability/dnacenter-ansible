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
module: sda_control_plane_device
short_description: Manage SdaControlPlaneDevice objects of Sda
description:
- Get control plane device from SDA Fabric.
- Delete control plane device in SDA Fabric.
- Add control plane device in SDA Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_ipaddress:
    description:
    - Device IP Address.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      deviceManagementIpAddress:
        description:
        - It is the sda control plane device's deviceManagementIpAddress.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda control plane device's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_control_plane_device
# Reference by Internet resource
- name: SdaControlPlaneDevice reference
  description: Complete reference of the SdaControlPlaneDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaControlPlaneDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_control_plane_device
  cisco.dnac.sda_control_plane_device:
    state: query  # required
    device_ipaddress: SomeValue  # string, required
  register: query_result

- name: delete_control_plane_device
  cisco.dnac.sda_control_plane_device:
    state: delete  # required
    device_ipaddress: SomeValue  # string, required

- name: add_control_plane_device
  cisco.dnac.sda_control_plane_device:
    state: create  # required
    payload:  # required
    - deviceManagementIpAddress: SomeValue  # string
      siteNameHierarchy: SomeValue  # string

"""

RETURN = """
"""

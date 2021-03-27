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
module: sda_edge_device
short_description: Manage SdaEdgeDevice objects of Sda
description:
- Delete edge device from SDA Fabric.
- Get edge device from SDA Fabric.
- Add edge device in SDA Fabric.
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
        - It is the sda edge device's deviceManagementIpAddress.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda edge device's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_edge_device
# Reference by Internet resource
- name: SdaEdgeDevice reference
  description: Complete reference of the SdaEdgeDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaEdgeDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_edge_device
  cisco.dnac.sda_edge_device:
    state: delete  # required
    device_ipaddress: SomeValue  # string, required
  
- name: get_edge_device
  cisco.dnac.sda_edge_device:
    state: query  # required
    device_ipaddress: SomeValue  # string, required
  register: query_result
  
- name: add_edge_device
  cisco.dnac.sda_edge_device:
    state: create  # required
    payload:  # required
    - deviceManagementIpAddress: SomeValue  # string
      siteNameHierarchy: SomeValue  # string
  
"""

RETURN = """
delete_edge_device:
    description: Delete edge device from SDA Fabric.
    returned: success
    type: dict
    contains:
    status:
      description: Status, property of the response body.
      returned: success
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: success
      type: str
      sample: '<description>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'

get_edge_device:
    description: Get edge device from SDA Fabric.
    returned: always
    type: dict
    contains:
    status:
      description: Status, property of the response body.
      returned: always
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: always
      type: str
      sample: '<description>'
    name:
      description: Name, property of the response body.
      returned: always
      type: str
      sample: '<name>'
    roles:
      description: Roles, property of the response body (list of strings).
      returned: always
      type: list
    deviceManagementIpAddress:
      description: Device Management Ip Address, property of the response body.
      returned: always
      type: str
      sample: '<devicemanagementipaddress>'
    siteHierarchy:
      description: Site Hierarchy, property of the response body.
      returned: always
      type: str
      sample: '<sitehierarchy>'

add_edge_device:
    description: Add edge device in SDA Fabric.
    returned: success
    type: dict
    contains:
    status:
      description: Status, property of the response body.
      returned: success
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: success
      type: str
      sample: '<description>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'

"""

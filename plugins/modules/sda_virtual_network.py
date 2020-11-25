#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: sda_virtual_network
short_description: Manage SdaVirtualNetwork objects of Sda
description:
- Get virtual network (VN) from SDA Fabric.
- Delete virtual network (VN) from SDA Fabric.
- Add virtual network (VN) in SDA Fabric.
version_added: '1.0'
author: first last (@GitHubID)
options:
  site_name_hierarchy:
    description:
    - SiteNameHierarchy query parameter.
    type: str
    required: True
  virtual_network_name:
    description:
    - VirtualNetworkName query parameter.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      virtualNetworkName:
        description:
        - It is the sda virtual network's virtualNetworkName.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda virtual network's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_virtual_network
# Reference by Internet resource
- name: SdaVirtualNetwork reference
  description: Complete reference of the SdaVirtualNetwork object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaVirtualNetwork reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_vn
  cisco.dnac.sda_virtual_network:
    state: query  # required
    site_name_hierarchy: SomeValue  # string, required
    virtual_network_name: SomeValue  # string, required
  register: query_result
  
- name: delete_vn
  cisco.dnac.sda_virtual_network:
    state: delete  # required
    site_name_hierarchy: SomeValue  # string, required
    virtual_network_name: SomeValue  # string, required
  
- name: add_vn
  cisco.dnac.sda_virtual_network:
    state: create  # required
    payload:  # required
    - virtualNetworkName: SomeValue  # string
      siteNameHierarchy: SomeValue  # string
  
"""

RETURN = """
get_vn:
    description: Get virtual network (VN) from SDA Fabric.
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

delete_vn:
    description: Delete virtual network (VN) from SDA Fabric.
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
    name:
      description: Name, property of the response body.
      returned: success
      type: str
      sample: '<name>'
    roles:
      description: Roles, property of the response body (list of strings).
      returned: success
      type: list
    deviceManagementIpAddress:
      description: Device Management Ip Address, property of the response body.
      returned: success
      type: str
      sample: '<devicemanagementipaddress>'
    siteHierarchy:
      description: Site Hierarchy, property of the response body.
      returned: success
      type: str
      sample: '<sitehierarchy>'

add_vn:
    description: Add virtual network (VN) in SDA Fabric.
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
    name:
      description: Name, property of the response body.
      returned: success
      type: str
      sample: '<name>'
    roles:
      description: Roles, property of the response body (list of strings).
      returned: success
      type: list
    deviceManagementIpAddress:
      description: Device Management Ip Address, property of the response body.
      returned: success
      type: str
      sample: '<devicemanagementipaddress>'
    siteHierarchy:
      description: Site Hierarchy, property of the response body.
      returned: success
      type: str
      sample: '<sitehierarchy>'

"""

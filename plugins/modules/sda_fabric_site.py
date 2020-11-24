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
module: sda_fabric_site
short_description: Manage SdaFabricSite objects of Sda
description:
- Delete Site from SDA Fabric.
- Get Site info from SDA Fabric.
- Add Site in SDA Fabric.
version_added: '1.0'
author: first last (@GitHubID)
options:
  site_name_hierarchy:
    description:
    - Site Name Hierarchy.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      fabricName:
        description:
        - It is the sda fabric site's fabricName.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda fabric site's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_fabric_site
# Reference by Internet resource
- name: SdaFabricSite reference
  description: Complete reference of the SdaFabricSite object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaFabricSite reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_site
  cisco.dnac.sda_fabric_site
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: delete  # required
    site_name_hierarchy: SomeValue  # string, required
  delegate_to: localhost
  
- name: get_site
  cisco.dnac.sda_fabric_site
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    site_name_hierarchy: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
- name: add_site
  cisco.dnac.sda_fabric_site
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    payload:  # required
    - fabricName: SomeValue  # string
      siteNameHierarchy: SomeValue  # string
  delegate_to: localhost
  
"""

RETURN = """
delete_site:
    description: Delete Site from SDA Fabric.
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

get_site:
    description: Get Site info from SDA Fabric.
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
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: always
      type: str
      sample: '<executionstatusurl>'

add_site:
    description: Add Site in SDA Fabric.
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

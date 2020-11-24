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
module: sda_fabric
short_description: Manage SdaFabric objects of Sda
description:
- Get SDA Fabric Info.
- Delete SDA Fabric.
- Add SDA Fabric.
version_added: '1.0'
author: first last (@GitHubID)
options:
  fabric_name:
    description:
    - Fabric Name.
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
        - It is the sda fabric's fabricName.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_fabric
# Reference by Internet resource
- name: SdaFabric reference
  description: Complete reference of the SdaFabric object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaFabric reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_sda_fabric_info
  cisco.dnac.sda_fabric
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    fabric_name: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
- name: delete_sda_fabric
  cisco.dnac.sda_fabric
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: delete  # required
    fabric_name: SomeValue  # string, required
  delegate_to: localhost
  
- name: add_fabric
  cisco.dnac.sda_fabric
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    payload:  # required
    - fabricName: SomeValue  # string
  delegate_to: localhost
  
"""

RETURN = """
get_sda_fabric_info:
    description: Get SDA Fabric Info.
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

delete_sda_fabric:
    description: Delete SDA Fabric.
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

add_fabric:
    description: Add SDA Fabric.
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

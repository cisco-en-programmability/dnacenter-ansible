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
module: sda_host_onboarding_access_point
short_description: Manage SdaHostOnboardingAccessPoint objects of Sda
description:
- Delete Port assignment for access point in SDA Fabric.
- Get Port assignment for access point in SDA Fabric.
- Add Port assignment for access point in SDA Fabric.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  device_ip:
    description:
    - Device-ip query parameter.
    type: str
    required: True
  interface_name:
    description:
    - InterfaceName query parameter.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      siteNameHierarchy:
        description:
        - It is the sda host onboarding access point's siteNameHierarchy.
        type: str
      deviceManagementIpAddress:
        description:
        - It is the sda host onboarding access point's deviceManagementIpAddress.
        type: str
      interfaceName:
        description:
        - It is the sda host onboarding access point's interfaceName.
        type: str
      dataIpAddressPoolName:
        description:
        - It is the sda host onboarding access point's dataIpAddressPoolName.
        type: str
      voiceIpAddressPoolName:
        description:
        - It is the sda host onboarding access point's voiceIpAddressPoolName.
        type: str
      authenticateTemplateName:
        description:
        - It is the sda host onboarding access point's authenticateTemplateName.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_host_onboarding_access_point
# Reference by Internet resource
- name: SdaHostOnboardingAccessPoint reference
  description: Complete reference of the SdaHostOnboardingAccessPoint object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaHostOnboardingAccessPoint reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_port_assignment_for_access_point
  cisco.dnac.sda_host_onboarding_access_point:
    state: delete  # required
    device_ip: SomeValue  # string, required
    interface_name: SomeValue  # string, required
  
- name: get_port_assignment_for_access_point
  cisco.dnac.sda_host_onboarding_access_point:
    state: query  # required
    device_ip: SomeValue  # string, required
    interface_name: SomeValue  # string, required
  register: query_result
  
- name: add_port_assignment_for_access_point
  cisco.dnac.sda_host_onboarding_access_point:
    state: create  # required
    payload:  # required
    - siteNameHierarchy: SomeValue  # string
      deviceManagementIpAddress: SomeValue  # string
      interfaceName: SomeValue  # string
      dataIpAddressPoolName: SomeValue  # string
      voiceIpAddressPoolName: SomeValue  # string
      authenticateTemplateName: SomeValue  # string
  
"""

RETURN = """
delete_port_assignment_for_access_point:
    description: Delete Port assignment for access point in SDA Fabric.
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

get_port_assignment_for_access_point:
    description: Get Port assignment for access point in SDA Fabric.
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
    siteNameHierarchy:
      description: Site Name Hierarchy, property of the response body.
      returned: always
      type: str
      sample: '<sitenamehierarchy>'
    deviceManagementIpAddress:
      description: Device Management Ip Address, property of the response body.
      returned: always
      type: str
      sample: '<devicemanagementipaddress>'
    interfaceName:
      description: Interface Name, property of the response body.
      returned: always
      type: str
      sample: '<interfacename>'
    dataIpAddressPoolName:
      description: Data Ip Address Pool Name, property of the response body.
      returned: always
      type: str
      sample: '<dataipaddresspoolname>'
    voiceIpAddressPoolName:
      description: Voice Ip Address Pool Name, property of the response body.
      returned: always
      type: str
      sample: '<voiceipaddresspoolname>'
    scalableGroupName:
      description: Scalable Group Name, property of the response body.
      returned: always
      type: str
      sample: '<scalablegroupname>'
    authenticateTemplateName:
      description: Authenticate Template Name, property of the response body.
      returned: always
      type: str
      sample: '<authenticatetemplatename>'

add_port_assignment_for_access_point:
    description: Add Port assignment for access point in SDA Fabric.
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

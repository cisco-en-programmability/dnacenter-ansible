#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_host_onboarding_user_device
short_description: Manage SdaHostOnboardingUserDevice objects of Sda
description:
- Get Port assignment for user device in SDA Fabric.
- Delete Port assignment for user device in SDA Fabric.
- Add Port assignment for user device in SDA Fabric.
version_added: '1.0.0'
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
        - It is the sda host onboarding user device's siteNameHierarchy.
        type: str
      deviceManagementIpAddress:
        description:
        - It is the sda host onboarding user device's deviceManagementIpAddress.
        type: str
      interfaceName:
        description:
        - It is the sda host onboarding user device's interfaceName.
        type: str
      dataIpAddressPoolName:
        description:
        - It is the sda host onboarding user device's dataIpAddressPoolName.
        type: str
      voiceIpAddressPoolName:
        description:
        - It is the sda host onboarding user device's voiceIpAddressPoolName.
        type: str
      authenticateTemplateName:
        description:
        - It is the sda host onboarding user device's authenticateTemplateName.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_host_onboarding_user_device
# Reference by Internet resource
- name: SdaHostOnboardingUserDevice reference
  description: Complete reference of the SdaHostOnboardingUserDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaHostOnboardingUserDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_port_assignment_for_user_device
  cisco.dnac.sda_host_onboarding_user_device:
    state: query  # required
    device_ip: SomeValue  # string, required
    interface_name: SomeValue  # string, required
  register: query_result

- name: delete_port_assignment_for_user_device
  cisco.dnac.sda_host_onboarding_user_device:
    state: delete  # required
    device_ip: SomeValue  # string, required
    interface_name: SomeValue  # string, required

- name: add_port_assignment_for_user_device
  cisco.dnac.sda_host_onboarding_user_device:
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
"""

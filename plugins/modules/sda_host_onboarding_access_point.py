#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_host_onboarding_access_point
short_description: Manage SdaHostOnboardingAccessPoint objects of Sda
description:
- Delete Port assignment for access point in SDA Fabric.
- Get Port assignment for access point in SDA Fabric.
- Add Port assignment for access point in SDA Fabric.
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

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: array
  sample:
"""

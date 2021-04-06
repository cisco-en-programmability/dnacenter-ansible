#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: service_provider
short_description: Manage ServiceProvider objects of NetworkSettings
description:
- API to get service provider details (QoS).
- API to create service provider profile(QOS).
- API to update SP profile.
- API to delete Service Provider profile (QoS).
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  settings:
    description:
    - Settings, property of the request body.
    type: dict
    required: True
    suboptions:
      qos:
        description:
        - It is the service provider's qos.
        type: list
        elements: dict
        suboptions:
          model:
            description:
            - It is the service provider's model.
            - Required for state create.
            type: str
          oldProfileName:
            description:
            - It is the service provider's oldProfileName.
            type: str
            required: True
          profileName:
            description:
            - It is the service provider's profileName.
            - Required for state create.
            type: str
          wanProvider:
            description:
            - It is the service provider's wanProvider.
            - Required for state create.
            type: str


  sp_profile_name:
    description:
    - Sp profile name.
    - Required for state delete.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.service_provider
# Reference by Internet resource
- name: ServiceProvider reference
  description: Complete reference of the ServiceProvider object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ServiceProvider reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_service_provider_details
  cisco.dnac.service_provider:
    state: query  # required
  register: query_result

- name: create_sp_profile
  cisco.dnac.service_provider:
    state: create  # required
    settings:  # required
      qos:
      - profileName: SomeValue  # string, required
        model: SomeValue  # string, required
        wanProvider: SomeValue  # string, required

- name: update_sp_profile
  cisco.dnac.service_provider:
    state: update  # required
    settings:  # required
      qos:
      - oldProfileName: SomeValue  # string, required
        profileName: SomeValue  # string
        model: SomeValue  # string
        wanProvider: SomeValue  # string

- name: delete_sp_profile
  cisco.dnac.service_provider:
    state: delete  # required
    sp_profile_name: SomeValue  # string, required

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

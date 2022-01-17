#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: app_policy_queuing_profile
short_description: Resource module for App Policy Queuing Profile
description:
- Manage operations create, update and delete of the resource App Policy Queuing Profile.
- Update existing custom application queuing profile.
- Create new custom application queuing profile.
- Delete existing custom application policy queuing profile by id.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Id of custom queuing profile to delete.
    type: str
  payload:
    description: App Policy Queuing Profile's payload.
    suboptions:
      clause:
        description: App Policy Queuing Profile's clause.
        suboptions:
          instanceId:
            description: Instance id.
            type: int
          interfaceSpeedBandwidthClauses:
            description: App Policy Queuing Profile's interfaceSpeedBandwidthClauses.
            suboptions:
              instanceId:
                description: Instance id.
                type: int
              interfaceSpeed:
                description: Interface speed.
                type: str
              tcBandwidthSettings:
                description: App Policy Queuing Profile's tcBandwidthSettings.
                suboptions:
                  bandwidthPercentage:
                    description: Bandwidth percentage.
                    type: int
                  instanceId:
                    description: Instance id.
                    type: int
                  trafficClass:
                    description: Traffic Class.
                    type: str
                type: list
            type: list
          isCommonBetweenAllInterfaceSpeeds:
            description: Is common between all interface speeds.
            type: bool
          tcDscpSettings:
            description: App Policy Queuing Profile's tcDscpSettings.
            suboptions:
              dscp:
                description: Dscp value.
                type: str
              instanceId:
                description: Instance id.
                type: int
              trafficClass:
                description: Traffic Class.
                type: str
            type: list
          type:
            description: Type.
            type: str
        type: list
      description:
        description: Free test description.
        type: str
      id:
        description: Id of Queueing profile.
        type: str
      name:
        description: Queueing profile name.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5

# Reference to SDK documentation of current version
- name: SDK function create_application_policy_queuing_profile used
  description: SDK function create_application_policy_queuing_profile used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    application_policy.ApplicationPolicy.create_application_policy_queuing_profile

- name: SDK function update_application_policy_queuing_profile used
  description: SDK function update_application_policy_queuing_profile used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    application_policy.ApplicationPolicy.update_application_policy_queuing_profile

- name: SDK function delete_application_policy_queuing_profile used
  description: SDK function delete_application_policy_queuing_profile used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    application_policy.ApplicationPolicy.delete_application_policy_queuing_profile

notes:
  - Paths used are put /dna/intent/api/v1/app-policy-queuing-profile,
    post /dna/intent/api/v1/app-policy-queuing-profile,
    delete /dna/intent/api/v1/app-policy-queuing-profile/{id}
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.app_policy_queuing_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Create
  cisco.dnac.app_policy_queuing_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Delete by id
  cisco.dnac.app_policy_queuing_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
